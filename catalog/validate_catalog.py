#!/usr/bin/env python3
"""Validate a Fatal Twelve Japanese-first JSONL catalog.

This validator has no third-party dependencies.  When source inputs are given it
rebuilds the catalog in memory and compares identity-bearing fields, making the
check substantially stronger than validating JSON shape alone.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Sequence

import build_catalog as builder


FORBIDDEN_REFERENCE_KEYS = {
    "english_text",
    "english_prose",
    "reference_text",
    "reference_translation",
    "new_text",
}
ENGLISH_SFX_RE = re.compile(
    r"(?i)(?:\bba[- ]?dump\b|\bclunk\b|\bwhoosh\b|\btch\b|\bheh\b|\bwaugh\b)"
)
KANA_RE = re.compile(r"[\u3040-\u30ff]")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_no}: record must be an object")
            records.append(value)
    return records


def walk_keys(value: Any, path: str = "$") -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            found.append((f"{path}.{key}", key))
            found.extend(walk_keys(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(walk_keys(child, f"{path}[{index}]"))
    return found


def token_multiset_for_target(text: str) -> dict[str, int]:
    # Target text has no source literal coordinate space, so semantic protected
    # tokens are extracted with a synthetic literal.
    literal = json.dumps(text, ensure_ascii=False)
    return builder.hard_token_multiset(builder.protected_tokens(text, literal))


def validate_shape(records: list[dict[str, Any]], errors: list[str], warnings: list[str], require_translated: bool) -> None:
    stable_ids: set[str] = set()
    translation_ids: set[str] = set()
    expected_index = 1

    for record in records:
        sid = record.get("stable_id", "<missing>")
        prefix = f"{sid}: "
        for key in (
            "schema_version",
            "stable_id",
            "command_index",
            "lane",
            "source",
            "localization",
            "alignment",
            "protected_tokens",
            "protected_token_multiset",
            "english_alignment",
            "translation",
        ):
            if key not in record:
                errors.append(prefix + f"missing required field {key}")

        if record.get("schema_version") != builder.SCHEMA_VERSION:
            errors.append(prefix + "schema_version mismatch")
        if sid in stable_ids:
            errors.append(prefix + "duplicate stable_id")
        stable_ids.add(sid)
        if record.get("command_index") != expected_index:
            errors.append(prefix + f"command_index should be {expected_index}")
        expected_index += 1

        for key_path, key in walk_keys(record):
            if key in FORBIDDEN_REFERENCE_KEYS:
                errors.append(prefix + f"forbidden English-prose field at {key_path}")

        source = record.get("source", {})
        text_ja = source.get("text_ja")
        if not isinstance(text_ja, str) or not text_ja:
            errors.append(prefix + "source.text_ja must be nonempty")
            continue
        if source.get("language") != "ja":
            errors.append(prefix + "source language is not ja")
        if source.get("text_sha256") != builder.sha256_text(text_ja):
            errors.append(prefix + "source text hash mismatch")

        group_code = source.get("group_code")
        if not isinstance(group_code, list) or not all(isinstance(x, str) for x in group_code):
            errors.append(prefix + "source.group_code must be a string list")
        else:
            group_blob = "".join(code + "\r\n" for code in group_code)
            if source.get("group_sha256") != builder.sha256_text(group_blob):
                errors.append(prefix + "source group hash mismatch")
            digest = source.get("renpy_digest")
            if digest is not None:
                actual = hashlib.md5(group_blob.encode("utf-8")).hexdigest()[:8]
                if digest != actual:
                    errors.append(prefix + "Ren'Py digest mismatch")

        expected_tokens = builder.protected_tokens(text_ja, _source_literal(record))
        if record.get("protected_tokens") != expected_tokens:
            errors.append(prefix + "protected token extraction mismatch")
        expected_multiset = builder.hard_token_multiset(expected_tokens)
        if record.get("protected_token_multiset") != expected_multiset:
            errors.append(prefix + "protected token multiset mismatch")

        localization = record.get("localization", {})
        tid = localization.get("translation_id")
        menu_key = localization.get("menu_key")
        expected_sid = builder.make_stable_id(source.get("script", ""), tid, menu_key)
        if sid != expected_sid:
            errors.append(prefix + "stable_id does not follow the declared identity rule")
        if tid:
            if tid in translation_ids:
                errors.append(prefix + f"duplicate translation_id {tid}")
            translation_ids.add(tid)

        alignment = record.get("english_alignment", {})
        if alignment.get("prose_imported") is not False:
            errors.append(prefix + "English alignment must declare prose_imported=false")
        if set(alignment) - {"mode", "key_present", "prose_imported"}:
            warnings.append(prefix + "unexpected field in English alignment")

        evidence = record.get("alignment", {})
        if evidence.get("sequence_alignment_used") is not False:
            errors.append(prefix + "sequence alignment is forbidden")
        if evidence.get("reference_prose_used") is not False:
            errors.append(prefix + "reference prose use is forbidden")
        if evidence.get("confidence") not in {"exact", "unmatched-reference"}:
            errors.append(prefix + "invalid alignment confidence")
        expected_alignment_evidence = {
            "computed_translation_id": tid,
            "renpy_digest": source.get("renpy_digest"),
            "source_group_sha256": source.get("group_sha256"),
            "source_text_sha256": source.get("text_sha256"),
            "reference_key_present": alignment.get("key_present"),
        }
        if evidence.get("evidence") != expected_alignment_evidence:
            errors.append(prefix + "alignment evidence does not match source identity")

        voice = record.get("voice_call")
        if voice is not None:
            if voice.get("statement") not in group_code:
                errors.append(prefix + "voice statement is absent from source group_code")
            if voice.get("function") == "get_voice_filename":
                parsed = builder.parse_voice(voice["statement"], voice["line"])
                if parsed != voice:
                    errors.append(prefix + "voice metadata does not reproduce from statement")

        translation = record.get("translation", {})
        ko = translation.get("text_ko")
        status = translation.get("status")
        if require_translated and (not isinstance(ko, str) or not ko.strip()):
            errors.append(prefix + "Korean translation required but empty")
        if ko is not None:
            if not isinstance(ko, str) or not ko.strip():
                errors.append(prefix + "non-null Korean translation must be nonempty")
            else:
                actual_tokens = token_multiset_for_target(ko)
                if actual_tokens != expected_multiset:
                    errors.append(prefix + "Korean translation mutated protected tokens")
                if KANA_RE.search(ko):
                    warnings.append(prefix + "Korean translation contains kana; manual residue review required")
                suspects = sorted(set(match.group(0) for match in ENGLISH_SFX_RE.finditer(ko)))
                if suspects:
                    warnings.append(prefix + f"possible English-SFX contamination: {suspects}")
        elif status not in {"untranslated", "deferred"}:
            errors.append(prefix + "null Korean text must have untranslated/deferred status")

        context = record.get("context", {})
        for direction in ("previous", "next"):
            for neighbor in context.get(direction, []):
                neighbor_sid = neighbor.get("stable_id")
                if not isinstance(neighbor_sid, str):
                    errors.append(prefix + f"invalid {direction} context stable_id")


def _source_literal(record: dict[str, Any]) -> str:
    code = record.get("source", {}).get("statement_code", "")
    split = builder.split_quoted_statement(code)
    if split is None:
        return json.dumps(record.get("source", {}).get("text_ja", ""), ensure_ascii=False)
    return str(split["literal"])


def validate_context(records: list[dict[str, Any]], errors: list[str]) -> None:
    by_id = {record["stable_id"]: record for record in records if "stable_id" in record}
    for record in records:
        sid = record.get("stable_id", "<missing>")
        for direction in ("previous", "next"):
            for neighbor in record.get("context", {}).get(direction, []):
                target = by_id.get(neighbor.get("stable_id"))
                if target is None:
                    errors.append(f"{sid}: context points to unknown stable_id {neighbor.get('stable_id')}")
                    continue
                expected = builder.compact_context(target)
                if neighbor != expected:
                    errors.append(f"{sid}: stale or mutated {direction} context for {neighbor.get('stable_id')}")


def compare_rebuild(
    records: list[dict[str, Any]],
    source_rpy: Path,
    script_path: str,
    characters_rpy: Path | None,
    reference_rpy: Path | None,
    reference_language: str,
    context_radius: int,
    errors: list[str],
) -> dict[str, Any]:
    source_text, _ = builder.decode_utf8_strict(source_rpy)
    characters, _ = builder.parse_character_definitions(characters_rpy)
    reference = builder.parse_reference_index(reference_rpy, reference_language)
    rebuilt, diagnostics = builder.build_records(
        source_text,
        script_path=script_path,
        characters=characters,
        reference=reference,
        context_radius=context_radius,
    )
    if len(records) != len(rebuilt):
        errors.append(f"rebuild record count mismatch: catalog={len(records)} source={len(rebuilt)}")
        return diagnostics

    identity_fields = (
        "schema_version",
        "stable_id",
        "command_index",
        "lane",
        "visibility",
        "source",
        "localization",
        "alignment",
        "speaker",
        "voice_call",
        "runtime_context",
        "prelude_commands",
        "menu_context",
        "protected_tokens",
        "protected_token_multiset",
        "layout",
        "english_alignment",
        "context",
    )
    for actual, expected in zip(records, rebuilt):
        for field in identity_fields:
            if actual.get(field) != expected.get(field):
                errors.append(
                    f"{actual.get('stable_id', '<missing>')}: source rebuild mismatch in {field}"
                )
    return diagnostics


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("--meta", type=Path)
    parser.add_argument("--source-rpy", type=Path)
    parser.add_argument("--script-path")
    parser.add_argument("--characters-rpy", type=Path)
    parser.add_argument("--reference-rpy", type=Path)
    parser.add_argument("--reference-language", default="english")
    parser.add_argument("--context-radius", type=int, default=2)
    parser.add_argument("--require-translated", action="store_true")
    parser.add_argument("--output", type=Path)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    records = read_jsonl(args.catalog)
    errors: list[str] = []
    warnings: list[str] = []
    validate_shape(records, errors, warnings, args.require_translated)
    validate_context(records, errors)

    rebuild_diagnostics = None
    if args.source_rpy:
        if not args.script_path:
            raise SystemExit("--script-path is required with --source-rpy")
        rebuild_diagnostics = compare_rebuild(
            records,
            args.source_rpy,
            args.script_path.replace("\\", "/"),
            args.characters_rpy,
            args.reference_rpy,
            args.reference_language,
            args.context_radius,
            errors,
        )

    meta_checks: dict[str, Any] = {}
    if args.meta:
        meta = json.loads(args.meta.read_text(encoding="utf-8"))
        catalog_hash = builder.file_info(args.catalog)
        expected = meta.get("catalog", {})
        if expected.get("sha256") != catalog_hash["sha256"]:
            errors.append("metadata catalog SHA-256 mismatch")
        if expected.get("size") != catalog_hash["size"]:
            errors.append("metadata catalog size mismatch")
        stats = builder.summarize_records(records)
        if meta.get("statistics") != stats:
            errors.append("metadata statistics mismatch")
        if meta.get("policy", {}).get("reference_prose_stored") is not False:
            errors.append("metadata does not lock reference_prose_stored=false")
        if rebuild_diagnostics is not None and meta.get("diagnostics") != rebuild_diagnostics:
            errors.append("metadata diagnostics differ from source rebuild")
        meta_checks = {"catalog_hash": catalog_hash, "statistics": stats}

    report = {
        "schema_version": builder.SCHEMA_VERSION,
        "validated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "catalog": str(args.catalog.resolve()),
        "records": len(records),
        "require_translated": args.require_translated,
        "source_rebuild_performed": bool(args.source_rpy),
        "metadata_checked": bool(args.meta),
        "errors": errors,
        "warnings": warnings,
        "passed": not errors,
        "meta_checks": meta_checks,
    }
    output = args.output or args.catalog.with_suffix(".validation.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

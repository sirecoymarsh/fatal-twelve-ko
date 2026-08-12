#!/usr/bin/env python3
"""Build per-script master drafts from exact catalogs and immutable draft packets.

This tool performs structural validation only.  It never rewrites or reviews a
Korean draft string.  Catalog metadata is authoritative; packet draft strings
are copied byte-for-value at the decoded JSON string level.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "fatal-twelve-master-draft-v1"
REPORT_SCHEMA_VERSION = "fatal-twelve-master-build-report-v1"
NUMBER_RE = re.compile(r"(?<![0-9])(?:[0-9]+(?:\.[0-9]+)?)(?![0-9])")
VARIABLE_RE = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")
MISSING = object()


class ManifestError(ValueError):
    """The explicit manifest is invalid."""


@dataclass(frozen=True)
class Candidate:
    script_key: str
    packet_id: str
    packet_path: Path
    packet_path_key: str
    packet_sha256: str
    packet_schema: str
    packet_entry_index: int
    raw: dict[str, Any]
    stable_id: str
    sequence: int
    source_jp: str
    translation_id: str | None
    translation_id_present: bool
    menu_key: str | None
    menu_key_present: bool
    protected_tokens: list[dict[str, Any]]
    draft_ko: str
    source_file: str | None
    source_line: int | None

    @property
    def draft_ko_sha256(self) -> str:
        return text_sha256(self.draft_ko)


def text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def expand_string(value: str, variables: dict[str, str]) -> str:
    result = value
    for _ in range(len(variables) + 2):
        updated = VARIABLE_RE.sub(lambda match: variables.get(match.group(1), match.group(0)), result)
        if updated == result:
            break
        result = updated
    unresolved = VARIABLE_RE.findall(result)
    if unresolved:
        raise ManifestError(f"unresolved variables {unresolved!r} in {value!r}")
    return result


def expand_path(value: str, variables: dict[str, str]) -> Path:
    return Path(expand_string(value, variables))


def path_key(path: Path) -> str:
    return os.path.normcase(os.path.abspath(str(path))).replace("/", "\\")


def source_file_key(value: str) -> str:
    return value.replace("\\", "/")


def nested(mapping: dict[str, Any], *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return MISSING
        current = current[key]
    return current


def first_present(mapping: dict[str, Any], paths: Iterable[tuple[str, ...]]) -> Any:
    for parts in paths:
        value = nested(mapping, *parts)
        if value is not MISSING:
            return value
    return MISSING


def load_catalog(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"{path}:{line_number}: catalog record must be an object")
            records.append(record)
    return records


def extract_packet_entries(document: Any, path: Path) -> tuple[list[dict[str, Any]], str]:
    if isinstance(document, list):
        entries = document
        schema = "root-array"
    elif isinstance(document, dict):
        schema = str(document.get("schema_version") or document.get("schema") or "unversioned-object")
        entries = MISSING
        for key in ("entries", "records", "items", "translations"):
            if isinstance(document.get(key), list):
                entries = document[key]
                schema = f"{schema}:{key}"
                break
        if entries is MISSING:
            raise ValueError(f"{path}: no supported entry array (entries/records/items/translations)")
    else:
        raise ValueError(f"{path}: packet root must be an object or array")
    if not all(isinstance(entry, dict) for entry in entries):
        raise ValueError(f"{path}: every packet entry must be an object")
    return entries, schema


def normalize_candidate(
    *,
    script_key: str,
    packet_id: str,
    packet_path: Path,
    packet_sha: str,
    packet_schema: str,
    entry_index: int,
    raw: dict[str, Any],
) -> Candidate:
    stable_id = first_present(raw, (("catalog_stable_id",), ("stable_id",), ("catalog", "stable_id")))
    sequence = first_present(
        raw,
        (("command_index",), ("catalog_command_index",), ("sequence",), ("catalog", "command_index")),
    )
    source_jp = first_present(
        raw,
        (("source_jp",), ("source", "text_ja"), ("source_text_ja",), ("source_text",)),
    )
    translation_id = first_present(
        raw,
        (("translation_id",), ("localization", "translation_id"), ("catalog", "translation_id")),
    )
    menu_key = first_present(raw, (("menu_key",), ("localization", "menu_key"), ("catalog", "menu_key")))
    protected_tokens = first_present(raw, (("protected_tokens",), ("source", "protected_tokens")))
    draft_ko = first_present(
        raw,
        (
            ("draft_ko",),
            ("translation_ko",),
            ("target_ko",),
            ("text_ko",),
            ("translation", "text_ko"),
            ("target", "text_ko"),
        ),
    )
    source_file = first_present(raw, (("source_file",), ("source", "script"), ("catalog", "source_file")))
    source_line = first_present(raw, (("source_line",), ("source", "line"), ("catalog", "source_line")))

    translation_id_present = translation_id is not MISSING
    menu_key_present = menu_key is not MISSING
    if not translation_id_present:
        translation_id = None
    if not menu_key_present:
        menu_key = None

    required = {
        "stable_id": stable_id,
        "sequence": sequence,
        "source_jp": source_jp,
        "protected_tokens": protected_tokens,
        "draft_ko": draft_ko,
    }
    missing = [key for key, value in required.items() if value is MISSING]
    if missing:
        raise ValueError(f"missing normalized fields: {', '.join(missing)}")
    if not isinstance(stable_id, str) or not stable_id:
        raise ValueError("stable_id must be a nonempty string")
    if isinstance(sequence, bool):
        raise ValueError("sequence must be an integer")
    try:
        sequence = int(sequence)
    except (TypeError, ValueError) as exc:
        raise ValueError("sequence must be an integer") from exc
    if not isinstance(source_jp, str):
        raise ValueError("source_jp must be a string")
    if translation_id is not None and not isinstance(translation_id, str):
        raise ValueError("translation_id must be a string or null")
    if menu_key is not None and not isinstance(menu_key, str):
        raise ValueError("menu_key must be a string or null")
    if not isinstance(protected_tokens, list) or not all(isinstance(token, dict) for token in protected_tokens):
        raise ValueError("protected_tokens must be an array of objects")
    if not isinstance(draft_ko, str) or draft_ko == "":
        raise ValueError("draft_ko must be a nonempty string")
    if source_file is MISSING:
        source_file = None
    elif not isinstance(source_file, str):
        raise ValueError("source_file must be a string when present")
    if source_line is MISSING or source_line is None:
        source_line = None
    else:
        try:
            source_line = int(source_line)
        except (TypeError, ValueError) as exc:
            raise ValueError("source_line must be an integer when present") from exc

    return Candidate(
        script_key=script_key,
        packet_id=packet_id,
        packet_path=packet_path,
        packet_path_key=path_key(packet_path),
        packet_sha256=packet_sha,
        packet_schema=packet_schema,
        packet_entry_index=entry_index,
        raw=raw,
        stable_id=stable_id,
        sequence=sequence,
        source_jp=source_jp,
        translation_id=translation_id,
        translation_id_present=translation_id_present,
        menu_key=menu_key,
        menu_key_present=menu_key_present,
        protected_tokens=protected_tokens,
        draft_ko=draft_ko,
        source_file=source_file,
        source_line=source_line,
    )


def catalog_projection(record: dict[str, Any]) -> dict[str, Any]:
    source = record.get("source") or {}
    localization = record.get("localization") or {}
    return {
        "stable_id": record.get("stable_id"),
        "sequence": record.get("command_index"),
        "source_jp": source.get("text_ja"),
        "source_file": source.get("script"),
        "source_line": source.get("line"),
        "source_text_sha256": source.get("text_sha256"),
        "translation_id": localization.get("translation_id"),
        "menu_key": localization.get("menu_key"),
        "protected_tokens": record.get("protected_tokens"),
    }


def compare_candidate(candidate: Candidate, catalog_record: dict[str, Any]) -> list[dict[str, Any]]:
    expected = catalog_projection(catalog_record)
    errors: list[dict[str, Any]] = []

    def mismatch(field: str, actual: Any, expected_value: Any) -> None:
        errors.append(
            {
                "kind": f"{field}_mismatch",
                "script_key": candidate.script_key,
                "stable_id": candidate.stable_id,
                "packet_id": candidate.packet_id,
                "packet_path": str(candidate.packet_path),
                "packet_entry_index": candidate.packet_entry_index,
                "actual": actual,
                "expected": expected_value,
            }
        )

    if candidate.sequence != expected["sequence"]:
        mismatch("sequence", candidate.sequence, expected["sequence"])
    if candidate.source_jp != expected["source_jp"]:
        mismatch("source_jp", candidate.source_jp, expected["source_jp"])
    if (not candidate.translation_id_present and expected["translation_id"] is not None) or (
        candidate.translation_id_present and candidate.translation_id != expected["translation_id"]
    ):
        mismatch("translation_id", candidate.translation_id, expected["translation_id"])
    if (not candidate.menu_key_present and expected["menu_key"] is not None) or (
        candidate.menu_key_present and candidate.menu_key != expected["menu_key"]
    ):
        mismatch("menu_key", candidate.menu_key, expected["menu_key"])
    if canonical_json(candidate.protected_tokens) != canonical_json(expected["protected_tokens"]):
        mismatch("protected_tokens", candidate.protected_tokens, expected["protected_tokens"])
    if candidate.source_file is not None and source_file_key(candidate.source_file) != source_file_key(expected["source_file"]):
        mismatch("source_file", candidate.source_file, expected["source_file"])
    if candidate.source_line is not None and candidate.source_line != expected["source_line"]:
        mismatch("source_line", candidate.source_line, expected["source_line"])
    if text_sha256(candidate.source_jp) != expected["source_text_sha256"]:
        mismatch("source_text_sha256", text_sha256(candidate.source_jp), expected["source_text_sha256"])

    packet_source_hash = first_present(candidate.raw, (("source_text_sha256",), ("source", "text_sha256")))
    if packet_source_hash is not MISSING and packet_source_hash != expected["source_text_sha256"]:
        mismatch("packet_source_text_sha256", packet_source_hash, expected["source_text_sha256"])

    if candidate.raw.get("english_reference_used") is True:
        mismatch("english_reference_used", True, False)
    if candidate.raw.get("external_translation_api_used") is True:
        mismatch("external_translation_api_used", True, False)

    for message in hard_token_errors(catalog_record, candidate.draft_ko):
        errors.append(
            {
                "kind": "hard_token_mismatch",
                "script_key": candidate.script_key,
                "stable_id": candidate.stable_id,
                "sequence": candidate.sequence,
                "packet_id": candidate.packet_id,
                "packet_path": str(candidate.packet_path),
                "packet_entry_index": candidate.packet_entry_index,
                "message": message,
            }
        )
    return errors


def hard_token_errors(record: dict[str, Any], target: str) -> list[str]:
    tokens = [token for token in record.get("protected_tokens", []) if token.get("severity") == "hard"]
    errors: list[str] = []

    tags = collections.Counter(token.get("value") for token in tokens if token.get("kind") == "renpy_text_tag")
    for value, count in tags.items():
        if not isinstance(value, str):
            errors.append(f"invalid RenPy tag token {value!r}")
        elif target.count(value) != count:
            errors.append(f"RenPy tag {value!r}: expected {count}, got {target.count(value)}")

    number_values = [token.get("value") for token in tokens if token.get("kind") == "number"]
    arabic: collections.Counter[str] = collections.Counter()
    roman: collections.Counter[str] = collections.Counter()
    for value in number_values:
        if not isinstance(value, str):
            errors.append(f"invalid number token {value!r}")
            continue
        normalized = unicodedata.normalize("NFKC", value)
        if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", normalized):
            arabic[normalized] += 1
        else:
            roman[value] += 1
    if arabic:
        target_numbers = collections.Counter(NUMBER_RE.findall(unicodedata.normalize("NFKC", target)))
        if arabic != target_numbers:
            errors.append(f"Arabic numbers: expected {dict(arabic)}, got {dict(target_numbers)}")
    for value, count in roman.items():
        if target.count(value) != count:
            errors.append(f"Roman numeral {value!r}: expected {count}, got {target.count(value)}")

    literal_escapes = collections.Counter(
        token.get("value") for token in tokens if token.get("kind") == "literal_escape"
    )
    decoded_escapes = {"\\n": "\n", "\\r": "\r", "\\t": "\t", "\\\\": "\\"}
    for value, count in literal_escapes.items():
        if not isinstance(value, str):
            errors.append(f"invalid literal escape token {value!r}")
            continue
        target_value = decoded_escapes.get(value, value)
        if target.count(target_value) != count:
            errors.append(f"literal escape {value!r}: expected {count}, got {target.count(target_value)}")

    known_kinds = {"renpy_text_tag", "number", "literal_escape"}
    other_tokens = collections.Counter(
        (token.get("kind"), token.get("value")) for token in tokens if token.get("kind") not in known_kinds
    )
    for (kind, value), count in other_tokens.items():
        if not isinstance(value, str):
            errors.append(f"invalid {kind!r} token {value!r}")
        elif target.count(value) != count:
            errors.append(f"{kind} token {value!r}: expected {count}, got {target.count(value)}")
    return errors


def candidate_report(candidate: Candidate, *, selected: bool) -> dict[str, Any]:
    return {
        "selected": selected,
        "packet_id": candidate.packet_id,
        "packet_path": str(candidate.packet_path),
        "packet_sha256": candidate.packet_sha256,
        "packet_entry_index": candidate.packet_entry_index,
        "sequence": candidate.sequence,
        "draft_ko": candidate.draft_ko,
        "draft_ko_sha256": candidate.draft_ko_sha256,
    }


def build_master_entry(
    record: dict[str, Any], candidate: Candidate, hard_token_findings: list[str]
) -> dict[str, Any]:
    source = record["source"]
    localization = record["localization"]
    speaker = record.get("speaker")
    return {
        "stable_id": record["stable_id"],
        "sequence": record["command_index"],
        "command_index": record["command_index"],
        "source_file": source["script"],
        "source_line": source["line"],
        "source_label": source.get("label"),
        "lane": record.get("lane"),
        "speaker": speaker.get("code") if isinstance(speaker, dict) else None,
        "source_jp": source["text_ja"],
        "source_text_sha256": source["text_sha256"],
        "source_group_sha256": source.get("group_sha256"),
        "source_statement_code": source.get("statement_code"),
        "source_group_code": source.get("group_code"),
        "translation_id": localization.get("translation_id"),
        "id_origin": localization.get("id_origin"),
        "menu_key": localization.get("menu_key"),
        "voice_call": record.get("voice_call"),
        "protected_tokens": record.get("protected_tokens", []),
        "draft_ko": candidate.draft_ko,
        "draft_ko_sha256": candidate.draft_ko_sha256,
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "status": candidate.raw.get("status", "first_draft_unreviewed"),
        "qa": candidate.raw.get("qa", "deferred_until_full_first_draft"),
        "identity_validation": "passed",
        "hard_token_validation": {
            "passed": not hard_token_findings,
            "findings": hard_token_findings,
        },
        "structural_validation": "passed" if not hard_token_findings else "hard_token_findings_reported",
        "provenance": {
            "packet_id": candidate.packet_id,
            "packet_path": str(candidate.packet_path),
            "packet_sha256": candidate.packet_sha256,
            "packet_schema": candidate.packet_schema,
            "packet_entry_index": candidate.packet_entry_index,
            "translation_text_copied_verbatim": True,
        },
    }


def validate_catalog(
    script: dict[str, Any], records: list[dict[str, Any]], catalog_path: Path
) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    expected_count = script["expected_records"]
    if len(records) != expected_count:
        errors.append(
            {
                "kind": "catalog_record_count_mismatch",
                "script_key": script["script_key"],
                "catalog": str(catalog_path),
                "actual": len(records),
                "expected": expected_count,
            }
        )
    sequences = [record.get("command_index") for record in records]
    if sequences != list(range(1, len(records) + 1)):
        errors.append(
            {
                "kind": "catalog_sequence_not_contiguous",
                "script_key": script["script_key"],
                "catalog": str(catalog_path),
            }
        )
    stable_ids = [record.get("stable_id") for record in records]
    duplicate_ids = [stable_id for stable_id, count in collections.Counter(stable_ids).items() if count > 1]
    if duplicate_ids:
        errors.append(
            {
                "kind": "catalog_duplicate_stable_id",
                "script_key": script["script_key"],
                "stable_ids": duplicate_ids,
            }
        )
    expected_source = source_file_key(script["source_file"])
    wrong_sources = sorted(
        {
            (record.get("source") or {}).get("script")
            for record in records
            if source_file_key((record.get("source") or {}).get("script", "")) != expected_source
        }
    )
    if wrong_sources:
        errors.append(
            {
                "kind": "catalog_source_file_mismatch",
                "script_key": script["script_key"],
                "actual": wrong_sources,
                "expected": script["source_file"],
            }
        )
    for record in records:
        projection = catalog_projection(record)
        if not isinstance(projection["stable_id"], str) or not projection["stable_id"]:
            errors.append({"kind": "catalog_invalid_stable_id", "script_key": script["script_key"]})
        if not isinstance(projection["source_jp"], str):
            errors.append(
                {
                    "kind": "catalog_invalid_source_jp",
                    "script_key": script["script_key"],
                    "stable_id": projection["stable_id"],
                }
            )
        elif text_sha256(projection["source_jp"]) != projection["source_text_sha256"]:
            errors.append(
                {
                    "kind": "catalog_source_hash_mismatch",
                    "script_key": script["script_key"],
                    "stable_id": projection["stable_id"],
                }
            )
        if not isinstance(projection["protected_tokens"], list):
            errors.append(
                {
                    "kind": "catalog_invalid_protected_tokens",
                    "script_key": script["script_key"],
                    "stable_id": projection["stable_id"],
                }
            )
    return errors


def validate_packet_expectation(
    *, script_key: str, packet: dict[str, Any], candidates: list[Candidate]
) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    expected_occurrences = packet.get("expected_occurrences")
    if expected_occurrences is not None and len(candidates) != expected_occurrences:
        errors.append(
            {
                "kind": "packet_occurrence_count_mismatch",
                "script_key": script_key,
                "packet_id": packet["id"],
                "actual": len(candidates),
                "expected": expected_occurrences,
            }
        )
    sequences = sorted(candidate.sequence for candidate in candidates)
    if "expected_sequences" in packet and sequences != sorted(packet["expected_sequences"]):
        errors.append(
            {
                "kind": "packet_sequence_set_mismatch",
                "script_key": script_key,
                "packet_id": packet["id"],
                "actual": sequences,
                "expected": sorted(packet["expected_sequences"]),
            }
        )
    if "expected_command_index" in packet and candidates:
        first, last = packet["expected_command_index"]
        if sequences[0] != first or sequences[-1] != last:
            errors.append(
                {
                    "kind": "packet_command_range_mismatch",
                    "script_key": script_key,
                    "packet_id": packet["id"],
                    "actual": [sequences[0], sequences[-1]],
                    "expected": [first, last],
                }
            )
        if not packet.get("allow_command_gaps") and sequences != list(range(first, last + 1)):
            errors.append(
                {
                    "kind": "packet_command_range_not_contiguous",
                    "script_key": script_key,
                    "packet_id": packet["id"],
                    "expected": [first, last],
                }
            )
    return errors


def choose_duplicate(
    *,
    stable_id: str,
    candidates: list[Candidate],
    policies: dict[str, dict[str, Any]],
    variables: dict[str, str],
) -> tuple[Candidate | None, dict[str, Any], list[dict[str, Any]]]:
    errors: list[dict[str, Any]] = []
    policy = policies.get(stable_id)
    if policy is None:
        errors.append(
            {
                "kind": "unlisted_duplicate",
                "script_key": candidates[0].script_key,
                "stable_id": stable_id,
                "candidate_count": len(candidates),
            }
        )
        selected = None
    else:
        selected_path_value = policy.get("selected_packet")
        selected_hash = policy.get("selected_draft_ko_sha256")
        if not isinstance(selected_path_value, str) or not isinstance(selected_hash, str):
            errors.append(
                {
                    "kind": "invalid_conflict_policy",
                    "script_key": candidates[0].script_key,
                    "stable_id": stable_id,
                }
            )
            selected = None
        else:
            selected_path = path_key(expand_path(selected_path_value, variables))
            matches = [
                candidate
                for candidate in candidates
                if candidate.packet_path_key == selected_path and candidate.draft_ko_sha256 == selected_hash
            ]
            if len(matches) != 1:
                errors.append(
                    {
                        "kind": "conflict_policy_selection_mismatch",
                        "script_key": candidates[0].script_key,
                        "stable_id": stable_id,
                        "matching_candidates": len(matches),
                        "selected_packet": str(expand_path(selected_path_value, variables)),
                        "selected_draft_ko_sha256": selected_hash,
                    }
                )
                selected = None
            else:
                selected = matches[0]
    report = {
        "script_key": candidates[0].script_key,
        "stable_id": stable_id,
        "sequence": candidates[0].sequence,
        "source_jp": candidates[0].source_jp,
        "policy": policy,
        "resolved": selected is not None,
        "candidates": [candidate_report(candidate, selected=candidate is selected) for candidate in candidates],
    }
    return selected, report, errors


def expected_pending_sequences(packet: dict[str, Any]) -> set[int]:
    if "expected_sequences" in packet:
        return {int(value) for value in packet["expected_sequences"]}
    if "expected_command_index" in packet:
        first, last = packet["expected_command_index"]
        return set(range(int(first), int(last) + 1))
    return set()


def process_script(
    *,
    script: dict[str, Any],
    variables: dict[str, str],
    conflict_policies: dict[str, dict[str, Any]],
    masters_dir: Path,
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], Path]:
    script_key = script["script_key"]
    catalog_path = expand_path(script["catalog"], variables)
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    conflicts: list[dict[str, Any]] = []

    if not catalog_path.is_file():
        raise FileNotFoundError(f"catalog does not exist: {catalog_path}")
    records = load_catalog(catalog_path)
    errors.extend(validate_catalog(script, records, catalog_path))
    catalog_by_id = {record.get("stable_id"): record for record in records}
    catalog_sequence_by_id = {record.get("stable_id"): record.get("command_index") for record in records}

    candidates_by_id: dict[str, list[Candidate]] = collections.defaultdict(list)
    hard_token_findings_by_candidate: dict[tuple[str, int], list[str]] = {}
    ready_packet_reports: list[dict[str, Any]] = []
    pending_packet_reports: list[dict[str, Any]] = []
    pending_sequences: set[int] = set()
    packet_occurrences = 0

    packet_ids: set[str] = set()
    for packet in script["packets"]:
        packet_id = packet.get("id")
        if not isinstance(packet_id, str) or not packet_id:
            raise ManifestError(f"{script_key}: packet id must be a nonempty string")
        if packet_id in packet_ids:
            raise ManifestError(f"{script_key}: duplicate packet id {packet_id}")
        packet_ids.add(packet_id)
        packet_path_value = packet.get("path")
        if packet_path_value is None:
            expected_sequences = expected_pending_sequences(packet)
            pending_sequences.update(expected_sequences)
            pending_packet_reports.append(
                {
                    "packet_id": packet_id,
                    "manifest_status": packet.get("status"),
                    "path": None,
                    "expected_occurrences": packet.get("expected_occurrences"),
                    "expected_command_index": packet.get("expected_command_index"),
                    "expected_sequences": packet.get("expected_sequences"),
                }
            )
            continue
        if not isinstance(packet_path_value, str):
            raise ManifestError(f"{script_key}/{packet_id}: path must be a string or null")
        packet_path = expand_path(packet_path_value, variables)
        if not packet_path.is_file():
            errors.append(
                {
                    "kind": "packet_file_missing",
                    "script_key": script_key,
                    "packet_id": packet_id,
                    "packet_path": str(packet_path),
                }
            )
            continue
        packet_sha = file_sha256(packet_path)
        try:
            raw_entries, packet_schema = extract_packet_entries(read_json(packet_path), packet_path)
        except Exception as exc:
            errors.append(
                {
                    "kind": "packet_load_error",
                    "script_key": script_key,
                    "packet_id": packet_id,
                    "packet_path": str(packet_path),
                    "message": str(exc),
                }
            )
            continue
        normalized: list[Candidate] = []
        for entry_index, raw in enumerate(raw_entries):
            try:
                candidate = normalize_candidate(
                    script_key=script_key,
                    packet_id=packet_id,
                    packet_path=packet_path,
                    packet_sha=packet_sha,
                    packet_schema=packet_schema,
                    entry_index=entry_index,
                    raw=raw,
                )
            except Exception as exc:
                errors.append(
                    {
                        "kind": "packet_entry_normalization_error",
                        "script_key": script_key,
                        "packet_id": packet_id,
                        "packet_path": str(packet_path),
                        "packet_entry_index": entry_index,
                        "message": str(exc),
                    }
                )
                continue
            normalized.append(candidate)
        errors.extend(validate_packet_expectation(script_key=script_key, packet=packet, candidates=normalized))
        packet_occurrences += len(normalized)
        ready_packet_reports.append(
            {
                "packet_id": packet_id,
                "manifest_status": packet.get("status"),
                "effective_status": "ready",
                "path": str(packet_path),
                "sha256": packet_sha,
                "schema": packet_schema,
                "occurrences": len(normalized),
                "expected_occurrences": packet.get("expected_occurrences"),
            }
        )
        for candidate in normalized:
            catalog_record = catalog_by_id.get(candidate.stable_id)
            if catalog_record is None:
                errors.append(
                    {
                        "kind": "unexpected_stable_id",
                        "script_key": script_key,
                        "stable_id": candidate.stable_id,
                        "sequence": candidate.sequence,
                        "packet_id": candidate.packet_id,
                        "packet_path": str(candidate.packet_path),
                        "packet_entry_index": candidate.packet_entry_index,
                    }
                )
                continue
            candidate_errors = compare_candidate(candidate, catalog_record)
            errors.extend(candidate_errors)
            blocking_errors = [error for error in candidate_errors if error["kind"] != "hard_token_mismatch"]
            token_findings = [error["message"] for error in candidate_errors if error["kind"] == "hard_token_mismatch"]
            if token_findings:
                hard_token_findings_by_candidate[(candidate.packet_path_key, candidate.packet_entry_index)] = token_findings
            if not blocking_errors:
                candidates_by_id[candidate.stable_id].append(candidate)

    selected: dict[str, Candidate] = {}
    duplicate_occurrences = 0
    for stable_id, candidates in candidates_by_id.items():
        if len(candidates) == 1:
            selected[stable_id] = candidates[0]
            continue
        duplicate_occurrences += len(candidates) - 1
        chosen, conflict_report, duplicate_errors = choose_duplicate(
            stable_id=stable_id,
            candidates=candidates,
            policies=conflict_policies,
            variables=variables,
        )
        conflicts.append(conflict_report)
        errors.extend(duplicate_errors)
        if chosen is not None:
            selected[stable_id] = chosen

    missing_ids = [record["stable_id"] for record in records if record["stable_id"] not in selected]
    missing_sequences = [catalog_sequence_by_id[stable_id] for stable_id in missing_ids]
    unexplained_missing = [sequence for sequence in missing_sequences if sequence not in pending_sequences]
    pending_not_missing = sorted(sequence for sequence in pending_sequences if sequence not in set(missing_sequences))
    if unexplained_missing:
        errors.append(
            {
                "kind": "unexplained_missing_records",
                "script_key": script_key,
                "count": len(unexplained_missing),
                "sequences": unexplained_missing,
            }
        )
    if pending_not_missing:
        errors.append(
            {
                "kind": "pending_placeholder_overlaps_selected_records",
                "script_key": script_key,
                "count": len(pending_not_missing),
                "sequences": pending_not_missing,
            }
        )

    for stable_id, policy in conflict_policies.items():
        if stable_id in catalog_by_id and stable_id not in {conflict["stable_id"] for conflict in conflicts}:
            warnings.append(
                {
                    "kind": "unused_conflict_policy",
                    "script_key": script_key,
                    "stable_id": stable_id,
                    "policy": policy,
                }
            )

    master_entries = [
        build_master_entry(
            record,
            selected[record["stable_id"]],
            hard_token_findings_by_candidate.get(
                (
                    selected[record["stable_id"]].packet_path_key,
                    selected[record["stable_id"]].packet_entry_index,
                ),
                [],
            ),
        )
        for record in records
        if record["stable_id"] in selected
    ]
    hard_token_failed_records = sum(not entry["hard_token_validation"]["passed"] for entry in master_entries)
    coverage = {
        "catalog_records": len(records),
        "packet_occurrences": packet_occurrences,
        "selected_unique_records": len(selected),
        "duplicate_extra_occurrences": duplicate_occurrences,
        "missing_records": len(missing_ids),
        "missing_sequences": missing_sequences,
        "missing_stable_ids": missing_ids,
        "pending_explained_missing_records": len(missing_sequences) - len(unexplained_missing),
        "unexplained_missing_records": len(unexplained_missing),
        "translation_ids": sum(entry["translation_id"] is not None for entry in master_entries),
        "menu_keys": sum(entry["menu_key"] is not None for entry in master_entries),
        "hard_token_failed_records": hard_token_failed_records,
    }
    structural_pass = not errors
    coverage_complete = not pending_packet_reports and not missing_ids and len(selected) == len(records)
    complete = coverage_complete
    master = {
        "schema_version": SCHEMA_VERSION,
        "script_key": script_key,
        "source_file": script["source_file"],
        "catalog": {
            "path": str(catalog_path),
            "sha256": file_sha256(catalog_path),
            "records": len(records),
        },
        "translation_text_policy": "immutable; copied verbatim from explicitly listed packets",
        "catalog_metadata_policy": "authoritative",
        "validation_scope": "structural only; no translation review or correction",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "structural_pass": structural_pass,
        "coverage_complete": coverage_complete,
        "complete": complete,
        "coverage": coverage,
        "ready_packets": ready_packet_reports,
        "pending_packets": pending_packet_reports,
        "resolved_conflict_stable_ids": [conflict["stable_id"] for conflict in conflicts if conflict["resolved"]],
        "entries": master_entries,
    }
    master_path = masters_dir / f"scenario_{script_key}.master.json"
    write_json(master_path, master)
    script_report = {
        "script_key": script_key,
        "source_file": script["source_file"],
        "catalog_path": str(catalog_path),
        "catalog_sha256": file_sha256(catalog_path),
        "master_path": str(master_path),
        "master_sha256": file_sha256(master_path),
        "structural_pass": structural_pass,
        "coverage_complete": coverage_complete,
        "complete": complete,
        "coverage": coverage,
        "ready_packets": ready_packet_reports,
        "pending_packets": pending_packet_reports,
        "conflict_count": len(conflicts),
        "errors": errors,
        "warnings": warnings,
    }
    return script_report, conflicts, errors, master_path


def validate_manifest(manifest: dict[str, Any]) -> None:
    if manifest.get("schema_version") != "fatal-twelve-master-packet-manifest-v1":
        raise ManifestError("unsupported or missing manifest schema_version")
    scripts = manifest.get("scripts")
    if not isinstance(scripts, list):
        raise ManifestError("scripts must be an array")
    expectations = manifest.get("catalog_expectations") or {}
    if len(scripts) != expectations.get("file_count"):
        raise ManifestError(
            f"manifest script count {len(scripts)} != expected {expectations.get('file_count')}"
        )
    total = sum(script.get("expected_records", 0) for script in scripts)
    if total != expectations.get("record_count"):
        raise ManifestError(
            f"manifest expected record total {total} != expected {expectations.get('record_count')}"
        )
    keys = [script.get("script_key") for script in scripts]
    if len(keys) != len(set(keys)):
        raise ManifestError("script_key values must be unique")
    catalogs = [script.get("catalog") for script in scripts]
    if len(catalogs) != len(set(catalogs)):
        raise ManifestError("catalog paths must be unique")
    for script in scripts:
        for key in ("script_key", "source_file", "catalog", "expected_records", "packets"):
            if key not in script:
                raise ManifestError(f"script entry missing {key}")
        if not isinstance(script["packets"], list):
            raise ManifestError(f"{script['script_key']}: packets must be an array")


def build(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    manifest_path = args.manifest.resolve()
    manifest = read_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ManifestError("manifest root must be an object")
    validate_manifest(manifest)
    variables = manifest.get("variables") or {}
    if not isinstance(variables, dict) or not all(
        isinstance(key, str) and isinstance(value, str) for key, value in variables.items()
    ):
        raise ManifestError("variables must be a string-to-string object")

    if args.output_root is None:
        output_root = manifest_path.parent / "output"
    else:
        output_root = args.output_root.resolve()
    masters_dir = output_root / "masters"
    masters_dir.mkdir(parents=True, exist_ok=True)

    conflict_policy_list = manifest.get("conflict_policies") or []
    if not isinstance(conflict_policy_list, list):
        raise ManifestError("conflict_policies must be an array")
    conflict_policies: dict[str, dict[str, Any]] = {}
    for policy in conflict_policy_list:
        if not isinstance(policy, dict) or not isinstance(policy.get("stable_id"), str):
            raise ManifestError("each conflict policy must contain stable_id")
        if policy["stable_id"] in conflict_policies:
            raise ManifestError(f"duplicate conflict policy for {policy['stable_id']}")
        conflict_policies[policy["stable_id"]] = policy

    script_reports: list[dict[str, Any]] = []
    all_conflicts: list[dict[str, Any]] = []
    all_errors: list[dict[str, Any]] = []
    output_paths: list[Path] = []
    for script in manifest["scripts"]:
        report, conflicts, errors, master_path = process_script(
            script=script,
            variables=variables,
            conflict_policies=conflict_policies,
            masters_dir=masters_dir,
        )
        script_reports.append(report)
        all_conflicts.extend(conflicts)
        all_errors.extend(errors)
        output_paths.append(master_path)

    used_conflict_ids = {conflict["stable_id"] for conflict in all_conflicts}
    unused_global_policies = sorted(set(conflict_policies) - used_conflict_ids)
    if unused_global_policies:
        all_errors.append(
            {
                "kind": "unused_global_conflict_policies",
                "stable_ids": unused_global_policies,
            }
        )

    summary = {
        "expected_catalog_files": manifest["catalog_expectations"]["file_count"],
        "actual_catalog_files": len(script_reports),
        "expected_catalog_records": manifest["catalog_expectations"]["record_count"],
        "actual_catalog_records": sum(report["coverage"]["catalog_records"] for report in script_reports),
        "packet_occurrences": sum(report["coverage"]["packet_occurrences"] for report in script_reports),
        "selected_unique_records": sum(
            report["coverage"]["selected_unique_records"] for report in script_reports
        ),
        "duplicate_extra_occurrences": sum(
            report["coverage"]["duplicate_extra_occurrences"] for report in script_reports
        ),
        "missing_records": sum(report["coverage"]["missing_records"] for report in script_reports),
        "pending_packets": sum(len(report["pending_packets"]) for report in script_reports),
        "hard_token_failed_records": sum(
            report["coverage"]["hard_token_failed_records"] for report in script_reports
        ),
        "hard_token_findings": sum(error.get("kind") == "hard_token_mismatch" for error in all_errors),
        "resolved_conflicts": sum(1 for conflict in all_conflicts if conflict["resolved"]),
        "unresolved_conflicts": sum(1 for conflict in all_conflicts if not conflict["resolved"]),
        "structural_errors": len(all_errors),
        "structural_pass": not all_errors and all(report["structural_pass"] for report in script_reports),
        "coverage_complete": all(report["coverage_complete"] for report in script_reports),
        "complete": all(report["complete"] for report in script_reports),
        "translation_qa_performed": False,
        "translation_text_modified": False,
    }

    conflict_report = {
        "schema_version": "fatal-twelve-master-conflict-report-v1",
        "translation_review_performed": False,
        "selection_rule": "Only an exact manifest policy may select a duplicated occurrence.",
        "conflict_count": len(all_conflicts),
        "resolved_conflicts": sum(1 for conflict in all_conflicts if conflict["resolved"]),
        "conflicts": all_conflicts,
    }
    conflict_path = output_root / "conflict_report.json"
    write_json(conflict_path, conflict_report)

    coverage_report = {
        "schema_version": REPORT_SCHEMA_VERSION,
        "manifest": {"path": str(manifest_path), "sha256": file_sha256(manifest_path)},
        "summary": summary,
        "scripts": script_reports,
        "conflict_report": {"path": str(conflict_path), "sha256": file_sha256(conflict_path)},
        "errors": all_errors,
    }
    coverage_path = output_root / "coverage_report.json"
    write_json(coverage_path, coverage_report)

    master_index = {
        "schema_version": "fatal-twelve-master-index-v1",
        "manifest": {"path": str(manifest_path), "sha256": file_sha256(manifest_path)},
        "summary": summary,
        "masters": [
            {
                "script_key": report["script_key"],
                "path": report["master_path"],
                "sha256": report["master_sha256"],
                "catalog_records": report["coverage"]["catalog_records"],
                "selected_unique_records": report["coverage"]["selected_unique_records"],
                "coverage_complete": report["coverage_complete"],
                "complete": report["complete"],
                "structural_pass": report["structural_pass"],
            }
            for report in script_reports
        ],
        "coverage_report": {"path": str(coverage_path), "sha256": file_sha256(coverage_path)},
        "conflict_report": {"path": str(conflict_path), "sha256": file_sha256(conflict_path)},
    }
    index_path = output_root / "master_index.json"
    write_json(index_path, master_index)

    result = {
        "summary": summary,
        "manifest": str(manifest_path),
        "manifest_sha256": file_sha256(manifest_path),
        "output_root": str(output_root),
        "master_index": str(index_path),
        "master_index_sha256": file_sha256(index_path),
        "coverage_report": str(coverage_path),
        "coverage_report_sha256": file_sha256(coverage_path),
        "conflict_report": str(conflict_path),
        "conflict_report_sha256": file_sha256(conflict_path),
    }
    if all_errors:
        exit_code = 1
    elif args.require_complete and not summary["complete"]:
        exit_code = 2
    else:
        exit_code = 0
    return result, exit_code


def parse_args(argv: list[str]) -> argparse.Namespace:
    default_manifest = Path(__file__).with_name("packet_manifest.json")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=default_manifest)
    parser.add_argument("--output-root", type=Path)
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="Return exit code 2 when manifest placeholders leave expected records pending.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        result, exit_code = build(args)
    except Exception as exc:
        print(json.dumps({"fatal_error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

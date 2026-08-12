#!/usr/bin/env python3
"""Render validated corrected masters into per-script RPY plus global strings."""

from __future__ import annotations

import argparse
import ast
import collections
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from final_qa_common import (
    TRANSLATE_HEADER_RE,
    canonical_json,
    file_sha256,
    read_json,
    replace_statement_text,
    text_sha256,
    token_validation_findings,
    write_json,
)


CORRECTED_INDEX_SCHEMA = "fatal-twelve-corrected-master-index-v1"
RENDER_MANIFEST_SCHEMA = "fatal-twelve-final-rpy-render-manifest-v1"


class RenderError(ValueError):
    """Corrected master validation or final rendering failed."""


def path_key(path: Path) -> str:
    return os.path.normcase(os.path.abspath(str(path))).replace("/", "\\")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def validate_corrected_master(
    *, script_key: str, reference: dict[str, Any]
) -> tuple[dict[str, Any], Path, str]:
    path_value = reference.get("path")
    expected_sha = reference.get("sha256")
    expected_records = reference.get("records")
    if not isinstance(path_value, str) or not isinstance(expected_sha, str) or not isinstance(expected_records, int):
        raise RenderError(f"{script_key}: invalid corrected master reference")
    path = Path(path_value)
    if not path.is_file():
        raise RenderError(f"{script_key}: corrected master does not exist: {path}")
    if file_sha256(path) != expected_sha:
        raise RenderError(f"{script_key}: corrected master SHA-256 mismatch")
    document = read_json(path)
    if not isinstance(document, dict):
        raise RenderError(f"{script_key}: corrected master root must be an object")
    is_system_ui = document.get("schema_version") == "fatal-twelve-system-ui-master-v1"
    kind = reference.get("kind") or ("system_ui_strings" if is_system_ui else "scenario")
    if kind not in {"scenario", "system_ui_strings"}:
        raise RenderError(f"{script_key}: unsupported corrected master kind {kind!r}")
    document_key = document.get("script_key")
    identity_matches = document_key == script_key or (
        is_system_ui and kind == "system_ui_strings" and script_key == "system_ui" and document_key is None
    )
    if not identity_matches:
        raise RenderError(f"{script_key}: corrected master identity mismatch")
    if kind == "system_ui_strings" and not is_system_ui:
        raise RenderError(f"{script_key}: system_ui_strings kind requires the system UI master schema")
    entries = document.get("entries")
    if not isinstance(entries, list) or len(entries) != expected_records:
        raise RenderError(f"{script_key}: corrected master record count mismatch")
    stable_ids: set[str] = set()
    for position, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            raise RenderError(f"{script_key}:{position}: entry must be an object")
        required = [
            "stable_id",
            "sequence",
            "source_jp",
            "translation_id",
            "menu_key",
            "draft_ko",
            "draft_ko_sha256",
            "protected_tokens",
        ]
        if kind == "scenario":
            required.extend(["source_statement_code", "source_group_code"])
        missing = [field for field in required if field not in entry]
        if missing:
            raise RenderError(f"{script_key}:{position}: missing fields {missing}")
        if entry["sequence"] != position:
            raise RenderError(f"{script_key}:{position}: sequence is not contiguous")
        stable_id = entry["stable_id"]
        if not isinstance(stable_id, str) or not stable_id or stable_id in stable_ids:
            raise RenderError(f"{script_key}:{position}: invalid or duplicate stable_id")
        stable_ids.add(stable_id)
        if not isinstance(entry["source_jp"], str) or not isinstance(entry["draft_ko"], str):
            raise RenderError(f"{script_key}:{position}: source/draft must be strings")
        if text_sha256(entry["draft_ko"]) != entry["draft_ko_sha256"]:
            raise RenderError(f"{script_key}:{position}: draft_ko SHA-256 mismatch")
        findings = token_validation_findings(entry, entry["draft_ko"])
        if findings:
            raise RenderError(
                f"{script_key}:{position}: runtime/protected-token validation failed: "
                f"{json.dumps(findings, ensure_ascii=False, separators=(',', ':'))}"
            )
        translation_id = entry["translation_id"]
        menu_key = entry["menu_key"]
        if (translation_id is None) == (menu_key is None):
            raise RenderError(
                f"{script_key}:{position}: exactly one of translation_id/menu_key must be non-null"
            )
        if translation_id is not None and (not isinstance(translation_id, str) or not translation_id):
            raise RenderError(f"{script_key}:{position}: invalid translation_id")
        if menu_key is not None and (not isinstance(menu_key, str) or not menu_key):
            raise RenderError(f"{script_key}:{position}: invalid menu_key")
    return document, path, kind


def render_script(
    script_key: str, entries: list[dict[str, Any]]
) -> tuple[str, list[str], list[dict[str, Any]], str]:
    lines = [
        f"# Fatal Twelve Korean final scenario: {script_key}",
        "# Generated from corrected exact master; source group/runtime commands preserved.",
        "# Menu strings are emitted once in the global scenario_strings.rpy file.",
        "",
    ]
    translation_ids: list[str] = []
    menu_entries: list[dict[str, Any]] = []
    source_group_digest = hashlib.sha256()
    for entry in entries:
        if entry["translation_id"] is None:
            menu_entries.append(entry)
            continue
        translation_id = entry["translation_id"]
        statement = entry["source_statement_code"]
        group = entry["source_group_code"]
        if not isinstance(statement, str) or not isinstance(group, list) or not all(
            isinstance(line, str) for line in group
        ):
            raise RenderError(f"{entry['stable_id']}: invalid source statement/group code")
        if group.count(statement) != 1:
            raise RenderError(
                f"{entry['stable_id']}: source_statement_code must occur exactly once in source_group_code"
            )
        rendered_group: list[str] = []
        replacements = 0
        for code_line in group:
            if code_line == statement:
                rendered_group.append(
                    replace_statement_text(statement, entry["source_jp"], entry["draft_ko"])
                )
                replacements += 1
            else:
                rendered_group.append(code_line)
        if replacements != 1:
            raise RenderError(f"{entry['stable_id']}: expected one statement replacement")
        for original, rendered in zip(group, rendered_group):
            if original != statement and original != rendered:
                raise RenderError(f"{entry['stable_id']}: non-statement runtime command changed")

        source_group_digest.update(entry["stable_id"].encode("utf-8"))
        source_group_digest.update(b"\0")
        source_group_digest.update(canonical_json(group).encode("utf-8"))
        source_group_digest.update(b"\n")
        translation_ids.append(translation_id)
        lines.append(f"translate korean {translation_id}:")
        lines.append("")
        lines.extend(f"    {code_line}" for code_line in rendered_group)
        lines.append("")
        lines.append("")
    text = "\n".join(lines).rstrip() + "\n"
    parsed_ids = TRANSLATE_HEADER_RE.findall(text)
    if parsed_ids != translation_ids or len(parsed_ids) != len(set(parsed_ids)):
        raise RenderError(f"{script_key}: rendered translation headers differ from master order")
    return text, translation_ids, menu_entries, source_group_digest.hexdigest()


def parse_supplemental_strings(path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Parse a data-only translate-korean-strings RPY supplement.

    Only comments, blank lines, one strings header, and paired old/new Python
    string literals are accepted. This keeps add-only runtime keys in the same
    collision-checked global keyspace as scenario and system-UI keys.
    """
    resolved = path.resolve()
    if not resolved.is_file():
        raise RenderError(f"supplemental strings file does not exist: {resolved}")
    raw = resolved.read_text(encoding="utf-8-sig")
    header_seen = False
    pending_old: tuple[str, int] | None = None
    pairs: list[dict[str, Any]] = []
    for line_number, line in enumerate(raw.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "translate korean strings:":
            if header_seen or pending_old is not None or pairs:
                raise RenderError(f"{resolved}:{line_number}: duplicate or misplaced strings header")
            header_seen = True
            continue
        if not header_seen:
            raise RenderError(f"{resolved}:{line_number}: content before strings header")
        if stripped.startswith("old "):
            if pending_old is not None:
                raise RenderError(f"{resolved}:{line_number}: old without preceding new")
            try:
                old = ast.literal_eval(stripped[4:])
            except (SyntaxError, ValueError) as exc:
                raise RenderError(f"{resolved}:{line_number}: invalid old string literal") from exc
            if not isinstance(old, str) or not old:
                raise RenderError(f"{resolved}:{line_number}: old must be a nonempty string")
            pending_old = (old, line_number)
            continue
        if stripped.startswith("new "):
            if pending_old is None:
                raise RenderError(f"{resolved}:{line_number}: new without preceding old")
            try:
                target = ast.literal_eval(stripped[4:])
            except (SyntaxError, ValueError) as exc:
                raise RenderError(f"{resolved}:{line_number}: invalid new string literal") from exc
            if not isinstance(target, str) or not target:
                raise RenderError(f"{resolved}:{line_number}: new must be a nonempty string")
            old, old_line = pending_old
            pairs.append(
                {
                    "old": old,
                    "target": target,
                    "old_line": old_line,
                    "new_line": line_number,
                }
            )
            pending_old = None
            continue
        raise RenderError(f"{resolved}:{line_number}: executable or unsupported supplement content")
    if not header_seen:
        raise RenderError(f"{resolved}: missing translate korean strings header")
    if pending_old is not None:
        raise RenderError(f"{resolved}:{pending_old[1]}: old has no matching new")
    if not pairs:
        raise RenderError(f"{resolved}: supplemental strings file contains no pairs")
    report = {
        "path": str(resolved),
        "sha256": file_sha256(resolved),
        "pairs": len(pairs),
        "merged_into": "strings/scenario_strings.rpy",
        "parser_policy": "data-only old/new literal pairs",
    }
    return pairs, report


def render_comment_text(value: Any) -> str:
    """Return one physical-line, non-executable provenance comment text."""
    pieces = []
    for char in str(value):
        codepoint = ord(char)
        if char == "\\":
            pieces.append("\\\\")
        elif char == "\r":
            pieces.append("\\r")
        elif char == "\n":
            pieces.append("\\n")
        elif char == "\t":
            pieces.append("\\t")
        elif codepoint < 0x20 or char in {"\u0085", "\u2028", "\u2029"}:
            pieces.append(f"\\u{codepoint:04x}")
        else:
            pieces.append(char)
    rendered = "".join(pieces)
    if len(rendered.splitlines()) != 1:
        raise RenderError("provenance comment was not reduced to one physical line")
    return rendered


def render_global_strings(menu_by_old: dict[str, dict[str, Any]]) -> str:
    lines = [
        "# Fatal Twelve Korean global menu strings",
        "# Identical old keys are deduplicated only when every target is exactly equal.",
        "",
        "translate korean strings:",
        "",
    ]
    expected_old: list[str] = []
    expected_new: list[str] = []
    for old, item in menu_by_old.items():
        expected_old.append(old)
        expected_new.append(item["target"])
        for occurrence in item["occurrences"]:
            provenance = (
                f"{occurrence['script_key']}:{occurrence['sequence']} "
                f"{occurrence['menu_key']} {occurrence['stable_id']}"
            )
            lines.append(f"    # {render_comment_text(provenance)}")
        lines.append(f"    old {json.dumps(old, ensure_ascii=False)}")
        lines.append(f"    new {json.dumps(item['target'], ensure_ascii=False)}")
        lines.append("")
    text = "\n".join(lines).rstrip() + "\n"
    parsed_old: list[str] = []
    parsed_new: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("old "):
            parsed_old.append(ast.literal_eval(stripped[4:]))
        elif stripped.startswith("new "):
            parsed_new.append(ast.literal_eval(stripped[4:]))
    if parsed_old != expected_old or parsed_new != expected_new:
        raise RenderError("global menu strings literal round trip failed")
    return text


def render(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    corrected_index_path = args.master_index.resolve()
    output_root = args.output_root.resolve()
    if not corrected_index_path.is_file():
        raise RenderError(f"corrected master index does not exist: {corrected_index_path}")
    corrected_index = read_json(corrected_index_path)
    if not isinstance(corrected_index, dict) or corrected_index.get("schema_version") != CORRECTED_INDEX_SCHEMA:
        raise RenderError("input must be a corrected master index produced by apply_corrections.py")
    references = corrected_index.get("masters")
    summary = corrected_index.get("summary")
    if not isinstance(references, list) or not isinstance(summary, dict):
        raise RenderError("corrected master index is missing masters or summary")
    if len(references) != summary.get("scripts"):
        raise RenderError("corrected master index script count mismatch")
    if len({reference.get("script_key") for reference in references}) != len(references):
        raise RenderError("duplicate script_key in corrected master index")

    masters: list[tuple[str, str, dict[str, Any], Path, dict[str, Any]]] = []
    input_record_total = 0
    input_hashes: dict[str, str] = {}
    for reference in references:
        if not isinstance(reference, dict) or not isinstance(reference.get("script_key"), str):
            raise RenderError("invalid corrected master reference")
        script_key = reference["script_key"]
        document, path, kind = validate_corrected_master(script_key=script_key, reference=reference)
        masters.append((script_key, kind, document, path, reference))
        input_record_total += len(document["entries"])
        input_hashes[script_key] = reference["sha256"]
    if input_record_total != summary.get("records"):
        raise RenderError("corrected master record total mismatch")

    rendered_scripts: dict[str, dict[str, Any]] = {}
    global_translation_ids: dict[str, tuple[str, str]] = {}
    menu_by_old: dict[str, dict[str, Any]] = {}
    menu_key_map: dict[str, tuple[str, str]] = {}
    total_menu_occurrences = 0
    for script_key, kind, document, master_path, reference in masters:
        if kind == "system_ui_strings":
            text = None
            translation_ids = []
            menu_entries = document["entries"]
            source_group_sha = None
        else:
            text, translation_ids, menu_entries, source_group_sha = render_script(
                script_key, document["entries"]
            )
        for translation_id in translation_ids:
            previous = global_translation_ids.get(translation_id)
            if previous is not None:
                raise RenderError(
                    f"duplicate global translation_id {translation_id}: {previous[0]} and {script_key}"
                )
            global_translation_ids[translation_id] = (script_key, str(master_path))
        for entry in menu_entries:
            total_menu_occurrences += 1
            old = entry["source_jp"]
            target = entry["draft_ko"]
            menu_key = entry["menu_key"]
            previous_key = menu_key_map.get(menu_key)
            if previous_key is not None and previous_key != (old, target):
                raise RenderError(
                    f"menu_key maps to conflicting old/target values: {menu_key}"
                )
            menu_key_map[menu_key] = (old, target)
            existing = menu_by_old.get(old)
            occurrence = {
                "script_key": script_key,
                "sequence": entry["sequence"],
                "stable_id": entry["stable_id"],
                "menu_key": menu_key,
            }
            if existing is None:
                menu_by_old[old] = {"target": target, "occurrences": [occurrence]}
            elif existing["target"] != target:
                raise RenderError(
                    "global menu old-key target conflict: "
                    + json.dumps(
                        {
                            "old": old,
                            "first_target": existing["target"],
                            "conflicting_target": target,
                            "first_occurrences": existing["occurrences"],
                            "conflicting_occurrence": occurrence,
                        },
                        ensure_ascii=False,
                        separators=(",", ":"),
                    )
                )
            else:
                existing["occurrences"].append(occurrence)
        rendered_scripts[script_key] = {
            "kind": kind,
            "text": text,
            "translation_ids": translation_ids,
            "menu_entries": menu_entries,
            "source_group_code_sha256": source_group_sha,
            "master_path": master_path,
            "master_reference": reference,
        }

    master_unique_old_keys = len(menu_by_old)
    master_deduplicated_occurrences = total_menu_occurrences - master_unique_old_keys
    supplemental_reports: list[dict[str, Any]] = []
    supplemental_old_keys: dict[str, tuple[str, int, str]] = {}
    total_supplemental_pairs = 0
    for supplemental_path in args.supplemental_strings:
        pairs, report = parse_supplemental_strings(supplemental_path)
        report_index = len(supplemental_reports)
        for pair_index, pair in enumerate(pairs, 1):
            old = pair["old"]
            target = pair["target"]
            if old in menu_by_old:
                raise RenderError(
                    "supplemental old-key collision with scenario/system UI: "
                    + json.dumps(
                        {
                            "old": old,
                            "supplemental_path": report["path"],
                            "supplemental_line": pair["old_line"],
                            "existing_target": menu_by_old[old]["target"],
                            "supplemental_target": target,
                        },
                        ensure_ascii=False,
                        separators=(",", ":"),
                    )
                )
            previous = supplemental_old_keys.get(old)
            if previous is not None:
                raise RenderError(
                    "duplicate supplemental old key: "
                    + json.dumps(
                        {
                            "old": old,
                            "first_path": previous[0],
                            "first_line": previous[1],
                            "conflicting_path": report["path"],
                            "conflicting_line": pair["old_line"],
                        },
                        ensure_ascii=False,
                        separators=(",", ":"),
                    )
                )
            supplemental_old_keys[old] = (report["path"], pair["old_line"], target)
            menu_by_old[old] = {
                "target": target,
                "occurrences": [
                    {
                        "script_key": "supplemental_strings",
                        "sequence": pair_index,
                        "stable_id": (
                            f"supplemental::{report['sha256'][:16]}::{pair_index:04d}"
                        ),
                        "menu_key": old,
                        "supplemental_input_index": report_index,
                    }
                ],
            }
            total_supplemental_pairs += 1
        supplemental_reports.append(report)

    global_strings_text = render_global_strings(menu_by_old)
    scripts_dir = output_root / "scenario"
    strings_dir = output_root / "strings"
    output_script_reports: list[dict[str, Any]] = []
    system_ui_reports: list[dict[str, Any]] = []
    for script_key, kind, _, master_path, reference in masters:
        rendered = rendered_scripts[script_key]
        if kind == "system_ui_strings":
            system_ui_reports.append(
                {
                    "script_key": script_key,
                    "kind": kind,
                    "corrected_master_path": str(master_path),
                    "corrected_master_sha256": reference["sha256"],
                    "records": len(rendered["menu_entries"]),
                    "menu_occurrences_collected_globally": len(rendered["menu_entries"]),
                    "per_script_rpy": None,
                }
            )
            continue
        output_path = scripts_dir / f"scenario_{script_key}.rpy"
        if path_key(output_path) == path_key(master_path):
            raise RenderError(f"refusing to overwrite corrected master: {master_path}")
        write_text(output_path, rendered["text"])
        if output_path.read_text(encoding="utf-8") != rendered["text"]:
            raise RenderError(f"{script_key}: RPY output round trip failed")
        output_script_reports.append(
            {
                "script_key": script_key,
                "kind": kind,
                "corrected_master_path": str(master_path),
                "corrected_master_sha256": reference["sha256"],
                "path": str(output_path),
                "sha256": file_sha256(output_path),
                "bytes": output_path.stat().st_size,
                "records": len(rendered["translation_ids"]) + len(rendered["menu_entries"]),
                "translate_blocks": len(rendered["translation_ids"]),
                "menu_occurrences_collected_globally": len(rendered["menu_entries"]),
                "source_group_code_sha256": rendered["source_group_code_sha256"],
                "statement_replacement_validation": "passed",
            }
        )

    global_strings_path = strings_dir / "scenario_strings.rpy"
    write_text(global_strings_path, global_strings_text)
    if global_strings_path.read_text(encoding="utf-8") != global_strings_text:
        raise RenderError("global strings RPY output round trip failed")

    for script_key, _, _, path, _ in masters:
        if file_sha256(path) != input_hashes[script_key]:
            raise RenderError(f"corrected master changed during rendering: {path}")
    for report in supplemental_reports:
        if file_sha256(Path(report["path"])) != report["sha256"]:
            raise RenderError(f"supplemental strings changed during rendering: {report['path']}")

    manifest = {
        "schema_version": RENDER_MANIFEST_SCHEMA,
        "render_mode": "validated source_group_code statement substitution",
        "corrected_masters_modified": False,
        "corrected_master_index": {
            "path": str(corrected_index_path),
            "sha256": file_sha256(corrected_index_path),
        },
        "summary": {
            "input_masters": len(masters),
            "scripts": len(output_script_reports),
            "system_ui_string_masters": len(system_ui_reports),
            "records": input_record_total,
            "translate_blocks": len(global_translation_ids),
            "menu_occurrences": total_menu_occurrences,
            "unique_global_menu_old_keys": master_unique_old_keys,
            "deduplicated_same_target_menu_occurrences": master_deduplicated_occurrences,
            "supplemental_string_inputs": len(supplemental_reports),
            "supplemental_string_pairs": total_supplemental_pairs,
            "supplemental_old_key_conflicts": 0,
            "total_unique_global_old_keys": len(menu_by_old),
            "menu_target_conflicts": 0,
            "runtime_and_protected_token_validation": "passed",
            "source_group_statement_replacement_validation": "passed",
        },
        "scripts": output_script_reports,
        "system_ui_string_masters": system_ui_reports,
        "supplemental_strings": supplemental_reports,
        "global_strings": {
            "path": str(global_strings_path),
            "sha256": file_sha256(global_strings_path),
            "bytes": global_strings_path.stat().st_size,
            "menu_occurrences": total_menu_occurrences,
            "supplemental_pairs": total_supplemental_pairs,
            "unique_old_keys": len(menu_by_old),
            "old_keys": [
                {
                    "old": old,
                    "target_sha256": text_sha256(item["target"]),
                    "occurrences": item["occurrences"],
                }
                for old, item in menu_by_old.items()
            ],
        },
    }
    manifest_path = output_root / "render_manifest.json"
    write_json(manifest_path, manifest)
    result = {
        "render_manifest": str(manifest_path),
        "render_manifest_sha256": file_sha256(manifest_path),
        "output_root": str(output_root),
        "global_strings": str(global_strings_path),
        "global_strings_sha256": file_sha256(global_strings_path),
        "summary": manifest["summary"],
    }
    return result, 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--master-index", type=Path, required=True)
    parser.add_argument(
        "--supplemental-strings",
        type=Path,
        action="append",
        default=[],
        help="Data-only Ren'Py strings RPY to merge into the global collision-checked keyspace. Repeatable.",
    )
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        result, exit_code = render(args)
    except Exception as exc:
        print(json.dumps({"fatal_error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Apply reviewer JSONL corrections to an isolated master working copy.

Every correction is guarded by ``stable_id`` plus an exact, unnormalised
``old_ko`` match.  Duplicate stable IDs are forbidden across all reviewer
files.  New targets must pass runtime/protected-token validation before any
output master is written.
"""

from __future__ import annotations

import argparse
import collections
import copy
import json
import os
import sys
from pathlib import Path
from typing import Any

from final_qa_common import (
    file_sha256,
    read_json,
    text_sha256,
    token_validation_findings,
    write_json,
)


CORRECTED_INDEX_SCHEMA = "fatal-twelve-corrected-master-index-v1"
AUDIT_SCHEMA = "fatal-twelve-correction-audit-v1"
REVIEW_GROUP_SCHEMA = "fatal-twelve-review-group-manifest-v1"


class CorrectionError(ValueError):
    """Correction input or exact-guard validation failed."""


def path_key(path: Path) -> str:
    return os.path.normcase(os.path.abspath(str(path))).replace("/", "\\")


def load_review_assignments(path: Path) -> tuple[dict[str, str], list[str], str]:
    document = read_json(path)
    if not isinstance(document, dict) or document.get("schema_version") != REVIEW_GROUP_SCHEMA:
        raise CorrectionError("invalid review group manifest")
    groups = document.get("groups")
    if not isinstance(groups, list):
        raise CorrectionError("review group manifest has no groups array")
    assignment: dict[str, str] = {}
    group_order: list[str] = []
    for group in groups:
        group_id = group.get("group_id") if isinstance(group, dict) else None
        scripts = group.get("scripts") if isinstance(group, dict) else None
        if not isinstance(group_id, str) or not group_id or not isinstance(scripts, list):
            raise CorrectionError("invalid review group entry")
        if group_id in group_order:
            raise CorrectionError(f"duplicate review group {group_id}")
        group_order.append(group_id)
        for item in scripts:
            script_key = item.get("script_key") if isinstance(item, dict) else None
            if not isinstance(script_key, str) or not script_key:
                raise CorrectionError(f"{group_id}: invalid script assignment")
            if script_key in assignment:
                raise CorrectionError(f"script assigned to multiple reviewers: {script_key}")
            assignment[script_key] = group_id
    return assignment, group_order, file_sha256(path)


def validate_master_document(
    *, script_key: str, document: dict[str, Any], expected_sha: str, path: Path
) -> None:
    if file_sha256(path) != expected_sha:
        raise CorrectionError(f"{script_key}: master SHA-256 differs from index")
    document_key = document.get("script_key")
    is_system_ui = document.get("schema_version") == "fatal-twelve-system-ui-master-v1"
    identity_matches = document_key == script_key or (
        is_system_ui and script_key == "system_ui" and document_key is None
    )
    if not identity_matches or not isinstance(document.get("entries"), list):
        raise CorrectionError(f"{script_key}: invalid master document")
    entries = document["entries"]
    stable_ids: set[str] = set()
    for position, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            raise CorrectionError(f"{script_key}:{position}: entry must be an object")
        for field in (
            "stable_id",
            "sequence",
            "source_jp",
            "draft_ko",
            "draft_ko_sha256",
            "protected_tokens",
        ):
            if field not in entry:
                raise CorrectionError(f"{script_key}:{position}: missing {field}")
        if entry["sequence"] != position:
            raise CorrectionError(f"{script_key}:{position}: non-contiguous sequence")
        if not isinstance(entry["stable_id"], str) or entry["stable_id"] in stable_ids:
            raise CorrectionError(f"{script_key}:{position}: invalid or duplicate stable_id")
        stable_ids.add(entry["stable_id"])
        if not isinstance(entry["source_jp"], str) or not isinstance(entry["draft_ko"], str):
            raise CorrectionError(f"{script_key}:{position}: source/draft must be strings")
        if text_sha256(entry["draft_ko"]) != entry["draft_ko_sha256"]:
            raise CorrectionError(f"{script_key}:{position}: draft_ko SHA-256 mismatch")


def parse_correction_spec(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise CorrectionError("--correction must be REVIEWER=PATH")
    reviewer, path_value = value.split("=", 1)
    if not reviewer or not path_value:
        raise CorrectionError("--correction must be REVIEWER=PATH")
    return reviewer, Path(path_value)


def load_correction_file(reviewer: str, path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not path.is_file():
        raise CorrectionError(f"{reviewer}: correction JSONL does not exist: {path}")
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise CorrectionError(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
            if not isinstance(record, dict):
                raise CorrectionError(f"{path}:{line_number}: correction must be an object")
            record = copy.deepcopy(record)
            record["_input_line"] = line_number
            records.append(record)
    return records, {
        "reviewer": reviewer,
        "path": str(path),
        "sha256": file_sha256(path),
        "records": len(records),
    }


def validate_correction_shape(record: dict[str, Any], reviewer: str, path: Path) -> None:
    line = record["_input_line"]
    missing = [field for field in ("stable_id", "old_ko", "new_ko") if field not in record]
    if missing:
        raise CorrectionError(f"{path}:{line}: missing fields {missing}")
    if not isinstance(record["stable_id"], str) or not record["stable_id"]:
        raise CorrectionError(f"{path}:{line}: stable_id must be a nonempty string")
    if not isinstance(record["old_ko"], str) or not isinstance(record["new_ko"], str):
        raise CorrectionError(f"{path}:{line}: old_ko/new_ko must be strings")
    if record["new_ko"] == "":
        raise CorrectionError(f"{path}:{line}: new_ko must not be empty")
    if record["old_ko"] == record["new_ko"]:
        raise CorrectionError(f"{path}:{line}: no-op correction is forbidden")
    if "reviewer" in record and record["reviewer"] != reviewer:
        raise CorrectionError(f"{path}:{line}: embedded reviewer does not match {reviewer}")
    if "script_key" in record and not isinstance(record["script_key"], str):
        raise CorrectionError(f"{path}:{line}: script_key guard must be a string")
    if "sequence" in record and not isinstance(record["sequence"], int):
        raise CorrectionError(f"{path}:{line}: sequence guard must be an integer")
    if "note" in record and not isinstance(record["note"], str):
        raise CorrectionError(f"{path}:{line}: note must be a string")


def apply(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    master_index_path = args.master_index.resolve()
    review_groups_path = args.review_groups.resolve()
    output_root = args.output_root.resolve()
    if not master_index_path.is_file():
        raise CorrectionError(f"master index does not exist: {master_index_path}")
    if not review_groups_path.is_file():
        raise CorrectionError(f"review group manifest does not exist: {review_groups_path}")
    if not args.correction:
        raise CorrectionError("at least one --correction REVIEWER=PATH is required")

    review_assignment, reviewer_order, review_groups_sha = load_review_assignments(review_groups_path)
    master_index = read_json(master_index_path)
    if not isinstance(master_index, dict) or not isinstance(master_index.get("masters"), list):
        raise CorrectionError("invalid master index")
    master_refs = master_index["masters"]
    if len({item.get("script_key") for item in master_refs}) != len(master_refs):
        raise CorrectionError("duplicate script_key in master index")

    masters: dict[str, dict[str, Any]] = {}
    master_paths: dict[str, Path] = {}
    input_master_hashes: dict[str, str] = {}
    stable_index: dict[str, tuple[str, int]] = {}
    total_records = 0
    for reference in master_refs:
        if not isinstance(reference, dict):
            raise CorrectionError("master index item must be an object")
        script_key = reference.get("script_key")
        path_value = reference.get("path")
        expected_sha = reference.get("sha256")
        if not isinstance(script_key, str) or not isinstance(path_value, str) or not isinstance(expected_sha, str):
            raise CorrectionError("invalid master index item")
        if script_key not in review_assignment:
            raise CorrectionError(f"master script has no reviewer assignment: {script_key}")
        path = Path(path_value)
        if not path.is_file():
            raise CorrectionError(f"master does not exist: {path}")
        document = read_json(path)
        if not isinstance(document, dict):
            raise CorrectionError(f"{script_key}: master root must be an object")
        validate_master_document(
            script_key=script_key,
            document=document,
            expected_sha=expected_sha,
            path=path,
        )
        masters[script_key] = document
        master_paths[script_key] = path
        input_master_hashes[script_key] = expected_sha
        total_records += len(document["entries"])
        for entry_index, entry in enumerate(document["entries"]):
            stable_id = entry["stable_id"]
            if stable_id in stable_index:
                raise CorrectionError(f"stable_id is not globally unique: {stable_id}")
            stable_index[stable_id] = (script_key, entry_index)

    correction_specs = [parse_correction_spec(value) for value in args.correction]
    reviewer_files: dict[str, Path] = {}
    for reviewer, path in correction_specs:
        if reviewer not in reviewer_order:
            raise CorrectionError(f"unknown reviewer group: {reviewer}")
        if reviewer in reviewer_files:
            raise CorrectionError(f"multiple correction JSONLs supplied for reviewer {reviewer}")
        reviewer_files[reviewer] = path.resolve()

    correction_inputs: list[dict[str, Any]] = []
    validated_corrections: list[dict[str, Any]] = []
    seen_stable_ids: dict[str, tuple[str, Path, int]] = {}
    for reviewer in reviewer_order:
        path = reviewer_files.get(reviewer)
        if path is None:
            continue
        records, input_report = load_correction_file(reviewer, path)
        correction_inputs.append(input_report)
        for record in records:
            validate_correction_shape(record, reviewer, path)
            stable_id = record["stable_id"]
            line = record["_input_line"]
            if stable_id in seen_stable_ids:
                previous = seen_stable_ids[stable_id]
                raise CorrectionError(
                    f"duplicate correction stable_id {stable_id}: "
                    f"{previous[1]}:{previous[2]} and {path}:{line}"
                )
            seen_stable_ids[stable_id] = (reviewer, path, line)
            location = stable_index.get(stable_id)
            if location is None:
                raise CorrectionError(f"{path}:{line}: unknown stable_id {stable_id}")
            script_key, entry_index = location
            expected_reviewer = review_assignment[script_key]
            if reviewer != expected_reviewer:
                raise CorrectionError(
                    f"{path}:{line}: reviewer {reviewer} cannot modify {script_key}; expected {expected_reviewer}"
                )
            entry = masters[script_key]["entries"][entry_index]
            if record.get("script_key", script_key) != script_key:
                raise CorrectionError(f"{path}:{line}: script_key exact guard failed")
            if record.get("sequence", entry["sequence"]) != entry["sequence"]:
                raise CorrectionError(f"{path}:{line}: sequence exact guard failed")
            if record["old_ko"] != entry["draft_ko"]:
                raise CorrectionError(f"{path}:{line}: old_ko exact guard failed for {stable_id}")
            findings = token_validation_findings(entry, record["new_ko"])
            if findings:
                raise CorrectionError(
                    f"{path}:{line}: new_ko runtime/protected-token validation failed for "
                    f"{stable_id}: {json.dumps(findings, ensure_ascii=False, separators=(',', ':'))}"
                )
            validated_corrections.append(
                {
                    "reviewer": reviewer,
                    "input_path": str(path),
                    "input_sha256": input_report["sha256"],
                    "input_line": line,
                    "script_key": script_key,
                    "sequence": entry["sequence"],
                    "stable_id": stable_id,
                    "source_jp": entry["source_jp"],
                    "source_text_sha256": entry.get("source_text_sha256"),
                    "old_ko": record["old_ko"],
                    "old_ko_sha256": text_sha256(record["old_ko"]),
                    "new_ko": record["new_ko"],
                    "new_ko_sha256": text_sha256(record["new_ko"]),
                    "note": record.get("note"),
                    "runtime_protected_token_validation": "passed",
                }
            )

    working_masters = copy.deepcopy(masters)
    corrections_by_script: dict[str, list[dict[str, Any]]] = collections.defaultdict(list)
    for correction in validated_corrections:
        script_key = correction["script_key"]
        entry_index = correction["sequence"] - 1
        entry = working_masters[script_key]["entries"][entry_index]
        if entry["stable_id"] != correction["stable_id"] or entry["draft_ko"] != correction["old_ko"]:
            raise CorrectionError("internal correction exact guard failed before commit")
        entry["draft_ko"] = correction["new_ko"]
        entry["draft_ko_sha256"] = correction["new_ko_sha256"]
        entry["correction_status"] = "reviewer_correction_applied"
        history = entry.get("correction_history")
        if history is None:
            history = []
        if not isinstance(history, list):
            raise CorrectionError(f"{correction['stable_id']}: correction_history is not an array")
        history = copy.deepcopy(history)
        history.append(
            {
                "reviewer": correction["reviewer"],
                "input_path": correction["input_path"],
                "input_sha256": correction["input_sha256"],
                "input_line": correction["input_line"],
                "old_ko_sha256": correction["old_ko_sha256"],
                "new_ko_sha256": correction["new_ko_sha256"],
                "runtime_protected_token_validation": "passed",
            }
        )
        entry["correction_history"] = history
        corrections_by_script[script_key].append(correction)

    output_masters_dir = output_root / "masters"
    output_master_reports: list[dict[str, Any]] = []
    total_remaining_token_failed_records = 0
    for reference in master_refs:
        script_key = reference["script_key"]
        source_path = master_paths[script_key]
        output_path = output_masters_dir / source_path.name
        if path_key(output_path) == path_key(source_path):
            raise CorrectionError(f"refusing to overwrite source master: {source_path}")
        document = working_masters[script_key]
        remaining_findings = []
        for entry in document["entries"]:
            findings = token_validation_findings(entry, entry["draft_ko"])
            entry["hard_token_validation"] = {
                "passed": not findings,
                "findings": findings,
            }
            entry["structural_validation"] = (
                "passed" if not findings else "runtime_or_protected_token_findings_reported"
            )
            if findings:
                remaining_findings.append(
                    {
                        "stable_id": entry["stable_id"],
                        "sequence": entry["sequence"],
                        "findings": findings,
                    }
                )
        total_remaining_token_failed_records += len(remaining_findings)
        if isinstance(document.get("coverage"), dict):
            document["coverage"]["hard_token_failed_records"] = len(remaining_findings)
        document["runtime_and_protected_token_validation_pass"] = not remaining_findings
        document["correction_application"] = {
            "base_master_path": str(source_path),
            "base_master_sha256": input_master_hashes[script_key],
            "applied_corrections": len(corrections_by_script[script_key]),
            "remaining_runtime_or_protected_token_failed_records": len(remaining_findings),
            "translation_text_changed_only_by_explicit_jsonl": True,
        }
        write_json(output_path, document)
        reloaded = read_json(output_path)
        if reloaded != document:
            raise CorrectionError(f"{script_key}: corrected master JSON round trip failed")
        output_master_reports.append(
            {
                "script_key": script_key,
                "kind": (
                    "system_ui_strings"
                    if document.get("schema_version") == "fatal-twelve-system-ui-master-v1"
                    else "scenario"
                ),
                "path": str(output_path),
                "sha256": file_sha256(output_path),
                "records": len(document["entries"]),
                "applied_corrections": len(corrections_by_script[script_key]),
                "remaining_runtime_or_protected_token_failed_records": len(remaining_findings),
            }
        )

    for script_key, source_path in master_paths.items():
        if file_sha256(source_path) != input_master_hashes[script_key]:
            raise CorrectionError(f"source master changed during correction application: {source_path}")

    audit = {
        "schema_version": AUDIT_SCHEMA,
        "application_mode": "transactional working-copy only",
        "source_masters_modified": False,
        "exact_guard": ["stable_id", "old_ko"],
        "duplicate_correction_policy": "forbidden across all reviewer files",
        "new_target_validation": "runtime and protected tokens",
        "base_master_index": {"path": str(master_index_path), "sha256": file_sha256(master_index_path)},
        "review_group_manifest": {"path": str(review_groups_path), "sha256": review_groups_sha},
        "correction_inputs": correction_inputs,
        "summary": {
            "reviewer_files": len(correction_inputs),
            "masters": len(output_master_reports),
            "records": total_records,
            "corrections_applied": len(validated_corrections),
            "remaining_runtime_or_protected_token_failed_records": total_remaining_token_failed_records,
            "ready_for_final_render": total_remaining_token_failed_records == 0,
        },
        "corrections": validated_corrections,
        "output_masters": output_master_reports,
    }
    audit_path = output_root / "correction_audit.json"
    write_json(audit_path, audit)

    corrected_index = {
        "schema_version": CORRECTED_INDEX_SCHEMA,
        "base_master_index": {"path": str(master_index_path), "sha256": file_sha256(master_index_path)},
        "review_group_manifest": {"path": str(review_groups_path), "sha256": review_groups_sha},
        "correction_audit": {"path": str(audit_path), "sha256": file_sha256(audit_path)},
        "summary": {
            "scripts": len(output_master_reports),
            "records": total_records,
            "corrections_applied": len(validated_corrections),
            "remaining_runtime_or_protected_token_failed_records": total_remaining_token_failed_records,
            "ready_for_final_render": total_remaining_token_failed_records == 0,
            "source_masters_modified": False,
        },
        "masters": output_master_reports,
    }
    corrected_index_path = output_root / "corrected_master_index.json"
    write_json(corrected_index_path, corrected_index)
    result = {
        "corrected_master_index": str(corrected_index_path),
        "corrected_master_index_sha256": file_sha256(corrected_index_path),
        "correction_audit": str(audit_path),
        "correction_audit_sha256": file_sha256(audit_path),
        "output_root": str(output_root),
        "summary": corrected_index["summary"],
    }
    return result, 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--master-index", type=Path, default=here / "output" / "master_index.json")
    parser.add_argument("--review-groups", type=Path, default=here / "review_group_manifest.json")
    parser.add_argument(
        "--correction",
        action="append",
        default=[],
        metavar="REVIEWER=PATH",
        help="Reviewer-specific JSONL. Repeat once per reviewer with corrections.",
    )
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        result, exit_code = apply(args)
    except Exception as exc:
        print(json.dumps({"fatal_error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

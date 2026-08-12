#!/usr/bin/env python3
"""Export immutable master entries into fixed reviewer-group TSV context chunks.

The exporter is deliberately read-only with respect to master JSON and Korean
draft prose.  It validates assignment coverage and serialization round trips;
it does not review, normalize, or correct translations.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import math
import os
import re
import sys
from pathlib import Path
from typing import Any


MANIFEST_SCHEMA = "fatal-twelve-review-group-manifest-v1"
INDEX_SCHEMA = "fatal-twelve-review-packet-index-v1"
COVERAGE_SCHEMA = "fatal-twelve-review-packet-coverage-v1"
VARIABLE_RE = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")
TSV_COLUMNS = [
    "review_group",
    "chunk_id",
    "script_key",
    "sequence",
    "stable_id",
    "source_line",
    "lane",
    "speaker",
    "source_jp",
    "draft_ko",
    "protected_tokens",
    "source_text_sha256",
    "draft_ko_sha256",
]


class ExportError(ValueError):
    """Manifest, master, or export structure is invalid."""


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def text_sha256(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def expand_string(value: str, variables: dict[str, str]) -> str:
    result = value
    for _ in range(len(variables) + 2):
        updated = VARIABLE_RE.sub(lambda match: variables.get(match.group(1), match.group(0)), result)
        if updated == result:
            break
        result = updated
    unresolved = VARIABLE_RE.findall(result)
    if unresolved:
        raise ExportError(f"unresolved variables {unresolved!r} in {value!r}")
    return result


def expand_path(value: str, variables: dict[str, str]) -> Path:
    return Path(expand_string(value, variables))


def validate_group_manifest(manifest: dict[str, Any]) -> None:
    if manifest.get("schema_version") != MANIFEST_SCHEMA:
        raise ExportError("unsupported or missing review group manifest schema")
    expectations = manifest.get("expectations")
    groups = manifest.get("groups")
    policy = manifest.get("chunk_policy")
    if not isinstance(expectations, dict) or not isinstance(groups, list) or not isinstance(policy, dict):
        raise ExportError("manifest must contain expectations, chunk_policy, and groups")
    if len(groups) != expectations.get("group_count"):
        raise ExportError("reviewer group count does not match manifest expectation")
    group_ids = [group.get("group_id") for group in groups]
    if len(group_ids) != len(set(group_ids)) or not all(isinstance(value, str) and value for value in group_ids):
        raise ExportError("reviewer group IDs must be unique nonempty strings")

    script_keys: list[str] = []
    group_total = 0
    for group in groups:
        scripts = group.get("scripts")
        if not isinstance(scripts, list):
            raise ExportError(f"{group.get('group_id')}: scripts must be an array")
        calculated = 0
        for script in scripts:
            if not isinstance(script, dict):
                raise ExportError(f"{group.get('group_id')}: script assignment must be an object")
            key = script.get("script_key")
            count = script.get("expected_records")
            if not isinstance(key, str) or not key or not isinstance(count, int) or count <= 0:
                raise ExportError(f"{group.get('group_id')}: invalid script assignment")
            script_keys.append(key)
            calculated += count
        if calculated != group.get("expected_records"):
            raise ExportError(
                f"{group.get('group_id')}: assigned records {calculated} != expected {group.get('expected_records')}"
            )
        group_total += calculated
    if len(script_keys) != expectations.get("script_count"):
        raise ExportError("assigned script count does not match manifest expectation")
    if len(script_keys) != len(set(script_keys)):
        duplicates = sorted(key for key, count in collections.Counter(script_keys).items() if count > 1)
        raise ExportError(f"scripts assigned to more than one reviewer group: {duplicates}")
    if group_total != expectations.get("record_count"):
        raise ExportError("assigned record total does not match manifest expectation")

    for field in ("target_records", "minimum_records", "maximum_records"):
        if not isinstance(policy.get(field), int) or policy[field] <= 0:
            raise ExportError(f"chunk_policy.{field} must be a positive integer")
    if not policy["minimum_records"] <= policy["target_records"] <= policy["maximum_records"]:
        raise ExportError("chunk target must be within minimum and maximum")
    if policy.get("scope") != "per_script_contiguous_command_index":
        raise ExportError("only per-script contiguous command-index chunks are supported")
    if policy.get("cross_script_chunks") is not False:
        raise ExportError("cross-script chunks must remain disabled")


def choose_chunk_sizes(total: int, policy: dict[str, Any]) -> list[int]:
    minimum = policy["minimum_records"]
    maximum = policy["maximum_records"]
    target = policy["target_records"]
    if total <= maximum:
        return [total]
    least_chunks = math.ceil(total / maximum)
    most_chunks = total // minimum
    if least_chunks > most_chunks:
        raise ExportError(f"cannot split {total} records within [{minimum}, {maximum}]")
    chunk_count = min(
        range(least_chunks, most_chunks + 1),
        key=lambda count: (abs((total / count) - target), count),
    )
    base, remainder = divmod(total, chunk_count)
    sizes = [base + (1 if index < remainder else 0) for index in range(chunk_count)]
    if sum(sizes) != total or min(sizes) < minimum or max(sizes) > maximum:
        raise ExportError(f"invalid balanced chunk sizes for {total}: {sizes}")
    return sizes


def validate_master(
    *, script_key: str, expected_records: int, master_ref: dict[str, Any]
) -> tuple[dict[str, Any], Path]:
    path_value = master_ref.get("path")
    if not isinstance(path_value, str):
        raise ExportError(f"{script_key}: master index path is missing")
    path = Path(path_value)
    if not path.is_file():
        raise ExportError(f"{script_key}: master does not exist: {path}")
    expected_sha = master_ref.get("sha256")
    actual_sha = file_sha256(path)
    if expected_sha != actual_sha:
        raise ExportError(f"{script_key}: master SHA-256 mismatch")
    document = read_json(path)
    if not isinstance(document, dict) or document.get("script_key") != script_key:
        raise ExportError(f"{script_key}: invalid master document identity")
    entries = document.get("entries")
    if not isinstance(entries, list) or len(entries) != expected_records:
        raise ExportError(
            f"{script_key}: master entry count {len(entries) if isinstance(entries, list) else None} != {expected_records}"
        )
    if document.get("coverage_complete") is not True:
        raise ExportError(f"{script_key}: master coverage is not complete")
    if master_ref.get("selected_unique_records") != expected_records:
        raise ExportError(f"{script_key}: master index unique-record count mismatch")

    required = {
        "sequence",
        "stable_id",
        "source_line",
        "speaker",
        "source_jp",
        "draft_ko",
        "protected_tokens",
        "source_text_sha256",
        "draft_ko_sha256",
    }
    stable_ids: list[str] = []
    for position, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            raise ExportError(f"{script_key}:{position}: master entry must be an object")
        missing = sorted(required - entry.keys())
        if missing:
            raise ExportError(f"{script_key}:{position}: missing fields {missing}")
        if entry["sequence"] != position:
            raise ExportError(f"{script_key}:{position}: non-contiguous sequence {entry['sequence']}")
        if not isinstance(entry["stable_id"], str) or not entry["stable_id"]:
            raise ExportError(f"{script_key}:{position}: invalid stable_id")
        if not isinstance(entry["source_line"], int):
            raise ExportError(f"{script_key}:{position}: invalid source_line")
        if entry["speaker"] is not None and not isinstance(entry["speaker"], str):
            raise ExportError(f"{script_key}:{position}: invalid speaker")
        if not isinstance(entry["source_jp"], str) or not isinstance(entry["draft_ko"], str):
            raise ExportError(f"{script_key}:{position}: source_jp/draft_ko must be strings")
        if not isinstance(entry["protected_tokens"], list):
            raise ExportError(f"{script_key}:{position}: protected_tokens must be an array")
        if text_sha256(entry["source_jp"]) != entry["source_text_sha256"]:
            raise ExportError(f"{script_key}:{position}: source_jp SHA-256 mismatch")
        if text_sha256(entry["draft_ko"]) != entry["draft_ko_sha256"]:
            raise ExportError(f"{script_key}:{position}: draft_ko SHA-256 mismatch")
        stable_ids.append(entry["stable_id"])
    duplicates = [stable_id for stable_id, count in collections.Counter(stable_ids).items() if count > 1]
    if duplicates:
        raise ExportError(f"{script_key}: duplicate master stable IDs: {duplicates}")
    return document, path


def write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=TSV_COLUMNS,
            delimiter="\t",
            lineterminator="\n",
            quoting=csv.QUOTE_MINIMAL,
            extrasaction="raise",
        )
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if reader.fieldnames != TSV_COLUMNS:
            raise ExportError(f"{path}: TSV header mismatch")
        return list(reader)


def export(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    manifest_path = args.manifest.resolve()
    manifest = read_json(manifest_path)
    if not isinstance(manifest, dict):
        raise ExportError("review group manifest root must be an object")
    validate_group_manifest(manifest)
    variables = manifest.get("variables") or {}
    if not isinstance(variables, dict) or not all(
        isinstance(key, str) and isinstance(value, str) for key, value in variables.items()
    ):
        raise ExportError("variables must be a string-to-string object")

    master_index_path = (
        args.master_index.resolve()
        if args.master_index is not None
        else expand_path(manifest["master_index"], variables)
    )
    output_root = (
        args.output_root.resolve()
        if args.output_root is not None
        else expand_path(manifest["output_root"], variables)
    )
    if not master_index_path.is_file():
        raise ExportError(f"master index does not exist: {master_index_path}")
    master_index = read_json(master_index_path)
    if not isinstance(master_index, dict) or not isinstance(master_index.get("masters"), list):
        raise ExportError("invalid master index")
    expected = manifest["expectations"]
    if len(master_index["masters"]) != expected["script_count"]:
        raise ExportError("master index script count does not match reviewer manifest")
    if (master_index.get("summary") or {}).get("selected_unique_records") != expected["record_count"]:
        raise ExportError("master index record total does not match reviewer manifest")
    if (master_index.get("summary") or {}).get("coverage_complete") is not True:
        raise ExportError("master index coverage is not complete")
    master_refs = {item.get("script_key"): item for item in master_index["masters"]}

    assigned_script_keys = [
        script["script_key"] for group in manifest["groups"] for script in group["scripts"]
    ]
    missing_scripts = sorted(set(master_refs) - set(assigned_script_keys))
    unexpected_scripts = sorted(set(assigned_script_keys) - set(master_refs))
    if missing_scripts or unexpected_scripts:
        raise ExportError(
            f"reviewer/master script-set mismatch; unassigned={missing_scripts}, unknown={unexpected_scripts}"
        )

    masters: dict[str, tuple[dict[str, Any], Path]] = {}
    for group in manifest["groups"]:
        for script in group["scripts"]:
            key = script["script_key"]
            masters[key] = validate_master(
                script_key=key,
                expected_records=script["expected_records"],
                master_ref=master_refs[key],
            )

    output_root.mkdir(parents=True, exist_ok=True)
    policy = manifest["chunk_policy"]
    assignment_counts: collections.Counter[tuple[str, str]] = collections.Counter()
    global_stable_ids: set[str] = set()
    assignment_digest = hashlib.sha256()
    immutable_digest = hashlib.sha256()
    group_reports: list[dict[str, Any]] = []
    all_chunk_reports: list[dict[str, Any]] = []
    expected_tsv_paths: set[Path] = set()

    for group in manifest["groups"]:
        group_id = group["group_id"]
        group_dir = output_root / group_id
        group_chunks: list[dict[str, Any]] = []
        group_exported = 0
        for script_assignment in group["scripts"]:
            script_key = script_assignment["script_key"]
            master, master_path = masters[script_key]
            entries = master["entries"]
            sizes = choose_chunk_sizes(len(entries), policy)
            offset = 0
            for chunk_number, size in enumerate(sizes, 1):
                chunk_entries = entries[offset : offset + size]
                offset += size
                start_sequence = chunk_entries[0]["sequence"]
                end_sequence = chunk_entries[-1]["sequence"]
                if [entry["sequence"] for entry in chunk_entries] != list(
                    range(start_sequence, end_sequence + 1)
                ):
                    raise ExportError(f"{script_key}: chunk {chunk_number} is not sequence-contiguous")
                chunk_id = f"{group_id}-{script_key}-{chunk_number:03d}"
                filename = (
                    f"{group_id}__scenario_{script_key}__{start_sequence:04d}-{end_sequence:04d}"
                    f"__{size:03d}.tsv"
                )
                tsv_path = group_dir / filename
                expected_tsv_paths.add(tsv_path.resolve())
                rows: list[dict[str, Any]] = []
                for entry in chunk_entries:
                    assignment_key = (script_key, entry["stable_id"])
                    assignment_counts[assignment_key] += 1
                    if entry["stable_id"] in global_stable_ids:
                        raise ExportError(f"global stable_id assigned more than once: {entry['stable_id']}")
                    global_stable_ids.add(entry["stable_id"])
                    assignment_line = (
                        f"{group_id}\t{chunk_id}\t{script_key}\t{entry['sequence']}\t{entry['stable_id']}\n"
                    )
                    assignment_digest.update(assignment_line.encode("utf-8"))
                    immutable_digest.update(entry["stable_id"].encode("utf-8"))
                    immutable_digest.update(b"\0")
                    immutable_digest.update(entry["source_jp"].encode("utf-8"))
                    immutable_digest.update(b"\0")
                    immutable_digest.update(entry["draft_ko"].encode("utf-8"))
                    immutable_digest.update(b"\n")
                    rows.append(
                        {
                            "review_group": group_id,
                            "chunk_id": chunk_id,
                            "script_key": script_key,
                            "sequence": entry["sequence"],
                            "stable_id": entry["stable_id"],
                            "source_line": entry["source_line"],
                            "lane": entry.get("lane") or "",
                            "speaker": entry.get("speaker") or "",
                            "source_jp": entry["source_jp"],
                            "draft_ko": entry["draft_ko"],
                            "protected_tokens": canonical_json(entry["protected_tokens"]),
                            "source_text_sha256": entry["source_text_sha256"],
                            "draft_ko_sha256": entry["draft_ko_sha256"],
                        }
                    )
                write_tsv(tsv_path, rows)

                round_trip = read_tsv(tsv_path)
                if len(round_trip) != size:
                    raise ExportError(f"{tsv_path}: row-count round trip mismatch")
                for original, decoded in zip(chunk_entries, round_trip):
                    if int(decoded["sequence"]) != original["sequence"]:
                        raise ExportError(f"{tsv_path}: sequence round trip mismatch")
                    if decoded["stable_id"] != original["stable_id"]:
                        raise ExportError(f"{tsv_path}: stable_id round trip mismatch")
                    if int(decoded["source_line"]) != original["source_line"]:
                        raise ExportError(f"{tsv_path}: source_line round trip mismatch")
                    if decoded["speaker"] != (original.get("speaker") or ""):
                        raise ExportError(f"{tsv_path}: speaker round trip mismatch")
                    if decoded["source_jp"] != original["source_jp"]:
                        raise ExportError(f"{tsv_path}: source_jp round trip mismatch")
                    if decoded["draft_ko"] != original["draft_ko"]:
                        raise ExportError(f"{tsv_path}: draft_ko round trip mismatch")
                    if canonical_json(json.loads(decoded["protected_tokens"])) != canonical_json(
                        original["protected_tokens"]
                    ):
                        raise ExportError(f"{tsv_path}: protected_tokens round trip mismatch")

                chunk_report = {
                    "group_id": group_id,
                    "chunk_id": chunk_id,
                    "script_key": script_key,
                    "master_path": str(master_path),
                    "master_sha256": file_sha256(master_path),
                    "chunk_number": chunk_number,
                    "chunk_count_for_script": len(sizes),
                    "start_sequence": start_sequence,
                    "end_sequence": end_sequence,
                    "records": size,
                    "below_policy_minimum": size < policy["minimum_records"],
                    "short_script_exception": len(entries) < policy["minimum_records"],
                    "path": str(tsv_path),
                    "sha256": file_sha256(tsv_path),
                    "bytes": tsv_path.stat().st_size,
                    "round_trip_validation": "passed",
                }
                group_chunks.append(chunk_report)
                all_chunk_reports.append(chunk_report)
                group_exported += size
            if offset != len(entries):
                raise ExportError(f"{script_key}: chunk export did not consume every entry")
        if group_exported != group["expected_records"]:
            raise ExportError(
                f"{group_id}: exported records {group_exported} != expected {group['expected_records']}"
            )
        group_reports.append(
            {
                "group_id": group_id,
                "expected_records": group["expected_records"],
                "exported_records": group_exported,
                "script_count": len(group["scripts"]),
                "scripts": [script["script_key"] for script in group["scripts"]],
                "chunk_count": len(group_chunks),
                "chunks": group_chunks,
            }
        )

    expected_assignment_keys = {
        (script_key, entry["stable_id"])
        for script_key, (master, _) in masters.items()
        for entry in master["entries"]
    }
    actual_assignment_keys = set(assignment_counts)
    duplicate_assignments = sorted(
        [
            {"script_key": key[0], "stable_id": key[1], "assignments": count}
            for key, count in assignment_counts.items()
            if count != 1
        ],
        key=lambda item: (item["script_key"], item["stable_id"]),
    )
    missing_assignments = sorted(expected_assignment_keys - actual_assignment_keys)
    unexpected_assignments = sorted(actual_assignment_keys - expected_assignment_keys)
    exported_records = sum(report["exported_records"] for report in group_reports)
    if duplicate_assignments or missing_assignments or unexpected_assignments:
        raise ExportError("record-to-review-chunk assignment is not exactly one-to-one")
    if exported_records != expected["record_count"] or len(expected_assignment_keys) != expected["record_count"]:
        raise ExportError("exported or expected assignment total is not 18,184")

    existing_tsv_paths = {path.resolve() for path in output_root.glob("*/*.tsv")}
    stale_tsv_paths = sorted(str(path) for path in existing_tsv_paths - expected_tsv_paths)
    if stale_tsv_paths:
        raise ExportError(f"stale TSV packets exist outside this manifest run: {stale_tsv_paths}")

    chunk_sizes = [chunk["records"] for chunk in all_chunk_reports]
    short_chunks = [chunk for chunk in all_chunk_reports if chunk["short_script_exception"]]
    non_short_out_of_policy = [
        chunk
        for chunk in all_chunk_reports
        if not chunk["short_script_exception"]
        and not policy["minimum_records"] <= chunk["records"] <= policy["maximum_records"]
    ]
    if non_short_out_of_policy:
        raise ExportError("one or more non-short-script chunks violate the chunk size policy")

    coverage = {
        "schema_version": COVERAGE_SCHEMA,
        "validation_scope": "assignment and serialization only; translation review not performed",
        "translation_text_modified": False,
        "master_index": {"path": str(master_index_path), "sha256": file_sha256(master_index_path)},
        "review_group_manifest": {"path": str(manifest_path), "sha256": file_sha256(manifest_path)},
        "expected_groups": expected["group_count"],
        "exported_groups": len(group_reports),
        "expected_scripts": expected["script_count"],
        "exported_scripts": len(masters),
        "expected_records": expected["record_count"],
        "exported_records": exported_records,
        "unique_assignments": len(actual_assignment_keys),
        "missing_assignments": [
            {"script_key": script_key, "stable_id": stable_id}
            for script_key, stable_id in missing_assignments
        ],
        "unexpected_assignments": [
            {"script_key": script_key, "stable_id": stable_id}
            for script_key, stable_id in unexpected_assignments
        ],
        "duplicate_assignments": duplicate_assignments,
        "exactly_one_group_and_chunk_per_record": True,
        "continuous_sequence_chunks": True,
        "tsv_round_trip_validation": "passed",
        "source_jp_and_draft_ko_immutable": True,
        "assignment_sha256": assignment_digest.hexdigest(),
        "immutable_content_sha256": immutable_digest.hexdigest(),
        "chunk_policy": policy,
        "chunk_count": len(all_chunk_reports),
        "minimum_chunk_records": min(chunk_sizes),
        "maximum_chunk_records": max(chunk_sizes),
        "short_script_exception_chunks": len(short_chunks),
        "non_short_out_of_policy_chunks": len(non_short_out_of_policy),
        "groups": [
            {
                "group_id": report["group_id"],
                "expected_records": report["expected_records"],
                "exported_records": report["exported_records"],
                "script_count": report["script_count"],
                "chunk_count": report["chunk_count"],
            }
            for report in group_reports
        ],
    }
    coverage_path = output_root / "review_packet_coverage.json"
    write_json(coverage_path, coverage)

    packet_index = {
        "schema_version": INDEX_SCHEMA,
        "format": "RFC-style quoted TSV, UTF-8 with BOM",
        "columns": TSV_COLUMNS,
        "review_mode": "read-only first-draft context packets",
        "translation_review_performed": False,
        "translation_text_modified": False,
        "master_index": {"path": str(master_index_path), "sha256": file_sha256(master_index_path)},
        "review_group_manifest": {"path": str(manifest_path), "sha256": file_sha256(manifest_path)},
        "coverage": {"path": str(coverage_path), "sha256": file_sha256(coverage_path)},
        "summary": {
            "groups": len(group_reports),
            "scripts": len(masters),
            "records": exported_records,
            "chunks": len(all_chunk_reports),
            "exactly_one_group_and_chunk_per_record": True,
            "tsv_round_trip_validation": "passed",
            "source_jp_and_draft_ko_immutable": True,
        },
        "groups": group_reports,
    }
    index_path = output_root / "review_packet_index.json"
    write_json(index_path, packet_index)

    result = {
        "review_group_manifest": str(manifest_path),
        "review_group_manifest_sha256": file_sha256(manifest_path),
        "master_index": str(master_index_path),
        "master_index_sha256": file_sha256(master_index_path),
        "output_root": str(output_root),
        "review_packet_index": str(index_path),
        "review_packet_index_sha256": file_sha256(index_path),
        "review_packet_coverage": str(coverage_path),
        "review_packet_coverage_sha256": file_sha256(coverage_path),
        "summary": packet_index["summary"],
    }
    return result, 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    default_manifest = Path(__file__).with_name("review_group_manifest.json")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=default_manifest)
    parser.add_argument("--master-index", type=Path)
    parser.add_argument("--output-root", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        result, exit_code = export(args)
    except Exception as exc:
        print(json.dumps({"fatal_error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

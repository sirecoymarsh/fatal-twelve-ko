#!/usr/bin/env python3
"""Read-only helpers for reviewer A's Japanese-source QA pass.

This script never writes a master or translated RPY.  It can print compact
packet views, build deterministic candidate reports, and validate a guarded
correction JSONL against the exported TSV snapshots.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent
SCENARIO_PACKET_DIR = ROOT / "review_packets" / "A"
UI_PACKET_DIR = ROOT / "review_packets" / "A_UI"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def packet_paths(scope: str) -> list[Path]:
    directory = SCENARIO_PACKET_DIR if scope == "scenario" else UI_PACKET_DIR
    return sorted(directory.glob("*.tsv"))


def read_rows(scope: str, selected: str | None = None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    paths = packet_paths(scope)
    if selected:
        paths = [path for path in paths if selected in path.name]
    for path in paths:
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            for row in csv.DictReader(stream, delimiter="\t"):
                row["sequence"] = int(row["sequence"])
                row["_packet"] = path.name
                rows.append(row)
    return rows


def compact(scope: str, selected: str | None, start: int | None, end: int | None) -> None:
    rows = read_rows(scope, selected)
    for row in rows:
        sequence = row["sequence"]
        if start is not None and sequence < start:
            continue
        if end is not None and sequence > end:
            continue
        if scope == "scenario":
            prefix = f'{row["script_key"]}:{sequence:04d} L{row["source_line"]} [{row["speaker"] or row["lane"]}]'
        else:
            contexts = json.loads(row["contexts"])
            first = contexts[0] if contexts else {}
            prefix = (
                f'UI:{sequence:04d} {first.get("source_file", "?")}:'
                f'{first.get("source_line", "?")} [{first.get("lane", "?")}]'
            )
        print(prefix)
        print(f'  JP {row["source_jp"]}')
        print(f'  KO {row["draft_ko"]}')
        protected = json.loads(row["protected_tokens"])
        if protected:
            print(f'  TK {json.dumps(protected, ensure_ascii=False, separators=(",", ":"))}')


def scan(scope: str) -> None:
    rows = read_rows(scope)
    counts: collections.Counter[str] = collections.Counter()
    examples: dict[str, list[str]] = collections.defaultdict(list)
    kana = re.compile(r"[ぁ-ゖァ-ヺ]|")
    for row in rows:
        source = row["source_jp"]
        target = row["draft_ko"]
        tests = {
            "curly_quote": "“" in target or "”" in target,
            "ascii_quote": '"' in target,
            "identical_nonmechanical": source == target and any(ch.isalpha() for ch in source),
            "empty": not target,
            "jp_kana_residue": bool(re.search(r"[ぁ-ゖァ-ヺ]", target)),
            "question_marks_name": "???" in target or "？？？" in target,
        }
        for kind, matched in tests.items():
            if matched:
                counts[kind] += 1
                if len(examples[kind]) < 20:
                    examples[kind].append(
                        f'{row.get("script_key", "UI")}:{row["sequence"]} {source!r} => {target!r}'
                    )
    print(json.dumps({"records": len(rows), "counts": counts, "examples": examples}, ensure_ascii=False, indent=2))


def index_rows(scope: str) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for row in read_rows(scope):
        stable_id = row["stable_id"]
        if stable_id in index:
            raise ValueError(f"duplicate stable_id in {scope}: {stable_id}")
        index[stable_id] = row
    return index


def validate(scope: str, correction_path: Path) -> None:
    index = index_rows(scope)
    seen: set[str] = set()
    counts: collections.Counter[str] = collections.Counter()
    with correction_path.open("r", encoding="utf-8-sig") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            record = json.loads(line)
            stable_id = record.get("stable_id")
            if stable_id in seen:
                raise ValueError(f"line {line_number}: duplicate stable_id {stable_id}")
            seen.add(stable_id)
            if stable_id not in index:
                raise ValueError(f"line {line_number}: unknown stable_id {stable_id}")
            source = index[stable_id]
            if record.get("old_ko") != source["draft_ko"]:
                raise ValueError(f"line {line_number}: old_ko guard mismatch")
            if record.get("new_ko") == source["draft_ko"]:
                raise ValueError(f"line {line_number}: no-op correction")
            if "sequence" in record and record["sequence"] != source["sequence"]:
                raise ValueError(f"line {line_number}: sequence guard mismatch")
            if scope == "scenario" and "script_key" in record and record["script_key"] != source["script_key"]:
                raise ValueError(f"line {line_number}: script_key guard mismatch")
            counts[record.get("category", "unspecified")] += 1
    print(
        json.dumps(
            {
                "scope": scope,
                "checked_snapshot_records": len(index),
                "corrections": len(seen),
                "categories": counts,
                "correction_sha256": file_sha256(correction_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def inventory() -> None:
    result: dict[str, Any] = {}
    for scope in ("scenario", "ui"):
        paths = packet_paths(scope)
        rows = read_rows(scope)
        result[scope] = {
            "records": len(rows),
            "unique_stable_ids": len({row["stable_id"] for row in rows}),
            "packets": [
                {"name": path.name, "sha256": file_sha256(path), "bytes": path.stat().st_size}
                for path in paths
            ],
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    compact_parser = sub.add_parser("compact")
    compact_parser.add_argument("scope", choices=("scenario", "ui"))
    compact_parser.add_argument("--select")
    compact_parser.add_argument("--start", type=int)
    compact_parser.add_argument("--end", type=int)
    scan_parser = sub.add_parser("scan")
    scan_parser.add_argument("scope", choices=("scenario", "ui"))
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("scope", choices=("scenario", "ui"))
    validate_parser.add_argument("correction_path", type=Path)
    sub.add_parser("inventory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "compact":
        compact(args.scope, args.select, args.start, args.end)
    elif args.command == "scan":
        scan(args.scope)
    elif args.command == "validate":
        validate(args.scope, args.correction_path)
    elif args.command == "inventory":
        inventory()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

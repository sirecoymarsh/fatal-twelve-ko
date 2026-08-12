#!/usr/bin/env python3
"""Copy the Ren'Py launcher/runtime into a byte-verified isolated engine tree.

No executable is started.  The baseline game is snapshotted before and after
the copy, and both snapshots are persisted before a mismatch can abort the run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import stat
import sys
import uuid
from pathlib import Path, PurePosixPath
from typing import Iterable


CHUNK_SIZE = 1024 * 1024
COPY_FILES = ("fatal.exe", "fatal.py")
COPY_DIRECTORIES = ("lib", "renpy")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_reparse(path: Path) -> bool:
    metadata = path.lstat()
    attributes = getattr(metadata, "st_file_attributes", 0)
    return path.is_symlink() or bool(attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def assert_no_reparse_ancestry(path: Path) -> None:
    current = path.resolve(strict=False)
    while True:
        if current.exists() and is_reparse(current):
            raise ValueError(f"reparse-point ancestry rejected: {current}")
        parent = current.parent
        if parent == current:
            return
        current = parent


def overlap(first: Path, second: Path) -> bool:
    first = Path(os.path.normcase(first.resolve(strict=False)))
    second = Path(os.path.normcase(second.resolve(strict=False)))
    try:
        first.relative_to(second)
        return True
    except ValueError:
        pass
    try:
        second.relative_to(first)
        return True
    except ValueError:
        return False


def snapshot_tree(root: Path, label: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for directory, directory_names, file_names in os.walk(root, followlinks=False):
        directory_path = Path(directory)
        for name in list(directory_names):
            path = directory_path / name
            if is_reparse(path):
                raise ValueError(f"reparse point rejected in {label}: {path}")
        for name in file_names:
            path = directory_path / name
            if is_reparse(path):
                raise ValueError(f"reparse point rejected in {label}: {path}")
            relative = path.relative_to(root).as_posix()
            records.append(
                {
                    "path": relative,
                    "size": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
    records.sort(key=lambda item: str(item["path"]))
    folded: set[str] = set()
    for record in records:
        key = str(record["path"]).casefold()
        if key in folded:
            raise ValueError(f"case-colliding path in {label}: {record['path']}")
        folded.add(key)
    return records


def tree_digest(records: Iterable[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for record in sorted(records, key=lambda item: str(item["path"])):
        digest.update(
            f"{record['path']}\0{record['size']}\0{record['sha256']}\n".encode("utf-8")
        )
    return digest.hexdigest()


def diff_snapshots(
    before: list[dict[str, object]], after: list[dict[str, object]]
) -> list[dict[str, object]]:
    before_map = {str(record["path"]): record for record in before}
    after_map = {str(record["path"]): record for record in after}
    result: list[dict[str, object]] = []
    for path in sorted(before_map.keys() | after_map.keys()):
        left = before_map.get(path)
        right = after_map.get(path)
        if left is None:
            result.append({"path": path, "change": "added", "before": None, "after": right})
        elif right is None:
            result.append({"path": path, "change": "removed", "before": left, "after": None})
        elif left["size"] != right["size"] or left["sha256"] != right["sha256"]:
            result.append({"path": path, "change": "modified", "before": left, "after": right})
    return result


def write_json_atomic(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.incoming-{uuid.uuid4().hex}")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


def collect_copy_sources(baseline: Path) -> list[tuple[str, Path]]:
    result: list[tuple[str, Path]] = []
    for relative in COPY_FILES:
        source = baseline / relative
        if not source.is_file() or is_reparse(source):
            raise ValueError(f"required engine file missing or unsafe: {relative}")
        result.append((relative, source))
    for directory_relative in COPY_DIRECTORIES:
        directory = baseline / directory_relative
        if not directory.is_dir() or is_reparse(directory):
            raise ValueError(f"required engine directory missing or unsafe: {directory_relative}")
        for path in sorted(directory.rglob("*"), key=lambda item: item.as_posix()):
            if is_reparse(path):
                raise ValueError(f"engine source reparse point rejected: {path}")
            if path.is_file():
                result.append((path.relative_to(baseline).as_posix(), path))
    folded: set[str] = set()
    for relative, _ in result:
        key = relative.casefold()
        if key in folded:
            raise ValueError(f"case-colliding engine source path: {relative}")
        folded.add(key)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-game-root", required=True, type=Path)
    parser.add_argument("--engine-root", required=True, type=Path)
    parser.add_argument("--expected-baseline-tree-sha256", required=True)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    baseline = args.baseline_game_root.resolve(strict=True)
    engine = args.engine_root.resolve(strict=False)
    report = args.report.resolve(strict=False)
    if not baseline.is_dir():
        raise ValueError("baseline game root is not a directory")
    if engine.exists():
        raise ValueError("engine root must not already exist")
    if overlap(baseline, engine) or overlap(baseline, report) or overlap(engine, report):
        raise ValueError("baseline, isolated engine, and report paths must not overlap")
    assert_no_reparse_ancestry(baseline)
    assert_no_reparse_ancestry(engine.parent)
    assert_no_reparse_ancestry(report.parent)

    sources = collect_copy_sources(baseline)
    before = snapshot_tree(baseline, "baseline game before isolated engine copy")
    before_digest = tree_digest(before)
    if before_digest != args.expected_baseline_tree_sha256:
        raise ValueError("baseline full-tree SHA-256 differs from the trusted original audit")
    write_json_atomic(
        Path(str(report) + ".live_before.json"),
        {
            "schema_version": 1,
            "tree_label": "baseline_game_before_engine_copy",
            "file_count": len(before),
            "tree_sha256": before_digest,
            "files": before,
        },
    )

    incoming = engine.with_name(f"{engine.name}.incoming-{uuid.uuid4().hex}")
    incoming.mkdir(parents=True)
    engine_records: list[dict[str, object]] = []
    try:
        for relative, source in sources:
            destination = incoming.joinpath(*PurePosixPath(relative).parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            record = {
                "path": relative,
                "size": destination.stat().st_size,
                "sha256": sha256_file(destination),
                "mtime_ns": destination.stat().st_mtime_ns,
            }
            if record["size"] != source.stat().st_size or record["sha256"] != sha256_file(source):
                raise ValueError(f"copied engine byte verification failed: {relative}")
            engine_records.append(record)
        actual = snapshot_tree(incoming, "unpromoted isolated engine")
        expected_triplets = [
            {"path": item["path"], "size": item["size"], "sha256": item["sha256"]}
            for item in engine_records
        ]
        if actual != expected_triplets:
            raise ValueError("isolated engine exact file-set verification failed")
        engine.parent.mkdir(parents=True, exist_ok=True)
        incoming.replace(engine)
    except Exception:
        print(f"unpromoted engine evidence retained: {incoming}", file=sys.stderr)
        raise

    after = snapshot_tree(baseline, "baseline game after isolated engine copy")
    after_digest = tree_digest(after)
    differences = diff_snapshots(before, after)
    write_json_atomic(
        Path(str(report) + ".live_after.json"),
        {
            "schema_version": 1,
            "tree_label": "baseline_game_after_engine_copy",
            "file_count": len(after),
            "tree_sha256": after_digest,
            "files": after,
        },
    )
    write_json_atomic(
        Path(str(report) + ".live_diff.json"),
        {
            "schema_version": 1,
            "unchanged": not differences,
            "difference_count": len(differences),
            "differences": differences,
        },
    )
    if differences:
        raise ValueError("baseline game tree changed while preparing the isolated engine")

    engine_records.sort(key=lambda item: str(item["path"]))
    engine_digest = tree_digest(engine_records)
    result = {
        "schema_version": "fatal-twelve-isolated-engine-copy-v1",
        "status": "PASS",
        "operation": "copy_only",
        "process_started": False,
        "copy_allowlist": ["fatal.exe", "fatal.py", "lib/**", "renpy/**"],
        "engine_file_count": len(engine_records),
        "engine_tree_sha256": engine_digest,
        "engine_files": engine_records,
        "baseline_file_count": len(before),
        "baseline_tree_sha256": before_digest,
        "expected_baseline_tree_sha256": args.expected_baseline_tree_sha256,
        "baseline_unchanged": True,
    }
    write_json_atomic(report, result)
    print(f"ISOLATED ENGINE COPY PASS: {len(engine_records)} files")
    print(f"Engine tree SHA-256: {engine_digest}")
    print(f"Baseline tree SHA-256: {before_digest}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ISOLATED ENGINE COPY FAILED: {error}", file=sys.stderr)
        raise SystemExit(2)

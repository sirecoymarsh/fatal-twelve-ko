#!/usr/bin/env python3
"""Read-only byte inventory of an installed game against its original ZIP.

The report deliberately stores only logical labels and relative paths.  Absolute
host paths, drive letters, and user names are never serialized.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath
from typing import BinaryIO, Iterable


CHUNK_SIZE = 1024 * 1024


def sha256_stream(stream: BinaryIO) -> str:
    digest = hashlib.sha256()
    while True:
        chunk = stream.read(CHUNK_SIZE)
        if not chunk:
            return digest.hexdigest()
        digest.update(chunk)


def sha256_file(path: Path) -> str:
    with path.open("rb") as stream:
        return sha256_stream(stream)


def canonical_relative(value: str) -> str:
    value = value.replace("\\", "/")
    candidate = PurePosixPath(value)
    if (
        not value
        or value.startswith("/")
        or candidate.is_absolute()
        or any(part in ("", ".", "..") for part in candidate.parts)
        or ":" in value
    ):
        raise ValueError(f"unsafe relative path: {value!r}")
    return candidate.as_posix()


def digest_records(records: Iterable[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for record in sorted(records, key=lambda item: str(item["path"])):
        line = (
            f"{record['path']}\0{record['size']}\0{record['sha256']}\n"
        ).encode("utf-8")
        digest.update(line)
    return digest.hexdigest()


def inspect_live_tree(root: Path) -> tuple[dict[str, Path], list[str]]:
    files: dict[str, Path] = {}
    reparse_points: list[str] = []
    for directory, directory_names, file_names in os.walk(root, followlinks=False):
        directory_path = Path(directory)
        for name in list(directory_names):
            path = directory_path / name
            attrs = path.lstat().st_file_attributes if hasattr(path.lstat(), "st_file_attributes") else 0
            if path.is_symlink() or attrs & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                rel = path.relative_to(root).as_posix()
                reparse_points.append(rel)
                directory_names.remove(name)
        for name in file_names:
            path = directory_path / name
            attrs = path.lstat().st_file_attributes if hasattr(path.lstat(), "st_file_attributes") else 0
            rel = canonical_relative(path.relative_to(root).as_posix())
            if path.is_symlink() or attrs & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                reparse_points.append(rel)
                continue
            key = rel.casefold()
            if key in files:
                raise ValueError(f"case-colliding live paths: {files[key]} and {path}")
            files[key] = path
    return files, sorted(reparse_points)


def inspect_archive(
    archive: zipfile.ZipFile, prefix: str
) -> tuple[dict[str, tuple[str, zipfile.ZipInfo]], list[str]]:
    normalized_prefix = prefix.replace("\\", "/").strip("/") + "/"
    files: dict[str, tuple[str, zipfile.ZipInfo]] = {}
    rejected: list[str] = []
    for info in archive.infolist():
        name = info.filename.replace("\\", "/")
        if info.is_dir() or not name.startswith(normalized_prefix):
            continue
        raw_relative = name[len(normalized_prefix) :]
        try:
            relative = canonical_relative(raw_relative)
        except ValueError:
            rejected.append(raw_relative)
            continue
        mode = (info.external_attr >> 16) & 0xFFFF
        if stat.S_ISLNK(mode):
            rejected.append(relative)
            continue
        key = relative.casefold()
        if key in files:
            raise ValueError(
                f"case-colliding archive paths: {files[key][0]} and {relative}"
            )
        files[key] = (relative, info)
    return files, sorted(rejected)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--game-root", required=True, type=Path)
    parser.add_argument("--source-zip", required=True, type=Path)
    parser.add_argument("--zip-prefix", required=True)
    parser.add_argument("--restore-report", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    game_root = args.game_root.resolve(strict=True)
    source_zip = args.source_zip.resolve(strict=True)
    output = args.output.resolve(strict=False)
    if not game_root.is_dir() or not source_zip.is_file():
        raise SystemExit("game root or source ZIP is not a readable file system object")
    try:
        output.relative_to(game_root)
    except ValueError:
        pass
    else:
        raise SystemExit("output report must be outside the live game tree")

    restore_report: dict[str, object] = {}
    if args.restore_report:
        restore_report = json.loads(args.restore_report.read_text(encoding="utf-8"))

    live_files, live_reparse_points = inspect_live_tree(game_root)
    archive_size = source_zip.stat().st_size
    archive_sha256 = sha256_file(source_zip)

    original_records: list[dict[str, object]] = []
    live_common_records: list[dict[str, object]] = []
    missing: list[str] = []
    different: list[dict[str, object]] = []
    exact_paths: list[str] = []

    with zipfile.ZipFile(source_zip, "r") as archive:
        archive_files, archive_rejected = inspect_archive(archive, args.zip_prefix)
        if not archive_files:
            raise SystemExit("ZIP prefix contains no files")

        for key in sorted(archive_files):
            relative, info = archive_files[key]
            with archive.open(info, "r") as stream:
                original_sha = sha256_stream(stream)
            original_record = {
                "path": relative,
                "size": info.file_size,
                "sha256": original_sha,
            }
            original_records.append(original_record)
            live_path = live_files.get(key)
            if live_path is None:
                missing.append(relative)
                continue
            live_size = live_path.stat().st_size
            live_sha = sha256_file(live_path)
            live_common_records.append(
                {"path": relative, "size": live_size, "sha256": live_sha}
            )
            if live_size == info.file_size and live_sha == original_sha:
                exact_paths.append(relative)
            else:
                different.append(
                    {
                        "path": relative,
                        "original_size": info.file_size,
                        "original_sha256": original_sha,
                        "live_size": live_size,
                        "live_sha256": live_sha,
                    }
                )

        extras: list[dict[str, object]] = []
        for key in sorted(set(live_files) - set(archive_files)):
            path = live_files[key]
            relative = canonical_relative(path.relative_to(game_root).as_posix())
            extras.append(
                {
                    "path": relative,
                    "size": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )

        restoration_checks: list[dict[str, object]] = []
        for record in restore_report.get("files", []):
            relative = canonical_relative(str(record["path"]))
            key = relative.casefold()
            archive_entry = archive_files.get(key)
            live_path = live_files.get(key)
            if archive_entry is None or live_path is None:
                restoration_checks.append({"path": relative, "match": False})
                continue
            archive_relative, info = archive_entry
            with archive.open(info, "r") as stream:
                original_sha = sha256_stream(stream)
            live_sha = sha256_file(live_path)
            restoration_checks.append(
                {
                    "path": archive_relative,
                    "size": live_path.stat().st_size,
                    "sha256": live_sha,
                    "match": live_path.stat().st_size == info.file_size
                    and live_sha == original_sha,
                }
            )

    anchor_checks: list[dict[str, object]] = []
    for anchor in restore_report.get("anchors", []):
        relative = canonical_relative(str(anchor["path"]))
        live_path = live_files.get(relative.casefold())
        expected = str(anchor["expected"])
        actual = sha256_file(live_path) if live_path else None
        anchor_checks.append(
            {"path": relative, "expected_sha256": expected, "sha256": actual, "match": actual == expected}
        )

    restoration_match = all(item["match"] for item in restoration_checks)
    anchors_match = all(item["match"] for item in anchor_checks)
    report = {
        "schema_version": "fatal-twelve-live-original-zip-readonly-audit-v1",
        "status": "PASS" if restoration_match and anchors_match and not live_reparse_points else "FAIL",
        "operation": "read_only",
        "source_archive_label": "original_distribution_zip",
        "source_archive_size": archive_size,
        "source_archive_sha256": archive_sha256,
        "zip_prefix": args.zip_prefix.replace("\\", "/").strip("/") + "/",
        "original_file_count": len(original_records),
        "live_file_count": len(live_files),
        "common_file_count": len(live_common_records),
        "exact_original_file_count": len(exact_paths),
        "missing_original_file_count": len(missing),
        "different_original_file_count": len(different),
        "extra_live_file_count": len(extras),
        "full_tree_matches_archive": not missing and not different and not extras,
        "original_tree_sha256": digest_records(original_records),
        "live_common_tree_sha256": digest_records(live_common_records),
        "missing_original_files": missing,
        "different_original_files": different,
        "extra_live_files": extras,
        "archive_rejected_entries": archive_rejected,
        "live_reparse_points": live_reparse_points,
        "restoration_file_count": len(restoration_checks),
        "all_restoration_files_match_original": restoration_match,
        "restoration_files": restoration_checks,
        "anchor_count": len(anchor_checks),
        "all_anchors_match": anchors_match,
        "anchors": anchor_checks,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"{report['status']}: original={len(original_records)} exact={len(exact_paths)} "
        f"different={len(different)} missing={len(missing)} extras={len(extras)}"
    )
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

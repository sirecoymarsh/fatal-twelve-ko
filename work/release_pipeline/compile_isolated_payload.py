#!/usr/bin/env python3
"""Compile frozen Ren'Py sources with a fully isolated engine copy.

The trusted game tree is read only.  Exact full-tree snapshots are persisted
before and after the copied engine process runs.  Only explicitly allowlisted
``game/*.rpyc`` files are promoted to the clean payload directory.
"""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import uuid
from ctypes import wintypes
from pathlib import Path, PurePosixPath
from typing import Iterable


CHUNK_SIZE = 1024 * 1024


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"UTF-8 BOM rejected: {path.name}")
    value = json.loads(raw.decode("utf-8"), object_pairs_hook=reject_duplicate_keys)
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path.name}")
    return value


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
    first_text = os.path.normcase(str(first.resolve(strict=False)))
    second_text = os.path.normcase(str(second.resolve(strict=False)))
    try:
        os.path.commonpath((first_text, second_text))
    except ValueError:
        return False
    common = os.path.commonpath((first_text, second_text))
    return common == first_text or common == second_text


def canonical_relative(value: str) -> str:
    if not value or "\\" in value or ":" in value or value.startswith("/"):
        raise ValueError(f"unsafe relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise ValueError(f"unsafe relative path: {value!r}")
    result = path.as_posix()
    if result != value:
        raise ValueError(f"non-canonical relative path: {value!r}")
    return result


def safe_join(root: Path, relative: str) -> Path:
    relative = canonical_relative(relative)
    result = root.joinpath(*PurePosixPath(relative).parts).resolve(strict=False)
    try:
        result.relative_to(root.resolve(strict=True))
    except ValueError as error:
        raise ValueError(f"path escapes root: {relative}") from error
    return result


def snapshot_tree(root: Path, label: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for directory, directory_names, file_names in os.walk(root, followlinks=False):
        directory_path = Path(directory)
        for name in directory_names:
            path = directory_path / name
            if is_reparse(path):
                raise ValueError(f"reparse point rejected in {label}: {path}")
        for name in file_names:
            path = directory_path / name
            if is_reparse(path):
                raise ValueError(f"reparse point rejected in {label}: {path}")
            records.append(
                {
                    "path": path.relative_to(root).as_posix(),
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
    left = {str(record["path"]): record for record in before}
    right = {str(record["path"]): record for record in after}
    result: list[dict[str, object]] = []
    for path in sorted(left.keys() | right.keys()):
        before_record = left.get(path)
        after_record = right.get(path)
        if before_record is None:
            result.append({"path": path, "change": "added", "before": None, "after": after_record})
        elif after_record is None:
            result.append({"path": path, "change": "removed", "before": before_record, "after": None})
        elif (
            before_record["size"] != after_record["size"]
            or before_record["sha256"] != after_record["sha256"]
        ):
            result.append(
                {"path": path, "change": "modified", "before": before_record, "after": after_record}
            )
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


def process_paths_windows() -> list[tuple[int, str]]:
    if os.name != "nt":
        return []
    psapi = ctypes.WinDLL("psapi", use_last_error=True)
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    psapi.EnumProcesses.argtypes = [
        ctypes.POINTER(wintypes.DWORD), wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)
    ]
    psapi.EnumProcesses.restype = wintypes.BOOL
    kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    kernel32.OpenProcess.restype = wintypes.HANDLE
    kernel32.QueryFullProcessImageNameW.argtypes = [
        wintypes.HANDLE, wintypes.DWORD, wintypes.LPWSTR, ctypes.POINTER(wintypes.DWORD)
    ]
    kernel32.QueryFullProcessImageNameW.restype = wintypes.BOOL
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel32.CloseHandle.restype = wintypes.BOOL
    capacity = 4096
    process_ids = (wintypes.DWORD * capacity)()
    needed = wintypes.DWORD()
    if not psapi.EnumProcesses(process_ids, ctypes.sizeof(process_ids), ctypes.byref(needed)):
        raise OSError(ctypes.get_last_error(), "EnumProcesses failed")
    count = needed.value // ctypes.sizeof(wintypes.DWORD)
    result: list[tuple[int, str]] = []
    query_limited_information = 0x1000
    for process_id in process_ids[:count]:
        if not process_id:
            continue
        handle = kernel32.OpenProcess(query_limited_information, False, process_id)
        if not handle:
            continue
        try:
            size = wintypes.DWORD(32768)
            buffer = ctypes.create_unicode_buffer(size.value)
            if kernel32.QueryFullProcessImageNameW(handle, 0, buffer, ctypes.byref(size)):
                result.append((int(process_id), buffer.value))
        finally:
            kernel32.CloseHandle(handle)
    return result


def assert_process_not_running(executable: Path, label: str) -> None:
    expected = os.path.normcase(str(executable.resolve(strict=True)))
    for process_id, process_path in process_paths_windows():
        if os.path.normcase(os.path.abspath(process_path)) == expected:
            raise ValueError(f"exact {label} executable is running (PID {process_id})")


def verify_anchors(config: dict[str, object], root: Path, label: str) -> list[dict[str, object]]:
    game = config.get("game")
    if not isinstance(game, dict) or not isinstance(game.get("anchors"), list):
        raise ValueError("release config game anchors are invalid")
    result: list[dict[str, object]] = []
    for raw_anchor in game["anchors"]:
        if not isinstance(raw_anchor, dict) or not isinstance(raw_anchor.get("accepted"), list):
            raise ValueError("release config anchor is invalid")
        relative = canonical_relative(str(raw_anchor.get("path", "")))
        path = safe_join(root, relative)
        if not path.is_file() or is_reparse(path):
            raise ValueError(f"{label} anchor missing or unsafe: {relative}")
        size = path.stat().st_size
        digest = sha256_file(path)
        matched = any(
            isinstance(state, dict)
            and int(state.get("size", -1)) == size
            and str(state.get("sha256", "")) == digest
            for state in raw_anchor["accepted"]
        )
        if not matched:
            raise ValueError(f"{label} anchor hash rejected: {relative}")
        result.append({"path": relative, "size": size, "sha256": digest, "match": True})
    return result


def verify_engine_manifest(engine: Path, manifest_path: Path) -> tuple[list[dict[str, object]], str]:
    manifest = load_json(manifest_path)
    if (
        manifest.get("status") != "PASS"
        or manifest.get("operation") != "copy_only"
        or manifest.get("process_started") is not False
        or not isinstance(manifest.get("engine_files"), list)
    ):
        raise ValueError("isolated engine manifest provenance is invalid")
    expected: dict[str, dict[str, object]] = {}
    for raw_record in manifest["engine_files"]:
        if not isinstance(raw_record, dict):
            raise ValueError("isolated engine manifest record is invalid")
        relative = canonical_relative(str(raw_record.get("path", "")))
        if not (
            relative in ("fatal.exe", "fatal.py")
            or relative.startswith("lib/")
            or relative.startswith("renpy/")
        ):
            raise ValueError(f"engine manifest path outside explicit allowlist: {relative}")
        key = relative.casefold()
        if key in expected:
            raise ValueError(f"duplicate/case-colliding engine manifest path: {relative}")
        expected[key] = raw_record
        path = safe_join(engine, relative)
        if not path.is_file() or is_reparse(path):
            raise ValueError(f"isolated engine file missing or unsafe: {relative}")
        if path.stat().st_size != int(raw_record.get("size", -1)) or sha256_file(path) != str(
            raw_record.get("sha256", "")
        ):
            raise ValueError(f"isolated engine byte verification failed: {relative}")
    actual = snapshot_tree(engine, "isolated engine before compile")
    actual_keys = {str(record["path"]).casefold() for record in actual}
    if actual_keys != set(expected):
        raise ValueError("isolated engine exact file-set verification failed")
    digest = tree_digest(actual)
    if digest != manifest.get("engine_tree_sha256"):
        raise ValueError("isolated engine tree digest differs from its copy manifest")
    return actual, digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-game-root", required=True, type=Path)
    parser.add_argument("--engine-root", required=True, type=Path)
    parser.add_argument("--engine-manifest", required=True, type=Path)
    parser.add_argument("--expected-baseline-tree-sha256", required=True)
    parser.add_argument("--stage-root", required=True, type=Path)
    parser.add_argument("--release-config", required=True, type=Path)
    parser.add_argument("--clean-payload-root", required=True, type=Path)
    parser.add_argument("--compile-timeout-seconds", type=int, default=300)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    if args.compile_timeout_seconds < 1 or args.compile_timeout_seconds > 3600:
        raise ValueError("compile timeout must be in 1..3600 seconds")

    baseline = args.baseline_game_root.resolve(strict=True)
    engine = args.engine_root.resolve(strict=True)
    engine_manifest_path = args.engine_manifest.resolve(strict=True)
    stage = args.stage_root.resolve(strict=True)
    config_path = args.release_config.resolve(strict=True)
    payload = args.clean_payload_root.resolve(strict=False)
    report = args.report.resolve(strict=False)
    for directory in (baseline, engine, stage):
        if not directory.is_dir():
            raise ValueError(f"required directory missing: {directory.name}")
        assert_no_reparse_ancestry(directory)
    for path in (engine_manifest_path, config_path):
        if not path.is_file() or is_reparse(path):
            raise ValueError(f"required file missing or unsafe: {path.name}")
    roots = (baseline, engine, stage, payload)
    for index, first in enumerate(roots):
        for second in roots[index + 1 :]:
            if overlap(first, second):
                raise ValueError("baseline, engine, stage, and payload roots must be pairwise disjoint")
    if any(overlap(root, report) for root in roots):
        raise ValueError("report path must be outside protected roots")
    assert_no_reparse_ancestry(payload.parent)
    assert_no_reparse_ancestry(report.parent)
    if payload.exists() and (not payload.is_dir() or any(payload.iterdir())):
        raise ValueError("clean payload root must be absent or empty")

    config = load_json(config_path)
    entries = config.get("payload_allowlist")
    if not isinstance(entries, list) or not entries:
        raise ValueError("release config payload allowlist is empty or invalid")
    payload_paths: list[str] = []
    folded_payload: set[str] = set()
    for raw_entry in entries:
        if not isinstance(raw_entry, dict):
            raise ValueError("payload allowlist entry is invalid")
        relative = canonical_relative(str(raw_entry.get("path", "")))
        if not relative.startswith("game/") or not relative.lower().endswith(".rpyc"):
            raise ValueError(f"only compiled game/*.rpyc payload is allowed: {relative}")
        key = relative.casefold()
        if key in folded_payload:
            raise ValueError(f"duplicate/case-colliding payload path: {relative}")
        folded_payload.add(key)
        payload_paths.append(relative)
    payload_paths.sort()

    source_records: list[dict[str, object]] = []
    expected_sources: set[str] = set()
    for compiled_relative in payload_paths:
        source_relative = compiled_relative[:-1]
        source = safe_join(stage, source_relative)
        if not source.is_file() or is_reparse(source):
            raise ValueError(f"allowlisted compiled file has no safe staging source: {source_relative}")
        expected_sources.add(source_relative.casefold())
        source_records.append(
            {
                "path": source_relative,
                "size": source.stat().st_size,
                "sha256": sha256_file(source),
            }
        )
        stale = safe_join(stage, compiled_relative)
        if stale.exists():
            if not stale.is_file() or is_reparse(stale):
                raise ValueError(f"stale compiled target is unsafe: {compiled_relative}")
            stale.unlink()
    actual_sources = {
        path.relative_to(stage).as_posix().casefold()
        for path in stage.rglob("*")
        if path.is_file() and path.suffix.casefold() == ".rpy"
    }
    if actual_sources != expected_sources:
        raise ValueError("staging .rpy file-set differs from the explicit payload allowlist")
    stale_compiled = [path for path in stage.rglob("*") if path.is_file() and path.suffix.casefold() == ".rpyc"]
    if stale_compiled:
        raise ValueError("unexpected stale .rpyc remains in staging")

    anchors_before = verify_anchors(config, baseline, "baseline")
    engine_before, engine_before_digest = verify_engine_manifest(engine, engine_manifest_path)
    game_config = config.get("game")
    if not isinstance(game_config, dict):
        raise ValueError("release config game object is invalid")
    executable_relative = canonical_relative(str(game_config.get("process_executable_relative_path", "")))
    baseline_executable = safe_join(baseline, executable_relative)
    engine_executable = safe_join(engine, executable_relative)
    if sha256_file(engine_executable) != sha256_file(baseline_executable):
        raise ValueError("isolated executable differs from the trusted baseline executable")
    assert_process_not_running(baseline_executable, "baseline game")
    assert_process_not_running(engine_executable, "isolated engine")

    live_before = snapshot_tree(baseline, "baseline game before compile")
    live_before_digest = tree_digest(live_before)
    if live_before_digest != args.expected_baseline_tree_sha256:
        raise ValueError("baseline full-tree SHA-256 differs from the trusted original audit")
    write_json_atomic(
        Path(str(report) + ".live_before.json"),
        {
            "schema_version": 1,
            "tree_label": "baseline_game_before_compile",
            "file_count": len(live_before),
            "tree_sha256": live_before_digest,
            "files": live_before,
        },
    )

    environment = os.environ.copy()
    environment["SDL_AUDIODRIVER"] = "dummy"
    environment["PYTHONHASHSEED"] = "0"
    invocation_error: str | None = None
    exit_code = -1
    output = b""
    try:
        completed = subprocess.run(
            [str(engine_executable), str(stage), "compile", "--keep-orphan-rpyc"],
            cwd=stage,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=args.compile_timeout_seconds,
        )
        exit_code = completed.returncode
        output = completed.stdout
    except subprocess.TimeoutExpired as error:
        invocation_error = f"compile timed out after {args.compile_timeout_seconds} seconds"
        output = error.output or b""
    except OSError as error:
        invocation_error = str(error)
    Path(str(report) + ".compile.log").parent.mkdir(parents=True, exist_ok=True)
    Path(str(report) + ".compile.log").write_bytes(output)

    live_after = snapshot_tree(baseline, "baseline game after compile")
    live_after_digest = tree_digest(live_after)
    live_differences = diff_snapshots(live_before, live_after)
    write_json_atomic(
        Path(str(report) + ".live_after.json"),
        {
            "schema_version": 1,
            "tree_label": "baseline_game_after_compile",
            "file_count": len(live_after),
            "tree_sha256": live_after_digest,
            "files": live_after,
        },
    )
    write_json_atomic(
        Path(str(report) + ".live_diff.json"),
        {
            "schema_version": 1,
            "unchanged": not live_differences,
            "difference_count": len(live_differences),
            "differences": live_differences,
        },
    )
    engine_after = snapshot_tree(engine, "isolated engine after compile")
    engine_after_digest = tree_digest(engine_after)
    engine_differences = diff_snapshots(engine_before, engine_after)
    write_json_atomic(
        Path(str(report) + ".engine_diff.json"),
        {
            "schema_version": 1,
            "before_tree_sha256": engine_before_digest,
            "after_tree_sha256": engine_after_digest,
            "difference_count": len(engine_differences),
            "differences": engine_differences,
        },
    )
    if live_differences:
        raise ValueError("baseline game tree changed during isolated compile; persisted snapshots retained")
    anchors_after = verify_anchors(config, baseline, "post-compile baseline")
    assert_process_not_running(baseline_executable, "baseline game")
    assert_process_not_running(engine_executable, "isolated engine")
    if invocation_error is not None:
        raise ValueError(f"isolated Ren'Py compile invocation failed: {invocation_error}")
    if exit_code != 0:
        raise ValueError(f"isolated Ren'Py compile failed with exit code {exit_code}")

    for relative in ("errors.txt", "traceback.txt", "game/errors.txt", "game/traceback.txt"):
        artifact = safe_join(stage, relative)
        if artifact.is_file() and artifact.stat().st_size:
            raise ValueError(f"Ren'Py compile emitted an error artifact: {relative}")
    actual_compiled = {
        path.relative_to(stage).as_posix().casefold(): path.relative_to(stage).as_posix()
        for path in stage.rglob("*")
        if path.is_file() and path.suffix.casefold() == ".rpyc"
    }
    if set(actual_compiled) != folded_payload:
        raise ValueError("compiled staging .rpyc file-set differs from the explicit allowlist")

    incoming = payload.with_name(f"{payload.name}.incoming-{uuid.uuid4().hex}")
    incoming.mkdir(parents=True)
    payload_records: list[dict[str, object]] = []
    try:
        for relative in payload_paths:
            source = safe_join(stage, relative)
            destination = incoming.joinpath(*PurePosixPath(relative).parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            payload_records.append(
                {
                    "path": relative,
                    "size": destination.stat().st_size,
                    "sha256": sha256_file(destination),
                }
            )
        actual_payload = snapshot_tree(incoming, "clean compiled payload")
        if actual_payload != payload_records:
            raise ValueError("clean payload exact file-set verification failed")
        if payload.exists():
            payload.rmdir()
        incoming.replace(payload)
    except Exception:
        print(f"unpromoted payload evidence retained: {incoming}", file=sys.stderr)
        raise

    result = {
        "schema_version": "fatal-twelve-isolated-compile-payload-v2",
        "status": "PASS",
        "game_execution": False,
        "engine_compile": True,
        "engine_isolated": True,
        "audio_driver": "dummy",
        "python_hash_seed": "0",
        "live_tree_file_count": len(live_before),
        "live_tree_sha256": live_before_digest,
        "expected_live_tree_sha256": args.expected_baseline_tree_sha256,
        "live_tree_unchanged": True,
        "live_tree_difference_count": 0,
        "baseline_anchors_before": anchors_before,
        "baseline_anchors_after": anchors_after,
        "engine_manifest_sha256": sha256_file(engine_manifest_path),
        "engine_executable_sha256": sha256_file(engine_executable),
        "engine_tree_sha256_before": engine_before_digest,
        "engine_tree_sha256_after": engine_after_digest,
        "engine_changed_file_count": len(engine_differences),
        "engine_changed_files": engine_differences,
        "compile_exit_code": exit_code,
        "compile_log_sha256": sha256_file(Path(str(report) + ".compile.log")),
        "source_rpy_file_count": len(source_records),
        "source_rpy_files": source_records,
        "payload_file_count": len(payload_records),
        "payload_files": payload_records,
    }
    write_json_atomic(report, result)
    print(f"COMPILE/PAYLOAD PASS: {len(payload_records)} compiled .rpyc files")
    print(f"Live tree SHA-256: {live_before_digest}")
    print(f"Isolated engine changes: {len(engine_differences)} files")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, UnicodeError, json.JSONDecodeError) as error:
        print(f"COMPILE/PAYLOAD FAILED: {error}", file=sys.stderr)
        raise SystemExit(2)

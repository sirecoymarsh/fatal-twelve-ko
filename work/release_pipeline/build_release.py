#!/usr/bin/env python3
"""Build a deterministic, allowlist-only Fatal Twelve Korean patch ZIP.

The builder deliberately accepts only compiled ``.rpyc`` payload files.  It
never walks a game installation and it never copies a workspace wholesale.
All paths written to public artifacts are normalized relative paths.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


SCHEMA_VERSION = 1
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
PUBLIC_FILES = (
    "Install-KoreanPatch.ps1",
    "Restore-KoreanPatch.ps1",
    "PatchCore.psm1",
    "README_KO.txt",
)
TEXT_EXTENSIONS = {".json", ".txt", ".ps1", ".psm1", ".md", ".sha256"}
FORBIDDEN_PUBLIC_SUFFIXES = {
    ".rpy", ".py", ".pyc", ".pyo", ".log", ".bak", ".tmp", ".sav",
    ".save", ".png", ".jpg", ".jpeg", ".gif", ".dll", ".exe", ".msi",
    ".bat", ".cmd", ".7z", ".rar",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
PATCH_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")
VERSION_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
GENERIC_ABSOLUTE_RE = re.compile(
    rb"(?i)(?:[a-z]:[\\/](?:users|documents|temp|windows|program files|down|ai)[\\/]|"
    rb"\\\\[^\\\r\n]+[\\/][^\\\r\n]+[\\/])"
)


class BuildError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical_rel(value: str, *, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise BuildError(f"{field}: non-empty string required")
    if "\\" in value:
        raise BuildError(f"{field}: use '/' separators: {value!r}")
    p = PurePosixPath(value)
    if p.is_absolute() or value.startswith("/") or ":" in value:
        raise BuildError(f"{field}: absolute/drive path rejected: {value!r}")
    if any(part in ("", ".", "..") for part in p.parts):
        raise BuildError(f"{field}: non-canonical path rejected: {value!r}")
    result = p.as_posix()
    if result != value:
        raise BuildError(f"{field}: path must already be canonical: {value!r}")
    return result


def validate_hash_record(record: dict[str, Any], *, field: str) -> None:
    if type(record.get("size")) is not int or record["size"] < 0:
        raise BuildError(f"{field}.size: non-negative integer required")
    digest = record.get("sha256")
    if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
        raise BuildError(f"{field}.sha256: lowercase SHA-256 required")


def is_reparse_or_symlink(path: Path) -> bool:
    if path.is_symlink():
        return True
    try:
        attrs = os.lstat(path).st_file_attributes  # type: ignore[attr-defined]
    except (AttributeError, OSError):
        return False
    return bool(attrs & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def windows_streams(path: Path) -> list[str]:
    """Return non-default NTFS stream names; empty on non-Windows/filesystems."""
    if os.name != "nt":
        return []
    import ctypes
    from ctypes import wintypes

    class WIN32_FIND_STREAM_DATA(ctypes.Structure):
        _fields_ = [("StreamSize", ctypes.c_longlong), ("cStreamName", wintypes.WCHAR * 296)]

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    find_first = kernel32.FindFirstStreamW
    find_first.argtypes = [wintypes.LPCWSTR, wintypes.DWORD,
                           ctypes.POINTER(WIN32_FIND_STREAM_DATA), wintypes.DWORD]
    find_first.restype = wintypes.HANDLE
    find_next = kernel32.FindNextStreamW
    find_next.argtypes = [wintypes.HANDLE, ctypes.POINTER(WIN32_FIND_STREAM_DATA)]
    find_next.restype = wintypes.BOOL
    find_close = kernel32.FindClose
    find_close.argtypes = [wintypes.HANDLE]
    invalid = wintypes.HANDLE(-1).value
    data = WIN32_FIND_STREAM_DATA()
    handle = find_first(str(path), 0, ctypes.byref(data), 0)
    if handle == invalid:
        error = ctypes.get_last_error()
        if error in (1, 2, 38, 87):  # unsupported, absent, EOF, invalid parameter
            return []
        raise BuildError(f"cannot enumerate alternate streams for {path.name}: WinError {error}")
    names: list[str] = []
    try:
        while True:
            name = data.cStreamName
            if name and name != "::$DATA":
                names.append(name)
            if not find_next(handle, ctypes.byref(data)):
                error = ctypes.get_last_error()
                if error == 38:  # ERROR_HANDLE_EOF
                    break
                raise BuildError(f"cannot enumerate alternate streams for {path.name}: WinError {error}")
    finally:
        find_close(handle)
    return names


def enumerate_regular_files(root: Path) -> set[str]:
    if not root.is_dir():
        raise BuildError("payload root is not a directory")
    result: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        here = Path(dirpath)
        for name in list(dirnames):
            p = here / name
            if is_reparse_or_symlink(p):
                raise BuildError(f"payload reparse point/symlink rejected: {p.relative_to(root).as_posix()}")
        for name in filenames:
            p = here / name
            rel = p.relative_to(root).as_posix()
            if is_reparse_or_symlink(p) or not p.is_file():
                raise BuildError(f"payload non-regular file rejected: {rel}")
            streams = windows_streams(p)
            if streams:
                raise BuildError(f"payload alternate data stream rejected: {rel}: {streams}")
            result.add(rel)
    return result


def load_utf8_json(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raise BuildError("configuration must be UTF-8 without BOM")
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise BuildError(f"invalid UTF-8 JSON configuration: {e}") from e
    if not isinstance(data, dict):
        raise BuildError("configuration root must be an object")
    return data


def validate_config(config: dict[str, Any]) -> None:
    if set(config) != {
        "patch_id", "release_version", "release_root_name", "game",
        "payload_allowlist", "supported_prestate_profiles",
    }:
        raise BuildError("configuration keys do not match the exact schema")
    if not isinstance(config["patch_id"], str) or not PATCH_ID_RE.fullmatch(config["patch_id"]):
        raise BuildError("patch_id must be a short lowercase identifier")
    if not isinstance(config["release_version"], str) or not VERSION_RE.fullmatch(config["release_version"]):
        raise BuildError("release_version contains unsupported characters")
    root_name = config["release_root_name"]
    if not isinstance(root_name, str) or not VERSION_RE.fullmatch(root_name):
        raise BuildError("release_root_name must be a safe single directory name")

    game = config["game"]
    if not isinstance(game, dict) or set(game) != {"display_name", "process_executable_relative_path", "anchors"}:
        raise BuildError("game keys do not match the exact schema")
    if not isinstance(game["display_name"], str) or not game["display_name"].strip():
        raise BuildError("game.display_name is required")
    exe_rel = canonical_rel(game["process_executable_relative_path"], field="game.process_executable_relative_path")
    if not exe_rel.lower().endswith(".exe"):
        raise BuildError("process executable path must end in .exe")
    anchors = game["anchors"]
    if not isinstance(anchors, list) or not anchors:
        raise BuildError("at least one trusted game anchor is required")
    anchor_paths: set[str] = set()
    for i, anchor in enumerate(anchors):
        if not isinstance(anchor, dict) or set(anchor) != {"path", "accepted"}:
            raise BuildError(f"game.anchors[{i}] keys do not match schema")
        path = canonical_rel(anchor["path"], field=f"game.anchors[{i}].path")
        folded = path.casefold()
        if folded in anchor_paths:
            raise BuildError(f"duplicate anchor path: {path}")
        anchor_paths.add(folded)
        accepted = anchor["accepted"]
        if not isinstance(accepted, list) or not accepted:
            raise BuildError(f"game.anchors[{i}].accepted cannot be empty")
        seen_hashes: set[tuple[int, str]] = set()
        for j, item in enumerate(accepted):
            if not isinstance(item, dict) or set(item) != {"id", "size", "sha256"}:
                raise BuildError(f"anchor accepted record {i}/{j} keys do not match schema")
            if not isinstance(item["id"], str) or not PATCH_ID_RE.fullmatch(item["id"]):
                raise BuildError(f"anchor accepted id {i}/{j} is invalid")
            validate_hash_record(item, field=f"anchor[{i}].accepted[{j}]")
            sig = (item["size"], item["sha256"])
            if sig in seen_hashes:
                raise BuildError(f"duplicate accepted anchor signature for {path}")
            seen_hashes.add(sig)

    payload = config["payload_allowlist"]
    if not isinstance(payload, list) or not payload:
        raise BuildError("payload_allowlist cannot be empty")
    payload_paths: set[str] = set()
    state_ids_by_path: dict[str, set[str]] = {}
    for i, entry in enumerate(payload):
        if not isinstance(entry, dict) or set(entry) != {"path", "role", "pre_states"}:
            raise BuildError(f"payload_allowlist[{i}] keys do not match schema")
        path = canonical_rel(entry["path"], field=f"payload_allowlist[{i}].path")
        if not path.lower().endswith(".rpyc") or not path.startswith("game/"):
            raise BuildError(f"payload must be compiled game/*.rpyc only: {path}")
        folded = path.casefold()
        if folded in payload_paths:
            raise BuildError(f"duplicate/case-colliding payload path: {path}")
        if folded in anchor_paths:
            raise BuildError(f"payload path cannot also be a game anchor: {path}")
        payload_paths.add(folded)
        if not isinstance(entry["role"], str) or not entry["role"].strip():
            raise BuildError(f"payload role is required: {path}")
        states = entry["pre_states"]
        if not isinstance(states, list) or not states:
            raise BuildError(f"pre_states cannot be empty: {path}")
        ids: set[str] = set()
        signatures: set[tuple[str, int | None, str | None]] = set()
        for j, state_rec in enumerate(states):
            if not isinstance(state_rec, dict):
                raise BuildError(f"pre_state {i}/{j} must be an object")
            if state_rec.get("kind") == "absent":
                if set(state_rec) != {"id", "kind"}:
                    raise BuildError(f"absent pre_state {i}/{j} keys do not match schema")
                sig = ("absent", None, None)
            elif state_rec.get("kind") == "file":
                if set(state_rec) != {"id", "kind", "size", "sha256"}:
                    raise BuildError(f"file pre_state {i}/{j} keys do not match schema")
                validate_hash_record(state_rec, field=f"pre_state[{i}][{j}]")
                sig = ("file", state_rec["size"], state_rec["sha256"])
            else:
                raise BuildError(f"pre_state kind must be absent or file: {path}")
            sid = state_rec.get("id")
            if not isinstance(sid, str) or not PATCH_ID_RE.fullmatch(sid):
                raise BuildError(f"invalid pre_state id for {path}")
            if sid in ids or sig in signatures:
                raise BuildError(f"duplicate pre_state id or signature for {path}")
            ids.add(sid)
            signatures.add(sig)
        state_ids_by_path[path] = ids

    profiles = config["supported_prestate_profiles"]
    if not isinstance(profiles, list) or not profiles:
        raise BuildError("supported_prestate_profiles cannot be empty")
    profile_ids: set[str] = set()
    profile_sigs: set[tuple[tuple[str, str], ...]] = set()
    canonical_payload_paths = {entry["path"] for entry in payload}
    for i, profile in enumerate(profiles):
        if not isinstance(profile, dict) or set(profile) != {"id", "description", "states"}:
            raise BuildError(f"profile[{i}] keys do not match schema")
        pid = profile["id"]
        if not isinstance(pid, str) or not PATCH_ID_RE.fullmatch(pid) or pid in profile_ids:
            raise BuildError(f"invalid/duplicate profile id: {pid!r}")
        profile_ids.add(pid)
        if not isinstance(profile["description"], str) or not profile["description"].strip():
            raise BuildError(f"profile description is required: {pid}")
        states = profile["states"]
        if not isinstance(states, list) or len(states) != len(payload):
            raise BuildError(f"profile must identify every payload path exactly once: {pid}")
        seen: set[str] = set()
        sig_items: list[tuple[str, str]] = []
        for j, state_ref in enumerate(states):
            if not isinstance(state_ref, dict) or set(state_ref) != {"path", "state_id"}:
                raise BuildError(f"profile state {i}/{j} keys do not match schema")
            path = canonical_rel(state_ref["path"], field=f"profile[{i}].states[{j}].path")
            if path not in canonical_payload_paths or path in seen:
                raise BuildError(f"profile contains missing/duplicate/unknown path: {pid}: {path}")
            sid = state_ref["state_id"]
            if sid not in state_ids_by_path[path]:
                raise BuildError(f"profile references unknown state id: {pid}: {path}: {sid}")
            seen.add(path)
            sig_items.append((path, sid))
        sig = tuple(sorted(sig_items))
        if sig in profile_sigs:
            raise BuildError(f"duplicate supported profile mapping: {pid}")
        profile_sigs.add(sig)


def copy_public_file(source: Path, destination: Path) -> None:
    if not source.is_file() or is_reparse_or_symlink(source):
        raise BuildError(f"missing or unsafe public template: {source.name}")
    streams = windows_streams(source)
    if streams:
        raise BuildError(f"public template alternate data stream rejected: {source.name}: {streams}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


def public_file_record(root: Path, rel: str, *, role: str, origin: str) -> dict[str, Any]:
    path = root / PurePosixPath(rel)
    return {
        "path": rel,
        "role": role,
        "origin": origin,
        "size": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def scan_public_tree(root: Path, forbidden_needles: Iterable[bytes]) -> None:
    for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        suffix = path.suffix.lower()
        if rel.startswith("payload/"):
            if suffix != ".rpyc":
                raise BuildError(f"non-rpyc payload escaped allowlist: {rel}")
            continue
        if suffix in FORBIDDEN_PUBLIC_SUFFIXES:
            raise BuildError(f"forbidden public file type: {rel}")
        if suffix in TEXT_EXTENSIONS:
            data = path.read_bytes()
            if b"\x00" in data:
                raise BuildError(f"NUL byte in public text file: {rel}")
            if GENERIC_ABSOLUTE_RE.search(data):
                raise BuildError(f"absolute workstation path pattern in public file: {rel}")
            folded = data.lower()
            for needle in forbidden_needles:
                if needle and needle.lower() in folded:
                    raise BuildError(f"private build path/user token leaked into public file: {rel}")


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def write_deterministic_zip(root: Path, root_name: str, destination: Path) -> None:
    entries = sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix())
    destination.parent.mkdir(parents=True, exist_ok=True)
    tmp = destination.with_suffix(destination.suffix + ".tmp")
    if tmp.exists():
        tmp.unlink()
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in entries:
            rel = path.relative_to(root).as_posix()
            arcname = f"{root_name}/{rel}"
            info = zipfile.ZipInfo(arcname, FIXED_ZIP_TIME)
            info.create_system = 0
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0
            info.flag_bits |= 0x800  # UTF-8 names
            with path.open("rb") as f:
                zf.writestr(info, f.read(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    os.replace(tmp, destination)


def build(config_path: Path, payload_root: Path, output_dir: Path) -> dict[str, Any]:
    config = load_utf8_json(config_path)
    validate_config(config)
    expected_payload = {entry["path"] for entry in config["payload_allowlist"]}
    actual_payload = enumerate_regular_files(payload_root)
    if actual_payload != expected_payload:
        missing = sorted(expected_payload - actual_payload)
        unexpected = sorted(actual_payload - expected_payload)
        raise BuildError(f"payload tree differs from exact allowlist; missing={missing}; unexpected={unexpected}")

    script_root = Path(__file__).resolve().parent
    templates = script_root / "templates"
    output_dir.mkdir(parents=True, exist_ok=True)
    release_root_name = config["release_root_name"]
    staging_parent = Path(tempfile.mkdtemp(prefix="release-build-", dir=output_dir))
    staging = staging_parent / release_root_name
    staging.mkdir()
    try:
        for name in PUBLIC_FILES:
            copy_public_file(templates / name, staging / name)

        payload_records: list[dict[str, Any]] = []
        by_path = {entry["path"]: entry for entry in config["payload_allowlist"]}
        for rel in sorted(expected_payload):
            source = payload_root / PurePosixPath(rel)
            destination = staging / "payload" / PurePosixPath(rel)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            source_entry = by_path[rel]
            payload_records.append({
                "path": rel,
                "role": source_entry["role"],
                "origin": "compiled-korean-rpyc",
                "size": destination.stat().st_size,
                "sha256": sha256_file(destination),
                "pre_states": source_entry["pre_states"],
            })

        package_records = [
            public_file_record(staging, "Install-KoreanPatch.ps1", role="transactional-installer", origin="generated"),
            public_file_record(staging, "PatchCore.psm1", role="transaction-core", origin="generated"),
            public_file_record(staging, "README_KO.txt", role="public-instructions", origin="generated"),
            public_file_record(staging, "Restore-KoreanPatch.ps1", role="transactional-restorer", origin="generated"),
        ]
        for item in payload_records:
            package_records.append(public_file_record(
                staging, "payload/" + item["path"], role=item["role"], origin=item["origin"]
            ))
        package_records.sort(key=lambda item: item["path"])

        manifest = {
            "schema_version": SCHEMA_VERSION,
            "patch_id": config["patch_id"],
            "release_version": config["release_version"],
            "release_root_name": release_root_name,
            "game": config["game"],
            "payload": payload_records,
            "supported_prestate_profiles": config["supported_prestate_profiles"],
            "package_files": package_records,
            "integrity": {
                "algorithm": "SHA-256",
                "manifest_sidecar": "install_manifest.sha256",
                "zip_hash_is_external": True,
            },
        }
        manifest_path = staging / "install_manifest.json"
        manifest_path.write_bytes(json_bytes(manifest))
        manifest_digest = sha256_file(manifest_path)
        (staging / "install_manifest.sha256").write_text(
            f"{manifest_digest} *install_manifest.json\n", encoding="ascii", newline="\n"
        )

        forbidden_needles: list[bytes] = []
        for value in (str(config_path.resolve()), str(payload_root.resolve()), str(script_root.resolve()),
                      os.environ.get("USERNAME", ""), os.environ.get("USERPROFILE", "")):
            if value and len(value) >= 4:
                forbidden_needles.append(value.encode("utf-8", "ignore"))
        scan_public_tree(staging, forbidden_needles)

        expected_public = {item["path"] for item in package_records} | {
            "install_manifest.json", "install_manifest.sha256"
        }
        actual_public = {p.relative_to(staging).as_posix() for p in staging.rglob("*") if p.is_file()}
        if actual_public != expected_public:
            raise BuildError("staging tree differs from computed public allowlist")

        zip_name = f"{release_root_name}.zip"
        zip_path = output_dir / zip_name
        write_deterministic_zip(staging, release_root_name, zip_path)
        zip_digest = sha256_file(zip_path)
        sidecar = output_dir / f"{zip_name}.sha256"
        sidecar.write_text(f"{zip_digest} *{zip_name}\n", encoding="ascii", newline="\n")

        audit = {
            "schema_version": 1,
            "status": "PASS",
            "patch_id": config["patch_id"],
            "release_version": config["release_version"],
            "payload_file_count": len(payload_records),
            "public_file_count": len(expected_public),
            "manifest_sha256": manifest_digest,
            "zip_name": zip_name,
            "zip_size": zip_path.stat().st_size,
            "zip_sha256": zip_digest,
        }
        (output_dir / f"{release_root_name}.build_report.json").write_bytes(json_bytes(audit))
        return audit
    finally:
        shutil.rmtree(staging_parent, ignore_errors=True)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--payload-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        report = build(args.config, args.payload_root, args.output_dir)
    except BuildError as e:
        print(f"BUILD REJECTED: {e}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Exercise a final built patch ZIP against a minimal disposable baseline fixture.

The game executable is copied only as a hash anchor and is never launched.
Only installer/restorer PowerShell processes run, always with SDL audio disabled.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any


class FixtureError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def strict_json(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise FixtureError(f"UTF-8 BOM rejected: {path.name}")
    value = json.loads(raw.decode("utf-8"))
    if not isinstance(value, dict):
        raise FixtureError(f"JSON root is not an object: {path.name}")
    return value


def canonical_rel(value: str) -> str:
    if not value or "\\" in value or ":" in value:
        raise FixtureError(f"unsafe relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise FixtureError(f"unsafe relative path: {value!r}")
    return path.as_posix()


def safe_extract(zip_path: Path, destination: Path) -> Path:
    seen: set[str] = set()
    roots: set[str] = set()
    with zipfile.ZipFile(zip_path, "r") as archive:
        infos = archive.infolist()
        if not infos:
            raise FixtureError("release ZIP is empty")
        for info in infos:
            name = canonical_rel(info.filename.rstrip("/"))
            key = name.casefold()
            if key in seen:
                raise FixtureError(f"duplicate/case-colliding ZIP path: {name}")
            seen.add(key)
            roots.add(PurePosixPath(name).parts[0])
            if info.is_dir():
                continue
            target = destination.joinpath(*PurePosixPath(name).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info, "r") as source, target.open("xb") as output:
                shutil.copyfileobj(source, output)
    if len(roots) != 1:
        raise FixtureError(f"ZIP must have exactly one top-level directory: {sorted(roots)}")
    package = destination / next(iter(roots))
    if not package.is_dir():
        raise FixtureError("extracted package root is missing")
    return package


def verify_zip_sidecar(zip_path: Path) -> str:
    sidecar = zip_path.with_name(zip_path.name + ".sha256")
    if not sidecar.is_file():
        raise FixtureError("external ZIP SHA-256 sidecar is missing")
    text = sidecar.read_text(encoding="ascii")
    match = re.fullmatch(r"([0-9a-f]{64}) \*([^\r\n]+)\r?\n?", text)
    if not match or match.group(2) != zip_path.name:
        raise FixtureError("external ZIP SHA-256 sidecar format/name mismatch")
    actual = sha256_file(zip_path)
    if actual != match.group(1):
        raise FixtureError("final ZIP SHA-256 mismatch")
    return actual


def verify_extracted_package(package: Path) -> tuple[dict[str, Any], str]:
    manifest_path = package / "install_manifest.json"
    manifest_hash_path = package / "install_manifest.sha256"
    match = re.fullmatch(
        r"([0-9a-f]{64}) \*install_manifest\.json\r?\n?",
        manifest_hash_path.read_text(encoding="ascii"),
    )
    if not match:
        raise FixtureError("extracted manifest sidecar is invalid")
    digest = sha256_file(manifest_path)
    if digest != match.group(1):
        raise FixtureError("extracted manifest hash mismatch")
    manifest = strict_json(manifest_path)
    expected = {record["path"] for record in manifest["package_files"]} | {
        "install_manifest.json", "install_manifest.sha256"
    }
    actual = {path.relative_to(package).as_posix() for path in package.rglob("*") if path.is_file()}
    if actual != expected:
        raise FixtureError(f"extracted package file set mismatch: missing={sorted(expected-actual)}, unexpected={sorted(actual-expected)}")
    for record in manifest["package_files"]:
        rel = canonical_rel(record["path"])
        path = package.joinpath(*PurePosixPath(rel).parts)
        if path.stat().st_size != record["size"] or sha256_file(path) != record["sha256"]:
            raise FixtureError(f"extracted package file hash mismatch: {rel}")
    return manifest, digest


def powershell_exe() -> Path:
    path = Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32" / "WindowsPowerShell" / "v1.0" / "powershell.exe"
    if not path.is_file():
        raise FixtureError("Windows PowerShell 5.1 is unavailable")
    return path


def child_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment["SDL_AUDIODRIVER"] = "dummy"
    return environment


def invoke(script: Path, game: Path, external: Path, *extra: str,
           success: bool = True, timeout: int = 180) -> subprocess.CompletedProcess[str]:
    command = [
        str(powershell_exe()), "-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
        "-File", str(script), "-GameRoot", str(game),
        "-BackupRoot", str(external / "backups"), "-StateRoot", str(external / "state"),
        "-RecoveryRoot", str(external / "recovery"), *extra,
    ]
    result = subprocess.run(command, text=True, encoding="utf-8", errors="replace",
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=child_environment(), timeout=timeout)
    if success and result.returncode != 0:
        raise FixtureError(f"PowerShell command failed:\n{result.stdout}\n{result.stderr}")
    if not success and result.returncode == 0:
        raise FixtureError(f"PowerShell command unexpectedly succeeded:\n{result.stdout}")
    return result


def snapshot(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256_file(path)
        for path in sorted(root.rglob("*")) if path.is_file()
    }


def assert_no_temps(game: Path) -> None:
    leftovers = [
        path.relative_to(game).as_posix() for path in game.rglob("*")
        if path.is_file() and ".fatal12ko-" in path.name
    ]
    if leftovers:
        raise FixtureError(f"transaction temp files remain: {leftovers}")


def match_hash_record(path: Path, records: list[dict[str, Any]], label: str) -> dict[str, Any]:
    if not path.is_file():
        raise FixtureError(f"baseline file missing: {label}")
    size, digest = path.stat().st_size, sha256_file(path)
    matches = [record for record in records if record["size"] == size and record["sha256"] == digest]
    if len(matches) != 1:
        raise FixtureError(f"baseline hash rejected: {label}: {digest}")
    return matches[0]


def prepare_minimal_fixture(baseline: Path, fixture: Path, manifest: dict[str, Any], profile_id: str) -> tuple[dict[str, str], dict[str, str]]:
    if fixture.exists():
        shutil.rmtree(fixture)
    fixture.mkdir(parents=True)
    baseline_tracked: dict[str, str] = {}
    for anchor in manifest["game"]["anchors"]:
        rel = canonical_rel(anchor["path"])
        source = baseline.joinpath(*PurePosixPath(rel).parts)
        match_hash_record(source, list(anchor["accepted"]), rel)
        baseline_tracked[rel] = sha256_file(source)
        target = fixture.joinpath(*PurePosixPath(rel).parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    profiles = [profile for profile in manifest["supported_prestate_profiles"] if profile["id"] == profile_id]
    if len(profiles) != 1:
        raise FixtureError(f"profile id is missing/ambiguous: {profile_id}")
    payload_map = {entry["path"]: entry for entry in manifest["payload"]}
    for ref in profiles[0]["states"]:
        rel = canonical_rel(ref["path"])
        entry = payload_map[rel]
        states = [state for state in entry["pre_states"] if state["id"] == ref["state_id"]]
        if len(states) != 1:
            raise FixtureError(f"profile references unknown state: {rel}/{ref['state_id']}")
        state = states[0]
        source = baseline.joinpath(*PurePosixPath(rel).parts)
        if state["kind"] == "absent":
            if source.exists():
                raise FixtureError(f"baseline target should be absent for profile {profile_id}: {rel}")
        elif state["kind"] == "file":
            match_hash_record(source, [state], rel)
            baseline_tracked[rel] = sha256_file(source)
            target = fixture.joinpath(*PurePosixPath(rel).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        else:
            raise FixtureError(f"unsupported pre-state kind: {rel}")
    return snapshot(fixture), baseline_tracked


def verify_baseline_unchanged(baseline: Path, tracked: dict[str, str]) -> None:
    for rel, expected in tracked.items():
        path = baseline.joinpath(*PurePosixPath(rel).parts)
        if not path.is_file() or sha256_file(path) != expected:
            raise FixtureError(f"read-only baseline changed: {rel}")


def verify_installed(game: Path, package: Path, manifest: dict[str, Any]) -> None:
    for entry in manifest["payload"]:
        rel = canonical_rel(entry["path"])
        target = game.joinpath(*PurePosixPath(rel).parts)
        packaged = package.joinpath("payload", *PurePosixPath(rel).parts)
        if not target.is_file() or target.stat().st_size != entry["size"] or sha256_file(target) != entry["sha256"]:
            raise FixtureError(f"installed payload hash mismatch: {rel}")
        if target.read_bytes() != packaged.read_bytes():
            raise FixtureError(f"installed payload bytes differ from extracted package: {rel}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--baseline-game", required=True, type=Path)
    parser.add_argument("--work-root", required=True, type=Path)
    parser.add_argument("--profile-id", default="trusted-pristine")
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args(argv)

    zip_path = args.zip.resolve(strict=True)
    baseline = args.baseline_game.resolve(strict=True)
    work = args.work_root.resolve()
    if work == baseline or work.is_relative_to(baseline) or baseline.is_relative_to(work):
        raise FixtureError("work root and read-only baseline game tree must not overlap")
    if work.exists() and any(work.iterdir()):
        raise FixtureError("work root must be absent or empty")
    work.mkdir(parents=True, exist_ok=True)
    zip_digest = verify_zip_sidecar(zip_path)
    package = safe_extract(zip_path, work / "Unicode 압축 해제 Ω")
    manifest, manifest_digest = verify_extracted_package(package)
    game = work / "Unicode 게임 fixture Ω"
    original_snapshot, tracked_baseline = prepare_minimal_fixture(baseline, game, manifest, args.profile_id)
    install = package / "Install-KoreanPatch.ps1"
    restore = package / "Restore-KoreanPatch.ps1"
    tests: list[str] = []

    external = work / "external pristine"
    invoke(install, game, external)
    verify_installed(game, package, manifest)
    invoke(install, game, external)
    verify_installed(game, package, manifest)
    invoke(restore, game, external)
    if snapshot(game) != original_snapshot:
        raise FixtureError("final payload pristine restore is not byte-exact")
    invoke(restore, game, external)
    if snapshot(game) != original_snapshot:
        raise FixtureError("final payload idempotent restore changed the fixture")
    assert_no_temps(game)
    tests.append("pristine_install_idempotent_restore")

    tampered_package = work / "tampered package"
    shutil.copytree(package, tampered_package)
    first_rel = canonical_rel(manifest["payload"][0]["path"])
    victim = tampered_package.joinpath("payload", *PurePosixPath(first_rel).parts)
    raw = bytearray(victim.read_bytes())
    raw[0] ^= 0x55
    victim.write_bytes(raw)
    invoke(tampered_package / "Install-KoreanPatch.ps1", game, work / "external payload tamper", success=False)
    if snapshot(game) != original_snapshot:
        raise FixtureError("tampered final payload changed fixture before rejection")
    tests.append("tampered_payload_prewrite_rejection")

    unknown = game.joinpath(*PurePosixPath(first_rel).parts)
    unknown.parent.mkdir(parents=True, exist_ok=True)
    unknown_original = unknown.read_bytes() if unknown.exists() else None
    unknown.write_bytes(b"unknown baseline state\n")
    tampered_snapshot = snapshot(game)
    unknown_external = work / "external baseline tamper"
    invoke(install, game, unknown_external, success=False)
    if snapshot(game) != tampered_snapshot or unknown_external.exists():
        raise FixtureError("unknown final target state was not rejected before external/game writes")
    if unknown_original is None:
        unknown.unlink()
    else:
        unknown.write_bytes(unknown_original)
    tests.append("tampered_baseline_prewrite_rejection")

    failure_external = work / "external nth failure"
    invoke(install, game, failure_external, "-TestFailAfterReplacement", "1", success=False)
    if snapshot(game) != original_snapshot:
        raise FixtureError("final payload Nth replacement rollback is not byte-exact")
    assert_no_temps(game)
    tests.append("nth_replacement_verified_rollback")

    interrupt_external = work / "external interruption"
    signal = work / "중단 신호.txt"
    command = [
        str(powershell_exe()), "-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
        "-File", str(install), "-GameRoot", str(game),
        "-BackupRoot", str(interrupt_external / "backups"), "-StateRoot", str(interrupt_external / "state"),
        "-RecoveryRoot", str(interrupt_external / "recovery"), "-TestPauseAfterReplacement", "1",
        "-TestPauseSignalPath", str(signal),
    ]
    process = subprocess.Popen(command, env=child_environment(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    deadline = time.monotonic() + 90
    while time.monotonic() < deadline and not signal.exists() and process.poll() is None:
        time.sleep(0.1)
    if not signal.exists():
        stdout, stderr = process.communicate(timeout=10)
        raise FixtureError(f"final interruption point was not reached: {process.returncode}: {stdout!r}: {stderr!r}")
    process.kill()
    process.wait(timeout=10)
    invoke(install, game, interrupt_external)
    verify_installed(game, package, manifest)
    invoke(restore, game, interrupt_external)
    if snapshot(game) != original_snapshot:
        raise FixtureError("final interrupted transaction recovery/restore is not byte-exact")
    assert_no_temps(game)
    tests.append("forced_interruption_journal_recovery")

    recovery_external = work / "external recovery tamper"
    invoke(install, game, recovery_external)
    installed_snapshot = snapshot(game)
    recovery_files = list((recovery_external / "recovery" / manifest["patch_id"]).rglob("*.rpyc"))
    if not recovery_files:
        raise FixtureError("final recovery copies were not created")
    recovery_victim = recovery_files[0]
    raw = bytearray(recovery_victim.read_bytes())
    raw[0] ^= 0x23
    recovery_victim.write_bytes(raw)
    invoke(restore, game, recovery_external, success=False)
    if snapshot(game) != installed_snapshot:
        raise FixtureError("tampered recovery copy caused a restore write")
    recovery_rel = recovery_victim.relative_to(next((recovery_external / "recovery" / manifest["patch_id"]).iterdir())).as_posix()
    source = package.joinpath("payload", *PurePosixPath(recovery_rel).parts)
    shutil.copyfile(source, recovery_victim)
    invoke(restore, game, recovery_external)
    if snapshot(game) != original_snapshot:
        raise FixtureError("final recovery-copy repair did not restore byte-exactly")
    tests.append("tampered_recovery_prewrite_rejection")

    verify_baseline_unchanged(baseline, tracked_baseline)
    version_result = subprocess.run(
        [str(powershell_exe()), "-NoLogo", "-NoProfile", "-NonInteractive", "-Command", "$PSVersionTable.PSVersion.ToString()"],
        text=True, encoding="utf-8", errors="replace", stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env=child_environment(), timeout=30,
    )
    if version_result.returncode != 0 or not version_result.stdout.strip().startswith("5.1"):
        raise FixtureError("final fixture did not run under Windows PowerShell 5.1")
    report = {
        "schema_version": 1,
        "status": "PASS",
        "game_execution": False,
        "audio_driver": "dummy",
        "baseline_unchanged": True,
        "powershell_version": version_result.stdout.strip(),
        "zip_name": zip_path.name,
        "zip_sha256": zip_digest,
        "manifest_sha256": manifest_digest,
        "payload_file_count": len(manifest["payload"]),
        "profile_id": args.profile_id,
        "tests": [{"name": name, "status": "PASS"} for name in tests],
        "passed": len(tests),
        "failed": 0,
    }
    output = args.report.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FixtureError, OSError, UnicodeError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"FINAL FIXTURE FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)

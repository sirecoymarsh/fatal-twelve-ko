#!/usr/bin/env python3
"""Windows PowerShell 5.1 fixture matrix for the release pipeline.

This suite uses inert synthetic bytes only.  It never launches Fatal Twelve and
never reads or writes the user's game installation.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import zipfile
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
PIPELINE = HERE.parent
RUN_ROOT = PIPELINE / "test_runs" / "유니코드 경로 Ω"
BUILD_ROOT = RUN_ROOT / "빌드 결과"
PAYLOAD_ROOT = RUN_ROOT / "컴파일 산출물"
CONFIG_PATH = RUN_ROOT / "synthetic_config.json"
PATCH_ID = "fatal-twelve-ko-fixture"
RELEASE_ROOT_NAME = "FatalTwelve_KoreanPatch_fixture"
TARGETS = {
    "game/tl/korean/f12_slot.rpyc": b"compiled Korean slot fixture\x00\x01\x02\n",
    "game/tl/korean/scenario/scenario001.rpyc": b"compiled Korean scenario fixture\x10\x11\x12\n",
}
ORIGINALS = {
    "game/tl/korean/f12_slot.rpyc": b"known original slot fixture\x20\x21\n",
    "game/tl/korean/scenario/scenario001.rpyc": b"known original scenario fixture\x30\x31\n",
}
PROCESS_FIXTURE_BYTES = (Path(os.environ.get("SystemRoot", r"C:\Windows")) / "System32" / "ping.exe").read_bytes()
ANCHORS = {
    # A copied Windows utility is used only to test canonical process-path handling.
    # It is never included in the public package and is not the game executable.
    "fatal.exe": PROCESS_FIXTURE_BYTES,
    "game/scenario.rpa": b"inert trusted scenario archive anchor\n",
}


class TestFailure(RuntimeError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write_bytes(root: Path, rel: str, data: bytes) -> None:
    path = root.joinpath(*rel.split("/"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def tree_snapshot(root: Path) -> dict[str, str]:
    if not root.exists():
        return {}
    return {
        p.relative_to(root).as_posix(): file_digest(p)
        for p in sorted(root.rglob("*")) if p.is_file()
    }


def assert_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise TestFailure(f"{label}: expected {expected!r}, got {actual!r}")


def assert_true(value: bool, label: str) -> None:
    if not value:
        raise TestFailure(label)


def make_config() -> dict[str, Any]:
    payload_allowlist = []
    for rel, patched in TARGETS.items():
        original = ORIGINALS[rel]
        payload_allowlist.append({
            "path": rel,
            "role": "compiled Korean fixture",
            "pre_states": [
                {"id": "absent", "kind": "absent"},
                {"id": "original", "kind": "file", "size": len(original), "sha256": digest(original)},
                {"id": "patched", "kind": "file", "size": len(patched), "sha256": digest(patched)},
            ],
        })
    paths = list(TARGETS)
    profiles = [
        {
            "id": "pristine-original",
            "description": "Every synthetic target is the known original.",
            "states": [{"path": p, "state_id": "original"} for p in paths],
        },
        {
            "id": "pristine-absent",
            "description": "Every additive target is absent.",
            "states": [{"path": p, "state_id": "absent"} for p in paths],
        },
        {
            "id": "known-mixed",
            "description": "The first target is original and the second is already patched.",
            "states": [
                {"path": paths[0], "state_id": "original"},
                {"path": paths[1], "state_id": "patched"},
            ],
        },
        {
            "id": "already-patched",
            "description": "Every target already equals this exact release.",
            "states": [{"path": p, "state_id": "patched"} for p in paths],
        },
    ]
    return {
        "patch_id": PATCH_ID,
        "release_version": "fixture-1",
        "release_root_name": RELEASE_ROOT_NAME,
        "game": {
            "display_name": "Fatal Twelve synthetic fixture",
            "process_executable_relative_path": "fatal.exe",
            "anchors": [
                {
                    "path": rel,
                    "accepted": [{"id": "fixture", "size": len(data), "sha256": digest(data)}],
                }
                for rel, data in ANCHORS.items()
            ],
        },
        "payload_allowlist": payload_allowlist,
        "supported_prestate_profiles": profiles,
    }


def powershell_exe() -> Path:
    system_root = Path(os.environ.get("SystemRoot", r"C:\Windows"))
    path = system_root / "System32" / "WindowsPowerShell" / "v1.0" / "powershell.exe"
    if not path.is_file():
        raise TestFailure("Windows PowerShell 5.1 executable was not found")
    return path


def powershell_version() -> str:
    environment = os.environ.copy()
    environment["SDL_AUDIODRIVER"] = "dummy"
    result = subprocess.run(
        [str(powershell_exe()), "-NoLogo", "-NoProfile", "-NonInteractive", "-Command",
         "$PSVersionTable.PSVersion.ToString()"],
        text=True, encoding="utf-8", errors="replace", env=environment,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30,
    )
    if result.returncode != 0:
        raise TestFailure(f"cannot query Windows PowerShell version: {result.stderr}")
    version = result.stdout.strip()
    if not version.startswith("5.1"):
        raise TestFailure(f"fixture must run under Windows PowerShell 5.1, found {version!r}")
    return version


def invoke_script(script: Path, game: Path, external: Path, *extra: str,
                  expect_success: bool = True, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    command = [
        str(powershell_exe()), "-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
        "-File", str(script), "-GameRoot", str(game),
        "-BackupRoot", str(external / "backups"),
        "-StateRoot", str(external / "state"),
        "-RecoveryRoot", str(external / "recovery"),
        *extra,
    ]
    environment = os.environ.copy()
    environment["SDL_AUDIODRIVER"] = "dummy"
    result = subprocess.run(command, text=True, encoding="utf-8", errors="replace", env=environment,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    if expect_success and result.returncode != 0:
        raise TestFailure(f"PowerShell command failed ({result.returncode}):\nSTDOUT={result.stdout}\nSTDERR={result.stderr}")
    if not expect_success and result.returncode == 0:
        raise TestFailure(f"PowerShell command unexpectedly succeeded:\n{result.stdout}")
    return result


def prepare_game(root: Path, profile: str) -> Path:
    game = root / "게임 폴더"
    for rel, data in ANCHORS.items():
        write_bytes(game, rel, data)
    paths = list(TARGETS)
    if profile == "original":
        for rel, data in ORIGINALS.items():
            write_bytes(game, rel, data)
    elif profile == "absent":
        pass
    elif profile == "mixed":
        write_bytes(game, paths[0], ORIGINALS[paths[0]])
        write_bytes(game, paths[1], TARGETS[paths[1]])
    elif profile == "patched":
        for rel, data in TARGETS.items():
            write_bytes(game, rel, data)
    else:
        raise ValueError(profile)
    return game


def assert_targets(game: Path, expected: dict[str, bytes]) -> None:
    for rel, data in expected.items():
        path = game.joinpath(*rel.split("/"))
        assert_true(path.is_file(), f"target exists: {rel}")
        assert_equal(path.read_bytes(), data, f"target bytes: {rel}")


def assert_no_transaction_temps(game: Path) -> None:
    leftovers = [
        p.relative_to(game).as_posix() for p in game.rglob("*") if p.is_file()
        and (p.name.endswith(".incoming") or p.name.endswith(".replace-backup") or ".fatal12ko-" in p.name)
    ]
    assert_equal(leftovers, [], "no game-tree transaction temp files")


def extract_package(zip_path: Path, root: Path) -> Path:
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(root)
    package = root / RELEASE_ROOT_NAME
    assert_true(package.is_dir(), "deterministic ZIP root extracted")
    return package


def new_case(name: str, package_zip: Path, profile: str = "original") -> tuple[Path, Path, Path]:
    root = RUN_ROOT / "fixtures" / name
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    package = extract_package(package_zip, root / "압축 해제")
    game = prepare_game(root, profile)
    external = root / "외부 상태"
    return package, game, external


def run_matrix(package_zip: Path) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []

    def case(name: str, function) -> None:
        started = time.monotonic()
        function()
        results.append({"name": name, "status": "PASS", "seconds": round(time.monotonic() - started, 3)})

    def pristine_idempotent() -> None:
        package, game, external = new_case("01 pristine idempotent", package_zip)
        before = tree_snapshot(game)
        install = package / "Install-KoreanPatch.ps1"
        restore = package / "Restore-KoreanPatch.ps1"
        invoke_script(install, game, external)
        assert_targets(game, TARGETS)
        invoke_script(install, game, external)
        assert_targets(game, TARGETS)
        invoke_script(restore, game, external)
        assert_equal(tree_snapshot(game), before, "pristine byte-exact restore")
        invoke_script(restore, game, external)
        assert_equal(tree_snapshot(game), before, "idempotent second restore")
        assert_no_transaction_temps(game)

    def additive_absent() -> None:
        package, game, external = new_case("02 absent additive", package_zip, "absent")
        before = tree_snapshot(game)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external)
        assert_targets(game, TARGETS)
        invoke_script(package / "Restore-KoreanPatch.ps1", game, external)
        assert_equal(tree_snapshot(game), before, "absent targets removed on exact restore")
        assert_no_transaction_temps(game)

    def supported_mixed() -> None:
        package, game, external = new_case("03 supported mixed", package_zip, "mixed")
        before = tree_snapshot(game)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external)
        assert_targets(game, TARGETS)
        invoke_script(package / "Restore-KoreanPatch.ps1", game, external)
        assert_equal(tree_snapshot(game), before, "mixed state exact restore")
        assert_no_transaction_temps(game)

    def tampered_payload() -> None:
        package, game, external = new_case("04 payload tamper", package_zip)
        before = tree_snapshot(game)
        victim = package.joinpath("payload", *next(iter(TARGETS)).split("/"))
        raw = bytearray(victim.read_bytes())
        raw[0] ^= 0x5A
        victim.write_bytes(raw)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external, expect_success=False)
        assert_equal(tree_snapshot(game), before, "tampered payload rejected before game write")
        assert_true(not external.exists(), "tampered payload rejected before backup/state/recovery write")

    def tampered_baseline() -> None:
        package, game, external = new_case("05 baseline tamper", package_zip)
        before = tree_snapshot(game)
        victim = game.joinpath(*next(iter(TARGETS)).split("/"))
        victim.write_bytes(b"unknown target baseline\n")
        tampered = tree_snapshot(game)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external, expect_success=False)
        assert_equal(tree_snapshot(game), tampered, "unknown baseline rejected before game write")
        assert_true(not external.exists(), "unknown baseline rejected before backup/state/recovery write")
        assert_true(before != tampered, "baseline test fixture was actually tampered")

    def tampered_anchor() -> None:
        package, game, external = new_case("05b anchor tamper", package_zip)
        victim = game / "game" / "scenario.rpa"
        raw = bytearray(victim.read_bytes())
        raw[0] ^= 0x7F
        victim.write_bytes(raw)
        before = tree_snapshot(game)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external, expect_success=False)
        assert_equal(tree_snapshot(game), before, "tampered trusted anchor rejected before game write")
        assert_true(not external.exists(), "tampered trusted anchor rejected before external write")

    def unsupported_mixture() -> None:
        package, game, external = new_case("05c unsupported mixture", package_zip)
        paths = list(TARGETS)
        write_bytes(game, paths[0], TARGETS[paths[0]])
        write_bytes(game, paths[1], ORIGINALS[paths[1]])
        before = tree_snapshot(game)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external, expect_success=False)
        assert_equal(tree_snapshot(game), before, "unsupported cross-product mixture rejected")
        assert_true(not external.exists(), "unsupported mixture rejected before external write")

    def unexpected_package_file() -> None:
        package, game, external = new_case("05d unexpected package file", package_zip)
        (package / "unexpected.txt").write_text("not allowlisted\n", encoding="utf-8")
        before = tree_snapshot(game)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external, expect_success=False)
        assert_equal(tree_snapshot(game), before, "unexpected package file rejected before game write")
        assert_true(not external.exists(), "unexpected package file rejected before external write")

    def tampered_backup() -> None:
        package, game, external = new_case("06 backup tamper", package_zip)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external)
        before_restore = tree_snapshot(game)
        backup_files = [p for p in (external / "backups" / PATCH_ID).rglob("*.rpyc")]
        assert_true(bool(backup_files), "backup fixture files exist")
        raw = bytearray(backup_files[0].read_bytes())
        raw[0] ^= 0x33
        backup_files[0].write_bytes(raw)
        invoke_script(package / "Restore-KoreanPatch.ps1", game, external, expect_success=False)
        assert_equal(tree_snapshot(game), before_restore, "tampered backup rejected before restore write")
        assert_no_transaction_temps(game)

    def tampered_state_path() -> None:
        package, game, external = new_case("06b state path tamper", package_zip)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external)
        unrelated = game / "game" / "unrelated.txt"
        unrelated.write_text("must survive\n", encoding="utf-8")
        before = tree_snapshot(game)
        state_path = external / "state" / PATCH_ID / "installed.json"
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["entries"][0]["replacement_backup_path"] = str(unrelated)
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        invoke_script(package / "Restore-KoreanPatch.ps1", game, external, expect_success=False)
        assert_equal(tree_snapshot(game), before, "tampered state path rejected before restore write")
        assert_equal(unrelated.read_text(encoding="utf-8"), "must survive\n", "tampered state cannot delete unrelated file")

    def nth_failure() -> None:
        package, game, external = new_case("07 Nth failure", package_zip)
        before = tree_snapshot(game)
        invoke_script(package / "Install-KoreanPatch.ps1", game, external,
                      "-TestFailAfterReplacement", "1", expect_success=False)
        assert_equal(tree_snapshot(game), before, "Nth replacement failure rolled back byte-exactly")
        state = external / "state" / PATCH_ID
        assert_true(not (state / "installed.json").exists(), "Nth failure leaves no installed state")
        assert_true(not (state / "in_progress.json").exists(), "Nth failure leaves no stale journal after verified rollback")
        assert_no_transaction_temps(game)

    def forced_interruption() -> None:
        package, game, external = new_case("08 forced interruption", package_zip)
        before = tree_snapshot(game)
        signal = RUN_ROOT / "pause 신호.txt"
        if signal.exists():
            signal.unlink()
        command = [
            str(powershell_exe()), "-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
            "-File", str(package / "Install-KoreanPatch.ps1"), "-GameRoot", str(game),
            "-BackupRoot", str(external / "backups"), "-StateRoot", str(external / "state"),
            "-RecoveryRoot", str(external / "recovery"), "-TestPauseAfterReplacement", "1",
            "-TestPauseSignalPath", str(signal),
        ]
        environment = os.environ.copy()
        environment["SDL_AUDIODRIVER"] = "dummy"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment)
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline and not signal.exists() and process.poll() is None:
            time.sleep(0.1)
        if not signal.exists():
            stdout, stderr = process.communicate(timeout=5)
            raise TestFailure(f"interruption pause was not reached: rc={process.returncode}; out={stdout!r}; err={stderr!r}")
        process.kill()
        process.wait(timeout=10)
        journal = external / "state" / PATCH_ID / "in_progress.json"
        assert_true(journal.is_file(), "forced interruption preserved in-progress journal")
        invoke_script(package / "Install-KoreanPatch.ps1", game, external)
        assert_targets(game, TARGETS)
        invoke_script(package / "Restore-KoreanPatch.ps1", game, external)
        assert_equal(tree_snapshot(game), before, "journal recovery then restore is byte-exact")
        assert_true(not journal.exists(), "recovered interruption journal removed")
        assert_no_transaction_temps(game)

    def unicode_and_clean_tree() -> None:
        package, game, external = new_case("09 한글 및 공백 Ω", package_zip)
        result = invoke_script(package / "Install-KoreanPatch.ps1", game, external)
        assert_true("INSTALL PASS" in result.stdout, "PowerShell 5.1 Unicode-path install reports PASS")
        result = invoke_script(package / "Restore-KoreanPatch.ps1", game, external)
        assert_true("RESTORE PASS" in result.stdout, "PowerShell 5.1 Unicode-path restore reports PASS")
        assert_no_transaction_temps(game)

    def canonical_process_path() -> None:
        package, game, external = new_case("10 process canonical path", package_zip)
        environment = os.environ.copy()
        environment["SDL_AUDIODRIVER"] = "dummy"
        flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
        other = RUN_ROOT / "다른 폴더" / "fatal.exe"
        other.parent.mkdir(parents=True, exist_ok=True)
        other.write_bytes(PROCESS_FIXTURE_BYTES)
        different = subprocess.Popen([str(other), "127.0.0.1", "-n", "30"], env=environment,
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=flags)
        try:
            time.sleep(0.25)
            assert_true(different.poll() is None, "same-name different-path fixture process is running")
            invoke_script(package / "Install-KoreanPatch.ps1", game, external)
        finally:
            different.kill()
            different.wait(timeout=10)
        invoke_script(package / "Restore-KoreanPatch.ps1", game, external)

        package, game, external = new_case("10b exact process canonical path", package_zip)
        exact = subprocess.Popen([str(game / "fatal.exe"), "127.0.0.1", "-n", "30"], env=environment,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=flags)
        try:
            time.sleep(0.25)
            assert_true(exact.poll() is None, "exact target-path fixture process is running")
            before = tree_snapshot(game)
            invoke_script(package / "Install-KoreanPatch.ps1", game, external, expect_success=False)
            assert_equal(tree_snapshot(game), before, "exact target process blocks before game write")
            assert_true(not external.exists(), "exact target process blocks before external write")
        finally:
            exact.kill()
            exact.wait(timeout=10)

    for name, function in (
        ("pristine_install_restore_and_idempotency", pristine_idempotent),
        ("additive_absent_install_restore", additive_absent),
        ("explicit_supported_mixed_state", supported_mixed),
        ("tampered_payload_prewrite_rejection", tampered_payload),
        ("tampered_game_baseline_prewrite_rejection", tampered_baseline),
        ("tampered_trusted_anchor_prewrite_rejection", tampered_anchor),
        ("unsupported_mixture_prewrite_rejection", unsupported_mixture),
        ("unexpected_package_file_prewrite_rejection", unexpected_package_file),
        ("tampered_backup_prewrite_rejection", tampered_backup),
        ("tampered_state_path_prewrite_rejection", tampered_state_path),
        ("nth_replacement_failure_verified_rollback", nth_failure),
        ("forced_interruption_journal_recovery", forced_interruption),
        ("unicode_spaces_windows_powershell_5_1", unicode_and_clean_tree),
        ("canonical_process_path_same_name_and_exact_target", canonical_process_path),
    ):
        case(name, function)
    return results


def main() -> int:
    if RUN_ROOT.exists():
        shutil.rmtree(RUN_ROOT)
    PAYLOAD_ROOT.mkdir(parents=True)
    for rel, data in TARGETS.items():
        write_bytes(PAYLOAD_ROOT, rel, data)
    CONFIG_PATH.write_text(json.dumps(make_config(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    build_a = BUILD_ROOT / "A"
    build_b = BUILD_ROOT / "B"
    for destination in (build_a, build_b):
        command = [sys.executable, str(PIPELINE / "build_release.py"), "--config", str(CONFIG_PATH),
                   "--payload-root", str(PAYLOAD_ROOT), "--output-dir", str(destination)]
        environment = os.environ.copy()
        environment["SDL_AUDIODRIVER"] = "dummy"
        result = subprocess.run(command, text=True, encoding="utf-8", errors="replace", env=environment,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise TestFailure(f"deterministic builder failed:\n{result.stdout}\n{result.stderr}")
    zip_a = build_a / f"{RELEASE_ROOT_NAME}.zip"
    zip_b = build_b / f"{RELEASE_ROOT_NAME}.zip"
    assert_equal(file_digest(zip_a), file_digest(zip_b), "two clean builds are byte-identical")
    sidecar_text = (build_a / f"{RELEASE_ROOT_NAME}.zip.sha256").read_text(encoding="ascii")
    assert_equal(sidecar_text, f"{file_digest(zip_a)} *{RELEASE_ROOT_NAME}.zip\n", "external ZIP hash sidecar")

    with zipfile.ZipFile(zip_a, "r") as zf:
        names = zf.namelist()
        assert_true(all(name.startswith(RELEASE_ROOT_NAME + "/") for name in names), "ZIP uses one safe root")
        assert_true(all(not name.lower().endswith(".rpy") for name in names), "ZIP excludes Ren'Py source")
        assert_true(all(".." not in Path(name).parts for name in names), "ZIP paths do not escape")
        public_text = b"".join(zf.read(name) for name in names if Path(name).suffix.lower() in {".json", ".txt", ".ps1", ".psm1", ".sha256"})
        for forbidden in (str(PIPELINE).encode("utf-8"), os.environ.get("USERNAME", "").encode("utf-8")):
            if len(forbidden) >= 4:
                assert_true(forbidden.lower() not in public_text.lower(), "public payload contains no workstation path/username")

    tests = run_matrix(zip_a)
    report = {
        "schema_version": 1,
        "status": "PASS",
        "powershell": str(powershell_exe().name),
        "powershell_version": powershell_version(),
        "game_execution": False,
        "synthetic_only": True,
        "deterministic_build": {
            "zip_sha256": file_digest(zip_a),
            "second_build_sha256": file_digest(zip_b),
            "byte_identical": True,
        },
        "tests": tests,
        "passed": len(tests),
        "failed": 0,
    }
    report_path = PIPELINE / "fixture_test_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TestFailure as exc:
        print(f"FIXTURE MATRIX FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)

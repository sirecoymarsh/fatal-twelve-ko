#!/usr/bin/env python3
"""Validate the four-boot fully isolated Ren'Py runtime smoke evidence."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from final_qa_common import file_sha256, read_json, write_json


HERE = Path(__file__).resolve().parent
ROOT = HERE / "runtime_smoke_engine"
GAME = ROOT / "game"
EXECUTION = ROOT / "runtime_smoke_execution.json"
RESULTS = GAME / "smoke_results.jsonl"
PIPELINE_RESULT = HERE / "final_text_build" / "final_text_pipeline_result.json"
OUT = HERE / "technical_qa" / "isolated_runtime_smoke.json"


LOOKUPS = {
    "開いてみよう": "열어 보자",
    "Are you sure you want to quit?": "게임을 종료하시겠습니까?",
    "Are you sure you want to return to the main menu?\nThis will lose unsaved progress.":
        "타이틀 화면으로 돌아가시겠습니까?\n저장하지 않은 진행 상황은 사라집니다.",
    "Numeral XII": "번호 XII",
}


def main() -> None:
    execution = read_json(EXECUTION)
    if execution.get("schema_version") != "fatal-twelve-isolated-runtime-smoke-execution-v1":
        raise SystemExit("runtime execution schema mismatch")
    isolated_root = Path(execution["isolated_root"]).resolve()
    executable = Path(execution["executable_path"]).resolve()
    if isolated_root != ROOT.resolve() or executable != (ROOT / "fatal.exe").resolve():
        raise SystemExit("runtime execution path binding mismatch")
    if execution.get("live_executable_invoked") is not False:
        raise SystemExit("live executable invocation contract failed")
    environment = execution.get("process_scoped_environment", {})
    if environment.get("SDL_AUDIODRIVER") != "dummy" or environment.get("RENPY_RENDERER") != "sw":
        raise SystemExit("process-scoped dummy audio/software renderer contract failed")
    runs = execution.get("runs")
    if not isinstance(runs, list) or len(runs) != 4:
        raise SystemExit("runtime must contain four isolated process runs")
    if [row.get("phase") for row in runs] != [0, 1, 2, 3] or any(row.get("exit_code") != 0 for row in runs):
        raise SystemExit("runtime phase/exit-code gate failed")
    if any(Path(row["executable_path"]).resolve() != executable for row in runs):
        raise SystemExit("one or more runtime phases used an unexpected executable")
    if execution.get("live_anchor_immutability_pass") is not True:
        raise SystemExit("live anchor immutability flag is not PASS")
    if execution.get("live_anchor_sha256_before") != execution.get("live_anchor_sha256_after"):
        raise SystemExit("live anchor hash maps differ")

    records = [json.loads(line) for line in RESULTS.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if len(records) != 4 or [row["phase"] for row in records] != [0, 1, 2, 3]:
        raise SystemExit("runtime result record universe mismatch")
    expected_boot = [
        ("korean", "korean"),
        ("japanese", None),
        ("english", "english"),
        ("korean", "korean"),
    ]
    expected_after = [
        ("japanese", None),
        ("english", "english"),
        ("korean", "korean"),
        ("korean", "korean"),
    ]
    for index, record in enumerate(records):
        if record.get("pass") is not True or record.get("errors") != []:
            raise SystemExit(f"runtime phase {index} contains assertion errors: {record.get('errors')}")
        if record.get("config_sound") is not False:
            raise SystemExit(f"runtime phase {index} config.sound was not false")
        audio_state = record.get("audio_state", {})
        if set(audio_state) != {"music", "sfx", "voice"} or any(
            state.get("volume") != 0.0 or state.get("muted") is not True for state in audio_state.values()
        ):
            raise SystemExit(f"runtime phase {index} audio mixer mute gate failed")
        if (record.get("marker_at_boot"), record.get("language_at_boot")) != expected_boot[index]:
            raise SystemExit(f"runtime phase {index} boot persistence mismatch")
        if (record.get("marker_after_action"), record.get("language_after_action")) != expected_after[index]:
            raise SystemExit(f"runtime phase {index} transition mismatch")
        if not {"english", "korean"}.issubset(set(record.get("known_languages", []))):
            raise SystemExit(f"runtime phase {index} language registration mismatch")
        actual = {row["old"]: row for row in record.get("lookups", [])}
        if set(actual) != set(LOOKUPS):
            raise SystemExit(f"runtime phase {index} representative lookup universe mismatch")
        for old, korean in LOOKUPS.items():
            row = actual[old]
            if row.get("korean") != korean or row.get("japanese") != old or row.get("english") != old:
                raise SystemExit(f"runtime phase {index} scoped lookup mismatch: {old!r}")
            expected_current = korean if expected_boot[index][1] == "korean" else old
            if row.get("current") != expected_current:
                raise SystemExit(f"runtime phase {index} current-language lookup mismatch: {old!r}")
        if record.get("dummy_english_lookup") != "__f12_smoke_english_translated__":
            raise SystemExit(f"runtime phase {index} English slot lookup failed")

    phase_state = (GAME / "smoke_phase.txt").read_text(encoding="ascii").strip()
    persistent = GAME / "saves" / "persistent"
    if phase_state != "4" or not persistent.is_file():
        raise SystemExit("restart persistence evidence files are incomplete")
    traceback_files = list(ROOT.glob("traceback*.txt")) + list(GAME.glob("traceback*.txt"))
    if traceback_files:
        raise SystemExit(f"Ren'Py traceback files present: {traceback_files}")

    pipeline = read_json(PIPELINE_RESULT)
    source_strings = Path(pipeline["global_strings"]["path"])
    copied_strings = GAME / "tl" / "korean" / "scenario_strings.rpy"
    if file_sha256(source_strings) != pipeline["global_strings"]["sha256"]:
        raise SystemExit("pipeline global strings hash mismatch")
    if file_sha256(copied_strings) != file_sha256(source_strings):
        raise SystemExit("runtime smoke strings copy differs from frozen render")

    expected_compiled = [
        GAME / "options.rpyc",
        GAME / "script.rpyc",
        GAME / "f12_korean_bootstrap.rpyc",
        GAME / "tl" / "korean" / "f12_slot.rpyc",
        GAME / "tl" / "korean" / "scenario_strings.rpyc",
        GAME / "tl" / "english" / "smoke_english.rpyc",
    ]
    missing_compiled = [str(path) for path in expected_compiled if not path.is_file()]
    if missing_compiled:
        raise SystemExit(f"isolated engine did not compile expected harness RPY: {missing_compiled}")

    report = {
        "schema_version": "fatal-twelve-isolated-runtime-smoke-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "execution": {"path": str(EXECUTION.resolve()), "sha256": file_sha256(EXECUTION)},
        "isolated_engine": {
            "root": str(ROOT.resolve()),
            "executable": str(executable),
            "executable_sha256": file_sha256(executable),
            "live_executable_invoked": False,
            "process_runs": 4,
            "all_exit_codes_zero": True,
            "sdl_audiodriver": "dummy",
            "renpy_config_sound": False,
            "music_sfx_voice_volume": 0.0,
            "music_sfx_voice_muted": True,
            "renderer": "sw",
            "traceback_files": [],
        },
        "language_persistence": {
            "boot_sequence": ["korean", "japanese", "english", "korean"],
            "transition_sequence": ["japanese", "english", "korean"],
            "persistent_file": str(persistent.resolve()),
            "persistent_file_sha256": file_sha256(persistent),
            "normal_restart_round_trips": 3,
            "verdict": "PASS",
        },
        "representative_string_lookup": {
            "cases": len(LOOKUPS),
            "process_phases": 4,
            "korean_matches": len(LOOKUPS) * 4,
            "japanese_noninterference_matches": len(LOOKUPS) * 4,
            "english_noninterference_matches": len(LOOKUPS) * 4,
            "multiline_ui_lookup": "PASS",
            "numeral_supplement_lookup": "PASS",
            "verdict": "PASS",
        },
        "compiled_harness_rpy": [
            {"path": str(path.resolve()), "sha256": file_sha256(path)} for path in expected_compiled
        ],
        "frozen_global_strings": {
            "source_path": str(source_strings.resolve()),
            "source_sha256": file_sha256(source_strings),
            "isolated_copy_path": str(copied_strings.resolve()),
            "isolated_copy_sha256": file_sha256(copied_strings),
        },
        "live_anchor_immutability": {
            "sha256_before": execution["live_anchor_sha256_before"],
            "sha256_after": execution["live_anchor_sha256_after"],
            "pass": True,
        },
        "results": records,
        "verdict": "PASS",
    }
    write_json(OUT, report)
    print(json.dumps({
        "report": str(OUT.resolve()),
        "report_sha256": file_sha256(OUT),
        "process_runs": 4,
        "persistence_round_trips": 3,
        "representative_lookups": len(LOOKUPS) * 4,
        "audio_driver": "dummy",
        "live_executable_invoked": False,
        "verdict": "PASS",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

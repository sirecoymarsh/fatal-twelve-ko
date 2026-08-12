#!/usr/bin/env python3
"""Assemble a fresh, exact Ren'Py source stage from the frozen final render."""

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


EXPECTED_SCENARIO_COUNT = 29
EXPECTED_GLOBAL_STRING_COUNT = 1
SCRIPT_VERSION_SHA256 = "d052a3281338ff0c8e8e28b48ac5375085553df182ceb3f63400d946ad48e2d3"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_reparse(path: Path) -> bool:
    metadata = path.lstat()
    return path.is_symlink() or bool(
        getattr(metadata, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT
    )


def copy_record(source: Path, destination: Path, relative: str) -> dict[str, object]:
    if not source.is_file() or is_reparse(source):
        raise ValueError(f"source missing or unsafe: {source.name}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    source_hash = sha256_file(source)
    destination_hash = sha256_file(destination)
    if destination.stat().st_size != source.stat().st_size or destination_hash != source_hash:
        raise ValueError(f"stage copy verification failed: {relative}")
    return {"path": relative, "size": destination.stat().st_size, "sha256": destination_hash}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-rpy-root", required=True, type=Path)
    parser.add_argument("--pipeline-result", required=True, type=Path)
    parser.add_argument("--bootstrap", required=True, type=Path)
    parser.add_argument("--slot", required=True, type=Path)
    parser.add_argument("--script-version", required=True, type=Path)
    parser.add_argument("--expected-bootstrap-sha256", required=True)
    parser.add_argument("--expected-slot-sha256", required=True)
    parser.add_argument("--stage-root", required=True, type=Path)
    parser.add_argument("--expected-pipeline-result-sha256", required=True)
    parser.add_argument("--expected-render-manifest-sha256", required=True)
    parser.add_argument("--expected-global-strings-sha256", required=True)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    final_rpy = args.final_rpy_root.resolve(strict=True)
    pipeline_result = args.pipeline_result.resolve(strict=True)
    bootstrap = args.bootstrap.resolve(strict=True)
    slot = args.slot.resolve(strict=True)
    script_version = args.script_version.resolve(strict=True)
    stage = args.stage_root.resolve(strict=False)
    report = args.report.resolve(strict=False)
    if stage.exists():
        raise ValueError("stage root must not already exist")
    if sha256_file(pipeline_result) != args.expected_pipeline_result_sha256:
        raise ValueError("frozen pipeline result SHA-256 mismatch")
    render_manifest = final_rpy / "render_manifest.json"
    if sha256_file(render_manifest) != args.expected_render_manifest_sha256:
        raise ValueError("frozen render manifest SHA-256 mismatch")
    global_strings = final_rpy / "strings" / "scenario_strings.rpy"
    if sha256_file(global_strings) != args.expected_global_strings_sha256:
        raise ValueError("frozen global strings SHA-256 mismatch")
    if sha256_file(script_version) != SCRIPT_VERSION_SHA256:
        raise ValueError("trusted script_version.txt SHA-256 mismatch")
    if sha256_file(bootstrap) != args.expected_bootstrap_sha256:
        raise ValueError("reviewed bootstrap SHA-256 mismatch")
    if sha256_file(slot) != args.expected_slot_sha256:
        raise ValueError("reviewed language-slot SHA-256 mismatch")

    scenario_sources = sorted((final_rpy / "scenario").glob("*.rpy"), key=lambda path: path.name)
    string_sources = sorted((final_rpy / "strings").glob("*.rpy"), key=lambda path: path.name)
    all_rpy = sorted(final_rpy.rglob("*.rpy"), key=lambda path: path.as_posix())
    if len(scenario_sources) != EXPECTED_SCENARIO_COUNT:
        raise ValueError(f"expected {EXPECTED_SCENARIO_COUNT} scenario RPY files")
    if len(string_sources) != EXPECTED_GLOBAL_STRING_COUNT or string_sources != [global_strings]:
        raise ValueError("frozen strings source set is not exact")
    if all_rpy != sorted(scenario_sources + string_sources, key=lambda path: path.as_posix()):
        raise ValueError("unexpected RPY outside frozen scenario/strings source roots")

    incoming = stage.with_name(f"{stage.name}.incoming-{uuid.uuid4().hex}")
    incoming.mkdir(parents=True)
    records: list[dict[str, object]] = []
    try:
        records.append(
            copy_record(bootstrap, incoming / "game" / "f12_korean_bootstrap.rpy", "game/f12_korean_bootstrap.rpy")
        )
        records.append(
            copy_record(slot, incoming / "game" / "tl" / "korean" / "f12_slot.rpy", "game/tl/korean/f12_slot.rpy")
        )
        for source in scenario_sources:
            relative = f"game/tl/korean/scenario/{source.name}"
            records.append(copy_record(source, incoming.joinpath(*PurePosixPath(relative).parts), relative))
        records.append(
            copy_record(
                global_strings,
                incoming / "game" / "tl" / "korean" / "strings" / "scenario_strings.rpy",
                "game/tl/korean/strings/scenario_strings.rpy",
            )
        )
        records.append(copy_record(script_version, incoming / "game" / "script_version.txt", "game/script_version.txt"))
        actual = sorted(
            path.relative_to(incoming).as_posix()
            for path in incoming.rglob("*")
            if path.is_file()
        )
        expected = sorted(str(record["path"]) for record in records)
        if actual != expected:
            raise ValueError("assembled stage exact file-set verification failed")
        stage.parent.mkdir(parents=True, exist_ok=True)
        incoming.replace(stage)
    except Exception:
        print(f"unpromoted stage evidence retained: {incoming}", file=sys.stderr)
        raise

    records.sort(key=lambda item: str(item["path"]))
    result = {
        "schema_version": "fatal-twelve-final-rpy-stage-v2",
        "status": "PASS",
        "game_executed": False,
        "source_rpy_file_count": len(records) - 1,
        "scenario_rpy_file_count": len(scenario_sources),
        "global_strings_rpy_file_count": len(string_sources),
        "stage_file_count": len(records),
        "frozen_pipeline_result_sha256": args.expected_pipeline_result_sha256,
        "frozen_render_manifest_sha256": args.expected_render_manifest_sha256,
        "frozen_global_strings_sha256": args.expected_global_strings_sha256,
        "reviewed_bootstrap_sha256": args.expected_bootstrap_sha256,
        "reviewed_slot_sha256": args.expected_slot_sha256,
        "stage_files": records,
    }
    report.parent.mkdir(parents=True, exist_ok=True)
    temporary = report.with_name(f"{report.name}.incoming-{uuid.uuid4().hex}")
    temporary.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, report)
    print(f"FINAL STAGE PASS: {len(records) - 1} RPY sources, {len(records)} files")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, UnicodeError) as error:
        print(f"FINAL STAGE FAILED: {error}", file=sys.stderr)
        raise SystemExit(2)

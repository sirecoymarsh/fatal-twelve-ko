#!/usr/bin/env python3
"""Apply the 22 exact-guarded Arabic-number restorations and rebuild provenance.

This script is intentionally single-use against the pre-apply failure inventory.
It changes only ``new_ko`` in the two selected canonical correction JSONLs.  All
input masters and policy artifacts remain read-only, and every mutation must be
an exact, explicitly declared semantic-surface replacement.
"""

from __future__ import annotations

import copy
import json
import os
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import build_final_correction_manifest
from final_qa_common import NUMBER_RE, file_sha256, read_json, text_sha256, token_validation_findings


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
REVIEWS = HERE / "reviews"
FAILURES = REVIEWS / "numeric_token_failures.preapply.json"
MANIFEST = REVIEWS / "global_correction_manifest.json"
VALIDATION = REVIEWS / "global_correction_manifest.validation.json"
REPORT = REVIEWS / "numeric_token_fixes.applied.json"
EXPECTED_FAILURES_SHA256 = "35e01943856f3dbba06a5a0159b3f50b78d23e79103d14cf9cd809dec2c3d07b"


# Each tuple is (stable_id, exact old numeric surface, exact new numeric
# surface).  Requiring old_target.replace(old_surface, new_surface) to equal the
# declared final target proves that no surrounding translated prose is changed.
FIXES = {
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_1_1149574d": (
        "둘", "2명", "결국 2명만 남았고, 대답을 보류했다고는 해도 몹시 어색했다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_c149b304": (
        "동전 두 개", "동전 2개",
        "그리고 직원에게 이 주스의 가격을 물었다. 분위기에 걸맞게 비싸다고 생각하면서도, 1000엔짜리 지폐 한 장과 100엔짜리 동전 2개를 건넸다.",
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_ea240ca0": (
        "하루 전", "1일 전", "아란 스코피온은 1일 전, 스케일 존스에게 정보 교환을 제안받았다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_acc64346": (
        "한 가지", "1가지", "그리고 스케일이 그에게 1가지 더 제안한 것이 있었다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_32a048d7": (
        "한 바퀴", "1바퀴", "1바퀴를 돌듯 차례대로 서로를 지명하고 방어해, 누구도 다른 사람을 지명할 수 없게 만드는 방법이다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_640fc55b": (
        "아홉 번째", "9번째", "9번째 선정이 시작되면, 그 정보로 린카를 지명한다――는 방법이다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_45064d02": (
        "카드 한 장", "카드 1장", "아란은 카드 1장을 꺼내 짧게 중얼거렸다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_5dabba4c": (
        "세 장", "3장", "정작 아란은 아직 카드 3장을 모으지 못했지만, 지명당한 미하루가 살아남았다는 건 미하루가 스케일의 카드 3장을 모았다는 뜻이다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_3b875abd": (
        "세 장", "3장", "그리고 린카도 이미 스케일의 카드 3장을 모았을 것이라고 그는 확신하고 있었다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_c1650caf": (
        "두 달", "2개월", "오데트와 이 나라를 찾은 지 이제 곧 2개월이 되어 간다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_037dea14": (
        "네 번", "4번", "여신의 선정도 순조롭게 진행된다면 이제 4번 남았다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_aa6ba20d": (
        "아홉 번째", "9번째", "스케일의 작전대로라면 9번째 선정에서 스케일이 린카를, 페데리코가 미하루를, 아란이 페데리코를 지명할 터였다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_1370b6b2": (
        "두 시간", "2시간", "2시간쯤 빈둥거리며 보낸 뒤, 샤워를 하고 자기로 했다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_s1_end_2_b3d45669": (
        "첫 번째", "1번째", "『5분이 지나면 네 할머니를 죽인다. 1번째 시도에서 카드가 만들어지지 않아도 죽일 거야』"
    ),
    "scenario.rpa::scenario/009.rpy::tid::f009_root_E_95bdac2b": (
        "네 시간", "4시간", "여기서 할머니 댁까지는 신칸센을 타도 4시간 넘게 걸리니, 그야말로 도착하자마자 되돌아온 셈이다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::sentei9_d60be73f": (
        "다섯 명", "5명", "남은 참가자는 고작 5명."
    ),
    "scenario.rpa::scenario/009.rpy::tid::sentei9_be6fe051": (
        "아홉 번째", "9번째", "정체된 나날이 이어지는 가운데 9번째 선정이 시작됐다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::sentei9_7db88862": (
        "두 번째", "2번째", "내가 상층에 온 건 이번이 2번째였다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::sentei9_e88612a9": (
        "차선이 세 개", "3차선", "3차선 이상인 고가 고속도로."
    ),
    "scenario.rpa::scenario/009.rpy::tid::sentei9_f735ab2a": (
        "두 번째", "2번째", "이렇게 나의 2번째 지명이 끝났다."
    ),
    "scenario.rpa::scenario/009.rpy::tid::sentei9_e9257080": (
        "한 명", "1명", "「그럼 오늘 밤의 탈락자는 1명――」"
    ),
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_cee92cf3": (
        "열두 번째", "12번째", "1부터 차례로 세어 도달한 12번째. 우연이라기에는 확실히 절묘하다."
    ),
}


def workspace_path(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def write_jsonl_atomic(path: Path, rows: list[dict]) -> None:
    temporary = path.with_name(path.name + ".numeric-fix.tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(temporary, path)


def write_json_atomic(path: Path, payload: dict) -> None:
    temporary = path.with_name(path.name + ".numeric-fix.tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def normalized_numbers(text: str) -> Counter[str]:
    return Counter(NUMBER_RE.findall(unicodedata.normalize("NFKC", text)))


def main() -> None:
    if file_sha256(FAILURES) != EXPECTED_FAILURES_SHA256:
        raise SystemExit("pre-apply numeric failure inventory SHA-256 mismatch")
    failure_doc = read_json(FAILURES)
    failures = failure_doc.get("entries") if isinstance(failure_doc, dict) else None
    if failure_doc.get("records") != 22 or not isinstance(failures, list) or len(failures) != 22:
        raise SystemExit("pre-apply numeric failure inventory must contain exactly 22 entries")
    failures_by_id = {row["stable_id"]: row for row in failures}
    if len(failures_by_id) != 22 or set(failures_by_id) != set(FIXES):
        raise SystemExit("numeric fix stable-ID universe differs from the 22-entry failure inventory")

    manifest_before = read_json(MANIFEST)
    manifest_items = {
        Path(item["path"]).name: item for item in manifest_before.get("correction_files", [])
    }
    target_files = sorted({row["file"] for row in failures})
    if target_files != [
        "ROOT.009.consolidated.corrections.jsonl",
        "ROOT.011_02_and_GH.consolidated.corrections.jsonl",
    ]:
        raise SystemExit(f"unexpected correction-file universe: {target_files}")

    paths = {name: REVIEWS / name for name in target_files}
    snapshots = {path: path.read_bytes() for path in [*paths.values(), MANIFEST, VALIDATION] if path.exists()}
    report_snapshot = REPORT.read_bytes() if REPORT.exists() else None
    policy_paths = {
        "ruby_map": HERE / "ruby_map.approved.json",
        "structural_overlay": REVIEWS / "structural_fixes_spec.json",
        "approval_ledger": REVIEWS / "qa_approvals.draft.json",
    }
    policy_hashes_before = {name: file_sha256(path) for name, path in policy_paths.items()}

    rows_by_file: dict[str, list[dict]] = {}
    locations: dict[str, tuple[str, int, dict]] = {}
    touched_file_summary = []
    for name, path in paths.items():
        manifest_item = manifest_items.get(name)
        if manifest_item is None or manifest_item.get("sha256") != file_sha256(path):
            raise SystemExit(f"manifest does not bind the current correction file: {name}")
        rows = load_jsonl(path)
        if manifest_item.get("records") != len(rows):
            raise SystemExit(f"manifest record count mismatch: {name}")
        rows_by_file[name] = rows
        for index, row in enumerate(rows, 1):
            sid = row.get("stable_id")
            if sid in FIXES:
                if sid in locations:
                    raise SystemExit(f"duplicate selected stable ID: {sid}")
                locations[sid] = (name, index, row)
        touched_file_summary.append({
            "path": workspace_path(path),
            "sha256_before": file_sha256(path),
            "records": len(rows),
        })
    if set(locations) != set(FIXES):
        raise SystemExit("one or more numeric fixes did not join exactly once to the canonical JSONLs")

    structural = read_json(policy_paths["structural_overlay"])
    structural_by_id = {row["stable_id"]: row for row in structural["entries"]}
    approvals = read_json(policy_paths["approval_ledger"])
    approval_ids = {row["stable_id"] for row in approvals["entries"]}
    if set(FIXES) & approval_ids:
        raise SystemExit("numeric fix unexpectedly overlaps an exact target-hash approval")

    master_cache: dict[str, tuple[Path, dict]] = {}
    applied_entries = []
    for sid, (surface_before, surface_after, final_target) in FIXES.items():
        failure = failures_by_id[sid]
        name, line_no, row = locations[sid]
        script = failure["script"]
        sequence = failure["sequence"]
        if (failure["file"], failure["line"]) != (name, line_no):
            raise SystemExit(f"failure-inventory line guard mismatch: {sid}")
        if (row.get("script"), row.get("sequence"), row.get("reviewer")) != (script, sequence, "ROOT"):
            raise SystemExit(f"canonical identity/reviewer guard mismatch: {sid}")
        if row.get("old_ko") != failure.get("old_ko") or row.get("new_ko") != failure.get("new_ko"):
            raise SystemExit(f"canonical old/current-target guard mismatch: {sid}")
        if row["new_ko"].count(surface_before) < 1:
            raise SystemExit(f"declared old numeric surface absent: {sid}")
        if row["new_ko"].replace(surface_before, surface_after) != final_target:
            raise SystemExit(f"fix changes text outside the declared numeric surface: {sid}")

        if script not in master_cache:
            master_path = HERE / "output" / "masters" / f"scenario_{script}.master.json"
            master_cache[script] = (master_path, read_json(master_path))
        master_path, master_doc = master_cache[script]
        entry = master_doc["entries"][sequence - 1]
        if (entry.get("stable_id"), entry.get("sequence"), entry.get("source_jp"), entry.get("draft_ko")) != (
            sid,
            sequence,
            failure.get("source_jp"),
            row.get("old_ko"),
        ):
            raise SystemExit(f"source master exact semantic-unit guard mismatch: {sid}")

        before_findings = token_validation_findings(entry, row["new_ko"])
        if len(before_findings) != 1 or before_findings[0].get("kind") != "arabic_number_mismatch":
            raise SystemExit(f"pre-fix finding is not exactly one Arabic-number mismatch: {sid}")
        expected_numbers = Counter({str(key): int(value) for key, value in failure["expected"].items()})
        if Counter(before_findings[0].get("expected", {})) != expected_numbers:
            raise SystemExit(f"pre-fix expected number multiset mismatch: {sid}")
        after_findings = token_validation_findings(entry, final_target)
        if after_findings:
            raise SystemExit(f"post-fix protected-token failure {sid}: {after_findings}")
        if normalized_numbers(final_target) != expected_numbers:
            raise SystemExit(f"post-fix normalized number multiset mismatch: {sid}")

        if sid in structural_by_id and structural_by_id[sid].get("final_ko") != final_target:
            raise SystemExit(f"numeric fix would invalidate structural-overlay final target: {sid}")

        before_target = row["new_ko"]
        preserved = copy.deepcopy(row)
        row["new_ko"] = final_target
        if {key: value for key, value in row.items() if key != "new_ko"} != {
            key: value for key, value in preserved.items() if key != "new_ko"
        }:
            raise SystemExit(f"fields other than new_ko changed: {sid}")
        applied_entries.append({
            "file": workspace_path(paths[name]),
            "line": line_no,
            "script": script,
            "sequence": sequence,
            "stable_id": sid,
            "source_jp": entry["source_jp"],
            "source_sha256": text_sha256(entry["source_jp"]),
            "master_old_ko_guard": row["old_ko"],
            "master_old_ko_sha256": text_sha256(row["old_ko"]),
            "target_before": before_target,
            "target_before_sha256": text_sha256(before_target),
            "numeric_surface_before": surface_before,
            "numeric_surface_after": surface_after,
            "target_after": final_target,
            "target_after_sha256": text_sha256(final_target),
            "expected_nfkc_arabic_numbers": dict(expected_numbers),
            "before_findings": before_findings,
            "after_findings": after_findings,
            "only_declared_numeric_surface_changed": True,
        })

    master_hashes_before = {
        workspace_path(path): file_sha256(path) for path, _ in master_cache.values()
    }
    manifest_sha_before = file_sha256(MANIFEST)
    validation_sha_before = file_sha256(VALIDATION)
    try:
        for name, rows in rows_by_file.items():
            write_jsonl_atomic(paths[name], rows)

        # Re-run the same authoritative builder used for the frozen manifest;
        # this refreshes both correction-file hashes and the validation report.
        build_final_correction_manifest.main()

        policy_hashes_after = {name: file_sha256(path) for name, path in policy_paths.items()}
        master_hashes_after = {
            workspace_path(path): file_sha256(path) for path, _ in master_cache.values()
        }
        if policy_hashes_after != policy_hashes_before:
            raise RuntimeError("a policy artifact changed during numeric correction")
        if master_hashes_after != master_hashes_before:
            raise RuntimeError("a source master changed during numeric correction")
        manifest_after = read_json(MANIFEST)
        validation_after = read_json(VALIDATION)
        if validation_after.get("summary", {}).get("verdict") != "PASS":
            raise RuntimeError("regenerated global manifest validation is not PASS")
        after_items = {
            Path(item["path"]).name: item for item in manifest_after.get("correction_files", [])
        }
        for item in touched_file_summary:
            name = Path(item["path"]).name
            item["sha256_after"] = file_sha256(paths[name])
            if after_items.get(name, {}).get("sha256") != item["sha256_after"]:
                raise RuntimeError(f"regenerated manifest does not bind updated file: {name}")

        report = {
            "schema_version": "fatal-twelve-numeric-token-fix-report-v1",
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "source_failure_inventory": {
                "path": workspace_path(FAILURES),
                "sha256": file_sha256(FAILURES),
                "records": 22,
            },
            "summary": {
                "records": len(applied_entries),
                "correction_files_changed": len(touched_file_summary),
                "protected_token_findings_before": 22,
                "protected_token_findings_after": 0,
                "exact_master_old_guards_pass": True,
                "exact_current_target_guards_pass": True,
                "semantic_unit_numeric_surface_only": True,
                "source_masters_modified": False,
                "policy_artifacts_modified": False,
                "verdict": "PASS",
            },
            "manifest": {
                "path": workspace_path(MANIFEST),
                "sha256_before": manifest_sha_before,
                "sha256_after": file_sha256(MANIFEST),
            },
            "manifest_validation": {
                "path": workspace_path(VALIDATION),
                "sha256_before": validation_sha_before,
                "sha256_after": file_sha256(VALIDATION),
                "verdict": validation_after["summary"]["verdict"],
            },
            "changed_correction_files": touched_file_summary,
            "source_master_immutability": {
                "sha256_before": master_hashes_before,
                "sha256_after": master_hashes_after,
                "pass": True,
            },
            "policy_artifact_immutability": {
                "sha256_before": policy_hashes_before,
                "sha256_after": policy_hashes_after,
                "pass": True,
            },
            "entries": sorted(applied_entries, key=lambda row: (row["script"], row["sequence"])),
            "actions_not_performed": ["game execution", "game compilation"],
        }
        write_json_atomic(REPORT, report)
    except BaseException:
        for path, payload in snapshots.items():
            path.write_bytes(payload)
        if report_snapshot is None:
            if REPORT.exists():
                REPORT.unlink()
        else:
            REPORT.write_bytes(report_snapshot)
        raise

    print(json.dumps({
        "report": workspace_path(REPORT),
        "report_sha256": file_sha256(REPORT),
        "manifest_sha256": file_sha256(MANIFEST),
        "validation_sha256": file_sha256(VALIDATION),
        "records": len(applied_entries),
        "verdict": "PASS",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

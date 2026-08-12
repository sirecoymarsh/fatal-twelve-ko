#!/usr/bin/env python3
"""Materialize the 42 strict numeric-token fixes missing from correction review.

The immutable scenario master index is SHA-bound. The selected records are the
complete set of still-failing base targets after the 2,596 reviewed corrections;
no master is modified. Output is one guarded correction JSONL plus an exhaustive
before/after report.
"""

from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from final_qa_common import file_sha256, read_json, text_sha256, token_validation_findings


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
REVIEWS = HERE / "reviews"
MASTER_INDEX = HERE / "output" / "master_index.json"
GLOBAL_MANIFEST = REVIEWS / "global_correction_manifest.json"
OUTPUT = REVIEWS / "ROOT.base_numeric_token_fixes.corrections.jsonl"
REPORT = REVIEWS / "ROOT.base_numeric_token_fixes.report.json"
EXPECTED_MASTER_INDEX_SHA256 = "33a690260a2e516adb353ebdfdf9d70c92a6ec1e90fa058b626c55d557995d68"


FINAL_TARGETS = {
    "scenario.rpa::scenario/002.rpy::tid::f002_e9a7e479": "≪여신의 선정≫에서 1명만 남을 수 있다면――.",
    "scenario.rpa::scenario/002.rpy::tid::f002_7b58bb48": "그리고 이제 2번째 선정이 시작될 때까지 나는 진전도 후퇴도 없는 나날을 보냈다.",
    "scenario.rpa::scenario/002.rpy::tid::f002_961fb560": "이걸로 베이징 덕은 3접시째다. 사이사이에 물만두와 만터우 같은 것도 먹었다.",
    "scenario.rpa::scenario/002.rpy::tid::f002_900e7419": "「뭐, 그러니까 말이야. 세계 1위의 요리가 프랑스 요리라는 사실은 변함없지만, 중국 요리에는 2위를 줘도 괜찮겠어」",
    "scenario.rpa::scenario/002.rpy::tid::f002_ea8bf169": "「1번째 선정에서 아무도 우리를 지명하지 않았으니, 운 좋게 카드를 다 모은 녀석은 없다는 사실이 드러났지」",
    "scenario.rpa::scenario/003.rpy::tid::f003_862ae915": "이제야 2번째 선정이 끝난 듯한 기분이 들었다.",
    "scenario.rpa::scenario/004.rpy::tid::f004_s1_end_11446a0c": "그녀의 얼굴을 보는 건 벌써 3번째다. 꿈의 세계에서. 운명의 대회랑에서.",
    "scenario.rpa::scenario/004.rpy::tid::f004_s1_end_a9681c4e": "「그 2명이!」",
    "scenario.rpa::scenario/004.rpy::tid::f004_s1_end_bed8e84a": "Ⅺ의 여성은 2번째 선정에서 Ⅶ의 남성을 탈락시킨 사람이다. Ⅻ의 스코피온 씨와 마찬가지로 무척 냉혹한 눈을 하고 있었다.",
    "scenario.rpa::scenario/004.rpy::tid::f004_s1_end_00ec6cd0": "설마 그 2명이 협력 관계였다니. Ⅲ의 남자는 내가 성명을 알아 조금 유리할 줄 알았지만 그 여자와 한패라면 유리할 것도 없을 것이다.",
    "scenario.rpa::scenario/004.rpy::tid::f004_s1_end_825e5dc4": "「……1명보다 2명이 더 즐겁잖아?」",
    "scenario.rpa::scenario/004.rpy::tid::f004_s2_end_849bc0c7": "「아니, 같이 가자. 2명이 가는 편이 좋을 것 같아」",
    "scenario.rpa::scenario/004.rpy::tid::f004_s2_end_882082a0": "나도 가능하다면 이곳에 2번이나 오고 싶지는 않았다. 아니, 가게 자체를 부정하는 게 아니라 분위기가 거북한 것이다. 남자 손님뿐이라 우리는 아무래도 눈에 띄기도 하고.",
    "scenario.rpa::scenario/004.rpy::tid::f004_s2_end_166d6a02": "3명이 함께 돌아가기로 하고, 내가 소냐를 재우게 된 경위를 설명했다.",
    "scenario.rpa::scenario/004.rpy::tid::f004_s2_end_e2c27dc8": "아키하바라에서 소부선을 타고 신주쿠까지 온 3명은 환승하려고 일단 승강장에 나왔다.",
    "scenario.rpa::scenario/004.rpy::tid::f004_s2_end_c95c09a3": "방과 후 우리 3명은 교문에 있었다.",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_dd8f9cf8": "가게는 결국 내 몸 상태가 나빠 1주일 정도 쉬기로 했다.",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_8a249351": "「……그렇군. 히츠지 씨는 다른 사람보다 기억이 많이 개변되었다는 추측밖에 지금은 할 수 없지만, 너는 ≪세계가 개변된≫ 2가지 기억을 비교적 선명하게 가지고 있어」",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_4641e4a9": "「지금부터는 우리 3명이 싸우자. 상대는 다른 참가자가 아니야. 우리의 운명이야」",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_16fc20fe": "「――뭐, 됐어. 네 마음은 기쁘지만 마음만 받을게. 아까도 말했지? 우리는 우선 마지막 2명이 되어야 해」",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_ad905753": "나는 다른 참가자들의 정보도, 우리 2명이 살아남을 방도도 아무것도 갖고 있지 않다.",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_16bb4f13": "「데키마, 노나, 모르타라는 3종류가 있고, 각각 그리스 신화의 모이라라는 운명의 여신과 대응한다고 적혀 있었어요」",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_05b04bd2": "「참고로 현재 그의 가족 구성은 남동생 4명과 여동생 1명이라고 해. 그 가족은 아란의 수입으로 생활하는 모양이야」",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_a61d2db5": "페데리코는 카드북에서 카드 1장을 꺼내 흔들어 보였다.",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_f3a4bc78": "배경 정보가 없으므로 오데트의 사인을 이해한 것이 아니기 때문이라고 2명 모두 알고 있다.",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_9f27bd2f": "「8번째 선정에서는 페데리코가 나를 지명하고, 스케일이 너를 지명해서 둘이 탈락한다. 너한테서 아란의 ≪사인≫ 카드를 얻으면 스케일의 목적은 달성되지」",
    "scenario.rpa::scenario/008.rpy::tid::f008_s1_end_bb7be56c": "12명이 죽는 동시에 그 죽음이 없었던 일이 된 운명의 날.",
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_53e6f637": "운명의 대회랑을 한 바퀴 둘러싸듯 떠 있는 12개의 둥근 바닥 위에 선 사람은 이제 나와 미하루뿐이었다.",
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_fb727df2": "「오늘 밤은 11번째 선정. 수많은 탄식 끝에 두 분 중 한 분이 저의 그릇이 되시겠지요」",
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_3ac1a7c8": "「12번째. 어머, 운명적이네요」",
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_b9491b89": "12번. 그것은 확실히 운명적인 숫자였다.",
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_aecdd8bd": "하지만 이번 선정이 12번째라면 의미가 달라진다.",
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_45ece4ae": "「저는 운명의 여신의 힘으로 ≪인과의 때≫에 묶인 12명의 ≪목숨을 잃지 않은 세계≫를 본류에 한데 묶고 있습니다」",
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_d17fdf3b": "「≪인과의 때≫로 이어져 있었기에 제가 12개나 되는 세계를 다시 엮을 수 있었던 것이니까요」",
    "scenario.rpa::scenario/011_02.rpy::tid::sentei11_4d222207": "희망은 내 카드북에 잠든 카드 1장에 맡겨졌다.",
    "scenario.rpa::scenario/BAD_END_01.rpy::tid::fBAD_01_d132aa03": "「뭔가 오랜만이네. 이렇게 2명이서 말이야」",
    "scenario.rpa::scenario/BAD_END_01.rpy::tid::fBAD_01_6a058e20": "나를 포함한 이 3명이 사이좋게 지내는 것.",
    "scenario.rpa::scenario/BAD_END_02.rpy::tid::fBAD_02_ba8b287a": "2개월 전의 이야기.",
    "scenario.rpa::scenario/BAD_END_04.rpy::tid::fBAD_04_444cd946": "그렇게 저는 17살이 되었습니다.",
    "scenario.rpa::scenario/MIHARU_END.rpy::tid::fMIHARU_c9522701": "우리 12명이 ≪있었어야 했던≫ 곳.",
    "scenario.rpa::scenario/TRUE_END.rpy::tid::fTRUE_ebf20dfa": "게다가 3명에게서 각자 선물까지 받고 말았다.",
    "scenario.rpa::scenario/UNHAPPY_END.rpy::tid::fUNHAPPY_c7022cf4": "인형을 데리고 다니는 소녀를 포함해 가족 3명이 함께 걷고 있었다.",
}


def workspace_path(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def write_jsonl_atomic(path: Path, rows: list[dict]) -> None:
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(temporary, path)


def write_json_atomic(path: Path, payload: dict) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def main() -> None:
    if file_sha256(MASTER_INDEX) != EXPECTED_MASTER_INDEX_SHA256:
        raise SystemExit("master_index SHA-256 mismatch")
    index = read_json(MASTER_INDEX)
    manifest = read_json(GLOBAL_MANIFEST)
    prior_ids = set()
    prior_targets = {}
    prior_files = []
    for item in manifest["correction_files"]:
        path = REPO_ROOT / item["path"]
        if file_sha256(path) != item["sha256"]:
            raise SystemExit(f"prior correction hash mismatch: {path}")
        prior_files.append({"path": workspace_path(path), "sha256": item["sha256"], "records": item["records"]})
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if line.strip():
                sid = json.loads(line)["stable_id"]
                if sid in prior_ids:
                    raise SystemExit(f"duplicate prior correction stable ID: {sid}")
                prior_ids.add(sid)
                prior_targets[sid] = json.loads(line)["new_ko"]
    if prior_ids & set(FINAL_TARGETS):
        raise SystemExit("base numeric fix overlaps an existing canonical correction")

    selected = []
    all_failures = []
    master_hashes = {}
    for ref in index["masters"]:
        path = Path(ref["path"])
        if file_sha256(path) != ref["sha256"]:
            raise SystemExit(f"source master hash mismatch: {path}")
        master_hashes[workspace_path(path)] = ref["sha256"]
        document = read_json(path)
        script = document["script_key"]
        for entry in document["entries"]:
            effective_target = prior_targets.get(entry["stable_id"], entry["draft_ko"])
            findings = token_validation_findings(entry, effective_target)
            if findings:
                all_failures.append((script, entry, findings))
            sid = entry["stable_id"]
            if sid not in FINAL_TARGETS:
                continue
            if len(findings) != 1 or findings[0].get("kind") != "arabic_number_mismatch":
                raise SystemExit(f"selected base row is not exactly one Arabic-number failure: {sid}")
            final = FINAL_TARGETS[sid]
            after = token_validation_findings(entry, final)
            if after:
                raise SystemExit(f"selected base row still fails protected-token validation: {sid}: {after}")
            expected = Counter({str(key): int(value) for key, value in findings[0]["expected"].items()})
            selected.append({
                "script": script,
                "stable_id": sid,
                "sequence": entry["sequence"],
                "old_ko": entry["draft_ko"],
                "new_ko": final,
                "category": "보호 숫자 토큰 복원",
                "reason": "일본어 의미 원문의 명시 Arabic 숫자를 반각 ASCII로 정확히 보존",
                "reviewer": "ROOT",
                "_report": {
                    "source_jp": entry["source_jp"],
                    "source_sha256": text_sha256(entry["source_jp"]),
                    "target_before_sha256": text_sha256(entry["draft_ko"]),
                    "target_after_sha256": text_sha256(final),
                    "expected_nfkc_arabic_numbers": dict(expected),
                    "before_findings": findings,
                    "after_findings": after,
                },
            })

    failure_ids = {entry["stable_id"] for _, entry, _ in all_failures}
    if len(all_failures) != 42 or failure_ids != set(FINAL_TARGETS) or len(selected) != 42:
        raise SystemExit(json.dumps({
            "all_failure_records": len(all_failures),
            "missing_targets": sorted(failure_ids - set(FINAL_TARGETS)),
            "unexpected_targets": sorted(set(FINAL_TARGETS) - failure_ids),
        }, ensure_ascii=False, indent=2))
    selected.sort(key=lambda row: (row["script"], row["sequence"], row["stable_id"]))
    correction_rows = [{key: value for key, value in row.items() if key != "_report"} for row in selected]
    write_jsonl_atomic(OUTPUT, correction_rows)
    report_entries = []
    for row in selected:
        report_entries.append({
            "script": row["script"],
            "sequence": row["sequence"],
            "stable_id": row["stable_id"],
            "source_jp": row["_report"]["source_jp"],
            "source_sha256": row["_report"]["source_sha256"],
            "target_before": row["old_ko"],
            "target_before_sha256": row["_report"]["target_before_sha256"],
            "target_after": row["new_ko"],
            "target_after_sha256": row["_report"]["target_after_sha256"],
            "expected_nfkc_arabic_numbers": row["_report"]["expected_nfkc_arabic_numbers"],
            "before_findings": row["_report"]["before_findings"],
            "after_findings": row["_report"]["after_findings"],
        })
    per_script = Counter(row["script"] for row in selected)
    report = {
        "schema_version": "fatal-twelve-base-numeric-token-fixes-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_master_index": {
            "path": workspace_path(MASTER_INDEX),
            "sha256": file_sha256(MASTER_INDEX),
            "masters": len(index["masters"]),
        },
        "prior_correction_manifest": {
            "path": workspace_path(GLOBAL_MANIFEST),
            "sha256": file_sha256(GLOBAL_MANIFEST),
            "correction_files": prior_files,
            "stable_ids": len(prior_ids),
        },
        "output": {"path": workspace_path(OUTPUT), "sha256": file_sha256(OUTPUT), "records": len(correction_rows)},
        "summary": {
            "records": 42,
            "per_script": dict(sorted(per_script.items())),
            "protected_token_failed_records_before": 42,
            "protected_token_failed_records_after": 0,
            "exact_old_master_guards_pass": True,
            "existing_correction_overlap": 0,
            "source_masters_modified": False,
            "verdict": "PASS",
        },
        "source_master_hashes": master_hashes,
        "entries": report_entries,
        "actions_not_performed": ["game execution", "game compilation"],
    }
    write_json_atomic(REPORT, report)
    print(json.dumps({
        "corrections": workspace_path(OUTPUT),
        "corrections_sha256": file_sha256(OUTPUT),
        "report": workspace_path(REPORT),
        "report_sha256": file_sha256(REPORT),
        "records": len(correction_rows),
        "verdict": "PASS",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

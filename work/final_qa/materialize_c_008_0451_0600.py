#!/usr/bin/env python3
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "output" / "masters" / "scenario_008.master.json"
OUT = ROOT / "reviews" / "C.manual.008_0451_0600.corrections.jsonl"
REPORT = ROOT / "reviews" / "C.manual.008_0451_0600.report.json"

MANUAL: dict[int, tuple[str, str, str]] = {
    474: ("나와 한 몸의 양면인, 전철에서의 죽음.", "비유/의미", "表裏一体를 동전에 한정하지 않고 린카와 맞물린 죽음이라는 의미로 복원"),
    500: ("하지만 가장 직접적인 당사자가 돌아가셨으니, 여러 상황이 모호해도 이상하지 않다고 자연스럽게 받아들였다.", "어휘", "一番の当事者를 중요도의 평가가 아니라 사건의 직접 당사자로 명확화"),
    505: ("한 달 전이었다면 계속 마음에 걸렸겠지만, 이제는 완전히 받아들이고 있었다.", "의미/자연스러움", "もやもやしっぱなし와 開き直る의 심리 변화를 문맥에 맞게 복원"),
    511: ("「오늘 할머니, 조금 이상했어」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    521: ("여신의 선정이 치러지는 운명의 대회랑이 아니라, 비유하자면 그래, 꿈속에 존재하는 또 하나의 세계.", "고정 용어", "運命の大広間의 승인 표기 운명의 대회랑 적용"),
    523: ("「오랜만……은 아니군. 이제 그런 군소리는 필요 없으려나」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    524: ("「자신의 운명과 결착을 지은 너를 기다리는 건 분명 더욱 험난한 길이겠지」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    525: ("「무한한 가능성 속에서 네가 길을 만들어 가는 거야. 네 목숨이 궤적을 만들어 가는 거야. 그건 결코 기적 같은 게 아니지」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    526: ("「너희 인간이 지닌 의지의 힘이라는 걸까. 나도 이제야 흥미가 생기기 시작했어」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    528: ("「네 망각이 또 하나 풀려난다는 거지」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    537: ("「――――! ――――!」", "문자 폭", "한국어 target에 남은 U+3000 전각 공백을 반각 공백으로 교정"),
    545: ("「야옹」", "의성어", "일본어 고양이 울음 にゃーお를 자연스러운 한국어 의성어로 직접 번역"),
    549: ("내가 전철 안에서 폭발에 휘말려 목숨을 잃은 인과의 때.", "고정 용어", "因果の刻의 승인 표기 인과의 때 적용"),
    555: ("「그 꿈은 달라. 그때 기억이…… 아니야」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    562: ("「야옹」", "의성어", "일본어 고양이 울음 にゃーお를 자연스러운 한국어 의성어로 직접 번역"),
    563: ("「너한테 물은 게 아니거든」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    567: ("「――그런데에, 오늘은 또 리땅하고 둘이네」", "발화/인용부호", "ってぇ의 늘이는 말투는 보존하고 덧붙은 마침표 제거"),
    571: ("……보기만 해도 속이 느글거릴 것 같다.", "어휘", "단 음식 문맥의 胸やけ를 속 쓰림이 아닌 느글거림으로 교정"),
    572: ("「오늘은 단 게 당기는 날이거든」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    580: ("물론 가게 일이 있어서 디자인 관련 책을 몇 종류만 빌려 갈 생각이긴 하지만.", "수량/어휘", "何種類か는 책 권수가 아니라 여러 종류라는 의미이므로 복원"),
    581: ("「리땅, 또 심각한 표정 짓고 있어」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    582: ("「아, 미안 미안」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    586: ("「있잖아, 리땅」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    589: ("「리땅이랑 미하룽, 나오링이 다 같이 뭘 하는지는 모르고, 내가 따돌림당하는 것도 아니니까 상관없긴 한데 말이야」", "주체/발화", "ハブられてるわけじゃない의 피동 주체와 구어체를 자연스럽게 복원"),
    590: ("「골든위크가 끝난 뒤로 계에에에에속 다들 상태가 이상한 건 알고 있지만 말이야」", "발화/인용부호", "ずーーーーーっと의 늘임은 보존하고 원문에 없는 마침표 제거"),
    591: ("「다 같이 영화랑 노래방이랑 볼링이랑 수족관에 놀러 가기로 한 약속도 없어져 버리긴 했지만 말이야」", "발화/인용부호", "なくなっちゃたりしてた의 구어적 회상과 원문 종결을 자연스럽게 복원"),
    592: ("「……볼링이랑 수족관이 늘었잖아」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    593: ("「아니, 다음으로 미룬다는 느낌? 하고 싶은 건 많을수록 좋잖아」", "발화/인용부호", "いやぁ의 말머리와 구어체를 자연스럽게 복원"),
    595: ("「으음, 됐어. 여기까지. 이야기 흐름도 끊겼고」", "발화/인용부호", "불필요한 모음 늘임과 원문에 없는 마침표 제거"),
    596: ("「응, 그만두자」", "인용부호", "원문 대사 끝에 없는 마침표 제거"),
    598: ("「어차피 거의 매일 계속 얼굴 보잖아」", "발화/인용부호", "ずーっと를 자연스러운 한국어로 직접 옮기고 원문에 없는 마침표 제거"),
}

FW_TRANS = str.maketrans("０１２３４５６７８９％", "0123456789%")
ROMAN_RE = re.compile(r"[\u2160-\u2188]+")
TAG_RE = re.compile(r"\{[^{}]+\}|\[[^\[\]]+\]")
KANA_RE = re.compile(r"[ぁ-ゖゝ-ゟァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")


def quote_skeleton(text: str) -> list[str]:
    return [ch for ch in text if ch in "「」『』≪≫"]


def numbers(text: str) -> list[str]:
    return re.findall(r"\d+(?:\.\d+)?", text.translate(FW_TRANS))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    sys.path.insert(0, str(ROOT))
    import audit_master

    ruby_map = audit_master.load_ruby_map(ROOT / "ruby_map.approved.json")
    entries = json.loads(MASTER.read_text(encoding="utf-8-sig"))["entries"]
    by_seq = {int(entry["sequence"]): entry for entry in entries}
    assert len(entries) == 1500 and set(by_seq) == set(range(1, 1501))
    rows, failures, post_issues = [], [], []
    checks = collections.Counter()
    for sequence, (new_ko, category, reason) in sorted(MANUAL.items()):
        assert 451 <= sequence <= 600
        entry = by_seq[sequence]
        old, source = str(entry["draft_ko"]), str(entry["source_jp"])
        row = {"script": "008", "stable_id": entry["stable_id"], "sequence": sequence,
               "old_ko": old, "new_ko": new_ko, "category": category, "reason": reason,
               "reviewer": "C", "source_jp": source}
        values = {
            "changed": new_ko != old,
            "encoding": "\ufffd" not in new_ko and not any(0x80 <= ord(ch) <= 0x9F for ch in new_ko),
            "width_clear": re.search(r"[０-９]", new_ko) is None and "\u3000" not in new_ko,
            "tag_exact": collections.Counter(TAG_RE.findall(source)) == collections.Counter(TAG_RE.findall(new_ko)),
            "roman_exact": ROMAN_RE.findall(source) == ROMAN_RE.findall(new_ko),
            "quote_exact": quote_skeleton(source) == quote_skeleton(new_ko),
            "newline_exact": source.count("\n") == new_ko.count("\n"),
            "number_exact": numbers(source) == numbers(new_ko),
            "kana_clear": KANA_RE.search(new_ko) is None,
        }
        for key, passed in values.items():
            checks[key] += int(passed)
        if not all(values.values()):
            failures.append({"sequence": sequence, "bad": [k for k, v in values.items() if not v]})
        corrected = dict(entry)
        corrected["draft_ko"] = new_ko
        audit_master.audit_entry(corrected, "008", post_issues, ruby_map=ruby_map)
        rows.append(row)
    assert len({row["stable_id"] for row in rows}) == len(rows)
    assert not failures, failures
    assert not post_issues, [(x["sequence"], x["rule_id"]) for x in post_issues]
    OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    report = {"schema_version": "fatal-twelve-c-008-partial-review-v1",
              "source_authority": "Japanese only", "english_reference_used": False,
              "external_translation_api_used": False, "script": "008", "range": [451, 600],
              "exhaustive_checked": 150, "manual_corrections": len(rows),
              "unchanged_approved": 150 - len(rows), "checks": dict(checks),
              "post_correction_audit_issues": len(post_issues), "failures": failures,
              "master_sha256": sha(MASTER), "output_sha256": sha(OUT)}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

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
OUT = ROOT / "reviews" / "C.manual.008_0601_0750.corrections.jsonl"
REPORT = ROOT / "reviews" / "C.manual.008_0601_0750.report.json"

MANUAL: dict[int, tuple[str, str, str]] = {
    630: ("소냐에게 보였던 무른 면과 꼭 닮은 느낌이었다.", "문법/주어", "그 감각과 무른 면을 병렬 비교한 초벌 문장을 자연스러운 수식 관계로 교정"),
    648: ("그럴 수밖에 없는 이유가 있었다고 해도, 언젠가는 해야만 할 일이었다고 해도, 사실은 변하지 않는다.", "시제/문법", "いずれはそうしなくてはいけなかったこと의 의무와 시제를 자연스럽게 복원"),
    650: ("「하핫, 그럴 리 없잖아. 즐거운 일은 많을수록 좋은 게 당연하지」", "의성어/발화", "일본어 웃음 かかっ를 자연스러운 한국어 웃음으로 직접 번역"),
    655: ("「내가 태어난 곳은 고흐의 수확 같은 풍경이 이어지는, 시대에 뒤처진 시골이었어」", "인용부호/문법", "원문에 없는 작품명 낫표를 제거하고 수식 호흡을 교정"),
    664: ("오데트는 그 말을 듣고 하하하 하고 크게 웃었다.", "의성어", "일본어 웃음 かかか를 자연스러운 한국어 웃음으로 직접 번역"),
    667: ("미하루는 정말 조금도 감상에 젖지 않은 듯한 오데트에게 두려움마저 느끼고 있었다.", "어휘", "感傷を 감상으로만 옮겨 생긴 중의성을 제거"),
    674: ("미하루도 여기까지 오자 속수무책이었다.", "관용구", "お手上げ를 문자 그대로 두 손을 든다고 옮긴 표현을 자연스럽게 교정"),
    689: ("미하루는 보통 긴소매보다 조금 더 길게 입도록 신경 썼고, 반소매 차림일 때는 장갑을 착용했다.", "문법/묘사", "소매 길이와 착용 습관의 수식 관계를 자연스럽게 복원"),
    691: ("혹시라도 살짝 보일 듯할 때는 다른 손이나 가방, 카드북 등으로 손목을 가려 왔다.", "표기", "원문에 없는 카드북 강조 괄호를 제거"),
    694: ("「무슨 카페였더라. 네가 아르바이트하는 곳의 제복은 장갑 착용이 허용돼 있지. 음식점치고는 드문 일이야」", "발화/용어", "なんとか喫茶의 이름을 떠올리지 못하는 거친 발화를 자연스럽게 복원"),
    699: ("「하핫, 무슨 소리야. 나는 말이지, 네가 내 약점을 간파한 게 오히려 상쾌할 정도야」", "의성어/문법", "일본어 웃음을 직접 번역하고 見抜かれて의 피동 관계를 자연화"),
    701: ("「나는 네가 좋아. 연애 감정으로 좋아한다는 말이야」", "발화/의미", "恋愛的な意味でな를 자연스러운 한국어 고백으로 복원"),
    702: ("「넌 남의 약한 모습을 잘 알아차렸어. 나는 그 점에 반해 버린 거지. 뭐, 4번째 선정에서 한 방 먹었을 때부터 신경 쓰이기는 했어」", "어휘/문법", "人の弱さに敏感だった와 惚れた의 관계를 자연스럽게 복원"),
    707: ("「농담 아니야. 너도 나도 약해. 약한 사람끼리는 서로 끌리는 법이야」", "어휘/발화", "奴ら를 사물처럼 들리는 약한 것들로 옮긴 표현 교정"),
    712: ("「하핫, 알고 있어」", "의성어/발화", "일본어 웃음 かかっ를 자연스러운 한국어 웃음으로 직접 번역"),
    716: ("「……뼈저리게」", "관용구", "痛いほど의 강한 이해를 한국어 관용 표현으로 복원"),
    720: ("「하지만 이대로 페데리코에게 지명당하는 것도 재미없어. 나를 찬 대가는 받아 내야 하니, 한 가지 협조해 줘야겠어」", "관용구/주체", "フられちまった借りを返してもらう의 주체와 대가를 자연스럽게 복원"),
    727: ("「하핫, 질투 나네. 그럼 잘 있어」", "의성어/발화", "일본어 웃음 かかっ를 자연스러운 한국어 웃음으로 직접 번역"),
    735: ("「저기…… 미시마 선배. 오늘은 무슨 일이세요?」", "구두점", "말줄임 뒤의 일본어식 쉼표를 한국어 발화 호흡으로 교정"),
    739: ("그건 5월 3일, ≪인과의 때≫ 다음 날이었다.", "고정 용어", "因果の刻의 승인 표기 인과의 때 적용"),
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
        assert 601 <= sequence <= 750
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
              "external_translation_api_used": False, "script": "008", "range": [601, 750],
              "exhaustive_checked": 150, "manual_corrections": len(rows),
              "unchanged_approved": 150 - len(rows), "checks": dict(checks),
              "post_correction_audit_issues": len(post_issues), "failures": failures,
              "master_sha256": sha(MASTER), "output_sha256": sha(OUT)}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

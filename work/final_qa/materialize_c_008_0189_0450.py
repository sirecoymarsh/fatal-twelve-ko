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
OUT = ROOT / "reviews" / "C.manual.008_0189_0450.corrections.jsonl"
REPORT = ROOT / "reviews" / "C.manual.008_0189_0450.report.json"

MANUAL: dict[int, tuple[str, str, str]] = {
    197: ("사정을 모르는 학생들에게는 마오도 그렇고, 내가 기행을 벌인 것처럼 보일지도 모른다.", "수식/주체", "真央も含めて가 사정을 모르는 관찰자 쪽에 붙는 관계를 자연스럽게 복원"),
    221: ("「기적이 일어났다고 생각했어요. 그런데 이상하게도 그 뒤의 기억이 흐릿해서……. 휴교 중에 책을 읽거나 놀았을 텐데 별로 기억나지 않아요」", "중복/문법", "何故かおかしい를 이상하게 뭔가 이상하다고 중복 번역한 표현 교정"),
    239: ("중간에 잠시 쉬어 가야 할 정도로 긴 이야기가 됐다.", "명백한 직역", "休憩を挟む를 휴식을 넣는다고 옮긴 표현 교정"),
    244: ("「나는――살고 싶다고 생각했어. 이 선정을 거치는 동안 여러 마음을 알게 됐고, 또 여러 마음을 맡았어」", "문법/어휘", "想いを知る와 託される의 병렬 및 수동 의미를 자연스럽게 복원"),
    254: ("「미안하지만 나는 찬성할 수 없네. 가능성이…… 너무 희박하잖아?」", "어휘/자연스러움", "可能性はなさ過ぎる의 자연스러운 한국어 표현"),
    260: ("「아니, 달라. 문화제가 끝나면 다시――라고 했잖아. 그러니 이건 부탁이야」", "용어", "学園祭를 기존 시나리오의 승인 표기 문화제로 통일"),
    267: ("「어디까지나 그런 방법이 있다는 전제하에서지만, 찬성할게」", "문법", "方法があればという前提의 인용절과 조사 호응 교정"),
    271: ("「그럼 나는 아르바이트가 있어서 이만 먼저 실례할게」", "문법/발화", "문장 중간에서 끊긴 でね를 자연스러운 퇴장 발화로 복원"),
    273: ("「있잖아, 미하루. 이제 서로 숨기는 일은 없도록 하자. 오늘은 아르바이트가 아니라……스케일 씨 일행을 만나러 가는 거지?」", "문법/자연스러움", "隠し事はもう、なしにしよう의 상호 관계를 자연스럽게 복원"),
    301: ("하지만 나도 예전 그대로일 수는 없다.", "명백한 직역", "今まで通りではいられない의 자연스러운 한국어 표현"),
    312: ("「하지만 그렇기에 나는 둘 다 살아남을 방법이 있는지 제대로 찾아볼 거야. 단서가 완전히 없는 것도 아니야. 예를 들면 이 책」", "이중부정/문법", "方法がないか探す를 방법이 없는지 찾는다는 뜻으로 읽히지 않게 교정"),
    328: ("「운명의 여신……파르카가 꿈의 세계에서 한 말과 같네. ≪운명의 대회랑≫에 ≪운명의 대시계≫」", "고정 용어", "運命の大広間의 승인 표기 운명의 대회랑 적용"),
    344: ("「사과하지 않아도 돼. 나오미가 느낀 그 위화감을 그냥 넘기지 마. 우리는 그런 감각도 없이 눈앞의 일을 받아들여 버렸으니까」", "명백한 직역", "違和感は大切にして를 위화감을 소중히 여긴다고 직역한 표현 교정"),
    358: ("아마 아란 씨도 이미 이곳을 알아봤을지 모른다.", "목적어 누락", "앞 문장의 라이온관 위치를 조사 대상으로 명확하게 복원"),
    384: ("미하루에게는 린카와 자신, 2명이 한편이라는 사실을 끝까지 숨기는 것이 과제였다.", "명백한 직역", "凛火と自分の２를 자신이라는 둘로 옮긴 표현 교정"),
    392: ("「조금 부유해진 탓인지는 모르겠지만, 아무래도 욕심이 생긴 모양이야. 가난한 사람들에게 돈도 빌려주기 시작했다더군」", "명백한 직역", "小金持ちになった弊害의 부자연스러운 폐해 표현 교정"),
    399: ("「그 뒤 10대였던 아란 스코피온이 아버지가 쓰던 거래 경로를 이용해 회사를 세우고 부를 이룬 것은 유명한 이야기지」", "어휘/의미", "父のルート를 추상적인 경로가 아닌 보석 거래망으로 명확화"),
    403: ("「회사나 경영, 재산 같은 건 생각해 봤지만 아니었거든. 당신에게 의지할 수밖에 없어. 잘 부탁해」", "발화", "頼むぜ를 의문문으로 옮긴 오류 교정"),
    414: ("「사람 신경을 긁는 말투를 아는 모양인데, 그래도 오데트만큼은 못하는군」", "명백한 직역", "人が嫌がる言い方의 의도와 비교 대상을 자연스럽게 복원"),
    431: ("「그것보다 말이야. 미하루, 당신은 오데트의 ≪미련≫에 짐작 가는 게 있다고 했지?」", "어휘", "心当たり를 장소를 뜻하는 짚이는 곳으로 옮긴 오류 교정"),
    434: ("「나는 그녀의 미련 자체를 아는 게 아니야. 어디까지나 짐작 가는 게 있을 뿐이야」", "어휘", "心当たり를 장소를 뜻하는 짚이는 곳으로 옮긴 오류 교정"),
    436: ("「아이――나는 그것이 그녀의 미련과 관련 있다고 생각해」", "문법/의미", "未練に繋がる의 관련 관계를 자연스럽게 복원"),
    444: ("미하루는 소피아가 외모와 나이에 비해 영리하다는 걸 알고 있었기에, 그런 소피아가 오데트를 순순히 믿었다는 점을 의심스럽게 여겼다.", "주어/문법", "賢いこと와 素直に信じたこと의 인과·목적어 관계를 자연스럽게 복원"),
    447: ("――소피아는 오데트의 미련을 알았기에, 오데트가 자신에게 자비를 베풀었다는 걸 알아차렸다.", "시제/주어", "慈悲を与えた의 완료 행위와 행위 주체를 명확하게 복원"),
    448: ("「그 여자는 감정에 따라 움직여. 일도 호불호에 따라 받을지 말지 정해……그런 말을 했던 기억은 있어」", "명백한 직역", "好き嫌いで를 좋고 싫음으로 옮긴 표현을 자연스럽게 교정"),
    449: ("「하지만…… 아이라. 당연히 이것만으로는 카드도 생기지 않아」", "발화/조사", "子供、か의 반추하는 말끝을 자연스럽게 복원"),
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
        assert 189 <= sequence <= 450
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
              "external_translation_api_used": False, "script": "008", "range": [189, 450],
              "exhaustive_checked": 262, "manual_corrections": len(rows),
              "unchanged_approved": 262 - len(rows), "checks": dict(checks),
              "post_correction_audit_issues": len(post_issues), "failures": failures,
              "master_sha256": sha(MASTER), "output_sha256": sha(OUT)}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "output" / "masters" / "scenario_011_01.master.json"
OUT = ROOT / "reviews" / "C.011_01.consolidated.corrections.jsonl"
REPORT = ROOT / "reviews" / "C.011_01.consolidated.report.json"

MANUAL: dict[int, tuple[str, str, str]] = {
    7: ("「루 씨라고 읽는구나. 중국 사람일까……」", "고유명사", "魯昌鎬의 승인 표기 루 창호에 맞춰 성씨 읽기를 루로 통일"),
    19: ("――아란 스코피온과 페데리코 카르미나티가 탈락한 지금 우리는 초조해할 필요가 없어. 기말고사를 무사히 마친 뒤 ≪여신의 선정≫에 관해 생각하자.", "명백한 직역", "시험을 이겨 낸다는 부자연스러운 표현을 乗り切る의 의미에 맞게 복원"),
    29: ("내 일이 아닌데도 나는 분했다.", "문법", "感情を思う로 중복된 서술을 자연스럽게 교정"),
    95: ("미하루는 자연스럽게 내게 다가와 왼쪽 소매를 살짝 잡아당겼다.", "어휘/신체", "左手の袖를 왼손 소매라는 비문이 아닌 왼팔 쪽 소매로 복원"),
    142: ("「너도 이미 가진 ≪사인≫ 카드에 관한 이야기야. 내가 나 자신을 죽이게 되기까지의 일을 알아 줬으면 해」", "문법/의미", "ぼくがぼくを殺すに至るまで의 재귀 관계와 과정 표현을 자연스럽게 복원"),
    150: ("「그래. 전에 내 옛날 이야기를 했을 때 아메차에 들어간 뒤 너를 만나기까지를 거의 생략했을 거야. 그 공백을 지금부터 채울게」", "오역/인물", "君に出会う를 마오를 만난 것으로 바꾼 명백한 인물 오역 교정"),
    158: ("「내 아버지, 그러니까 자기 남편이 사고를 냈는데도 이혼하지 않고 잘못을 함께 짊어지며, 어머니는 인생을 다시 시작하려 노력했어」", "문법/주어", "ぼくの父親、自分の夫라는 동격과 어머니의 행동 주체를 복원"),
    163: ("「자신이 저지른 행동의 결과에 대한 책임도, 앞으로 기다리고 있던 죄와 싸우는 나날도 버렸어」", "문법/병렬", "두 목적어와 捨てた의 병렬 관계를 자연스럽게 복원"),
    164: ("「한편으로 내 어머니는 아버지의 죄에서 해방되기도 했어. 자유로워졌다고 해도 돼」", "명백한 직역", "といってもいい의 허용 표현을 자연스럽게 교정"),
    167: ("미하루의 어머니라면 외모가 뛰어나다는 데 의심의 여지가 없고, 미하루도 어머니가 나이와 그간의 고생에 비해 외모도 내면도 젊다고 말했다.", "문법/어휘", "年齢と重ねた苦労の割には의 비교 관계와 内面을 자연스럽게 복원"),
    172: ("「나는 우리 집이 넉넉하지 않다는 걸 알았기에 필사적으로 공부해 명문 진학 학교인 아메차에 장학생으로 들어갔어」", "용어", "進学校를 단순 진학 학교가 아닌 대학 진학 실적이 높은 학교로 명확화"),
    235: ("「나, 나오미랑 내가!」", "말더듬/조사", "わ、私と直未が의 놀란 말더듬과 동반 조사를 자연스럽게 복원"),
    237: ("여신 이야기가 나온 직후에 나오미와 내가 사귀는 꿈이라니.", "말더듬/문법", "한국어에서 성립하지 않는 나, 나오미와 내가라는 반복·조사 교정"),
    240: ("「그 꿈을 꾼 때가 5월 2일과 3일 사이――≪인과의 때≫」", "용어/표기", "因果の刻의 승인 표기 인과의 때와 반각 날짜 적용"),
    276: ("「한 가지만 확인할게」", "명백한 직역", "確認させて의 어색한 사역 표현을 자연스럽게 교정"),
    280: ("아직 알 수 없는 『지명할 사람이 사라졌을 때의 대응』과 린다 씨의 『카드북과 같은 장정의 일기장』도 그렇다.", "인용부호", "원문의 『』 종류와 계층을 정확히 복원"),
    292: ("선정이 막 시작됐을 때 라이온관에서 이야기했을 때처럼, 나도 모르게 또 소리치고 싶어지는 대답이다.", "문법/시점", "選定が始まってすぐ와 종속절의 호응을 자연스럽게 복원"),
    328: ("그렇게 대놓고 말하니 다시 부끄러워졌다.", "명백한 직역", "はっきりと言われると의 발화 태도를 자연스럽게 복원"),
    355: ("「나는 미하루를 좋아해. 하지만 그게 연애 감정으로 좋아하는지는 몰라. 애초에 연애 감정으로 누군가를 좋아한다는 게 뭔지 나는 모르니까」", "문법/용어", "恋愛としての好き와 恋愛的な好き의 자연스러운 한국어 결합"),
    364: ("징그러울 만큼 입가가 헤벌어졌다.", "오역/묘사", "ほっぺたが綻んだ의 웃음을 볼이 느슨해졌다고 직역한 표현 교정"),
    385: ("집에 돌아오자마자 나는 잠자리에 들 준비를 했다.", "어휘", "寝る準備가 잘 준비로 읽히는 중의적 표현 교정"),
    387: ("기말고사 마지막 날이었고, 마오의 권유로 놀러 갔고, 미하루의 고백에 대답을――.", "조사/의미", "고백에 대한 대답의 주체·대상 관계를 자연스럽게 복원"),
}

FW_TRANS = str.maketrans("０１２３４５６７８９％", "0123456789%")
FW_RE = re.compile(r"[０-９]")
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
    assert len(entries) == 408 and set(by_seq) == set(range(1, 409))

    selected: dict[int, tuple[str, str, str]] = {}
    width_sequences = []
    for sequence, entry in by_seq.items():
        old = str(entry["draft_ko"])
        normalized = old.translate(FW_TRANS)
        if normalized != old:
            selected[sequence] = (normalized, "표기", "한국어 target의 전각 숫자·퍼센트를 반각으로 통일")
            width_sequences.append(sequence)
    manual_width_overlap = []
    for sequence, value in MANUAL.items():
        if sequence in selected:
            manual_width_overlap.append(sequence)
        selected[sequence] = value

    rows = []
    checks = collections.Counter()
    failures = []
    post_issues = []
    for sequence, (new_ko, category, reason) in sorted(selected.items()):
        entry = by_seq[sequence]
        old, source = str(entry["draft_ko"]), str(entry["source_jp"])
        row = {"script": "011_01", "stable_id": entry["stable_id"], "sequence": sequence,
               "old_ko": old, "new_ko": new_ko, "category": category, "reason": reason,
               "reviewer": "C", "source_jp": source}
        values = {
            "changed": new_ko != old,
            "encoding": "\ufffd" not in new_ko and not any(0x80 <= ord(ch) <= 0x9F for ch in new_ko),
            "width_clear": FW_RE.search(new_ko) is None and "\u3000" not in new_ko,
            "tag_exact": collections.Counter(TAG_RE.findall(source)) == collections.Counter(TAG_RE.findall(new_ko)),
            "roman_exact": ROMAN_RE.findall(source) == ROMAN_RE.findall(new_ko),
            "quote_exact": quote_skeleton(source) == quote_skeleton(new_ko),
            "newline_exact": source.count("\n") == new_ko.count("\n"),
            "number_exact": numbers(source) == numbers(new_ko),
            "kana_clear": KANA_RE.search(new_ko) is None,
        }
        for name, passed in values.items():
            checks[name] += int(passed)
        if not all(values.values()):
            failures.append({"sequence": sequence, "bad": [k for k, v in values.items() if not v]})
        corrected = dict(entry)
        corrected["draft_ko"] = new_ko
        audit_master.audit_entry(corrected, "011_01", post_issues, ruby_map=ruby_map)
        rows.append(row)

    assert len({row["stable_id"] for row in rows}) == len(rows)
    assert not failures, failures
    assert not post_issues, [(x["sequence"], x["rule_id"]) for x in post_issues]
    OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    report = {
        "schema_version": "fatal-twelve-c-011-01-review-v1",
        "source_authority": "Japanese only", "english_reference_used": False,
        "external_translation_api_used": False, "script": "011_01",
        "exhaustive_checked": 408, "manual_corrections": len(MANUAL),
        "automatic_width_records": len(width_sequences), "manual_width_overlap": manual_width_overlap,
        "output_unique_corrections": len(rows), "unchanged_approved": 408 - len(rows),
        "checks": dict(checks), "post_correction_audit_issues": len(post_issues),
        "failures": failures, "master_sha256": sha(MASTER), "output_sha256": sha(OUT),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

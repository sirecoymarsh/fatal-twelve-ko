#!/usr/bin/env python3
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER_DIR = ROOT / "output" / "masters"
OUT = ROOT / "reviews" / "A.endings.consolidated.corrections.jsonl"
REPORT = ROOT / "reviews" / "A.endings.consolidated.report.json"

SCRIPTS = {
    "BAD_END_01": 58,
    "BAD_END_02": 80,
    "BAD_END_03": 21,
    "BAD_END_04": 43,
    "MIHARU_END": 26,
    "TRUE_END": 125,
    "UNHAPPY_END": 87,
}

# Japanese-source-only semantic decisions.  No official English prose was used.
MANUAL: dict[tuple[str, int], tuple[str, str, str]] = {
    ("BAD_END_01", 14): (
        "「이곳은 기분이 좋아. 할 수만 있었다면 너와 함께 오고 싶었어」",
        "의미/자연스러움",
        "望むことなら의 실현 불가능한 바람을 자연스럽게 복원",
    ),
    ("BAD_END_01", 52): (
        "「별일 아니야. 내가 먼저 말하지 않으면 이제 와서 호칭을 바꿀 수도 없잖아? 그래서야」",
        "어휘",
        "呼び方를 사람을 부르는 호칭으로 명확하게 번역",
    ),
    ("BAD_END_02", 3): (
        "두 사람은 서로 다른 곳에서 저마다 죽음의 운명을 따랐다.",
        "문법",
        "死の運命를 관형절로 잘못 옮긴 표현 교정",
    ),
    ("BAD_END_02", 7): (
        "오구마 마오는 절친의 집 앞에서 나직이 중얼거렸다.",
        "고유명사",
        "小熊의 승인 표기 오구마와 親友의 의미 반영",
    ),
    ("BAD_END_02", 36): (
        "「리땅…… 아, 린카 시시마이 말인가. 알아. 내…… 동료였던 녀석이 꽤나 편을 들어 줬거든」",
        "오역",
        "肩入れする는 마음을 쏟는다는 연애 표현이 아니라 편을 들어 돕는다는 뜻",
    ),
    ("BAD_END_02", 44): (
        "무척 아끼던 두 사람의 흔적을 조금이라도 더 많이 자기 안에 새기고 싶다. 자신이 몰랐던 두 사람의 모습이라면 더더욱.",
        "어조",
        "大好き의 포괄적인 애정을 불필요한 연애 의미 없이 복원",
    ),
    ("BAD_END_02", 62): (
        "그는 자신이 구사할 수 있는 온갖 화술을 동원해 미하루를 설득했다.",
        "명백한 직역",
        "自分の持てる最大限の話術를 자연스러운 한국어로 교정",
    ),
    ("BAD_END_02", 67): (
        "――다만 한 가지, 시시마이 린카의 영혼을 손에 넣을 수는 있다고.",
        "문법/의미",
        "ただ一つ의 제한 강조와 다음 문장으로 이어지는 호흡 복원",
    ),
    ("BAD_END_02", 74): (
        "그 사실도, 털어놓을 용기가 없는 자신에 대한 혐오도 미하루의 마음을 좀먹고 있었다.",
        "문법",
        "話せない勇気のなさと自己嫌悪의 수식 관계를 자연스럽게 복원",
    ),
    ("BAD_END_04", 28): (
        "오구마 마오는 마음에 뻥 뚫린 구멍 때문에 집으로 돌아가지 못하고 있었다.",
        "고유명사",
        "小熊의 승인 표기 오구마 적용",
    ),
    ("BAD_END_04", 35): (
        "피해자의 이름은 시시마이 린카. 참혹하게도 오늘이 17살 생일이었으며, 친구들에게 축하를 받으러 왔던 것이다.",
        "수치/자연스러움",
        "17歳の誕生日를 열일곱 번째 생일이 아닌 나이 17살의 생일로 복원",
    ),
    ("TRUE_END", 24): (
        "「아, 나오링은 집에 있는 유카타를 빌려 입을 거라 현장에서 바로 만나겠대」",
        "발화/문법",
        "直接待ち合わせだって의 전달 발화를 자연스럽게 복원",
    ),
    ("TRUE_END", 37): (
        "「응. 그럼 미하루, 내 방에서 입는 법을 알려 줘」",
        "조사",
        "목적격 조사를 보완해 자연스럽게 교정",
    ),
    ("TRUE_END", 50): (
        "「……나도 모르게 넋을 잃게 되네」",
        "명백한 직역",
        "見惚れてしまう의 자연스러운 한국어 표현",
    ),
    ("TRUE_END", 77): (
        "늘씬한 몸매와 반듯한 얼굴이 어우러져 훨씬 나이가 많아 보인다. 나와 동갑이라고 믿기 어려울 정도로.",
        "어휘/의미",
        "年上를 노화처럼 들리는 나이 들어 보인다 대신 상대적 연상으로 복원",
    ),
    ("TRUE_END", 100): (
        "얼버무리려는 셈이겠지만, 전혀 통하지 않았다.",
        "주체/자연스러움",
        "ごまかせていない의 실패 의미를 자연스럽게 복원",
    ),
    ("TRUE_END", 109): (
        "오히려 내가 더 부끄러워져 한 번 고개를 반대편으로 돌렸다.",
        "명백한 직역",
        "私の方が의 비교 강조를 자연스럽게 복원",
    ),
    ("UNHAPPY_END", 7): (
        "여름방학에는 뭔가 특별한 일이 생기려나, 하고.",
        "조사/의미",
        "夏休みくらいは의 기간·최소 기대를 시점 표현으로 잘못 옮긴 부분 교정",
    ),
    ("UNHAPPY_END", 10): (
        "나도 친구인 마오와 미하루, 후배인 나오미와 함께 평범한 일상을 보내게 되리라는 걸 마음 한편으로는 알고 있다.",
        "주어/문법",
        "私や…と의 동반 관계를 빠짐없이 복원",
    ),
    ("UNHAPPY_END", 12): (
        "그저 문득 산책이나 나가 볼까 하는 생각이 들어, 발길이 이곳으로 향했다.",
        "발화/자연스러움",
        "혼잣생각을 상대에게 권하는 가자고로 옮긴 오류 교정",
    ),
    ("UNHAPPY_END", 31): (
        "그 뒤 남자는 함께 있던 가족과 대화를 나누는데, 중국어라 전혀 알아들을 수 없었다.",
        "주어/문법",
        "중국어로 대화한 주체와 화자의 비이해 관계를 명확하게 복원",
    ),
    ("UNHAPPY_END", 42): (
        "「오, 그림이 될 만한 두 사람 발견. 한 장 찍게 해 줘」",
        "명백한 직역",
        "画になる의 사진으로 보기 좋은 피사체라는 뜻을 자연스럽게 복원",
    ),
    ("UNHAPPY_END", 45): (
        "그들은 모두 키가 컸지만, 전철에서 볼 법한 남고생들처럼 신이 나 있었다.",
        "문법/묘사",
        "단순 대조를 원인처럼 만든 조사와 見る의 장면 표현 교정",
    ),
    ("UNHAPPY_END", 68): (
        "소녀는 곰 인형으로 내게 꾸벅 인사했다.",
        "첨가/자연스러움",
        "ぬいぐるみのくまで에 없는 움직임을 단정한 첨가 제거",
    ),
    ("UNHAPPY_END", 72): (
        "마치 이상한 나라에 와 버린 기분이었지만, 신경 써 봐야 소용없다고 생각하니 이내 아무래도 상관없어졌다.",
        "문법/자연스러움",
        "気にしても無駄だと、どうでもよくなった의 인과와 서술 호흡 복원",
    ),
    ("UNHAPPY_END", 83): (
        "우리는 너무도 당연하게 살아 있다.",
        "어조",
        "当たり前に의 살아 있음에 대한 자각을 자연스럽게 복원",
    ),
}

FW_TRANS = str.maketrans("０１２３４５６７８９％", "0123456789%")
ROMAN_RE = re.compile(r"[\u2160-\u2188]+")
TAG_RE = re.compile(r"\{[^{}]+\}|\[[^\[\]]+\]")
KANA_RE = re.compile(r"[ぁ-ゖゝ-ゟァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")


def quote_skeleton(text: str) -> list[str]:
    return [ch for ch in text if ch in "「」『』≪≫"]


def explicit_numbers(text: str) -> list[str]:
    return re.findall(r"\d+(?:\.\d+)?", text.translate(FW_TRANS))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    sys.path.insert(0, str(ROOT))
    import audit_master

    ruby_map = audit_master.load_ruby_map(ROOT / "ruby_map.approved.json")
    masters: dict[str, dict[int, dict]] = {}
    master_hashes: dict[str, str] = {}
    exhaustive_total = 0
    for script, expected in SCRIPTS.items():
        path = MASTER_DIR / f"scenario_{script}.master.json"
        doc = json.loads(path.read_text(encoding="utf-8-sig"))
        entries = doc["entries"]
        by_seq = {int(entry["sequence"]): entry for entry in entries}
        assert len(entries) == expected
        assert set(by_seq) == set(range(1, expected + 1))
        masters[script] = by_seq
        master_hashes[script] = sha(path)
        exhaustive_total += expected

    rows: list[dict] = []
    checks = collections.Counter()
    failures: list[dict] = []
    post_audit_issues: list[dict] = []
    corrections_by_script = collections.Counter()
    for (script, sequence), (new_ko, category, reason) in sorted(MANUAL.items()):
        entry = masters[script][sequence]
        source = str(entry["source_jp"])
        old = str(entry["draft_ko"])
        row = {
            "script": script,
            "stable_id": entry["stable_id"],
            "sequence": sequence,
            "old_ko": old,
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": "A",
            "source_jp": source,
        }
        values = {
            "changed": new_ko != old,
            "encoding": "\ufffd" not in new_ko and not any(0x80 <= ord(ch) <= 0x9F for ch in new_ko),
            "fullwidth_clear": not re.search(r"[０-９]", new_ko) and "\u3000" not in new_ko,
            "tag_exact": collections.Counter(TAG_RE.findall(source)) == collections.Counter(TAG_RE.findall(new_ko)),
            "roman_exact": ROMAN_RE.findall(source) == ROMAN_RE.findall(new_ko),
            "quote_exact": quote_skeleton(source) == quote_skeleton(new_ko),
            "newline_exact": source.count("\n") == new_ko.count("\n"),
            "numbers_exact": explicit_numbers(source) == explicit_numbers(new_ko),
            "residual_kana_clear": KANA_RE.search(new_ko) is None,
        }
        for key, passed in values.items():
            checks[key] += int(passed)
        if not all(values.values()):
            failures.append({"script": script, "sequence": sequence, "bad": [k for k, v in values.items() if not v]})
        corrected = dict(entry)
        corrected["draft_ko"] = new_ko
        audit_master.audit_entry(corrected, script, post_audit_issues, ruby_map=ruby_map)
        rows.append(row)
        corrections_by_script[script] += 1

    assert len({row["stable_id"] for row in rows}) == len(rows)
    assert not failures, failures
    assert not post_audit_issues, [(x["script"], x["sequence"], x["rule_id"]) for x in post_audit_issues]

    OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    report = {
        "schema_version": "fatal-twelve-ending-review-v1",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "scripts": SCRIPTS,
        "exhaustive_checked": exhaustive_total,
        "manual_corrections": len(rows),
        "corrections_by_script": dict(sorted(corrections_by_script.items())),
        "unchanged_approved": exhaustive_total - len(rows),
        "stable_id_unique": len({row["stable_id"] for row in rows}),
        "checks": dict(checks),
        "post_correction_audit_issues": len(post_audit_issues),
        "failures": failures,
        "master_sha256": master_hashes,
        "output_sha256": sha(OUT),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

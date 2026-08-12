#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "output" / "masters" / "scenario_012_01GH.master.json"
SEEDS = ROOT / "reviews" / "ROOT.corrections.jsonl"
OUT = ROOT / "reviews" / "ROOT.012_01GH.consolidated.corrections.jsonl"
REPORT = ROOT / "reviews" / "ROOT.012_01GH.consolidated.report.json"

# Japanese-source-only semantic review decisions.  Seed typography/name fixes
# are merged below, so overlapping rows already contain the normalized form.
MANUAL: dict[int, tuple[str, str, str]] = {
    11: ("아니, 침착하도록 하죠.", "문법/말투", "落ち着きましょう의 자기 권유형을 자연스럽게 복원"),
    25: ("「리, 린카 선배, 왜 그러세요? 커, 컬러 렌즈예요?」", "용어/말더듬", "カラコン은 서클 렌즈로 한정되지 않는 컬러 렌즈이며 첫음절 말더듬 보존"),
    31: ("「아니, 아니, 아니…… 선배, 말투가 평소보다 왠지 우아하고…… 너무 어색해서요……」", "명백한 직역", "違和感がある를 한국어 대화체로 교정"),
    41: ("역시 당당하게 나간 게 정답이었네요.", "명백한 직역", "堂々としていて正解의 행동 의미를 자연스럽게 복원"),
    45: ("잠시 뜸을 들인 뒤, 시시마이 린카의 기억을 끌어냅니다.", "오역", "少し時間を置いて는 시간을 들여 작업한다는 뜻이 아니라 잠시 간격을 둔다는 뜻"),
    68: ("취미나 기호가 의심을 사더라도, 차츰 제 것으로 바꾸어 가는 편이 좋겠죠.", "문법/의미", "趣味趣向이 의심받는 것이 아니라 갑작스러운 변화가 의심을 산다는 관계 복원"),
    74: ("잡담이라는 건 이런 것이군요.", "용어/의미", "世間話는 세상 돌아가는 이야기가 아니라 일상적인 잡담"),
    77: ("조금 뒤, 나오미 님이 진지한 표정으로 말합니다.", "어휘", "神妙な顔의 문맥상 의미를 진지한 표정으로 통일"),
    78: ("진지하다는 것도 재미있는 말이네요.", "어휘", "앞 문장의 神妙 말놀이를 동일 어휘로 연결"),
    79: ("저도 그녀를 따라 진지한 표정을 지어 보죠. 여신이 진지한 표정이라니. 전직이지만요.", "어휘/문맥", "연속된 神妙 말놀이와 元女神 농담을 자연스럽게 연결"),
    80: ("「이제 슬슬…… 놀이공원에 가지 않으실래요? 그게…… 미시마 선배를 잊은 건 아니에요」", "호칭/높임말", "未島先輩의 성씨 표기와 후배가 선배에게 쓰는 권유형 복원"),
    82: ("「가기로 했던 놀이공원에 가서…… 슬퍼하고, 그리워하고…… 울고. 그래도 3명이 함께라고 실감하면서」", "오역/숫자", "惜しんで는 고인을 아쉬워한다기보다 그리워하고 애도한다는 뜻이며 전각 숫자 정규화"),
    83: ("「물론 제가 미시마 선배를 대신할 수 있다고는 생각하지 않아요. 그래도 린카 선배도 마오 선배도 조금씩 앞을 바라봐 주셨으면 해요」", "호칭", "未島先輩를 전역 고정 성씨 호칭 미시마 선배로 복원"),
    90: ("「……그러게. 신경 쓰게 만들었네, 미안해. 그래도 고마워. 마오한테는 내가 먼저 말을 걸어 볼게」", "의미", "私から声をかける의 먼저 다가가 말을 건다는 의미 복원"),
    97: ("눈동자 색 같은 건 당당하게 굴면 역시 괜찮은 거였네요.", "명백한 직역", "堂々としている를 부자연스러운 위치 표현이 아닌 태도로 번역"),
    98: ("문제는 속에 든 것. 음, 좋은 말이네요.", "오역/말장난", "中身는 내용물이 아니라 몸 안의 인격을 가리키는 이중 의미"),
    107: ("어째서인지 머리에 통증이 내리쳤습니다.", "명백한 직역", "痛みが走る의 한국어 관용 표현 교정"),
    124: ("저는 설거지를 하고 전표를 준비했습니다. 이런 작업 역시 몸이 기억하고 있습니다.", "오역", "この辺りの作業를 장소인 이 근처의 작업으로 옮긴 오류 교정"),
    134: ("아까보다 더 날카로운 통증이 머리를 내리쳤습니다.", "명백한 직역", "痛みが頭を走る의 부자연스러운 직역 교정"),
    148: ("서로 짝을 이룬 컵인 건 친구와 함께 쓰던 거라서일까요.", "문법/의미", "お揃いのカップ와 친구 소유 관계를 자연스럽게 복원"),
    154: ("「돌려주지 않겠어요」", "높임말", "返しませんわ의 목적어에게 불필요하게 붙은 드리다 제거"),
    155: ("「당신이라고 해도 이제는 저를 뜻하니까요」", "의미", "貴女サマとはもうワタクシのこと의 지칭 관계 복원"),
    182: ("기말고사 결과가 나오고 통지표가 배부되면서, 사립 아메차 여자대학교 부속 고등학교 2학년인 나의 1학기가 막을 내렸다.", "문법/숫자", "시험 결과 반환이라는 번역투를 고치고 전각 숫자를 반각으로 정규화"),
    183: ("두근거리며 시험 결과를 보고 있자 마오가 재미있다는 듯 캐물었다.", "오역", "食いついてきた를 신체적으로 달라붙었다고 옮긴 오류 교정"),
    188: ("분명 마오의 점수가 나보다 낮을 터였다.", "시제/문법", "성적표를 보기 전 추측 장면의 시제와 중복 확신 표현 교정"),
    195: ("「뭐, 아무튼 이걸로 시험도 끝났네. 여름 방학엔 뭐 할까?」", "말투", "まあまあ를 말더듬처럼 옮긴 표현 교정"),
    227: ("에어컨을 켜고 싶어질 만큼 더운 밤에도 슬슬 질릴 무렵이었다.", "문법/의미", "暑い夜にも嫌気が差す의 주체와 상태를 자연스럽게 복원"),
    230: ("위협 같은 건 하지 않고 내 옆에서 몸을 둥글게 웅크린다.", "명백한 직역", "猫が丸くなる의 자연스러운 한국어 묘사"),
    234: ("게다가 카드북은 ≪운명의 대회랑≫이 붕괴할 때 함께 사라졌으니, 이제 와서 그 영어를 읽기란 지극히 어려운 일이다.", "고정 표기", "カードブック 고정 표기를 카드북으로 통일"),
    255: ("내 마음속 목소리가 그에게 전해지는 모양인지, 후후, 웃는 소리가 들린다.", "명백한 직역", "微笑む声를 미소 짓는 목소리라고 한 비자연적 결합 교정"),
    259: ("알아차리지 못하고 있다", "시제/선택지", "현재 상태를 묻는 선택지 気付いていない의 시제 복원"),
    265: ("「여신은 ≪{rb}마음{/rb}{rt}꿈{/rt}의 조각≫이라고 표현했지만, 틀림없이 인간의 지혜를 초월한 에너지라 불리는 것이지」", "오역", "人智를 단순 인지로 축소한 오류 교정; ruby 구조 보존"),
    279: ("「첫 번째는 ≪여신의 선정≫에 참가한 모두가 살아 있는 세계를 자아내고, ≪인과의 때≫ 자체를 ≪없었던 일≫로 만드는 것」", "고정 용어", "因果の刻의 고정 표기 인과의 때 적용"),
    280: ("「그 대가로 그동안의 기억은 세계에서 잊힌다. 물론 너 자신의 기억도. 네가 기억하고 있다면 세계가 원래대로 돌아가려 할 테니까」", "문법/의미", "世界から記憶は忘却される의 피동 관계와 생략된 記憶 복원"),
    285: ("아무튼 그가 제시한 두 가지 선택지는 이해하기 쉽다.", "명백한 직역", "二択ならば分かりやすい의 자연스러운 한국어 표현"),
}

FW_TRANS = str.maketrans("０１２３４５６７８９％", "0123456789%")
ROMAN_RE = re.compile(r"[\u2160-\u2188]+")
TAG_RE = re.compile(r"\{[^{}]+\}|\[[^\[\]]+\]")
KANA_RE = re.compile(r"[ぁ-ゖゝ-ゟァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def quote_skeleton(text: str) -> list[str]:
    return [ch for ch in text if ch in "「」『』≪≫"]


def explicit_numbers(text: str) -> list[str]:
    text = text.translate(FW_TRANS)
    return re.findall(r"\d+(?:\.\d+)?", text)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    master_doc = json.loads(MASTER.read_text(encoding="utf-8-sig"))
    entries = master_doc["entries"]
    by_seq = {int(e["sequence"]): e for e in entries}
    assert len(entries) == 313 and set(by_seq) == set(range(1, 314))

    seed_rows = [r for r in load_jsonl(SEEDS) if r.get("script") == "012_01GH"]
    assert len(seed_rows) == 13
    by_stable = {e["stable_id"]: e for e in entries}
    for row in seed_rows:
        e = by_stable[row["stable_id"]]
        assert row["old_ko"] == e["draft_ko"]
        assert int(row["sequence"]) == int(e["sequence"])

    selected: dict[int, dict] = {int(r["sequence"]): dict(r) for r in seed_rows}
    overlap = []
    for sequence, (new_ko, category, reason) in MANUAL.items():
        e = by_seq[sequence]
        if sequence in selected:
            overlap.append(sequence)
        selected[sequence] = {
            "script": "012_01GH",
            "stable_id": e["stable_id"],
            "sequence": sequence,
            "old_ko": e["draft_ko"],
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": "ROOT",
            "source_jp": e["source_jp"],
        }

    rows = [selected[k] for k in sorted(selected)]
    assert len({r["stable_id"] for r in rows}) == len(rows)
    checks = Counter()
    failures: list[dict] = []
    for row in rows:
        e = by_seq[int(row["sequence"])]
        old, new, source = e["draft_ko"], row["new_ko"], e["source_jp"]
        checks["old_guard"] += row["old_ko"] == old
        checks["changed"] += new != old
        checks["encoding"] += "\ufffd" not in new and not any(0x80 <= ord(c) <= 0x9F for c in new)
        checks["fullwidth_clear"] += not re.search(r"[０-９]", new) and "\u3000" not in new
        checks["tag_exact"] += Counter(TAG_RE.findall(source)) == Counter(TAG_RE.findall(new))
        checks["roman_exact"] += ROMAN_RE.findall(source) == ROMAN_RE.findall(new)
        checks["quote_exact"] += quote_skeleton(source) == quote_skeleton(new)
        checks["newline_exact"] += source.count("\n") == new.count("\n")
        checks["numbers_exact"] += explicit_numbers(source) == explicit_numbers(new)
        checks["residual_kana_clear"] += KANA_RE.search(new) is None
        bad = []
        if row["old_ko"] != old: bad.append("old_guard")
        if new == old: bad.append("no_op")
        if "\ufffd" in new or any(0x80 <= ord(c) <= 0x9F for c in new): bad.append("encoding")
        if re.search(r"[０-９]", new) or "\u3000" in new: bad.append("fullwidth")
        if Counter(TAG_RE.findall(source)) != Counter(TAG_RE.findall(new)): bad.append("tags")
        if ROMAN_RE.findall(source) != ROMAN_RE.findall(new): bad.append("roman")
        if quote_skeleton(source) != quote_skeleton(new): bad.append("quotes")
        if source.count("\n") != new.count("\n"): bad.append("newline")
        if explicit_numbers(source) != explicit_numbers(new): bad.append("numbers")
        if KANA_RE.search(new): bad.append("residual_kana")
        if bad:
            failures.append({"sequence": row["sequence"], "bad": bad})
    assert not failures, failures

    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    report = {
        "schema_version": "fatal-twelve-root-consolidated-review-v1",
        "script": "012_01GH",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "exhaustive_checked": 313,
        "manual_corrections": len(MANUAL),
        "seed_corrections": len(seed_rows),
        "seed_manual_overlap_sequences": overlap,
        "output_unique_corrections": len(rows),
        "checks": dict(checks),
        "failures": failures,
        "master_sha256": sha(MASTER),
        "seed_sha256": sha(SEEDS),
        "output_sha256": sha(OUT),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

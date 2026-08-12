from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent
MASTER = BASE / "output" / "masters" / "scenario_009.master.json"
EXISTING = BASE / "reviews" / "ROOT.corrections.jsonl"
OUTPUT = BASE / "reviews" / "ROOT.manual.009_001_0884.corrections.jsonl"
REPORT = BASE / "reviews" / "ROOT.manual.009_001_0884.report.json"


CANDIDATES = [
    (16, "인도인이라고는 생각하기 힘든, 아란 스코피온이라는 이름.", "문법/부자연스러움", "한국어 수식 관계와 문장 호흡 교정"),
    (17, "그는 그 이름을 지었을 때 자신의 진정한 인생을 시작할 각오를 다졌다.", "조사/문법", "이름과 각오 사이 조사 관계 교정"),
    (64, "「조사해 보니 채택된 사진은 거의 없었던 모양이라…… 돈이 되지 않았다는 뜻이죠. 그래서 린카 선배가 번뜩이는 아이디어를 내 줬어요!」", "오역", "ひらめいてくれました 의미 복원"),
    (83, "「응, 나도 생각해 봤어. 하지만 스케일 씨는 이곳도 우리 할머니 집도 금방 알아낼 거야――너도 알고 있을 거라고 생각해. 위험에 휘말리게 할 수는 없어.」", "주체/의미", "分かっている의 인식 주체 복원"),
    (91, "「그러니까 지금 남아 있는 모두가 서로를 지명하면 이제 누구도 다른 누구를 지명할 수 없게 돼. 그러면 다들…… 살아남을 수 있지 않을까?」", "중복/문법", "중복 제거 및 논리 명확화"),
    (130, "「어라, 그러고 보니 월요일인데 오늘은 일찍 왔네, 마오. 어제는 밤늦게까지 안 깨어 있었구나.」", "오역", "夜更かし는 밤샘이 아니라 늦게까지 깨어 있음"),
    (133, "「그래서 어제는 일찍 자 버린 거지. 여배우 이야기인데, 마오 님의 추천작! 리땅은 꼭 읽어 봤으면 좋겠어.」", "누락", "빠진 첫 문장 복원"),
    (174, "「그걸 미하루에게 전하다니, 오데트가 무슨 생각을 한 건지 알 수가 없군. 자네가 정보를 모두 모아 탈락시켜 준 덕분에 나는 크게 도움을 받았어.」", "주체/의미", "행위 주체와 도움 관계 복원"),
    (210, "「너는……. 아, 그러고 보니 네 나라에서는 술이 금지였던가?」", "오역", "ああ 감탄 오역 교정"),
    (250, "나는 웬일로 소매를 걷어붙였다.", "의미", "珍しく의 평소와 다름 복원"),
    (264, "「하핫, 아프군.」", "오역/감탄", "かかっ 웃음 직접 해석"),
    (316, "「나는 정의에 따라 행동하고 있는 거야.」", "명백한 직역", "正義の下に 자연화"),
    (318, "첫인사 따위는 선정 참가자끼리 필요 없다.", "명백한 부자연스러움", "初めましての挨拶 직역 교정"),
    (321, "그는 말을 더듬지도 않고 술술 대답했다.", "의미 누락", "言葉につっかえる의 부정 의미 복원"),
    (323, "――믿을 수 없어. 미리 들은 미하루의 이야기만으로도 그렇게 생각했지만, 역시 이 사람은 믿을 수 없다.", "문법", "앞뒤 판단 연결 교정"),
    (329, "「하하하, 진정해, 아가씨. 앞으로 이 아이에게 무슨 짓을 할 생각은 없어――지금으로서는 말이야.」", "오역", "落ち着いてくれ 의미 복원"),
    (354, "여신의 선정 자체에 의문을 품은 적도 있지만, 결국 답에 다가가기는커녕 의문만 깊어질 뿐이었다.", "중복/논리", "답과 수수께끼의 대조 명확화"),
    (378, "그가 던진 질문은 나도, 아마 나오미도 알고 싶었던 것이었다.", "주어/문법", "질문과 알고 싶은 사람 관계 교정"),
    (380, "「나는 이번 선정이 시작될 때까지 꿈속에서 여신 파르카와 대화할 수 있었어.」", "조사/문법", "선정을 타동사로 처리한 오류 교정"),
    (401, "「미하루와 내가 마지막 두 사람이 되었을 때, 역시 미하루는 그 한 자리를 내게 양보할 생각이었던…… 거지. 서로를 지명하고, 미하루는 방어하지 않는다…… 그런 거지?」", "문법/발화 호흡", "의미를 방해하는 잘못된 끊김 정리"),
    (419, "「의미가 없지 않아요! 미하루 선배는 그만큼 린카 선배가 살아남을 수 있도록 고민해서――」", "문법/의미", "考えて의 목적과 방향 복원"),
    (438, "「시간이 지나면 괜찮을…… 거라고 생각해. 하지만 내 책임이야. 내가 스케일 씨의 말에 마음이 흔들렸으니까, 미하루는 그게 불가능하다고 알려 주려고……」", "오역", "傾いた의 마음이 흔들린 의미 복원"),
    (443, "「……갈수록 모르겠어요. 여신님과 ≪여신의 선정≫은 대체 뭘까요?」", "조사", "두 의문 대상의 병렬 조사 교정"),
    (451, "「선배와 만난 것, 선배가 저를 구하고 죽은 것, 제가 살해당한 것, 선배에게 도움을 받은 것.」", "조사", "도움을 준 사람에 붙는 조사 교정"),
    (468, "「……선배가 여전히 선배다워서 정말 안심했어요.」", "문법", "선배답다와 안도감 연결 교정"),
    (507, "나와 마찬가지로 미하루도 사복을 입고 있었다. 교복이었다면 경찰이 말을 걸 가능성이 커진다.", "피동/논리", "말을 거는 행위 방향 복원"),
    (515, "「그뿐만 아니라 반드시 이야기해 두어야 할 것이 있어. 내가 여신 파르카와 대화를 나누며 들은 이야기야.」", "문법/중복", "듣고 이야기한다는 관계 명확화"),
    (523, "미하루의 생일은 12월 12일. 나보다 늦을 것이다.", "오자", "초벌의 ‘뒤여야’ 교정"),
    (547, "「그걸로 충분하지 않을까? 설명할 수 없는 일은 설명할 수 없는 채로 두어도 괜찮다고 생각해. 여신도 자세한 이야기는 하지 않으니까.」", "명백한 직역", "理由のつかない 자연화"),
    (587, "미하루의 속눈썹 끝에는 야경에서 흩어진 빛 알갱이가 맺혀 있었다.", "이미지 오역", "야경의 빛이 속눈썹에 맺힌 이미지 복원"),
    (605, "「자, 잠깐만. 내, 내 예상이 맞다면, 그, 자, 잠깐만. 내가 마, 마음의 준비가…… 그게, 왜냐하면……」", "말더듬 누락", "원문의 당황한 말더듬과 반복 복원"),
    (616, "다른 사람이 보내는 진지한 연애 감정이 이토록 마음을 뒤흔든다는 것을.", "명백한 직역", "恋愛的な好意 자연화"),
    (633, "「즉답으로 거절당하지 않은 것만으로도 지금은 충분하려나. 확실히 입 밖에 내고 나니 오히려 후련해졌어.」", "문법/의미", "거절 결과와 고백 뒤 후련함 명확화"),
    (636, "그리고 그렇게 들뜬 마음도 미하루의 한마디로 갑자기 현실로 되돌아왔다.", "조사/중복", "중복 조사 제거 및 원인 관계 교정"),
    (648, "결국 둘만 남았고, 대답을 보류했다고는 해도 몹시 어색했다.", "문법/부자연스러움", "둘만 남은 상황과 보류된 대답 관계 명확화"),
    (675, "고백에 뒤따르는 것은 대답이다.", "명백한 직역", "고백 뒤 대답이 따른다는 의미 자연화"),
    (680, "내가 마오에게 어떤 질문을 할지 예상하고 있었던 모양이다.", "목적어 누락", "질문의 상대 마오 복원"),
    (681, "「그래도 내가 아는 건 말이야, 미하룽에게는 결코 어중간한 각오가 아니었겠구나, 그 정도려나.」", "문법", "판단 범위와 말끝 연결 교정"),
    (707, "전원이 살아남을지도 모른다――나뿐만 아니라 스케일 씨도 내놓았던 이 제안을 다시 한번 진지하게 검토하고 있었다.", "동사/문법", "제안을 내놓고 검토한다는 행위 관계 교정"),
    (716, "「나오미에게 이야기를 들어 달라고 하자.」", "목적어 누락", "이야기를 들어 줄 상대 나오미 복원"),
    (727, "마오는 미하루의 마음 자체는 알아차리고 있다고 말했지만, 함부로 이야기할 일도 아니다.", "삽입 오역", "근거 없이 삽입된 ‘나오미도’ 제거"),
    (745, "게이코 씨를 내버려 둘 수 없었던 것도, 그날 쓰러진 소냐에게 말을 건 것도, 시게쓰구 씨의 부탁을 들어준 것도 모두 내 의지인 동시에 내 의지가 아니었다.", "오역", "お願いを聞いた의 부탁을 들어준 의미 복원"),
    (763, "「그게, 그러니까, 저……. 제가 하고 싶은 말은…… 이건 지금까지와 아무것도 달라지지 않았잖아요? 미하루 선배와 둘이 남는다는 것도, 제가 무거운 짐을 함께 짊어지는 것도요.」", "문법/발화", "문장 성분과 망설이는 발화 복원"),
    (787, "우리 집에서도 걸어서 갈 수 있을 만큼 가까운 곳인 모양이다.", "의미", "徒歩圏内 의미 복원"),
    (796, "그런 번화가의 골목으로 들어서자, 미리 듣지 않았다면 놓쳤을 법한 작은 간판이 보였다.", "문법", "조건절과 발견 장면 연결 교정"),
    (808, "여러 과일을 짜 만든 믹스 주스. 제대로 된 잔에 담겨 생오렌지가 꽂혀 있다.", "문법/묘사", "주스·잔·오렌지 장식 관계 명확화"),
    (824, "「여신은 여러 사람이 남았을 때를 두고 『그때가 오면 알려 주겠다』며 모호하게 말했어.」", "오역", "お楽しみ를 답을 유보한 의미로 복원"),
    (837, "아마 그런 생각이 얼굴에 드러나서 그를 의심하는 기색이 역력했을 것이다.", "중복", "같은 확신을 나타내는 표현 중복 제거"),
    (839, "「그래서 한 번 내 지금까지의 인생을 들어 줬으면 해. 넌 내 정보를 알고 있을 거야. 이제 내 카드를 얻어 갈까 봐 걱정할 필요도 없으니까.」", "주체/문법", "정보를 아는 사람과 카드를 얻는 사람 관계 명확화"),
    (847, "동생인 스케일 씨는 입버릇처럼 「형이라면」이라는 말을 계속 들었고, 그 말은 이윽고 저주가 되었다.", "주어 누락", "비교를 계속 당한 사람이 스케일임을 복원"),
    (848, "비교당하는 데 정신적인 고통을 느끼고, 어릴 때 늘 함께 놀았던 형 앞에서 열등감을 느끼며 시기하기 시작했다.", "오역", "卑屈의 열등감과 위축 의미 복원"),
    (853, "이윽고 그는 광고를 배우고 싶어져 도시의 대학에서 그래픽 디자인을 전공했다.", "표현/문법", "학업 동기와 전공 선택 관계 자연화"),
    (854, "앞으로의 시대에는 사진을 찍기만 해서는 사업으로 이어지기 어렵다고 생각했기 때문이다.", "조사 누락", "사진 촬영만으로 사업이 되기 어렵다는 조건 복원"),
    (858, "「한순간 한순간을 담아내는 사진의 궁극적인 형태야. 지식과 경험, 그리고 운이 없으면 최고의 사진은 절대로 찍을 수 없어!」", "명백한 직역", "切り取る를 순간을 담아낸다는 뜻으로 자연화"),
    (860, "카메라 이야기를 하는 그의 얼굴을 보고 나는 그런 생각이 들었다.", "명백한 부자연스러움", "‘감상을 품다’식 직역 교정"),
    (862, "아란 씨에게 전해 들은 정보나 생성된 카드만으로 그를 짐작했을 때와는 인상이 전혀 달랐다.", "문법/의미", "간접 정보 판단과 직접 본 인상 대비 복원"),
    (865, "「자국 선수가 금메달을 따는 순간을 촬영하고 싶다――이것이 지금도 품고 있는 내 ≪미련≫이야.」", "시제/문법", "현재까지 이어지는 소망의 시제 복원"),
    (873, "「숨겨 둔 자식 주변의 과격한 친구들이 중심이 되어 사소한 괴롭힘을 거듭했지.」", "주체/의미", "괴롭힘 주체와 積み上げた의 반복·누적 의미 복원"),
    (876, "「괴롭힘이라고 해도 경범죄에 해당하는 일까지 있었어. 무엇보다 A의 정신은 차츰 좀먹혀 갔지. 그리고 결국 A는――자살했어.」", "문법/의미", "괴롭힘·정신 훼손·자살의 인과 명확화"),
    (883, "스케일 씨는 지금까지의 이야기를 열기를 띠며 마무리했다.", "문법/부자연스러움", "이야기 마무리 서술 자연화"),
]


TAG_RE = re.compile(r"\{[^{}\n]*\}|\[[^\[\]\n]*\]")
NUM_RE = re.compile(r"[0-9０-９]+")
QUOTE_CHARS = "「」『』≪≫“”‘’\""
FW_TRANS = str.maketrans("０１２３４５６７８９", "0123456789")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def normalized_numbers(text: str) -> list[str]:
    return [m.translate(FW_TRANS) for m in NUM_RE.findall(text)]


NUMBER_WORDS = {
    "0": ("\uc601", "\uc81c\ub85c"),
    "1": ("\ud558\ub098", "\ud55c \uba85", "\ud55c \uc0ac\ub78c"),
    "2": ("\ub458", "\ub450 \uba85", "\ub450 \uc0ac\ub78c"),
    "3": ("\uc14b", "\uc138 \uba85", "\uc138 \uc0ac\ub78c"),
    "4": ("\ub137", "\ub124 \uba85", "\ub124 \uc0ac\ub78c"),
    "5": ("\ub2e4\uc12f",),
    "6": ("\uc5ec\uc12f",),
    "7": ("\uc77c\uacf1",),
    "8": ("\uc5ec\ub35f",),
    "9": ("\uc544\ud649",),
    "10": ("\uc5f4",),
    "11": ("\uc5f4\ud558\ub098", "\uc5f4\ud55c"),
    "12": ("\uc5f4\ub458", "\uc5f4\ub450"),
}


def numbers_semantically_preserved(old_numbers: list[str], new_text: str) -> tuple[bool, list[dict]]:
    new_numbers = normalized_numbers(new_text)
    if old_numbers == new_numbers:
        return True, [{"mode": "digit_exact_or_fullwidth_normalized", "values": old_numbers}]
    remaining = Counter(new_numbers)
    evidence = []
    for number in old_numbers:
        if remaining[number]:
            remaining[number] -= 1
            evidence.append({"value": number, "mode": "digit"})
            continue
        matched_word = next((word for word in NUMBER_WORDS.get(number, ()) if word in new_text), None)
        if matched_word is None:
            return False, evidence + [{"value": number, "mode": "missing"}]
        evidence.append({"value": number, "mode": "korean_number_word", "text": matched_word})
    if any(remaining.values()):
        return False, evidence + [{"mode": "unexpected_new_digits", "values": list(remaining.elements())}]
    return True, evidence


def validation(entry: dict, new_ko: str) -> dict:
    old_ko = entry["draft_ko"]
    protected = entry.get("protected_tokens") or []
    protected_diffs = []
    protected_values = sorted({
        token.get("value") if isinstance(token, dict) else token
        for token in protected
        if not (isinstance(token, dict) and token.get("kind") == "number")
    })
    for token in protected_values:
        old_count = old_ko.count(token)
        new_count = new_ko.count(token)
        if old_count != new_count:
            protected_diffs.append({"token": token, "old_count": old_count, "new_count": new_count})

    old_numbers = normalized_numbers(old_ko)
    new_numbers = normalized_numbers(new_ko)
    numbers_pass, number_evidence = numbers_semantically_preserved(old_numbers, new_ko)
    old_quotes = Counter(ch for ch in old_ko if ch in QUOTE_CHARS)
    new_quotes = Counter(ch for ch in new_ko if ch in QUOTE_CHARS)
    old_tags = Counter(TAG_RE.findall(old_ko))
    new_tags = Counter(TAG_RE.findall(new_ko))
    checks = {
        "protected_tokens_pass": not protected_diffs,
        "numbers_pass": numbers_pass,
        "quotes_pass": old_quotes == new_quotes,
        "renpy_tags_pass": old_tags == new_tags,
    }
    return {
        **checks,
        "pass": all(checks.values()),
        "protected_token_differences": protected_diffs,
        "old_numbers_normalized": old_numbers,
        "new_numbers_normalized": new_numbers,
        "number_preservation_evidence": number_evidence,
        "old_quotes": dict(old_quotes),
        "new_quotes": dict(new_quotes),
        "old_renpy_tags": dict(old_tags),
        "new_renpy_tags": dict(new_tags),
    }


def main() -> None:
    if len(CANDIDATES) != 60:
        raise SystemExit(f"candidate count mismatch: {len(CANDIDATES)}")
    sequences = [item[0] for item in CANDIDATES]
    if len(set(sequences)) != len(sequences):
        raise SystemExit("duplicate candidate sequence")
    if min(sequences) < 1 or max(sequences) > 884:
        raise SystemExit("candidate sequence outside 1..884")

    master = json.loads(MASTER.read_text(encoding="utf-8"))
    entries = master["entries"]
    by_sequence: dict[int, list[dict]] = {}
    for entry in entries:
        by_sequence.setdefault(entry["sequence"], []).append(entry)

    existing_rows = []
    for line_no, line in enumerate(EXISTING.read_text(encoding="utf-8-sig").splitlines(), 1):
        if line.strip():
            row = json.loads(line)
            row["_line"] = line_no
            existing_rows.append(row)
    existing_by_id: dict[str, list[dict]] = {}
    for row in existing_rows:
        existing_by_id.setdefault(row["stable_id"], []).append(row)

    written = []
    overlaps = []
    no_ops = []
    validations = []
    for sequence, new_ko, category, reason in CANDIDATES:
        matches = by_sequence.get(sequence, [])
        if len(matches) != 1:
            raise SystemExit(f"sequence {sequence}: expected one master entry, got {len(matches)}")
        entry = matches[0]
        stable_id = entry["stable_id"]
        old_ko = entry["draft_ko"]
        check = validation(entry, new_ko)
        validations.append({"sequence": sequence, "stable_id": stable_id, **check})

        overlap_rows = existing_by_id.get(stable_id, [])
        if overlap_rows:
            overlaps.append({
                "sequence": sequence,
                "stable_id": stable_id,
                "candidate_old_ko_sha256": hashlib.sha256(old_ko.encode("utf-8")).hexdigest(),
                "candidate_new_ko_sha256": hashlib.sha256(new_ko.encode("utf-8")).hexdigest(),
                "existing_rows": [
                    {
                        "line": row["_line"],
                        "old_ko_exact_match": row.get("old_ko") == old_ko,
                        "new_ko_exact_match": row.get("new_ko") == new_ko,
                        "existing_old_ko": row.get("old_ko"),
                        "existing_new_ko": row.get("new_ko"),
                        "category": row.get("category"),
                        "reason": row.get("reason"),
                    }
                    for row in overlap_rows
                ],
                "omitted_from_new_file": True,
            })
            continue

        if old_ko == new_ko:
            no_ops.append({"sequence": sequence, "stable_id": stable_id})
            continue

        written.append({
            "script": "009",
            "stable_id": stable_id,
            "sequence": sequence,
            "old_ko": old_ko,
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": "ROOT",
        })

    failures = [row for row in validations if not row["pass"]]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in written),
        encoding="utf-8",
        newline="\n",
    )

    report = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "script": "009",
        "review_scope": {"sequence_start": 1, "sequence_end": 884},
        "reviewer": "ROOT",
        "source_policy": {
            "master_is_authoritative": True,
            "old_ko_exact_from_master_draft_ko": True,
            "english_prose_opened_or_used": False,
            "master_modified": False,
            "existing_corrections_modified": False,
        },
        "inputs": {
            "master": str(MASTER),
            "master_sha256": sha256(MASTER),
            "existing_corrections": str(EXISTING),
            "existing_corrections_sha256": sha256(EXISTING),
        },
        "output": {
            "corrections": str(OUTPUT),
            "corrections_sha256": sha256(OUTPUT),
        },
        "counts": {
            "candidate_count": len(CANDIDATES),
            "candidate_unique_sequence_count": len(set(sequences)),
            "written_count": len(written),
            "existing_stable_id_overlap_count": len(overlaps),
            "no_op_count": len(no_ops),
            "validation_pass_count": len(validations) - len(failures),
            "validation_failure_count": len(failures),
        },
        "existing_stable_id_overlaps": overlaps,
        "no_ops": no_ops,
        "validation": {
            "normalizes_fullwidth_digits_for_numeric_equivalence": True,
            "all_pass": not failures,
            "failures": failures,
            "records": validations,
        },
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    print(json.dumps({
        "candidate_count": len(CANDIDATES),
        "written_count": len(written),
        "overlap_count": len(overlaps),
        "no_op_count": len(no_ops),
        "validation_failure_count": len(failures),
        "output": str(OUTPUT),
        "report": str(REPORT),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

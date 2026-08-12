#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "output" / "masters" / "scenario_002.master.json"
OUT = ROOT / "reviews" / "A.002.consolidated.corrections.jsonl"
REPORT = ROOT / "reviews" / "A.002.consolidated.report.json"

MANUAL: dict[int, tuple[str, str, str]] = {
    46: ("흔히 부잣집 아가씨들이 다니는 학교로 오해받지만, 기독교계로 유치원부터 줄곧 여학교인 곳들과 비교하면 실상은 도쿄에서 흔히 볼 수 있는 진학교다.", "의미/문법", "お嬢様学校에 없는 명문 의미를 제거하고 비교 구문을 자연스럽게 복원"),
    60: ("하지만 내 기대를 배반하듯, 이날은 수업 시작 시간이 되어도 미하루가 학교에 오지 않았다.", "오역", "気持ちの裏をかく를 비웃는 행위로 옮긴 오류 교정"),
    78: ("그 얘기라면 어제는 딱히 이상한 일이 없었던 것 같은데.", "명백한 직역", "それならそれで의 중복 직역을 문맥에 맞게 교정"),
    86: ("「알려 줘도 되는데, 미하룽의 고민은 리땅만 해결할 수 있거든～」", "조사/문법", "りーたんにしか의 한정 주어를 자연스럽게 복원"),
    110: ("손님도 하나같이 남자뿐이라 우리는 무척 튀는 것 같았다.", "명백한 직역", "見事に男性ばかり의 강조를 보란 듯이라고 오해한 표현 교정"),
    151: ("참고로 라이온관의 경영 상황은 할머니가 시골에서도 전부 파악하고 계셨다.", "조사/문법", "田舎の方から把握していた의 장소·행위자 관계 교정"),
    157: ("교복으로 갈아입은 미하루였다. 메이드복이 떠올라 조금 히죽거릴 뻔했다.", "중복 표현", "学校の制服을 학교 교복이라고 중복 번역한 표현 교정"),
    163: ("「일이 편한 것에 비해 시급이 높거든. 솔직히 나처럼 꼭 돈을 벌어야 하는 애가 오히려 드물어. 대부분 용돈 벌이니까」", "명백한 직역", "稼がないと困る를 돈을 벌지 않으면 곤란하다고 한 직역 교정"),
    191: ("「미안해…… 소리 질러서」", "문법/발화", "ごめん、怒鳴った의 사과 이유를 자연스러운 한국어로 연결"),
    202: ("「내 정보는 너한테 알려 주지 않을게. 내가 노려질 위험이 커지는 건 싫으니까」", "대명사/문법", "직접 대화 중 凛火를 제삼자처럼 옮긴 표현과 狙われる 주체 복원"),
    227: ("본래라면 서로를 탈락시켜야 하는 관계지만 우리는 협력 관계를 맺고 있다.", "고정 용어/의미", "蹴落とし合う를 물리적으로 떨어뜨린다고 한 직역 교정"),
    228: ("아니, 정확히는 내가 일방적으로 협력 관계를 맺도록 강요당했다고 해야겠지.", "피동/주체", "一方的に結ばされていた의 강제 피동과 페데리코의 관점 복원"),
    258: ("오데트는 사오싱주를 단숨에 들이켠 뒤, 대담한 미소를 지으며 대답했다.", "오역", "不敵な笑い는 불온함이 아니라 겁 없고 대담한 미소"),
    304: ("「루 창호의 카드…… 그러니까 “Ⅶ”번의 성명 카드로 빙고다」", "인명 표기", "魯昌鎬의 중국계 전체 이름을 루 창호로 띄어 씀"),
    309: ("「그렇다면 저혈당…… 아니, 기업 임원까지 올라간 놈이 목숨이 걸린 실수를 저지를 리는 없어. 회의 중 돌연사…… ≪뇌경색≫이나 ≪심근경색≫이겠군」", "명백한 직역", "命に関わるミス의 자연스러운 한국어 결합 교정"),
    345: ("루의 남은 정보인 ≪미련≫을 얻을 단서를 찾기 위해서다.", "조사/의미", "魯の残りの情報의 소유·수식 관계 복원"),
    470: ("「뭐, 어디든 상관없잖아. 이제 일요일을 맞기만 하면 되니 잔치나 하러 가자. 첫날에 갔던 가게가 좋겠군. 그곳의 베이징 덕은 맛있었어」", "표기 일관성", "北京ダック 표기를 베이징 덕으로 통일"),
    477: ("「그런데 말이야, 이쯤 되면 의심받겠어, 아저씨?」", "오역", "怪しまれる의 피동 의미를 수상하다는 상태로 옮긴 오류 교정"),
    482: ("우리가 오늘까지 조사해 온 남자――루 창호 본인이 눈앞에 서 있었다.", "인명 표기", "魯昌鎬의 전체 이름 띄어쓰기 통일"),
    507: ("「잠깐. 우리는 당신의 정보를 전부 갖고 있다고. 엿듣고 있었으니 알잖아」", "문장 유형", "단정문 こっちは持ってるんだぞ를 의문문으로 만든 오류 교정"),
    523: ("「네 속셈대로 우리가 서로 싸운다 쳐도, 만에 하나 내가 지고 이 녀석이 살아남으면 어쩔 셈이지? 네 가족이 죽은 일까지 없었던 일이 되지는 않을 텐데?」", "의미/말끝", "ならないぞ의 위협성 확인을 엉뚱한 인용 의문형으로 만든 오류 교정"),
    528: ("나조차 지나치게 일방적인 폭력에 조금 질겁했다.", "오역", "引いていた는 싫증이 아니라 폭력에 질려 물러서는 반응"),
    554: ("「알았어, 알았다고. 우린 대등해. 때리지 마, 알겠지? 때리면 루한테 가 버릴 거야」", "문법/대화체", "연속된 위협성 확인 질문을 자연스러운 한국어 발화로 복원"),
    557: ("이 녀석은 여유로워 보이지만 의외로 아슬아슬한 줄타기를 하고 있다. 물론 나도 마찬가지이기는 하지만.", "관용구", "ぎりぎりな橋を渡る의 위험을 감수하는 의미를 한국어 관용 표현으로 교정"),
    592: ("나는 운명의 대회랑에 서 있었다.", "고정 용어", "運命の大広間의 고정 표기 운명의 대회랑 적용"),
    603: ("대회랑 중앙에 있는 시계의 중심에 반듯한 자세로 서 있었다.", "고정 용어", "같은 공간을 가리키는 大広間 표기를 대회랑으로 통일"),
    647: ("시계의 짧은바늘이 남자가 선 바닥을 향했다.", "조사/문법", "男性の床를 남자가 소유한 바닥으로 옮긴 직역 교정"),
    648: ("지명자와 피지명자, 두 사람이 각각 서 있는 바닥이 수상한 빛을 내뿜고 있었다.", "조사/문법", "두 참가자와 발판의 위치 관계를 명확하게 복원"),
    649: ("그 상태로 긴바늘이 “Ⅻ”번 남자를 가리켰다. 오늘 밤에는 지명하지 않을 생각인지 작게 고개를 가로저었다.", "명백한 직역", "小さな動作で首を振る의 부자연스러운 명사구 교정"),
}

FW_TRANS = str.maketrans("０１２３４５６７８９％", "0123456789%")
ROMAN_RE = re.compile(r"[\u2160-\u2188]+")
TAG_RE = re.compile(r"\{[^{}]+\}|\[[^\[\]]+\]")
KANA_RE = re.compile(r"[ぁ-ゖゝ-ゟァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")


def qsk(text: str) -> list[str]:
    return [c for c in text if c in "「」『』≪≫“”"]


def nums(text: str) -> list[str]:
    normalized = text.translate(FW_TRANS)
    found: list[tuple[int, str]] = [
        (m.start(), m.group(0)) for m in re.finditer(r"\d+(?:\.\d+)?", normalized)
    ]
    digits = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
              "六": 6, "七": 7, "八": 8, "九": 9}
    for m in re.finditer(r"[一二三四五六七八九十]+(?=[泊人枚回度個階月年日時分秒皿])", normalized):
        token = m.group(0)
        if "十" in token:
            left, right = token.split("十", 1)
            value = (digits.get(left, 1) * 10) + (digits.get(right, 0) if right else 0)
        else:
            value = digits[token]
        found.append((m.start(), str(value)))
    native = {"한": 1, "두": 2, "세": 3, "네": 4, "다섯": 5,
              "여섯": 6, "일곱": 7, "여덟": 8, "아홉": 9, "열": 10}
    for m in re.finditer(r"(?<![가-힣])(한|두|세|네|다섯|여섯|일곱|여덟|아홉|열)(?=\s*(?:명|사람|개|장|번|시간|층|박|일|개월|주))", normalized):
        found.append((m.start(), str(native[m.group(1)])))
    return [value for _, value in sorted(found)]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    doc = json.loads(MASTER.read_text(encoding="utf-8-sig"))
    entries = doc["entries"]
    by_seq = {int(e["sequence"]): e for e in entries}
    assert len(entries) == 668 and set(by_seq) == set(range(1, 669))

    selected: dict[int, dict] = {}
    auto_sequences = []
    for e in entries:
        old = e["draft_ko"]
        new = old.translate(FW_TRANS).replace("\u3000", " ")
        if new != old:
            seq = int(e["sequence"])
            auto_sequences.append(seq)
            selected[seq] = {
                "script": "002", "stable_id": e["stable_id"], "sequence": seq,
                "old_ko": old, "new_ko": new, "category": "typography",
                "reason": "한국어 문장 안 전각 숫자·숫자 기호를 의미가 같은 반각으로 정규화",
                "reviewer": "A", "source_jp": e["source_jp"],
            }

    overlap = []
    for seq, (new, category, reason) in MANUAL.items():
        e = by_seq[seq]
        # Manual targets that overlap an automatic width row must also be clean.
        new = new.translate(FW_TRANS).replace("\u3000", " ")
        if seq in selected:
            overlap.append(seq)
        selected[seq] = {
            "script": "002", "stable_id": e["stable_id"], "sequence": seq,
            "old_ko": e["draft_ko"], "new_ko": new, "category": category,
            "reason": reason, "reviewer": "A", "source_jp": e["source_jp"],
        }

    rows = [selected[k] for k in sorted(selected)]
    assert len({r["stable_id"] for r in rows}) == len(rows)
    checks = Counter()
    failures = []
    for row in rows:
        e = by_seq[int(row["sequence"])]
        old, new, src = e["draft_ko"], row["new_ko"], e["source_jp"]
        values = {
            "old_guard": row["old_ko"] == old,
            "changed": new != old,
            "encoding": "\ufffd" not in new and not any(0x80 <= ord(c) <= 0x9F for c in new),
            "width": not re.search(r"[０-９]", new) and "\u3000" not in new,
            "tags": Counter(TAG_RE.findall(src)) == Counter(TAG_RE.findall(new)),
            "roman": ROMAN_RE.findall(src) == ROMAN_RE.findall(new),
            "quotes": qsk(src) == qsk(new),
            "newline": src.count("\n") == new.count("\n"),
            "numbers": nums(src) == nums(new),
            "kana": KANA_RE.search(new) is None,
        }
        for k, v in values.items(): checks[k] += v
        if not all(values.values()): failures.append({"sequence": row["sequence"], "bad": [k for k,v in values.items() if not v]})
    assert not failures, failures

    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    report = {
        "schema_version": "fatal-twelve-review-consolidated-v1", "reviewer": "A", "script": "002",
        "source_authority": "Japanese only", "english_reference_used": False,
        "external_translation_api_used": False, "exhaustive_checked": 668,
        "manual_corrections": len(MANUAL), "automatic_width_corrections": len(auto_sequences),
        "manual_auto_overlap_sequences": overlap, "output_unique_corrections": len(rows),
        "checks": dict(checks), "failures": failures, "master_sha256": sha(MASTER),
        "output_sha256": sha(OUT),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

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
OUT = ROOT / "reviews" / "C.011_01FGH.consolidated.corrections.jsonl"
REPORT = ROOT / "reviews" / "C.011_01FGH.consolidated.report.json"
SCRIPTS = {"011_01F": 210, "011_01G": 192, "011_01H": 63}

MANUAL: dict[tuple[str, int], tuple[str, str, str]] = {
    ("011_01F", 7): ("내가 손님석에 앉아 있자 문이 열리는 종소리가 났다. 들어온 사람은 익숙한 손님이었다.", "어휘", "카페 客席를 공연장 객석이 아닌 손님 좌석으로 자연스럽게 번역"),
    ("011_01F", 28): ("「……알겠습니다. 내일 폐점 후에 폐가 되지 않는다면 다시 와도 될까요? 미하루 선배께도 와 달라고 해서요」", "문법", "ご迷惑じゃなければ의 잘못된 명사 결합 교정"),
    ("011_01F", 45): ("다시 나는 일기장에서 책갈피를 빼냈다. 끼워 둔 책갈피는 공교롭게도 고양이 모양이었다.", "어휘", "あらためて를 새삼스레가 아닌 다시 하는 동작으로 복원"),
    ("011_01F", 51): ("오늘 그 이야기를 해 두지 않았더라면 나는 두 사람에게 연락하는 것조차 잊었을 것이다.", "의미", "その話をしていなかったら를 약속 자체로 한정한 첨가 제거"),
    ("011_01F", 64): ("「이 여자아이, 다이아나 하리슨 씨는――여신 파르카와 같은 얼굴을 하고 있어」", "문법", "중복 주제와 서술어 누락을 자연스럽게 교정"),
    ("011_01F", 70): ("내 손에 새로운 카드가 생성되어 있었다.", "시제/자연스러움", "手元には生成された의 발견 시점과 상태를 자연스럽게 복원"),
    ("011_01F", 98): ("이미 분위기는 팽팽하게 얼어붙어 긴장감으로 가득했다.", "명백한 직역", "空気はひりつき의 긴장된 분위기를 자연스럽게 복원"),
    ("011_01F", 109): ("가족처럼 가까운 사람부터 그저 아는 사이 정도인 사람까지, 아무런 규칙성도 없었다.", "문법/범위", "身内ほど…知人ほど의 범위와 대조를 자연스럽게 복원"),
    ("011_01F", 113): ("그 불길한 예감은 12번째 사람이 죽었을 때 적중하고 말았다.", "누락/수치", "12人目の時에서 생략된 사람과 사망 문맥을 복원"),
    ("011_01F", 122): ("유일하게 기댈 아버지는 연기를 마셔 의식불명의 중태였다.", "명백한 직역", "頼みの父親의 의지할 수 있는 사람이라는 의미와 문장 호응 교정"),
    ("011_01F", 127): ("린다는 그 일을 스스로를 향한 경고처럼 일기장에 남겼다.", "어휘/의미", "戒めのように의 교훈과 자기 경계 의미를 자연스럽게 복원"),
    ("011_01F", 134): ("「어쨌든 이게 비장의 수가 될 수 있다는 판단은 맞는 것 같아. 틀림없이――」", "문법", "切り札足り得る라는 판단과 정답의 관계를 자연스럽게 복원"),
    ("011_01F", 168): ("실마리는 처음부터 내 곁에 있었는데도, 마지막 순간에야 내 손에 들어온 가능성이었다.", "명백한 직역", "手に降りてきた可能性를 자연스러운 한국어로 교정"),
    ("011_01F", 171): ("여신 본인에게 물어도 답할 리 없고, 애초에 우리는 그녀가 인간이었을 때를 기억하지 못한다고 예상하고 있다.", "문법", "기억하다에 불필요하게 붙은 목적어·보조동사 결합 교정"),
    ("011_01F", 177): ("「시험해 본다는…… 건가요?」", "발화/문장부호", "って、ことですか의 망설이는 호흡을 자연스럽게 복원"),
    ("011_01F", 189): ("「그, 그래서……이 일기장, 빌려도 될까요?」", "말더듬", "そそ의 말더듬을 음절을 그대로 반복한 부자연스러운 표현 대신 한국어 발화로 복원"),
    ("011_01F", 195): ("내게 이 일기장은 정보의 출처이기도 하다. 나오미가 읽으면 내가 놓친 정보를 얻을 수 있을지도 모른다.", "어휘", "情報源을 사람을 뜻하는 정보원으로 오해하지 않게 교정"),
    ("011_01G", 29): ("그래서 초등학생이던 나는 수족관을 우주 같다고 생각했다. 지금 생각하면 참 어린아이답다.", "중복/문법", "記憶がある를 앞 문장과 중복한 표현 제거"),
    ("011_01G", 33): ("관내가 넓지는 않았지만, 그만큼 수조 배치 등에 공을 들여 알찬 시간을 보낼 수 있었다.", "문법", "広くはない館内의 부자연스러운 관형 관계 교정"),
    ("011_01G", 42): ("「그, 그만. 그런 말은 부끄러우니까 하지 마」", "감탄/의미", "もうっ를 정말로 오역하지 않고 당황해 만류하는 발화로 복원"),
    ("011_01G", 56): ("그렇지 않고서야 어지간한 일이 없는 한 미하루가 토요일과 일요일에 모두 아르바이트를 쉬는 일은 없을 것이다.", "문법/중복", "よっぽどのことがない限り와 이중 부정의 호응 교정"),
    ("011_01G", 61): ("「우리 집에 묵는 건 괜찮은데, 그, 그, 그런 건 아직, 아직 이르니까」", "말더듬/문법", "원문에 없는 단어 내부 끊김을 제거하고 망설임만 보존"),
    ("011_01G", 65): ("「린카가 먼저 그런 말을 할 줄은 몰랐어. 린카도 그런 지식은 있구나. 걱정 마. 솔직히 난 거기까진 생각하지 않았어」", "명백한 직역", "凛火の方から를 린카 쪽에서가 아닌 발화 주체로 자연스럽게 복원"),
    ("011_01G", 96): ("지난달 5월 6일 일요일. 4명이서 찾아왔던 이곳에 이번에는 미하루와 둘이서 왔다.", "표기", "날짜와 인원 전각 숫자를 반각으로 통일"),
    ("011_01G", 105): ("「그렇다면 내 소원은 조금 욕심내서 5가지. 네 옆에서 스릴 놀이기구를 타는 것. 유령의 집에 들어가는 것. 여름 한정 퍼레이드를 보는 것. 너와 같은 기념품을 사는 것」", "표기/분류사", "전각 숫자를 반각으로 통일하고 열거 항목에 맞는 단위 적용"),
    ("011_01G", 107): ("「놀이공원에 와서 5가지면 충분히 겸손하지 않아? 그래도 알았어……좋아, 전부 이룰 거야」", "표기/분류사", "전각 숫자를 반각으로 통일하고 소원 항목 단위 적용"),
    ("011_01G", 126): ("「서로 ≪여신의 선정≫ 참가자가 된 줄 알았더니, 그 안에서 마지막 두 사람이 됐어」", "오역/어조", "と思えば의 전개를 된 것도 모자라라는 부정 평가로 확대한 오류 교정"),
    ("011_01G", 145): ("「어제 린카가 잠든 사이 그 입술을 빼앗긴 했지만」", "인칭/문법", "凛火の唇이라는 지시 관계를 한국어 문장 안에서 자연스럽게 연결"),
    ("011_01G", 146): ("「뭐엇!?」", "감탄사", "はへっ를 일본어 음차로 남기지 않고 당황한 한국어 반응으로 직접 번역"),
    ("011_01G", 165): ("「오늘 밤이 11번째 선정이기 때문이야. 예를 들어 여신은 강제적인 권한을 행사해 그 지명을 무효로 만들지도 몰라. 그런 경우에도 한 번의 유예가 있으면 다른 방법을 생각할 수 있어」", "어휘/문법", "強権과 一度の猶予를 오해 소지가 없는 자연스러운 한국어로 복원"),
    ("011_01G", 185): ("「제대로 대답하길 잘했어」", "문법/자연스러움", "자기 자신에게 하는 よかったな…返事をして의 인과를 자연스럽게 복원"),
    ("011_01G", 192): ("그 동그랗고 까만 눈을 한동안 마주 바라봤다.", "조사/문법", "시선의 대상인 눈에 붙은 잘못된 접속 조사를 목적격으로 교정"),
    ("011_01H", 12): ("「오늘은 마오 님 추천 만화를 잔뜩 빌려 왔습니다. 하룻밤에 다 못 읽을 만큼. 휴, 무거웠어」", "조사", "기간에 붙은 불필요한 주제 조사 제거"),
    ("011_01H", 22): ("그렇기에 벌을 받는다고 용서되는 일도 아니다.", "의미/문법", "罰で許されることはできない의 벌과 용서의 관계를 자연스럽게 복원"),
    ("011_01H", 23): ("괴로운 건 미하루 쪽이라는 걸 알지만――마음 정리가 되지 않아 아까 한숨을 쉰 것이다.", "명백한 직역", "割り切れない를 자연스러운 한국어로 교정"),
    ("011_01H", 25): ("「이번 주말이 끝나면 마음을 추스르는 거야. 이건 마오 님의 명령」", "어휘/의미", "切り替える를 마음을 바꾼다는 뜻이 아닌 감정 정리로 복원"),
    ("011_01H", 32): ("일단 부딪쳐 보자는 식의 가벼운 마음이 아니었다.", "관용구", "当たって砕けろ의 관용적 의미를 될 대로 되라로 오역한 부분 교정"),
    ("011_01H", 38): ("인간관계만 봐도 이번 일은 확실히 복잡하다.", "명백한 직역", "人間関係を見るとなるほど의 부자연스러운 연결 교정"),
    ("011_01H", 46): ("일요일 밤, 곧 11번째 선정을 맞이할 때가 되자 나는 내 방에서 느긋하게 시간을 보내고 있었다.", "수치/표기", "11回目를 의미와 반각 숫자로 보존"),
    ("011_01H", 47): ("결국 주말 대부분을 마오와 보낸 나는 스스로 생각해도 꽤나 타락한 생활을 했다.", "의미", "堕落した生活을 단순히 늘어져 있었다고 약화한 표현 교정"),
    ("011_01H", 50): ("물론 미하루와의 일이 내 마음을 무겁게 짓누른 것도 사실이고, 마오와 지내면서 마음이 훨씬 편해진 것도 사실이지만.", "문법/중복", "무겁게 짓눌러 온의 중복과 목적어 누락 교정"),
    ("011_01H", 57): ("다음 주부터는 마음을 추스르자. 마오가 말한 대로 하자.", "어휘/의미", "切り替える를 마음을 바꾼다는 뜻이 아닌 감정 정리로 복원"),
}

FW_TRANS = str.maketrans("０１２３４５６７８９％", "0123456789%")
ROMAN_RE = re.compile(r"[\u2160-\u2188]+")
TAG_RE = re.compile(r"\{[^{}]+\}|\[[^\[\]]+\]")
KANA_RE = re.compile(r"[ぁ-ゖゝ-ゟァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")
FW_RE = re.compile(r"[０-９]")


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
    masters: dict[str, dict[int, dict]] = {}
    master_hashes = {}
    for script, expected in SCRIPTS.items():
        path = MASTER_DIR / f"scenario_{script}.master.json"
        entries = json.loads(path.read_text(encoding="utf-8-sig"))["entries"]
        by_seq = {int(entry["sequence"]): entry for entry in entries}
        assert len(entries) == expected and set(by_seq) == set(range(1, expected + 1))
        masters[script] = by_seq
        master_hashes[script] = sha(path)

    selected: dict[tuple[str, int], tuple[str, str, str]] = {}
    width_sequences = []
    for script, by_seq in masters.items():
        for sequence, entry in by_seq.items():
            old = str(entry["draft_ko"])
            normalized = old.translate(FW_TRANS)
            if normalized != old:
                selected[(script, sequence)] = (normalized, "표기", "한국어 target의 전각 숫자·퍼센트를 반각으로 통일")
                width_sequences.append([script, sequence])
    manual_width_overlap = []
    for key, value in MANUAL.items():
        if key in selected:
            manual_width_overlap.append(list(key))
        selected[key] = value

    rows = []
    checks = collections.Counter()
    failures = []
    post_issues = []
    per_script = collections.Counter()
    for (script, sequence), (new_ko, category, reason) in sorted(selected.items()):
        entry = masters[script][sequence]
        old, source = str(entry["draft_ko"]), str(entry["source_jp"])
        row = {"script": script, "stable_id": entry["stable_id"], "sequence": sequence,
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
            failures.append({"script": script, "sequence": sequence, "bad": [k for k, v in values.items() if not v]})
        corrected = dict(entry)
        corrected["draft_ko"] = new_ko
        audit_master.audit_entry(corrected, script, post_issues, ruby_map=ruby_map)
        rows.append(row)
        per_script[script] += 1

    assert len({row["stable_id"] for row in rows}) == len(rows)
    assert not failures, failures
    assert not post_issues, [(x["script"], x["sequence"], x["rule_id"]) for x in post_issues]
    OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    exhaustive = sum(SCRIPTS.values())
    report = {
        "schema_version": "fatal-twelve-c-011-01fgh-review-v1",
        "source_authority": "Japanese only", "english_reference_used": False,
        "external_translation_api_used": False, "scripts": SCRIPTS,
        "exhaustive_checked": exhaustive, "manual_corrections": len(MANUAL),
        "automatic_width_records": len(width_sequences), "manual_width_overlap": manual_width_overlap,
        "output_unique_corrections": len(rows), "corrections_by_script": dict(sorted(per_script.items())),
        "unchanged_approved": exhaustive - len(rows), "checks": dict(checks),
        "post_correction_audit_issues": len(post_issues), "failures": failures,
        "master_sha256": master_hashes, "output_sha256": sha(OUT),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

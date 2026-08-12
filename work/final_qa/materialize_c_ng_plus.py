#!/usr/bin/env python3
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "output" / "masters" / "scenario_NG_plus.master.json"
OUT = ROOT / "reviews" / "C.NG_plus.consolidated.corrections.jsonl"
REPORT = ROOT / "reviews" / "C.NG_plus.consolidated.report.json"

MANUAL: dict[int, tuple[str, str, str]] = {
    2: ("오구마 마오의 불길한 예감은 얄궂게도 대부분 맞아떨어진다.", "고유명사", "小熊의 승인 표기 오구마 적용"),
    9: ("중학교 2학년이 된 봄, 반 배정이 이뤄지고 약 일주일이 지났을 무렵.", "표기", "한국어 문장 안의 전각 숫자를 반각으로 통일"),
    28: ("밖에 나가면 내가 싫어하지 않을 만한 사람이 분명 있을 거라고.", "주체/의미", "自分が嫌いにならない人를 자기혐오로 읽히지 않게 주체 복원"),
    30: ("이날도 평소처럼 혼자 등교하고 혼자 하교할 생각이었지만, 이를 가로막듯 반 친구 한 명이 말을 걸어왔다.", "수/의미", "단수 クラスメイト를 복수로 확대한 오류 교정"),
    31: ("비교적 외모가 괜찮아 교실 내 서열 상위권에 자리한 3인조였다.", "표기", "한국어 문장 안의 전각 숫자를 반각으로 통일"),
    35: ("사립 아메차여자대학 부속중학교의 특별 장학생이었고, 성숙한 외모 덕분에 연예 기획사에서 스카우트 제의를 받을 정도였다.", "오역/문법", "特待生를 특기생이 아닌 특별 장학생으로 복원하고 문장 호응 교정"),
    46: ("――오구마 씨는 냉정하니까. 뭐, 원래 미시마 씨랑 얘기한 것도 아니니 상관없나.", "고유명사", "小熊의 승인 표기 오구마 적용"),
    54: ("그 아이들은 어째서인지 조그만 도시의 조그만 학교, 그 안에서도 더 조그만 반에서 서열 상위에 있다는 걸 대단한 지위라고 진지하게 여겼다.", "명백한 직역", "ステータスに感じている의 부자연스러운 지위로 여기다 결합 교정"),
    61: ("그래서 마오는 곧바로 행동에 나섰다.", "명백한 직역", "行動を起こすのはすぐだった를 자연스럽게 복원"),
    74: ("오구마 마오는 초등학생 때 우수한 아이였다.", "고유명사", "小熊의 승인 표기 오구마 적용"),
    77: ("오구마 집안은 경제적으로 여유가 있었다.", "고유명사", "小熊의 승인 표기 오구마 적용"),
    80: ("하지만 많은 아이가 그렇듯, 마오에게 공부에만 매달리는 나날은 그 밖의 모든 시간을 잃는 것과 같았다.", "명백한 직역", "それ以外の日々を失う의 의미를 자연스럽게 복원"),
    89: ("기대와 부담이 마오에게는 같은 뜻이라는 걸 깨닫는 건 훨씬 더 먼 훗날의 일이다.", "어휘/자연스러움", "重荷를 문맥상 부담으로 옮기고 문장 호흡 교정"),
    93: ("마오는 붙임성이 나쁜 편은 아니었다. 따돌림 제안에는 차분히 대답했지만, 일상적인 대화라면 별문제 없이 말을 주고받았다.", "어휘", "人当たりが悪い의 대인 태도 의미를 자연스럽게 복원"),
    94: ("그래서 그렇게 매몰차게 퇴짜를 맞은 게 재미있었다.", "어휘/자연스러움", "あしらわれた의 상대에게 가볍게 거절당한 의미를 복원"),
    99: ("마오는 하하, 하고 멋쩍게 웃으며 그날은 미하루의 뒷모습을 배웅했다.", "의성어/어조", "たはは를 일본어 음차가 아닌 문맥에 맞는 한국어 웃음으로 직접 번역"),
    103: ("미하루의 대답은 거의 언제나 같았다.", "중복", "大体いつも를 대개 늘로 중복 번역한 표현 교정"),
    112: ("마오도 어디선가 11명 중 1명 정도는 경험이 있다고 들은 적이 있었다.", "표기", "한국어 문장 안의 전각 숫자를 반각으로 통일"),
    119: ("마오는 곧바로 대답했다.", "명백한 직역", "間をおかず를 과장된 망설임 표현 없이 직접 복원"),
    123: ("시간을 두고 생각해 보면, 그 아이가 왜 「역겹다」고 느끼는지는 마오도 알 수 있었을 것이다.", "문법", "가정절·주어·목적어의 호응을 자연스럽게 교정"),
    132: ("「……오구마 씨」", "고유명사", "小熊의 승인 표기 오구마 적용"),
    134: ("「이번에는 내가 제안을 받았어. 오구마 씨를 무시하지 않겠냐고」", "고유명사", "小熊의 승인 표기 오구마 적용"),
    149: ("마오를 무시하자고 제안해 놓고 곧장 자신에게 말을 걸다니 참 대단하다고 마오는 생각했다.", "어조/문법", "立派だなあ의 반어와 문장 호응을 자연스럽게 복원"),
    157: ("마오는 신이 나서 윙크까지 하며 그렇게 대답해 보았다.", "어조/자연스러움", "はりきって의 의기양양한 태도를 자연스럽게 복원"),
    162: ("그곳에 극적인 사건 따위는 없었다. 반에서 겉돌게 된 두 사람이 자연스럽게 붙어 다닌다는, 굳이 따지면 부정적인 계기로 가까워진 셈이었다.", "문법/의미", "ネガティブな距離の縮まり方의 계기와 결과 관계를 자연스럽게 복원"),
    165: ("마오는 반에서 그럭저럭 다른 아이들과 어울리게 되었고, 미하루는 여전히 기피됐다――즉, 원래대로 돌아온 것이다.", "명백한 직역", "そこそこ話すポジション의 반 내 인간관계 의미를 자연스럽게 복원"),
    177: ("옥상의 메마른 공기를 마오도 미하루도 좋아하게 되었다.", "조사/문법", "좋아하는 대상에 잘못 붙은 주제 조사를 목적격으로 교정"),
    182: ("과거에 마음을 돌리게 되는 건 으레 무슨 일이 생겼을 때다.", "명백한 직역", "過去に思いを馳せる의 자연스러운 한국어 표현"),
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
    document = json.loads(MASTER.read_text(encoding="utf-8-sig"))
    entries = document["entries"]
    by_seq = {int(entry["sequence"]): entry for entry in entries}
    assert len(entries) == 185 and set(by_seq) == set(range(1, 186))

    rows = []
    checks = collections.Counter()
    failures = []
    post_issues = []
    for sequence, (new_ko, category, reason) in sorted(MANUAL.items()):
        entry = by_seq[sequence]
        old = str(entry["draft_ko"])
        source = str(entry["source_jp"])
        row = {
            "script": "NG_plus",
            "stable_id": entry["stable_id"],
            "sequence": sequence,
            "old_ko": old,
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": "C",
            "source_jp": source,
        }
        values = {
            "changed": new_ko != old,
            "encoding": "\ufffd" not in new_ko and not any(0x80 <= ord(ch) <= 0x9F for ch in new_ko),
            "width_clear": not re.search(r"[０-９]", new_ko) and "\u3000" not in new_ko,
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
            failures.append({"sequence": sequence, "bad": [key for key, passed in values.items() if not passed]})
        corrected = dict(entry)
        corrected["draft_ko"] = new_ko
        audit_master.audit_entry(corrected, "NG_plus", post_issues, ruby_map=ruby_map)
        rows.append(row)

    assert len({row["stable_id"] for row in rows}) == len(rows)
    assert not failures, failures
    assert not post_issues, [(issue["sequence"], issue["rule_id"]) for issue in post_issues]
    OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    report = {
        "schema_version": "fatal-twelve-c-ng-plus-review-v1",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "script": "NG_plus",
        "exhaustive_checked": 185,
        "manual_corrections": len(rows),
        "unchanged_approved": 185 - len(rows),
        "stable_id_unique": len({row["stable_id"] for row in rows}),
        "checks": dict(checks),
        "post_correction_audit_issues": len(post_issues),
        "failures": failures,
        "master_sha256": sha(MASTER),
        "output_sha256": sha(OUT),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

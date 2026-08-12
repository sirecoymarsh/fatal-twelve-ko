from __future__ import annotations

import json
from pathlib import Path


OUT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\translations\draft\scenario\MIHARU_END_source_only.json")


ROWS = [
    (31, "rinka", "「……いける」", "「……괜찮은데」"),
    (33, "narrator", "公園のベンチに座って、私は紙コップに入れたコーヒーを飲んでいた。", "공원 벤치에 앉아, 나는 종이컵에 든 커피를 마시고 있었다."),
    (35, "narrator", "今日は一日この場所にいようと決めていた。", "오늘은 하루 종일 이곳에 있기로 했다."),
    (37, "narrator", "どうやら今日はここにいなくてはならない日らしいから。", "아무래도 오늘은 이곳에 있어야만 하는 날인 모양이니까."),
    (39, "narrator", "だから、コーヒーを淹れてきたのだ。", "그래서 커피를 내려 온 것이다."),
    (41, "narrator", "テイクアウト用の紙カップをサンプルでもらったので、それを試してみたのだ。", "테이크아웃용 종이컵을 견본으로 받았기에, 한번 써 보는 중이었다."),
    (45, "rinka", "「今度、直未にも飲んでもらおう」", "「다음에는 나오미에게도 마셔 보라고 해야지」"),
    (47, "narrator", "この場所は。", "이곳은."),
    (49, "narrator", "私にとっても、想い出の場所だ。", "내게도 추억이 깃든 곳이다."),
    (51, "narrator", "海晴と初めて出会った場所であり。", "미하루와 처음 만난 곳이며."),
    (53, "narrator", "おばあちゃんと何度も来た場所であり。", "할머니와 몇 번이고 찾아왔던 곳이며."),
    (55, "narrator", "直未と罪の重さを分かち合った場所であり。", "나오미와 죄의 무게를 함께 나눈 곳이며."),
    (57, "narrator", "運命の、終着点。", "운명의, 종착점."),
    (59, "narrator", "私たち12人が≪いるはずだった≫場所。", "우리 열두 명이 ≪있었어야 했던≫ 곳."),
    (61, "narrator", "私の選択は、正しいものだったと信じている。", "나의 선택이 옳았다고 믿는다."),
    (63, "narrator", "結果として、海晴は私の中から消えなかった。", "결과적으로, 미하루는 내 안에서 사라지지 않았다."),
    (65, "narrator", "長きに亘る≪女神の選定≫は、今日、完全に終わったのだ。", "오랫동안 이어진 ≪여신의 선정≫은 오늘 완전히 끝났다."),
    (67, "narrator", "私の中に残った迷惑な力はまだ薄れる気配がないけれど、あの男性の言葉の通り、時間の問題なのだろう。", "내 안에 남은 성가신 힘은 아직 옅어질 기미가 없지만, 그 남자의 말대로 시간 문제겠지."),
    (69, "narrator", "なかったことになってしまった日々に意味はあったのか。", "없었던 일이 되어 버린 나날에는 의미가 있었을까."),
    (71, "narrator", "そんな疑問が風に乗って湧いた。", "그런 의문이 바람을 타고 피어올랐다."),
    (73, "narrator", "答えは決まっている。", "답은 정해져 있다."),
    (75, "narrator", "意味なんてない。", "의미 따위는 없어."),
    (77, "narrator", "あるのはただ、想い出だけだ。", "있는 것은 그저, 추억뿐이다."),
    (81, "rinka", "「あーあ、暇だなぁ」", "「아아, 심심하다」"),
    (83, "narrator", "私は思わず、そう呟いていた。", "나는 무심코 그렇게 중얼거렸다."),
    (85, "narrator", "高い空を見上げて。", "드높은 하늘을 올려다보며."),
]


def main() -> None:
    entries = []
    for line, speaker, source_jp, draft_ko in ROWS:
        entries.append(
            {
                "stable_id": f"scenario/MIHARU_END.rpy::L{line}",
                "sequence": None,
                "translation_id": None,
                "translation_id_status": "pending_ast_alignment",
                "source_file": "scenario/MIHARU_END.rpy",
                "source_line": line,
                "speaker": speaker,
                "source_jp": source_jp,
                "draft_ko": draft_ko,
                "source_authority": "Japanese only",
                "english_reference_used": False,
                "status": "first_draft_unreviewed",
                "qa": "deferred_until_full_first_draft",
            }
        )
    packet = {
        "packet_id": "scenario_MIHARU_END_source_only",
        "source_language": "Japanese",
        "target_language": "Korean",
        "entry_count": len(entries),
        "translation_id_alignment": "pending AST-aware catalog merge",
        "status": "first_draft_unreviewed",
        "qa_policy": "No translation QA until the complete first draft is finished; review once afterward.",
        "english_text_in_translator_packet": False,
        "entries": entries,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(entries)} source-line-keyed Japanese-to-Korean draft entries")
    print(OUT)


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from pathlib import Path


OUT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\translations\draft\scenario\BAD_END_04_source_only.json")


ROWS = [
    (28, "narrator", "ワタクシたちは、遊園地に来ていました。", "저희는 놀이공원에 와 있었습니다."),
    (30, "narrator", "それも、今日はなんとワタクシのお誕生日。", "그런데 오늘은 무려 제 생일이랍니다."),
    (32, "narrator", "一日たっぷり、皆サマと遊びました。", "하루 종일 실컷 여러분과 놀았습니다."),
    (37, "mao", "「いやー、楽しかったねぇ」", "「이야, 재미있었네」"),
    (42, "naomi", "「わたしも……楽しかったです」", "「저도…… 즐거웠어요」"),
    (44, "narrator", "お二人の間には、どこか寂しい空気が流れています。", "두 분 사이에는 어딘가 쓸쓸한 공기가 흐르고 있습니다."),
    (46, "narrator", "無理もありません。", "당연한 일이겠지요."),
    (48, "narrator", "海晴サマのことを思い出しているのでしょう。", "미하루 님을 떠올리고 계신 것이겠지요."),
    (50, "narrator", "ワタクシも、凛火サマの記憶に触れて数日。", "저도 린카 님의 기억을 접한 지 며칠."),
    (52, "narrator", "彼女の存在の大きさには、すでに気がついておりますもの。", "그녀의 존재가 얼마나 컸는지는 이미 깨닫고 있답니다."),
    (57, "rinka", "「二人とも、ありがとう。今日はとても……楽しかった」", "「둘 다 고마워. 오늘은 정말…… 즐거웠어」"),
    (59, "narrator", "すっかり、ワタクシの言葉遣いも板についてきました。", "이제는 저도 이 말투가 제법 익숙해졌습니다."),
    (61, "narrator", "少し間を入れるのがポイントのようです。", "조금 뜸을 들이는 것이 요령인 모양입니다."),
    (66, "rinka", "「色々あったけどさ、こうしてここに来られることはきっと、幸せだと思う」", "「여러 일 있었지만 말이야, 이렇게 여기 올 수 있다는 건 분명 행복한 일이라고 생각해」"),
    (68, "narrator", "きっとこういう言葉が、この時の正解なのでしょう。", "분명 이런 말이 지금의 정답이겠지요."),
    (70, "narrator", "私はお二人サマの目を見て、しっかりと口にするのです。", "저는 두 분의 눈을 바라보며 또렷이 말합니다."),
    (75, "mao", "「ね、りーたんはりーたんだよね？」", "「있지, 리땅은 리땅 맞지?」"),
    (77, "narrator", "真央サマが、私に訊ねます。", "마오 님이 제게 묻습니다."),
    (79, "narrator", "ワタクシは質問の意図が分からず、戸惑ってしまいました。", "저는 질문의 뜻을 알 수 없어 당황하고 말았습니다."),
    (81, "narrator", "どう答えようか考えていると、真央サマの方から答えてくださいました。", "어떻게 답할지 생각하고 있자, 마오 님이 먼저 대답해 주셨습니다."),
    (86, "mao", "「ごめん、変なこと聞いちゃったよねぇ」", "「미안, 이상한 걸 물어봤네」"),
    (91, "mao", "「りーたんはりーたん。間違いないよね」", "「리땅은 리땅이야. 틀림없지」"),
    (96, "naomi", "「そ、そうですよ！　凛火先輩は……凛火先輩ですよね」", "「그, 그래요! 린카 선배는…… 린카 선배예요」"),
    (101, "rinka", "「……変なの」", "「……이상하네」"),
    (103, "narrator", "こうして私は、17歳になりました。", "그렇게 저는 열일곱 살이 되었습니다."),
    (105, "narrator", "さて、後は夜のパレードを見て帰りましょう。", "자, 이제 밤 퍼레이드를 보고 돌아가도록 하지요."),
    (123, "narrator", "その事件は、早速ニュースになっていた。", "그 사건은 곧바로 뉴스가 되었다."),
    (125, "narrator", "小熊真央は、心にぽっかりと穴が空いてしまったせいで、家に帰ることができずにいた。", "코구마 마오는 마음에 뻥 뚫린 구멍 때문에 집으로 돌아가지 못하고 있었다."),
    (130, "mao", "「りーたんまで……」", "「리땅마저……」"),
    (132, "narrator", "ニュースの内容は、こうだ。", "뉴스 내용은 이러했다."),
    (134, "narrator", "老若男女問わず人気のスターダストキングダムで、事故が発生した。", "남녀노소를 가리지 않고 인기 있는 스타더스트 킹덤에서 사고가 발생했다."),
    (136, "narrator", "夜のパレード中、フロートが倒れ、近くで観覧していた女子高生が下敷きになった。", "밤 퍼레이드 도중 플로트가 쓰러져, 근처에서 관람하던 여고생이 그 아래에 깔렸다."),
    (138, "narrator", "多くの電飾を使用していたフロートは断線をきっかけに発火し、炎上。", "수많은 전구 장식을 사용한 플로트는 단선을 계기로 불이 붙어 화염에 휩싸였다."),
    (140, "narrator", "下敷きになった女子高生は救助虚しく、焼死した。", "깔린 여고생은 구조 노력도 허무하게 불에 타 숨졌다."),
    (142, "narrator", "被害者の名前は、獅子舞凛火。悲惨なことに、今日は17歳の誕生日であり、友人たちにお祝いしてもらいに来ていたのだ。", "피해자의 이름은 시시마이 린카. 참혹하게도 오늘이 열일곱 번째 생일이었으며, 친구들에게 축하를 받으러 왔던 것이었다."),
    (147, "mao", "「りーたん……」", "「리땅……」"),
    (149, "narrator", "真央は、ただ泣くことしかできなかった。", "마오는 그저 울 수밖에 없었다."),
    (151, "narrator", "自分が抱えていた違和感などどうでもよかった。", "자신이 품었던 위화감 따위는 아무래도 좋았다."),
    (153, "narrator", "生きていなかったら、もうおしまいだ。", "살아 있지 않다면, 이제 끝이다."),
    (155, "narrator", "この先はないのだ。", "앞으로는 아무것도 없다."),
    (160, "mao", "「うわああっ」", "「으아아아!」"),
    (162, "narrator", "夜の駅。", "밤의 역."),
    (164, "narrator", "たくさんの人が、泣き叫ぶ真央のことを見て、無視をした。", "수많은 사람은 울부짖는 마오를 보고도 외면했다."),
]


def main() -> None:
    entries = []
    for line, speaker, source_jp, draft_ko in ROWS:
        entries.append(
            {
                "stable_id": f"scenario/BAD_END_04.rpy::L{line}",
                "sequence": None,
                "translation_id": None,
                "translation_id_status": "pending_ast_alignment",
                "source_file": "scenario/BAD_END_04.rpy",
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
        "packet_id": "scenario_BAD_END_04_source_only",
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

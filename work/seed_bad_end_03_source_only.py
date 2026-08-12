from __future__ import annotations

import json
from pathlib import Path


OUT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\translations\draft\scenario\BAD_END_03_source_only.json")


ROWS = [
    (26, "narrator", "誰もいなくなったその場所で、女神パルカは微笑んでいた。", "아무도 남지 않은 그곳에서, 여신 파르카는 미소 짓고 있었다."),
    (31, "parca", "「意外な結末――というべきなのでしょうか」", "「뜻밖의 결말――이라고 해야 할까요」"),
    (36, "parca", "「Ⅰ番サマはもう少し長く、生きてくださると思っていましたのに。だって――」", "「Ⅰ번 님께서는 조금 더 오래 살아 주실 줄 알았는데요. 왜냐하면――」"),
    (41, "parca", "「おや、誰が聞いているか分かりませんものね。これ以上はこの場所でも、お話ししない方がよろしいでしょうかしら」", "「이런, 누가 듣고 있을지 모르겠군요. 더 이상은 이곳에서도 이야기하지 않는 편이 좋으려나요」"),
    (43, "narrator", "スケール・ジョーンズは獅子舞凛火を指名した。", "스케일 존스는 시시마이 린카를 지명했다."),
    (45, "narrator", "同時に、アラン・スコーピオンはスケール・ジョーンズを指名した。", "동시에 아란 스코피온은 스케일 존스를 지명했다."),
    (47, "narrator", "その時点で、獅子舞凛火は人質にとられていた祖母が助からないのだと直感した。", "그 시점에서 시시마이 린카는 인질로 붙잡힌 할머니가 살아남지 못하리라고 직감했다."),
    (52, "parca", "「けれどⅠ番サマのあのお顔は、とても印象的でございました」", "「하지만 Ⅰ번 님의 그 표정은 아주 인상적이었답니다」"),
    (54, "narrator", "祖母の死と自分の死を確信した瞬間の、絶望という言葉では表現しきれない表情。", "할머니의 죽음과 자신의 죽음을 확신한 순간 지은, 절망이라는 말만으로는 다 표현할 수 없는 표정."),
    (56, "narrator", "パルカはその顔を見て、一体どんな気持ちを湧き立たせていたのか。", "파르카는 그 얼굴을 보며 대체 어떤 감정이 치밀어 올랐던 걸까."),
    (58, "narrator", "きっとパルカですら、その気持ちの正体を知ることはない。", "아마 파르카 자신조차 그 감정의 정체를 알지 못하리라."),
    (63, "parca", "「さて、残る参加者はⅡ番サマ、Ⅲ番サマ、Ⅻ番サマ」", "「자, 남은 참가자는 Ⅱ번 님, Ⅲ번 님, Ⅻ번 님」"),
    (65, "narrator", "彼女は微笑みながら、淡々と残った参加者を挙げる。", "그녀는 미소 지은 채 담담하게 남은 참가자들을 열거한다."),
    (70, "parca", "「一体どなたが脱落し、どなたが生き残るのでしょうか」", "「과연 어느 분이 탈락하고, 어느 분이 살아남으실까요」"),
    (75, "parca", "「どなたがワタクシの器になるのか、未だ予想がつきません」", "「어느 분이 저의 그릇이 될지, 아직은 예상할 수 없답니다」"),
    (80, "parca", "「こうなってしまえば、もはやどなたサマでも同じですけれども」", "「이렇게 되어 버렸으니, 이제 어느 분이든 마찬가지이긴 하지만요」"),
    (85, "parca", "「……あら？」", "「……어머?」"),
    (87, "narrator", "パルカは首を傾げて、口にする。", "파르카는 고개를 갸웃하며 입을 열었다."),
    (92, "parca", "「それは、どうしてでしたっけ？」", "「그건, 왜였던가요?」"),
    (94, "narrator", "こぼれた疑問に、返事は決して返ってこない。", "흘러나온 의문에 답이 돌아오는 일은 결코 없다."),
    (96, "narrator", "パルカは再び、≪女神の選定≫の管理者へと戻るのであった。", "파르카는 다시 ≪여신의 선정≫의 관리자로 돌아가는 것이었다."),
]


def main() -> None:
    entries = []
    for line, speaker, source_jp, draft_ko in ROWS:
        entries.append(
            {
                "stable_id": f"scenario/BAD_END_03.rpy::L{line}",
                "sequence": None,
                "translation_id": None,
                "translation_id_status": "pending_ast_alignment",
                "source_file": "scenario/BAD_END_03.rpy",
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
        "packet_id": "scenario_BAD_END_03_source_only",
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

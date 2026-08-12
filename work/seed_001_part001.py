from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko")


ENTRIES = [
    ("f001_9ce2c448", 32, "narrator", "一つの結果に到達するまでの過程を、人は物語や人生と呼ぶ。", "하나의 결과에 도달하기까지의 과정을 사람들은 이야기나 인생이라 부른다."),
    ("f001_365e9d7b", 34, "narrator", "様々な出会いがあり、別れがあり、事件があり、選択があり、そして未来の可能性の中を進み、一つの結果へ到達する。", "그 과정에는 수많은 만남과 이별, 사건과 선택이 있으며, 그렇게 미래의 가능성 속을 나아가 하나의 결과에 도달한다."),
    ("f001_1dcd767b", 36, "narrator", "この世界というのは――運命というのは、そういう風にできている。", "이 세계는――운명은, 그렇게 이루어져 있다."),
    ("f001_d2cb40bf", 38, "narrator", "運命は変わらないから運命なんだ。どんなに理不尽でも。", "운명은 변하지 않기에 운명이다. 아무리 불합리하더라도."),
    ("f001_1cc3f16e", 40, "narrator", "これまで生きてきた私の人生の中で起きたこと、その全ては何かの過程の結果なのだ。", "지금껏 살아온 내 인생에서 일어난 일들, 그 모든 것은 어떤 과정 끝에 나온 결과다."),
    ("f001_98ad5030", 42, "narrator", "その途中で失われた可能性のことなんて、私は考えたことがなかった。", "그 도중에 사라진 가능성 따위, 나는 생각해 본 적이 없었다."),
    ("f001_8869472c", 44, "narrator", "たら、れば、かもしれないに思いを馳せるほど、壮絶な人生ではなかったのだ。", "했더라면, 그랬다면, 어쩌면 같은 말에 생각이 잠길 만큼 파란만장한 인생은 아니었다."),
    ("f001_f21956c5", 46, "narrator", "物語は、人生は、たった一つだと思い込んでいた。", "이야기도, 인생도, 단 하나뿐이라고 굳게 믿고 있었다."),
    ("f001_8024772c", 58, "narrator", "私の名前は、{rb}獅子舞{/rb}{rt}ししまい{/rt}{rb}凛火{/rb}{rt}りんか{/rt}。", "내 이름은 시시마이 린카."),
    ("f001_bc643489", 60, "narrator", "都内でそこそこ有名な女子校、私立{rb}飴茶{/rb}{rt}あめちゃ{/rt}女子大学付属高校の２年生だ。", "도쿄에서 제법 유명한 여학교, 사립 아메차 여자대학 부속 고등학교 2학년이다."),
    ("f001_823596c6", 62, "narrator", "トップ高に入った優等生からほとんど学校に来ない問題児まで色々な人がいた中学時代とは打って変わり、ここでは大人しいお嬢様ばかりだ。", "최상위권 고등학교에 진학한 우등생부터 학교에 거의 나오지 않는 문제아까지 별별 애들이 다 있던 중학교 때와는 달리, 이곳에는 얌전한 아가씨들뿐이다."),
    ("f001_f123f239", 64, "narrator", "そんな中、私は周囲から不良のレッテルを貼られていた。", "그런 가운데 나는 주변으로부터 불량학생이라는 딱지가 붙어 있었다."),
    ("f001_7f693824", 66, "narrator", "理由のひとつが――そしてそれがもっとも大きいのだけど――黒に金色のメッシュが入った髪にあった。", "이유 중 하나가――그리고 그게 가장 큰 이유였는데――검은색 사이사이에 금빛이 섞인 내 머리카락이었다."),
    ("f001_d9a60451", 68, "narrator", "地毛なのだから校則や偏見でとやかく言われることもないのだけれど、どうやら小学校からずっと女子校のお嬢様たちにはアバンギャルドに過ぎるらしい。", "타고난 머리색이라 교칙이나 편견을 들먹이며 이래라저래라 할 일은 없었지만, 초등학교 때부터 줄곧 여학교만 다닌 아가씨들에게는 아무래도 너무 파격적인 모양이다."),
    ("f001_481b5537", 70, "narrator", "服装や容姿に関する校則が緩いからこそ私は飴茶を選んだのに、実態は暗黙のルールだか伝統だかが染みついているから校則の規定がないというだけであった。", "복장이나 외모에 관한 교칙이 느슨해서 아메차를 골랐건만, 실상은 암묵적인 규칙인지 전통인지가 워낙 뿌리 깊어서 굳이 교칙에 적어 놓지 않았을 뿐이었다."),
    ("f001_b4fa6dee", 72, "narrator", "入学したての頃こそ校則違反ではないのに見た目だけで不良扱いされることに腹を立てたが、３ヵ月も経たずに気にならなくなった。", "입학 초기에는 교칙을 어긴 것도 아닌데 겉모습만 보고 불량학생 취급하는 게 화났지만, 석 달도 지나지 않아 신경 쓰이지 않게 됐다."),
    ("f001_4c787f24", 74, "narrator", "私には私の世界があるように、彼女たちには彼女たちの世界があることが分かったからだ。", "나에게 나만의 세계가 있듯, 그녀들에게도 그녀들만의 세계가 있다는 걸 알았기 때문이다."),
    ("f001_62952f0d", 76, "narrator", "私が彼女たちの価値観を理解できないように、彼女たちもまた私の価値観を理解することはない。", "내가 그녀들의 가치관을 이해할 수 없듯, 그녀들 역시 내 가치관을 이해하지 못한다."),
    ("f001_f5ed11df", 78, "narrator", "実のところ、これまでの私はそんな風に理解できるものだけを理解して生きていくのだと割り切っていた。", "사실 지금까지의 나는 그렇게, 이해할 수 있는 것만 이해하며 살아가면 된다고 선을 그어 왔다."),
    ("f001_5f791863", 80, "narrator", "だが、ある時を境に運命の歯車が大きく動き出すことになった。", "하지만 어느 순간을 기점으로 운명의 톱니바퀴가 크게 움직이기 시작했다."),
    ("f001_eb489c3e", 82, "narrator", "それは、ゴールデンウィーク直前のある日からだった――。", "그건 골든위크 직전, 어느 날부터였다――."),
    ("f001_9e0ab144", 112, "rinka", "「見て。駅の時計止まっちゃってる……故障かな？」", "“봐. 역 시계가 멈췄어…… 고장 났나?”"),
    ("f001_619b8ef6", 114, "narrator", "改札口を抜けた先にあるアナログ時計に目を遣って、私は{rb}直未{/rb}{rt}なおみ{/rt}に話しかけた。", "개찰구를 빠져나온 곳에 있는 아날로그 시계로 눈을 돌리며, 나는 나오미에게 말을 걸었다."),
    ("f001_17909fec", 120, "naomi", "「本当だ……凛火先輩、よく気付きましたね！　駅の時計が止まってるなんて珍しいのに」", "“정말이네요…… 린카 선배, 용케 알아채셨네요! 역 시계가 멈춰 있다니 드문 일인데요.”"),
    ("f001_c934fe7d", 125, "rinka", "「だよね。あ、ごめん、直未の話、遮っちゃったよね？　何の話だっけ？」", "“그치? 아, 미안. 나오미 말 끊었지? 무슨 얘기였더라?”"),
    ("f001_80a288e9", 130, "naomi", "「えっと、あれですよ、あれ。あの……はははー、わたしも忘れちゃいました」", "“그러니까, 그거예요, 그거. 저기…… 하하하, 저도 잊어버렸어요.”"),
    ("f001_94682d80", 147, "narrator", "はにかみながら答えたのは、一つ年下の{rb}日辻{/rb}{rt}ひつじ{/rt}{rb}直未{/rb}{rt}なおみ{/rt}だ。", "수줍게 웃으며 대답한 사람은 한 살 아래인 히츠지 나오미다."),
    ("f001_53b2ce10", 149, "narrator", "後輩といっても部活や委員会で知り合ったわけではなく、ちょっとした偶然で私たちは先輩後輩の関係になった。", "후배라고는 해도 동아리나 위원회에서 만난 건 아니고, 사소한 우연을 계기로 우리는 선후배 사이가 됐다."),
    ("f001_8de07126", 151, "narrator", "私は上下関係とか気にしないから、友達って感じだけど。", "나는 위아래 관계 같은 건 신경 쓰지 않으니, 친구에 가깝지만."),
    ("f001_28abb60e", 153, "narrator", "直未と私は、二人でうちへ向かう途中であった。いつものように駅の改札を抜け、ホームへと向かっている。", "나오미와 나는 둘이서 우리 집으로 가는 길이었다. 여느 때처럼 역 개찰구를 지나 승강장으로 향하고 있었다."),
    ("f001_8e0e7d7f", 163, "naomi", "「わきゃっ！」", "“꺅!”"),
    ("f001_75c7f5d5", 169, "rinka", "「ちょっと」", "“조심해.”"),
    ("f001_49521422", 171, "narrator", "小さな悲鳴をあげた直後、直未は何もないところで転びそうになり、体が傾いた。", "작게 비명을 지른 직후, 나오미는 아무것도 없는 곳에서 넘어질 듯 몸이 기울었다."),
    ("f001_5f66ce55", 173, "narrator", "私は直未の手を掴んで、体を支える。", "나는 나오미의 손을 붙잡아 몸을 받쳐 주었다."),
    ("f001_d5615035", 175, "narrator", "私の方が体が小さいのでちょっと引っ張られたが、直未もすぐ自分で体勢を整えていた。", "내 쪽이 체구가 작아 살짝 끌려가긴 했지만, 나오미도 금세 스스로 자세를 바로잡았다."),
    ("f001_99d0f9a5", 180, "naomi", "「す、すみません……」", "“죄, 죄송해요……”"),
    ("f001_38e83cc7", 186, "rinka", "「別に、謝ることじゃないよ」", "“딱히 사과할 일은 아니야.”"),
    ("f001_47ae53a1", 190, "naomi", "「あ、ありがとうございます！」", "“가, 감사합니다!”"),
    ("f001_7992c73e", 195, "rinka", "「それもなんか大げさ」", "“그것도 좀 거창한데.”"),
    ("f001_d4f16a28", 197, "narrator", "直未はいつもどこかおどおどしていて、そのせいで注意力散漫なのか分からないが――よく転ぶ。", "나오미는 늘 어딘가 안절부절못한다. 그래서 주의가 산만한 건지는 모르겠지만――자주 넘어진다."),
    ("f001_8df83878", 199, "narrator", "小動物みたいで、どちらかというと守ってあげたくなるタイプだと思う。", "작은 동물 같아서, 굳이 따지면 지켜 주고 싶어지는 타입이라고 생각한다."),
    ("f001_aeb21865", 204, "naomi", "「それで、その……」", "“그래서, 저기……”"),
    ("f001_3dde34fb", 209, "rinka", "「ん？　どうしたの？」", "“응? 왜 그래?”"),
    ("f001_e2203c0a", 214, "naomi", "「えっと……手……」", "“저기…… 손이요……”"),
    ("f001_1db0b123", 216, "narrator", "直未を支えたときからずっと、手を握ったままでいたみたいだ。", "나오미를 받쳐 준 뒤로 줄곧 손을 잡은 채였던 모양이다."),
    ("f001_1be9ae60", 221, "rinka", "「あ、ごめん。痛かった？」", "“아, 미안. 아팠어?”"),
    ("f001_c3e05e7c", 226, "naomi", "「い、いえ！　全然……痛くはない、ですけど……」", "“아, 아니요! 전혀…… 아프지는, 않은데요……”"),
    ("f001_4595dbfc", 228, "narrator", "直未はうつむいたまま、そう答えた。", "나오미는 고개를 숙인 채 그렇게 대답했다."),
    ("f001_4df66257", 230, "narrator", "自覚はなかったがちょっと強く握り過ぎたかもしれないと思い、私は恐る恐る手を離した。", "자각은 없었지만 조금 세게 잡았을지도 모르겠다는 생각에, 나는 조심조심 손을 놓았다."),
    ("f001_ba90f33d", 235, "naomi", "「あ！　そ、その！」", "“아! 저, 저기!”"),
]


VOICE_TAG = {"rinka": "rnk", "naomi": "nom"}


def main() -> None:
    draft_dir = PROJECT / "translations" / "draft" / "scenario"
    rpy_dir = PROJECT / "work" / "draft_rpy" / "tl" / "korean" / "scenario"
    draft_dir.mkdir(parents=True, exist_ok=True)
    rpy_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for seq, (translation_id, source_line, speaker, source_jp, draft_ko) in enumerate(ENTRIES, 1):
        records.append(
            {
                "stable_id": f"scenario/001.rpy::{translation_id}",
                "sequence": seq,
                "translation_id": translation_id,
                "source_file": "scenario/001.rpy",
                "source_line": source_line,
                "speaker": speaker,
                "source_jp": source_jp,
                "draft_ko": draft_ko,
                "source_authority": "Japanese only",
                "english_reference_used": False,
                "status": "first_draft_unreviewed",
                "qa": "deferred_until_full_first_draft",
            }
        )

    payload = {
        "packet_id": "scenario_001_part001",
        "source_language": "Japanese",
        "target_language": "Korean",
        "entry_count": len(records),
        "status": "first_draft_unreviewed",
        "qa_policy": "No translation QA until the complete first draft is finished; review once afterward.",
        "english_text_in_translator_packet": False,
        "entries": records,
    }
    (draft_dir / "001_part001.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    lines = [
        "# Fatal Twelve Korean first draft",
        "# Source: Japanese only. English prose was not used.",
        "# Status: unreviewed; translation QA deferred until the complete first draft.",
        "",
    ]
    for record in records:
        lines.append(f"translate korean {record['translation_id']}:")
        lines.append("")
        speaker = record["speaker"]
        if speaker in VOICE_TAG:
            lines.append(f'    voice get_voice_filename("{VOICE_TAG[speaker]}")')
            lines.append("")
        prefix = "" if speaker == "narrator" else f"{speaker} "
        lines.append(f"    {prefix}{json.dumps(record['draft_ko'], ensure_ascii=False)}")
        lines.append("")
        lines.append("")
    (rpy_dir / "001_part001.rpy").write_text("\n".join(lines), encoding="utf-8", newline="\n")

    print(f"wrote {len(records)} Japanese-to-Korean draft entries")
    print(draft_dir / "001_part001.json")
    print(rpy_dir / "001_part001.rpy")


if __name__ == "__main__":
    main()

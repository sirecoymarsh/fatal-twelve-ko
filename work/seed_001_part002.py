from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko")


# translation_id, source_line, speaker, Japanese source, Korean first draft, optional Ren'Py tail
ENTRIES = [
    ("f001_f743c599", 240, "naomi", "「で、電車が来そうですし。い！行きましょう！」", "“저, 전철도 곧 올 것 같고. 가, 가요!”", ""),
    ("f001_4cc96fb3", 242, "narrator", "直未は転んだときにずれた眼鏡の位置を両手で直すと、慌てた調子でホームの方を指さした。", "나오미는 넘어질 때 비뚤어진 안경을 양손으로 고쳐 쓰고는, 다급한 어조로 승강장 쪽을 가리켰다.", ""),
    ("f001_612a0fbe", 244, "narrator", "１分前の繰り返しになるが、こういう時は大体――。", "1분 전과 똑같은 말이 되겠지만, 이럴 때는 대개――.", ""),
    ("f001_f67093cd", 252, "naomi", "「きゃっ！」", "“꺅!”", " with quake_fast"),
    ("f001_3bc493f4", 257, "rinka", "「もう、落ち着かないから！」", "“정말, 좀 진정해!”", ""),
    ("f001_4229b38e", 261, "narrator", "直未が歩き出したのと同時に通りかかった人にぶつかってしまう。", "나오미가 걷기 시작한 순간 마침 지나가던 사람과 부딪치고 말았다.", ""),
    ("f001_f1d8c559", 263, "narrator", "しかも、今度はぶつかった相手と一緒に転んでしまった。", "게다가 이번에는 부딪친 상대와 함께 넘어지고 말았다.", ""),
    ("f001_588e8415", 268, "naomi", "「す、すみません！」", "“죄, 죄송해요!”", ""),
    ("f001_a128379e", 273, "rinka", "「ごめんなさい、私の後輩が……」", "“미안해. 내 후배가……”", ""),
    ("f001_164986d8", 279, "narrator", "私は、起き上がろうとする直未たちの方へ近づいた。", "나는 몸을 일으키려는 나오미와 상대 쪽으로 다가갔다.", ""),
    ("f001_53102087", 281, "narrator", "直未にぶつかられた相手は、直未よりも年下の少女に見えた。背丈は私とそう変わらないが、顔つきがもう少し幼かった。", "나오미와 부딪친 상대는 나오미보다도 어린 소녀로 보였다. 키는 나와 별 차이가 없었지만, 얼굴 생김새가 조금 더 앳됐다.", ""),
    ("f001_b7cd9412", 283, "narrator", "直未も大きな目のせいで高校生ではなく中学生に間違われがちだが、それよりも明らかに幼い。", "나오미도 큰 눈 때문에 고등학생이 아니라 중학생으로 오해받곤 하지만, 그보다도 확실히 어려 보였다.", ""),
    ("f001_e5ceb827", 291, "yuu_unk1", "「…………」", "“…………”", ""),
    ("f001_b8a8dcc6", 297, "rinka", "「あ、あの。大丈夫かな？」", "“저, 저기. 괜찮아?”", ""),
    ("f001_5debcb07", 306, "narrator", "声をかけた時、少女と目が合った。目は薄い色をしていた。帽子で隠していたが、見れば、髪も特徴的で綺麗な白髪だ。", "말을 건 순간 소녀와 눈이 마주쳤다. 눈동자는 옅은 색이었다. 모자에 가려져 있었지만, 자세히 보니 머리카락도 눈에 띄는 아름다운 백발이었다.", ""),
    ("f001_c2fa182f", 308, "narrator", "正面からしっかり見ると、幼いながらもそのはっきりとした目鼻立ちが際立った。", "정면에서 똑바로 보니, 어린 나이에도 또렷한 이목구비가 더욱 돋보였다.", ""),
    ("f001_076abf78", 310, "narrator", "恐らく、日本人ではないのだろう。ということは髪の色も地毛かもしれない。", "아마 일본인은 아닐 것이다. 그렇다면 머리색도 타고난 색일지 모른다.", ""),
    ("f001_e5ceb827_1", 317, "yuu_unk1", "「…………」", "“…………”", ""),
    ("f001_e13fe35d", 319, "narrator", "直未と異なり、少女は背中から転んでいた。", "나오미와 달리 소녀는 등부터 바닥에 쓰러져 있었다.", ""),
    ("f001_7fb57779", 321, "narrator", "後ろからぶつかられたのだが、転んだ時に素早く身を反転させ、背負っていたリュックを抱えて守っていたようだ。", "뒤에서 부딪혔는데도 넘어지는 순간 재빨리 몸을 돌려, 등에 메고 있던 배낭을 끌어안아 지킨 모양이다.", ""),
    ("f001_ca0a2d04", 323, "narrator", "ずいぶん大きな荷物だ。恐らく、旅行者だろう。", "제법 큰 짐이었다. 아마 여행객이겠지.", ""),
    ("f001_1c06b871", 325, "narrator", "鞄の中にカメラなどの壊れやすいものが入っているために、荷物をかばったのかもしれない。", "가방 안에 카메라 같은 깨지기 쉬운 물건이 들어 있어서 짐을 감싼 걸지도 모른다.", ""),
    ("f001_5c55d1dd", 327, "narrator", "一人でいるということは、家族で日本に来ていてはぐれてしまったのだろうか。", "혼자 있는 걸 보면 가족과 함께 일본에 왔다가 떨어진 걸까.", ""),
    ("f001_5537a09b", 329, "narrator", "リュックには鍵の形をしたキーホルダーがついていた。", "배낭에는 열쇠 모양의 열쇠고리가 달려 있었다.", ""),
    ("f001_20305a99", 331, "narrator", "少女はすぐにすっくと立ち上がって、自分のかばった荷物を抱えたままこちらを睨むように見つめていた。", "소녀는 곧바로 벌떡 일어나 자신이 감싸 지킨 짐을 끌어안은 채, 우리를 노려보듯 바라보고 있었다.", ""),
    ("f001_833e8ce2", 337, "yuu_unk2", "「…………」", "“…………”", ""),
    ("f001_edf4bd95", 346, "rinka", "「直未、ほら、ちゃんと謝らないと」", "“나오미, 자. 제대로 사과해야지.”", ""),
    ("f001_31ef98a3", 348, "narrator", "直未は慌てていたのもあり立ち上がるのに手間取っていたようで、結局私の手を借りて体勢を整えた。", "나오미는 당황한 탓인지 일어서는 데 애를 먹고 있었고, 결국 내 손을 빌려 자세를 추슬렀다.", ""),
    ("f001_26bc2806", 353, "naomi", "「ほっ、本当にごめんなさい……あれ、外国の人？　わたしの言葉通じてっ……、こういう時はその、ソーリー？　パードン？」", "“저, 정말 죄송해요…… 어라, 외국인인가? 제 말이 통하……, 이럴 때는 그, 쏘리? 파든?”", ""),
    ("f001_6c394e5f", 358, "rinka", "「直未、とりあえず落ち着きなって」", "“나오미, 일단 진정해.”", ""),
    ("f001_833e8ce2_1", 370, "yuu_unk2", "「…………」", "“…………”", ""),
    ("f001_8801becf", 373, "narrator", "少女は直未がひととおり言い終えて頭を下げるのを見ていたが、言葉は発しなかった。", "소녀는 나오미가 한바탕 말을 쏟아 내고 고개 숙이는 모습을 지켜봤지만 아무 말도 하지 않았다.", ""),
    ("f001_bb303be4", 375, "narrator", "何やら訴えたいようだったが、彼女は黙ったままだった。", "뭔가 호소하고 싶은 듯했지만, 그녀는 입을 다문 채였다.", ""),
    ("f001_2f692f63", 380, "narrator", "そして、結局私たちの謝罪が通じたのがどうか分からないまま、ホームの方へと早足で去っていった。", "결국 우리의 사과가 전해졌는지도 알 수 없는 채, 소녀는 승강장 쪽으로 빠르게 걸어갔다.", ""),
    ("f001_bba0bd1f", 382, "narrator", "少女は一度だけ振り返ったが、直未ではなく私と目が合ったようだ。", "소녀는 한 번 뒤돌아봤지만, 나오미가 아니라 나와 눈이 마주친 듯했다.", ""),
    ("f001_454dea1a", 384, "narrator", "人混みの中に紛れてもしばらくはその容姿のおかげで目立っていた。", "인파 속에 섞인 뒤에도 한동안은 눈에 띄는 외모 덕분에 쉽게 보였다.", ""),
    ("f001_62d289ab", 386, "narrator", "同じように私の髪も目立つから、見つけやすかったのかもしれない。", "내 머리도 마찬가지로 눈에 띄니, 그쪽에서도 나를 찾기 쉬웠을지 모른다.", ""),
    ("f001_accf01fd", 388, "narrator", "親の元へ向かったのか、それともまさかあの歳にもかかわらず一人で日本へ来たのかなど、何も分からないままであった。", "부모에게 간 건지, 설마 그 나이에 혼자 일본에 온 건지, 아무것도 알 수 없었다.", ""),
    ("f001_5b1d004f", 393, "naomi", "「あの、ごめんなさい……」", "“저기, 죄송해요……”", ""),
    ("f001_fb755162", 398, "rinka", "「私に謝っても仕方ないって。ま、あの子にもちゃんと謝ったし、怪我もしてないみたいだから大丈夫じゃないかな」", "“나한테 사과해 봐야 소용없다니까. 뭐, 그 애한테도 제대로 사과했고 다친 것 같지도 않으니 괜찮지 않을까.”", ""),
    ("f001_19d92d40", 403, "rinka", "「とはいえ、気をつけなね？　直未はいつも焦り過ぎなんだから」", "“그래도 조심해야 해. 나오미는 늘 너무 허둥대니까.”", ""),
    ("f001_7f04b1cd", 408, "naomi", "「はい！　石橋を叩いて壊すくらいに、慎重に歩きます」", "“네! 돌다리를 두드리다 부숴 버릴 만큼 조심해서 걸을게요.”", ""),
    ("f001_bc1d9809", 413, "rinka", "「それ、意識し過ぎて絶対転ぶパターンだから」", "“그러다 너무 의식해서 반드시 넘어지는 패턴이거든.”", ""),
    ("f001_e64e3172", 418, "rinka", "「あ、あの子……見えなくなった」", "“아, 그 애…… 안 보이게 됐네.”", ""),
    ("f001_1651a052", 423, "naomi", "「さっきの男の子、どうかしたんですか？　まさか本当は怪我してたとか……」", "“아까 그 남자애, 무슨 일 있나요? 설마 사실은 다쳤다든가……”", ""),
    ("f001_3a849883", 428, "rinka", "「男の子？　いや女の子じゃなかった？」", "“남자애? 아니, 여자애 아니었어?”", ""),
    ("f001_e079a137", 433, "naomi", "「あれ！　でも綺麗な顔立ちだったから女の子って言われても納得です。わたし……ま、また失礼なことを」", "“어라! 그래도 예쁘게 생겨서 여자애라고 해도 납득돼요. 저…… 또, 또 실례되는 말을……”", ""),
    ("f001_6743e1fb", 442, "rinka", "「そう言われると、私も男の子な気がしてくる――って、前にもこんな会話しなかったっけ？」", "“그 말을 들으니 나도 남자애였던 것 같아지네――그런데 우리 전에도 이런 얘기 하지 않았나?”", ""),
    ("f001_681f4be6", 444, "narrator", "私は「いや、まあそれはいいとして」と挟んでから続けた。", "나는 ‘아니, 뭐, 그건 됐고’라고 끼워 넣은 뒤 말을 이었다.", ""),
    ("f001_f54aa5ab", 449, "rinka", "「あの子くらいの年の旅行者っぽい人が一人でいるなんて珍しいから、ちょっと気になっただけだよ」", "“그 애 정도 나이의 여행객처럼 보이는 사람이 혼자 있는 건 드문 일이니까, 조금 신경 쓰였을 뿐이야.”", ""),
]


VOICE_TAG = {
    "rinka": "rnk",
    "naomi": "nom",
    "yuu_unk1": "yuu",
    "yuu_unk2": "yuu",
}


def main() -> None:
    draft_dir = PROJECT / "translations" / "draft" / "scenario"
    rpy_dir = PROJECT / "work" / "draft_rpy" / "tl" / "korean" / "scenario"
    draft_dir.mkdir(parents=True, exist_ok=True)
    rpy_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for sequence, (translation_id, source_line, speaker, source_jp, draft_ko, tail) in enumerate(ENTRIES, 51):
        records.append(
            {
                "stable_id": f"scenario/001.rpy::{translation_id}",
                "sequence": sequence,
                "translation_id": translation_id,
                "source_file": "scenario/001.rpy",
                "source_line": source_line,
                "speaker": speaker,
                "source_jp": source_jp,
                "draft_ko": draft_ko,
                "renpy_tail": tail,
                "source_authority": "Japanese only",
                "english_reference_used": False,
                "status": "first_draft_unreviewed",
                "qa": "deferred_until_full_first_draft",
            }
        )

    payload = {
        "packet_id": "scenario_001_part002",
        "source_language": "Japanese",
        "target_language": "Korean",
        "entry_count": len(records),
        "status": "first_draft_unreviewed",
        "qa_policy": "No translation QA until the complete first draft is finished; review once afterward.",
        "english_text_in_translator_packet": False,
        "entries": records,
    }
    (draft_dir / "001_part002.json").write_text(
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
        rendered = json.dumps(record["draft_ko"], ensure_ascii=False)
        lines.append(f"    {prefix}{rendered}{record['renpy_tail']}")
        lines.append("")
        lines.append("")
    (rpy_dir / "001_part002.rpy").write_text("\n".join(lines), encoding="utf-8", newline="\n")

    print(f"wrote {len(records)} Japanese-to-Korean draft entries")
    print(draft_dir / "001_part002.json")
    print(rpy_dir / "001_part002.rpy")


if __name__ == "__main__":
    main()

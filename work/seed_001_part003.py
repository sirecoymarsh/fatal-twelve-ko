from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko")


ENTRIES = [
    ("f001_543a2a93", 454, "rinka", "「それに、どこかで会ったことがあるような気がして」", "“게다가 어디선가 만난 적이 있는 것 같아서.”"),
    ("f001_fff18ca1", 459, "naomi", "「……先輩、デジャブなんじゃないですか？　この路線って観光の人も多いですし、似たような会話をしててもおかしくなさそうです」", "“……선배, 데자뷔 아닐까요? 이 노선은 관광객도 많고, 비슷한 이야기를 나눈 적이 있어도 이상하지 않을 것 같아요.”"),
    ("f001_10e1937e", 464, "rinka", "「あー、確かに{rb}海晴{/rb}{rt}みはる{/rt}か{rb}真央{/rb}{rt}まお{/rt}と話してるかもね」", "“아, 확실히 미하루나 마오랑 얘기했을지도 모르겠네.”"),
    ("f001_a51f3468", 466, "narrator", "二人とも、直未と面識のある私の同級生だ。", "둘 다 나오미와도 아는 사이인 내 동급생이다."),
    ("f001_e201b9c8", 469, "narrator", "話が落ち着いたところで、電車の到着する音が聞こえてきた。直未も気付いたようで、二人の足は自然とホームへ向く。", "이야기가 일단락되자 전철이 도착하는 소리가 들려왔다. 나오미도 알아챘는지, 우리 둘은 자연스레 승강장으로 향했다."),
    ("f001_b2228902", 474, "rinka", "「私たちも行こうか。今度は転ばないでね？」", "“우리도 갈까? 이번에는 넘어지지 말고.”"),
    ("f001_8aad19d4", 479, "naomi", "「はい！」", "“네!”"),
    ("f001_772c32ef", 481, "narrator", "それ以降は特に、ぶつかった彼女もしくは彼のことを気にかけることはなく、私たちは新宿方面の電車に乗った。", "그 뒤로는 부딪쳤던 그 여자애인지 남자애인지를 딱히 신경 쓰지 않은 채, 우리는 신주쿠 방면 전철에 올랐다."),
    ("f001_c1b0c312", 498, "narrator", "私たちが乗り込んだのは、{rb}王塚{/rb}{rt}おうつか{/rt}駅。", "우리가 전철에 올라탄 곳은 오우츠카역."),
    ("f001_e21ae925", 500, "narrator", "そこから環状線で数駅の新宿で乗り換えて、地下鉄で２駅のところに私の家はある。", "거기서 순환선을 타고 몇 정거장 뒤인 신주쿠에서 갈아탄 다음, 지하철로 두 정거장 가면 우리 집이다."),
    ("f001_14a4df88", 502, "narrator", "時刻は午後5時頃。帰宅ラッシュと重なるせいで、環状線は大混雑だ。", "시간은 오후 5시쯤. 귀가 시간대와 겹쳐 순환선은 몹시 붐볐다."),
    ("f001_1851f125", 504, "narrator", "直未と私はほぼ密着状態で電車に揺られていた。", "나오미와 나는 거의 맞붙은 채 전철에 몸을 맡기고 있었다."),
    ("f001_cda9db13", 510, "naomi", "「ご、ごめんなさい、わたしが遅くなっちゃったからラッシュに巻き込まれちゃって……」", "“죄, 죄송해요. 제가 늦어져서 이렇게 붐빌 때 걸려 버렸네요……”"),
    ("f001_1885d1d1", 516, "rinka", "「いや直未が謝ることじゃないし。私だって慣れっこだから気にしなくていいよ」", "“아니, 나오미가 사과할 일도 아니고. 나도 익숙하니까 신경 쓰지 마.”"),
    ("f001_99d0f9a5_1", 521, "naomi", "「す、すみません……」", "“죄, 죄송해요……”"),
    ("f001_f69fad58", 533, "rinka", "「ってあれ、そこにあるのって」", "“그런데 어라, 저기 있는 건……”"),
    ("f001_f4e3fa3a", 542, "narrator", "人混みの中に、見覚えのあるリュックサックを見つけた。", "인파 속에서 낯익은 배낭을 발견했다."),
    ("f001_cbc2e2d4", 544, "narrator", "リュック自体はよくある形なので、正確には鍵のモチーフのキーホルダーに見覚えがあった。", "배낭 자체는 흔한 모양이니, 정확히는 열쇠 모양 열쇠고리가 눈에 익었다."),
    ("f001_79833bce", 546, "narrator", "案の定、さっきの子の姿もそこにあった。", "아니나 다를까, 아까 그 아이도 그곳에 있었다."),
    ("f001_2974cdfd", 548, "narrator", "大きなリュックを体の前に抱えて、車両の真ん中でうつむいていた。", "커다란 배낭을 몸 앞에 끌어안고, 객차 한가운데서 고개를 숙이고 있었다."),
    ("f001_70a47dba", 550, "narrator", "吊革に手は届かなそうだったが、人に挟まれているせいで転ぶこともなさそうだ。", "손잡이에는 손이 닿지 않을 듯했지만, 사람들 사이에 끼어 있어서 넘어질 일도 없어 보였다."),
    ("f001_3d4bf7c6", 559, "rinka", "「同じ車両だったんだ」", "“같은 칸이었구나.”"),
    ("f001_fbd2ac97", 564, "naomi", "「え？　どうしたんですか？」", "“네? 무슨 일이에요?”"),
    ("f001_b1b37b58", 573, "rinka", "「あれ？　あの子……リュック開いちゃってるな」", "“어라? 저 애…… 배낭이 열렸는데.”"),
    ("f001_31748f90", 575, "narrator", "満員電車で揉まれているうちに、リュックのチャックが開いてしまったのだろうか。", "만원 전철에서 이리저리 떠밀리는 사이 배낭 지퍼가 열린 걸까."),
    ("f001_d2cee431", 577, "narrator", "それどころじゃないのか、あの子は気付いていないようだった。", "그럴 정신조차 없는지, 그 애는 알아채지 못한 듯했다."),
    ("f001_b7f83d8b", 579, "narrator", "周りの乗客も、その子のリュックのことなんて興味がなさそうだった。視界にすら入っていないのだろう。", "주변 승객들도 그 아이의 배낭 따위에는 관심이 없어 보였다. 아예 눈에 들어오지도 않는 거겠지."),
    ("f001_4ddc27d2", 581, "narrator", "新聞を読んだり、中吊りを見たりして時間を潰している。一番多いのはスマートフォンではあるけれど。", "신문을 읽거나 차내 광고를 보며 시간을 보내고 있다. 가장 많은 건 스마트폰이지만."),
    ("f001_6281fea8", 583, "narrator", "私も、さっき直未がぶつからなかったら意識していなかったと思う。", "나도 아까 나오미가 부딪치지 않았다면 신경 쓰지 않았을 것이다."),
    ("f001_5b96a0ea", 585, "narrator", "だからあの子が何をしているのかは、私だけが目撃していた。", "그래서 그 애가 뭘 하고 있는지를 목격한 사람은 나뿐이었다."),
    ("f001_8da1d2e3", 587, "narrator", "追い詰められたような、深刻な表情も――。", "궁지에 몰린 듯한, 심각한 표정도――."),
    ("f001_d5e25177", 593, "rinka", "「機械……？」", "“기계……?”"),
    ("f001_e2f0d51d", 598, "narrator", "リュックの隙間から、何か真っ黒い物がのぞく。", "배낭 틈으로 새까만 무언가가 보였다."),
    ("f001_c2fcc6c4", 600, "narrator", "カメラやパソコンなどではない。", "카메라나 컴퓨터 같은 건 아니다."),
    ("f001_66ac87ab", 602, "narrator", "直感的に、私はフィクションの世界だけでしか見たことのない物の姿を思い出した。", "나는 직감적으로, 허구 속에서만 본 적 있는 물건의 모습을 떠올렸다."),
    ("f001_d4c3c1cb", 612, "rinka", "「爆――」", "“폭――”"),
    ("f001_30abc69c", 614, "narrator", "私が思わず口走ったのとほぼ同時であった。", "내가 나도 모르게 입 밖에 낸 것과 거의 동시에 일어난 일이었다."),
    ("f001_7a2f3873", 616, "narrator", "リュックの中から閃光が走る。", "배낭 안에서 섬광이 번뜩였다."),
    ("f001_acb39ed0", 628, "naomi", "「ばく？」", "“폭?”"),
    ("f001_84d44b62", 633, "rinka", "「直未っ！」", "“나오미!”"),
    ("f001_0ad924e8", 647, "narrator", "その瞬間だった。", "바로 그 순간이었다."),
    ("f001_42d80080", 649, "narrator", "車内に身の焼けるような熱がほとばしる。", "차 안으로 몸이 타 버릴 듯한 열기가 터져 나왔다."),
    ("f001_bb0721ef", 651, "narrator", "直後、鼓膜を破裂させるほどの轟音が響く。", "직후, 고막이 터질 만큼 거대한 굉음이 울렸다."),
    ("f001_9cca664f", 653, "narrator", "私は直未に覆い被さりながら彼女を突き飛ばした。", "나는 나오미를 몸으로 감싸며 밀쳐 냈다."),
    ("f001_dd13b953", 655, "narrator", "自分の体が衝撃と熱に押しのけられるのを感じた。", "충격과 열기에 내 몸이 밀려나는 것이 느껴졌다."),
    ("f001_b8361285", 657, "narrator", "――それは、文字通り体が焼けていく瞬間であった。", "――그건 말 그대로 몸이 타들어 가는 순간이었다."),
    ("f001_cebb6063", 677, "narrator", "炎の中に、自分の意志だけが置き去りにされていた。", "불길 속에 내 의지만이 덩그러니 남겨져 있었다."),
    ("f001_93019396", 682, "naomi_unk1", "「――ぱい！」", "“――배!”"),
    ("f001_fdace3ba", 684, "narrator", "声が聞こえる。", "목소리가 들린다."),
    ("f001_549105df", 686, "narrator", "私に感覚はなかった。", "나에게는 아무 감각도 없었다."),
]


VOICE_TAG = {"rinka": "rnk", "naomi": "nom", "naomi_unk1": "nom"}


def main() -> None:
    draft_dir = PROJECT / "translations" / "draft" / "scenario"
    rpy_dir = PROJECT / "work" / "draft_rpy" / "tl" / "korean" / "scenario"
    draft_dir.mkdir(parents=True, exist_ok=True)
    rpy_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for sequence, (translation_id, source_line, speaker, source_jp, draft_ko) in enumerate(ENTRIES, 101):
        records.append({
            "stable_id": f"scenario/001.rpy::{translation_id}",
            "sequence": sequence,
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
        })

    payload = {
        "packet_id": "scenario_001_part003",
        "source_language": "Japanese",
        "target_language": "Korean",
        "entry_count": len(records),
        "status": "first_draft_unreviewed",
        "qa_policy": "No translation QA until the complete first draft is finished; review once afterward.",
        "english_text_in_translator_packet": False,
        "entries": records,
    }
    (draft_dir / "001_part003.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

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
    (rpy_dir / "001_part003.rpy").write_text("\n".join(lines), encoding="utf-8", newline="\n")

    print(f"wrote {len(records)} Japanese-to-Korean draft entries")
    print(draft_dir / "001_part003.json")
    print(rpy_dir / "001_part003.rpy")


if __name__ == "__main__":
    main()

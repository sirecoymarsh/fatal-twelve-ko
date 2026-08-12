

label fMIHARU:

    if not _in_replay:
        call staffroll ("ED_MHR_UNH.mkv")

    call set_replay







    python:
        set_info_date(7, 23, "mon")
        set_info_time("noon")
        set_info_location("17")


    stop music fadeout 2
    scene ecg miharuend normal with fade_longest
    play music audio.miharu
    pause 1

    $ show_hud()


    voice get_voice_filename("rnk", 1883)
    rinka "「……いける」"

    "公園のベンチに座って、私は紙コップに入れたコーヒーを飲んでいた。"

    "今日は一日この場所にいようと決めていた。"

    "どうやら今日はここにいなくてはならない日らしいから。"

    "だから、コーヒーを淹れてきたのだ。"

    "テイクアウト用の紙カップをサンプルでもらったので、それを試してみたのだ。"


    voice get_voice_filename("rnk")
    rinka "「今度、直未にも飲んでもらおう」"

    "この場所は。"

    "私にとっても、想い出の場所だ。"

    "海晴と初めて出会った場所であり。"

    "おばあちゃんと何度も来た場所であり。"

    "直未と罪の重さを分かち合った場所であり。"

    "運命の、終着点。"

    "私たち12人が≪いるはずだった≫場所。"

    "私の選択は、正しいものだったと信じている。"

    "結果として、海晴は私の中から消えなかった。"

    "長きに亘る≪女神の選定≫は、今日、完全に終わったのだ。"

    "私の中に残った迷惑な力はまだ薄れる気配がないけれど、あの男性の言葉の通り、時間の問題なのだろう。"

    "なかったことになってしまった日々に意味はあったのか。"

    "そんな疑問が風に乗って湧いた。"

    "答えは決まっている。"

    "意味なんてない。"

    "あるのはただ、想い出だけだ。"


    voice get_voice_filename("rnk")
    rinka "「あーあ、暇だなぁ」"

    "私は思わず、そう呟いていた。"

    "高い空を見上げて。"

    $ renpy.end_replay()
    $ add_seen_chapter("12_2-4")

    call show_ending_image ("gui/MIHARUEND.png", True)

    $ persistent.MIHARU_clear = True
    $ grant_achievement("ending_02")
    $ grant_end_comp()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

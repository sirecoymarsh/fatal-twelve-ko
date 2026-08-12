

label fBAD_04:

    if not _in_replay:
        call staffroll ("ED_BAD.mkv")

    call set_replay






    python:
        set_info_date(7, 27, "fri")
        set_info_time("night")
        set_info_location("06")


    stop music fadeout 2
    scene bg amusementpark night with fade_longest
    play music audio.amusementpark_night
    pause 1

    $ show_hud()

    "ワタクシたちは、遊園地に来ていました。"

    "それも、今日はなんとワタクシのお誕生日。"

    "一日たっぷり、皆サマと遊びました。"

    show mao sci sel lau rev at std_l with std_in

    voice get_voice_filename("mao", 358)
    mao "「いやー、楽しかったねぇ」"

    show nom sci nor nor at std_c with std_in

    voice get_voice_filename("nom", 649)
    naomi "「わたしも……楽しかったです」"

    "お二人の間には、どこか寂しい空気が流れています。"

    "無理もありません。"

    "海晴サマのことを思い出しているのでしょう。"

    "ワタクシも、凛火サマの記憶に触れて数日。"

    "彼女の存在の大きさには、すでに気がついておりますもの。"

    show rnk sci nor 9sm at std_r with std_in

    voice get_voice_filename("rnk", 1880)
    rinka "「二人とも、ありがとう。今日はとても……楽しかった」"

    "すっかり、ワタクシの言葉遣いも板についてきました。"

    "少し間を入れるのがポイントのようです。"

    show rnk sci arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「色々あったけどさ、こうしてここに来られることはきっと、幸せだと思う」"

    "きっとこういう言葉が、この時の正解なのでしょう。"

    "私はお二人サマの目を見て、しっかりと口にするのです。"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「ね、りーたんはりーたんだよね？」"

    "真央サマが、私に訊ねます。"

    "ワタクシは質問の意図が分からず、戸惑ってしまいました。"

    "どう答えようか考えていると、真央サマの方から答えてくださいました。"

    show mao sci nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「ごめん、変なこと聞いちゃったよねぇ」"

    show mao sci nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんはりーたん。間違いないよね」"

    show nom sci que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「そ、そうですよ！　凛火先輩は……凛火先輩ですよね」"

    show rnk sci nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「……変なの」"

    "こうして私は、17歳になりました。"

    "さて、後は夜のパレードを見て帰りましょう。"









    $ set_info_location("02")


    stop music fadeout 2
    scene bg station01 night with fade_longest
    play music audio.death
    pause 1

    "その事件は、早速ニュースになっていた。"

    "小熊真央は、心にぽっかりと穴が空いてしまったせいで、家に帰ることができずにいた。"

    show mao sci nor ser at std_c with std_in

    voice get_voice_filename("mao")
    mao "「りーたんまで……」"

    "ニュースの内容は、こうだ。"

    "老若男女問わず人気のスターダストキングダムで、事故が発生した。"

    "夜のパレード中、フロートが倒れ、近くで観覧していた女子高生が下敷きになった。"

    "多くの電飾を使用していたフロートは断線をきっかけに発火し、炎上。"

    "下敷きになった女子高生は救助虚しく、焼死した。"

    "被害者の名前は、獅子舞凛火。悲惨なことに、今日は17歳の誕生日であり、友人たちにお祝いしてもらいに来ていたのだ。"

    show mao sci nor ser with std_change

    voice get_voice_filename("mao")
    mao "「りーたん……」"

    "真央は、ただ泣くことしかできなかった。"

    "自分が抱えていた違和感などどうでもよかった。"

    "生きていなかったら、もうおしまいだ。"

    "この先はないのだ。"

    show mao sci nor sad with std_change

    voice get_voice_filename("mao")
    mao "「うわああっ」"

    "夜の駅。"

    "たくさんの人が、泣き叫ぶ真央のことを見て、無視をした。"

    stop music fadeout 3
    scene black with Dissolve(3)
    pause 2

    $ renpy.end_replay()
    $ add_seen_chapter("11_4-5")

    call show_ending_image ("gui/BADEND_04.png")

    $ persistent.BAD04_clear = True
    $ grant_achievement("bad_end_04")
    $ grant_end_comp()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

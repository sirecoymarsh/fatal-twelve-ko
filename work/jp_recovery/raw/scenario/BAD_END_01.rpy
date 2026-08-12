

label fBAD_01:

    if not _in_replay:
        call staffroll ("ED_BAD.mkv")

    call set_replay






    python:
        set_info_date(7, 23, "mon")
        set_info_time("noon")
        set_info_location("17")


    stop music fadeout 2
    scene bg shinjukugyoen noon with fade_longest
    play music audio.miharu
    pause 1

    $ show_hud()

    "ぼくは、一人でその場所に来ていた。"

    "ここは、女神の語る運命の終着点。"

    show mhr sci pai lie at std_c with std_in

    voice get_voice_filename("mhr", 933)
    miharu "「……虚しいな。凛火のいない世界というのは」"

    "女神の選定。"

    "昨晩、ぼくにとって地獄のような日々は終わったのだ。"

    "凛火が脱落した時点で、ぼくにとっての女神の選定は終わったはずだった。"

    "だが、凛火はそれを許さなかった。"

    "凛火はぼくに、真央と日辻さんをよろしく、と言ったのだ。"

    "最愛の人との約束は、守らなくてはならない。"

    "だから、勝ち残った。"

    "いかにしてぼくが選定の最後の一人になったのかは、この際割愛する。"

    "結果として、女神は再びぼくの中へ還ったということになる。"

    "さぞ、居心地がいいことだろう。"

    show mhr sci sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「この場所は、気持ちがいいよ。望むことなら、君と来たかった」"

    "遠くに、時計台が見える。"

    "凛火は、この場所が好きだったという。"

    "いつか一緒に来たいと思っていたけれど、いつしか叶わぬ夢になっていた。"

    "できることならぼくが女神になって、運命を変えたいとも思っていた。"

    "凛火が死ななかった世界に。"

    show mao sci nor nor rev at std_l with std_in

    voice get_voice_filename("mao", 337)
    mao "「あ、みはるん～」"

    "真央が、ぼくの名前を呼んだ。"

    "凛火がいないこの世界で、ぼくが唯一友人と呼べる人だ。"

    "女神の選定のために尽力していたぼくは、真央と過ごす時間も減っていた。"

    "だから今日は、放課後久々に同じ時間を共有することになる。"

    show mao sci nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「何か久し振りだよねぇ。こうやって、２人でさ」"

    show mhr sci pai lie with std_change

    voice get_voice_filename("mhr")
    miharu "「……そうだね」"

    "真央は、どこか遠くを見つめてそう言った。"

    "凛火の死の傷は、決して癒やされることはない。"

    "凛火は、ぼくたちの中であまりに大きな存在だった。"

    "どこへ行っても、凛火の姿が目に浮かぶ。"

    "ぼくは意図的に、その後悔を受け入れていた。"

    "たとえ幻想でも、この目で凛火の姿を見ることができるならばそれでもいい。"

    "選定以前から抱えていたぼくの問題は、結局のところ何も解決していなかった。"

    "ぼくには自分が優秀だという自負がある。"

    "しかし、女神の選定で生き残るためには、その優秀さを全てつぎ込む必要があったのだ。"

    "一人になっても、ぼくの人生は続く。"

    show mao sci sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「そろそろかなぁ、あ、来た来た！　なおりーん」"

    show nom gsc har pal at std_r with std_in

    voice get_voice_filename("nom", 644)
    naomi "「お、お待たせしました……きゃっ」"

    hide nom with std_out

    "眼鏡をかけた後輩の日辻直未だ。"

    "まるでわざとやっているのではないかというくらい、彼女はよく転ぶ。"

    show mhr sci pai lie rev with std_change_wait

    "顔を赤らめながら、彼女は体を起こした。"

    "ぼくを含めたこの３人が、仲良くいること。"

    "それが凛火がぼくに託した最後の願い。"

    show mhr sci sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……では行こうか、直未」"

    show nom gsc nor lau at std_r with std_in

    voice get_voice_filename("nom")
    naomi "「はい！」"

    show nom gsc har sur with std_change

    voice get_voice_filename("nom")
    naomi "「……って、ひゃっ、あれ、未島先輩、わたしのこと、名前で……」"

    show mhr sci nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「これから、始まるからね」"

    "そう、始まるのだ。"

    show nom gsc nor sur with std_change

    voice get_voice_filename("nom")
    naomi "「えっ……？」"

    show mhr sci sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「もう、ぼくのことも海晴でいいよ」"

    show mao sci sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「ほほう～？　みはるん、何かあったねぇ」"

    show mhr sci sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「大したことはないよ。ぼくから言い出さないと、今更呼び方を変えることもできないだろう？　だからだよ」"

    show nom gsc nor lau with std_change

    voice get_voice_filename("nom")
    naomi "「わ、分かりました。み、み、海晴先輩！」"

    "凛火の願いを叶える日々が、これから始まるのだ。"

    "凛火がこの世界にいないのならば、せめてその想いだけでも、痕跡だけでも、ぼくがこの世界に刻もう。"

    "そうやってたとえゆっくりでも気持ちを整理していけば、いつかぼくの心の深い霧が晴れるかもしれない。"

    show mhr sci pai lie with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ……」"

    "そんな風に思えたら、楽だったのに――。"

    stop music fadeout 3
    scene black with Dissolve(3)
    pause 2

    $ renpy.end_replay()
    $ add_seen_chapter("7_3-5")

    call show_ending_image ("gui/BADEND_01.png")

    $ persistent.BAD01_clear = True
    $ grant_achievement("bad_end_01")
    $ grant_end_comp()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

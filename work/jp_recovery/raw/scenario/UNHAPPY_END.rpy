

label fUNHAPPY:

    if not _in_replay:
        call staffroll ("ED_MHR_UNH.mkv")

    call set_replay







    python:
        set_info_date(7, 23, "mon")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "目を覚ました私は、ゆっくりと体を起こしていた。"

    "何だか、頭が重い。"

    show rnk paj arm nor at std_c with std_in

    voice get_voice_filename("rnk", 1898)
    rinka "「んー」"

    "声を出して、背伸びをした。"

    "今日は夏休み一日目。正確には、国民の休日である海の日だ。"

    "夏休みまでは、なんてことない日々が続いていた。"

    "夏休みくらいは、何か特別なことが起こるかな、なんて。"

    hide rnk with std_out

    "夢のようなことを考えながら、私は朝の仕度を始めた。"

    "現実は、そう簡単に覆らない。"

    "私や友人の真央や海晴、後輩の直未と、普通の日常を送っていくのだろうと、心のどこかでは分かっている。"







    python:
        set_info_time("noon")
        set_info_location("17")


    stop music fadeout 1
    scene bg shinjukugyoen noon with fade_long
    play music audio.nichijo03
    pause 1

    "自分でもどうしてここへ来たいと思ったのか、まったく覚えていなかった。"

    "ただふと散歩に行こうと思いつき、足がこの場所へと向かっていた。"

    "新宿御苑。"

    "時計台の見える、私の想い出の場所。おばあちゃんと一緒に何度もここに来たことがあった。"

    show cha sta nor smi rev at std_cl with std_in


    voice get_voice_filename("cha", 32)
    chan_unk1 "「すみません、ホテルを探しているんですけど」"

    "歩いていると、観光客風の女性に声をかけられた。"

    "ここは外国の人も多いから、珍しいことではないけれど。"

    show rnk sci nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ホテルを探してるなら、とりあえず公園から出た方がいいと思いますけど」"

    show cha sta nor que rev with std_change


    voice get_voice_filename("cha")
    chan_unk1 "「え、あれ？　公園？　あたしいつの間にここに来たんだろ……」"

    "この公園は入場料がかかるんだけどなと思いながら、私は彼女がスマホを見るのを見守っていた。"

    "傍らには爽やかな男性がいる。落ち着いた様子は、彼氏さんというか旦那さんに見えた。"

    show cha sta nor nor rev with std_change


    voice get_voice_filename("cha")
    chan_unk1 "「んー、まあいいや。とりあえずこの公園でお散歩しよっかな。行こっ、ビル」"

    show cha sta nor smi rev with std_change


    voice get_voice_filename("cha")
    chan_unk1 "「ありがとねっ！」"

    hide cha with std_out

    "そう言うと、女性は軽快な足取りで去っていった。"

    "そうやって行き当たりばったりだから迷うんだなと納得したけれど、一緒にいる男性も笑っているし、きっととてもいい関係なのだろう。"

    "あれ、でも。"

    "あの人、英語じゃなかったっけ。私が英語分かるはずないのに、会話できてた。"

    "不思議なことは、さらに続いた。"

    hide rnk
    show cnh sta nor nor at std_c
    with std_swap


    voice get_voice_filename("cnh", 24)
    chanho_unk1 "「……綺麗な庭園だ」"

    "スーツを着た男性が、一人でそう呟いていた。"

    hide cnh with std_out

    "その後一緒にいた家族と会話をしているのだが、それは中国語。まったく理解することができない。"

    "歩いていると、今度は向こうの方の人たちが目に入った。"

    "何やら賑やかな話し声が聞こえてきたのだ。"

    show fed sta nor pa1 at std_c with std_in


    voice get_voice_filename("fed", 405)
    federico_unk3 "「おいおい、こんなところ来てどうするんだ？」"

    show ode noj nor lau rev at std_l with std_in


    voice get_voice_filename("ode", 502)
    odette_unk3 "「あ？　理由なんてねーよ。これからしばらく日本で暮らさないといけねーんだ」"

    show ode noj nor inn rev with std_change


    voice get_voice_filename("ode")
    odette_unk3 "「ちったぁこの国の文化を楽しめよ、アンポンタン」"

    show fed sta nor bad with std_change


    voice get_voice_filename("fed")
    federico_unk3 "「ま、仕方がねーか。あんたの船も沈んじまって、行く場所もない。この国なら、組織の連中も来ないだろうしよ」"

    show fed sta nor ama with std_change


    voice get_voice_filename("fed")
    federico_unk3 "「だがこの国で飲むイタリアワインは高過ぎる！」"

    show ode noj arm smi rev with std_change


    voice get_voice_filename("ode")
    odette_unk3 "「てめーが行ったのはぼったくりのロクでもない店だろ、どーせ。やれやれ、今日はあたしがいい店を紹介してやるよ」"

    show ode noj nor lau rev with std_change


    voice get_voice_filename("ode")
    odette_unk3 "「かかっ、てめーのおごりでな」"

    show fed sta nor ir2 with std_change


    voice get_voice_filename("fed")
    federico_unk3 "「ハァ？」"

    show sca sta nor gre behind fed at std_r with std_in


    voice get_voice_filename("sca", 300)
    scale_unk2 "「お、画になる二人を発見。一枚撮らせてもらうよ」"

    show fed sta nor ang rev with std_change


    voice get_voice_filename("fed")
    federico_unk3 "「おいっ！　勝手に撮ってんじゃ……」"

    show sca sta nor lau with std_change


    voice get_voice_filename("sca")
    scale_unk2 "「ＨＡＨＡＨＡ、ネットにはアップしないから安心してくれ。ただのおれの趣味だ」"

    "彼らはみんな背が高いが、電車で見る男子高校生みたいにはしゃいでいる。"

    "初対面なのに、まるで昔からの知り合いのようだ。"

    hide sca
    hide ode
    hide fed
    show aln sta nor irr at std_cr
    with std_swap


    voice get_voice_filename("aln", 419)
    alan_unk5 "「……フン。この場所に似合わない五月蠅い連中だ」"

    "彼らから少し離れたところで、褐色の肌の青年が愚痴をこぼしていた。"

    show aln sta nor nor with std_change


    voice get_voice_filename("aln")
    alan_unk5 "「アムが日本へ留学したいと駄々をこねていたが、これは見送らせるべきか」"

    show kik sta nor nor rev at std_cl with std_in


    voice get_voice_filename("kik", 124)
    keiko_unk3 "「あら、いいところですよ。この国は」"

    show aln sta nor nor with std_change


    voice get_voice_filename("aln")
    alan_unk5 "「……そうか」"

    show kik sta nor lau rev with std_change


    voice get_voice_filename("kik")
    keiko_unk3 "「この子、生まれて３ヵ月になるんです」"

    show aln sta nor que with std_change


    voice get_voice_filename("aln")
    alan_unk5 "「なぜ僕にそれを？」"

    show kik sta nor lau rev with std_change


    voice get_voice_filename("kik")
    keiko_unk3 "「あなた、余裕がなさそうに見えるから。せっかくの観光なのですから、肩の力を抜けばいいのに。ねー、春樹くん？」"

    show aln sta nor tre with std_change


    voice get_voice_filename("aln")
    alan_unk5 "「仕事のついでに寄っただけだ。余計なお世話ではあるが……ここでは肩を張る必要もない、か」"

    hide aln
    hide kik
    with std_out

    "今日は、知らない人たちの会話がよく聞こえてくる。"

    "疑問に思っても、答えをくれる人はいない。"

    show yuu sta eml non at std_cr with std_in


    voice get_voice_filename("yuu", 385)
    yuu_unk7 "「……はぁ」"

    show sig sta inn lau rev at std_cl with std_in


    voice get_voice_filename("sgt", 269)
    ushizuka_unk2 "「元気がないようだのう。どれ、今日は大勝ちしたんじゃ。売店でアイスを買ってやろう」"

    show yuu sta eml non with std_change


    voice get_voice_filename("yuu")
    yuu_unk7 "「……うん」"

    "おじいさんと一緒にいる少女の背負っているリュックには、きらりと金色の鍵が光っていた。"

    hide yuu
    hide sig
    with std_out

    "今度は、その少女を見ていたらしい女の子の元気な声が聞こえた。"

    show son sta exp exp rev at std_cl with std_in


    voice get_voice_filename("son", 169)
    sonya_unk2 "「オトウサマ！　ソーニャもアイスを食べたいであります！」"

    "ぬいぐるみを連れた少女は、家族３人で歩いていた。"

    "裕福そうな彼らは、とても幸せそうだった。"

    show son sta ban lau rev with std_change


    voice get_voice_filename("son")
    sonya_unk2 "「パサジール、そこのオネエサマにご挨拶です」"

    show rnk sci nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ええっ……」"

    "少女はぬいぐるみのくまで、私にぺこりと挨拶をしてきた。"

    "突然のことに戸惑いながら、とりあえず会釈で返しておいた。"

    hide son with std_out

    "これでよかったのだろうかと思っていると、いつの間にか少女と両親は売店の方へと向かっていった。"

    "なんだか今日はずいぶん賑やかだなぁ、と思っていた。"

    "まるで不思議の国に来てしまった気分だが、気にしても無駄だと、どうでもよくなった。"

    hide rnk with std_out

    "帰ろうかなと思ったとき、ベンチに見慣れた姿を見かけた。"

    "私は忍び足で、彼女の隣に座る。"



    play music audio.thebonds
    scene ecg unhappyend01 normal with dissolve_long


    voice get_voice_filename("mhr", 955)
    miharu "「……ばれているよ、凛火？」"


    voice get_voice_filename("rnk")
    rinka "「ふふ、知ってる。どうしてここに？」"


    voice get_voice_filename("mhr")
    miharu "「君に会いたくなったからさ」"


    voice get_voice_filename("rnk")
    rinka "「なんだ。いつも通りか」"

    "私はそのまま、海晴の肩に寄り掛かった。海晴は背が高いので、どちらかというと腕に頭を預ける形になった。"


    voice get_voice_filename("mhr")
    miharu "「……凛火……」"

    "どうしてか、疲れてしまったのだ。"

    "海晴は顔をほのかに赤くして、私の方へ少しだけ、体を傾けた。"

    "私たちは当たり前に、生きている。"

    "たった一つの人生を、生きている。"





    scene white with dissolve_long
    pause 1



    "その黒猫は、夕焼けを背にしていた。"


    voice get_voice_filename("cat", 29)
    lete "「にゃーお」"

    "一声鳴くと、自由気ままに歩いていった。"


    scene white
    pause 2

    $ renpy.end_replay()
    $ add_seen_chapter("12_3-4")

    call show_ending_image ("gui/UNHAPPYEND.png", True)

    $ persistent.UNHAPPY_clear = True
    $ grant_achievement("ending_03")
    $ grant_end_comp()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

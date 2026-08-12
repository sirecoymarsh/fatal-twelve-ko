

label f012_01F:







    python:
        set_info_scene("186")
        set_info_date(7, 16, "mon")
        set_info_time("emorning")
        set_info_location("01")

    stop music fadeout 2
    scene ecg pattern nor a with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    show let sta nor sm1 at std_c with std_in


    voice get_voice_filename("let", 39)
    lete_unk1 "「こんばんは。あるいは、おはよう。こんにちは……ではないかな」"

    show let sta nor tro with std_change


    voice get_voice_filename("let")
    lete_unk1 "「私も女神のように何か決め台詞というものが欲しかったけれど、中々思いつかないものだね」"

    "夢の中で、私はまた中性的な男性に出会った。"

    "彼はくだけた口調で言うと、挑発的に微笑む。"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「さて、冗談はここまでとしよう」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君はついに、君にとって最も根源的なピースを手に入れた。あとはそのピースをはめれば、原風景が完成する」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「完成するはずのなかった記憶のパズル」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「さて。それでは君を忘却の先へと案内しよう」"


    stop music fadeout 1
    scene ecg dianafire normal with fade_long
    play music audio.firedeath
    pause 1

    "炎の中にいた。"

    "身を焦がすような炎だった。"

    "肌はただれ、肺は煙で焼かれている。"

    "徐々に命が灰になっていくのだと、もう指先ひとつすら動かせない私には実感があった。"


    voice get_voice_filename("other", 12)
    linda "「ダイアナ」"


    voice get_voice_filename("other")
    linda "「ダイアナ！」"


    voice get_voice_filename("other")
    linda "「ダイアナ！　いやだ、置いて行くなんて……いや……一緒じゃなきゃ……。ダイアナい――！」"

    "誰かが何かを叫ぶ声が聞こえた。"

    "その声の主が誰なのか、ようやく分かった。"

    "それは、奇妙な運命の屈折。"

    "この記憶は直未と私の記憶であり、両親と私の記憶であり――リンダとダイアナの記憶でもあったのだ。"



    voice get_voice_filename("har")
    diana "「…………ンダ……」"



    voice get_voice_filename("har")
    diana "「に……げ…………」"

    "炎は広がっていき、叫び声は空気の震える音にかき消される。"

    "声が全く聞こえなくなる頃、私の意識も消えていった。"









    python:
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "目を覚ました私は、たっぷり汗をかいていた。"

    show lete normal at cat_c with std_in


    voice get_voice_filename("cat", 17)
    lete "「にゃおーん」"

    "それが布団に潜り込んでいたレテの熱だけではないと、はっきりと自覚している。"



    hide lete with std_out

    "炎の記憶。"

    "私の中に眠っていたこの記憶は、私のものだけではなかったのだ。"

    "血が繋がっているからなのか、日記帳を見たからなのか、私はそのどちらもがこの記憶が私の中に眠っている原因だと思った。"

    "そして私は、カードブックに新しいカードが生成されていることに気がついた。"

    show rnk paj arm vig at std_c with std_in

    voice get_voice_filename("rnk", 1718)
    rinka "「女神パルカ――ダイアナの死因」"

    hide rnk with std_out

    "中毒死、とカードには書かれていた。"

    $ add_character_cards("rnk", ["13_death"])

    "火事の死因で最も多いのは、実はこの中毒死だ。"

    "有毒ガス、つまり一酸化炭素中毒。"

    "あの記憶で見たダイアナさんは、苦しそうに死んでいった。"

    show lete normal at cat_c with std_in


    voice get_voice_filename("cat", 18)
    lete "「にゃっ」"



    hide lete with std_out

    "私が机に移動したからか、レテもベッドからぴょん、と飛び降りた。"

    "いつもの調子なら、このままどこかへ行ってしまう。"

    "だが、今朝の私は、そうはさせたくなかった。"

    show lete angry at cat_c with std_in


    voice get_voice_filename("cat")
    lete "「ふぎゃっ」"

    "私の方を見たら早足になった気がしたので、思わず尻尾をつかんでしまった。"

    "レテが、私から逃げるように見えたからだ。"


    voice get_voice_filename("cat")
    lete "「ふーっ！」"

    "レテは私の方に向き直り、威嚇してきた。"

    "尻尾をつかまれるのは心地よくないらしい。"

    "だが私は気にせず、レテの尻尾を引っ張った。"

    "そのまま逃げようとするレテを抱きかかえて、前足の肉球を見た。"



    hide lete with std_out


    play music audio.gimon
    show rnk paj nor que rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「やっぱり――」"

    "そこには、傷があった。"

    "レテではなく、リンダさんの飼い猫のレオが負っているはずの傷だ。"

    "リンダさんの日記には、レオがガラスを踏んで肉球に傷を負ったと書いてあった。"

    "傷は、遺伝するものではない。"

    "レテがどこかで怪我をしちゃったということも考えられるが、私はその可能性は低いと思っていた。"

    show rnk paj nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「夢の中に出てくるあの男の人……あなたなんでしょ？　理由とか仕組みとか、分からないけどさ」"

    show lete normal at cat_r with std_in


    voice get_voice_filename("cat")
    lete "「にゃ？」"


    hide lete with std_out

    "私は非現実的だと思いつつも、レテに向かってそう問い掛けてみた。"

    "夢の中にあの男性が出てくるとき、いつも必ず隣にレテがいる。"

    "そのことを意識するようになったのは、ダイアナさんとレオが一緒に写っている写真を見てからだ。"

    "似ているではすまない――まさかこの頃からずっと生きているなんて、あり得るか、と疑問が浮かんだ。"

    "あり得ないことを疑わなければ、きっと私は≪女神の選定≫の真実に辿り着けない。"

    "この子の肉球が、決定的だった。"

    "人の体が女神のような存在の≪器≫になるなら、猫が何か超常的なものの≪器≫になってもおかしくはない。"

    show rnk paj nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「≪夢の世界≫でしか話せない……とかなのかな」"

    "レテがあの男性だと想像すると、今まで同じ布団で寝ていたのが急に恥ずかしくなり、私は無言でレテを椅子の上に座らせた。"

    show rnk paj arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「とにかく私の言っていることが分かるなら、今晩も私の夢の中に来て。それで、話をしよう」"

    show lete normal at cat_r with std_in


    voice get_voice_filename("cat")
    lete "「にゃ」"

    "返ってきたのはただの鳴き声だったが、私はそれをレテの返事だと思っていた。"









    python:
        set_info_time("noon")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 noon with fade_long
    pause 1

    $ show_hud()

    "週が明け、期末試験後の月曜日から木曜日は試験休みだ。"

    "全校生徒のテストを採点し、成績表を準備するため、一年で数回訪れる繁忙期の一つと言っていいだろう。"

    "先生も猫の手を借りたい状況だろう。"

    "一方で私は、猫とお話がしたい状況というのは奇妙なものだ。"

    "というわけで、試験休みの間は朝と夕方からお店を開けようと思っていた。"

    "変則的だが、平日はその方が喜んでもらえるだろう。"






    python:
        set_info_scene("187")
        set_info_time("night")
        set_info_location("05")

    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "一日があっという間に終わり、私は部屋に戻ってきていた。"

    "部屋の真ん中ではレテが丸くなっていたので、座布団を持ってきてその上に乗っけてあげた。"

    "やはりこの猫、私の言葉を分かっている。"

    show rnk paj nor smi at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……おやすみ」"

    "一通り寝る準備を終えた私は、明日も早起きなので眠ることにした。"

    "きっと今日は、睡眠時間が短く感じるだろうから。"





    python:
        set_info_time("lnight")
        set_info_location("01")


    stop music fadeout 2
    scene ecg pattern nor a with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    "ああ、やはり私の予想は正しかったんだ。"

    "それを裏付けるように、私は再び≪運命の大広間≫とは違う夢の世界に来ていた。"

    show let sta nor sm2 at std_c with std_in

    voice get_voice_filename("let")
    lete "「こんばんにゃ。正体が知られてしまった以上、もう隠す必要もないかにゃ」"

    show let sta nor sm2 with std_change

    voice get_voice_filename("let")
    lete "「ここで君が話せないのは仕方ないんだにゃ。私は女神パルカ――元ご主人と違って≪運命の大広間≫を作り出すことはできないのにゃ」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「君の存在を概念上に固定することはできにゃいということだにゃ」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「私ができるのは精々、君の夢の世界に干渉することだけなのにゃ」"

    "あの男性がいきなりよく分からない口調で喋り始めたせいで、大事なことを言っているのに全然頭に入ってこなかった。"

    "というか気持ち悪いからやめて欲しい。"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「はは、辛辣だな。もっとも私が伝えたかったのは、君は話すことはできなくてもこうして私に意志を伝えることができる、ということだ」"

    "それで、あなたは結局何{rt}・{/rt}なの？"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「私はレテ。冥府を流れる忘却の川。正確には、それを模した力を与えられた存在……かな」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「語られる文献によって多少の違いはあるけれど、死後の世界で川の水を飲んだ者は過去の記憶を忘れる――概ね、そんな川であることを知ってもらえればいいさ」"

    "えーと、よく分からないんだけど。"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「≪女神の選定≫で発生する世界の変化。その記憶の矛盾を忘却によって解決しているのが、この私だ」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「私には人の記憶に干渉するという役目が与えられていると思ってもらえればいい」"

    "それで、やっぱりあなたはレテだったんだね。"

    "いや、肉球に傷があるからレオ……なのかな。"

    "一体どうして、あなたは人の形をして、女神のように夢に出てこられるの？"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「私はもう、この世界の何でもない存在だからさ」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「これはただの猫が私になり、いたいけな少女が女神になったということから始まる物語さ」"

    "やっぱり、ダイアナさんが女神パルカになったというのは正しかった。"

    "この状況で彼が言うのだから、間違いはないだろう。"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「ああ。君たちがリンダの日記を見てそこへ辿り着く可能性はあると思っていた」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「もっとも、私は君にヒントを出し続けていたのだから、私の正体にまで辿り着いてもらわなければ困るけれどね」"

    "どういうこと？"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「私たちにとって、現実世界での場所という概念は関係のないもの。それでも君の夢の世界に現れる時には、傍らにいるようにしていただろう？」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「さて。私たちの力が借りものであり仮初である以上、そう長く話すこともできない。手短に私の正体、レテという私が生まれるまでを教えよう」"

    "この男性も、パルカと同じように時間を気にしている。"

    "彼の言葉が気になるが、今は彼の話を遮らないようにした。"


    play music audio.restlessness

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「私が≪忘却の川≫の力を与えられたのは結果論だ。順序が違う」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「ダイアナは、11人の死ののちに自らも火事で命を落とした。この形が、彼女が女神になるのに最適な形だったのだ」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「偶然か必然か、それは私も分からない」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「とにかく、彼女の≪生きたい≫という強烈な想いは、この世界に存在するかもしれない≪何か≫に届いた」"

    "彼はその≪何か≫を、人が神と呼ぶものであったり霊と呼ぶものであったりと補足した。"

    "同時に、人間には認識できないものとも付け加えた。"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「本来、それでは何も起こらない。けれども彼女の死の前には11人分の失われた命があった」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「ダイアナを中心として、11人分の生と死の可能性が螺旋を描き、運命の歪みとなって存在していた」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「その歪みに、彼ら11人が持っていた想いの欠片が蓄積していた。概念上の存在にとって、想いというのは一種のエネルギー」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「≪何か≫と繋がったダイアナ・ハリソンは、歪みに蓄積していた力を消費することで女神パルカになるという奇蹟を起こした」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「その状況で13人目となった、リンダ・ハリソンを≪器≫として」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「もっとも、≪何か≫とは程遠い、≪器≫と≪儀式≫を必要とする不完全な存在ではあるけれどね」"

    show let sta nor sm2 with std_change

    voice get_voice_filename("let")
    lete "「と、ここで愛らしくキュートなレオという猫の登場だ」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「ダイアナが命を落とした火事の中で、私もまた死が目前に迫っていた」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「ダイアナは、レオに死んで欲しくなかった。その一心で、ただでさえ不完全な自分の力を私に分け与えた」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「正確には、分け与えた力によって私は≪何か≫と繋がった。運命の輪から外れた私は、死という概念を忘れてしまった」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「人のような意思と輪郭のみが与えられた存在。人でも猫でも――もちろん神でもない。それが私さ」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「残念ながら、ダイアナの意志も空しくレオはこの世界からいなくなってしまった。レテは何にもなれない何かだからね」"

    "彼の話は正直、半分くらいしか理解することができなかった。"

    "頭では分かっても、きちんと習熟できない感じだ。"

    "だが、きっと彼の言いたいことは単純だ。"

    "ダイアナは死にたくないからパルカになって、レオに死んでほしくないからレテにしたのだ。"

    "ああ、知りたくなかった。"

    "だって、そんな考え方は――私たちと同じだから。"

    "彼の話は、まだ続く。"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「ダイアナは優しい少女だ」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「だから忘却の力を手に入れた私は、まずダイアナから人間である時の記憶のほとんどを奪った」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「パルカという存在から人間のような意思が失われない、ぎりぎりのところまでさ」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「何故だか分かるかい？」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「自分が存続するために≪女神の選定≫を行うという業」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「残酷な希望を背負わせ、断ち切るという罪」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「優しい彼女がそれに耐えられるはずがないと、私は思ったのさ」"

    "私たちの運命に対し、あくまで傍観者であり続けた彼女。"

    "楽しんでいるように見えて、決して心から楽しんでいるようには見えなかったあの少女。"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「そうさ。女神パルカには君たちのような心があるわけではない」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「だからこそ無慈悲に選定の管理者を続け、その存在を存続してきた」"

    "女神の選定は、ダイアナという少女が存在し続けるためのシステム。"

    "そういうこと、なのだろう。"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「さて、ここからは私のお願いだ」"

    "お願い？"

    show let sta nor sm2 with std_change

    voice get_voice_filename("let")
    lete "「ああ。忘却の川としてではなく、ご主人様を愛した猫としてのお願いだ」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「あの子を、救って欲しい」"

    "救う？"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「そうだ。あの子はついに、女神として野望を持ってしまった」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「それは概念上の存在であることを捨て、受肉すること。人間に対し≪器≫を超える利用を行うこと」"

    "ダイアナは、生き還ろうとしてるってこと？"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「違う。ダイアナはそんなこと望んではいない」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「長きにわたる≪選定≫で、彼女はすでにパルカという人格を作り出している」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「僅かに残ったダイアナの記憶をベースに、新たな人格が誕生しているんだ」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「人格というものにおいて、野望や欲望は切り離せない。だからこそ、パルカは野望を持つことになった」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「条件が揃ってしまったからだ」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「肉体的にも性質的にも、かつて人間だった自分と等しい者に出会ってしまったからだ」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「実の姉の子孫であり、生まれつき運命の歪みの中にいた少女にね」"

    "ダイアナの実の姉、リンダさん。"

    "そして選定期間中に生まれて、その命がなかったことにならなかった……。"

    "私だ。"

    "もっとも今残っているのは海晴か私なのだし、その意味でも消去法で私になってしまうけれど。"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「ご明察。君の友人の中から君を見たパルカは、君も選定の参加者になるように運命を変えた」"

    "――え？"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「それは、パルカが運命に逆らうことと同義」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「仮初の運命の女神であるパルカは、決して運命に勝つことはできない」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「運命は、世界は、正しい形に戻ろうとするからね」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「だからあの子が君の体を使って受肉しても、待っているのは悲惨な死さ」"

    "救うって、何をすればいいの？"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「君たちはすでに、あと一歩のところまで来ているだろう？」"

    "女神を――指名すればいいの？"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「指名というのは、個人を明らかにすることで運命を呼び戻す行為」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「パルカが指名されれば、ダイアナの運命は本来の運命に引き戻される。新しく生まれた人格ではあれど、パルカもダイアナと同質の存在」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「共に、この世界から消えていく――やっと、死ぬことができる」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「ダイアナはもう、十分に頑張った。運命に逆らうこともない」"

    "なら、運命に逆らおうとしている私たちは……。"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「君たちとダイアナは違う。≪女神の選定≫の参加者が生き残るというのは、≪生きている可能性≫の世界を本流にすることに過ぎない」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「でも、あの子にはもう≪生きている可能性≫がない。生まれてから百年以上経ってしまっているしね」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「これが本当の意味で、運命に逆らうと言うことだ」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「けれど、痛みが伴い、苦しみが伴う。それらは自覚のないうちに、澱となって溜まっていくものさ」"

    "あなたは、それでいいんですか？"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「ダイアナは、今も泣いている。これは、彼女の意志でもあるさ」"

    "それは、どういう？"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「さて、私が君の≪夢の世界≫と繋がっていられるのもそろそろ限界だ」"


    play music audio.fatalhall

    "待って。"

    "まだ私たちはパルカの≪未練≫を知らない。"

    "それに、まだ聞きたいことも……。"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「心配しなくても、君は間もなく全てを知ることになるだろう」"

    show let sta nor sm2 with std_change

    voice get_voice_filename("let")
    lete "「そして君もまた、私から脱却しなければならない。ここからは君たちが知恵を絞って、君たちの力でその日を迎えてくれ」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「君たちが幸せになることのできる、その日を」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「最後に一つ謝ろう。今回の≪女神の選定≫が始まった当初、君の記憶を抜いたのもやはり、私だ」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「君が女神の肉体に適合することを忘れさせるためには、君の記憶も抜き取る必要があったんだ」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「女神が意図的に君を勝たせることがないように――」"

    show let sta nor tro with std_change

    voice get_voice_filename("let")
    lete "「――いや、言い方を変えよう。今のご主人様は君だ。君のご友人も私は知っている。君が幸せになるには、二人とも生き残ることが前提条件だっただろう？」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「私ができる協力というのは、それくらいだからね」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「しかし、すでに彼女は君を狙っている。君が徐々に記憶を取り戻すにつれて、女神も記憶を取り戻しているからだ」"

    "私たち二人が、生き残れるように。"

    "それは……。"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「君が最初から全てを知っていたら、この{rb}現在{/rb}{rt}いま{/rt}は訪れていない。もっとも私が与えたのはきっかけだけ。{rb}現在{/rb}{rt}いま{/rt}に到達できたのは、君の力さ」"

    "ありがとう……なのかな。"

    show let sta nor sm2 with std_change

    voice get_voice_filename("let")
    lete "「お礼を言うのはこちらだ。猫として一緒にいる時間の方がはるかに長かったけれど、君はとてもいいご主人様だった」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「次に会うのは、全てが終わった時だ。これ以上、手を貸すのは、私のルール違反だ」"

    show let sta nor ser with std_change

    voice get_voice_filename("let")
    lete "「ルールというのは、何かを守るためのツール。私がルール違反ばかりしていては、この世界の秩序は守れない」"

    show let sta nor sm1 with std_change

    voice get_voice_filename("let")
    lete "「おっと、思わず笑顔になってしまうほどあどけない猫ちゃんの姿では、会うだろうけれど」"

    show let sta nor sm2 with std_change

    voice get_voice_filename("let")
    lete "「それでは、成功を祈ろう」"

    "長い話が終わり、私の意識は再びまどろみに落ちていく。"

    "夢は脳の整理というが、これじゃ整理どころか大混乱だ。"

    $ add_seen_chapter("12_1-1")








    python:
        set_info_scene("188")
        set_info_date(7, 17, "tue")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "目覚めると、座布団の上には思わず笑顔になってしまうほどあどけない黒猫が眠っていた。"

    scene bg myroom morning large:
        zoom 1.5
        align (0.0, 0.6)
    show rnk paj nor smi rev up at std_l
    with dissolve

    voice get_voice_filename("rnk")
    rinka "「ありがとね、レテ」"

    scene bg myroom morning with dissolve

    show lete normal at cat_c with std_in

    voice get_voice_filename("cat")
    lete "「にゃーお」"

    "レテの返事を聞いて、私はベッドから起き上がった。"

    "レテは私に、自分たちの手でその日を迎えろと言った。"


    hide lete with std_out

    "その日、それは12回目の選定を超えた日。"

    "来週の月曜日。"

    "私たちが生きる可能性があるはずの、その日だ。"

    show rnk paj arm nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「さて、今日も……」"

    hide rnk with std_out

    "仕度をしようと思ったところで、スマートフォンの着信音が鳴り響いた。"

    "表示されていた名前は、真央だ。"

    "チャットではなく、電話。"

    "私は息を飲んで、通話のボタンをタッチした。"



    voice get_voice_filename("mao", 305)
    mao "『りーたん！　なおりんが、なおりんが……』"

    "すぐに、焦った真央の声が響いた。"

    "私は思わず、スマートフォンを床の上に落していた。"







    python:
        set_info_time("noon")
        set_info_location("19")


    stop music fadeout 1
    scene bg hospitallounge on with fade_long
    play music audio.impatience
    pause 1

    $ show_hud()

    "急いで直未のお見舞いに行った私たちは、ラウンジで話していた。真央は海晴にも連絡をしていて、私たちは３人で集まっていた。"

    "結論から言うと、直未は緊急入院していた。"

    show mao sci nor ser rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「今朝、いきなり倒れたって……いつもみたいに家で本を読んでちょっとうとうとしてると思ってたら、いきなり頭が痛いって言い出して……」"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「ひどい熱が出てたみたいで……それで、なおりんのお母さんが救急車を呼んだんだって」"

    show mhr sci sco thi rev at std_c with std_in

    voice get_voice_filename("mhr", 854)
    miharu "「原因は、分かっていないようだね」"

    "私も、直未のお母さんから状況を聞いた。"

    "原因は不明。"

    "しかし意識はなく、あまりに突然のことに少しの心当たりもないらしい。"

    "無理もない。直未は、私から見ても健康そのものだった。"

    "過労で倒れたというのとも様子が違うし、お医者さんもただ点滴をして寝かせることくらいしかできないようだった。"

    show rnk sci nor que at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「どうして、真央のところに連絡が？」"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんのお店に行こうって誘おうとしたら、お母さんが出て。それで……」"

    "外から見れば原因不明の熱と頭痛。"

    "私は、一度直未がその症状に苦しめられたのを目の当たりにしていた。"

    show rnk sci arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「その本って、何の本か分かる？」"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「分かんない。とっても、古い本だったってことくらいしか……」"

    show mao sci nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「でも、古いからカビとかアレルギーとかが原因かっていうと、そうでもないみたいだよぅ……」"

    "なるほど、と私は返事をした。"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「今私たちにできることは――ないね。これから検査とかもあるみたいだし、一旦帰ろうか」"

    "私は海晴に目配せをしてから、病院を出ることにした。"







    $ set_info_location("04")

    stop music fadeout 1
    scene bg lion01 noon with fade_long
    pause 1

    $ show_hud()

    "海晴は私の合図に気付いてくれたようで、私がライオン館へ帰ると、時間差でやってきた。"

    "真央は特にショックを受けていたので、先に帰るようにうながしていた。"

    "それに、真央がいると、しにくい話もある。"


    play music audio.investigation

    scene ecg girlstalkP2 ser with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「10回目の選定の前にも直未が倒れたっていう話をしたの、覚えてる？」"

    show ecg girlstalkV2 ser with dissolve


    voice get_voice_filename("mhr", 855)
    miharu "「ああ。アラン・スコーピオンが日辻さんを助けたという一件だね」"

    "うん、と私は頷いた。"

    scene ecg girlstalkP2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「あの時も、直未は頭が痛いって言って倒れた。熱も出ていたし……あの夜よりも症状はひどいけど、似ている」"

    scene ecg girlstalkV2 ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「記憶の混濁が原因だと言っていたね。ぼくたちと違い、日辻さんは選定の度に毎回記憶が塗り替えられている」"

    show ecg girlstalkV2 tro with ecg_change


    voice get_voice_filename("mhr")
    miharu "「それが、彼女にとって負担になり、頭痛が発生しているということだったね」"

    "≪女神の選定≫の序盤、自分の記憶をなくしていた私も同じように頭痛に苦しめられることがあった。"

    "直未の場合は変化する前の記憶の上に変化した後の記憶が上書きされていることになる。"

    "単純に考えて、私よりも二倍の負担があるはずだ。"

    scene ecg girlstalkP2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「私のせいだ……、私が気付かなかったから」"

    scene ecg girlstalkV2 ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「君のせいではない。ぼくも……ぼくもその可能性を想定するべきだった」"

    "私と一緒にいてくれた直未。"

    "一度は距離を取ることにしたけれど、ユウくんの一件以降、私は直未に委細を報告するようになっていた。"

    "それは塗り替えられた直未の記憶に、再び塗り替えられる前の直未の記憶を上書きすることに等しい。"

    "もっと気を遣ってあげられれば、入院なんてことにはならなかったはずだ。"


    voice get_voice_filename("mhr")
    miharu "「……今はお互い責めても仕方がないね。ぼくたちは、日辻さんの意識が戻るのを信じるしかない」"


    voice get_voice_filename("mhr")
    miharu "「そして、今ぼくたちがすべきことは≪女神の選定≫について考えることだ」"

    scene ecg girlstalkP2 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「……うん。ありがとう」"

    "海晴が冷静で、助かった。"

    "いや、この状況では海晴も冷静ということはないだろう。"

    "私が焦っているから、冷静でいようとしてくれているだけだ。"

    "私は深呼吸をして、一旦座ろうと提案をした。"

    "気持ちを切り替えるなんて無理だけど、このままでは海晴か私のどちらかは確実に死ぬ。"

    "前に進もうとしなければいけない。"

    show ecg girlstalkP2 ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「……見て」"

    "言って、私は一枚のカードを取り出した。"

    "昨日作られた、ダイアナの死因が書かれたカードだ。"

    "そして私は海晴に、レテから聞いたことを話すことにした。"





    stop music fadeout 1
    scene ecg girlstalkV1 ser with fade_long
    play music audio.disclose
    pause 1

    "長い、話になった。"

    "気持ちを落ち着けるために淹れたコーヒーは、すっかり空になっていた。"


    voice get_voice_filename("mhr")
    miharu "「なるほど。多くの疑問は解決した。そして、君にしかダイアナのカードが作られていない理由も予想がつく」"

    "海晴がそう言ったのに対して、私は首を傾げた。"


    voice get_voice_filename("mhr")
    miharu "「パルカが君を求めるのは、彼女にとって君が特別だから。反対に言えば、君にとってもパルカ――ダイアナは特別なはずだ」"

    scene ecg girlstalkP1 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「私の中に元々女神と同じような≪何か≫があった。だから、私だけカードを作ることができた……？」"

    "私がそう言うと、海晴は「恐らくは」と同意した。"

    scene ecg girlstalkV1 ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「とにかく、猫ではない方のレテは、信用するしかないだろう。又聞きだからかもしれないけれど、話の辻褄も合う」"

    scene ecg girlstalkP1 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「うん。何よりあの子は私たちのことも、ダイアナさんのことも好きなんだと思う」"

    scene ecg girlstalkV1 smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「あれだけ長く存在しているというのなら、もはや親心のようなものかもしれないね」"



    "私たちが話していると、たまたま、レテがとことこと通りかかった。"

    "名前を呼ぶと、レテは体をびくっとさせてから振り向いた。"

    scene ecg girlstalkP1 que with dissolve


    voice get_voice_filename("rnk")
    rinka "「直未はきっと、記憶のことで苦しんでる。助けることは……できないの？」"

    "レテなら、彼ならきっとできると思っていた。"

    "その原因を知っているかもしれないし、忘却させることができるなら、記憶をどちらかに統一することも可能なのかもしれない。"


    voice get_voice_filename("rnk")
    rinka "「って、眠らないと喋れないよね。今ここで居眠りすれば、話せる？」"

    "しかしレテは猫らしからぬ動きで首を振った。"

    "その否定の意志が、単に私の質問に答えただけではないとすぐに理解する。"

    "レテが夢の中で、これ以上手は貸さないと言っていたことを思い出す。"

    scene ecg girlstalkV1 ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「ぼくからも頼む。君は、日辻さんを救う方法を知っているのだろう？」"

    "海晴も、レテと視線を合わせて頼み込む。"

    "だがレテは鳴き声もあげず、ただそっぽを向いて去っていってしまった。"

    "そんなレテを引き留めることはできない。"

    "レテの言葉を思い出す。"

    "――そして君もまた、私から脱却しなければならない。ここからは君たちが知恵を絞って、君たちの力でその日を迎えてくれ。"

    scene ecg girlstalkP1 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「レテは、こうなることを知っていた……？」"

    "それも含めて、私たちにあの言葉をかけたのではないか。"

    "だとすればこれは、私たちが乗り越えなければいけない問題。"

    scene ecg girlstalkV1 ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「とにかく、明日また日辻さんの様子を見に行こうか」"


    voice get_voice_filename("rnk")
    rinka "「うん。そうしよう」"


    scene bg lion01 noon with dissolve_long

    "私たちは、ここで一旦解散をした。"

    "できることは待つことだけ。"

    "女神の≪未練≫についても考える余裕がなく、もどかしさを感じずにはいられなかった。"

    $ add_seen_chapter("12_1-2")








    python:
        set_info_scene("189")
        set_info_date(7, 18, "wed")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    pause 1

    $ show_hud()

    "やはりと言うべきか、昨晩、レテは私の夢には現れなかった。"

    "すぐに頼ろうとするのが人間の悪い癖なのか、私の悪い癖なのかは分からない。"

    "今日も、真央と病院に行く約束をしている。"

    "海晴は朝からバイトがあるため、今日は夕方に行くことになっている。"

    "海晴とは、その後、ライオン館で女神の≪未練≫について話すことになっている。"

    "私は急いで、準備を始めた。"







    python:
        set_info_time("evening")
        set_info_location("19")


    stop music fadeout 1
    scene bg hospitallounge on with fade_long
    play music audio.kinpaku
    pause 1

    $ show_hud()

    show mao sci nor ser rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「……退院の目途、立たないって」"

    "真央は暗い声で、そう告げた。"

    "私たちは言葉にならない吐息で返事をし、真央は直未のお母さんから聞いたことを続けて話す。"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「なんとかスキャンって検査もしたらしいけど、分からない。こんなの……突然過ぎるよ」"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「原因不明だから……このまま目を覚まさない可能性も……あるって……」"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「なおりん……どうしちゃったの……」"

    "事情をまったく知らない真央は、私よりもずっと不安だろう。"

    "私は思わず、真央に≪女神の選定≫と記憶のことを話したくなってしまう。"

    "だが、海晴が私の上着のすそをつかむ。"

    "これまで真央には余計な心配をかけないように、そして私たちの帰ってくる場所でいて欲しかったから、話さなかったのだ。"

    "ぐっと堪えて、私は拳を強く握っていた。"

    "話したところで、直未が良くなる見込みなど何もないのだ。"

    show rnk sci arm sad at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「直未を信じるしか――ない」"

    "気を抜けば泣いてしまいそうなほどに辛いけれど、これが今の精一杯だった。"







    python:
        set_info_time("night")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    show mhr sci nor ser rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「……今日はここまでにするよ」"

    "お見舞いの後、私は海晴とライオン館へ来ていた。"

    "だが特に得られる成果はなく、海晴は重い足取りでライオン館を後にした。"

    "話していたのは、女神の≪未練≫について。"

    "レテから聞いた話を元に色々と考えてみたが、カードが作られることはなかった。"

    "私は水曜日ということもあり、いよいよ焦りを感じ始めていた。"

    "何もできない無力さに、これまでうまくいってきたのは全て偶然だったのではないかと疑問に思ってしまう。"

    "きっと、このまま何もしなければ海晴はそのまま自分が脱落することを選ぶだろう。"

    "パルカはあの番号が任意で設定したものではないと言っていたけれど、これでは、私が最後の一人になるように、Ⅰ番に設定したのではと勘繰ってしまう。"

    "そうすれば、彼女の目的は達成されるのだから。"

    show rnk sci arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「そんなのっ……」"

    "それでも私は、拳を握りしめることしかできなかった。"

    $ add_seen_chapter("12_1-3")








    python:
        set_info_scene("190")
        set_info_date(7, 19, "thu")
        set_info_time("night")
        set_info_location("04")


    stop music fadeout 2
    scene bg lion01 night with fade_longest
    play music audio.gimon
    pause 1

    $ show_hud()

    show mhr sci nor ser rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「……今日はここまでにするよ」"

    "24時間経って、私は海晴からまったく同じセリフを聞くこととなった。"

    "直未は相変わらず目覚めず、私たちは女神の≪未練≫を手に入れることができていない。"

    "つまり、状況は何も変わってはいなかった。"

    "試験休みは今日で終わり。"

    "明日は学校で、テストの結果が返される。"

    "夏休みが間もなく始まるのに、私たちには先がない。"

    show rnk sci arm sad at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……駄目、なのかな。私たち、もう」"

    "焦りは、私を弱気にさせていた。"

    "希望が見えただけに、今日まで進展が何もないという落胆は大きかった。"


    stop music fadeout 1
    play se "slap"
    with quake_fast

    "下を向いた私の頬に、激しい熱が走る。同時に、ぴしゃりという破裂音が部屋の中に響いた。"

    show rnk sci arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……」"


    play music audio.resistance

    show mhr sci pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは、謝らないよ」"

    "簡単なことだ。"

    "海晴が私のほっぺたを、ビンタしたのだ。"

    "ひりひりと、熱を帯びた痛みを感じる。"

    show mhr sci pai ten rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火が諦めて、どうする？」"

    show mhr sci nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「レテの言う通り、凛火は自分の力でここまで来た。ぼくは生きていて、まだ生きることを諦めていない」"

    show mhr sci nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくにこれからも生き続けたいと思わせたのは、凛火だろう？」"

    show mhr sci pai ten rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火が折れちゃ――ぼくたちはみんな、駄目なんだ」"

    "頬を押さえる私を、海晴は震えた唇で見下ろしていた。"

    "海晴が本気で怒ったとき、泣きそうな顔をするんだと、思った。"

    "思えば海晴が私に対して本気で怒ったことは、これが初めてかもしれない。"

    show rnk sci nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「私は、何をすればいいと思う？」"

    show mhr sci pai ten rev with std_change

    voice get_voice_filename("mhr")
    miharu "「昨日、自分で言っていたよ。日辻さんを信じるしかない――と。君が折れないから、ぼくたちも彼女を信じられるんだ」"

    "私は頬から手を離して、しっかりと海晴を見据えた。"

    "じんじんとした痛みはまだ残っているが、そのことが、かえって私を冷静にさせた。"

    show rnk sci sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「直未を、信じる」"

    show rnk sci nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「そして私は、私のことを信じる。女神のカードを、必ず揃えられるって」"

    show mhr sci sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「――ああ」"

    "私の心は、一度折れた。"

    "それは、ユウくんに直未が殺されたとき。"

    "でも、今直未は生きている。きっと直未は、自分の中でせめぎ合う記憶と戦っている。"

    "なのに私が諦めようとしたら、駄目だ。"

    hide rnk
    hide mhr
    with std_out

    "私が背筋を伸ばして立ち上がると、海晴は急に我に返って、私の心配をしてくれた。"

    "すぐに頬を冷やさないと腫れが残るとか、口の中を噛んでないかとか、自分で叩いたのに少しおかしかった。"







    $ set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "一人で自分の部屋に戻ってきて、私は考え事をしていた。"

    "レテがああ言ったということは、必要な情報はもう揃っているはずなのだ。"

    "これから必要なのは、それらを繋げること。"

    "レテも、記憶をパズルのように表現していた。"

    show rnk paj nor apo at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「やっぱり関係あるよね」"

    "レテの話した女神の秘密と、直未の突然の入院。"

    "どちらも記憶という言葉が大きく関わっているという点で、無関係とは思えない。"

    "答えがあるか分からないことでも、今できるのは考えることだけ。"

    "私は入眠するまでずっと、そのことを考えていた。"

    "ちなみに海晴からは、私を心配するチャットが10件以上来ていた。"

    "それでも宣言通り謝らないあたりが、海晴らしい。"

    $ add_seen_chapter("12_1-4")









    python:
        set_info_scene("191")
        set_info_date(7, 20, "fri")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "目を覚ましても、新しい考えは浮かんでこなかった。"

    "今日は金曜日。12回目の選定まであと３日しかない。"

    "けれど、諦めるには早過ぎる。スケールさんのカードを生成したときは、もっと時間がなかったのだ。"

    "そういえば、日記帳のようなものがまだおばあちゃんの部屋にあるかもしれない。"

    "学校が終わったら、見てみていいかおばあちゃんに聞いてみよう。"

    "諦めなければ、ちゃんと次の手が浮かぶ。"

    "私はひとまず、学校へ行く準備を始めるのだった。"







    $ set_info_location("14")

    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    pause 1

    $ show_hud()

    "緊張状態で学校へ行った私は、全てを裏切られた気持ちになっていた。"

    "――ただしそれは、いい意味で。"

    play music audio.naomi

    show rnk sun sur su2 rev at std_cr, xoffset(-120) with std_in

    voice get_voice_filename("rnk")
    rinka "「……直未！」"

    show mao uni nor lau rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「なおりん！」"

    show mhr sun nor ser rev behind rnk at std_cl, xoffset(80) with std_in

    voice get_voice_filename("mhr")
    miharu "「……日辻さん」"

    "たまたま、登校時間の被った私たちは、そこで直未の姿を見かけることになる。"

    "いつ目覚めたのかという疑問やいきなり学校に来て大丈夫かという心配もあったが、それよりもまず嬉しかった。"

    "直未が、目を覚ましたのだから。"

    "しかし、私は再度全てを裏切られることとなる。"

    "今度は、いいのか悪いのかよく分からない意味で。"

    stop music fadeout 1

    show nom sun nor 9pc at std_r with std_in

    voice get_voice_filename("nom", 528)
    naomi "「ごきげんよう。先輩方」"

    "その一言で、私は凍ったように動かなくなっていた。"

    "恐らく、海晴も。"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「ごきげんよう～なおりん」"

    "恐らく真央だけが、直未の突然の変化に対応できていた。"

    show nom sun nor 9no with std_change

    voice get_voice_filename("nom")
    naomi "「ご心配おかけしましたわ。この通り、ワタクシはすっかり健康になりました」"

    show mao uni nor nor rev with std_change

    voice get_voice_filename("mao")
    mao "「そっかー、よかったぁ。本当に、すっごく心配したんだからねぇ」"

    show nom sun nor 9pc with std_change

    voice get_voice_filename("nom")
    naomi "「うふふふふ」"

    play music audio.gimon

    "直未は口元に手を当てて、お上品に笑った。"

    "その喋り方はこれまでの直未のものとは異なっていて、私が聞き覚えのあるものだった。"

    "――女神パルカ。"

    "私は彼女を連想して、一気に警戒心を高めた。"

    "私の肉体に入ろうとしていたんじゃなかったのだろうか。"

    "それに、そもそもまだ女神の選定には３日ある。"

    show nom sun nor 9la with std_change

    voice get_voice_filename("nom")
    naomi "「さあ、遅刻してしまいますわよ」"

    "数々の疑問を抱えたまま、私たちは校舎へと向かう。"







    $ set_info_location("08")

    scene bg schoolroom noon with fade_long
    pause 1

    $ show_hud()

    "直未とは一旦別れて、教室へ来ていた。"

    "真央は細かいことは気にせず直未の回復を喜んでいたが、私は手放しで喜ぶわけにはいかなかった。"

    "それは、海晴も同じ。"

    "もしかして、記憶の書き換えが行われ、真央はそもそも直未の口調に違和感を覚えていない……？"

    "その可能性が脳裏に浮かぶと、私は言いようもない緊張感が湧いてくる。"

    "もし直未に女神パルカが憑りつき、世界に記憶の改竄まで行われているとなれば、私は対抗ができない。"

    show mao uni sel glo rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「二日も眠ってたから、なおりん喋り方忘れちゃったのかなぁ。でもよかったぁ、元気になって」"

    show rnk sun nor smi at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「そうだね。顔色もよかったし」"

    show mhr sun sco cau at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「いつ回復したにしても、もう少し休んでいなくてよかったのかな」"

    "今の真央の言葉で、真央がただ直未の回復を喜んでいるから口調を気にしていないだけ、ということが分かった。"

    "だが、女神が憑りついたかもしれないという懸念は残ったままだ。"

    "放課後に会う約束をしているから、またしばらく様子見をするべきだろう。"







    $ set_info_time("noon")


    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.comicaldays
    pause 1

    $ show_hud()

    "久々の登校といっても、今日はテストの返却くらいしかやることがない。"

    "私にしては珍しく頑張った期末試験でもあるので、きちんと結果は確認することにする。"

    show mao uni nor no1 rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「さあ、りーたん。期末試験はどうだったぁ？」"

    "真央が早速、私のところまで結果を聞きに来た。"

    "私は自信満々に、成績表を真央に見せる。"

    show rnk sun nor smi at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「今回はちゃんと勉強したから、一教科も60点以下にはならなかったよ」"

    show mao uni nor dis rev with std_change

    voice get_voice_filename("mao")
    mao "「うわぁ……レベル……」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「さすがに今回は勉強量で圧倒的に負けてるから、うちが負けちゃうと思ったけど、そんなことはなかったねぇ」"

    "真央はそう言うと、自分の成績表を見せつけてきた。"

    "全教科70点を超えている。"

    "真央くらいの点数だと、学年の順位は半分以上だ。"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「日々の積み重ねって大事だねぇ」"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「ははは」"

    "私が苦笑いしかできずにいると、海晴も私の席まで来た。"

    show mhr sun sco con at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「仕方がないよ。今回は少し難しかった。ぼくも中々勉強に集中できず、学年１位を逃してしまったくらいだ」"

    "そんな海晴の成績は、もう眩しくて点数がよく見えなかった。"

    "１位を逃したという言葉通り、学年の順位は２位だった。"

    "奨学金の枠は３枠だったと思うから、成績の面では相変わらず問題がない。"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ま、中間の時の悲惨な点数に比べれば、今回はだーいぶ上がったよねぇ」"

    show mao uni nor dis rev with std_change

    voice get_voice_filename("mao")
    mao "「そろそろ受験のこととかも考えないといけないしぃ、はぁ、ユーウツだよぅ」"

    "うちの学校は一応進学校なので、ほとんどの生徒は高校に入学した時点で大学受験の勉強を始めている。"

    "そういえば直未も、夏休みは塾に行き始めると言っていた気がする。"

    "海晴は別として、真央と私はその意味でも異端組だ。"

    show mhr sun sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「大丈夫さ。進学校なだけあって、飴茶の定期試験はレベルが高い。まずは学校の勉強をちゃんとやっていれば、受験勉強の礎になるよ」"

    show mhr sun sco wic with std_change

    voice get_voice_filename("mhr")
    miharu "「学校のテストすらロクにできない人が塾に行ったところで、上辺の勉強法だけ学んでできるようになった気持ちになるだけさ」"

    "海晴なりに私たちを励まそうとしてくれているのは分かるのだが、海晴が言うと説得力があり過ぎて、もはや凶器のように思える。"

    "少なくとも直未に聞かせられないな、と思っていた。"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「というわけで真央様は、この夏休みもちゃぁんと遊びます」"

    "海晴の話を聞いていたのか聞いていないのか分からないが、真央はそう宣言をした。"

    show mhr sun nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「８月に花火大会があっただろう？　この日はみんな空けておいて欲しいかな」"

    show rnk sun nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「もちろん」"

    "それは、みんなで遊園地に行った夜に海晴と話した大切な約束。"

    "私は即答で返事をした。"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「よーし、じゃあこれからりーたんの家で作戦会議しようねぇ」"

    show rnk sun nor smi with std_change_wait

    "私は真央のその提案に、頷いた。"






    python:
        set_info_scene("192")
        set_info_time("noon")
        set_info_location("02")


    stop music fadeout 1
    scene bg station01 with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "ほとんど午前授業のようなものだったので、私たちは食堂でご飯を食べてからライオン館へ向かっているところだった。"

    "直未は相変わらず、あの口調だ。"

    show nom sun nor 9pc at std_c with std_in

    voice get_voice_filename("nom")
    naomi "「らあめんというのも、とても庶民的で美味しかったですわ」"

    "と、もう何が何だか分からない。"

    "直未の姿をしているのに喋り方は女神パルカだし、やけに俗物的なことを言っているしで、より混乱するばかり。"

    "真央のように気にしないスタンスでいる方がいい気もするが、そうもいかない。"

    show mao uni nor ch1 rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「なおりん、そういえばいつ目を覚ましたの？」"

    show nom sun nor 9se with std_change

    voice get_voice_filename("nom")
    naomi "「昨晩ですわ。本当に、ご心配をおかけいたしました」"

    show nom sun nor 9no with std_change

    voice get_voice_filename("nom")
    naomi "「お医者サマもお母サマもとても驚いていらっしゃいました。けれど、心拍数や血圧などは全て正常値でございました」"

    show nom sun nor 9pc with std_change

    voice get_voice_filename("nom")
    naomi "「本日が１学期の最終日ということで、皆サマの反対を押し切って登校いたしました」"

    show nom sun nor 9se with std_change

    voice get_voice_filename("nom")
    naomi "「健康そのものですから、ご心配には及びません」"

    show mhr sun sco thi at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「……なら、いいのだけど」"

    "海晴は、明らかに警戒心を強めていた。"

    "そんな会話をしながら、私たちはライオン館へ向かった。"







    python:
        set_info_time("evening")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 evening with fade_long
    pause 1

    $ show_hud()

    show mao uni nor nor rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「んじゃ、うちは用事があるからここで～」"

    hide mao with std_out

    "そう言って、真央はライオン館を去っていった。"

    "夏休みの話をするといって、実態はお菓子を食べながらの雑談で、予定はほとんど決まらなかった。"

    "もっとも、真央がそのうち何か提案するだろう。"

    "遊びの予定を真央任せにすることに、抵抗はない。"

    "目下、問題は私の目の前に座る少女にあった。"


    play music audio.gimon

    show rnk sun nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……そろそろ、説明してもらえる？」"

    "直未の顔をした誰かに向かって、私はそう訊ねていた。"

    show nom sun nor 9la rev at std_l with std_in

    voice get_voice_filename("nom")
    naomi "「ワタクシは日辻直未。花も恥じらう高校１年生。趣味は読書。少し人見知りもしますけれど、真面目で優しい性格でございます」"

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「――そう言っても、お二人サマには信じていただけないのでしょうね」"

    "その誰かはくすり、と妖しく笑う。"

    "私と海晴がさらに警戒心を強めると、彼女はそのまま続けた。"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「なーんて、からかうのはやめにしましょう。ワタクシはお二人の敵ではありません」"

    show nom sun nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「ワタクシはダイアナ・ハリソン。今は日辻直未サマの体をお借りしています」"

    show mhr sun sco thi at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「ダイアナ……。パルカではないのかい？」"

    "海晴の質問は、私も思ったものだった。"

    "ダイアナ・ハリソンはすでに死亡し、女神パルカに変わったはずではなかっただろうか。"

    "そこで私は、レテの話を思い出した。"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ダイアナさんの記憶を奪ったって、レテは言っていた。まさか、貴女は……」"

    show nom sun nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「さすが、先輩サマですわ」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「ワタクシはダイアナがパルカになり、レオがレテになった直後、彼女から奪われた人間としての記憶そのもの」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「直未サマの心と体を媒介に、一時的に人格として形成されているだけでございます」"

    show mhr sun sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「つまり、君は≪夢の世界≫に存在している女神とは別の存在だということかい？」"

    show nom sun nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「ええ。そしてワタクシはいわゆる魂でも霊でもございません。だから憑依された、とは思わないでくださいませ」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「あくまで直未サマの人格が、ワタクシの記憶をフィルターにして表出することで、ダイアナのようなものになっているだけでございます」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……細かいことは分からない。ただ、まず一つ聞かせて。直未は、無事なの？」"

    "私は直未の、いや、ダイアナの瞳を見てそう訊ねる。"

    "彼女の正体はこの際、いい。"

    "まずは、直未の安否が最重要だ。"


    play music audio.disclose

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「正直に申し上げましょう。目覚めるまでのワタクシは、非常に危険な状態でした」"

    show rnk sun arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたっ……！」"

    show nom sun nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「ですが、この状態になった以上、直未サマはもう大丈夫です」"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「彼が、レテが何かしたのかい？」"

    "ダイアナは、こくりと深く頷いた。"

    "しかし寂しそうな表情を浮かべて、続ける。"

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「しかしあの方の名誉のために、順序立ててお話をいたしましょう」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「ワタクシはおうちで、凛火先輩サマからお借りした日記帳を読みました」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「それはすなわち、上書きされているはずの≪女神の選定≫の記憶を掘り起こすに等しい行為」"

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「直未サマの脳内で起こった記憶の奔流がぶつかり合うことによる負担で、直未サマは意識を失ってしまいました」"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「これは直未サマの記憶に眠る知識ですが……コンピュータのメモリーに過剰なデータを書き込むと、破損してしまいますでしょう？」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「それと同じことが、起きようとしていたのでございます」"

    show rnk sun arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「脳が……壊れちゃうってこと……？」"

    "ダイアナは「ええ」と頷くと、続ける。"

    show nom sun nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「忘却の川であるレオ――いえ、レテサマならば二つの方法で救うことができました」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「一つは、≪女神の選定≫に関する記憶を完全に忘却させてしまうこと」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「もう一つは、貴女サマ方がパルカを脱落させるまでの間、レテサマの力の一部を分け与えること」"

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「パルカを脱落させれば、その時点で運命は固定されます」"

    show nom sun nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「その際に直未サマにある新しい記憶――改変された世界の記憶を消してしまえば、貴女サマ方と過ごした記憶を失わず、二つの記憶に苦しむこともなくなるでしょう」"

    show mhr sun sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「レテは、どうして日辻さんを救おうとしてくれたんだい？」"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「ああ見えて恥ずかしがり屋なレオのためにも、それは秘密にしておきましょう」"

    "私は、海晴の質問の答えが分かっていた。"

    "レテは私たちの幸せを願ってくれていたのだ。きっとそれ以外に、理由はない。"

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「この質問は、直未サマにとって≪女神の選定≫の記憶を失うかどうかという問いでもありました」"

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「直未サマは、≪女神の選定≫の記憶を残す方を即答で選びました。ただし、レオも無条件で力を貸すわけにはいきません」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「ただの人間に一時的とはいえ自分の力を貸し与えるというのは、レオにとってルール違反の行為でしょう」"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「そこで、ルール違反を許容するために制限とリスクを与えたのです。ワタクシ――忘却の川の力は、ダイアナの記憶とともに与えると」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「制限というのは、力がある間は直未サマの人格はワタクシを通さなくてはいけないこと、リスクはワタクシの記憶が入ってくる負担に耐えきること」"

    show rnk sun sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「記憶でパンクしそうな状態に、さらに新しい記憶を？　それって、もっとひどいことになるんじゃないの？」"

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「ええ。最悪、命を落とす危険がありましたわ。もちろん、レオは直未サマにそのことを説明いたしました」"

    show nom sun nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「それでも、直未サマはこれまでのことを忘れる方を選びませんでした。貴女サマ方と≪女神の選定≫を過ごした記憶を、失いたくないと決意したのです」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「耐えられるかどうか、レオにも分からなかったでしょう。けれど直未サマが貴女サマ方を信じたように、直未サマのことを信じたのでしょう」"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「そして日辻さんは君の記憶も受け入れた上で、その負担に耐えきった」"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「さようでございます」"

    "そのことは、直未が起きていることからも明らかだ。"

    "問題は、直未の人格がちゃんと戻ってくるかということだ。私は、ダイアナにそのことを訊ねた。"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「その点は心配いりません。ワタクシはパルカと同質の存在。パルカが消えれば、ワタクシも消えます」"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「ワタクシの記憶、つまりワタクシが直未サマから消えれば、直未サマは元通り」"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「先ほどお話しした通り、ワタクシの記憶が消えるときには改変された世界の記憶も一緒に忘却してもらいます」"

    show nom sun nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「そうすれば、記憶の矛盾に苦しめられることもなくなります」"

    show mhr sun sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「仮にぼくたちがパルカに敗北し、パルカが凛火として受肉した場合はどうなるんだい？」"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「あら、そんなことあり得るんですか？　ワタクシ、もはやお二人とも理想の未来しか見ていないと思っていましたけれど」"

    show mhr sun sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。言ってくれるね、日辻さん。その通りだ。ねえ、凛火？」"

    show rnk sun arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そうだね。私たちは、負けない」"

    show nom sun nor 9la rev with std_change

    voice get_voice_filename("nom")
    naomi "「ええ、その意気です。世界は認知によって成り立っています。先輩サマ方が理想の未来を思い描けば描くほど、それはより強固な運命に変わりますもの」"

    show nom sun nor 9qu rev with std_change

    voice get_voice_filename("nom")
    naomi "「さて、そしてワタクシの記憶を直未サマに授けたレオの真意を、貴女サマはもうお気づきでしょう？」"

    "海晴も私も、同時に頷いていた。"

    "ここまで来れば、気づかないことはない。"

    "女神を指名するにあたり、必要な最後のピース。"

    "それは、ダイアナの≪未練≫だ。"

    "本人が話しに来たということは、それは――。"

    show nom sun nor 9la rev with std_change

    voice get_voice_filename("nom")
    naomi "「現代の日本を、楽しませてくださいな」"

    show rnk sun arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「――え？」"

    show nom sun nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「そうすれば日曜日の夜、お二人にワタクシの≪未練≫をお教えしましょう」"

    show mhr sun sco con with std_change

    voice get_voice_filename("mhr")
    miharu "「……それ、パルカのやろうとしていることとほとんど同じではないのかい？」"

    show nom sun nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「あら？　だって元は同じ人間ですもの。ワタクシはお転婆お嬢様のダイアナ。日記を読んだ凛火先輩サマなら、ご存知でしたでしょう？」"

    "直未は立ち上がると、女神のようにスカートのすそを持ってお辞儀をした。"







    python:
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "部屋に戻って、私は安堵のため息をついていた。"

    "何はともあれ、直未は無事だった。"

    "そしてそれは、女神の≪未練≫にも繋がる道。"

    "直未は、自ら危険な方法を選んだと言っていた。"

    "でも、納得できる。"

    "直未はずっと、私たちと過ごした記憶が消えることを嫌がっていた。"

    show rnk paj arm lie at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「まさか……ね」"

    "レテは直未の記憶の改竄も行ったはずだ。"

    "だが完璧に行わなかったのは、直未の意志を尊重していたからなのかもしれない。"

    "だとすれば責任を負ったってことで、レテは恩義に厚いというべきか。"

    "お礼を言いたいのはこっちだと言うのに。"

    "その時、部屋のドアにこつんと何かが当たる音が聞こえた。"

    "きっと、レテだろう。ドアは半開きにしているから、そのうち自分でドアを押して入ってくるはずだ。"

    "そう思っていたが、一向に入ってこない。"

    show rnk paj sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「……レテ？」"

    "不審に思って、私は扉を開けてみた。"

    "そこには、レテがぐったりと倒れていた。"


    play music audio.impatience


    voice get_voice_filename("rnk")
    rinka "「レテ！」"

    scene ecg falllete fall with dissolve_long

    "焦った私は、レテを優しく抱きかかえて座布団の上まで運ぶ。"

    "水の入った皿を持ってきて、レテのそばに置いた。"


    voice get_voice_filename("cat", 24)
    lete "「にゃー……」"

    "レテからは、弱り切ったかすかな声だけが聞こえる。"

    "見るからに、衰弱していた。"


    scene bg myroom night
    show rnk paj arm nor at std_c
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「病院に行く？」"

    "私がそう訊くと、レテは僅かに首を横に振った。"

    "私の言葉は分かっているはずから、これはレテの否定の合図だろう。"

    "ということは病気――ではないはずだ。"

    "私はさっき、直未の姿を借りたダイアナから話を聞いていた。"

    "レテは自分の力の一部を直未に授けたと。"

    "レテは神様のような力で、ずっと長生きをしていると聞いていた。"

    "その力が減れば、このように憔悴してしまうということなのだろうか。"

    show rnk paj nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「レテも……必死だったんだね。ありがとう」"

    "私はそう呟いて、ベッドに寝転がる。"

    "私は色んなことを託されているのだと――あらためて、実感した。"

    $ add_seen_chapter("12_1-5")








    python:
        set_info_scene("193")
        set_info_date(7, 21, "sat")
        set_info_time("morning")
        set_info_location("02")


    stop music fadeout 2
    scene bg station01 with fade_longest
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "土曜日の朝。"

    "私はこの土日に急遽お店をお休みにすることにした。"

    "直未の体を借りているダイアナに、東京を案内するためだ。"

    "レテはクッションに寝かせて、近くに十分な量の水とご飯を置いておいた。"

    "心配だが、レテの態度を見るに、ダイアナを案内することを優先して欲しいらしかった。"

    "世間知らずな誰かを案内する――思い出すと、こんな展開は前にもあった。"

    show mhr sci sco con at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「しかし、ソフィアの時は彼女に目的があったけれど、今回はどこにしようか。日辻さ……ダイアナ、どこか行きたいところはあるかい？」"

    show nom sci nor 9no rev at std_l with std_in

    voice get_voice_filename("nom")
    naomi "「地下鉄というものに乗ってみたいですわ」"

    show rnk sci nor que at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「……地下鉄って、あの？」"

    show mhr sci sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そうか。東京に地下鉄ができたのは、現在の銀座線の一部にあたる浅草・上野間が開通した1927年だったね」"

    "日記帳から計算すると、ダイアナさんが命を落としたのは1910年頃。"

    "私たちにとって当たり前の地下鉄も、ダイアナさんにはアトラクションのようなものかもしれない。"

    "そういえば駅で合流してからも、自動改札や自動販売機、電車の本数の多さや駅ビルなど、目につくものほとんどに驚いていた。"

    "それでも抵抗なく切符を買ったり街を歩いたりできるのは、直未の体だからなのだろう。"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「地下鉄に乗るなら、浅草の方でも見る？　スカイツリーとか、当時なかったものもあるし」"

    show mhr sci nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そうなると、東京タワーも1958年に完成したものだ。どちらも展望台があるし、現代の東京を俯瞰して一望するには最適かもしれない」"

    show rnk sci arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「東京タワーか……でも、海晴の言う通りだね」"

    "東京タワーにはいい思い出があまりないが、あれももう一月ほど前のこと。"

    "そもそもこの世界ではユウくんによるテロ未遂はなかったことになっているし、気にし過ぎかもしれない。"

    show nom sci nor 9la rev with std_change

    voice get_voice_filename("nom")
    naomi "「ありがとうございます。お二人サマにお任せいたします」"

    show nom sci nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「実はワタクシ、こうして踏むはずのなかった地面を歩いているだけでも、とても楽しいのでございます」"

    "ダイアナは屈託のない笑顔でにっこりと笑った。"

    "その表情は、やはりどこかパルカに似ていた。きっと彼女から毒気がなくなれば、こうやって純粋に笑うのだろう。"







    python:
        set_info_time("noon")
        set_info_location("38")


    stop music fadeout 1
    scene bg tokyotower02 with fade_long
    play music audio.memories
    pause 1

    $ show_hud()

    "私たちは人の多い浅草方面から、こちらも人の多い東京タワーへと移動してきていた。"

    "回ったのは、スカイツリーと浅草寺だった。"

    "途中の商店街でメロンパンも食べた。"

    show nom sci nor 9no rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「ワタクシがもっと小さい頃に、凱旋門が建てられていたことを思い出しましたわ」"

    "雷門は平安時代に作られたものだったと記憶していたので、ダイアナの発言には最初疑問符が浮かんでいた。"

    "移動中に調べてみると、雷門は1865年に火事でなくなったあと、ずっと仮設の門が建てられていたらしい。"

    "海晴もこの事実は知らず、日露戦争の時は浅草寺の凱旋門が建てられていたということを聞き、さらに驚いていた。"

    "直未はこのことを覚えているのか分からないが、戻ってきたら教えてあげようと思っていた。"

    show nom sci nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「スカイツリーに比べると、低く感じますわね」"

    "東京タワーの展望台から街を見下ろして、ダイアナはぽつりとそう言った。"

    "確かに、回る順番を間違えたかもしれないと思いつつ、展望台の安くない料金を払っているから、複雑な気持ちになった。"

    show mhr sci nor ser at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「けれど、君の知識にもあるはずだろう。第二次世界大戦の時、この東京は焼け野原だった」"

    show mhr sci nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくも資料写真でしか知らないけれど……きっと焼け野原から立ち上がった真っ赤な塔は、単なるラジオ塔以上の価値があったと思う」"

    show nom sci nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「戦争……そうですわね。ワタクシは過去の選定の詳細を知りませんが、もしかしたら、その時期に選定は多く行われていたのかもしれません」"

    show nom sci nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「選定で生き残ることができても――長くはなかった」"

    show nom sci nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「兵士として同じ戦地に居合わせるだけでも、因果は発生いたしますから……」"

    "そう言うと、ダイアナは窓の外を見る目を細めた。"

    "私たちの参加している選定は、12回目。"

    "ダイアナの死から百年程度しか経っていないのに12回というのは、あらためて考えれば多い。10年に一度以上行われている計算になる。"

    "彼女の語る可能性を考慮すれば、辻褄が合うのかもしれないと思っていた。とてもやるせない、辻褄の合い方だけれど。"

    show nom sci nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「決して見慣れてはいけないのかもしれませんね。この穏やかな風景は、無数の人々の努力が作り出しているのですから」"

    "街は自然に生まれるわけではない。"

    "ダイアナは、優しい声でそう語るのだった。"








    python:
        set_info_time("evening")
        set_info_location("17")


    stop music fadeout 1
    scene bg shinjukugyoen noon with fade_long
    play music audio.thebonds
    pause 1

    $ show_hud()

    "最後に回る場所として、私たちは新宿御苑まで移動してきた。"

    show nom sci nor 9no rev at std_c with std_in

    voice get_voice_filename("nom")
    naomi "「≪運命の終着点≫ですわね」"

    show rnk sci nor smi at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「私にとっては、ハジマリの場所でもあるんだけどね」"

    show mhr sci nor ser rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「――ぼくにとっても」"

    show nom sci nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「その記憶は、直未サマの記憶にはございませんね。なので、ワタクシは聞かなかったことにしておきましょう」"

    "私が首を傾げると、ダイアナは小さくため息をついた。"

    show mhr sci nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ここの開園は、1906年だったね。ということは、君も来たことがあるのかい？」"

    show nom sci nor 9cl with std_change

    voice get_voice_filename("nom")
    naomi "「いいえ。この場はワタクシのような一般市民が気軽に来られる場所ではございませんでしたもの」"

    show nom sci nor 9la with std_change

    voice get_voice_filename("nom")
    naomi "「ですから実は、この中に入ることができて感動していますわ」"

    show nom sci nor 9no with std_change

    voice get_voice_filename("nom")
    naomi "「日本庭園とイギリス庭園、フランス庭園。趣の違った景色は、できることならば季節ごとに楽しみたかったですわね」"

    "ダイアナはそう言うと、風を浴びて髪を揺らした。"

    "そして腰のあたりには髪がないことに気がついて、耳の後ろに手を移動させた。"

    show nom sci nor 9pc with std_change

    voice get_voice_filename("nom")
    naomi "「いけませんね。ワタクシは本来この時代に存在してはいけない異物。一瞬、自分の体のように思ってしまいました」"

    "私は少し考えてから、ダイアナに答えた。"

    show rnk sci arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「今ダイアナが存在していることは、運命じゃないのかな」"

    "私の言葉に、二人とも何も答えはしなかった。"

    "無理もない。"

    "そんなこと、きっと誰にも分からない。"

    "もしかしたら、レテやパルカにも分からないかもしれない。"

    "その後、私たちは閉園時間までまったりとお散歩していた。"







    python:
        set_info_time("night")
        set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "部屋に戻ってみると、結構歩いたことを実感する。"

    "中々にハードな東京観光だ。"

    "ソーニャの時もそうだったけれど、ほとんど同じルートだったとはいえ、人も多いし慣れはなかった。"

    "明日は海晴がバイトだったので、案の定と言うべきか、メイド喫茶へ行くことになった。"

    "直未とは行ったことがあるが、ダイアナはない。"

    "現代日本に生まれた珍妙な文化に興味があるらしい。"

    "私としては、できるだけ避けたかったのだが、ダイアナが行きたいというのであれば仕方がない。"

    "目覚ましをかけて、今日は寝ることに決めた。"

    "レテは今夜も、元気がなさそうだった。"

    $ add_seen_chapter("12_1-6")








    python:
        set_info_scene("194")
        set_info_date(7, 22, "sun")
        set_info_time("noon")
        set_info_location("09")


    stop music fadeout 2
    scene bg maidcafe with fade_longest
    play music audio.maidcafe
    pause 1

    $ show_hud()

    "ダイアナとは秋葉原の駅で合流して、メイド喫茶へは一緒に歩いた。"

    "百年前の人なのに、ちゃんと駅まで来られるのはすごい。"

    "ここまで来るのも、道が人で一杯で大変だった。"

    "かつては歩行者天国になっていたらしいが、ある悲惨な事件以来、中止になってしまったのだ。"

    "すれ違う人々にも、それぞれの人生がある。"

    "気を抜けば忘れそうな事実を、道中、ダイアナはあらためて語っていた。"

    show mhr mai sco smi rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「お帰りなさいませ、お嬢様。いいかい、凛火？　君はもう、頼んではいけないメニューを分かっているね？」"

    show nom sci nor ser at std_c with std_in

    voice get_voice_filename("nom")
    naomi "「頼んではいけないメニューでございますか？」"

    show rnk sci arm ama at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「いや、ホントに気にしないで……。うん。周りの店員さんを見て、その辺りは満足して」"

    show nom sci nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「はぁ……、分かりましたけれど」"

    hide mhr with std_out

    "ソーニャと来たとき、私はしっかり反省した。"

    "あの気まずさは、もう味わいたくなかった。"

    "いや、海晴は可愛いんだけど、その後どうもいたたまれなくなるのだ。"

    "というわけで、無難にコーヒーと、ダイアナはココアを頼んだ。"

    "メイド喫茶といえば、メイドさん。メイドさんといえば、イギリス。"

    "ふと疑問に思ったことをダイアナに訊ねてみた。"

    show rnk sci nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「ダイアナの家には、メイドさんはいたの？」"

    show nom sci nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「ええ。お父サマは当時にしては裕福でしたし、ワタクシのおうちはいわゆる洋館でございました」"

    show nom sci nor 9cl rev with std_change

    voice get_voice_filename("nom")
    naomi "「日本へ一緒に来た方もいれば、日本でお雇いした方もいらっしゃいました」"

    show nom sci nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「ですが海晴サマほど、派手な服装ではありませんでしたわ」"

    show nom sci nor 9se rev with std_change

    voice get_voice_filename("nom")
    naomi "「何名かは――ワタクシの死の直前に亡くなってしまいましたけれど」"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……そっか」"

    "私は、ダイアナの言葉に静かに頷いた。"

    "謝ることではないと思ったので、私は代わりに話題を変えることにした。"

    show rnk sci nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「そういえば……ダイアナは喋り方が直未とずいぶん違うけど、おうちの人は大丈夫だったの？」"

    show nom sci nor 9la rev with std_change

    voice get_voice_filename("nom")
    naomi "「ええ。おうちでは直未サマの真似をしていますもの」"

    "意外な言葉に私はきょとん、とした顔を浮かべていたのだろう。"

    "ダイアナは悪戯っぽく笑ってから、続けた。"

    show nom sci nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「けれど、口調を真似するのは疲れてしまいますわ。ですから、今は自然体でいさせてください」"

    show rnk sci arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「まあ、別にいいけど」"

    "私も、そっちの方がいい。"

    "性格が違うのに口調が似ていたら、違和感がすごいだろう。"

    "ただでさえ今も、直未がダイアナで喋っているのに少し違和感があるのだから。"

    show mhr mai sco smi rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「お待たせいたしました」"

    "接客モードでコーヒーとココアを持ってきた海晴にお礼を言って、私たちは海晴のシフトが終わるのを待つことにした。"







    python:
        set_info_time("night")
        set_info_location("02")

    stop music fadeout 1
    scene bg station01 night with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    show nom sci nor 9la rev at std_l with std_in

    voice get_voice_filename("nom")
    naomi "「ふぅ。とっても満喫しましたわ」"

    "駅のホームで、ダイアナは幸せそうなため息をついた。"

    "海晴のバイトが終わったあと、私たちは上野の動物園と国立博物館を見た。"

    "午後からという急なスケジュールだったので、実際はかなりの早足だった。"

    "しかし、ダイアナはそれでも満足してくれたらしい。"

    "そして同時に――きっとこれが、ダイアナが見る最後の風景になるのだろう。"

    show mhr sci sco cau at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「もう、いいのかい？　頑張れば、もう一か所くらいは見ることができる」"

    show nom sci nor 9pc rev with std_change

    voice get_voice_filename("nom")
    naomi "「いいえ。これくらいが丁度いいのですわ。運命に逆行するこの身が味わう幸せは、これで十分」"

    show nom sci nor 9no rev with std_change

    voice get_voice_filename("nom")
    naomi "「それより、直未サマを色々なところへ連れて行ってあげてください。そうですね。我儘を控えているワタクシの、最後の我儘です」"

    show rnk sci arm nor at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「……分かった。なら、そろそろ行こうか。今夜は、ライオン館へ」"

    "そして私たちは無言のまま、電車が来るのを待った。"







    python:
        set_info_scene("195")
        set_info_time("night")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    "そして私たちは、日曜日の夜を迎えた。"

    "ついに明日が最後の≪女神の選定≫。"

    "海晴、ダイアナの記憶が表に出ている直未、私。"

    "３人で、いつものテーブルを囲んでいた。"


    play music audio.nichijo01

    scene ecg nighttalkU1 nor with dissolve_long

    voice get_voice_filename("nom")
    naomi "「とても、とても楽しい時間を過ごすことができました。まずは、お礼を申し上げましょう」"

    scene ecg nighttalkR1 smi smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「……うん。直未もきっと、あなたが楽しんでくれたなら嬉しく思っているはず」"


    voice get_voice_filename("mhr")
    miharu "「パルカとは別のダイアナだと言っていたにもかかわらず、ぼくたちが夢の世界で出会った君そのものだったよ」"

    scene ecg nighttalkU1 smi with dissolve


    voice get_voice_filename("nom")
    naomi "「あら、そうでしたかしら？」"

    "直未はくすりと笑うと、口元に手を当てて微笑んだ。"


    voice get_voice_filename("nom")
    naomi "「それでは、最後のピースをはめましょう」"

    scene ecg nighttalkR1 ser nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「……ちょっと待って」"

    "私は、頼りない足取りで近付いてくる一匹の猫の姿を見つけた。"

    scene bg lion01 night
    show lete normal at cat_r
    with dissolve

    "そろそろだと察知して、私の部屋から降りてきたのだろう。この数日ですっかり痩せたレテを抱きかかえて、私はテーブルの下に座らせた。"

    "レテの定位置と言えば、やっぱりここだ。"


    show nom sci nor 9se rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「この子も、お話が聞きたかったのですわね」"

    "ダイアナはしゃがんで、レテの毛並みを優しく撫でた。"

    "その穏やかな表情は、直未がしたことのない顔だ。"

    "きっとダイアナが生きている間、こんな風にレオのことを撫でてあげたのだろう。"

    scene ecg nighttalkU1 nor with dissolve_long


    voice get_voice_filename("nom")
    naomi "「それではお話ししましょう。ワタクシの≪未練≫について」"

    "こうして、私の運命は一つの決着に向かっていく――。"







    $ set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.thebonds
    pause 1

    "間もなく、深夜０時を迎える。"

    "この日、海晴と直未はうちに泊まることに決めていた。"

    "レテももちろん、連れてきている。"

    "明日の朝、ちゃんとみんなの顔を見られるように。"

    show nom sci nor 9se at std_c with std_in

    voice get_voice_filename("nom")
    naomi "「ここに、直未サマが出て来られないのが残念ですわねぇ」"

    show rnk sci arm sad rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「代わりに、明日の朝ここにいるのはあなたじゃないんでしょ？」"

    show nom sci nor 9pc with std_change

    voice get_voice_filename("nom")
    naomi "「ええ」"

    show nom sci nor 9se with std_change

    voice get_voice_filename("nom")
    naomi "「ワタクシはすでに運命の幕を閉じた身。未練はあっても、もはや執着はありません」"

    show nom sci nor 9no with std_change

    voice get_voice_filename("nom")
    naomi "「しかし、ワタクシのお姉サマの子孫を見ることができて安心いたしました」"

    show nom sci nor 9no with std_change

    voice get_voice_filename("nom")
    naomi "「ワタクシの最初の≪器≫になってしまったお姉サマも、きっと幸せな人生を過ごされたことでしょうから」"

    show rnk sci arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……きっと」"

    "ダイアナは、また穏やかな顔で微笑んだ。"

    "一緒にいる時間は短いけれど、直未の顔をしているせいか、私は彼女のことをすっかり好きになってしまっていた。"

    "お別れは寂しいけれど、私は彼女のことを忘れない。"

    show mhr sci nor nor at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「≪女神の選定≫が始まったときは、まさかこんな夜が来るとは思ってもみなかった」"

    show mhr sci pai ten with std_change

    voice get_voice_filename("mhr")
    miharu "「自分が生き残ることだけを考えていて――≪運命の大広間≫で君と出会ったときには、凛火が生き残ることだけを考えていた」"

    show mhr sci pai lie with std_change

    voice get_voice_filename("mhr")
    miharu "「白状すると、ぼくは君から告白の返事を聞けたならば、凛火に指名されようと思っていた」"

    show rnk sci nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……分かってるよ」"

    show mhr sci sco con with std_change

    voice get_voice_filename("mhr")
    miharu "「けれど、今は違う。もちろん、凛火から告白の返事を聞くためだけではない」"

    show mhr sci nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「ただ生きたいと願うことが、こんなに尊いことと知ったから」"

    "海晴はその時、とても眩しく見えた。"

    "私は海晴の綺麗な微笑みを見て、しっかりと頷いた。"

    show rnk sci nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私もこの選定で、色んな想いを知った。託された」"

    show rnk sci nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「これまでの人生でそれは、考えられないことだった。私の世界はちっぽけで、ライオン館と学校。海晴と真央と直未とおばあちゃん。それだけで成り立ってた」"

    show rnk sci nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、今は違う。世界は広いってことをちょっとだけ、知ることができた」"

    show rnk sci arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そして何より、私は獅子舞凛火だって知ることができた」"

    "自分なんて、不安定な存在なのだ。"

    "誰かと一緒にいなくては姿が見えなくなってしまうような、そんな存在。"

    "でも、それでも。"

    "私は生きたいと思った。"

    "一人じゃないから、生きたいと思った。"

    "誰かと一緒に過ごす奇跡のような日常に、生き続けたいと思った。"

    scene ecg falllete fall with dissolve_long


    voice get_voice_filename("cat")
    lete "「にゃぁ……」"

    "レテはか細い声で鳴く。"

    "辛いならよせばいいのに、前脚を天井に向かって伸ばしている。"


    scene bg myroom night
    show rnk sci nor smi rev at std_l
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「ありがと」"

    show nom sci nor 9no at std_c with std_in

    voice get_voice_filename("nom")
    naomi "「応援してくださっているのですね」"

    show rnk sci arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私たちも、何かしよう」"

    show mhr sci nor nor at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「では、手を繋ごう」"

    "海晴はそう言って、私の手を握った。"

    "私は直未の手を握って、直未は海晴の手を握った。"

    show nom sci nor 9pc with std_change

    voice get_voice_filename("nom")
    naomi "「ワタクシは体が一つですけれど二人分でございます」"

    show mhr sci sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「ああ、そうだね」"

    scene black with eyeshutter_close

    "３人で輪になって、目をつぶる。"



    voice get_voice_filename("rnk")
    rinka "「じゃあ、また明日――」"

    "誓いの言葉も、派手な言葉もない。"

    "私たちにあるのは、信頼だけ。"

    "手を繋いだまま、私はまどろみの中へと落ちていった。"

    $ add_seen_chapter("12_1-7")

label sentei12:

    call set_replay








    python:
        set_info_date(7, 22, "sun")
        set_info_scene("196")
        set_info_time("lnight")
        set_info_location("07")


    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall
    pause 1

    "運命の大広間。"

    "眼前に広がっているのは、すっかり見慣れてしまった光景。"

    "これまでに12回も来ている、その場所だった。"

    "どこまでも広がる闇の中に、いくつもの歯車が浮いている。上を見ると、わずかな光が暗闇の隙間から降り注いでいる。"

    "私が立っているのは、闇に浮いた直径３メートル程の円い床の上。裁判所の証言台のような手すりがついている。"

    "狭い円い床は、円になって12個並んでいる。まるで、時計の文字盤のような配置だ。"

    "12個の床の中心には、巨大な時計の針が空気を震わせながらゆっくりゆっくり時を刻んでいた。"

    "それぞれの床の上には、かつて12人の男女が立っていた"

    "けれどももう、そこにはたった二人しかいない。"

    "海晴と――私だ。"

    "果てなき広い闇の中で、私は海晴と向かい合っていた。"

    scene bg fatalhall01 up with dissolve

    show rnk uni nor nor ci at ci_r with ci_in

    voice get_voice_filename("rnk", 1789)
    rinka "「……来たね」"

    show mhr uni nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("mhr", 909)
    miharu "「――ああ」"

    "当然というべきか、直未の姿も、レテの姿もここにはなかった。"

    "≪運命の大広間≫はあくまで、≪女神の選定≫の参加者のための居場所。"

    "彼らが何かしらの力というものを持っていても、それとこれとは別、ということだろう。"

    "もっとも女神パルカとの決着を私たちの手でつけなくてはならないということには、何も変わりがない。"

    show dia sta fro nor ci at ci_c with ci_in

    voice get_voice_filename("dia", 404)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "高らかで清らかな声とともに、その少女は現れた。"

    "女神パルカは変わらず、微笑みを浮かべるばかりだった。"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「皆サマといっても、もはやお二人サマだけでございますけれども」"

    show dia sta nor rev ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「今宵、お二人のどちらかとお別れしなければならないのはとても、寂しいことですわ」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマ方がどんな結論を出したのか、ワタクシにお見せくださいませ」"

    show rnk uni nor que ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「一つ、聞かせて」"

    show dia sta fro gl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「なんでしょうか？」"


    play music audio.restlessness

    show rnk uni arm nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「貴女には……私たちの運命が、見えてるの？　この先の運命が、見えてるの？」"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「もし決まっているのなら……この選定にはどんな意味があったの？」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでは貴女サマの質問には、端的にお答えさせていただきましょう」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシが運命を見るとき、貴女サマのような認識で見ているわけではございません」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「複数の可能性を同時に観測しているのでございます」"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「たとえば12人の皆サマがいらっしゃったとき、皆サマがそれぞれ≪運命の終着点≫にいらっしゃる未来を、ワタクシは別々に見ていました」"

    show mhr uni nor ser rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「つまり、今は」"

    show dia sta nor nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「ええ。ワタクシにはⅠ番サマが≪運命の終着点≫に到達した未来も、Ⅱ番サマが再びワタクシの器になる未来も、見えていますわ」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「どちらかが脱落した時点で、その未来は世界の本流から遠ざかっていきますけれど」"

    "世界の本流から遠ざかる。"

    "前回の選定でその話を聞いていた私は、すでにその意味が分かっていた。"

    "今がむしろ、世界というものにとっては異常な状態なのだ。"

    "未来は選択されて削ぎ落され、正しい形に戻っていく。"

    show rnk uni arm sad ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「そっか。なら、あなたにも分からない世界は存在するってことだね」"

    show dia sta fro fee ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら？　ちゃんとワタクシのお話を聞いていらっしゃいましたか？」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「可能性は二つしかないのです。Ⅰ番サマが脱落するか、Ⅱ番サマが脱落するかの二つのみ」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「もしも貴女サマ方が決着をつけられなければ、Ⅰ番サマである貴女サマが最後の一人になるのです」"

    "パルカはいつも通りの余裕の声で、そう告げた。"

    "私はそんな彼女に対し、首を横に振り、答えていた。"

    show rnk uni arm nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「もう、いいんだよ。始めよう。最後の指名を」"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「ええ。それでは今宵の指名を始めましょう。回りなさい。運命の大時計」"

    "地響きの音とともに、時計の針が動き出す。"


    scene bg fatalhall01 up large
    show dia sta fro sm2 big at std_c
    with dissolve_long

    voice get_voice_filename("dia")
    parca "「それではⅠ番サマ。指名はいかがなさますか？」"

    "パルカは私の目を見据え、そう言った。"

    "彼女の目は、とても澄んでいる。"

    "ダイアナも生きていた頃は、きっとこんな瞳をしたいのだろう。"

    "お上品な彼女のイメージに、ぴったりだ。"

    "あらためてみると、やはり、パルカは少女だ。"

    "人よりも生への想いが強かっただけの女の子。"

    "この世界に存在するらしい何かと、たまたま波長が合ってしまっただけの女の子。"

    "運命から疎外されたにもかかわらず、運命に縛られ続けた女の子。"

    show dia sta fro cle big with ci_change

    voice get_voice_filename("dia")
    parca "「いかがなさいますか？」"

    "綺麗な声で、彼女は再び私にそう訊ねた。"

    "答えは決まっている。"

    "私はこの瞬間を噛み締めながら、答えた。"

    scene bg fatalhall01 up with dissolve

    show rnk uni arm nor ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「するよ、指名。これで、終わりにしよう」"

    "12週間にわたる≪女神の選定≫を。"

    "12回にわたる≪女神の選定≫を。"

    "長きにわたりあなたを苦しめた、運命の歪みを。"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「運命の女神パルカ――ダイアナ・ハリソン。あなたを、指名する」"

    "彼女の瞳をしっかりと見据え、私はそう告げた。"

    show dia sta fro fee ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「……はぁ？　でございますわ」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシを指名？　そんなこと、できるはずがないではありませんか」"

    show dia sta fro fee ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシは運命の女神パルカ。ダイアナ・ハリソンではございませんわ」"

    "女神は珍しく表情を歪ませ、不快そうな顔を浮かべた。"

    show mhr uni sco thi rev ci at ci_l with ci_in

    voice get_voice_filename("mhr")
    miharu "「指名……できない……？」"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「なるほど。Ⅱ番サマも共謀していらしたのですね」"

    show dia sta fro cle ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシに対する冒涜……そう思って差し支えはありませんね？」"

    "平然としている女神に対し、私は焦っていた。"

    "カードは揃えた。あとは指名するだけなのに。"

    "レテは、女神パルカからダイアナの記憶を抜き取ったと言っていた。"

    "だから、なのだろうか。"

    "いや、でも。"

    "レテはいつも中途半端な情報しか話さないけれど、必ず何かヒントがあった。"

    "私に記憶を戻していくときも、意味があったように。"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「計画は滞りなく。思惑は淀みなく」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「……察するに、貴女サマはワタクシの目的に気づいてしまったのですね？」"

    show rnk uni nor nor ci with ci_change_wait

    "パルカの質問に、私は頷いた。"

    "指名がうまくいかないことに緊張しているが、怯んだ姿を見せるわけにはいかない。"

    show mhr uni nor ser rev ci with ci_change_wait

    "隣にいる海晴も、同じように堂々としていた。"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシは貴女サマをいただこうと思っております」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマの肉体は、どうやらワタクシと同質。他の参加者の誰とも違った親近感を感じていました」"

    show dia sta fro cle ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマの存在も、ワタクシと同じ運命の歪みの中にありました。それはつまり、生まれながらにして極僅かではありますが……女神の力を持っていることと同じ」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「何より貴女サマの心は、≪女神の選定≫の最後の一人になるに相応しい輝きを放っています」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「Ⅱ番サマ。あなたは今宵、Ⅰ番サマを指名なさらないのでしょう？」"

    show mhr uni sco wic rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「……ああ。ぼくが凛火を指名するなんて、ありえないさ」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「ふふ、ふふ。それではこれで、指名者はなしではありませんか」"

    "不敵に笑う女神の声が、≪運命の大広間≫に響く。"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「以前に申し上げた通り、残るのはⅠ番サマということですわね」"

    hide dia with ci_out

    "パルカは無慈悲にそう言うと、回る時計を停止させ、何もない空間を歩いて行く。"

    "そして運命の大広間の中央まで移動すると、スカートのすそをつまみ上げ、お辞儀をした。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro nor big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それではこれをもちまして、≪女神の選定≫を終わりに……」"



    voice get_voice_filename("har")
    diana "「あら？　指名されたんですから、きちんと守らないといけませんわよね」"

    scene bg fatalhall01 normal with dissolve

    "パルカと同じ声でありながら、決してパルカではない声が、運命の大広間に響く。"


    scene bg fatalhall01 up with dissolve

    play music audio.parca
    show har sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("har", 4)
    diana "「ごきげんよう。優雅で高貴なワタクシ」"

    "気づけばパルカの正面には、栗毛の少女。ダイアナがいた。"

    "彼女は、真剣な表情で自分と同じ顔をした少女に向き合っている。"

    show dia sta nor ups ci at ci_r with ci_in

    voice get_voice_filename("dia")
    parca "「――え？」"

    "パルカは振り返ると、驚愕の声をあげた。"

    "それは、今まで聞いたことのない彼女の声だった。"

    show dia sta nor ups ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマは……？　一体どうして、ワタクシの{rb}≪運命の大広間≫{/rb}{rt}ばしょ{/rt}に……？」"

    show har sta nor que rev ci with ci_change

    voice get_voice_filename("har")
    diana "「これは受け売りですけれども、ここはそもそもワタクシのものではないのでしょう？」"

    show har sta nor nor rev ci with ci_change

    voice get_voice_filename("har")
    diana "「≪運命の大広間≫というのはあくまで、≪女神の選定≫というシステムを実行するために与えられているもの、とお聞きいたしましたけれど」"

    show dia sta fro fee ci with ci_change

    voice get_voice_filename("dia")
    parca "「ありえませんわ。たとえ他に女神がいらっしゃったとしても、あくまでここはワタクシの場所」"

    show dia sta nor ene ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシの許可なく侵入することなど、不可能でございます」"

    show har sta nor smi rev ci with ci_change

    voice get_voice_filename("har")
    diana "「ええ。ですからワタクシが許可をいたしました」"

    "パルカは目を細めて、ダイアナを不審そうに見つめていた。"

    "記憶のないパルカは、なぜ自分と同じ顔をした少女がそこにいるのか理解できないだろう。"

    "しかし私のことを同質の存在と感じ取れるのならば、ダイアナはより自分に近しい存在とも感じ取っているはずだ。"

    show dia sta fro cle ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマはワタクシ、ということですのね？」"

    show har sta nor nor rev ci with ci_change

    voice get_voice_filename("har")
    diana "「ええ。ワタクシは貴女サマ。貴女サマはワタクシ」"

    show har sta nor smi rev ci with ci_change

    voice get_voice_filename("har")
    diana "「生まれた順序はあれど、優劣はありませんわ」"

    show dia sta nor ene ci with ci_change

    voice get_voice_filename("dia")
    parca "「ご冗談を。ワタクシは女神。貴女サマがいらっしゃったことには驚きましたが……許し難い無礼には違いありません。立ち去っていただきます」"

    "ダイアナは手を伸ばしたパルカに対して、静かに首を横に振った。"

    "その顔に微笑みはなく、私が感じているのはむしろ、憐憫だった。"

    show har sta nor sad rev ci with ci_change

    voice get_voice_filename("har")
    diana "「立ち去るのは、ワタクシたちでございます。ワタクシたちはすでに、この世界にいてはいけないのですわ」"

    "ダイアナはパルカと同じように、手を伸ばした。"

    "そしてパルカの手のひらに、自分の手のひらを合わせる。"

    show dia sta nor ups ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマ――何を」"

    show har sta nor smi rev ci with ci_change

    voice get_voice_filename("har")
    diana "「さあ、戻りましょう。そして、受け入れましょう」"

    "――運命を。"

    "二人は広い光に包まれて、すぐに――。"

    scene ecg parcaindiana close with wfade_long


    voice get_voice_filename("dia")
    parca "「ごきげんよう。ワタクシが真に進むべき、運命サマ」"

    "一人の女神パルカへと変わった。"

    "それは、あまりにあっけない変化だった。"

    "瞬きの間に、ダイアナという少女の記憶は、パルカという人間であることを忘れてしまった少女の中へと帰っていった。"

    "見た目はパルカでありながら、まとっている雰囲気はこれまでと異なっていた。"


    scene bg fatalhall01 up
    show mhr uni sco thi rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「あれは、ぼくたちの知っている女神では――ないね」"

    show rnk uni arm nor ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「ダイアナは、戻るって言ってた。きっと、パルカから抜けていた記憶が、戻ったんだ」"

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「不思議ですわね」"

    show dia sta nor sad rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「記憶というのはこうも、胸を痛めるものなのですね」"

    "パルカの言葉の意味は、分からない。"

    "ただ一つ言えるのは、彼女はとても辛そうな顔を浮かべているということだった。"

    "そして少しの時間、パルカは何かを噛み締めるように目を閉じた。"

    "その間言葉は発せず、彼女が何を考えていたのかは分からない。"

    "しばらくして彼女は小さくを息を吸うと、ひり出すような声で告げた。"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでは、Ⅰ番サマによるワタクシの指名を行いましょう」"

    "今までの指名と同じように、Ⅰ番と書かれた床が動き出したのはこの直後だった。"

    show rnk uni arm lie ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「行ってくる」"

    show mhr uni sco smi rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「ああ。パルカ――いや、ダイアナなのかな。君には、今まで世話になったというべきだね」"

    show mhr uni sco con rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「思えば君とは、物心がつく前から知り合っていた。決して友人になることはできなかったけれど、きっと君はぼくの運命にとって必要な存在だった」"

    show mhr uni sco smi rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「君は本来の運命に還り、二度とぼくと会うことはないだろう。けれど、あえて言わせもらおう。これはぼくにとって、魔法の言葉だから」"

    show mhr uni nor rea rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「また――いつか」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「ええ。それでは、ごきげんよう」"

    "海晴の言葉を聞き終える頃、私たちはすでに移動を始めていたのだった。"









    $ set_info_location("16")

    stop music fadeout 1
    scene bg fatalhall02 normal with fade_long
    play music audio.fatalhall
    pause 2
    scene bg fatalhall02 up with dissolve

    show rnk uni nor nor ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「まさか、こんな瞬間が来るとは思ってなかった」"

    "運命の大広間の、上層。"

    "床の上に立っているのは私だけだった。"

    "女神パルカは何もない場所に、しかし背筋を伸ばして立っていた。"

    show dia sta fro nor ci at ci_l with ci_in

    voice get_voice_filename("dia")
    parca "「ワタクシはもっと思っていませんでしたわ。そもそも、ワタクシにはこんなにたくさんの記憶があるなど、知りませんでした」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシはあくまで、存在し続けるためのシステム。でもそれが矛盾でしたわね」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「本当にただのシステムならば、貴女サマを頂戴しようなんて思いませんものね」"

    show dia sta fro no2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「欲を持った時点で、ワタクシは人間であることに気がつくべきだったのでしょう」"

    show rnk uni nor que ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「一つ、質問。貴女が脱落したら、私たちはどうなるの？」"

    show dia sta fro fee ci with ci_change

    voice get_voice_filename("dia")
    parca "「レオはそんなことも、貴女サマに教えなかったのですね」"

    scene ecg parcaindiana general with dissolve_long


    voice get_voice_filename("dia")
    parca "「ワタクシが消えれば、貴女サマとⅡ番サマの二人が残ります……が、それだけでは、世界は貴女サマだけを生かそうとするでしょう」"


    voice get_voice_filename("dia")
    parca "「しかし、貴女サマには一度だけ、奇蹟を起こすことができるでしょう」"


    voice get_voice_filename("dia")
    parca "「≪運命の大広間≫は、人の{rb}想いの欠片{/rb}{rt}ユメ{/rt}をエネルギーとして蓄積しているのです」"


    voice get_voice_filename("dia")
    parca "「本来であれば、選定で脱落した11人分の想いの力を消費して、概念上の存在であるワタクシが現実の人間を器にするという奇蹟を起こす予定でした」"


    voice get_voice_filename("dia")
    parca "「当然、ワタクシが脱落すればその奇蹟は行われません。≪運命の大広間≫にはエネルギーが蓄積したままになります」"


    voice get_voice_filename("dia")
    parca "「貴女サマはそのエネルギーを使って、貴女サマもⅡ番サマも生きている――死がなかったことになっている――今の世界を固定してください」"


    voice get_voice_filename("dia")
    parca "「運命を、変えてください」"


    voice get_voice_filename("dia")
    parca "「すでに離れてしまった可能性の世界を引き戻すことは不可能でしょうけれども、今はまだ、お二人サマの生きている世界は交差し、存在しています」"


    voice get_voice_filename("dia")
    parca "「ワタクシを現実世界に存在させる奇蹟が起こせる力ならば、すでに絡み合っている世界を、世界の本流に変えてしまうことは容易いでしょう」"


    voice get_voice_filename("dia")
    parca "「そもそも、世界は誰かが見ることで存在しています」"


    voice get_voice_filename("dia")
    parca "「今や貴女サマだけでなく、ワタクシやレオ、直未サマや真央サマも、お二人サマが生き続ける未来を思い描いていることでしょう」"


    voice get_voice_filename("dia")
    parca "「背中を押してあげれば、簡単に運命は変わります。ふふ、運命の糸に背中はありませんけれど」"


    scene bg fatalhall02 up
    show rnk uni nor que ci at ci_r
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「私は――願えばいいの？」"

    show dia sta nor smi rev ci at ci_l with ci_in

    voice get_voice_filename("dia")
    parca "「ええ。ワタクシが消滅した時点で、最も女神に近いのは貴女サマになります」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「ここはあくまで、夢の中。貴女サマの認知が、世界を変えますわ。迷うことなく、お望みの未来を願ってくださいませ」"

    show dia sta nor sad rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「そろそろ、指名をしてくださいな。ワタクシ、これ以上お話をしていると名残惜しくなってしまいますもの」"

    "私は頷いて、カードブックを開いた。"

    "このカードブックとも、今日でお別れなのだろう。"

    "私がこれまでに取得した全てのカードが、空中に浮かび上がる。"

    "ああ、とても。"

    "長い、道のりだった。"


    play music audio.electing
    scene ecg senteirinka gentle with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「氏名――ダイアナ・ハリソン」"


    scene bg fatalhall02 up
    show dia sta nor smi rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("dia")
    parca "「ええ。パルカになった今でも、その名前がしっくりきますわね」"

    show dia sta nor sad rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「お父サマにいただいた、大切な名前ですもの」"

    scene ecg senteirinka gentle with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「死因――中毒死」"


    scene bg fatalhall02 up
    show dia sta nor sad rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("dia")
    parca "「思い出すと、とても悲しくなりますわね」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「リンダはワタクシを助けられなかったことを、後悔していたのでしょうか」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「間違いなく言えるのは、ワタクシはリンダの幸せを願っても――恨んだことは一度もありませんでした」"

    "目の前で家族を見捨てなくてはならなかった、リンダさんとお母さん。"

    "二人にとってもパルカの言葉は、この上なく救いになったことだろう。"

    scene ecg senteirinka gentle with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「未練――人生のやり直し」"


    scene ecg parcaindiana general with dissolve


    voice get_voice_filename("dia")
    parca "「その通りでございます」"

    "今晩、直未の中にいるダイアナは自分の未練をそう告げた。"

    "それは、いなくなってしまった人たちへの想いだった。"

    "ダイアナは特別な少女だった。"

    "周囲の11人が死んだという事実は、自分のせいだと彼女は語ったのだ。"

    "ダイアナに訪れるはずの運命は、彼女が拒否したから、別の誰かの運命に変わったのだ。"

    "けれどもそれも、12回目でついに逃れられない運命となった。"

    "もっとも彼女は、逃れられない運命を歪ませることで、存在し続けたのだけれど。"


    voice get_voice_filename("dia")
    parca "「もし人生をやり直せるなら――素直に運命を受け入れたい。ワタクシは死の瞬間、そう思っていました」"


    voice get_voice_filename("rnk")
    rinka "「記憶がレテに奪われても、その想いの一部は残っていた。だから私になって、人生をやり直そうとしたんだね」"


    voice get_voice_filename("dia")
    parca "「ええ。貴女サマのおっしゃる通りでございます」"


    voice get_voice_filename("dia")
    parca "「死にたくなかったくせに、他の誰かが死ぬのも嫌だった。そんな我儘な――運命の奴隷が、ダイアナ・ハリソンでした」"

    scene ecg trianglecard small with dissolve

    "３枚のカードは光を放ちながら、パルカと私の間に移動を始める。"


    scene bg fatalhall02 up
    show dia sta fro cle ci at ci_l
    with dissolve_long

    voice get_voice_filename("dia")
    parca "「最後に、懺悔させてください」"

    show rnk uni nor nor ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「駄目だよ。だってあなたは、ダイアナ・ハリソンなんだから」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「……あら？」"

    show rnk uni arm nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「なら、懺悔することなんて何もない。とっくに、あなたは許されている」"

    show dia sta nor sad rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「いいのですか？　運命の女神パルカが、皆サマに仮初の希望を与えて苦しめたことに間違いはありません。これまでに、何度も何度も何度も何度も」"

    show rnk uni arm sad ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「知らないよ。でも、あなたはただ生きたかっただけ。私と、何も変わらない」"

    "だって、私がずっと願い続けてきたのは。"

    "生き続けたいという、当たり前の望みだけなのだから。"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシを救って欲しいとは、レオもよく言ったものです」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「なるほど。まさか貴女サマが最後にそんなことを言ってくださるとは思いませんでした」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシ、少し泣きそうでございます」"

    show rnk uni arm lie ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「……嘘つき。涙を流してから言えよ」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら、口の悪い本性が出ましたわね。悪いのは目つきだけにしてくださいな」"

    scene ecg trianglecard cover with dissolve_long

    "光は、私たちごと運命の大広間全体を包み込んだ。"

    "きっとこれで、よかった。"

    "誰かを救うなんて大げさなことはできないけれど、ただ相手を知って、本気でぶつかること。"

    "私にできるのは、それだけだ。"


    voice get_voice_filename("dia")
    parca "「ありがとうございました」"

    "反対に、私が救われていた。"

    "あなたと決別を選んだ、私が。"






    stop music fadeout 2
    scene white with Dissolve(3)
    play music audio.death
    pause 2

    scene ecg dianafire normal with fade_longest

    "私は再び、炎の記憶を目にしていた。"

    "それはもう何度も見た記憶。"

    "皮肉にも、私の原風景なのだ。"





    voice get_voice_filename("rnk")
    rinka "「……ダイアナ……パルカ……」"

    "そう呟いても、彼女たちはもういない。"

    "本来の運命――遥か昔の死――へと戻っていったのだろう。"

    "彼女たちは現実世界の住人ではないので、これまでの行動はなかったことにはならないのだろう。"

    "これまでのパルカの行動が≪なかったことになる≫という可能性も考慮したけれど、さすがにないとは予想していた。どうやら、その予想は当たっていたようだ。"

    "もし予想が当たっていれば、≪女神の選定≫自体がなかったことになっている。"

    "私が≪運命の大広間≫にいるということは、世界は全く改変されていないということだ。"

    "それで、よかった。"

    "もし世界が変わってしまったら、海晴や直未や真央との関係も、変わってしまう。"

    "――戻ろう。"

    "心の中でそう思うと、私の立つ床は動き出した。"

    "私には、この選定最後の役目が残っているのだから。"







    python:
        set_info_scene("197")
        set_info_location("01")

    stop music fadeout 1
    scene bg fatalhall01 dark with fade_long
    pause 1

    "全てがうまくいくはずだった。"

    "パルカと別れ、彼女の言葉通りに≪運命の大広間≫に蓄積した力を使い、運命を固定する。"

    "そのはずだった。"


    play music audio.kinpaku

    show rnk uni arm uil at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……なに、これ……」"

    "だが、運命は優しくないということなのだろうか。"

    "私が戻ってきた運命の大広間は、黒い炎に包まれていた。"

    show rnk uni ang an2 with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴！」"

    "私が上層へ行く前と同じく、海晴はずっと床の上にいたらしい。"

    "というよりかは、いなければならなかったというべきか。"

    "私たちは運命の大広間において、自由に動くことができない。"

    "だが、今の私は違った。"

    "パルカのように床と床の間を歩き、海晴のいるⅡ番の床へと移動した。"

    show mhr uni pai irr rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「り……ん……か……」"

    "黒い炎は、海晴のことを蝕んでいた。"

    "肉体を燃やすのではなく、心を燃やしていた。"

    "パルカの言う通り、女神を脱落させた私はこの世界では女神に近い存在へと変わったのだろうか、外傷のない海晴の状態が手に取るように分かっていた。"

    show mhr uni pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「あ……れを……」"

    "海晴は弱った声で、運命の大広間の中心を指差した。"

    "炎はよく見ると、その中心から燃え広がっていた。"

    scene ecg parcafire alone with dissolve_long



    voice get_voice_filename("har")
    diana "「あ、ああああ……」"

    "その少女は、苦しそうな声で喘いでいた。"

    "頭を抱え、涙を流しながら喉を焼いていた。"


    voice get_voice_filename("rnk")
    rinka "「どうして……」"

    "パルカがまだ、存在している。"

    "間違いなく、彼女は脱落したはずなのだ。"

    "死の間際の映像も見た。"

    "女神だから例外――なんてことがあれば、きっとあの子は説明してくれたはずだ。"


    scene bg fatalhall01 dark
    show mhr uni pai irr rev at std_cl
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「分からない……すまない……ぼくも、突然、あの炎に……」"

    show rnk uni nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「大丈夫。喋らなくてもいいよ」"

    "症状としては、火事で煙を吸い込んだ時に似ている。"

    "肺がうまく機能していないような、そんな声だった。"

    "この炎は、よくないものだ。"

    "状況が分からなくても、それだけははっきりと理解できる。"

    "となれば、あの中心にいるパルカはもっと――。"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「助けなきゃ」"

    scene ecg parcafire alone with dissolve_long

    "体の方が、勝手に動いていた。"

    "何もない場所を歩くのは怖かったが、それでも、中心に向かって走っていた。"

    "パルカの身長ならば、背負って動くこともできるはずだ。"

    "とにかく中心にいるのは一番駄目だ。"

    "まず、海晴のいるⅡ番の床の上に連れて行こう。"

    "炎に熱はない。多少なら触れても問題はなさそうだ。"

    "私は時間を優先し、最短距離でパルカのところへと向かった。"



    voice get_voice_filename("har")
    diana "「あああああああああああ！」"

    "パルカは頭を抱えてうずくまっていた。"

    "私は、パルカを抱き締めた。"


    play music audio.firedeath
    scene ecg parcafire rinka with dissolve


    voice get_voice_filename("rnk")
    rinka "「大丈夫……！」"

    "こうなると、火事の中にいる少女そのものだ。"

    "ダイアナの死。"

    "炎が黒いこととここが夢の世界であることを除けば、今の状況は酷似している。"

    "私はパルカを見捨てる気はなかった。"

    "ここまでくれば必ず――救ってみせる。"

    "しかし、パルカは私の声など耳に入らず、丸くなってうずくまったままぴくりとも動かなかった。"


    voice get_voice_filename("rnk")
    rinka "「くっ……」"


    scene bg fatalhall01 dark
    show let sta con ser at std_cr
    with dissolve_long

    voice get_voice_filename("let", 128)
    lete "「……お困りのようだね」"

    show rnk uni arm ang rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「レテ！　どうして……」"

    "そういえば、やっと人型状態の彼と声を出して会話ができた。"

    "けれども、今そんなことは大事じゃない。"

    show let sta con tro with std_change

    voice get_voice_filename("let")
    lete "「残念だけれど、私は頃合いを見て消えにきたんだ。運命から外れてしまった私が死ぬには、因果で結ばれたパルカの消滅に引っ張られるしかないからね」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「しかしこの状況だ。できる限り手を貸そう」"

    "夢の世界のことについて私よりも多くを知るレテがこのタイミングで来てくれることはとても、頼もしかった。"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「取り急ぎ君がすべきは……まず、その子から離れることだ」"

    "レテは冷静な口調で、続けた。"

    scene ecg parcafire rinka with dissolve_long


    voice get_voice_filename("let")
    lete "「≪運命の大広間≫を覆う黒い炎は、ダイアナから出ているだろう？」"


    voice get_voice_filename("let")
    lete "「君はダイアナを救おうとしているんだね。この子がこれまでと同じダイアナだと思っているからかい？」"


    voice get_voice_filename("rnk")
    rinka "「勿体ぶってないで！」"


    voice get_voice_filename("let")
    lete "「おや……失礼。彼女はダイアナ。ただし君の後輩の肉体を借りていたダイアナでも、これまで女神として君たちの前に現れていたダイアナでもない」"


    voice get_voice_filename("let")
    lete "「私は以前君に、パルカになったダイアナから、人間であった時のほとんどの記憶を奪い取ったと話したはずだ」"


    voice get_voice_filename("let")
    lete "「そう、奪ったのはあくまでほとんど」"


    voice get_voice_filename("let")
    lete "「ダイアナがダイアナであるための最低限の記憶は、彼女の中に残したんだ」"


    voice get_voice_filename("let")
    lete "「つまり今の彼女は、あの時私が奪い取らなかった、残りの記憶といえばいい」"


    voice get_voice_filename("let")
    lete "「≪女神の選定≫という形で一時的な希望とその後に待つ絶望を人々に与え続け、人の命を踏み台にして生き続けた自分に嫌気がさした、人間らしい人格」"


    voice get_voice_filename("let")
    lete "「これまでずっと、パルカという存在を切り離し、隠れ続けてきたダイアナという少女の根幹だ」"


    voice get_voice_filename("let")
    lete "「恐らくは――パルカがダイアナの記憶を取り戻した際に、パルカの中に元々残っていたダイアナの記憶は統合されなかった」"


    voice get_voice_filename("let")
    lete "「君が抱きしめているその少女だけが、別の存在として新たに独立したんだ」"


    scene bg fatalhall01 dark
    show rnk uni arm ang rev at std_cl
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「なんで？」"

    show let sta con ser at std_cr with std_in

    voice get_voice_filename("let")
    lete "「分かるだろう。どんなに業を背負ってでも、消えたくないからに決まっている」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「死に際、人間であったダイアナがパルカになるほどの執着は、紛れもなくあの子から生まれたものだ」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「あれは、≪存続し続けたい≫という人間の欲望の極地。黒い炎は、彼女の心象風景」"

    show let sta con tro with std_change

    voice get_voice_filename("let")
    lete "「どんなに苦しんでも、ダイアナの本性は生きたいと思い続けてきたということだ」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「彼女は今――彼女は自分がパルカになった時の状況を再現することで、もう一度パルカになろうとしているんだ」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「幸いにも、ここには11人分の想いの力が蓄積している。奇しくも、元は自分と同一だった存在も含めてね」"

    show let sta con se2 with std_change

    voice get_voice_filename("let")
    lete "「ああ困った！　まさかそこまで、彼女が自らの存続に執着しているなんて……。私には、これ以上！」"

    show rnk uni nor ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……レテ？」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「失礼、取り乱してしまった。が……事態は深刻だ」"

    scene ecg parcafire rinka with dissolve_long

    "私が思ったことは、正しかったということだろうか。"

    "この状況がダイアナの死に似ているということ。"


    voice get_voice_filename("rnk")
    rinka "「ダイアナ！　ダイアナ！　落ち着いて！」"


    voice get_voice_filename("har")
    diana "「ああ、ああああああああ、ああ！」"


    voice get_voice_filename("let")
    lete "「無駄だ」"


    voice get_voice_filename("rnk")
    rinka "「どうすれば！」"


    voice get_voice_filename("let")
    lete "「……分からない」"

    "レテが、分からないと言った。"

    "レテが分からないことが、私に分かるはずが――。"

    "いや、諦めようとしてどうする。"

    "レテは自分のできることをしてくれた。"

    "あんなに弱った黒猫になってしまってまで、私たちのために尽くしてくれた。"

    "元から、彼は言ったはずだ。"

    "私が自分でどうにかしないといけないと。"


    scene bg fatalhall01 dark
    show rnk uni arm vig rev at std_cl
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「一つ、お願いがある。海晴を、現実世界に返してくれる？」"

    show let sta con ser at std_cr with std_in

    voice get_voice_filename("let")
    lete "「それは、すでに完了している」"


    hide rnk
    hide let
    with std_out

    "私はⅡ番の床を見た。"

    "そこにはすでに、海晴の姿はなかった。"


    scene bg fatalhall01 dark
    show let sta con ser at std_cr
    with dissolve_long

    voice get_voice_filename("let")
    lete "「君の後輩は、まだ辛うじて私の力が残っている。正確には、この空間と繋がっている」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「私がパルカの因果に引かれて≪運命の大広間≫に来ることができたように、君の後輩は危機を察知して君の友人を現実世界に連れ戻したのだろう」"

    show let sta con se2 with std_change

    voice get_voice_filename("let")
    lete "「私の意志とも繋がっているはずだからね」"

    "レテは焦った表情を浮かべたまま、続けた。"

    show let sta con se2 with std_change

    voice get_voice_filename("let")
    lete "「はっきり言おう。私は間もなく、消滅する」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「先ほど言った通り、私はパルカの因果に引かれている。つまり彼女が消滅している以上、私も消滅する」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「黙っていて申し訳ない。私の真の目的は、死ぬことにあった。運命の輪から外れてしまった私が死ぬには、そうするしかなかったんだ」"

    show rnk uni arm nor rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「なんでそんな、突然……」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「けれど君を助けたいという気持ちに嘘はない。目的を黙っていただけで、私は君たちの不利になるようなことはしていない」"

    show rnk uni nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……分かってる」"

    show let sta con tro with std_change

    voice get_voice_filename("let")
    lete "「だが、今はもう時間がない。君に協力している、存在の余裕がない」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「私と君の後輩が繋がっている今なら、君は現実世界に戻れる。戻るなら、今しかない」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私が戻ったら、ダイアナはどうなるの？」"

    "ダイアナのうめき声が、聞こえる。"

    "黒い炎はいまだ、揺らめき続けていた。"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「再び女神になり、≪因果の刻≫で結ばれた12人を選び出し、≪女神の選定≫を行うだろう」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「君の見知ったダイアナとパルカはすでに消滅しているから、二度と指名されることはない」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「存続することそのものを意義として、永遠に続くことだろう」"

    "それは、つまり。"

    show rnk uni arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ダイアナは永遠に救われない――」"

    show let sta con se2 with std_change

    voice get_voice_filename("let")
    lete "「ああ、言わなければよかった。話さなければ、君は大人しく元の世界へ帰っただろうに」"

    show let sta con ser with std_change

    voice get_voice_filename("let")
    lete "「私は今、心から後悔している」"

    "レテはきっと、私の表情を見てしまったのだろう。"

    "私の一族をずっと見続けているのだから、何を考えているのかくらいすぐに分かるはずだ。"

    show rnk uni arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「さすが。よく分かっているね、私のこと」"

    show let sta con se2 with std_change

    voice get_voice_filename("let")
    lete "「駄目だ。もう、私は――」"

    "レテの体が、真っ白に光り出す。"

    "運命の大広間で、カードが光るのに似ていた。"

    show rnk uni nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ありがとう、レテ」"

    show let sta con sm2 with std_change

    voice get_voice_filename("let")
    lete "「お礼を言うのはこちらだ」"

    show let sta con se2 with std_change

    voice get_voice_filename("let")
    lete "「しかし、まだ――」"

    hide let with std_out

    "レテはそれ以上言葉を続ける余裕はなく、消えていった。"

    "本来の運命に戻っていった。つまり、死んだ。"

    "ダイアナと同じところに行けたのなら、それは不幸ではないのだろう。"

    "少なくとも、彼がそれを望んでいたのは間違いないだろう。"

    "問題は、こっちのダイアナにあった。"


    play music audio.rinka
    scene ecg parcafire rinka with dissolve_long


    voice get_voice_filename("har")
    diana "「う、うう……」"

    "炎は広がり続け、運命の大広間を真っ黒にしてしまいそうだ。"

    "ダイアナの死に際の再現。"

    "状況だけでなく、彼女の抱えた恐怖そのものが再現されているかのようだった。"

    "私は彼女のちっぽけな背中を、見つめていた。"

    "レテが見抜いた、私の考え。"

    "それは――彼女を救いたいということだった。"

    "実を言うと、方法に心当たりがあった。"

    "女神は言っていた。"

    "ダイアナは自分を見捨てたリンダと母親を恨んではいないと。"

    "人間として、そんなことあり得るのだろうか。"

    "宙に舞う灰の欠片ほども、自分を見捨てた相手に負の感情を抱かないことなど、あり得るのだろうか。"

    "切り離されたのはパルカの方ではなく、ダイアナの方だったのだ。"

    "すくすくと育っていった負の感情。"

    "その原点が、死に際にかすかに生まれた妬みと恨みと憎しみ。"

    "だったら、どうすれば当時の完全な再現にならないかなんて、簡単だ。"


    voice get_voice_filename("rnk")
    rinka "「大丈夫。大丈夫だよ」"

    "ずっと――一緒にいてあげればいい。"

    "私はうずくまってうめき声を上げ続ける彼女を抱きしめたまま、願った。"


    voice get_voice_filename("rnk")
    rinka "「どうかもう、この子を救ってあげてください」"

    "――と。"

    $ add_seen_chapter("12_1-8")

    jump f012_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

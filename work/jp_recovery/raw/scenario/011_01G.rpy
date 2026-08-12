

label f011_01G:







    python:
        set_info_scene("177")
        set_info_time("noon")
        set_info_location("04")

    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "お昼時、海晴がライオン館へ寄ってくれていた。"

    "この日はアルバイトが休みらしい。土曜日なのに珍しい、と思っていた。"

    show mhr sci sco cau rev at std_cl with std_in

    voice get_voice_filename("mhr", 783)
    miharu "「今日は、何時までの予定なんだい？」"

    show rnk apr nor nor at std_cr with std_in

    voice get_voice_filename("rnk", 1618)
    rinka "「えっと、４時の予定。久し振りで、開けるのも遅かったし」"

    show mhr sci sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そうか、なら。閉店作業が終わったら、デートをしよう」"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、いいよ……え？　で、デート？」"

    "会話の流れで思わず頷いてしまったが、それは私が普段使うことのない単語だった。"

    "デート、確か、主にカップルが待ち合わせてどっかに行くやつだ。"

    show rnk apr arm shy with std_change

    voice get_voice_filename("rnk")
    rinka "「えええっ！」"

    show mhr sci nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「予定がないなら、決まりだね。実は、ぼくは久々に水族館に行きたかったんだ。小学生以来、行っていないからね」"

    show mhr sci sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「電車で30分くらいのところに、夜まで開いている水族館があるらしい。そうだね、そこで待ち合わせよう」"

    show rnk apr nor shy with std_change

    voice get_voice_filename("rnk")
    rinka "「うん」"

    "恥ずかしくなって、私は短い言葉で頷くことしかできなかった。"

    "そういえば全然意識していなかったけれど、昨日から、私たちは付き合うことになったのだ。"

    "昨日こそ手を繋いで帰ったけれど、あれは勢いというか、その。"

    "付き合うって、何すればいいんだ？"

    hide mhr with std_out

    "そんなことを考えているうちに、海晴は去ってしまった。"

    "どうやら初デートというのは、待ち合わせるところから始めなければいけないらしい。"

    "その後の３時間ほど、緊張と恥ずかしさのせいで仕事がぎこちなくなってしまった。"







    python:
        set_info_time("evening")
        set_info_location("02")

    stop music fadeout 1
    scene bg station01 with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "午後５時半頃。"

    "お店を閉め、片付けも一通り終えた私は、海晴との待ち合わせ場所に向かっていた。"

    "もう７月なので、この時間ではまだまだ明るい。"

    show rnk sci nor apo at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あー緊張する」"

    "私は思わず、そう呟いていた。"

    "海晴と二人でどこかに行くなんて今までなかったわけでもないのに、それをデートと呼ぶだけでこんなに変わってしまうだなんて思いもしなかった。"

    "そういえば水族館に行ったのは、私も小学生の頃が最後だったと思う。おばあちゃんと一緒に、結構遠くまで行った覚えがある。"

    "大きなジンベエザメを見て感動したのをよく覚えている。"

    "ジンベエザメの背中の模様は、星空のようだとも言われている。"

    "だから小学生の私は、水族館を宇宙のようだって思った記憶がある。今思えば、とても子供らしい。"

    "でも海晴との新しい関係の第一歩として、水族館というのは、いいかもしれない。"

    "だって私にとって、恋愛は宇宙と同じくらいわけの分からないものだから。"





    python:
        set_info_time("night")
        set_info_location("21")

    scene ecg familyrestaurantH2 nor with fade_long
    pause 1

    $ show_hud()

    "18時頃から水族館へ入った私たちは、結局閉館時間ぎりぎりまでいることになった。"

    "決して広くはない館内だったが、その分水槽の配置などが工夫されていて、充実した時間を過ごすことができた。"

    "館内でずっと手を繋いでいるのは恥ずかしかったけれど、水の生き物たちを見ていたらそんな些細なことは気にならなくなった。"

    "その後、お腹も空いたので私たちは近くのファミレスに入った。"

    show ecg familyrestaurantH2 smi with ecg_change


    voice get_voice_filename("mhr")
    miharu "「とても楽しかったね、凛火」"

    scene ecg familyrestaurantG2 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「うん。クラゲがたくさんいるとこもすごく綺麗だったし、エイとかマンタとか大きな魚も見られた」"


    voice get_voice_filename("rnk")
    rinka "「あんなビルの中に、水族館があったなんて知らなかったよ」"

    "子供や家族連れだけでなく、大人も楽しめるように力を入れていて、その、どうやらデートスポットとしても有名らしい。"

    "ビルから見る夜景も綺麗だったし、正直納得してしまった。"

    scene ecg familyrestaurantH2 smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「ぼくは子供のようにはしゃぐ君が可愛くて、凛火ばかり見ていた」"

    scene ecg familyrestaurantG2 shy with dissolve


    voice get_voice_filename("rnk")
    rinka "「も、もうっ。そういうの恥ずかしいからやめてよ」"

    "海晴は周りに人がいる時も、普通にこういうことを言う。"

    "私はそわそわとしてしまい、ハンバーグプレートについてきたフライドポテトをくわえて下を向いた。"

    "たぶん、海晴は私のこういう反応も見て楽しんでいる。"

    "分かっているけれど、ペースは完全に海晴のものだ。"

    scene ecg familyrestaurantH2 smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「明日、お店を開ける予定はあるかい？」"

    "水族館の感想が落ち着いた頃、海晴はそう訊ねてきた。"

    scene ecg familyrestaurantG2 que with dissolve


    voice get_voice_filename("rnk")
    rinka "「あるけど、どうして？」"

    scene ecg familyrestaurantH2 smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「そうか。実は今日、凛火の家に泊まる予定でね」"

    scene ecg familyrestaurantG2 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「ええっ！」"

    scene ecg familyrestaurantH2 smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「明日、遊園地に行こうと誘おうと思っていたんだ。来週になれば、≪女神の選定≫の最終局面を迎えてしまうからね」"

    "なるほど、それで朝が早いからうちに泊まるというわけか。"

    "突然だけど、海晴らしい合理的な判断だ。"

    "海晴はきっと、このために土日を空けてくれたのだろう。私には決して言わないが、恐らく誰かにバイトを代わってもらったに違いない。"

    "そうでなければ、海晴が土日のどちらもバイトがないというのはよっぽどのことがない限り、ないだろう。"

    "こんなことを言うと悲しいが、無理にでもお店を開けなければいけない状況ではない。"

    "一日一日が大切な状況だ。"

    "ならばと、私はお店を休みにして遊園地に行くことに決めた。"

    "だが――。"

    scene ecg familyrestaurantG2 shy with dissolve


    voice get_voice_filename("rnk")
    rinka "「うちに泊まるのはいいけど、そ、そ、そういうことはまだ、まだ早い、からね」"

    scene ecg familyrestaurantH2 shy with dissolve


    voice get_voice_filename("mhr")
    miharu "「――――っ」"

    "私が小声で言うと、海晴の方が顔を真っ赤にして、目を逸らした。"

    "そのままいつものようにくすっ、と笑うと、海晴も小声で答えてくれた。"


    voice get_voice_filename("mhr")
    miharu "「凛火の方からそう言われるとは、思っていなかった。凛火もそういう知識はあるんだね。大丈夫。ぼくは正直、そこまで想定していなかったよ」"

    scene ecg familyrestaurantG2 tro with dissolve


    voice get_voice_filename("rnk")
    rinka "「え、あ、それじゃ、ちょっと……」"

    "私の考え過ぎというか、これじゃ私の方がその、えっと、とにかく。"

    "私はどうしようもなくなってしまって、残っていたポテトを口の中に全部突っ込んで、むせた。"







    $ set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    "私たちは別々にシャワーを浴びて、今日は早く寝ることにした。"

    "この調子だと、明日も日記帳を読むことはできないだろう。"

    "だが、こういうのも悪くないと思っていた。"

    "海晴と一緒にいるのは、単純に楽しかった。"

    "この楽しいが続くのが、付き合うってことなのかな。"


    scene black with dissolve


    voice get_voice_filename("mhr")
    miharu "「おやすみ、凛火」"


    voice get_voice_filename("rnk")
    rinka "「うん、おやすみ。海晴」"

    "明日の朝は早い。"

    "心地よい疲労のおかげで、私はすぐ眠ることができていた。"

    $ add_seen_chapter("11_3-2")








    python:
        set_info_scene("178")
        set_info_date(7, 15, "sun")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_refreshing_morning
    pause 1

    $ show_hud()

    show mhr dat sco smi at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「おはよう、凛火。深い眠りだったようだね」"

    show rnk paj nor que rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「ふあ。おはよう、海晴。あれ、もう準備終わってるの？」"

    "海晴はすでに着替えていて、髪もセットして行く準備を済ませていた。"

    "どうやら私よりも１時間くらい早起きだったらしい。それって、ほとんど寝ていないことになるのではないだろうか。"

    "とはいえ、海晴の目の下にはクマもなく、元気そうだった。"

    "今日の海晴の服は、今まで見たことがない服だった。"



    show mhr dat sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「では、ぼくは下で待っているよ。君の邪魔になっても悪いからね」"

    hide mhr with std_out

    "今日の海晴は一段と綺麗だ。"

    "後ろ姿を見て、私はそう思っていた。"







    python:
        set_info_time("morning")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1

    show rnk dat nor shy at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「どう……かな？」"

    "私も準備を終えて、１階へと下りていた。"

    "海晴がお洒落をしたなら、私もと思って気合を入れてみた。"

    "可愛いから買ったはいいものの、普段着るのは気恥ずかしく、クローゼットをあたためていた服たちだ。"

    show mhr dat sco smi rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「素敵だ」"

    "海晴は臆面なく私の顔を見て、そう言った。"

    "面と向かって言われると、私はやっぱり目を逸らしてしまう。"

    "ともかく、私たちは早朝の街を歩き、駅へと向かうのであった。"







    $ set_info_location("06")


    stop music fadeout 1
    scene bg amusementpark noon with fade_long
    play music audio.amusementpark_noon
    pause 1

    $ show_hud()

    "スターダストキングダム。"

    "先月の５月６日の日曜日。４人で来たこの場所に、今度は海晴と二人で訪れていた。"

    "今日は日曜日なので混んではいたが、夏休み前だし、ゴールデンウィーク程ではない。"

    show mhr dat sco cau rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「さて、どうする？　ぼくは、凛火の行きたいところに行くよ」"

    show rnk dat nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「うーん、そうだね。せっかく来たし、今日は海晴の行きたいように回ろうよ？」"

    show mhr dat sco sh2 rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼ、ぼくのかい？　そう言われると、困ってしまうな」"

    "前回と同じように、どこに何があるかとか、どういうサービスがあるかとか、海晴は予習してきてくれているのだろう。"

    "私がここに行きたいといえば、きっと一番効率的な予定を組んでくれるだろう。"

    "しかし、別に効率的でなくたっていい。"

    show rnk dat nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「前は４人の意見をまとめてたからさ、今日は、海晴のしたいことが、私のしたいこと」"

    show mhr dat sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「なら、ぼくの希望は少し欲張って５つ。君の隣で絶叫マシンに乗ること。お化け屋敷に入ること。夏限定のパレードを見ること。君とお揃いのお土産を買うこと」"

    show mhr dat sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そして――あの日と同じ、夜のパレードを見ること」"

    show rnk dat nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「遊園地に来て５つって、十分謙虚じゃない？　でも、分かった……よし、全部、達成するよ」"

    hide rnk
    hide mhr
    with std_out

    "勇気を出して、今日は私から海晴の手を握った。"

    "そのまま手を引いて、私たちは園内へと向かって行く。"








    $ set_info_time("night")

    stop music fadeout 1
    scene bg amusementpark night with fade_long
    play music audio.amusementpark_night
    pause 1

    $ show_hud()

    "すっかり暗くなった午後８時頃、私たちは海晴の希望のうちすでに４つを達成していた。"

    "絶叫マシンは得意な方なので、フリーフォールには２回目も乗ろうかと思ったが、思いのほか海晴がダメージを受けていた。"

    "ここのお化け屋敷はどちらかというと雰囲気系で、怖いというよりホラーな世界観を楽しむというものだった。"

    "水を使った昼間のパレードは、なんと最前列で見た。ちょっぴり水がかかったけれど、天気がよかったのですぐに乾いた。"

    "お揃いのお土産も、買った。なんと名前が刻印されるペアカップを買ってしまった。"

    "これに関してはもう、完全に魔法にかかっていた。というか舞い上がっていた。"

    "一箱になっているタイプなので、私が一旦預かっている。責任重大だ。"

    "となると、残りは夜のパレード。私たちにとって、それは始まりの想い出でもあった。"

    "夜のパレードを見にきているのは、カップルが特に多い。これは、私が前回ここに来たときに学んだことだった。"

    "でも今回は、私たちもその一員だ。"

    show mhr dat sco smi rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「今日は来てくれてありがとう、凛火」"

    show rnk dat nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「お礼を言うことじゃないよ。私も来たかったから、来たんだ」"

    show mhr dat sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「あの日のことを覚えているかい？」"

    show rnk dat nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「……もちろん」"

    "私は海晴と並んで、パレードが始まるのを待っていた。"

    show rnk dat nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あの時からずいぶん、状況が変わったね」"

    show rnk dat nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「お互い≪女神の選定≫の参加者になったと思えば、その中で最後の二人になった」"

    show mhr dat sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それは偶然ではない。凛火の強さがそうさせたんだ」"

    show rnk dat nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「そうだね、否定はしない。否定をしちゃったら、今まで脱落してきた人たちに失礼だ」"

    show rnk dat nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「でもさ、同時に海晴の覚悟も、この状況を作ってる」"

    show mhr dat sco sh1 rev with std_change

    voice get_voice_filename("mhr")
    miharu "「だと、いいけれど。ぼくは凛火のことをずっと考えてきたから、今ここにいることができている」"

    "パーク内の夜景は、幻想的でとても綺麗だった。まるで夢の中。"

    "もしかしたら、夢の中の世界を知っている私たちがいっても皮肉になってしまうかもしれないけれど。"

    show rnk dat nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「でも一番の変化は、海晴と付き合ってるってことなのかな」"

    show rnk dat nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴に告白してもらって、私は自分に自信が持てたんだ。不思議だよね？」"

    show mhr dat sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくも同じさ。くすっ、確かに不思議かもしれないね」"

    "自分だけでは、自分のことが分からない。"

    "私は海晴から恋という気持ちをぶつけられることで、視野を広げることができた。"

    "海晴と付き合うことに決めてからのたった３日間で、世界の見え方はさらに変わった。"

    "きっとこの世界には、私の知らないものがまだたくさんある。"

    "隣に座るだけでどきどきするように変わってしまった自分の想いを、恋と呼ぶのかもまだ知らないのだから。"

    show mhr dat sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ねえ、凛火」"

    show rnk dat nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「何？」"

    show mhr dat sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「キスを、しようか？」"

    show rnk dat nor shy with std_change

    voice get_voice_filename("rnk")
    rinka "「へっ」"

    show mhr dat sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「昨日眠っているときに、凛火の唇は奪ってしまったけれど」"

    show rnk dat nor shy with std_change

    voice get_voice_filename("rnk")
    rinka "「はへっ！？」"

    show mhr dat sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「冗談さ。ぼくはまだ、ファーストキスをちゃんと残しているよ」"

    show rnk dat nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「確かめようのない冗談は心臓に悪いよ……」"

    show mhr dat sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「けれど、口に出さないとできないなら、まだするべき時ではないんだ。ぼくたちがキスをするとき、きっと確認なんて不要になっている」"

    "一瞬本当にどきりとしてしまった。"

    "私の知り得る恋愛関係の段階の中で、キスというのは相当上の段階だ。"

    "手を繋ぐのとは、東京タワーとスカイツリーくらいの差がある。クラゲとクジラくらいかもしれない。ああもう、動揺してるからわけわかんなくなってきた。"

    "やがて周辺の照明が暗くなり、パレードが始まった。"

    "私は隣に海晴の呼吸と鼓動を感じながら、光と音の芸術を楽しんでいた。"






    python:
        set_info_scene("179")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    "閉園の30分程前にパークを出て、海晴は荷物を取りにライオン館へ戻って来ていた。"

    "お泊りセットなどのかさばるものは、うちに置いていたのだ。"

    "今夜は≪女神の選定≫の日でもある。"

    "お互い自分の部屋でゆっくり休めるように、荷物だけ取りに来てもらうつもりだった。"

    "別れ際、海晴は真剣な表情を浮かべた。"


    play music audio.miharu 

    show mhr dat sco thi rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「一つ、提案があるんだ。聞いてくれるかい？」"

    show rnk dat nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「≪女神の選定≫のことだね」"

    show mhr dat sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ああ。今週ずっと考えていたんだけれど、今日、やっと考えがまとまったんだ」"

    show mhr dat sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君がぼくを指名して、ぼくがそれを防御する。君の提案を試してみるなら、今回しかないと思うんだ」"

    show rnk dat nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「どうして？」"

    show mhr dat sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「今夜が11度目の選定だからさ。例えば女神は、強権をもってその指名を無効にするかもしれない。その場合でも、一度の猶予があれば別の方法を考えることができる」"

    "海晴の話は納得できるものだったので、私は頷いた。"

    "私も、お互いが指名できなくなった場合の一人の決め方をいくつか思いついていた。"

    "例えば持っているカードの数とか、これまでにオープンにしたカードの数とか、カードが関わってくるはずだ。"

    "女神が選定の管理者としてその指名を無効にするというのは、あり得る話だ。"

    "もし私が思いついたように強制的に最後の一人を決める手段があるとするなら、最後の選定で私たちがお互いを指名できなくなってしまった場合に、逃げ場なくその手段をとらされるに違いない。"

    "とすれば確かに、試してみるのは今日しかない。案外ノーゲームになって、女神が神様たちの世界に帰る、なんてこともあるかもしれない。"

    "そんな世界があるかは分からないけれど。"

    show rnk dat nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……分かった。試してみよう」"

    show mhr dat sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ありがとう、凛火。また今夜、夢の世界で」"

    hide mhr with std_out

    "海晴は満足そうに言うと、静かにライオン館を後にした。"

    "――あ。"

    "せっかく買ったペアカップを、渡しそびれてしまった。"

    show rnk dat nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「まあいいか。月曜日、学校で渡せば」"

    "私はぼんやりとそんなことを考えながら、部屋へと戻っていった。"






    $ set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    "ベッドに寝転がって、昨日からのことを振り返っていた。"

    "海晴と水族館で初デート。"

    "しかも今日は遊園地に行ってしまった。"

    "とても贅沢な週末だった。"

    "今週は特別だったけれど、時々はこんなきらきらした一日を過ごせるのかと思うと、不思議と微笑んでいた。"

    show rnk paj arm lie at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「よかったな。ちゃんと、返事をして」"

    hide rnk with std_out

    "海晴と付き合い始めてまだたった２日。"

    "これからもっと色んな特別が待っているのだろう。"

    show lete normal at cat_c with std_in


    voice get_voice_filename("cat", 15)
    lete "「にゃー」"

    "黒猫のレテが、扉の隙間から私の部屋に入ってきた。"


    hide lete with std_out

    "私は機嫌がよかったので手招きをしてみたが、ふいとそっぽを向かれてしまった。"

    "来たばかりなのにまた部屋を出て行くのかと思いきや、もう一度振り返って私を見た。"

    "まんまるの黒い目と、そのまましばらく見つめ合っていた。"

    $ add_seen_chapter("11_3-3")

    jump f011_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

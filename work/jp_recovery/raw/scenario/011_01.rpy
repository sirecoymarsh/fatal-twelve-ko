

label f011_01:








    python:
        set_info_scene("170")
        set_info_date(7, 9, "mon")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "朝。"

    "胸には、喪失感があった。"

    "ベッドでしばらくぼーっとしていると、目覚まし時計が鳴った。"

    "どうやら私は目覚ましよりも先に起きたらしい。"

    scene ecg cardbook bli with dissolve_long

    "スマートフォンに、海晴からチャットが届いていた。"

    "それは、海晴が手にしたカードの情報だった。"

    python:
        add_character_cards("rnk", ["7_name"])
        add_character_cards("mhr", ["7_name"])

    show ecg cardbook op3 with ecg_change_wait


    voice get_voice_filename("rnk")
    rinka "「ロさんって読むんだ。中国の人かな……」"

    "彼は確か、ぽっちゃりしたおじさんだったと思う。"

    "どんな人生を歩んだのか分からないけれど、きっと色んな困難を乗り越えてきているに違いない。"


    scene bg myroom morning with dissolve_long

    "私もお礼に、≪Ⅵ・氏名≫の情報を送った。"

    $ add_character_cards("mhr", ["6_name"])

    "チャンさんという女性は、20代半ばくらいに見えた。今際の際の叫びを聞いていたから、きっと幸せの絶頂だったのだと分かる。"

    "人の数だけ、人生がある。"

    "当たり前のことだけど、深く深く、胸に刻まれた。"

    "その後、海晴からはもう一つ連絡が来た。"

    "――今日から、期末テストだね。"

    show rnk paj sur su1 at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「うぐっ」"

    "思わず、こんな声が出た。"

    "連絡にはまだ続きがある。"

    "――アラン・スコーピオンとフェデリーコ・カルミナーティが脱落した今、ぼくたちは焦ることはない。期末テストを乗り切ってから、≪女神の選定≫について考えよう。"

    "昨晩の選定で、アランさんとフェデリーコさんは脱落した。"

    "海晴の言う通り、私たち二人が生き残るためにどうすればいいかというのは、これからじっくり考えればいいことなのだ。"

    show rnk paj nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「アランさん……」"

    "気になったので、私はスマートフォンでアランさんの名前を検索してみた。"

    "有名な宝石会社の社長である彼の死は、日本のニュースサイトにも取り上げられていた。"

    "ニュースでは不審死と発表された後、自殺ということにされているようだ。"

    show rnk paj nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「アランさんが自殺なんてするはずないのに……」"

    "きっとアランさんを知る人ならば、みんなそのことを分かっているはずなのだ。"

    "だが、これはもう２ヵ月以上前の話になる。今更告発しても遅いし、何より私の言葉なんて誰も聞いてくれないだろう。"

    "自分のことではないのに、私は悔しいと思っていた。"

    "それに、アランさんはこうなることを予想していた。だから問題は――。"

    show rnk paj sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「アムリタさん！」"

    "次期社長は社長が生前に遺した今後の対応策により、実妹に決定。"

    "かなり内部で揉めたらしいが、最終的にはアムリタさんが就任したようだ。"

    "兄の遺志を継ぐため、アムリタ・スコーピオンに改姓し、経営者の一人として色々な人に支えられながら、頑張っていく意向を示した。"

    "いわゆる世襲人事というものだろう。ネットの記事には、否定的な意見も多かった。"

    "だが、私には分かる。彼女はそんな反発をものともせず、前に進んでいくのだろう。"

    "記事には写真も掲載されていて、幼さは残るけれど、確かに美人だな、と思っていた。"

    "自分に似ているとはとても思えないが――アランさんにそう言われたことは、今では誇りになっている。"

    show rnk paj arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「よし」"

    "私は私の人生を、頑張ろう。"

    "日記帳は、試験が終わってから読むことにした。"

    "もうちょっとで終わるのにもどかしいが、気になることが書いてあったら、勉強が手につかなくなってしまうかもしれない。"

    "私は背伸びをしてから、学校へ行く準備を始めた。"

    $ add_seen_chapter("11_1-1")








    python:
        set_info_scene("171")
        set_info_date(7, 13, "fri")
        set_info_time("noon")
        set_info_location("08")


    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show mao uni sel lau rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「終わったー！」"

    "月曜日から金曜日までの５日間にわたる期末試験が、ついに終わった。"

    "その間は一日につき２科目だったので学校にいた時間は短いが、それでも濃い日々だった。"

    "海晴や直未は私が勉強から逃げないように、放課後は私をほとんど毎日図書室へ連れて行った。"

    "勉強を始めたのは遅かったが、勉強時間では決して他の生徒に引けをとらないと思う。"

    "今回は赤点どころか、いい線いきそうな気すらしている。"

    "もっともその代償は大きく、私は答案用紙を提出した瞬間机に突っ伏していた。"

    show rnk sun arm sad at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「つかれた……」"

    "試験最終日の今日だけはホームルームがあるので、私はそのまま先生が来るのを待つことにした。"

    "元気のない私を見つけた真央が近づいてくる気配を感じる。"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたん、ずいぶんお疲れだねぇ」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「疲れたよ。こんなに勉強したの、高校入ってから今回が初めてだ」"

    show mhr sun sco thi at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「それは……どうかと思うけれど」"

    show mao uni nor dis rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんの成績はパンダ並みだったからねぇ」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「パンダ……」"

    "１年生の前半は、高校受験の時の貯金を崩してなんとかなったが、それ以降は勉強していないので落ちる一方。"

    "真央よりも順位は大分下だったので、言い返せない。"

    "思えば去年は店長代理をやっていなかったのに、一体何をやっていたのだろうか。"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「まーでも、今回りーたんが頑張ってたのはマジだもんねぇ」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「だから休ませて……」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「それはむ～り～。ね、みはるん？」"

    show mhr sun sco con with std_change

    voice get_voice_filename("mhr")
    miharu "「ああ。今日の放課後は４人でカラオケに行くらしいからね」"

    show rnk sun sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「ええっ。４人ってことは直未も？」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「そうだよ～。明日はもうお店を開けちゃうんでしょ？　だったら、今日遊んでおかないとねぇ」"

    show mao uni nor lau rev with std_change

    voice get_voice_filename("mao")
    mao "「文化祭の時に行けなかったからねぇ。リベンジだよぉ」"

    "――文化祭。"

    "そうか、今この世界の正しい記憶というのは、文化祭で事故があり、直未が軽傷を負い、遊びに行く約束がなくなってしまった、というものだ。"

    "文化祭の次の週に真央が遊びに行くのを計画していたけれど、流れてしまった。"

    "確かに期末テストが終わったこの日というのは、時期としては一番いいかもしれない。"

    "――が、私は疲れていた。"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「や、休ませて……」"

    show mhr sun sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火の気が抜けないように内緒にしておいたんだ。ぼくとしては凛火の意志を尊重したいけれど、まずは真央を説得することだね」"

    show rnk sun nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そっちの方が疲れる、かな……」"

    "仕方ない。"

    "遊びに行くモードになった真央を説得する方がエネルギーを消費する。"

    "今日は久し振りに、遊ぶことにしようか。"







    python:
        set_info_time("night")
        set_info_location("02")


    stop music fadeout 1
    scene bg station01 night with fade_long
    play music audio.comicaldays
    pause 1

    $ show_hud()

    show rnk sun arm ama at std_cr, xoffset(-140) with std_in

    voice get_voice_filename("rnk")
    rinka "「あー、喉カラカラ」"

    show nom sun har pal rev at std_cl, xoffset(70) with std_in

    voice get_voice_filename("nom")
    naomi "「わたしもです……。真央先輩、元気過ぎ……」"

    show mao uni sel lau rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「いやぁ、今日のために昨日は早く寝たからねぇ」"

    show mhr sun nor rea behind rnk at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「でも、ちゃんと勉強もしたのだろう？」"

    show mao uni nor dis rev with std_change

    voice get_voice_filename("mao")
    mao "「………………どうだかねっ」"

    "結局、私は流されるがまま、フリータイムが終わる夜７時まで遊んでしまった。"

    "その後はみんなでご飯を食べて、駅へと来ていた。"

    "思えば、久し振りにこんなに遊んだ。"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、楽しかったな」"

    show mhr sun pai lie with std_change

    voice get_voice_filename("mhr")
    miharu "「……そうだね」"

    "私がぼそりと言うと、海晴も確かめるような口調でそう言った。"

    "真央は相変わらず歌ったり歌わなかったりでずっと盛り上がってるし、直未は最初は恥ずかしがっていたけど歌うとうまいし、海晴はそもそも歌いたがらない。"

    "カラオケでの私は特に語ることがないくらい平凡だと思うが、海晴はやけに写真や動画を撮ってきた。"

    "一応気づかれないように気を遣っているらしいが、さすがの私もそれは気づいた。"

    "まあ、その理由を私はすでに知っているのだけれど。"

    "海晴はさりげなく私に近づくと、左手の袖を軽く引っ張った。"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「……あ」"

    "真央は横目で海晴を見たようで、わざとらしく直未の腕に抱きつくと、続けた。"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「なおりんっ、うち、お店にスマホ忘れちゃったかも」"

    show nom sun que que with std_change

    voice get_voice_filename("nom")
    naomi "「……あれ、さっき使ってませんでしたっけ？」"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「気のせいじゃない？　ってことでなおりん、ついて来て。りーたんとみはるんは、先帰っててねぇ」"

    show nom sun har sur with std_change

    voice get_voice_filename("nom")
    naomi "「あ、つ、ついて行きますから引っ張らないでください～」"

    hide nom
    hide mao
    with std_out

    "真央はそう言うと、直未の手を引いて来た道を引き返していった。"

    "駅のホームには、海晴と私が残されることになった。"

    "それが何を意味するか、考える必要もない。"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「……とりあえず、場所を移動しないかい？」"

    show rnk sun nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。それなら前と同じ、東京タワーのところへ行こう」"

    "海晴と私が出会った公園の方が相応しいかもしれないけれど、あそこは夜にはもう閉園してしまっている。"

    "ライオン館は避けた方がいいと、お互いに何となく分かっていた。"

    "だから海晴が告白してくれたあの場所がいいと、私は思ったのだった。"






    $ set_info_location("03")




    stop music fadeout 1
    scene black with dissolve_long
    play music audio.growapart
    pause 1

    "移動する電車の中、私たちは何も話さなかった。"

    "ただ海晴の横に私が立って、車輪の音を聞きながら車両に揺れられていく。"

    "この時間が、頭の整理の時間でもあった。"

    "待たせ過ぎてしまった、と自分でも思う。"

    "海晴に告白されてから、２週間と４日。18日もの間、保留にしていたのだ。"

    "今日まで返事を急かさないでいてくれたということは、その分我慢させてしまったということである。"

    "私は私の責任を果たさなくてはいけない。"

    "いや、もう責任とかそういう問題ではない。"

    "私がどう思っているかを、海晴に伝えればいいのだ。"

    "――今の私の、気持ちを。"

    "私は電車に揺られながら、海晴への答えを考えていた。"

    "どんな答えを告げるかはもう、決まっている。あとはそれを、どう伝えるかが問題だった。"






    python:
        set_info_scene("172")
        set_info_location("39")

    scene bg shibakouen night:
        subpixel True
        yalign 0.3
        linear 150 yalign 1.0
    with Dissolve(3)
    pause 1

    $ show_hud()

    "私たちはこの場所に到着するまで終始無言であった。"

    "ライトアップされた東京タワーがとても綺麗で、つい見とれてしまう。"

    "夏の夜は、春の夜とはまた違った空気が流れている。"

    "何から切り出せばいいのか、正解が分からなかった。"

    "だから私は、とにかく思い立った言葉を口にした。"


    scene bg shibakouen night at yalign (1.0) with dissolve

    show rnk sun nor apo at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「まず、ごめん。今日までずっと、返事ができなくって」"

    show mhr sun nor nor rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「……構わないよ。時間がかかることは真央から聞いていたし、≪女神の選定≫や期末試験という問題もあった」"

    show mhr sun sco sh2 rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ちょっと……少し……それなりに、ええとじっくり！　考え、させて？」"

    show mhr sun sco sh1 rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……と、あの日君は言った。だからぼくは、待つことにしたんだ」"

    "海晴はどうやら、私の言葉を一言一句覚えていたらしい。"

    "反復されると、恥ずかしい。"

    show mhr sun nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくの方からも先に言っておくべきことがある。今日遊びに行ったあとにぼくたちを二人きりにするということは、真央の提案なんだ」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「それはなんとなく、分かってた」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「けれども……そ、その。返事が聞きたいと思ったぼくの気持ちも、嘘ではない」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「それももちろん、分かってる」"

    "私の袖を引っ張ったことが、海晴の本心の表れだということは分かっている。"

    "あの時の海晴には、不安と期待と緊張と、全てが入り混じっていた。"

    "意識をするだけで、今までに比べて海晴の気持ちがずいぶん分かるようになっていた。"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そしてもう一つ、先に言うべきことがある。長い話になるかもしれないけれど、聞いてくれるかい？」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん。もちろん」"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それは君もすでに所持している≪死因≫のカードのこと。ぼくがぼくを殺すに至るまでのことを、知って欲しいんだ」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「この期に及んで隠し事をしたまま返事を求めるのは、自分でずるいと思ったんだ。だからぼくのもっとも醜いところを知った上で、決めて欲しい」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくの告白を受け入れるかどうか――ぼくと付き合うかどうかを、だ」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「分かった。私も先に一つ言わせて。海晴が醜いと思っていることがどんなことでも、私はそうは思わない」"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「嫌いになることもないし、拒絶することもないし、軽蔑することもない。そんなこと、あり得ない」"

    "私が言うと、海晴は深く頷いた。"

    "きっとこんなこと、海晴と私の間ではもう、口に出さなくてもいいことなのだ。"

    "海晴が話したいと思ったから、話してくれる。だから私も、ちゃんと聞く。"


    play music audio.disclose
    scene ecg miharupasttalk serious with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「そうだね。君にぼくの昔の話をしたとき、飴茶に入ってから君に出会う話を、ほとんど省略していたと思う。その空白を、今から埋める」"


    voice get_voice_filename("mhr")
    miharu "「この話はあくまで、加害者側の話。被害者の人生を奪ってしまったことに擁護のしようはなく、被害者の家族にどれだけ恨まれようが仕方ない」"


    voice get_voice_filename("mhr")
    miharu "「君も知っている通りぼくは自分の母親が嫌いであり、尊敬できる人ではないと思っている。けれども、昔からそうだったわけではない」"

    "海晴は、そこからお母さんの昔話を始めた。海晴がどんな考え方をしているのか知るために、欠かせないのだろう。"


    voice get_voice_filename("mhr")
    miharu "「けれどもぼくは加害者の側に生まれた人間だ。加害者にだって、人生はあるから」"

    "と、前置きをして。"

    "海晴のお父さんは海晴が小さい頃、人身事故で人の命を奪ってしまった。これは、昔、私が海晴と公園で会った時に聞いたことでもある。"

    "加害者であるが、辛くないなんてことはないだろう。そしてお父さんはもちろん、人生のパートナーであるお母さんも辛かったことに違いはない。"


    voice get_voice_filename("mhr")
    miharu "「ぼくの父親、自分の夫が事故を起こしても離婚せず、過ちを共に背負い、母親はもう一度人生をやり直すために努力をした」"

    "ちょっと間を置いて、海晴は続けた。"


    voice get_voice_filename("mhr")
    miharu "「しかし、母親は変わってしまった。きっかけは恐らく父親の自殺。元々、色んな感情を押し殺してきた母親のことだ、いつ限界がきてもおかしくはなかったのかもしれないけれど」"

    show ecg miharupasttalk sad with ecg_change


    voice get_voice_filename("mhr")
    miharu "「一番の原因は悲しみ以上にきっと――裏切られたという喪失感だ」"


    voice get_voice_filename("mhr")
    miharu "「自分の人生を捧げてでも犯罪者になってしまった夫を支えようと決意をしたにもかかわらず、当の本人は人生を投げた」"


    voice get_voice_filename("mhr")
    miharu "「自分の起こした行動の結果に対する責任を、これから待ち受ける罪との戦いの日々を、捨てた」"


    voice get_voice_filename("mhr")
    miharu "「一方でぼくの母親は、父親の罪から解放されもしたんだ。自由になったといってもいい」"

    "海晴のお母さんは、新たなパートナーを探し始めたという。"

    "やがて、同じ職場の年下の男性と恋に落ちた。"

    "海晴のお母さんなら容姿がいいことに疑いの余地はないし、海晴もまたお母さんのことを年齢と重ねた苦労の割には、外見も内面も若々しいと言っていた。"

    "年下の男性と恋愛をするのも、納得ができると付け加えた。"

    show ecg miharupasttalk serious with ecg_change


    voice get_voice_filename("mhr")
    miharu "「ぼくも一度、その男性に紹介されたことがある。彼は子持ちの母親のことも受け入れ、間もなく婚約というところまできていた」"


    voice get_voice_filename("mhr")
    miharu "「この時ぼくの母親は、いつも上機嫌だった。夕食はよくぼくの好物を作ってくれたし、出かける時に服を並べて選ぶ姿は、まるで少女のように幸せそうだった」"

    show ecg miharupasttalk lie with ecg_change


    voice get_voice_filename("mhr")
    miharu "「決して裕福とは言えない家計を切り詰めて、ぼくにお洒落もさせてくれていた。ああ、ぼくはまだこの時期、母親のことが好きだった」"

    show ecg miharupasttalk serious with ecg_change


    voice get_voice_filename("mhr")
    miharu "「ぼくは自分の家が裕福ではないことを分かっているからこそ、必死で勉強し、進学校である飴茶に奨学生として入った」"


    voice get_voice_filename("mhr")
    miharu "「母親も、ぼくが大学へ行く頃には再婚して数年が経ち、家計も安定しているだろう、と見通しを立てていた」"

    "未島家にはちゃんと、将来があった。"

    "海晴のお母さんは、恋する乙女と母親をきちんと両立していたに違いない。"

    show ecg miharupasttalk sad with ecg_change


    voice get_voice_filename("mhr")
    miharu "「けれど、彼女は再び裏切られることになる」"

    "婚約指輪まで渡してきた男性は、ある時、突然別れを切り出してきたそうだ。"


    voice get_voice_filename("mhr")
    miharu "「８月、だったと思う。その男の職場に新卒で入社してきた女性社員と恋に落ちてしまった、と」"

    "この時、海晴のお母さんと男性の間にはすでに一年以上の交際期間があった。婚約までするくらいだから、短いとも言えた。"

    "だが、離れてしまった気持ちはもう戻らない。"

    show ecg miharupasttalk serious with ecg_change


    voice get_voice_filename("mhr")
    miharu "「これがぼくの母親にとって、人生で最後のイベントと言っていいだろう。これ以降、ぼくの母親は恐らく惰性で生きているだけさ」"


    voice get_voice_filename("mhr")
    miharu "「つまり母親が変わってしまったのはこの瞬間。生活は荒れ、食事を作らなくなった。ぼくの好物も忘れ、誕生日も忘れた」"

    "この言葉が正しいか分からないが、私はネグレクト、という単語を思い出していた。"

    "無関心、育児放棄であり、まだまだ親の愛が必要な子供にとっては一種の虐待ともいえる。"


    voice get_voice_filename("mhr")
    miharu "「口を開けばその女性の愚痴ばかりになり、家で酒を飲むようにもなった。派遣社員として働いていたとはいえ、自分のための必要最低限の家事しかしなかった」"

    show ecg miharupasttalk sad with ecg_change


    voice get_voice_filename("mhr")
    miharu "「人間というのは、変化に心を動かされる。これまでのぼくと母親の関係が良好であった分、ぼくは正直――辛かった」"


    voice get_voice_filename("mhr")
    miharu "「ぼくがリストカットをするようになったのは、この時期であり、この時期がもっとも自らを傷つけた」"


    voice get_voice_filename("mhr")
    miharu "「ぼくは、ぼくを見て欲しかった。好きな物を買ってもらえなくても家事をやってもらえなくてもいいから、せめて誕生日にはおめでとうの一言くらいは欲しかった」"

    show ecg miharupasttalk serious with ecg_change


    voice get_voice_filename("mhr")
    miharu "「そして同時に、母親の怒りの矛先は、男性ではなく彼を奪った女性に向いていたことが、当時のぼくには疑問だった」"


    voice get_voice_filename("mhr")
    miharu "「その女性が彼を誘惑したのかもしれない。けれど、最終的に心変わりし、母親を裏切ったのは男性の方だ。だから男性に対して怒りが向くのが自然なのではないかと、母親を理解できなかった」"


    voice get_voice_filename("mhr")
    miharu "「母親を被害者とするならば、加害者は男性で然るべきだろうと思っていた。巻き込まれた側の女性を敵視し、自分の娘の聞こえるところで聞くに堪えない言葉を言うなんて、と軽蔑の気持ちもあったかもしれない」"

    "無関心と軽蔑。海晴にのしかかる家庭内でのストレスは、それでも母親に向けられるのではなく、抱えることしかできなかったのだ。"

    show ecg miharupasttalk sad with ecg_change


    voice get_voice_filename("mhr")
    miharu "「手首を切っても承認されない。もっと傷つけばいい。その負の連鎖は中学１年生の冬からずっと続いていた」"


    voice get_voice_filename("mhr")
    miharu "「幼い頃に君と出会った経験がぼくの支柱であったのだけれど……このおよそ半年間、過負荷の状態だった」"


    voice get_voice_filename("mhr")
    miharu "「そして中学２年生のときのクラス替えで、ぼくは真央に出会った。これが、ぼくにとって一つの転換点だったんだ」"

    "当時の真央はどうやら、海晴とは違った意味で他のクラスメイトと距離を置いていたらしい。"

    "女子同士のグループとか、いじめの誘いとか、乗らないと自分が無視をされるとか、そういうことが嫌だったから。"

    "今でこそ真央は自分の意志で嫌なことを撥ね除けられるけれど、中学生の時は違ったらしい。"

    "だから離れることで、自分のやりたくないことはやらないようにしていたそうだ。"

    show ecg miharupasttalk lie with ecg_change


    voice get_voice_filename("mhr")
    miharu "「当時、真央は他人との距離の取り方が下手だった。もっとも、ぼくはそれ以上に他人との付き合いが下手だったのだけどね」"

    "真央は、海晴がリストカットしているのを見て避けることもなかったし、怒ったり説教をしたりすることもなかった。また、理解を示すこともなかった。"

    "海晴にとって、その距離が心地よかったらしい。"


    scene bg shibakouen night
    show mhr sun sco thi rev at std_cl
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「真央はぼくに、母親だからといって好きでいなくてもいいことを教えてくれた。嫌いになってもいいと」"

    show rnk sun arm sad at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「それは……真央らしいね」"

    "私が言うと、海晴は無言で頷いた。"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくはやっと、母親のことが嫌いになれた。母親の行動を客観的に見つめ、少なくとも現状は、尊敬できる大人ではないと認めることができたんだ」"

    "好きなら好き、嫌いなら嫌い。"

    "嫌いになってもまた好きになってもいいし、好きになってから嫌いになってもいい。"

    "それこそ、自分の好きにすればいいのだと。"

    "真央ならそう言うだろう。"

    show mhr sun pai ten rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それでも、ぼくは時々耐えられなくなり、手首を切ってしまった」"

    "だが、確実に頻度は激減したのだという。"

    "独りじゃないことが、海晴の支えになった。"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「高校に上がり、君と出会う。君に恋してからの一年間は、省略させてもらうよ」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん」"

    "海晴は簡潔に、この頃にはリストカットはしなくなっていたことを話してくれた。"

    "ただ、積み重ねられた傷痕は中々消えることがない。海晴はこの頃から――今も、夏になってもずっと手首を隠し続けていた。"

    scene ecg miharupasttalk serious with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「２年生になって、日辻さんが現れた」"

    "そこがもう一つの転機だと、海晴は続けた。"

    "私が直未と出会い、一緒に過ごす時間が増えていった。"

    "よく考えると、たった１ヵ月だ。それだけの期間で、一緒に遊園地に行きたいと思うほど仲良くなっていたのだ。"

    "しかし客観的に見て、直未と私との出会いは特別なものではないだろう。"

    "ありふれた日常の一幕だ。"

    "だが、海晴にとってはそうではなかった。"


    voice get_voice_filename("mhr")
    miharu "「君の隣には常に、ぼくがいたんだ」"


    voice get_voice_filename("mhr")
    miharu "「真央はぼくの気持ちを知っていたから、いつも一歩引いていた。けれど、日辻さんは違っただろう？」"

    show ecg miharupasttalk sad with ecg_change


    voice get_voice_filename("mhr")
    miharu "「単純に言えば、君が日辻さんと過ごす時間と同じ量、ぼくが凛火と過ごす時間が減ったんだ」"

    "海晴ははっきりと、そう言った。"

    "私はみんなと平等に付き合うとか、そもそもそういう意識がなかったので、悪いとは思わない。"

    "けれどそう思ってしまう海晴を悪いとも思わない。海晴がそう思うのも、今の私は理解ができるから。"




    play music audio.miharu
    scene bg shibakouen night
    show mhr sun pai ten rev at std_cl
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「ある日、女神が夢の中でこれからの運命をぼくに告げた。日辻さんは――ぼくから凛火を奪っていくと」"

    show rnk sun sur su2 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「女神……パルカが？　どういうこと……？」"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「その日、夢を見た。あれはぼくの不安が現れた夢だったのか、パルカが見せた≪可能性の世界≫の一つだったのか、今でも分からない」"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火と日辻さんが付き合っている夢を――見たんだ」"

    show rnk sun arm shy with std_change

    voice get_voice_filename("rnk")
    rinka "「わ、私と直未がっ！」"

    "いきなり出てきた言葉に、私は一瞬頭が真っ白になった。"

    "女神の話が出てきた直後に、な、直未と私が付き合っている夢。"

    "そんな可能性の世界があるのか知らないけれど、少なくとも現実ではないことは確かだ。"

    "話の腰を折っても仕方がないので、私は海晴の話の続きを待った。"

    show mhr sun sco dis rev with std_change

    voice get_voice_filename("mhr")
    miharu "「この夢を見たのが５月２日と３日の間――≪因果の刻≫」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴や、私たちが命を落とした日」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ただ、はっきりと言っておく。ぼくの自殺のきっかけは、君たちが付き合っている夢を見たことではない。君が幸せであるなら、ぼくはいずれ乗り越えることができる」"

    "海晴は、告白の返事がどちらでも問題ない、とさらに念押しをした。"

    "仮に私にフられても、再び自殺を考えるようなことは決してないと。"

    "また、その考えは当時も同じであったと、繰り返した。"

    "問題はその夢を見たときに海晴に生まれた感情だと、続ける。"

    scene ecg miharupasttalk sad with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「ぼくは、日辻直未に怒り、彼女を恨み、彼女を憎んだ。きっと、それら抗えない感情を嫉妬心と呼ぶのだろう」"


    voice get_voice_filename("mhr")
    miharu "「そしてぼくは理解した。男性に別れを告げられた時、母親の怒りの矛先が何故、巻き込まれた側の女性だったのかを」"


    voice get_voice_filename("mhr")
    miharu "「ぼくと母親は血が繋がっている。ぼくが嫌いになった母親は、ぼくの未来の可能性の一つなんだと」"

    show ecg miharupasttalk lie with ecg_change


    voice get_voice_filename("mhr")
    miharu "「ぼくはぼくを否定した。だから――死にたくなった」"

    "リストカットとは違う原因なのだと、海晴は言った。"

    "血を流すことで誰かの気を引きたい、承認されたい、そういう感情ではなかったのだと。"

    show ecg miharupasttalk sad with ecg_change


    voice get_voice_filename("mhr")
    miharu "「自分がこの世界に存在しているのが、嫌になったんだ」"


    scene bg shibakouen night with dissolve_long

    "それは、私には理解のできない感情だった。"

    "だから海晴と私は、別の人間なのだ。"

    "海晴と、だけではない。"

    "誰しもが絶対に理解し合えない部分があるからこそ、人はみんな違う体に入っている。"

    show rnk sun nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「今は、どう思っているの？」"

    show mhr sun nor ser rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「それはある意味では、≪女神の選定≫に助けられた。ぼくが自殺に成功していたことは同時に、ぼくは自分を否定できる人間だと、ぼくに自覚させた」"

    "自分ですら嫌悪する、負の感情を抱く自分。"

    "それをきちんと否定し、覚悟をもって世界から消せる人間なのだと、自覚できたこと。"

    "それは海晴にとって、一つの希望であったらしい。"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「自殺という自制心を持っているのだから生きていいと、ぼくは自分を許すことができた」"

    "だから、≪運命の大広間≫で私と会うまでは自分が最後の一人になると決意していたという。"

    "そう、補足した。"


    play music audio.growapart

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「さて、ここまでが蛇鉈海晴という人間が死に至るまでの物語――ここまで聞いてもらったうえで、答えを聞きたい」"

    "海晴は真剣な表情で、私へ向き直った。"

    "この話を私にするのは、もしかしたら告白する以上に勇気がいることだったかもしれない。"

    "直未に対して酷いことを思っていたということを、はっきり話した。"

    "私は、海晴も真央も直未もみんな好きだ。海晴もそのことを知っている。"

    "だからこそ私と一緒にいるためにも、直未は嫌いだと割り切ることはできなかったはずだ。"

    "それに海晴も、決して直未のことは嫌いではないに違いない。海晴の嫉妬心はあくまで、私が直未と過ごす時間が増えた、ということに対してだけだろう。"

    "ここまでの話をしないで私に判断させるのはずるい――その気持ちはよく分かった。"

    "それだけ私のことを本気で好きでいてくれているということ。"

    "私に対して、真剣だということ。"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「一つ、確認させて」"

    "それが分かっているから、私からも聞かなくてはならないことがある。"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「≪女神の器≫っていうのがあくまで一人で、生き残るのは一人だけって海晴は言ったけど――やっぱり私は、二人じゃなきゃ嫌だ」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「何だっていいから可能性があるなら、それに賭けたい」"

    "未だ分からない『指名者がいなくなった場合の対応』やリンダさんの『カードブックと同じ装丁の日記帳』もそうだ。"

    "足掻ける限り、足掻きたい。"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴はそのことに対して、どう思ってるの？」"

    "私が聞くと、海晴は下を向いてしばらく考えた。"

    "それは答えを躊躇っているのではなく、考えをまとめているように見えた。"

    "打算や計算のない、正直な答えが聞きたかった。海晴も、私がそう思っていることは分かっているはずだ。"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「やはりぼくの一番は君に生きて欲しいということだ。ぼく自身のことは――分からない」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「正直に言ってくれて、ありがとう」"

    "海晴は信頼に、応えてくれた。"

    "海晴なら私が欲しい答えは分かっているはずだ。"

    "――自分も考えが変わった、二人で生き残る方法を探そう。"

    "でも、海晴が答えたのはそうじゃない。"

    "選定が始まってすぐライオン館で話したときのように、思わずまた怒鳴りたくなってしまう答えだ。"

    "あの時から何も変わっていない、海晴の覚悟。"

    "だから少し、安心した。"

    "海晴はちゃんと、私の知ってる海晴だ。"

    show rnk sun nor shy with std_change

    voice get_voice_filename("rnk")
    rinka "「えっと、じゃ、じゃあ。あらためるね」"

    "いよいよとなると、私はとても緊張してしまった。"

    "顔は熱く、心臓は突然止まってしまいそうなほど痛い。"

    "目の前を見れば、きっと私よりもずっと顔の赤い海晴。"

    "自分でも、これまでしゃんとしていた自分が別人なのではないかと疑ってしまう。"

    "でも、仕方がない。"

    "これはきっと、お互いの人生を変える一言なのだ。"


    stop music fadeout 1





    menu:
        "私は海晴に――。"
        "返事をする":

            $ persistent.s17_1_seen = True
            $ grant_hear_all()
            jump f011_01.s1_1
        "返事はできない":

            $ persistent.s17_2_seen = True
            $ grant_hear_all()
            jump f011_01.s1_2

label f011_01.s1_1:







    show rnk sun arm shy with std_change

    voice get_voice_filename("rnk", 1565)

    menu:
        rinka "「わ、わ、私は――」"
        "海晴と付き合う":

            $ persistent.s18_1_seen = True
            $ grant_hear_all()
            jump f011_01.s2_1
        "海晴とは付き合えない":

            $ persistent.s18_2_seen = True
            $ grant_hear_all()
            jump f011_01.s2_2




label f011_01.s1_2:


    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk", 1566)
    rinka "「返事はまだ――できない」"


    play music audio.thebonds

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr", 757)
    miharu "「……なんだって？」"

    "海晴は目を丸くしてそう言うと、そのまま停止してしまった。"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「今夜に返事をしたら、それがどっちでも――海晴はきっと満足する」"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「宙ぶらりんな今の状況なら、海晴だって生きたいって思うでしょ？　返事は必ずするって約束は、守る。だから、守らせて」"

    show mhr sun sco sh1 rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君は……ずるいな。そんなこと言って、まだ考えがまとまっていないのだろう？」"

    show rnk sun nor shy with std_change

    voice get_voice_filename("rnk")
    rinka "「うぐっ、実はそれも……なくは……ないです……」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴のことが大切過ぎて、ちゃんと二人が生き残る方法を見つけないと、落ち着いてなんて考えられない」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……でもね。海晴が真央に頼んでまで結論を急いだのは、次の選定までに返事を聞きたかったから」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「そして満足して、私に指名されるつもりだった。私からの指名を防御して指名できなくする方法を試してみようと、嘘をついて」"

    "私が言うと、海晴は目を逸らした。"

    "海晴の本心を聞いたからこそ、分かったのだ。"

    "海晴が私を好きであれば好きであるほど、何らかの決着をつけて、私を生かすことを望むだろう。"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「悪いけど、いくら海晴だって許さない。死ぬなんて絶対――許さない」"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくのこと、嫌いになったかい？」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「なるわけ、ない。海晴こそ、結局、私が優柔不断なのがばれちゃったわけだし、私のこと嫌いになったんじゃない？」"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「正直に言うと、凛火からあの質問があった時点で、こうなることを予想はしていた」"

    show rnk sun sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「……え？」"

    show mhr sun sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「もっとも、凛火を嫌いになるなんてありえない。困ったり迷ったりする凛火も、好きだ」"

    "はっきりと言われると、また恥ずかしくなってしまう。"

    show rnk sun nor shy with std_change

    voice get_voice_filename("rnk")
    rinka "「わ、分かったから。とにかく、取引みたいで気分よくないかもしれないけどさ……」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「≪女神の選定≫が終わったら、ちゃんと返事をする。だからそれまで――生きる方法を一緒に考えよう」"

    show mhr sun sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……ああ。変わったね、凛火も」"

    show mhr sun sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、このまま死んだら、化けて出てしまうね。凛火から返事を聞けるよう、ぼくも二人が残れるよう、覚悟を決めるよ」"

    "変わったのは海晴も同じかもしれない。"

    "そう。今この瞬間、海晴は変わった。"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ただ、一つだけ確認させて欲しい。先延ばしにしているだけではなく、ぼくにもちゃんと可能性は、あるのかな？」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん。私は恋愛したことがないからまだよく分からないだけで――どっちの可能性もある」"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「どっちつかずの状態で偉そうなこと言って……ごめんね」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「構わないよ。元々、付き合おうがフられようが決着をつけるためだったんだ。だから可能性があるなら、それはいいことだ」"

    "海晴はそう言うと、長い髪を揺らして微笑んだ。"

    "夜景の光を浴びてところどころきらきらと光る。"

    "海晴は、とても可愛い。"

    "頭もいいし、器量もいい。"

    "時々嫌味も言うけど、友達想い。"

    "いつも余裕があるように見せて、いつも一生懸命なことを私は知っている。"

    "そんな海晴を見れば、やっぱり可能性がないなんて言えないな。"

    "白状すると、私は自分で言った言葉の通り、まだ迷っているのだ。"

    "あーあ、やっぱ最低だ、私。"

    "海晴じゃなかったら、きっと告白を取り消されている。"

    "そして私たちは、家へ帰ることにした。"

    "ここに来ると駅まで二人で歩かないといけないのだけれど、今夜は別に、気まずくなんてなかった。"


    $ flags_route_F = True
    jump f011_01.s2_end


label f011_01.s2_1:


    show rnk sun nor shy with std_change

    voice get_voice_filename("rnk", 1580)
    rinka "「そ、その……」"

    show rnk sun nor shy with std_change

    voice get_voice_filename("rnk")
    rinka "「付き合ってみてもいいのかなって、思った」"


    voice get_voice_filename("mhr", 766)
    miharu "「ああ、そうだよね。そもそもぼくたちは同性だ。そういったことに偏見はなくとも、自分が同性と恋愛できるかどうかは別……え？」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火、もう一度言ってくれないかい？」"


    play music audio.miharu

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「私は海晴が好き。でもそれは恋愛としての好きかどうかは分からない。でもそもそも、恋愛的な好きなんて私、知らないから」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「付き合ってみて探してもいいのかなって、思った。あれ、答えになってるかな？」"

    "海晴は口をぱくぱくさせて、その場でしばらく止まっていた。"

    "何かを言いたくて、でも言えないような様子だった。"

    "やがて、海晴からかすかに声が聞こえた。"

    scene ecg miharupasttalk shy with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「嬉しくて――死にそうだ」"

    "顔を真っ赤にして、微笑んでいる。"

    "いつもの余裕ある表情ではなく、笑ってしまうのを抑えきれないような、そんな顔だった。"

    "そんな海晴はとても可愛い、と思った。今からこの子と交際関係になるのだと思うと、自然と私もにやけが止まらなかった。"

    "気持ち悪いくらいに、ほっぺたが綻んだ。"

    "ああ、きっと私は海晴に恋をする。"

    "この時、そんな予感があった。"




    scene bg shibakouen night with dissolve_long

    "その夜は、手を繋いで駅まで帰った。"

    "この街は夜景がとても綺麗で、あたたかかった。"

    "女同士だからから、手を繋ぐことに抵抗はないはずなのに。"

    "やっぱりちょっと、こそばゆかった。"


    $ flags_route_G = True
    jump f011_01.s2_end

label f011_01.s2_2:


    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk", 1584)
    rinka "「――ごめん」"

    "私は、その一言しか告げることができなかった。"

    "海晴は一瞬、顔から色を失った。"

    "そして時間を置いて、続ける。"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr", 769)
    miharu "「ありがとう。ちゃんと返事をくれて。ぼくは――満足だ。大丈夫、心配しなくて。明日からぼくたちはまた、友達だろう？」"

    hide mhr with std_out

    "早口でそう言うとその質問の答えを待たずに、海晴は駆け足で駅へ向かって行った。"

    "追いかける資格はない。"

    "海晴が今どんな顔をしているのか、想像がついてしまうから。"

    "そんな悲しい顔にさせたのは、私だから。"

    "やっぱり、私は海晴の気持ちに応えることはできない。海晴と付き合うことはできない。"

    "そういうのはまだ分からないし、関係性が変わるのも、怖い。"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめんね……」"

    "誰もいなくなったこの場所で、私はもう一度呟いた。"

    "そして私は、ライトアップされた東京タワーを背にして、帰る。目にちらつく夜景の光を、鬱陶しく感じていた。"


    $ flags_route_H = True
    jump f011_01.s2_end



label f011_01.s2_end:






    python:
        set_info_scene("173")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "家に帰ってすぐ、私は寝る準備をした。"

    "今日は色々なことがあり過ぎた。"

    "期末試験の最終日で、真央に誘われて遊びに行って、海晴に告白の返事を――。"



    if flags_route_F:
        "正確にはしなかったけれど、とにかく、一つの結論を出すことはできた。"




    if flags_route_G:

        "した。"

        "人生で初めての彼女、というだ。"

        "彼氏もできたことないのに彼女とか、不思議だ。"

        "でも変だとは思わない。"

        "それは、海晴をも否定することになってしまうから。"

        "何より、この気持ちに嘘はないのだ。"





    if flags_route_H:
        "してしまった。"

        "そして私は、海晴のことを傷つけた。"



    "とにかく、今日はもう寝よう。"

    "明日は久し振りにお店を開けるから、朝も早い。"

    "色々と仕度も多いのだ。"

    "おばあちゃんにもメールを送ったし、あとは寝るだけ。"

    "次の選定が11回目であることが幸いした。"

    "その一度を何事もなく終えても、あともう一度猶予があるからだ。"

    "日記帳を読めないのはもどかしいが、今日はゆっくりと疲れを癒やすことに決めた。"

    $ add_seen_chapter("11_1-2")

    if flags_route_F:
        $ add_seen_chapter("11_2-1")








    python:
        set_info_scene("174")
        set_info_date(7, 14, "sat")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest

    pause 1

    $ show_hud()

    show rnk paj sur su1 at std_c with std_in

    voice get_voice_filename("rnk", 1586)
    rinka "「ん……朝だ……」"

    "朝起きて、私は背伸びをした。"

    "今日は久々に、お店を開ける日だ。"

    "準備も多いので営業時間は短めで、９時から16時頃までの予定だ。"

    "私は朝の仕度をして、１階へと向かった。"





    if flags_route_F:
        jump f011_01F
    elif flags_route_G:
        jump f011_01G
    elif flags_route_H:
        jump f011_01H
    else:
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

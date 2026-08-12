

label fTRUE:

    if not _in_replay:
        call staffroll ("ED_TRUE.mkv")

    call set_replay







    python:
        set_info_date(8, 11, "sat")
        set_info_time("noon")
        set_info_location("04")


    stop music fadeout 2
    scene bg lion01 noon with fade_longest
    play music audio.nichijo01
    pause 1

    $ show_hud()

    show mao sci sel lau rev at std_c with std_in

    voice get_voice_filename("mao", 365)
    mao "「やああああああっとこの日が来たねぇ！」"

    "ライオン館にまずやって来たのは、真央だった。"

    "夏休み真っ只中のこの日。"

    "私たちは花火大会へ行く約束をしていた。"

    show mao sci sel nor rev with std_change

    voice get_voice_filename("mao")
    mao "「なおりんは塾で忙しいし、みはるんはバイトで忙しいし、りーたんはお店で忙しいしぃで、全然時間とれなかったもんねぇ」"

    show mao sci nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「みんなで集まるの、りーたんの誕生日以来じゃない？」"

    show rnk sci nor que at std_r with std_in

    voice get_voice_filename("rnk", 1886)
    rinka "「そういえば……そうかも」"

    "最後に集まったのは、７月２７日。"

    "私自身すっかり自分の誕生日を忘れていて、普通にお店を開けていた。"

    "お店の終わり際に海晴、真央、直未がサプライズで来てくれた。"

    "どうせ忘れている、という真央の予想が大当たりした形になった。"

    "料理は海晴がここで作ってくれて、ケーキは直未がおうちで焼いてきてくれた。"

    "海晴は私の好物が分からなくて困ったということで、主にイタリアンで、とにかく色々なものを作ってくれた。"

    "そういえば、私はあまり好きな食べ物の話をしたことがなかった。"

    "その時に食べたプッタネスカというパスタは、とても美味しかった。赤かったし。"

    "直未は私が極端に甘いものが苦手なのを覚えていてくれて、甘さ控えめのシフォンケーキに、ほどよい甘さの生クリームがコーティングしてある力作だった。"

    "紅茶風味だったのは、もしかしたらダイアナが入っていた名残かもしれないというのは、考え過ぎだろうか。"

    "しかも、３人からそれぞれプレゼントまでもらってしまった。"

    "海晴からは、花束をもらった。私の好きな赤を中心とした花束だ。花瓶に入れてお店に飾ると、ライオン館をより私のお店にしてくれた。"

    "直未のプレゼントは、本だ。ハードカバーの海外小説。直未が好きな作品で、読み易いながら哲学的な要素もあるらしい。版画の挿絵も、シックな雰囲気で可愛らしい。"

    "真央からはハンドクリームなどの詰め合わせセット。洗い物が多い私は手が荒れがちなので、実用的でありがたい。それにお店に影響が出ないよう、わざわざ無香料のものを選んでくれた。"

    "どれも私のことを想ってくれたもので、とても嬉しかった。"

    "しかもその夜はおばあちゃんからも電話が来て、とても充実した一日になった。"

    show mao sci nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「あ、なおりんはおうちにある浴衣を借りるから、直接待ち合わせだって」"

    show mao sci sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ってことはあとは」"

    show mhr sci nor rea rev at std_l with std_in

    voice get_voice_filename("mhr", 942)
    miharu "「お待たせ、凛火、真央」"

    "真央が到着してから10分程経って、海晴がライオン館に来た。"

    show mhr sci sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「直未はまだ来ないのかい？」"

    show mao sci sel glo with std_change

    voice get_voice_filename("mao")
    mao "「なおりんは、現地しゅーごーだって」"

    show rnk sci nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「えっと、じゃあどういう順番にしようか？」"

    "せっかくの花火大会。"

    "私たちは浴衣で行こうと約束をしていた。"

    "私はおばあちゃんのお古の浴衣があるのでそれを着て、海晴と真央は海晴の知っている衣装屋さんから借りるそうだ。"

    "バイト先のつてで、安くしてくれるらしい。"

    show mhr sci sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火の着付けをしてから、ぼくたちの浴衣選びに付き合ってくれ」"

    show mao sci nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「そうだねぇ。ちょっと動きにくいけど、我慢してねぇ」"

    show rnk sci arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。じゃあ海晴、私の部屋で教えて」"

    show mhr sci nor con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ああ、任せてくれ」"

    "海晴は最近バイト先で浴衣の日というのがあったこともあり、着付けはばっちりらしい。"

    show mhr sci nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「真央も、行こう。凛火の浴衣姿を、崩れないうちに写真に収めてもらわないと」"

    show mao sci nor que with std_change

    voice get_voice_filename("mao")
    mao "「え、あれ、うちも。うん、珍しいなぁ、みはるん」"

    "あれから、まだ海晴に返事はできていない。"

    "海晴は急かすことはしないけれど、稀に視線が痛い時がある。"

    "私もそろそろ、どう答えるかというのはまとまっていた。"

    "あとは、時間が開いてしまったからこその、微妙な気まずさを乗り越える勇気が必要だ。"

    "勇気というのは本当に必要にならないと湧いてこないようで、あれだけ激動の日々を過ごしていたのに、告白の返事一つマトモにできない駄目な私だった。"

    "そんなことを思いながら、私は二人と一緒に自分の部屋に向かった。"






    python:
        set_info_time("night")
        set_info_location("41")

    stop music fadeout 1
    scene bg hanabitaikai normal with fade_long
    play se "fireworks"
    pause 2
    scene ecg trueend01 light with dissolve_long
    stop se fadeout 3
    pause 1
    show ecg trueend01 dark with ecg_change_wait
    pause 1


    voice get_voice_filename("nom", 651)
    naomi "「す、すごいですっ」"


    voice get_voice_filename("mao")
    mao "「綺麗だねぇ」"


    voice get_voice_filename("mhr")
    miharu "「……思わず、見惚れてしまうね」"


    voice get_voice_filename("rnk")
    rinka "「来て、よかった」"


    play music audio.relaxtime
    scene bg hanabitaikai non with dissolve_long

    "大混雑の花火大会。"

    "夕方から場所取りを始めた私たちは座る席こそ確保できなかったが、少し高台になったところから花火を眺めていた。"

    "穴場、のはずなのだが人は多く、立ち見でも混雑には変わりなかったけれど。"

    "そんなことを忘れてしまうくらい、空で弾ける音と光は魅力的だった。"

    "この日を、楽しみにしてきた。"

    "毎日ずっと考えていたわけではないけれども、それでも、この瞬間に立ち会えることに言葉を失ってしまっていた。"

    scene ecg trueend01 dark with dissolve_long


    voice get_voice_filename("mao")
    mao "「むぅー、みはるんの浴衣選びがもうちょっと早ければ、座れたかもだよねぇ」"


    voice get_voice_filename("mhr")
    miharu "「ちょっと待ってくれ。ぼくよりも真央の方が選ぶのに時間がかかっていただろう？」"


    voice get_voice_filename("mao")
    mao "「いや、昔のことは忘れたよぅ」"


    voice get_voice_filename("nom")
    naomi "「はは……」"

    play se "fireworks"
    scene bg hanabitaikai normal with dissolve_long

    "浴衣を着て出るのなんて、小学生ぶりかもしれない。"

    "あの頃は強制的に着せられて、不愛想なお人形さんになっていた記憶がある。"

    "それでも浴衣は可愛いと思っていたような、そうじゃなかったような……。"

    scene ecg trueend01 light with dissolve_long


    voice get_voice_filename("mao")
    mao "「今ってどれくらいなんだろねぇ」"

    "真央の浴衣は、結構派手な柄だ。"

    "一番年相応に見えるというか、高校生ならではというか。"

    show ecg trueend01 dark with ecg_change_wait


    voice get_voice_filename("nom")
    naomi "「まだ、半分くらいのはずですっ。きっと、今、弾を詰めている途中です！」"


    voice get_voice_filename("nom")
    naomi "「これからどどどーんって、さっきよりもすごいんだと思います！」"

    scene bg hanabitaikai non with dissolve_long

    "直未は、少し大人びて見える。"

    "お母さんの浴衣と言っていて、落ち着いている模様だからかもしれない。"

    "絶対転ぶと思ったけれど、まだ転んでいない。"

    "直未の成長、ということだろうか。"

    scene ecg trueend01 dark with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「この花火大会では、約１万5000発の花火が打ち上がるらしい。半分ということは、すでに7500発も花火が打ち上がっているみたいだね」"


    voice get_voice_filename("mhr")
    miharu "「どうだい、真央。本当に数が合っているか数えてみたらどうだい？」"

    "海晴の浴衣は、落ち着いた地の色に、これまた落ち着いた柄。"

    "スタイルと整った顔があいまって、かなり年上に見える。私と同い年とは信じられないくらいに。"


    voice get_voice_filename("mao")
    mao "「んー、来年かなぁ」"


    voice get_voice_filename("mhr")
    miharu "「くすっ。そうだね。来年もまた――」"

    "そのギャップのせいか、時折見せる笑顔がいつもの海晴よりもちょっと幼く見える。"


    voice get_voice_filename("rnk")
    rinka "「当然」"


    voice get_voice_filename("nom")
    naomi "「あ、あのー、せんぱいたち、受験では……？」"


    voice get_voice_filename("rnk")
    rinka "「うっ」"


    voice get_voice_filename("mao")
    mao "「心配性だなぁ。来られるくらいに、ちゃんと勉強してればいいんでしょっ？　余裕余裕！」"


    voice get_voice_filename("mhr")
    miharu "「同感だ」"


    voice get_voice_filename("rnk")
    rinka "「夏休み終わったら、真剣に進路考えるから……今は……」"


    voice get_voice_filename("nom")
    naomi "「あは、ははは……」"

    "直未の乾いた笑いが、虚しく響いた。"

    "そんな話をしていると、ちょっとずつ辺りがざわついてくる。"

    "後半戦がそろそろ始まる、ということだろうか。"

    play se "fireworks"
    show ecg trueend01 light with ecg_change_wait


    voice get_voice_filename("mao")
    mao "「おおっ」"


    voice get_voice_filename("nom")
    naomi "「すごいですっ」"

    play se "fireworks"
    scene bg hanabitaikai normal with dissolve_long

    "後半戦は、前半よりもさらに派手に激しくなっていった。"

    "私たちは空にずっと、視線を奪われていた。"


    voice get_voice_filename("nom")
    naomi "「ふぎゃっ」"


    voice get_voice_filename("mao")
    mao "「あちゃー……」"

    scene bg hanabitaikai non with dissolve

    "花火の切れ間に聞こえたのは直未の焦った声と、真央の呆れた声だった。"

    "気づけば私たちの隣から消えていて、離れようとしていたみたいだ。"

    "ばつが悪そうな顔の真央と目が合うと、真央はぺろりと舌を出してみせた。"

    "ごまかしのつもりだろうが、ごまかせていない。"

    "その意図はもう、すっかり分かってしまっている。"

    "あーあ、もう。"

    "結局お膳立てされちゃうんだ、私は。"

    "自分が情けなくなりつつ、隣にいる海晴を見上げた。"

    "海晴も当然二人に気づいているのだろうけれど、空に残った煙を見つめていた。"

    "顔を真っ赤にして、時々視線だけこちらに向けてくる。"

    "私よりもずっと、そういうことに敏感な海晴だ。"

    "気づかないはずがないのだ。"

    "私の方が恥ずかしくなって、一度顔を反対側に向ける。"

    "そこには、隠れる気のない真央と直未が緊張の面持ちで見守っていた。"

    play se "fireworks"
    scene bg hanabitaikai normal with dissolve


    voice get_voice_filename("rnk")
    rinka "「ふぅー」"

    "小さく息を吐いて、小さく息を吸う。"

    "あの夜が海晴の一世一代の大勝負ならば、この夜が私の大勝負。"

    scene ecg trueend02 normal with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「……海晴」"

    "私は海晴に向き直り、名前を呼んだ。"

    scene ecg trueend03 normal with dissolve


    voice get_voice_filename("mhr")
    miharu "「……なんだい？」"

    "ぎこちない動作で振り向きながら、海晴はそう答えた。"

    "伝えたいことは、決まっている。"

    show ecg trueend02 normal with dissolve

    "私は。"

    if not (persistent.MIHARU_clear and persistent.UNHAPPY_clear):


        voice get_voice_filename("rnk", 1895)
        rinka "「――――」"
    else:




        voice get_voice_filename("rnk", 1896)
        rinka "「私も大好きだよ、海晴」"


    "その時偶然にも、この日一番大きい花火の音が上がった。"

    show ecg trueend03 normal with ecg_change_wait



    if not (persistent.MIHARU_clear and persistent.UNHAPPY_clear):
        voice get_voice_filename("mhr", 3001)
    else:
        $ grant_achievement("say_answer")
        voice get_voice_filename("mhr", 3002)
    miharu "「……ああ」"

    "きっとこれも、運命なのだろう。"





    $ renpy.end_replay()
    $ add_seen_chapter("13-2")

    call show_ending_image ("gui/TRUEEND.png", True)

    $ persistent.TRUE_clear = True
    $ grant_achievement("ending_01")
    $ grant_end_comp()

    return




    voice get_voice_filename("rnk")
    rinka "「ごめん。やっぱり私たち、親友だ」"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

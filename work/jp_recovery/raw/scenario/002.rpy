

label f002:




    python:
        set_info_scene("11")
        set_info_date(5, 7, "mon")
        set_info_time("emorning")
        set_info_location("05")







    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "今朝の目覚めは、憂鬱というのが一番的確だ。"

    "反面、全く寝た気はしなかったけれど。"

    "そして私は、忘れていたことをいくつか思い出したのだ。"

    "５月２日の水曜日、ライオン館に行く前に直未と私は一緒に下校をしていた。"

    "その時、火事に巻き込まれた。だから私の≪死因≫はきっと≪焼死≫。"

    "夢ではなく、事実のはずだ。"

    "というのも、どうやら体の方にはっきりとその瞬間の記憶が染みついていたらしく、火事に巻き込まれたことを思い出した時、しばらく体の震えが止まらなかったのだ。"

    "電車に乗っていた私たちは、突然の火事に巻き込まれていた。直未が助かったのを確認して、安堵した記憶がある。"

    "火事の原因は――分からない。思い出そうとすると、また体が震えるだけでなく、頭痛もする。"

    "鍵の形のチャーム、そしてそれがついたリュックサックだけが、何故かはっきりと脳裏に焼き付いていた。"

    "意識を失った――死んだ直後、パルカと名乗った少女と出会ったことも思い出した。"

    "彼女の言う通り、昨晩パルカのした説明は全て私が一度聞いたものであったはずだ。"

    "話を聞いた場所はきっと、パルカの言う≪夢の世界≫とやらなのだろう。"

    "これらの記憶のピースを繋ぎ合わせると、昨晩の夢を信じざるをえない。"

    show rnk paj nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「駄目だ、分からない……」"

    "とはいえ、私の結論はこれであった。"

    "あれが夢ではなかったとして、何一つ理解したことにはならないのだ。"

    "電車で起きた火事についても調べてみたが、その日の環状線にはボヤ騒ぎ一つ記録がなかった。"

    show rnk paj arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「なかったことに、なってる――。パルカはそう言っていた」"

    hide rnk with std_out

    "私が≪選定≫の参加者だから、死因となった火事自体がなかったことになっている。"

    "そう考えるほかはない。"

    "本棚を見ると、変わらない位置にその本は置かれていた。"

    "この本は≪運命の大広間≫で見たのと同じものなのだろうか。だとすれば、本がひとりでに夢と現実を行き来したというのだろうか。"

    show rnk paj arm ang at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あーもう、考えてもラチがあかない」"

    scene ecg cardbook op3 with dissolve_long

    "カードは依然、４枚のままだった。"

    "――４枚？"

    "それはおかしい、と思った。"

    "パルカは情報を集めれば自然とカードができると言っていた。概念が実存になることの象徴らしい。"

    "私の≪死因≫のカードがないのだ。"

    "そして、もう一つ。"

    "あの場所には、海晴がいた。海晴も選定の参加者であるということ。カードが割り振られているということ。"

    "私は海晴の名前を知っている。未島海晴。だとすれば、カードが増えていてもおかしくはないはずだ。"



    scene bg myroom morning
    show rnk paj nor que at std_c
    with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「他に何か条件があるのかな……？」"

    "いや、問題はそんなことではない。"

    "無意識に考えないようにしてきたが、もう逃げるのはやめよう。"

    "≪女神の選定≫が１人しか残れないというのであれば――。"

    show rnk paj arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴か私、どちらかしか生きられない」"

    "とはいえ、海晴と話したい。"

    "海晴は私の見た夢なんて知らなくて、全部が私の妄想だったって可能性もまだ――限りなくゼロに近いかもしれないけれど――なくはない。"

    hide rnk with std_out

    "私は観念して、学校へ行く仕度を始めた。"

    "朝食を食べようと思ってパンを焼いたが、口にすることができず冷蔵庫にしまった。"







    python:
        set_info_scene("12")
        set_info_location("08")
        set_info_time("emorning")

    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show mao uni nor lau rev at std_cl
    with std_in

    voice get_voice_filename("mao")
    mao "「あ、おはよーりーたん」"

    "教室に着くと、すでに真央がいた。"

    "私立飴茶女子大学付属高校。通称“アメジョ”だ。"

    "幼稚園から大学まで設置されている伝統ある学校らしい。中学までは共学で、高校からは完全な女子大学に変わる。"

    "お嬢様学校とよく勘違いをされるが、キリスト教系のよくある幼稚園からずっと女子校であるようなところに比べると、実態は都内でよくある進学校だ。"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「昨日は楽しかったよねぇ」"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「うん……。楽しかったね」"

    "真央からそう言われて、私は元気に返事をすることができなかった。"

    "どうしても、あの夢のことがちらつく。"

    "ここにいる私は、本当は死んでいるはずの私――なのだろうか。"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「元気ないぞ～、りーたん！　疲れちゃった？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「そうかも。結構歩いてたし」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「うちも昨日は疲れてすぐ寝ちゃったよ～。だから今朝はちょー早起きだったのだよ……」"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「だから月曜日なのに遅刻しなかったんだね」"

    show mao uni nor glo rev with std_change

    voice get_voice_filename("mao")
    mao "「まるでうちが月曜日はいつも遅刻してるみたいな言い方だねぇ。違わないけど」"

    hide rnk
    hide mao
    with std_out

    "真央と話していて、私は少し元気が出てきた。"

    "夢が事実であれ、今の私にやれることは分からない。だったら、普通に過ごす方がいいのかもしれない。"

    "少なくとも、海晴とちゃんと話すまでは――。"

    "だが私の気持ちの裏をかいたかのように、この日、始業時間になっても海晴は登校してこなかった。"







    $ set_info_time("noon")

    scene bg schoolroom noon with fade_long
    pause 1

    $ show_hud()

    "放課後になっても、結局海晴は来なかった。"

    "チャットを送ってはみたが、既読すらつかなかった。"

    "あの夢のこともあり心配に思っていた。しかし、その心配は真央が私の席の方まで来てすぐに解決した。"

    show mao uni sel irr rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「みはるん、今日体調不良だったんだってさ～。もう良くなったから、バイトには行くみたいだけど」"

    show rnk uni sur su1 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「え？　返事来たの？」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「おうっ。ソッコー来たよ？」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「私の方、既読にすらならないんだけど……」"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「ああー、いや、なんでだろうねぇ。気付かなかったんじゃないかな？」"

    "とぼける真央に、私は不服そうな顔を作って見せた。"

    "真央は目を逸らしたが、私はじっと見ていた。視線が泳いでいたが、すぐに私と目が合った。"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「二人の間にさ、昨日、何かあった？」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……？　昨日……？」"

    "真央から言われた私は、つい聞き返してしまった。"

    "まさか、真央はすでに海晴から何かを聞いている――？"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「パレードの時、二人きりだったよね？」"

    "そこまで聞いて、私は肩の力を抜いた。"

    "これは、パークでの話だ。"

    "それならそれで、昨日は大しておかしなことはなかったと思うけれど。"

    "しかし真央の表情はどこか真剣だった。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「うちさ、みはるんが悩んでるって知ってるんだよね」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……何に？」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「さあ？」"

    "一変して真央はとぼけた顔に変わる。"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「ええっ？　教えてくれないの？」"

    "真央が真剣な表情をするのは珍しいので、身構えていたというのに。"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「教えてもいいんだけどさ、みはるんの悩みって、りーたんにしか解決できないからね～」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「私にしか？」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「んじゃ、また明日～」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「ええっ、ち、ちょっと！」"

    hide mao with std_out

    "私の制止も聞かず、真央は教室を去っていった。"

    "部活をやっていない真央だが、放課後はさっさと帰ることが多い。"

    "ヒマだから、とうちに来ることは実はそう多くない。何をやっているのかは「色々ね～」とはぐらかして教えてくれない。"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴……」"

    "海晴の悩みとは、一体なんなのだろうか。"

    "昨日のパークで何か言いたげだった海晴の姿を思い出した。"

    "直後に見た選定の夢。無関係だとは考えにくいと今更ながらに思った。"

    "そういえば、バイトには行くみたいと真央は言っていた。なるほどそういうことかと、私は納得していた。"

    "真央はなんだかんだ、親切だ。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、海晴のバイト先はなぁ……」"

    "心の中で、思わずそう呟いていた。"

    "どこでバイトしているのかも、お店の名前も知っているが、行きにくい。"

    "飲食店と言えば飲食店ではあるのだけれど。"

    "真央がついて来てくれれば大丈夫な気もするけれど、あの調子では駄目そうだ。"

    "うーんとしばらく考えて、私はスマホのチャットを開いた。"






    python:
        set_info_scene("13")
        set_info_time("evening")
        set_info_location("09")

    stop music fadeout 1
    scene bg maidcafe with fade_long
    play music audio.maidcafe
    pause 1

    $ show_hud()

    show nom gun que que rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「あの……先輩ってこういうところによく来るんですか？」"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「私も初めて。海晴がここでバイトしてるから、話したかったんだけど……」"

    "海晴のバイト先は、秋葉原にあるメイド喫茶だ。"

    "大手ではなく個人経営のため、アイドルのような売り方をしているメイド喫茶ではなく、店員がメイド服を着ているだけのようだが、それでも入るのには抵抗がある。"

    "特に私一人で入る勇気はなかった。直未には申し訳ないが、無理を言って一緒に来てもらったのだった。"

    "お客さんも見事に男性ばかりで、私たちはとても浮いているように思えた。"

    scene ecg miharumaid nor with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「凛火……。君はもう少し女心を学んだ方がいい」"

    "海晴はひどく疲れ切った声でそう言うと、注文した≪ほっとこ～ひ～≫を持ってきた。"

    scene bg maidcafe
    show rnk uni nor apo at std_cr
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「何か、ごめん。ちょっと話したくて……。いてもたってもいられなくなっちゃってさ」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「チャットも既読にはならなかったけど、真央がバイトには出てるって言うから……」"

    show mhr mai sco thi rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「やっぱり真央か。ちょっと今朝は体調が悪くてね。真央からチャットが来たのは朝でその時にバイトは行けそうと返したんだ。凛火が送ってくれたのは午後だよね？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。昼休み」"

    show mhr mai sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「充電を忘れてしまったから、電源を切って充電していたんだ。しかし、凛火からの連絡を見落とすとは大きな失敗だね。普段はほとんど連絡してくれないのだから」"

    scene ecg maidcafe nor large:
        subpixel True
        zoom 1.8
        align (0.0, 1.0)
        xoffset -200
    with dissolve_long
    play se "set_glass_down_on_table"
    with quake_fast

    voice get_voice_filename("mhr")
    miharu "「あ、そうだこれもだったね」"

    "海晴は思い出したように、『ふわふわここあ』を直未の前に置いた。"

    "手が滑ってしまったのか、グラスをコースターから外れたところに勢いよく置いてしまったせいで、どんと大きな音がなった。"

    "一部のお客さんもびっくりして振り向いていた。"

    show ecg maidcafe nor large:
        easein 0.3 xoffset 0.0 yalign 0.2


    voice get_voice_filename("nom")
    naomi "「ひっ」"

    scene ecg maidcafe nor with dissolve


    voice get_voice_filename("mhr")
    miharu "「おっと、これは失礼したよ」"

    "海晴は直未の方を向き、小さくお辞儀をした。"

    "謝られた直未の方がびくっと肩を震わせていた。"


    voice get_voice_filename("mhr")
    miharu "「凛火はライオン館みたいに落ち着ける喫茶店を想像していたのかもしれないけれど、あいにくこの調子でね。もっとも、メイド喫茶という時点で分かって欲しかったけれど……」"


    voice get_voice_filename("mhr")
    miharu "「話があるなら、仕事の後にライオン館へ寄るよ。凛火がよければ、だけれどね」"


    voice get_voice_filename("rnk")
    rinka "「ああ、うん。それで大丈夫……。なんか、ごめん」"


    scene bg maidcafe large:
        yalign 0.2
    show rnk uni nor smi up at std_c
    with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「でもさ、初めて見たけど似合ってるよね、メイド服。元が可愛いからかな、すごく目立ってるし」"

    stop music fadeout 1
    scene ecg miharumaid shy
    with dissolve_long
    play music audio.miharu




    voice get_voice_filename("mhr")
    miharu "「似合っ……てる……。可愛い……。照れるな。まさか凛火からそんなことを言ってもらえるなんて」"

    "海晴は珍しく、顔を赤らめていた。"

    "きっとお客さんには、可愛いなど言われ慣れているだろうに。同級生が来てしまい、恥ずかしいというのもあるかもしれない。"

    show ecg miharumaid bit with ecg_change

    voice get_voice_filename("mhr")
    miharu "「愛嬌を振り撒いていれば高い時給をもらえるから選んだけれど、それだけでも、このバイトをしてよかったというものだよ」"


    voice get_voice_filename("nom")
    naomi "「あの、そんなこと言って……他のお客さんに……」"

    "直未がそう言うと、店内の他のところから笑いが起こった。"

    show ecg miharumaid bit with ecg_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。ご覧の通り、ぼくは元々こういう営業の仕方をしているからね。問題ないのさ」"


    voice get_voice_filename("rnk")
    rinka "「……海晴らしいね」"

    "色々なお店の在り方があるのだなぁ、と感心しつつ、この空気は苦手だと思っていた。"



    stop music fadeout 1
    scene bg maidcafe
    show mhr mai sco wic rev at std_l
    with dissolve_long
    play music audio.maidcafe



    voice get_voice_filename("mhr")
    miharu "「じゃあ、ゆっくりするといい」"

    "海晴は営業スマイルを浮かべて、仕事に戻っていった。"

    show nom gun hes sor at std_r with std_in

    voice get_voice_filename("nom")
    naomi "「あの……わたし、来てよかったんでしょうか」"

    show rnk uni arm sad rev at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「私も同じこと思ってる。可愛い服目当てで女子のお客さんもいるのかと思ったけど、全然だね」"

    show nom gun har ser with std_change

    voice get_voice_filename("nom")
    naomi "「いやっ、あのっ、そうじゃなくて……」"

    "煮え切らない直未をよそに、私はコーヒーに口をつけた。"

    "私たちは注文した飲み物を急いで飲み、退店することにした。"

    "その後は電車で途中まで一緒だったが、私が新宿で降りたところで別れた。"







    python:
        set_info_scene("14")
        set_info_time("night")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "夜９時頃になって、私は閉店の準備を始めていた。"

    "今日はお店を開けたのが遅かったので、お客さんは少なかった。"

    "おばあちゃんがいて料理も出していた頃は、夕食を食べに来る人も多かったが、今は食事メニューはほとんどないから仕方がない。"

    "それでも落ち着く場所でお喋りを楽しみたくて来てくれる人がいるのは、嬉しいことだった。"

    "ちなみに、ライオン館の経営状況は全ておばあちゃんが田舎の方から把握していた。"

    "実際の発注は私が行うのだが、一日のレポートを見て、詳細な指示が送られてくる。"

    "おばあちゃんは田舎にノートパソコンを持ち込んでいるのだ。"

    "あの歳で、私よりもよっぽどＩＴ関係に詳しい。"

    "片付けも一通り終えたところで、店の扉が開いた。からんからんというベルの音に、私は入り口を見た。"


    play music audio.miharu

    show mhr uni sco smi rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「やあ、凛火」"

    "学校の制服に着替えた海晴だ。メイド服を思い出して、少しにやけそうになってしまった。"

    "普段の姿からは想像がつかないけれど、とても似合っていたからだ。海晴は背が高くてスタイルもいいので、何を着ても似合うだろう。"

    "だが海晴も仕事でやっているのだし、笑うのは失礼だ。"

    show rnk uni arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……お疲れ様。バイト長引いた？」"

    show mhr uni sco sh1 rev with std_change

    voice get_voice_filename("mhr")
    miharu "「すまないね。引き継ぎ予定だった子がドタキャンしてしまったから、長引いてしまったんだ」"


    show rnk uni arm nor with std_change
    voice get_voice_filename("rnk")
    rinka "「ふぅん、よくないよね。バイトとはいえ、仕事なんだから」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「仕事が楽な割に時給が高いからね。正直、ぼくみたいに稼がないと困るって子の方が珍しい。大半はお小遣い稼ぎだからね」"

    show mhr uni nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、それにしても凛火が言うと説得力があるね」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴が言っても同じだよ」"

    "海晴は家庭の事情で、バイト代が生活費の多くを占めているそうだ。学費は特待生をとったため、全額免除。"

    "詳しいところは私も知らないが、両親が離婚して、今はお母さんとの二人暮らしらしい。そのお母さんも体調を崩しがちで、中々安定した収入が難しいようだ。"

    "私は仕事をしていると言ってもお金のためではないし、何よりおばあちゃんによって生活が支えられているので海晴ほどの切実さはまだない。"

    "おばあちゃんも、実際のところ主な収入は不動産によるもの、と言っていたことがある。詳細は聞いても教えてくれなかったけれど。"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それで……ぼくと話したかったんだよね？　何だい？　ぼくは期待してもいいの？」"


    show rnk uni arm sad with std_change
    voice get_voice_filename("rnk")
    rinka "「分かってるでしょ。長くなるから、座りなよ」"

    hide rnk with std_out

    "私は片付けの手を止めてエプロンを外し、客席の方へ移動した。"


    stop music fadeout 1

    show mhr uni nor smi with std_change

    voice get_voice_filename("mhr")
    miharu "「長くなんてならないよ。この話はすぐに終わる」"

    "海晴は座ろうとする私を制して、続けた。"


    play music audio.growapart

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「夢の世界――≪女神の選定≫というのはぼくも見た。だからぼくたちが死んでしまっているのは事実だ」"

    $ add_character_cards("mhr", ["1_name"])

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「どうやら君は、その詳細を覚えていなかったみたいだけれど」"

    show rnk uni arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……あの後、思い出したよ。まだ記憶はぐちゃぐちゃしてるけど、女神とかいう女の子に会ったのは、昨日が初めてじゃないことも」"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、なら話が早い。必ず――生き残ろう」"

    "海晴は微笑みを浮かべながら、そう言った。"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「どうして笑えるの？」"

    "その表情を見て、私はつい感情的になってしまった。"

    "海晴が≪女神の選定≫というのを事実と言ったことで、興奮してしまっていた。"

    "あの夢を見たときからずっと抑えていたものが、溢れ出しそうだった。"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「簡単さ。君はぼくが参加していなかったのならば、『生き残る』と決意できたよね？」"

    show mhr uni pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火は優しいから、それを口にすることはぼくが本来の運命に戻る――死ぬのだと認めてしまうと心を痛めている。そして、そんな選択肢は選べないと思っている」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「でも、いいんだよ。だってこの命は君に捧げようと思っている」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「――――は？　海晴、何を？」"

    show mhr uni pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「簡単なことだよ。ぼくは凛火か自分のどちらかしか生きられないとなったら、迷うことなく凛火の命を選ぶ」"

    show rnk uni ang an2 with std_change

    voice get_voice_filename("rnk")
    rinka "「ふざけんなよ……そんなこと言わないでよ！」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「気軽に言うことじゃない……そんなの。冗談でも、やめてよ……」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめん……怒鳴った」"

    "私は海晴から視線を逸らして、息を整えた。"

    "海晴は首を振ってからゆっくりと口を開いた。"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「覚悟があるから言えるんだ」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それに、選定の参加者は全員が生に固執していると言っていいだろう。甘いことを言っていたら君は――死んでしまう」"

    show rnk uni nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「……海晴は、どうして冷静でいられるの？」"

    "海晴も選定の参加者ならば、考えたくないけれど――死因が必ずあるはずなのだ。"

    "死の瞬間が記憶に焼き付いているということ。"

    "私は記憶が抜け落ちるほどにショックで、未だに実感が湧いていないというのに……どうして海晴は落ち着いていられるのか分からなかった。"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君のためさ」"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「今日話せてよかった。やはり君は、きっと他の参加者を出し抜いたりすることはできない」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくの情報は凛火には教えないでおこう。狙われるリスクが増えるのは嫌だからね」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「学校では、普通でいよう。君は生き残るのだから、日常に支障が出てはいけない」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火も最大限の努力をしてくれ。君が死んだらその時点で、ぼくの脱落は決まったようなものだ」"

    show mhr uni sco thi with std_change_wait

    "海晴は淡々と言うと、そのまま私に背を向けた。"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「必ず、君を守る――」"

    hide mhr with std_out
    play se "bell02"

    "ドアのベルが鳴り終わり、海晴の背中が見えなくなってしばらくしてからも、私は何も言うことはできなかった。"

    "海晴は≪自身のカード≫を３枚とも取得しているのか、どうして私は海晴のカードを持っていないのか……聞かなければいけないことは、後になって思い出した。"





    stop music fadeout 1
    scene black with dissolve_long
    pause 1

    "そしてこれから２度目の選定が始まるまでの間、私は進展も後退もない日々を過ごしていた。"

    "直未には少しずつコーヒーの淹れ方を教え始め、海晴や真央とは今までと同じように会話をし、からかわれたりしていた。"

    "だが、この日常の中で私は、胸につっかえた何かが解消されることはなかった。"

    "女神の選定の参加者になってしまったという事実は、徐々に重みを増していくのであった。"

    $ add_seen_chapter("2-1")











    python:
        set_info_scene("15")
        set_info_date(5, 9, "wed")
        set_info_time("night")
        set_info_location("10")


    $ show_hud()

    scene black
    pause 4

    play music audio.badguys fadein 5    
    scene ecg chinarest federico boutou large:
        subpixel True
        zoom 0.8
        align (0.5, 0.1)
        yoffset -400

        linear 20.0 yoffset 0
    with dissolve_longest

    $ persistent.fed_botou_seen = True

    pause 1

    "生きる価値のない悪人、オレには自分がそのうちの一人であるという自負があった。"

    "イタリア南部の田舎でマフィアをやってたオレは、盗みから始まり殺しまでやって、何人も裏切って見捨ててきた。"

    "下っ端ではあったが、マフィアという裏の世界でオレは勝ち続けてきたんだ。"

    "だが、このまま順風満帆かと思われたオレは大事なところでポカをやらかして命を落としちまうハメになった。"

    "勝たなくても負けなきゃいいっていう悪人の世界の中で、初めての敗北。イコール死、だ。"

    "しかし、幸運の女神とやらは善人にも悪人にも平等にやって来るらしい。"

    "女神の選定の参加者になったことで、オレは生き残る――いや、≪生き還る≫チャンスを得た。"

    "生きる価値がないのと生きたいって意志は全くの別物だ。生きるために価値なんて必要ない。ただ自分がよければそれでいい。"

    "オレ――フェデリーコ・カルミナーティはそうやって生きてきた。"

    "だからこそ、オレはもう敗者にはならないと決めた。"

    "にもかかわらず、オレが死んじまったのをいいことに今度は不幸の神様がやって来ちまった。"

    scene ecg chinarest odetto ama with dissolve


    voice get_voice_filename("ode")
    odette "「おい、お前、何ぼーっとしてやがんだ？」"

    "こいつの名前はオデット・マランソン。"

    python:
        gameinfo_cardbook_fed_unlocked = True
        gameinfo_cardbook_ode_unlocked = True
        add_character_cards("fed", ["11_name"])
        add_character_cards("ode", ["11_name"])

    "オレと同じく≪女神の選定≫の参加者だ。"

    "本来なら蹴落とし合う関係にあるのだが、オレたちは協力関係を結んでいる。"

    "いや、正確には一方的に結ばされていたと言っていいだろう。"

    scene ecg chinarest federico ser with dissolve

    voice get_voice_filename("fed")
    federico "「別に、考え事をしてただけだ」"

    scene ecg chinarest odetto nor with dissolve


    voice get_voice_filename("ode")
    odette "「いいからそんな暇があったら食えよ、カプリコーノ。せっかくの中華料理だ」"


    scene ecg chinarest odetto nor large:
        align (0.6, 0.25)
    with dissolve

    "オデットにはオレのことを『カプリコーノ』と呼ばせている。これはコードネームのようなものだ。オレの星座からとっている。"

    "オレはオデットのことを『ヴィエルジュ』と呼ぶようにしている。フランス語の発音はイタリア人のオレにとっては少し言いにくい。"

    "コードネームで呼び合うのは、オレの提案だった。"

    "≪氏名≫とは女神の選定で相手を蹴落とすための情報のひとつであるからだ。"

    "そして一応は、お互いの名前を知らないことになっている。"

    "オデットのことだからオレの本名の情報をすでにつかんでいるかもしれないが、知っていたとしても呼ぶことはないはずだ。"

    "オレもオデットの名前を知ってはいるが、そのことは言っていない。こうして牽制し合うことで、協力関係は成り立っているのだ。"



    scene ecg chinarest odetto smi with dissolve

    voice get_voice_filename("ode")
    odette "「しかし、ここが北京でよかった。中華料理の中で、あたしは北京料理ってのが一番好きだからね」"

    show ecg chinarest odetto kno with ecg_change

    voice get_voice_filename("ode")
    odette "「元々が清王朝の宮廷料理だからな。タレの味が丁寧なんだ。それに寒い北京の気候に合わせてカロリーが高い。味も重要だが、あたしみたいな海の女にゃカロリーが必要だ」"

    show ecg chinarest odetto smi with ecg_change

    voice get_voice_filename("ode")
    odette "「特にこの北京ダックっていうのは中国の最大の発明じゃないかと思ってる。脂が美味いんだ」"

    show ecg chinarest odetto kno with ecg_change

    voice get_voice_filename("ode")
    odette "「フォアグラ用のガチョウといい勝負なくらいの残酷な飼育法だが、こう美味いんじゃ仕方ない。まずく生まれ変わるしか道はねぇからな」"

    "そう言いながら、オデットは口の中にバクバクと料理を放り込んでいく。"

    "これで北京ダックは３皿目だ。間には水餃子や饅頭などを挟んでいる。"

    "コース料理を美徳としているフランス人の注文の仕方とは思えない。"

    "何より見ているこっちが胸やけしてしまいそうな食べっぷりだ。"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("ode")
    odette "「ま、つまりだ。世界で１番の料理がフランス料理なのは動かないが、中華料理には２番を与えてやってもいい」"

    scene ecg chinarest federico ser with dissolve

    voice get_voice_filename("fed")
    federico "「待てヴィエルジュ。お前の言葉には苦言を呈したい。２番以下はどこに譲ってもいいが、１番はイタリアンだ」"

    scene ecg chinarest odetto smi with dissolve

    voice get_voice_filename("ode")
    odette "「よしいいだろう。じゃあ今から腕っぷしのいい中国人を呼んできて、フランス人、イタリア人、中国人の中で勝った国の料理が世界一だ」"

    scene ecg chinarest federico ama with dissolve

    voice get_voice_filename("fed")
    federico "「待て待て、分かった――いや分かってはいないがこの話題はやめてくれ」"

    "オデットならそういうこともやりかねない。しかも、どんなに腕っぷしの強い奴を連れて来ても勝つのはこの女だ。"

    "素手で単純に殴り合ったら、男ですらオデットに勝てる奴は少ない。海の男たちの間で長年頭領をやるってのはそういうことだ。"

    scene ecg chinarest odetto nor with dissolve

    voice get_voice_filename("ode")
    odette "「さてフェデリーコ、酒はいるか？　このショウコウシュってのは溶かした飴みたいで中々美味いぞ？」"

    $ add_character_cards("ode", ["3_name"])


    voice get_voice_filename("fed")
    federico "「オデットあんた……あ」"

    "ついのせられて、オレは彼女の名前を口にしていた。"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("ode")
    odette "「さっきお前が何を考えてたのか知らないが、無意味な牽制はもうやめねぇか？」"

    scene ecg chinarest federico ser with dissolve

    voice get_voice_filename("fed")
    federico "「どういう意味だ？」"

    "オレは言いたいことが分かっていながら聞き返す。"

    "オデットは紹興酒を一気に飲み干してから、不敵に笑って答えた。"

    scene ecg chinarest odetto nor with dissolve

    voice get_voice_filename("ode")
    odette "「さあな。だがこの≪女神の選定≫とやらでよ、≪氏名≫って情報は一番すぐに分かる情報じゃねーか」"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("ode")
    odette "「お前はコードネームで呼び合うことを提案したが、意味ねえんだ。調べれば分かることだからな」"

    show ecg chinarest odetto kno with ecg_change

    voice get_voice_filename("ode")
    odette "「死因もそうだ。自分の死んだ時間におおよその見当がついているから、時間をかけて調べれば自ずと知ることができる。特にあたしとお前なんか……な」"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("ode")
    odette "「言いたいことは分かるな？」"

    scene ecg chinarest federico ser with dissolve

    voice get_voice_filename("fed")
    federico "「馬鹿にするな。この≪選定≫は≪未練≫を探り合う情報戦ってことが言いたいんだろ？　それくらいは分かってる」"

    scene ecg chinarest odetto smi with dissolve

    voice get_voice_filename("ode")
    odette "「分かった上でコードネームを使うってんだからお前は小物なんだよ。≪氏名≫なんて捨てろ捨てろ」"


    voice get_voice_filename("fed")
    federico "「だが、全員分の≪未練≫はカードでランダムに配布されてるじゃねえか。誰かがオレたちの≪未練≫のカードを持っているはずだぜ？」"

    show ecg chinarest odetto nor with ecg_change

    voice get_voice_filename("ode")
    odette "「初期カードはランダムなんだから、都合よくあたしらの情報を３枚揃えられるわけじゃない」"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("ode")
    odette "「１回目の選定で誰もあたしらを指名しなかったんだから、運よく揃った奴はいないってことが明らかになってる」"

    show ecg chinarest odetto ama with ecg_change

    voice get_voice_filename("ode")
    odette "「あのインド人も、あたしらのカードを入手したわけじゃなさそうだしな。もしそうなら、やれる奴からやってった方が得だ」"

    scene ecg chinarest federico ave with dissolve

    voice get_voice_filename("fed")
    federico "「もし、最初に配られた３枚で誰かの手元にあんたのカードが揃ってたらどうするつもりだったんだ？」"

    scene ecg chinarest odetto smi with dissolve

    voice get_voice_filename("ode")
    odette "「運命を呪うだけだよ。賭けに負けたって、死ぬだけだ」"

    "オレはこの女が苦手だった。"

    "頭がいいようで、肝心なところを運任せにしてしまう。"

    "慎重で論理的かと思えば、いきなり大胆なことをしでかす。"

    "何を考えているのか分からない。オレにとって女なんて、男の言いなりでしかなかったのに。"

    "そしてオレがこいつを一番苦手なのは――。"

    show ecg chinarest odetto lau with ecg_change

    voice get_voice_filename("ode")
    odette "「まあ、最後の２人になるまでは協力関係だ。従わないってんなら、また殴ってやるからかかって来な」"

    "最終的には全部暴力で解決しようとするところだった。"

    "この野蛮なゴリラ女め、とオレは心の中で悪態をついた。"



    stop music fadeout 1

    scene ecg chinarest federico ave with dissolve

    voice get_voice_filename("fed")
    federico "「……で、だ。選定の最後の日には日本にいなくちゃいけないんだろ？　なのにどうしてオレたちは中国にいるんだ？」"

    scene ecg chinarest odetto smi with dissolve

    voice get_voice_filename("ode")
    odette "「決まってるだろ？　あたしは北京ダックが好きだが、本場では食ったことがなかったんだ」"


    voice get_voice_filename("fed")
    federico "「おいおいマジかよ……」"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("ode")
    odette "「ついでに、宿題の答え合わせをしに来たんだ」"

    scene ecg chinarest federico ama with dissolve

    voice get_voice_filename("fed")
    federico "「は？」"


    play music audio.investigation

    scene ecg chinarest odetto nor with dissolve

    voice get_voice_filename("ode")
    odette "「あたしたちの船が襲われる直前、中国食品企業の重役さんが会議中に倒れたってニュースが入ってたんだ」"

    "あたしたちの船――その言葉から分かる通り、オデット・マランソンは海運業者の代表を務めていた。"

    "しかし、この女が普通の海運業者なわけはない。"

    "依頼を受ければ麻薬でも死体でも運ぶ、言わば裏の運び屋だ。"

    "国からさえも依頼を受けるから、存在自体が黙認されている。"

    "もっとも受ける依頼はもっぱらオデットが決めるらしく、あの女基準で「つまらない」依頼は受けないそうだ。"

    "とある事情でオレもその船に乗り合わせちまったせいで、こうしてオデットと手を組むハメになっちまった。"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("ode")
    odette "「≪選定≫で生還した後、気になったんで詳細を調べたんだ。だが……そんな事件の情報はなかった」"

    scene ecg chinarest federico ama with dissolve

    voice get_voice_filename("fed")
    federico "「お、おいそれって……」"

    "オレは、料理を運ぶ手を止めていたことに気付いた。"

    "対照的に、オデットは瓶に残った紹興酒をグラスに注がずに直で飲み干した。"

    scene ecg chinarest odetto ser with dissolve

    voice get_voice_filename("ode")
    odette "「仕事柄こういう世界の情勢ってのを気にしてないといけないから、あたしは一度聞いたら忘れねー」"

    show ecg chinarest odetto smi with ecg_change

    voice get_voice_filename("ode")
    odette "「{rb}魯{/rb}{rt}Ro{/rt} {rb}昌鎬{/rb}{rt}Chanho{/rt}――そいつの名前だ。調べ直してみたらまあ、ピンピンしてるみたいだぜ」"


    scene ecg cardbook clo with dissolve_long


    voice get_voice_filename("ode")
    odette "「お――？」"

    "オデットが中国企業の重役とやらの名前を口にしたのとほぼ同時、彼女の傍らに置かれた本が怪しい光を放った。"

    "分厚い赤茶色の表紙に、金の歯車のような装飾がついている立派な本だ。だがその中身は、おもちゃのように空洞が空いているだけだ。"

    "オレも同じ本を持っている――≪選定≫のカードを管理する≪カードブック≫とやららしい。"

    scene ecg cardbook op1 with dissolve


    voice get_voice_filename("ode")
    odette "「こいつはいい」"

    "オデットが本を開くと、光はやがて一ヵ所に集束した。"

    scene ecg cardbook op2 with dissolve

    "光が消えるのと同時に、細長い長方形の紙片が現れる。オデットはそれを空中でキャッチした。"

    python:
        add_character_cards("fed", ["7_name"])
        add_character_cards("ode", ["7_name"])
        add_character_cards("cnh", ["7_name"])

    scene ecg chinarest odetto smi with dissolve

    voice get_voice_filename("ode")
    odette "「魯昌鎬のカード……つまり“Ⅶ”の氏名のカードでビンゴだ」"


    voice get_voice_filename("fed")
    federico "「マジかよ。こんな簡単に……」"

    "女神とかいう少女は≪死因≫がなかったことになっていると言っていた。"

    "オデットが発見したこの矛盾――確かに、魯という男の≪死因≫がなかったことになっているということだろう。"

    show ecg chinarest odetto nor with ecg_change

    voice get_voice_filename("ode")
    odette "「こうなりゃあてずっぽうだ。魯は太っていたな。ってことは糖尿病を患ってたかもしれない」"

    show ecg chinarest odetto kno with ecg_change

    voice get_voice_filename("ode")
    odette "「そうなると、低血糖……いや企業の重役に上り詰めた奴が命に関わるミスを犯すとは思えない。会議中に突然死……≪脳梗塞≫か≪心筋梗塞≫だな」"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("fed")
    federico "「カードは出ない……な」"

    "オデットはあてずっぽうと言っていたが、それは立派な推測であった。"

    "だがカードが出ないということは、間違っている？"

    show ecg chinarest odetto nor with ecg_change

    voice get_voice_filename("ode")
    odette "「いや、カードが生成されるには条件があんのかもしれねーな。魯の名前に気付いていたのに今までカードが出なかったのは何故だ……」"

    scene ecg chinarest federico ave with dissolve

    voice get_voice_filename("fed")
    federico "「分かるかよ、そんなもん。他にないか迷ってみたらどうだ？」"

    scene ecg chinarest odetto nor with dissolve

    voice get_voice_filename("ode")
    odette "「お前も考えろってんだ――いや待てよ。迷う？　さっきのあたしは迷っていた………あたしの確信がなかった」"

    scene ecg chinarest federico ama with dissolve

    voice get_voice_filename("fed")
    federico "「でかい独り言だな」"

    "オレのからかう言葉を無視して、オデットは続けた。"

    "にやりと皮肉混じりに笑ったその表情は、自信に満ち溢れていた。"

    scene ecg chinarest odetto nor with dissolve

    voice get_voice_filename("ode")
    odette "「どちらかと言えば、確率が高いのは≪脳梗塞≫。糖尿病の合併症で、会議中、突発的に起きてもおかしくはない。これでどうだ？」"

    "オデットは物言わぬ本に問い掛けた。"

    scene ecg cardbook op3 with dissolve

    "ただの物体であるはずの本は、答えるかのように光を湛えた。先ほどと同じようにして、オデットはカードを手に入れた。"

    python:
        add_character_cards("ode", ["7_death"])
        add_character_cards("cnh", ["7_death"])


    voice get_voice_filename("ode")
    odette "「“Ⅶ”の死因――脳梗塞。今回はどうにかなったが、単純なあてずっぽうじゃ駄目みたいだ。一個分かったルールは確信を持たないとカード化されないってトコだが、かなり曖昧だな」"

    scene ecg chinarest federico ama with dissolve

    voice get_voice_filename("fed")
    federico "「ふぅん、確信、ねぇ」"

    "オデットは変わらず、料理を食べる手を止めなかった。"


    play music audio.badguys
    show ecg chinarest federico nor with ecg_change_wait

    "なるべく平常心を保とうと思っていたが、ついオレも酒を一気に飲んでいた。"

    "不幸だと思っていたが、これは案外ラッキーなのかもしれない。"

    "この女は――使える。"

    "腕っぷしも強いし、思った以上に頭が切れる。一緒にいれば、安全に邪魔な奴らは排除できるはずだ。"

    "そんなこいつが、何故オレと協力する必要があったのか。恐らく、オレがオデットの情報を得ていると思い込んでいて、他の参加者にばらされないように協力関係を持ち掛けたのであろう。"

    "同じ船で沈んだからこそ、同じ死因のはずだ、と。≪氏名≫も≪死因≫も割れているから、近くに置いておきたい。"

    "しかしオレは、オデットの≪死因≫を知らない。同時に、オデットもオレの≪死因≫を知らないはずだ。"

    "船の襲撃で死んだにもかかわらず、オレもオデットも溺死や焼死じゃあないんだ。"

    "実のところ、オレたちはお互いの≪氏名≫しか知らないのだ。やはりこれは、駆け引きだ。オデットは何食わぬ顔で、知っているふりをしている。"

    "協力関係を結びながら、最後の二人になった時のためにオレの情報を探ろうとしているってわけだ。"

    scene ecg chinarest odetto smi with dissolve

    voice get_voice_filename("ode")
    odette "「ふぅん、いい喰いっぷりになったじぇねえか」"

    show ecg chinarest odetto lau with ecg_change

    voice get_voice_filename("ode")
    odette "「この店にある一番いいワインを持って来てくれ」"

    scene ecg chinarest federico ser with dissolve

    voice get_voice_filename("fed")
    federico "「いいぜ、付き合ってやる」"

    "これから、オレにとって最も重要な勝負が始まる。"

    "酒の飲みっぷりですら、負けてたまるか。"




    scene black with dissolve

    "この後オレたちは、店のワインが尽きるまで飲み続けた。"

    "あの女はさらにホテルに戻ってからも、水代わりにワインを開けやがった。"

    "さすがに付き合い切れず、オレは自分の部屋で眠った。"

    $ add_character_cards("fed", ["7_death"])

    "朝、オレのカードブックにも魯のカードが生成されていた。"

    stop music fadeout 2
    scene black
    pause 4

    $ add_seen_chapter("2-2")

    if config.is_trial:
        call trial_end
        return







    python:
        set_info_scene("16")
        set_info_date(5, 10, "thu")
        set_info_time("noon")
        set_info_location("11")


    scene bg hotel beijing with dissolve_longest
    play music audio.investigation
    pause 1

    $ show_hud()

    "翌日、オレはオデットからの指示を受けて魯の尾行をすることとなった。"

    "魯の残りの情報≪未練≫を取得するための手がかりを探すためだ。"

    "≪選定≫は日本時間の日曜24時を基準に行われるから、それまでに３つの情報を集めておけばオレたちは一歩有利になる。"

    "何故オレだけなのかと言えば……オデットが二日酔いでダウンしているからだ。"

    "とはいえしおらしく具合が悪いのではなく、いかにも不機嫌そうに物へ当たり散らしている。"

    "こいつは使えると思った昨日のオレの確信は、早くも揺らぎ始めていた。"





    play music audio.kinpaku
    show fed sta nor pa3 at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「やべえぞオデット！」"

    "数十分後、オレはすぐにホテルへ戻ってオデットを呼んだ。"

    "魯の会社は北京市街の一等地の高層ビルにあった。人の出入りが多く見失いかけたが、何とか動向を追うことができた。"

    "魯は出勤して数分後、すぐに再び会社を出たのだ。"

    "オレは営業のフリをして、フロントで魯のスケジュールを尋ねた。出張らしい。行先は渋られたが、オレはどうにか台湾支社というところまで聞き出すことができた。"

    "魯は、本日から台湾へ２泊３日の出張をする予定だそうだ。"

    "調べたところ、ここから空港まで急げば同じ便に乗ることができる。"

    show fed sta nor pa4 with std_change

    voice get_voice_filename("fed")
    federico "「奴は今日から台湾へ出張だ。追うぞ！　とっとと準備をしろ！」"

    "八つ当たりをされるのを覚悟して、オレはオデットの部屋の扉を叩いた。"

    "だが予想とは反対に、しっかりと準備を終えたオデットが部屋から出てきた。荷物もしっかりキャリーケースにまとめてある。"

    "ちなみにオレたちは漂着した身ではあるが、運よくスマートフォンとカードだけが生きていたので、必要なものは新しく買い揃えている。"

    show ode sta arm smi rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「丁度、チェックアウトの連絡をしたところだ」"

    show fed sta nor pa1 with std_change

    voice get_voice_filename("fed")
    federico "「…………は？」"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「あたしがその情報を掴んでないと思ったか？　昨日の時点で、すでに分かってたんだよ」"

    show fed sta nor bad with std_change

    voice get_voice_filename("fed")
    federico "「じゃあ、どうしてオレに尾行させたんだよ？」"

    show ode sta gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「協力関係だ。頼られてばっかりじゃあたしの損だろ？　この程度の情報も掴めないんだったら協力関係を破棄してやろうと試してたのさ」"

    "オデットは平然とした口調でそう告げる。"

    "お眼鏡に適わなかったらどうするか言わないあたり、ひどい奴だ。大体、オレがこいつに品定めされる理由もない。"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「ちっ、食えない女だ」"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「何か言ったか？」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「んでもねーよ！」"

    "オレの方も急いで荷物をまとめ、北京のホテルを後にした。"

    python:
        set_info_scene("17")
        set_info_time("night")
        set_info_location("12")









    stop music fadeout 1
    scene bg hotel taiwan with fade_long
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "なんとか魯が乗る予定の飛行機に間に合ったオレたちは、台湾に到着後、目的のホテルまで辿り着くことができた。"

    "魯の部屋とは離れた部屋を指定し、オレたちはワインとチーズを囲みながら今後の作戦会議をしていた。"

    show fed sta nor no2 at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「しかしビビったぜ。あんた、飛行機の中で魯を探すんだから」"

    show ode sta nor lau rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「生意気にビジネスクラスに乗ってやがったから、ロビーで見つからなかったんだ。ま、エコノミーじゃ出っ張った腹が邪魔だろうがな」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「偶然座席が余っててアップグレードできたんで、到着ロビーから尾行してホテルを突き止められた。結果オーライだな」"

    show fed sta nor bad with std_change

    voice get_voice_filename("fed")
    federico "「ビジネスクラスでいい思いをしたのはあんただけ、な。あんたは≪選定≫の場所で顔が割れてるんだぜ？　魯が騒いだりしたらどうするつもりだったんだ？」"

    show ode sta nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「そんなこと、警戒すらしてなかったみたいだ。まさかあたしら選定の参加者が中国まで追って来てるとは思ってないみたいだ」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「いや――それ以前に、平然と仕事をして暮らしているあたり、ありゃもしかしたら≪選定≫そのものを信じていない可能性もあるな」"

    show fed sta nor ama with std_change

    voice get_voice_filename("fed")
    federico "「マトモな大人なら、信じないだろあんなもん。オレもあんたと一緒に漂着したから、信じたってもんだ」"

    "オデットはふん、とニヒルに笑い、続けた。"

    show ode sta nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「自分の死を冷静に認識できてれば『どうして生きている？』って疑問が浮かぶんだけどな。そうなりゃ選定とやらの存在を信じざるをえない」"

    show fed sta nor ama with std_change

    voice get_voice_filename("fed")
    federico "「そんな風にぶっ飛んでんのはあんただけだ」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「んなことより、滞在期間……気にならないか？」"

    "オレはチーズを手に取ったまま、問い掛けた。"

    "オデットの目が一瞬細くなったのを見て、オレは続けた。"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「会社で聞いたときのあいつの出張期間は２泊。だがフロントで聞いたら――いや、問い詰めたら魯はここに１泊しかしないらしい」"

    show ode sta nor tro rev with std_change

    voice get_voice_filename("ode")
    odette "「お前、魯に報告がいかないようにうまくやったんだろうな？」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「当たり前だ。クレーマーのフリをして『魯の部屋がうるさい。部屋を変えてくれ』って言ってやった。そしたらフロントの奴は『明日までだから我慢してくれ』って答えたんだ」"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「まあ及第点……か。確かに、そいつは妙だな。あいつは明日に台湾支社へ行って、明後日には工場の視察に行く予定になっているはずだ」"

    show ode sta nor ser rev with std_change

    voice get_voice_filename("ode")
    odette "「どちらも、このホテルからのアクセスは悪くないはずだが……」"

    show ode sta nor smi rev with std_change

    voice get_voice_filename("ode")
    odette "「まあいい。なら、お前は明日も張り込みを頼む。あたしは別の視点から調べ物をしてみる」"

    show fed sta nor pa1 with std_change

    voice get_voice_filename("fed")
    federico "「はぁ？　何だよそれ」"

    show ode sta nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「今日は飯だ。台湾料理はまだ食ってないからな。あたしは海の幸にはうるさいが、どれ、地中海料理との違いを堪能してやろうぜ」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「ま、いずれにせよ早まって魯を問い詰めたりしたら逆効果だしな」"

    "オレとオデットは、残ったワインをグラスに分けて飲み干した。"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「地中海はフランスのもんじゃなくイタリアのもんだ。海の幸の比較ならオレの方が適任だわな」"

    stop music fadeout 2
    scene black with dissolve_longest
    pause 2

    $ add_seen_chapter("2-3")











    python:
        set_info_scene("18")
        set_info_date(5, 11, "fri")
        set_info_time("night")
        set_info_location("13")

    scene bg taiwantown restaurant with dissolve_longest
    play music audio.investigation
    pause 1

    $ show_hud()

    "台湾料理というのも案外悪くない、というのが昨日の感想だった。"

    "上品さがちいと足りないが、エビ饅頭やらそぼろ煮、ビーフンなどジャンキーではまりそうだ。"

    "辛いのもいい。{rb}豆板醤{/rb}{rt}トウバンジャン{/rt}と{rb}甜面醤{/rb}{rt}テンメンジャン{/rt}でつけた辛さは、酸味と甘みのバランスがよくコクがある。"

    "と、そんなオデットのようなことを言っている場合ではない。"

    "オレは食べ過ぎの胃もたれを感じながら、朝一番にホテルの駐車場で張っていた。"

    "魯がタクシーで移動を始めるのを見て、オレもすぐに後を追った。"

    "そして、会社の前で数時間、仕事が終わるまで待った。退屈も過ぎるが、待つことには慣れている。"

    "台湾の街並みは中々面白く、通行人も見ていて飽きにくい。１時間は余裕で潰せる。残りの７時間強は苦痛だったがな。"

    "ようやく会社から出て来た魯を見つける。"

    show fed sta nor nor at std_cr with std_change

    voice get_voice_filename("fed")
    federico "「来たな」"

    scene bg taiwantown restaurant large:
        align (0.0, 1.0)
    with dissolve

    "行きがそうだったようにタクシーで帰るものかと思ったが、帰りはどうやら徒歩らしい。"

    "クレーマーのフリをしたオレをあしらおうと、フロントの奴が魯は一泊と嘘をついた可能性はまだ残っている。"

    "直行で帰らないだけで、食事をしてから帰る可能性は高い。特に企業の役員ともなれば付き合いも多いはずだ。"

    "彼が向かったのは、市街地にあるイタリアンレストランだった。リストランテ、だ。"

    "イタリアンにはリストランテ・トラットリア・オステリアと種類がある。その中で一番敷居の高いのがリストランテだ。"

    scene bg taiwantown restaurant with dissolve

    show fed sta nor smi at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「ほう、いい趣味してるじゃねえか」"

    scene bg taiwantown restaurant large:
        zoom 1.3
        align (0.5, 0.9)
    with dissolve

    play se "bell02"

    "魯の入ったレストランはガラス張りになっていたので、俺は向かいのカフェに入った。ここもまたガラス張りになっていたので、中の様子はよく分かる。"

    "オレはエスプレッソを頼み、砂糖をたっぷりと入れた。こいつ一杯でリストランテの食事の時間と張り合うのは厳しいが、仕方がない。"

    "外から見る限りでは、中々上等な店らしい。予約を入れているようで、魯は店員に案内されて席へとついた。"

    "少しの間待つと、席の向かいに人影が見える。"

    "若い女だ。いかにもオヤジが好みそうな赤いドレスを着ている。"

    "魯は確か家族がいたはずだが――深く考えるまでもなく、オレはピンと来た。"

    "オレの好みとは少し違うが、美人でスタイルもいい。ただれた商売女とは違った気品も持ち合わせている。"



    voice get_voice_filename("fed")
    federico "「なるほど。ま、役員なんてのはこんなもんかね」"

    "それからしばらく、オレは二人の食事風景を観察することにしていた。"

    "ワインはあらかじめ決めていたようだ。しっかりとした飲み口の赤。あれは中々にセンスがいいチョイスだ。味の分かる女なら舌鼓を打つ。"

    "だが残念なことに、魯の奴が残ったパスタソースにパンをつけて食っている。あれは駄目だ。一緒にいる女に恥をかかせちまう。"

    "周りの店の価格帯に比べると、魯の選んだ店はかなり高級だ。"

    "恐らく、ある程度の年齢がいってから通えるようになったのだろう。基本的なマナーは身につけてはいるが、染みついた習慣は抜けないようだ。"

    "あの歳であの立場じゃ、誰も注意なんてできないだろうし。"

    "結局、連中が食後のエスプレッソを飲み干すまでに３時間も待つことになった。"

    "魯がカードで会計を済ませるあたりで、オレも店を出る準備をした。"

    "この後の行動は決まっている。オレが魯の立場でも同じことをするさ。"

    scene black with dissolve

    "タクシーに乗り込んだ二人を、同じくオレもタクシーで追った。"

    "向かった先はどうやら女のマンションのようだ。オレは魯と女がマンションに到着し、部屋に入るのを見届けて帰ることにした。"

    "台湾犬っていうのか分からないが、見たことのない種類の犬がご丁寧にお出迎えしていた。"



    python:
        set_info_time("night")
        set_info_location("12")








    stop music fadeout 1
    scene bg hotel taiwan with fade_long
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    show ode sta nor gla rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「遅かったじゃねえか」"

    show fed sta nor no2 at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「まあ、な。どうだ、そっちは？」"

    "オデットは所在なさげに手をひらひらと振った。どうやら特に新しい情報を得ることができなかったらしく、苛立っているようだ。"

    "反面、オレの方は上機嫌だ。重要な情報を手にすることができたのだから。"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「んじゃ、情報を手に入れたのはオレだけってことかな」"

    show ode sta arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「勿体ぶらずにとっと言いやがれバカチン」"

    "やはり、オデットは苛立っている。"

    "オレは「やれやれ」とため息をついてから話し始めることにした。"


    play music audio.investigation

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「魯のヤロー、真面目な顔して女と合流してやがった」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「女？　家族……じゃないな。妻も３人の子供もまだ北京に住んでいるはずだ」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「ああ、若い女だったぜ。ありゃ愛人だな。ご丁寧にマンションに入る時キスをしてやがった」"

    show ode sta nor tro rev with std_change

    voice get_voice_filename("ode")
    odette "「悪趣味な奴だな」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「だろ？　あのふとっちょ、真面目そうな顔して愛人作ってやがったんだ。犬にも懐かれてるみたいだから、相当通い詰めてるぜ？」"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「犬にも……ね。おっと、悪趣味なのはお前だぜ？　中年男の恋事情を覗き見してんだからさ」"

    show fed sta nor ama with std_change

    voice get_voice_filename("fed")
    federico "「あんた、苛ついてるからってそりゃねえぜ」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「ともかく、だ。こいつの未練は≪愛人≫で決まりだな」"

    show ode sta nor gla rev with std_change_wait

    "すでに、≪家族≫や≪仕事≫という言葉は試していた。だが、そのどれもカードを生成するには至らなかった。"

    "無意識に確信を持てていなかったからかもしれないが、それでも、直感的に間違っている気がしていた。"

    "これでどうだとばかりに、オレは本に向かって問いかけてやった。"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「おい！　どうなんだ！　≪愛人≫で間違いないはずだろ！」"

    "本は少しも光ることはなく、一瞬生まれた沈黙では空調の音が聞こえるばかりだった。"

    show ode sta nor tro rev with std_change

    voice get_voice_filename("ode")
    odette "「…………残念。読みが甘かったみたいだな。あれだけ自信満々で反応しないんだから、情報自体が間違ってるってことだろうな」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「………………」"

    "オレは何も言い返すことができず、タバコを口に咥えた。"

    show ode sta nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「吸うなら喫煙所へ行ってくれ。あたしはタバコの煙が嫌いなんだ」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「ちっ、やり直しかよ。もういい、また明日あいつを追うんだな？」"

    "オレが投げ遣りに言うと、オデットは「ふん」と皮肉な笑いを浮かべた。"

    show ode sta gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「お前にゃまた尾行をしてもらおうかな。あたしは――今度こそ尻尾を掴んでやるさ」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「好きにしてくれ。ちっ、今頃魯は愛人とよろしくかよ」"

    "一瞬オデットの横顔が目に入ったが、こんなゴリラ女は頼まれても願い下げだ。"

    "くだらないことを考えてしまった自分にため息をついて、オレはタバコを吸いに部屋を出た。"

    $ add_seen_chapter("2-4")



    python:
        set_info_scene("19")
        set_info_date(5, 12, "sat")
        set_info_time("night")
        set_info_location("11")









    stop music fadeout 2
    scene bg hotel beijing with fade_longest
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "朝一に台湾を出て、オレたちは再び北京のホテルへチェックインしていた。"

    "その後、オデットは調べ物があると出かけ、オレは魯を尾行していた。"

    "普通に暮らしているだけでは、≪未練≫に繋がる手がかりを得ることができず、彼が帰宅したのを見届けてホテルに戻って来た。"

    show ode sta nor nor rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「遅かったじゃないか」"

    show fed sta nor no2 at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「あんた……どこへ行ってたんだ？」"

    show ode sta gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「ま、どこでもいいじゃないの。さて、あとは日曜を迎えるだけだし宴会しに行こう。初日に行った店がいいな。あそこの北京ダックはうまかった」"

    show fed sta nor pa4 with std_change

    voice get_voice_filename("fed")
    federico "「はあ？　魯の未練が分かったってのか？」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「ああ。だがお前にはまだ教えない。指名が２人になったら、優先権とやらの取り合いになるからな」"

    "≪指名≫における優先権の取り合い。女神はそんなことを言っていたような気もする。"

    "同じ奴を２人以上指名する者が出た場合、どちらかが自分の情報一つを全員に開示することで優先権を得られる。"

    "脱落させた奴の情報を得られるとはいえ、リスクが高過ぎる。魯の情報をオレに与えて同時指名になる可能性をなくすってわけか。"

    "なんだかんだ、信用されてないってことね。オレも同じだけどさ。"


    stop music fadeout 1

    show ode sta nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「ところでよ、いい加減怪しまれるぜ、おっさん？」"

    show fed sta nor pa4 with std_change

    voice get_voice_filename("fed")
    federico "「は？」"


    play music audio.gimon fadein 2

    "オデットの突然の発言は、オレに向けられたものではなかった。入り口……オレの入って来た扉に向かって話しかけていた。"

    "まさか、と嫌な想像をしていた。オレはごくりと息をのみ、扉を開けた。"

    scene bg hotel beijing large:
        align (1.0, 0.0)
    show cnh sta nor nor up at std_r
    with dissolve

    voice get_voice_filename("cnh")
    chanho "「気付かれていたみたいだね」"

    python:
        gameinfo_cardbook_cnh_unlocked = True

    "オレたちが今日まで調査していた男――魯昌鎬本人が目の前に立っていた。"

    "つまり、オレの方が尾行されていたということか。"

    scene bg hotel beijing
    show cnh sta nor nor at std_r
    show fed sta nor irr rev at std_c
    with dissolve

    voice get_voice_filename("fed")
    federico "「いつから、気付いて……」"

    show cnh sta nor nor with std_change

    voice get_voice_filename("cnh")
    chanho "「二人で協力していたとは、正直意外だったよ。だがどうにも嫌な感じがしてね。最初は裏金を調べに来たマスコミかとも思ったが、君のようなチンピラがそうとは思えなかった」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「チンピラだと？」"

    "オレのことを無視して、魯は続けた。"

    show cnh sta nor nor with std_change

    voice get_voice_filename("cnh")
    chanho "「オデット・マランソン。私をこそこそ調べていた首謀者は君だね？」"

    show ode sta gra smi rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「ほう、首謀者と来たか。やっぱり、あたしの方が偉そうに見えるってことだな」"


    play music audio.kinpaku

    show cnh sta nor cla with std_change

    voice get_voice_filename("cnh")
    chanho "「そんなことはどうでもいい！」"

    "魯の言う通りだ。大事なのは魯がオデットの名前を呼んでいたということ。"

    "つまり、彼はオデットの≪氏名≫を取得しているということ。ここでそれを明らかにしたということは、オデットに牽制を図っている。"

    "オデットもそれを分かった上であえて冗談を言っているのだろう。"

    show cnh sta nor nor with std_change

    voice get_voice_filename("cnh")
    chanho "「≪夢の世界≫……中々信じられない話ではあったが、夢の中で出会った人物が同じ飛行機の中にいたら信じないわけにはいかんよ」"

    show cnh sta nor nor with std_change

    voice get_voice_filename("cnh")
    chanho "「君のように目立つ女性は、間違えるはずもないしね」"

    "確かにオデットは目立つ。"

    "超高身長に、筋肉の鎧のような体。顔こそ美人かもしれないが、なにせゴリラ女だ。"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「確かに目立つぜ」"

    show ode sta gra gla rev with std_change

    voice get_voice_filename("ode")
    odette "「おい、何にやにやしてんだ」"

    show cnh sta nor nor with std_change

    voice get_voice_filename("cnh")
    chanho "「君こそ、笑っている場合ではないのでは？　私が何故わざわざここへ来たと思う？」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「ふん」"

    show cnh sta nor smi with std_change

    voice get_voice_filename("cnh")
    chanho "「取引だ。私にも家族がいる。こんなところで死ぬわけにはいかないからね」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「お前さんはあたしの≪死因≫か≪未練≫のどちらかを知っているわけだ」"

    "一息ついてから、オデットはわざとらしく首を左右に振った。"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「両方じゃないな。だったら最初の選定であたしを殺してる」"

    show cnh sta nor smi with std_change

    voice get_voice_filename("cnh")
    chanho "「話が早くて助かるよ」"

    show fed sta nor irr rev with std_change

    voice get_voice_filename("fed")
    federico "「待て。こっちはあんたの情報をすべて持ってるんだぞ？　立ち聞きしてたんだから分かってるはずだ」"

    show cnh sta nor nor with std_change

    voice get_voice_filename("cnh")
    chanho "「ああ。だから私の取引はこうだ」"

    show cnh sta nor nor with std_change

    voice get_voice_filename("cnh")
    chanho "「ミス・オデット、君は私を指名しないと約束してくれ。さもなければ、このチンピラに君の情報を教える」"

    "魯は真剣な表情で、そう告げた。"

    "何、と思わずにやけそうになってしまった。"

    "ホテルの一室には緊張が走る――かに思えた。"

    "張り詰めた空気を、オデットの笑い声が断ち切ったのだ。"



    stop music fadeout 1
    scene black with dissolve
    pause 1
    play se "punch01"
    scene white with dissolve_fastest
    pause 0.1
    scene black with dissolve_fastest
    play se "crash01"
    pause 2

    "直後、オデットは魯の顔面を思い切り殴った。あの巨体と怪力で殴られたせいで、１００ｋｇは超えていそうな魯も廊下の反対側まで叩きつけられた。"

    scene bg hotel beijing with dissolve

    show cnh sta nor pan at std_r with std_in

    voice get_voice_filename("cnh")
    chanho "「ぐあっ……何をする……？」"

    "オデットはゆっくりと歩み寄り、倒れたままの魯の前に座り込み、また笑った。"

    "魯は頬を押さえているが、今度は鼻血が止まらないようだった。"


    play music audio.odette
    scene ecg odettobt fun with dissolve_long


    voice get_voice_filename("ode")
    odette "「はははははは！　笑わせんな。こんなの全然取引になってねえんだよ」"


    voice get_voice_filename("cnh")
    chanho "「何だと？　今すぐ情報をばらしてもいいんだぞ？　そうすれば貴様らは仲間割れに」"

    show ecg odettobt mad with ecg_change


    voice get_voice_filename("ode")
    odette "「やってみろよ。だが、そうしたらあたしはお前の家族を全員、こいつに殺させる」"


    scene bg hotel beijing
    show fed sta nor pa1 at std_c
    with dissolve_long



    voice get_voice_filename("fed")
    federico "「は？」"


    play se "floor_hit"
    show fed sta nor pan with std_change_wait

    "オデットは床をばん、と破裂音がするほどの力で殴り、オレを制した。"

    scene ecg odettobt fun with dissolve_long


    voice get_voice_filename("ode")
    odette "「お前の目論見が成功して仲間割れしたとして、万が一にあたしが負けてこいつが生き残ったらどうだ？　お前の家族が死んだことはなかったことにはならないぞ？」"


    voice get_voice_filename("ode")
    odette "「家族だけじゃなく、お前の≪未練≫も死んじまう」"


    voice get_voice_filename("cnh")
    chanho "「貴様……何て外道な」"

    show ecg odettobt mad with ecg_change


    voice get_voice_filename("ode")
    odette "「はははは！　黙れよ、クソジジイ」"




    scene bg hotel beijing with dissolve_long
    play se ["punch01", "crash01"]
    with quake_normal

    "オデットは立ち上がり、魯の腹部を思い切り蹴り飛ばした。"

    show cnh sta nor pan at std_r with std_in

    "オレから見ても、一方的に過ぎる暴力に若干引いていた。"

    scene ecg odettobt mad with dissolve_long


    voice get_voice_filename("ode")
    odette "「小物が粋がってんじゃねえ。お前が大人しく死んどけば、何もかもうまくいくんだよ」"


    voice get_voice_filename("ode")
    odette "「取引がしたいってんなら、てめーもあたしの情報を集めてからだ。あたしが指名してもちゃんと防御できるようにな」"


    voice get_voice_filename("cnh")
    chanho "「貴様……！」"

    show ecg odettobt fun with ecg_change


    voice get_voice_filename("ode")
    odette "「ビジネスマンなら、０を１にする交渉じゃなく、１を１００にする取引をすべきだろ？」"

    "オデットは魯のシャツの胸ぐらをつかみながらゆっくりと言った。"


    scene bg hotel beijing
    show cnh sta nor pan at std_r
    with dissolve_long

    "オデットが凄むと、魯は何も言わずに目を閉じていた。"

    show ode sta arm irr rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「遺言状でも書いてな。意味はなくなっちまうけどよ」"


    stop music fadeout 1
    scene bg hotel beijing with fade_long

    "オレはオデットに促され、部屋へ戻った。色々と言いたかったが、逆らうことはできなかった。"

    "前に言った通り。"

    "この女は、最後は暴力で解決しようとするんだ。"


    play music audio.badguys

    "部屋に戻ってから、オデットは何食わぬ顔で言った。"

    show ode sta arm irr rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「さ、飯食いに行くぞ」"

    show fed sta nor pa2 at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「わ、分かったよ」"

    "こいつは普通じゃない。"

    "マフィアってのはある程度の経済活動が成立しているから、悪事はするが意外と社会性ってのが身についている。"

    "海ってのは、ある意味じゃ社会と断絶されている。そのせいで、このオレでさえもイっちまってると思う奴が生まれてしまうんだろう。"

    "オレはあらためて感じていた。"







    $ set_info_location("10")

    stop music fadeout 1
    scene black with dissolve_long
    pause 2
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "オレたちがホテルを出る時には、魯の姿はすでになかった。今頃、残された時間を家族と過ごしていると思うと気の毒にもなった。"

    "とはいえ、何だかんだきちんと飯を食って酒を飲んでいるオレも普通じゃないな、と思っていた。"

    "たらふく食べたところで、オデットは一瞬、真剣な表情を浮かべた。"

    scene ecg chinarest odetto smi with dissolve_long

    voice get_voice_filename("ode")
    odette "「お前、こっそりあいつと接触しようとは思うなよ？」"

    show ecg chinarest odetto ser with ecg_change

    voice get_voice_filename("ode")
    odette "「死ぬよりも恐ろしい目ってのを、あたしは知ってるからよ」"

    "食事中にさりげなく、オデットは言ってのけた。"

    scene ecg chinarest federico ama with dissolve

    voice get_voice_filename("fed")
    federico "「ちっ……分かってるよ。残り２人になるまでは、この同盟は続けてやる」"

    scene ecg chinarest odetto ser with dissolve

    voice get_voice_filename("ode")
    odette "「何でお前が上から目線なんだよ？　あ？」"


    voice get_voice_filename("fed")
    federico "「分かった分かった。平等だ。殴るなよ？　殴ったら魯のところへ行くからな？」"

    show ecg chinarest odetto lau with ecg_change

    voice get_voice_filename("ode")
    odette "「ははははは！　それはいい。面白い冗談だ」"

    "大笑いを浮かべたオデットの目は、全く笑っていなかった。"

    show ecg chinarest odetto kno with ecg_change_wait

    "こいつは余裕に見えて、意外とぎりぎりな橋を渡っている。もちろん、それはオレも同じなのだけれど。"

    "オレに魯の≪未練≫を教えない理由は同時指名のリスクだけでなく、魯の所持カードの中にオデットの情報があることまで考慮に入れていたからであろう。"

    "こんな単純なことに今気付くようじゃ、オレはまだオデットを出し抜くなんてできないだろう。"

    "魯のところへ行くなんてもってのほかだ。デメリットがメリットを大きく上回る。"

    "こいつは仲間でいた方が得だと、オレは再認識した。"

    show ecg chinarest odetto ama with ecg_change

    voice get_voice_filename("ode")
    odette "「しかし、あんぐらいでかいと殴りがいがあるな。もう一発殴っておけばよかった」"

    scene ecg chinarest federico ama with dissolve

    voice get_voice_filename("fed")
    federico "「お前、あの時楽しんでただろ？」"

    scene ecg chinarest odetto smi with dissolve

    voice get_voice_filename("ode")
    odette "「あ、分かる？　命のやり取りをしてるって感じがして、サイコーに気持ちいいんだよ」"

    "こんな思考回路の狂った奴を敵に回すのは、馬鹿げているってもんだ。"

    "こうしてオレたちは、２回目の≪選定≫の日を待つのであった。"

    $ add_seen_chapter("2-5")





    python:
        set_info_scene("20")
        set_info_date(5, 13, "sun")
        set_info_time("night")
        set_info_location("05")








    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    show rnk paj nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……ふぅ」"





    menu:
        "この数日間、≪選定≫において私は特に進展のない生活を送っていた。"
        "直未との関係は……。":

            $ persistent.s4_1_seen = True
            $ grant_hear_all()
            jump f002.s1_1
        "海晴との関係は……。":

            $ flags_mhr_koukando += 1

            $ persistent.s4_2_seen = True
            $ grant_hear_all()
            jump f002.s1_2



label f002.s1_1:

    "直未とは、会う機会が増えていた。"

    "文化祭に向けて、直未にコーヒーの淹れ方を教え始めたからだ。"

    "お湯を床にこぼしたりフィルターを四つ折りにしてしまったりというミスは何度かあったが、まだカップを割ってはいなかった。"

    "慌てん坊な直未だが、カップは特におばあちゃんの思い出が詰まっているものであることは知っているので、気を遣ってくれたのだろう。"

    "一方海晴との関係は、あれ以降≪選定≫の始まる前と特に変わっていない。"

    show rnk paj arm sad with std_change

    voice get_voice_filename("rnk", 184)
    rinka "「……違うか」"

    "本当は、大きく変わってしまったのだ。"

    "二人とも、努めて今まで通りにしようとしているという意味で。"

    jump f002.s1_end



label f002.s1_2:

    "海晴との関係は、あれ以降≪選定≫の始まる前と特に変わっていない。"

    show rnk paj arm sad with std_change

    voice get_voice_filename("rnk", 185)
    rinka "「……違うか」"

    "本当は、大きく変わってしまったのだ。"

    "二人とも、努めて今まで通りにしようとしているという意味で。"

    "一方、直未とは会う機会が増えていた。"

    "文化祭に向けて、直未にコーヒーの淹れ方を教え始めたからだ。"

    "お湯を床にこぼしたりフィルターを四つ折りにしてしまったりというミスは何度かあったが、まだカップを割ってはいなかった。"

    "慌てん坊な直未だが、カップは特におばあちゃんの思い出が詰まっているものであることは知っているので、気を遣ってくれたのだろう。"



label f002.s1_end:

    show rnk paj nor nor with std_change

    voice get_voice_filename("rnk", 186)
    rinka "「今日は、もう寝よう」"

    hide rnk with std_out

    "私はそう独り言をこぼした。"

    "確か前は０時に突然意識が持っていかれてしまった。今回も同じなのであれば、先に眠ってしまえばいい。"

    "時計で11時頃なのを確認してから、私は目を瞑った。"

    $ add_seen_chapter("2-6")



label sentei2:

    call set_replay

    python:
        set_info_date(5, 13, "sun")
        set_info_scene("21")
        set_info_time("lnight")
        set_info_location("07")










    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall fadein 2
    pause 2
    show bg fatalhall01 up with dissolve
    pause 1

    $ show_hud()

    show rnk uni arm sad ci at ci_r with ci_in

    voice get_voice_filename("rnk", 187)
    rinka "「起きていても、眠っていても関係ないのか……」"

    hide rnk with std_out

    "私は、運命の大広間に立っていた。"

    "さすがは夢の世界。"

    "私が起きているか眠っているかなんて、関係がないようだった。"

    show mhr uni nor nor rev ci at ci_l
    show aln sta nor nor ci at ci_r
    with ci_in

    "左隣には海晴。右隣には“Ⅻ”の中東系らしき男性。"

    "二人ともちらりと顔を見ただけで、会話を交わすことはなかった。"

    "私はこの男性のことを怖いと思っていた。前の選定の時に相手を脱落させて戻ったとき、彼は無表情だった。"

    "自分が誰かの未来を奪ったとして、無感情になれるなんて信じられなかった。"

    "≪選定≫の参加者は誰も会話をしてはいなかった。"

    "暗闇の中に浮かぶ巨大な歯車が放つ地響きのような音が遠くに響き、息苦しくなるような沈黙がこの場を支配していた。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro gl2 big at std_c with std_in

    voice get_voice_filename("dia", 56)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "その沈黙を破ったのは、少女の声であった。"

    "大広間の中央にある時計の中心に、綺麗な姿勢で立っている。"

    "私がこの空間に来たときにはいなかった気もするが、いつの間にかそこに立っていた。"

    "もし瞬間移動というものがあるなら、周りの人はきっとこういう違和感を覚えることだろう。"

    "そもそも女神なのだから本当に瞬間移動ができるのかもしれない。"

    show dia sta fro smi big with std_change

    voice get_voice_filename("dia")
    parca "「皆サマ、まだまだお元気そうでございますわね。再び死ぬ実感などまだ湧いてはいないのでしょう」"

    "透明な彼女の声は、女神だと納得させられてしまう。"

    "彼女の無慈悲な発言も、私たち人を根本的に下に見ていると思えば、女神らしいものなのかもしれない。"

    "一週間で、私の女神パルカに対する認識は少し変わっていた。"

    scene ecg parcadeclaration:
        subpixel True
        align (0.5, 1.0)

        linear 13 yalign 0.0

    with Dissolve(3)
    pause 8


    voice get_voice_filename("dia")
    parca "「それでは、今宵も選定を始めましょう」"

    "静かな声で、女神は今日も終わりの始まりを告げた。"


    voice get_voice_filename("dia")
    parca "「廻れ！　運命の大時計よ」"



    stop music fadeout 1
    show bg fatalhall01 normal with dissolve_long
    play music audio.restlessness
    pause 1



    "パルカが静かな声でそういうと、時計の針が動き出した。"

    "長針の先は、まず私へ向いた。"

    "１回目の選定の時には余裕がなくて気付けなかったが、これは「指名を行う意志があるかどうか」の確認らしい。"

    show bg fatalhall01 up with dissolve

    show rnk uni nor que ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「私は……ないよ」"

    show mhr uni nor ser rev ci at ci_l with ci_in

    "次の海晴も同じく指名はなし。"

    hide rnk
    show fed sta nor nor ci at ci_r
    with ci_swap

    "その次……“Ⅲ”の男性も指名は行わないようだった。顔立ちからヨーロッパの人に見える。身長が高く、スーツを着込んでいた。"

    scene bg fatalhall01 normal with dissolve

    "そういえば、この世界での服装は一体どういう基準で選ばれるのだろう。"

    "寝る時にスーツとは思えないから、あの男性は起きているのに突然意識が≪夢の世界≫に来てしまったのだろうか。"

    "だが、必ずしも≪夢の世界≫に来た時の服装でここにいるわけではないのは、私自身が証明していた、"

    "パジャマを着ていたが、今は制服に変わっている。海晴も……制服だ。"

    "この制服は珍しい形ではないから、写真でも撮れなければすぐに特定されることはないだろうけれど、個人情報を晒していることに変わりはない。"

    "その基準は、私には分からなかった。"

    "私はあらためて、選定の参加者を眺めていた。"

    scene bg fatalhall01 up with dissolve

    show cnh sta nor pan rev ci at ci_l with ci_in

    "この中で“Ⅶ”の男性だけが明らかに落ち込んでいる。パルカの言葉は単なる皮肉だったのだろう。"

    "きっとこの人が指名される――誰もが思っているはずだ。"

    hide cnh with ci_out

    "ここに集められた人の共通点は、以前パルカが言っていた≪因果の刻≫以外にはないのだろう。"

    "性別も年齢も国籍も、全てがバラバラだ。"

    show yuu sta nor nor rev ci at ci_l with ci_in
    show son sta nor nor ci at ci_r with ci_in

    "“Ⅳ”や“Ⅹ”の子なんて、私よりも年下だ。どちらも女の子で、外国人のようだ。"

    "一体どうして彼女たちが死ななければいけなかったのだろう。"

    "そしてそれを知ることは、彼女たちを脱落させることに繋がってくると思うと嫌な気分になった。"

    hide yuu
    hide son
    show ode sta nor nor rev ci at ci_l
    with ci_swap

    "気付けば、針は“Ⅺ”まで進んでいた。背が高くてまるでスポーツ選手のような体型の女性だ。"

    "足が長く、胸もかなり大きい。"

    "明らかに日本人ではほぼありえないスタイルで、背が低い私であるが羨ましいとかそういう次元を超えていると思っていた。"

    "針は一度、彼女の前で止まる。"

    show ode sta gra smi rev ci with ci_change


    voice get_voice_filename("ode", 85)
    odette_num "「はぁん……」"

    "私がじろじろ見ていたからだろうか。女性と目が合ったような気がした。"

    show rnk uni arm sad ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「ひっ――――」"

    "瞬間、私は目を逸らしていた。"

    "どうしてだろうか、恐怖を感じていた。本能的な直感と言うのだろうか。"

    "この人は、違う。"

    "普通の人じゃない。体型とかそういう単純な話ではなく何かが違う。"

    "“Ⅻ”の男性ともまた違う恐ろしさがある。"

    hide rnk
    show cnh sta nor pan ci at ci_r
    with ci_swap

    "自分が指名されるのではないかと錯覚したが、彼女が指名したのは予想通り“Ⅶ”の男性だった。"

    "時計の短針が、男性の床へと向いた。"

    "指名者と被指名者の二人の床が、怪しい光を放っていた。"

    "その状態で、長針が“Ⅻ”の男性を指した。今夜は指名しないらしく、小さな動作で首を横に振った。"


    stop music fadeout 1

    scene bg fatalhall01 up large with dissolve

    show dia sta fro smi big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「“Ⅺ”サマが“Ⅶ”サマを指名ですわね」"

    "長針が一周したのを見届けてから、パルカは微笑んだ。"

    "これから誰かがこの儀式から脱落する――本来の死の運命に戻るというのに不釣り合いな表情だった。"

    scene bg fatalhall01 normal with dissolve

    "指名者と被指名者の床が動き出し、上へとせり上がっていく。"

    "前回と同じ流れのようだ。"

    scene bg fatalhall01 up with dissolve

    show rnk uni arm vig ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「戻って来るのは、どちらか一人……」"

    "私は、せり上がる床から目を逸らしていた。"






    scene black with dissolve_long
    pause 1

    "しばらくして、選定が終わる。"

    play music audio.fatalhall
    scene bg fatalhall01 up with dissolve

    "戻って来た女性は不満そうな顔でパルカに告げた。"

    show ode sta arm irr rev ci at ci_l with ci_in


    voice get_voice_filename("ode")
    odette_num "「Ⅴの氏名な。ちっ……最期まで小物かよ。またジジイだしよ」"

    show sig sta nor nor ci at ci_r with ci_in

    "彼女の言う“Ⅴ”はこの中で最高齢に見える男性だった。恐らく日本人。"

    "女性が彼の氏名を手に入れたことを聞いても動じてはいないようだ動揺を隠しているのかもしれない。"

    "感情の起伏で言えば、指名した女性の方がよっぽど激しい。"

    "それは、最初に指名して脱落させたⅫの男性とは対照的だった。"

    "無感情な彼とは違い、不満げだが裏では楽しんでいるようにも思える。ゲームに負けた子供……見た目と裏腹、そんな喩えが浮かんだ。"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者は１名。これをもって、選定を終了といたしましょう」"




    scene black with dissolve

    "もっと色々観察をしたかったが、パルカは冷淡な声で終わりを告げる。"

    "２回目の選定では、１度目よりも得る情報が多かった。"

    "だがそれは私にとって、より大きな波乱を予感させるものでもあった。"

    $ renpy.end_replay()
    $ add_seen_chapter("2-7")

    $ persistent.sentei2_clear = True
    $ grant_achievement("divine_selection_02")

    jump f003
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

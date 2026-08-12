

label f008:









    python:
        set_info_scene("111")
        set_info_date(6, 18, "mon")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "頭の中にかかっていた霧が、徐々に晴れていく。"





    menu:
        "近くには、人の気配を感じていた。"
        "「……直未？」":

            $ persistent.s13_1_seen = True
            $ grant_hear_all()
            jump f008.s1_1
        "「……海晴？」":

            $ persistent.s13_2_seen = True
            $ grant_hear_all()
            jump f008.s1_2
        "「……真央？」":

            $ persistent.s13_3_seen = True
            $ grant_hear_all()
            jump f008.s1_3

label f008.s1_1:




    voice get_voice_filename("rnk", 1120)
    rinka "「……直未？」"



    voice get_voice_filename("mhr", 400)
    miharu "「ぼくより、日辻さんの方がよかったかな？　今朝だからか、それとも――」"

    show rnk paj sur su2 rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「わ、わぁっ」"

    jump f008.s1_end

label f008.s1_2:



    voice get_voice_filename("rnk", 1122)
    rinka "「……海晴？」"



    voice get_voice_filename("mhr", 401)
    miharu "「聞き間違えじゃなければ、ぼくの名前を呼んでくれたのかい？　くすっ、それは嬉しいな」"

    show rnk paj arm shy rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「わ、わぁっ」"

    jump f008.s1_end

label f008.s1_3:




    voice get_voice_filename("rnk", 1124)
    rinka "「……真央？」"



    voice get_voice_filename("mhr", 402)
    miharu "「くすっ、凛火は変な夢でも見ていたのかな。選定の後に楽しい夢を見ることができたのだから、幸せというべきかもしれないね」"

    show rnk paj sur su2 rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「わ、わぁっ」"

    jump f008.s1_end


label f008.s1_end:


    play music audio.miharu

    show mhr sun sco smi at std_cr with std_in

    voice get_voice_filename("mhr", 403)
    miharu "「おはよう、凛火」"

    show rnk paj sur su1 rev with std_change

    voice get_voice_filename("rnk", 1126)
    rinka "「あれ……どうして？」"

    "私が目を覚ますと、傍らには海晴がいた。"

    "海晴は制服を着ていて、準備は万端、といった雰囲気だ。"

    show mhr sun nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくがここにいるか、だね。昨日、凛火が電車の火事の中にいたとき、ぼくが凛火を運んだんだ」"

    show mhr sun sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「あんな場所にいれば、病院に運ばれてもマスコミが押し寄せて来る。飴茶の生徒だと知れれば余計にね。凛火にそんな負担はかけさせないさ」"

    show mhr sun nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「一日経てば世界の改変が起こると思っていたから、そこまで大変なことではなかったよ」"

    show rnk paj nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「えっと、何で私が山手線にいるって分かったの？」"

    show mhr sun sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「スケールたちと協力関係を結んでいたことが幸いしたよ。信用していいのか分からない人たちだけれど、彼の情報は正確だった」"

    "海晴は、「もっと速く駆けつけられればよかった」と付け足した。"

    show rnk paj nor shy rev with std_change

    voice get_voice_filename("rnk")
    rinka "「もしかして、一晩ずっと隣にいてくれたの？」"

    show mhr sun sco sh1 with std_change

    voice get_voice_filename("mhr")
    miharu "「……一度、ぼくの荷物を取りに家へ帰ったけれどね。あんな状態の君を独りにしてはおけないよ」"

    show rnk paj arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……ありがと。ほっとした」"

    show mhr sun sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「それはぼくの言葉さ。運命の大広間で君の姿を見ることができたけれど、目覚めないのではないかと不安だったよ」"

    "私は意識を失ってしまったので分からないが、どうやら、面倒事に巻き込まれないようにしてくれたらしい。"

    "てっきり病院で寝ていると思ったから、拍子抜けだ。"

    "自分の部屋にいると思うと、少し落ち着く。"

    "手足も動くし、筋肉痛はあるけれど、重大な体の不調はなさそうだ。"

    "そうなると気になるのは一つ、だった。"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「世界がどうなったか……だね。ユウの件は世界への影響が大きかったから、ぼくの認識とも相違が大きい。ぼくもまだ調べ切れてはいないけれど、話をさせてもらうよ」"

    show mhr sun nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「その前に、まず学校へ行く準備を済ませてしまったらどうだい？　まだ時間はあるけれど、長い話になるからね」"

    "それから私は制服に着替えて準備を済ませ、１階へと移動することにした。"

    "話をするなら、ライオン館の方が落ち着いて話せる。"







    $ set_info_location("04")


    stop music fadeout 1
    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "私は、二人分のコーヒーを淹れた。"

    "たっぷり寝ていたからか目覚めるのも早く、登校までには１時間以上の余裕があった。"

    show mhr sun nor rea rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「思えば君とこうするのは、とても久し振りだね」"

    show rnk sun nor apo at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「私の心が……完全に折れちゃってたからね。真央が来てくれて、海晴が頑張ってるって思って、ようやく立ち直れた」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「無理もないさ。それに、ぼくは色々動いたけれど、結果を出すことができたのは凛火……君なんだ」"

    "直未の死。"

    "今から聞くのは、それに関する話だ。"

    "海晴は一呼吸置いてから、話を始めた。"


    play music audio.disclose

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「まず、昨日の爆破テロだ。あの事件は、原因不明の出火による火事……とされた。恐らく、列車の経年劣化により、配線の整備不良が出火の原因だろう……と」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「一昨日の東京タワーでの一件は、どうやら事件そのものがなかったことになっているらしい。動画の生配信も行われていたが、それを見た人の記憶がどうなっているか分からない」"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「日辻さんのように、深層心理が覚えていて、夢というかたちでなかったことになった可能性を見る人はこれから現れるかもしれない」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「この点は、真央にも聞いてみた方がいいだろう。真央なら、生配信を見ていてもおかしくはないからね」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「以上から推測できるのは、物質の移動や変化は残るけれど、行動は残らない、ということだね」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……桂子さんの時と同じだ」"

    "桂子さんから渡された手紙。"

    "彼女が脱落したあと、それは白紙になっていた。"

    "桂子さんが手紙をしたためたという行動が、なかったことになっていたのだ。"

    "嫌な、予感がした。"

    "直未の死後の肉体の変化を物質の移動とするならば、それは――。"

    show rnk sun arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「まさか――」"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「落ち着いてくれ、凛火。順番に話をするからね」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「さらに時系列を遡ろう。先月、渋谷で不審物が発見されたという事件をきっかけに、テロ組織≪ＮＵＬＬ日本支部≫の幹部が逮捕された」"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それは、選定の参加者が命を落とした日――因果の刻にユウが起こした≪山手線爆破テロ≫が≪なかったこと≫になったから起きた事件だ」"

    "そもそも組織として限界が来ていたところに、テロの失敗と実行犯の失踪が重なった。"

    "内部リークにより、テロ組織の幹部は逮捕されたのだ。"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「この事件も、なかったことになっている。いや、時期が変わったというべきだろう。彼らは、ゴールデンウィーク直後……つまり、まさに因果の刻の直後に逮捕されている」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「幼い少年の起こした自爆テロに関わってしまったことに恐れをなした、≪ＮＵＬＬ日本支部≫の内部リークにより、ね」"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「あの日……自爆テロは起きていた」"

    "ユウの死因は、もう≪なかったこと≫にはなっていないのだ。"

    "今私がここに座っているこの時点では、あの少年は命を落としている。"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「しかし、その時の犠牲者は怪我人が数人。死者は実行犯の少年のみ。ユウという名前も、あの時点での彼は持っていないのだったね」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私も……今は生きていることになってるからね。でも、おかしい。私の奥底に眠る記憶だと、他に死者もいたと、思う」"

    "あの満員電車で、しかも至近距離で死者が出ないというのは、奇跡でも起きない限りあり得ない。"

    "もっとも≪女神の選定≫に≪運命の改変≫自体がそもそも奇跡と呼べるのかもしれないけれど。"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「恐らく……君がトリガーだ。君が生きているから、運命は君を生かすために強引な改変をされている」"

    show rnk sun arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「私が死ねば……」"

    "炎に包まれた光景が、脳裏を駆け巡る。"

    "海晴の推測は納得ができる。"

    "だが、今もっとも知りたいのはそのことではなかった。"

    "私にとっての運命の決着――その結果が知りたかった。"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「それでさ……飴茶でのテロはどうなったの？」"

    "ごくり、と唾を飲んだ。"

    "嫌な予感はしていたけれど、自分を疑うことはしていない。"

    "そうでなければ、私はきっと――。"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「文化祭の日に起きた≪私立飴茶女子大学附属高校爆破テロ≫はなかったことになっている」"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「けれど、文化祭の倉庫として使っていた空き教室から出火し、その教室が焼け焦げた、という事件は存在している」"

    show rnk sun sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「嘘っ！　それって……、だって！」"

    "私は、息が止まりそうになっていた。"

    "心臓が急激に冷やされていくような錯覚。"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ただし死者は――ゼロだ」"

    show rnk sun sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……あっ……じゃあ、それって……」"

    "海晴の言葉を聞き、私の心臓は再び熱を取り戻した。"

    "急激な温度変化で、変になってしまいそうだ。"

    "死者がいないということはつまり、直未は、死んでいない。"

    "直未は、生きている――！"

    "けれど海晴の声は、とても静かだった。"

    "その理由は、すぐに分かった。"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ただし、火傷をしている可能性も、後遺症が残っている可能性も捨てきれない。火事そのものは、起こっているからね。ニュースだけでは、そこまで分からなかった」"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それに情けないことだけれど、ぼくも少し怖い。もし生きてはいても日辻さんの身に何かが……そう思うと、真央や本人に連絡する勇気が湧かなかった」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君の掴んだ現実がどうなっているか分からないから、どう聞いていいかも分からないしね」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「なんだ、そんなことか。心配する必要はないよ。だって、生きていれば不幸になんて――させないから」"

    show mhr sun sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。やはり君は……強いね」"


    voice get_voice_filename("rnk")
    rinka "「そんなことないよ。色んな人の助けを借りなきゃ、大切なものを守れないくらい弱いよ」"

    show mhr sun nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君がそう思うならそれでいいけれど。少なくとも、君が生きるべきだと、再確認できたのは事実だ」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……海晴、それはもう、違うよ」"

    "海晴はきょとんとした顔を浮かべる。"

    "私は、そのまま続けた。"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「生きるべき、とかじゃない。生きたいかどうかが、大事なんだ」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火……。君は、生きたいと願っているんだね？」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。私はもう、ぶれないよ。生きることに、悩まない。でもね、もう一つ決めたことがある」"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「それは、ソーニャも言っていたことなんだ。私たちは一度、その可能性を考えた。でも直未のことがあって……忘れてた」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「だから改めて言うよ。私たちは、二人で……」"


    hide rnk
    hide mhr
    with std_out

    play music audio.nichijo01
    show lete normal at cat_c with std_in


    voice get_voice_filename("cat")
    lete "「にゃーお」"


    voice get_voice_filename("rnk")
    rinka "「にゃっ……って、ちょっとぉ」"

    "私が海晴に自分の決意を表明しようとしたとき、気の抜けた声が割り込んできた。"

    "ライオン館に棲みついている黒猫のレテだ。"

    "早朝に歩いているなんて珍しい。"

    "レテは私と海晴の座っているテーブルまでちょろちょろと寄って来て、そこで丸くなった。"


    hide lete with std_out

    show mhr sun nor rea rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「やあ、初めましてだね」"

    show rnk sun nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あれ、そうだっけ？」"

    show mhr sun sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「話には聞いていたから、あまり初めてという気はしないけれどね」"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「はぁ、何か気が抜けちゃった」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それくらいが丁度いいさ。昨日までの激動の日々がようやく終わったんだ。ずっと気を張っていたら、それこそ気がもたないだろう」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「しかし、この猫……」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「レテがどうかした？」"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「レテ……そうか、この子の名前はレテ、だったね。レテ……どこかで聞いたことがあるような……」"

    show mhr sun sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、珍しい名前だから気になっただけかな。撫でてもいいかい？」"

    show rnk sun arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「あれ、海晴って動物苦手じゃなかったっけ？」"

    show mhr sun sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「苦手じゃなくて、嫌いだよ。けれどね、この子もきっと、凛火を支えてくれていたのだろう？　だったら、お礼をしないといけないよ」"

    hide mhr
    hide rnk
    with std_out

    show lete normal at cat_c with std_in

    "海晴は恐る恐る、レテに向かって手を伸ばした。"

    "動物慣れしていないというのがよく分かる。"


    voice get_voice_filename("rnk")
    rinka "「大丈夫だよ、ほら」"


    voice get_voice_filename("mhr")
    miharu "「わあっ」"



    stop music fadeout 1
    hide lete with std_out

    "海晴の驚いた声は、滅多に聞くことができない。"

    "貴重なものが聞けたとにやりとしたのも束の間、私は自分の行動に後悔することになった。"

    play se "body_fall01"
    with quake_fast


    show rnk sun nor nor at std_cr with std_in
    voice get_voice_filename("rnk")
    rinka "「海晴！」"

    "レテに触れるか触れないかというところで、海晴は椅子から落下し、床に倒れ込んでしまった。"


    voice get_voice_filename("rnk")
    rinka "「海晴、大丈夫……？　ごめんね、無理させちゃって……」"

    show mhr sun pai lie rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「……違う、君のせいではないよ。この猫に触れようとしたら、急にふらついてしまってね。ぼくが自分から倒れたんだ」"

    "私は海晴の体を支えて、椅子へ戻るのを手伝った。"

    "海晴の体は思ったよりずっと華奢だったが、柔らかい。"

    show mhr sun sco vig rev with std_change

    voice get_voice_filename("mhr")
    miharu "「なんだったんだ……今のは……」"


    voice get_voice_filename("rnk")
    rinka "「はは……、もしかして海晴、本能的に動物駄目なのかもね。ほらレテ、あっちにエサとお水を置いておくよ」"


    play music audio.nichijo01


    voice get_voice_filename("cat")
    lete "「にゃおーん」"

    "レテはエサのにおいに釣られたのか、バックヤードの方へとちょこちょこと歩いて行った。"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「失礼した。大丈夫、落ち着いたよ。話を戻すけれどつまり、日辻さんの状態は、会ってみるまで分からない」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「うん――分かった。私よりもずっと早起きして、調べててくれたんだよね。ありがとう。直未が生きていると分かったから、私は何も心配してないよ」"

    show mhr sun nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……ああ。嬉しいな。凛火の笑顔を見ることができるのは。そろそろいい時間だろう。学校へ行こうか」"

    "私はテーブルのカップを片付けてから、登校することにした。"







    $ set_info_location("18")

    scene bg lion02 noon with fade_long
    pause 1

    show rnk sun nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「そういえば、学校はどうなってたの？　先週、私サボったことになってないかな？」"

    show mhr sun nor rea rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「伝え忘れていたね。爆発事故と火災のせいで、１週間休校だったのさ。だからぼくたちの知っている先週と、状況はそう変わらないと思うよ」"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「なら大丈夫だね。お待たせ、じゃ、行こう」"

    "晴れた日の道を、私たちは歩いて行く。"






    python:
        set_info_scene("112")
        set_info_time("noon")
        set_info_location("08")


    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show mao uni nor che rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「いやぁ、久々の学校は疲れますなぁ～。半分以上寝て過ごしてしまったのだよ……」"

    show rnk sun nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「真央の場合、いつもとあんまり変わらないんじゃ」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「いやしかし、１週間も休みっていうのはちょっとやり過ぎだよねぇ。さすがのうちも暇を持て余しちゃったよ」"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんもみはるんも、ここぞとばかりにお仕事してたみたいだしぃ」"

    "どうやら、世界はちゃんと変わっているらしい。"

    "真央と一緒に泣いたあの日も、なかったことになっているようだ。"

    "私の前で初めて涙を見せた真央。"

    "真央の強さと優しさは、私だけが知っている。"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、あはは……」"

    "ライオン館は休みにしていたはずだが、真央にそういう言い訳をしていた、というところだろうか。"

    "念の為、帰ったら売上のチェックをしよう。"

    "ああ、おばあちゃんへの連絡も抜けているはずだから、今夜しないと。"

    "色々なことを思い出したがゆえの、苦笑いだった。"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ま、一番大変なのはなおりんだよねぇ」"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「……ね」"

    "私は、あえて相槌で答えた。"

    "真央はそのまま、言葉を続ける。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「目の前で爆発が起きてさ。怪我はなかったからいいものの、現場にいた分マスコミにも色々聞かれただろうし」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「大部分は学校が対応して守ってくれたみたいだけどさぁ。それでもどこからかなおりんのことを捜すんでしょ」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「怪我は、なかった……」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「せっかく文化祭のために一生懸命頑張ったのに、１日目で終了だもんねぇ。対応は正しいのかもだけど、せめて中止じゃなくて延期にすればよかったのにぃ」"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「あ、なおりんはこれから、りーたんのところでアルバイトとして雇ったらどう？　うち、もしかして天才じゃ……」"

    "真央の言葉はもう、ほとんど聞こえていなかった。"

    "直未が無事と、選定とは関係のない真央から聞くことができたのだ。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたん？」"

    show rnk sun nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、ごめん。ちょっとぼーっとしちゃって」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんも、まだ休み気分が抜けてませんなぁ。さて、そろそろお昼を買いに……」"



    voice get_voice_filename("nom")
    naomi "「せーんぱいっ」"

    "真央が購買へ誘ってきたとき、突然その声が教室に響いた。"

    "まるで、晴天の霹靂だ。"

    show rnk sun sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「あっ……あっ……」"

    "全身の力が抜けるような錯覚。"

    "だが直後、私はその声の主に向かって駆け出していた。"


    play music audio.naomi
    scene ecg rinkahug with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「直未っ！」"


    voice get_voice_filename("nom")
    naomi "「きゃ、きゃぁっ……ちょっとどうしたんですかっ、凛火先輩っ！」"


    voice get_voice_filename("rnk")
    rinka "「直未、よかった、直未……」"

    "私は人目もはばからず、直未に抱きついていた。"

    "直未の体に顔をうずめているから見えないだろうけれど、思わず涙ぐんでしまっていた。"


    voice get_voice_filename("mhr")
    miharu "「…………仕方ないな」"


    voice get_voice_filename("mao")
    mao "「みはるんが……怒ってない……」"


    voice get_voice_filename("nom")
    naomi "「ち、ちょっとどうしたんですか？」"


    voice get_voice_filename("rnk")
    rinka "「ごめん、もうちょっとだけ、このままでいさせて……」"


    voice get_voice_filename("mao")
    mao "「り、りーたんが告った！？」"


    voice get_voice_filename("mhr")
    miharu "「それは違う。まあ、今くらいはいいさ」"

    "私はそのまま、５分以上直未に抱きついていた。"

    "そのほとんどは、私の涙が収まるまでの時間だった。"

    "事情を知らない生徒からすれば、真央も含めて、私が奇行に走ったと見えるかもしれない。"

    "間違いなく。噂の種にはなるだろう。"

    "でも、そんなことどうでもいい。"


    voice get_voice_filename("rnk")
    rinka "「生きていてくれて、ありがとう」"

    "いきなりそんなことを言われても、事情を覚えていない直未は訳が分からないだろう。"

    "それでも、私は言わずにはいられなかった。"








    python:
        set_info_scene("113")
        set_info_time("evening")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 noon with fade_long
    pause 1

    $ show_hud()

    show nom sun hes sor rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「お邪魔しまーす……」"

    show mhr sun sco wic at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「お待たせ。日辻さんとは、ちょうどそこで出くわしてね」"


    play music audio.nichijo01

    "放課後、海晴と直未はライオン館を訪れた。"

    "お店は結局、私の体調不良により１週間程度の休みということになっていた。"

    "おばあちゃんにもその連絡は伝わっていて、明日の火曜日から営業再開予定だ。"

    "海晴と直未はいつもの席に座り、私は海晴の隣に座った。"

    "直未に来てもらったのは、無論、これまでにあったことを話すためだ。"

    "どこまで打ち明けるべきかちょっとだけ迷ったけれど、私は全てを話すことに決めていた。"

    "中途半端に関わらせたら、同じ轍を踏むことになるだろう。"


    play music audio.disclose
    scene ecg girlstalkT2 anx with dissolve_long


    voice get_voice_filename("nom")
    naomi "「≪女神の選定≫……のことですね？」"

    "やはりと言うべきか。"

    "直未もまた、そのことを分かっていた。"

    scene ecg girlstalkS2 que nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「うん……どこまで、覚えてるの？」"


    voice get_voice_filename("nom")
    naomi "「私が覚えているのは、文化祭の前日、公園で凛火先輩と二人きりで話して……」"


    voice get_voice_filename("mhr")
    miharu "「二人きりで？」"

    "直未は一度引きつった顔で海晴を見たが、すぐに私の方へ向き直った。"

    scene ecg girlstalkT2 tro with dissolve


    voice get_voice_filename("nom")
    naomi "「えっと、それで文化祭の日にユウくんの姿を見つけて追いかけた先の教室で、爆発に巻き込まれたのは覚えているんです」"


    voice get_voice_filename("nom")
    naomi "「その後の私の記憶は……意識を失って病院で目を覚ましたってところから始まります。熱中症のような症状で、目立った外傷はなし」"


    voice get_voice_filename("nom")
    naomi "「奇跡が起こったって思いました。でも、何故かおかしいんです。そこからの記憶が、曖昧で……。休校になっている間に本を読んだり遊んだりしてたはずなのに、あんまり覚えてなくって」"


    voice get_voice_filename("nom")
    naomi "「その間に読んだ本も手帳に書いてあるんですけど……内容をあんまり、覚えていないんです」"

    scene ecg girlstalkS2 que sad with dissolve


    voice get_voice_filename("nom")
    naomi "「そして何より……、夢を見るんです。ゴールデンウィーク直前、凛火先輩が目の前で死んじゃう夢と……同じくらいの現実感で……わたしが、ユウくんに殺される夢を……」"


    voice get_voice_filename("nom")
    naomi "「でも、それが本当に見た夢か、夢を見たように思っているだけなのか、分からないんです」"


    voice get_voice_filename("rnk")
    rinka "「直未はもう、それがどういう意味か……分かってるんだね」"


    voice get_voice_filename("nom")
    naomi "「……はい。わたしはその時、死んでしまっていたんですね。そして犯人はユウくんだった」"


    voice get_voice_filename("nom")
    naomi "「ユウくんが脱落した後、選定期間中の行動がなかったことになった……だから、わたしを殺した彼の行動も……なかったことに……」"

    show ecg girlstalkS2 ser ser with ecg_change


    voice get_voice_filename("mhr")
    miharu "「……なるほど。日辻さんの場合は、記憶の改変具合が他の人より大きい、という推測くらいしか今はできないけれど、君は≪世界が改変≫された２つの記憶を比較的はっきりと持っている」"


    voice get_voice_filename("mhr")
    miharu "「そこまで理解しているなら、この件については、ぼくたちからこれ以上話すこともないだろう……辛い記憶だ。不用意に思い出させるのは忍びない」"

    scene ecg girlstalkT2 anx with dissolve


    voice get_voice_filename("nom")
    naomi "「未島先輩……ありがとう、ございます。それで……あの……凛火先輩、すみませんでした。きっと、先輩がユウくんを脱落させたん……ですよね？」"


    voice get_voice_filename("nom")
    naomi "「……わたしのために……そんな……」"

    scene ecg girlstalkS2 ser ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「日辻さん、それは！」"


    voice get_voice_filename("rnk")
    rinka "「いいんだよ」"

    "私は海晴を諌め、続ける。"


    voice get_voice_filename("rnk")
    rinka "「でも、海晴の言う通り。直未が謝ることは何もない。ユウの指名は、私が私の意志で決めたことなんだ」"


    voice get_voice_filename("rnk")
    rinka "「ま、色々大変だったんだ。他の参加者たちと協力したり、拳銃を持たされたりしてさ」"

    scene ecg girlstalkT2 sur with dissolve


    voice get_voice_filename("nom")
    naomi "「え、ええっ！？　どうやったらそんな状況に……」"

    "戸惑う直未に、私はオデットさんたちと協力することになり、東京タワーのテロを阻止し、再び列車テロに直面したことを、順番に話した。"

    "途中でちょっと休憩を挟むくらいには、長い話になった。"

    "海晴もおおまかな状況は理解していただろうけれど、ちゃんと話したのは今が初めてなので、かなり驚いた表情を浮かべていた。"


    play music audio.rinka
    scene ecg girlstalkS2 ser nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「それでさ……二人に言おうと思ってたことがあるんだ」"

    show ecg girlstalkS2 ser smi with ecg_change


    voice get_voice_filename("mhr")
    miharu "「なんだい？」"

    scene ecg girlstalkT2 anx with dissolve


    voice get_voice_filename("nom")
    naomi "「……なんですか？」"

    scene ecg girlstalkS2 ser ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「私は――生きたいって思った。この選定の途中、色んな想いを知って、色んな想いを託された」"


    voice get_voice_filename("rnk")
    rinka "「そのことを、無駄にはしたくない」"


    voice get_voice_filename("mhr")
    miharu "「ようやく、君は決意してくれたんだね」"


    voice get_voice_filename("rnk")
    rinka "「でもね、だから海晴を犠牲にするなんてことはできない。私の世界には、海晴も直未も、真央もおばあちゃんも、猫のレテだって、大切なものがいないと駄目なんだ」"


    voice get_voice_filename("rnk")
    rinka "「ソーニャがいつか、言ってたよね。運命が悪いように変わるなら、いいようにも変わるって。私はいい人でいるのはやめる。私にとって都合のいいように、運命を変えたい」"


    voice get_voice_filename("rnk")
    rinka "「方法は分からないけど、まだ何も分からないけど、少なくとも、直未を助けることはできた」"


    voice get_voice_filename("rnk")
    rinka "「だから私は、海晴と二人で生き残る。その可能性を、見つけてみせる」"

    "私自身、それを成し遂げる手がかりが今は何もないことは分かっている。"

    "でも、言葉にしたかった。"

    "それは、行動の第一歩だ。"

    show ecg girlstalkS2 ser tro with ecg_change


    voice get_voice_filename("mhr")
    miharu "「申し訳ないけれど、ぼくは賛同できないな。可能性は……なさ過ぎるだろう？」"


    voice get_voice_filename("rnk")
    rinka "「……そう言うと思ってた」"


    voice get_voice_filename("nom")
    naomi "「未島先輩、でも、もしそんな方法があれば、わたしは……」"


    voice get_voice_filename("mhr")
    miharu "「しかし、ぼくたちが最後の二人にならなければ、何も成し遂げられないことに変わりはないさ」"


    voice get_voice_filename("rnk")
    rinka "「……そう言うとも、思ってた。だからそれまでに、何か手掛かりを見つける」"

    scene ecg girlstalkT2 tro with dissolve


    voice get_voice_filename("nom")
    naomi "「なんだか、もう、わたしの出る幕はないって感じになっちゃいましたね」"

    scene ecg girlstalkS2 ser ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「ううん、違う。学園祭が終わったらあらためて――って言ったでしょ。だからこれは、お願い」"


    voice get_voice_filename("rnk")
    rinka "「ここからは、私たち３人で戦おう。相手は他の参加者じゃない。私たちの、運命だ」"

    "私は、ようやくその言葉を口にすることができた。"

    "女神の選定が始まった時からずっと、そう言いたかったのかもしれない。"

    "迷っているままでは、言えなかった。"

    "でも、今は違う。"

    "私はもう、生きることを迷わない。"

    show ecg girlstalkS2 ser smi with ecg_change


    voice get_voice_filename("mhr")
    miharu "「あくまで方法があればという前提ではあるけれど、賛成させてもらうよ」"

    scene ecg girlstalkT2 uwa with dissolve


    voice get_voice_filename("nom")
    naomi "「はい！　わたしもその言葉を……待っていました！」"

    scene ecg girlstalkS2 smi smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「――ありがとう」"

    "二人の笑顔と、私はしっかりと向き合うことができた。"


    scene bg lion01 noon
    show mhr sun sco smi at std_c
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「ではぼくは、バイトがあってね。ここで失礼させてもらうよ」"

    hide mhr with std_out

    "海晴はそう言って、ライオン館を後にした。"







    python:
        set_info_time("evening")
        set_info_location("18")


    stop music fadeout 1
    scene bg lion02 evening with fade_long
    play music audio.growapart
    pause 1

    show rnk sun nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ねえ、海晴。隠し事はもう、なしにしようよ。今日はバイトじゃなくてさ……スケールさんたちと会いに行くんでしょ？」"

    "海晴がライオン館を出た直後、私はその後ろ姿を追っていた。"

    "直未には一言断って、ライオン館で待っていてもらっている。"

    "二人で話したい、ことがあったからだ。"

    show mhr sun nor ser rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「ああ、そうだ。ぼくは彼らと協力してオデット、アランの両名を脱落させる。そして協力関係を維持しつつスケールとフェデリーコの情報を探り、彼らも脱落させてみせる」"

    show mhr sun sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「性質としては、悪だね。まさか君はこの期に及んで、人を裏切ることはいけないとでも言うつもりかい？」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……違うよ。海晴にはさ、それが本当にできるの？」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「やり遂げるさ。君のために」"

    show rnk sun ang an2 with std_change

    voice get_voice_filename("rnk")
    rinka "「そうじゃないだろっ！」"

    "大声を出した私を、海晴は無言で見つめる。"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「……ごめん、怒っちゃった。でも、聞いて。私は海晴の行動に文句を言うつもりはない。むしろ、逆。私はもう、一人で海晴に背負わせたくはないよ」"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「私も一緒に、背負わせて欲しい。直未が私にそう言って救われたように、私も海晴の力になりたい」"

    show mhr sun sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「また、日辻さんかい？」"

    show rnk sun sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ、いや、そういう意味じゃ……」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「――まあいいさ。君の気持ちは嬉しいけれど、気持ちを受け取るに留めておくよ。さっきも言っただろう？　ぼくたちは、まず最後の２人にならなくてはならないんだ」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君は、その先の方法だけを探せばいい。君にははっきり言わなくては伝わらないね。他の参加者のことは、ぼくに任せてくれ」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「今回の件も、君は自ら危険に飛び込んだ。運命に縛られて死なないだけで、火災というのは、火傷のような外傷だけでなく、煙や酸欠空気による内臓への損傷の危険性もあるんだ」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「何度も指摘してきたはずだ。君は他の参加者に深入りし過ぎる。だからね、君が運命と立ち向かうと決めたのはぼくにとって朗報だったよ」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴……まさか。私を他の参加者から遠ざけるために、さっきは同意したの？　もしかして海晴は、運命に勝てるなんて、思っていないの？」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「さて。そろそろ行かないとバイトに遅れてしまう。短時間のシフトだけれど、入っているのは嘘じゃないんだ」"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「私は信じてるよ。私たちなら、運命を変えられるって」"

    show mhr sun sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくも凛火を信じている。けれどそれ以上に、凛火を愛している」"

    hide mhr with std_out

    "そう言うと、海晴は駅の方へ向かって行った。"

    "これ以上、私は海晴にかける言葉が思いつかなかった。"

    "反論ができない。"

    "他の参加者の情報も、私たち２人が生き残る算段も、私は何も持っていない。"

    "ただ理想を語ったに過ぎないから、海晴は私を突き放したのだ。"

    "海晴はこれまでと同じように、自分の調べた情報について私に最低限しか話すことはないだろう。"

    "だが、私だって今まで通りではいられない。"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「運命を変える方法を、私は見つけるよ」"

    "海晴は立ち止まらない決意をしている。"

    "それは、≪女神の選定≫が始まってからずっとだ。"

    "だったら私も、立ち止まってはいられない。"

    "そしてもう海晴に、私のために嘘をつかせたくない。"







    python:
        set_info_time("night")
        set_info_location("04")

    stop music fadeout 1
    scene ecg nighttalkT1 anx with fade_long
    pause 1

    $ show_hud()


    voice get_voice_filename("nom")
    naomi "「あの……大丈夫でしたか？」"


    voice get_voice_filename("rnk")
    rinka "「たぶん、直未が心配していた通りになったよ」"

    "私が答えると、直未ははっとした顔を浮かべていた。"

    "直未が賢い子なのは、十分知っている。"

    "私と海晴がどんなことで言い合ったか、気付いているに違いない。"


    play music audio.investigation
    scene ecg nighttalkS1 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「でも、だからこそ。私はちゃんと二人とも生き残れる方法がないか探すんだ。手がかりは、完全にないってわけじゃないんだ。例えばこの本」"


    voice get_voice_filename("rnk")
    rinka "「≪女神の選定≫のものって思い込んで最初に考えるのをやめちゃったけどさ、デザインとか装丁とか、もっと注意して調べてみるべきかもしれない」"


    voice get_voice_filename("nom")
    naomi "「せんぱい、それを調べてどうするつもりなんですか？」"


    voice get_voice_filename("rnk")
    rinka "「≪女神の選定≫、ううん。≪女神≫そのものを、知る」"

    "夢の中に現れた空間や、改変される現実世界に気をとられて、私たちはその事象を受け入れていた。"

    "結果を見て信じ、そのルールの中で抗うことをしなかった。"

    "でも疑うべきは、その存在そのものだったのだ。"

    show ecg nighttalkS1 smi with ecg_change


    voice get_voice_filename("rnk")
    rinka "「それに、まず≪パルカ≫って名前を調べるべき、なのかな。私は全然詳しくないけど、神話とか、そういうのもあるよね」"

    scene ecg nighttalkT1 smi with dissolve


    voice get_voice_filename("nom")
    naomi "「それなら、ちょっと力になれるかもしれません！　わたし、神話のことを調べてたんです。女神っていうくらいだから、何か分かるかなって……」"


    voice get_voice_filename("nom")
    naomi "「結局神話は神話だなって思って気にしていなかったんですけど、今はどんな情報が役に立つか分からないですもんね」"

    "直未は手帳を取り出して、前の方にあるページを開いた。"

    "本を読みながら、メモをとっていたのだろう。"

    "一度黙読してから、私に向き直る。"

    show ecg nighttalkT1 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「パルカっていうのは、ローマ神話の運命の女神の総称のようです」"


    voice get_voice_filename("nom")
    naomi "「デキマ、ノーナ、モルタっていう３種類がいるそうで、それぞれギリシア神話のモイラっていう運命の女神と対応しているって、書いてありました」"


    voice get_voice_filename("nom")
    naomi "「人間が生まれたときに、その人の人生――運命を決定する女神たちだそうです」"

    scene ecg nighttalkS1 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「運命の女神……パルカが夢の世界で言っていたのと同じだね。≪運命の大広間≫に、≪運命の大時計≫」"


    voice get_voice_filename("rnk")
    rinka "「時計、歯車。夢の世界はそういうもので作られていた。私たちに割り当てられた12の番号も、時計の文字盤の数と一致している……」"


    voice get_voice_filename("nom")
    naomi "「時間の神っていうと、ギリシア神話のクロノスって神様の方が有名ですよね……」"

    show ecg nighttalkS1 ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「でも私たちの≪氏名≫≪死因≫≪未練≫のカードは≪現在≫≪過去≫≪未来≫の象徴で、私たちの運命を表してるって、パルカは言ってた」"

    scene ecg nighttalkT1 tro with dissolve


    voice get_voice_filename("nom")
    naomi "「運命を時間で表現しているってことなんでしょうか……。そういえば凛火先輩のカードブックも、歯車みたいな飾りがついてますよね」"


    voice get_voice_filename("nom")
    naomi "「時計の中身って、歯車がたくさんありましたよね。だから歯車から時計、時計から時間、時間から運命をそれぞれ連想できるようになっている――そういうことなんでしょうか？」"

    show ecg nighttalkT1 uwa with ecg_change


    voice get_voice_filename("nom")
    naomi "「本だったら、稀に≪運命の歯車≫なんて表現も出てきますしね」"


    voice get_voice_filename("rnk")
    rinka "「でも、≪夢の世界≫のモチーフが分かったってだけだよね。うーん、全然、核心に迫ってる気がしない……」"

    show ecg nighttalkT1 anx with ecg_change


    voice get_voice_filename("nom")
    naomi "「モチーフ？　ちょっと待ってください……それって、おかしくないですか？」"


    voice get_voice_filename("rnk")
    rinka "「おかしい？　直未、何か気付いたの？」"

    show ecg nighttalkT1 tro with ecg_change


    voice get_voice_filename("nom")
    naomi "「い、いえ、そういうわけでは……。でも、パルカさんっていうのは女神様なんですよね？　なのに人間の考えるモチーフと合致しているって、何か違和感があって……」"

    scene ecg nighttalkS1 que with dissolve


    voice get_voice_filename("rnk")
    rinka "「パルカは、≪夢の世界≫っていう人間の認識できないものを、認識できるように作ったって言ってた」"


    voice get_voice_filename("rnk")
    rinka "「だから人々の想う運命の女神っていうイメージから、時計とか歯車とかがモチーフになった空間が生まれても、おかしくないんじゃないかな？」"

    "現に、私たちは連想ゲームのようにその言葉に辿り着いた。"

    "それに認知というのは、≪女神の選定≫においてカードの内容の決定にも関わる重要な要素だ。"

    scene ecg nighttalkT1 tro with dissolve


    voice get_voice_filename("nom")
    naomi "「そうなん、ですけど……ご、ごめんなさい。凛火先輩の言う通りなんですけど、ちょ、ちょっとだけ、変な感じがして」"


    voice get_voice_filename("rnk")
    rinka "「謝らなくていいよ。直未が感じた違和感は大切にして。私たちはそういうのを持たずに目の前の出来事を受け入れちゃってたわけだし」"

    "直未は頷いたものの、まだ申し訳なさそうな表情を浮かべていた。"

    "私には、直未の感じていることがよく分かっていない。"

    "きっとまだ根底には、人ではない女神のことなのだから考えても無駄、という思考があるからだろう。"

    "そういうところからやめようと、決意をしたばかりなのに。"


    voice get_voice_filename("nom")
    naomi "「うう……。でもやっぱり、あんまり役に立てませんでした……」"

    scene ecg nighttalkS1 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「そんなことないよ。ありがとう」"

    "本来なら、私がもっと早く疑問に思わなくてはならなかったのだ。"

    "にもかかわらず、直未は私よりもずっと先に調べてくれた。"

    show ecg nighttalkS1 que with ecg_change


    voice get_voice_filename("rnk")
    rinka "「さて、今日はここまで……かな。ねえ直未、明日の放課後、図書館に一緒に行ってくれない？」"


    voice get_voice_filename("nom")
    naomi "「図書館……はい、もちろんです！」"

    show ecg nighttalkS1 nor with ecg_change


    voice get_voice_filename("rnk")
    rinka "「ありがと。明日は、カードブックについて調べよう」"



    scene bg lion01 night with fade_long
    pause 1

    "外はすっかり暗くなっていたので、私は直未を駅まで送った。"

    "一人で大丈夫と言われたが、ライオン館の場所はオデットさんに知られている。"

    "恐らく、アランさんもすでに調べているかもしれない。"

    "あの二人が今私を積極的に狙う理由も考えられないが、直未を夜道で一人にするのは心配だ。"









    python:
        set_info_scene("114")
        set_info_time("night")
        set_info_location("34")


    stop music fadeout 2
    scene bg bar with fade_longest
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    show mhr sun sco dis rev at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「何度も言うけれど、ぼくは一介の高校生なんだ。あまりこういう店に呼び出さないでくれ。それに、アルバイト帰りでね。疲れているから、手短にして欲しい」"

    show fed sta nor smi behind mhr at std_r with std_in

    voice get_voice_filename("fed")
    federico "「アルバイト……例のなんとか喫茶か。あそこは辞めた方がいいぜ？　この辺りの夜の仕事の方が時給はいいみたいだ」"

    show sca sta nor smi rev behind mhr at std_l with std_in

    voice get_voice_filename("sca")
    scale "「そうじゃないさフェデリーコくん。あの場所にはわびさびがあっただろう？　ミハルもそこにやりがいを感じているのさ」"

    show mhr sun sco vig with std_change

    voice get_voice_filename("mhr")
    miharu "「……今すぐ辞めたいくらいだよ」"

    "海晴は、新宿にあるバー≪MILK CROWN≫を訪れていた。"

    "いつもの席に、スケールとフェデリーコが座っている。"

    "当然ながら、そこにオデットの姿はない。"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「オデットさんの姿がないね」"

    "凛火から事情は聞いているが、海晴は知らない振りをした。"

    "彼女が『荒事は自分の仕事』と啖呵を切って以来、初めての集まり。"

    "海晴は、今日までの間にスケールたちがオデットとどんなやり取りをしたのか、気になっていた。"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「ふぅむ。聡明な君ならもう気付いているだろう？　彼女は離反したよ」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「そしておれの提供した情報を元に、君のお友達と協力してユウの脱落まで成し遂げた、ということだね」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「あいつは恐らく、アランとも協力してたはずだ」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「どうしてそう思うのかな？」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「ただの勘だ。リンカってのは、戦いになったら足手まといだろ」"

    "海晴はむっとした表情を浮かべたが、そのままフェデリーコが話すのを待った。"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「直後の報道じゃ、銃弾で撃たれた男がいたみたいじゃねぇか。その後行方不明なんて、アラン以外に考えられねぇ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「なるほど。そうなると問題は、リンカはいいとして、オデットとアランが未だ協力関係を結んでいるかが問題だな」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「どっちの可能性もあるな。アランの情報網はオデットも評価してた」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「となるとおれたちは、二人の脱落が急務だな」"

    "海晴は見かけ上、自分・スケール・フェデリーコと凛火・オデット・アランの３対３となっているこの構図が、実際は異なっていることを理解していた。"

    "スケール・フェデリーコ、海晴・凛火、オデット、アラン。"

    "実際は２対２対１対１、だ。"

    "海晴にとっては凛火と自分の２をうまく隠し通すことが課題。"

    show mhr sun sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「両方同時は……現実的ではないね。ぼくがアランの≪死因≫を教えてもいいけれど、まだ彼の≪未練≫の手がかりはないのだろう？」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「雑誌のインタビュー記事や過去の公な発言を洗ってみたが、結果は想像通りだ」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「彼の身辺を調査させているが……家族構成程度しか分かっていない」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「家族構成？」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「母親は彼が幼い頃に病死。父親は彼が16歳の頃に殺害されている」"

    show fed sta nor ama with std_change

    voice get_voice_filename("fed")
    federico "「殺害？　そりゃ一体……」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「アランの父親は、元々小さな宝石商を営んでいたらしい。インド国内の採掘場から原石を買い付けて、加工会社へ卸していたそうだ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「小金持ちになった弊害かは分からないけれども、どうやら欲が出たらしくてね。貧しい人々への金貸しも始めたらしい」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「金融業者なんて立派なものじゃない。日本ではヤミ金というのだったかな？　かなりあこぎな商売だったそうだ」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「恨みを買ったってわけだな。そりゃ、殺られた方が悪いわな」"

    "自らもマフィアとして金融業を営んでいたフェデリーコならではの発言だ。"

    "スケールもその通りと言わんばかりに、肩を竦めた。"

    show mhr sun sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「なるほどね……」"

    "海晴はその話を聞いて、自分の持っている≪死因≫のカードと内容を紐付けていた。"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「その後、10代だったアラン・スコーピオンが父のルートを利用して会社を立ち上げ、財を成したのは有名な話だね」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「ちなみに現在の彼の家族構成は、弟が４人と妹が１人だそうだ。彼ら家族は、アランの収入が支えているらしい」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「だとすれば、その家族ってのがアランの未練じゃねぇのか？」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「おれもそれを想定したんだけどね。残念ながら、まだこれ以上の背景情報が手に入っていないんだ」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「会社やら経営、財産とかは想定してみたけど違ったからよ。あんたに頼るしかないんだ。頼むぜ？」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「家族という線はおれも濃厚だと思っている。任せてくれとは言わないが、おれの仲間には高い報酬を約束している。必ず情報をつかんでくれるさ」"

    show mhr sun sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「君の仲間、かい？」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「おっと。これ以上はおれの情報に関わるから教えられないね。しかしまあ、ジャーナリストのようなものと思ってくれ」"

    "海晴は再び、なるほど、と頷いた。"

    show mhr sun sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「それでは、まだアランの≪死因≫は教えられないね」"

    show fed sta nor pa1 with std_change

    voice get_voice_filename("fed")
    federico "「はァっ？　なんでだよ！」"

    show mhr sun sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「向こうのグループの凛火と同じだ。非力で社会的な力を持っていないぼくは、用済みと判断されればおしまいだからね」"

    show sca sta nor lau rev with std_change

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡＨＡ、非常に合理的な判断だね。構わないよ。アランの情報は、≪未練≫が判明したら教えてくれ。≪死因≫まで調べなくていいというだけで、気が楽だ」"

    show fed sta nor bad with std_change

    voice get_voice_filename("fed")
    federico "「そうなると……オレたちも黙っているわけにはいかねぇ」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「分かっているさ。オデット……君の元仲間を狙うわけだろう？」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「人が嫌がる言い方を心得てるみてーだが、それこそあんたのはオデットほどじゃねぇな」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「まあいい。オデットの死因の方なら、オレはすでに手に入れている」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「本当か？　いつ？」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「昨日の夜だ。一人になってふと、自分の怪我を見ていて思い出したんだ」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「オレは死の間際、あいつと同じ場所にいた」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「詳細はオレの情報にも繋がっちまうから教えられないが、その時、あいつは腹に傷を負ってた」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「だが、見ての通り、選定が始まってからのあいつに傷はない……。つまりその傷が、オデットの≪死因≫だったってわけだ」"

    "フェデリーコはカードブックから１枚のカードを取り出し、ちらつかせた。"

    "≪Ⅺ・失血死≫、カードにはそう書かれていた。"

    python:
        add_character_cards("fed", ["11_death"])
        add_character_cards("ode", ["11_death"])

    "しかし、スケールや海晴のところにはそのカードは作られない。"

    "背景情報がないため、オデットの死因を理解したことになっていないからだと、２人とも分かっている。"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「はぁ。君はそんな大事なことを、今日まで忘れていたのか？」"

    show fed sta nor pa1 with std_change

    voice get_voice_filename("fed")
    federico "「う、うるせぇっ！　あんな体力バカのゴリラ女とずっと一緒にいたんだ。思い出すモンも思い出せなかったんだよ」"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「死の瞬間、同じ場所にいた――と言っていたね？　その場合、オデットさんも君の≪死因≫を持っていると思った方がいいのではないかい？」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「ああ。その可能性はオレも元から想定してたさ。だが、≪未練≫までは持っていないだろうよ」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「でなけりゃ、あいつを裏切ったオレが前回の選定で指名されてない理由が説明できないからな」"

    show mhr sun nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「なるほど。それもそうだね」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「それより、だ。ミハル、あんたはオデットの≪未練≫に心当たりがあると言っていたな？」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「おれも覚えている。このままでいけば、オデットを指名するのはフェデリーコくんになる」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「そろそろ、オデットの≪未練≫を教えてくれないか？」"

    show mhr sun nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは彼女の未練そのものを知っているわけではないよ。あくまで心当たりがあるだけだ」"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「それで構わないというのなら――そうだね、話すならばこのタイミングしかないだろう」"


    play music audio.investigation

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「子供――ぼくはそれが、彼女の未練に繋がるものだと思っている」"

    "海晴はそれから、その理由を話した。"

    "きっかけはソフィアの一件だ。"

    "彼女に対して、≪世界を見る≫機会を与えたこと。"

    "あの時、ソフィアの感情など無視して、オデットは情報を聞き出すだけでよかったのだ。"

    "ソフィアがオデットの情報を話すリスクがあったとはいえ、方法はいくらでもあったはず。"

    "非効率な方法をとってまで、オデットはソフィアに慈悲を与えた。"

    "そしてソフィアも、オデットのその決断を信じた。"

    "海晴はソフィアが見た目と年齢に比べて賢いことを知っていたから、素直にオデットを信じたことを疑っていた。"

    "オデットが約束を反故にする可能性の方が高いくらいだっただろう。"

    "海晴はこのことに違和感をもつと同時に、ある仮説も立てていた。"

    "――ソフィアはオデットの未練を知っていたから、自分に慈悲を与えたと分かった。"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「あの女は感情で動く女だ。仕事も好き嫌いで受けるか受けないかを決める……そんなことを話した記憶はあるぜ」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「しかし……子供、か。当然これだけではカードも生まれない」"

    show mhr sun sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「ここまでは、ある程度の状況証拠に基づいた仮説さ。ここからが、ぼくの推論だ」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「オデットさんは自分で自分の生き方を選べる人。フェデリーコさん、ぼくの考えは間違っているかい？」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「あいつほど人の指図を受けない奴は珍しいと思うぜ」"

    "フェデリーコは、深く頷きながら答える。"

    "傍らのスケールは海晴の言いたいことを理解したのだろう、顎に手を当て、「そうか」と呟いた。"

    "海晴の視線を受け、スケールが思いついたことを話し始める。"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「彼女は未婚で子供もいないはず。しかし≪子供≫という言葉が関連して、未練になるほどの強い想いとなると……彼女には子供を産めない理由があるということだろうか」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「たとえば、肉体的な理由……」"

    "ここまで話しても、まだカードは生成されなかった。"

    "しかしスケールは、あながち遠くない推論だとも思っていた。"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「まだ何か足りないようだけれど、おれは君の話がオデットの未練からそう遠くないとも思う」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「分かった。オデット・マランソンの過去の病歴や手術歴を調べさせる。産婦人科系に絞って……だ」"

    show mhr sun sco con with std_change

    voice get_voice_filename("mhr")
    miharu "「話が早くて助かるね。では、ぼくはもう失礼するよ。また君の情報が集まったら呼んでくれ。前にも言ったけれど、高校生のぼくが遅くにこういう店に出入りするのはよくないからね」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「まあ待てよ。場所を変えたっていい。もう少し付き合わないか？　朝まで過ごせば、かえって問題なくなるぜ？」"

    show mhr sun sco vig rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……はぁ。下品で、最低だよ」"

    "フェデリーコに冷たい視線を浴びせながら、海晴は店から出て行った。"

    "その後、スケールとフェデリーコが二人で朝まで飲んでいたことを、海晴は知る由もなかった。"









    python:
        set_info_scene("115")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    show rnk paj arm ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「直未が……生きてた……」"

    "一日を終え、私はその喜びをひしひしと感じていた。"

    "目の前で命を奪われた直未と、再び出会うことができた。"

    "それは、私にとって奇跡に等しい。"

    "同時に、ユウの死に際の叫び声も思い出さずにはいられなかった。"

    "紛れもない、彼の本心。"

    "死の瞬間の映像も、私は見ていた。"

    "私と表裏一体の、電車での死。"

    show rnk paj arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……でももう、決めたから」"

    "思い出しても、立ち止まることはない。"

    "後悔はしていない。"

    "彼の燃やした命の先に、私は自らの意志で踏み出したから。"

    show rnk paj nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「さて、と」"

    "明日から、ライオン館も開店だ。"

    "すでにおばあちゃんとのお店に関するメールのやり取りは終わっているし、発注作業も済ませている。"

    "あとは寝るだけだったが、私はスマートフォンを手に取った。"

    "ちょっとだけ、おばあちゃんと電話で話そうと思った。"

    "喜びと悲しみ、安心と切なさの混ざった感情の行き場に困っていたから。"

    show rnk paj arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「たまには甘えたっていい――滅多に泣かなかった私に、おばあちゃんは口癖のように言ってたっけ」"

    "だから今日くらいは――いいよね。"




    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.relaxtime
    pause 1

    show rnk paj nor smi at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「うん……、うん……」"

    "おばあちゃんとの電話は、思っていたよりも長電話になっていた。"

    "長くなった原因は、私が赤ちゃんの時の話題にあった。"

    "今まで詳しく聞いたことのなかった、私が生まれたときのこと。"

    "私が生まれたのは、どうやら両親が火事で亡くなったのとほとんど同じタイミングだったそうだ。"

    "その頃のショックと猛烈な忙しさのせいか、詳しいことはまるで靄がかったようにおばあちゃんも思い出せないらしい。"

    "私のお母さんが私を産んだ瞬間のことは、誰も覚えていないそうだ。"

    "恐らくお父さんが覚えているのだろうけれど、すでにこの世にはいない。"

    "まるで突然そこに現れたかのように、私は焼け跡で泣いていたという。"

    "おばあちゃんは、いつ私の名前を聞いたのかも覚えていないらしい。"

    "ただし、私の母親が私に凛火という名前を与えたということだけは、はっきりと覚えていた。"

    "そしてその意味も。"

    "私としては、中々に衝撃的な話だった。"

    "けれど一番の当事者が亡くなっているのだから、色々な状況が曖昧でもおかしくはない、と自然と受け入れていた。"

    "ショックなことが続いたとき、ぼんやりとしたまま日々を過ごす感覚は、分かる。"

    "現に私は選定の参加者になるきっかけとなった電車での火事、そしてその時期周辺の記憶を失っていたのだから。"

    "おばあちゃんにしてみれば、もう16年も前の話。"

    "何かのきっかけで思い出すことはあるかもしれないけれど、私自身が今生きていることから考えると、思い出さなくても困ることはない。"

    "一月前だったらもやもやしっぱなしだっただろうに、私はすっかり開き直っていた。"

    show rnk paj nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、どうして……この話を？」"

    "私の質問に、おばあちゃんは少しだけ言い淀んだ。"

    "はきはきとものを言うおばあちゃんが私と話してこうなるのは、珍しい。"

    "受話器の向こうからうーんと唸る声が聞こえて、おばあちゃんは口を開いた。"

    "その後はお互い体に気を付けようね、なんてそんな話をして、電話を切った。"

    show rnk paj nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「今日のおばあちゃん、ちょっと変だったな」"

    "――生きているって、命があるって、奇跡のようなことだからだよ。"

    "それは、私の質問の答えにはなっていなかった。"

    "おばあちゃんの口癖でもない、初めて聞く言葉。"

    "だがその言葉は、私の中で奇妙な熱を持っていた。"




    python:
        set_info_scene("116")
        set_info_time(None)
        set_info_location("01")


    stop music fadeout 2
    scene ecg pattern nor a with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    "……。"

    "…………。"

    "あれ、おかしいな。"

    "選定の日ではないのに、意識がある。"

    "この感覚も、何度目だろうか。"

    "女神の選定が行われる運命の大広間ではなく、例えるならそう、夢の中にあるもう一つの世界。"

    "すぐ、男の人の声が聞こえるんだ。"

    show let sta nor sm1 at std_c with std_in


    voice get_voice_filename("let")
    lete_unk1 "「お久し振り、でもないね。もう、そんな御託はいらないかな」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「自分の運命と決着をつけた君に待ち受けているのは、きっとより困難な道だろう」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「無限の可能性の中に、君が道を作っていくんだ。君の命が軌跡を作っていくんだ。それは決して奇跡なんかではないね」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君たち人間の、意志の力というものだろうか。私は、ようやく興味を持ち始めたさ」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「おっと、無駄話はいいね。私が君の夢に顔を出すことが一体何を意味するのか、君はもう分かっているのだろう？」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君の忘却がまた一つ、紐解かれるということさ」"

    "体の自由もなく、意識も朦朧としている。"

    "鬱陶しい彼の声が遠くなった頃、私の意識はまた深いところへ落ちていく。"








    stop music fadeout 2
    scene black with dissolve_longest
    pause 2
    play music audio.firedeath
    play ambient "fireloop" fadein 5
    pause 1

    "炎の中にいた。"

    "身を焦がすような炎だった。"

    "肌はただれ、肺は煙で焼かれている。"

    "徐々に命が灰になっていくのだと、もう指先ひとつすら動かせない私には実感があった。"





    linda_unk1 "「――――」"


    linda_unk1 "「――――！」"


    linda_unk1 "「――――！　――――！」"

    "誰かが何かを叫ぶ声が聞こえた。"

    "しきりに何かを叫んでいる。"

    "炎は広がっていき、叫び声は空気の震える音にかき消される。"

    "声が全く聞こえなくなる頃、私の意識も消えていった。"

    $ add_seen_chapter("8-1")

    stop ambient fadeout 2








    python:
        set_info_scene("117")
        set_info_date(6, 19, "tue")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom morning large:
        zoom 1.5
        align (0.0, 0.6)
    with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    play se "futon_dive1"

    show rnk paj sur su2 up rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「うわあぁっ！」" with quake_fast

    "私は声を上げて目を覚ましていた。"

    "恐ろしい夢から、嫌な起き方をしたのだ。"

    show lete normal at cat_r with std_in


    voice get_voice_filename("cat")
    lete "「にゃーお」"

    "そう思ったら、ベッドの上、というか私の上には黒猫のレテが乗っかっていた。"

    "それは、いつかの朝の焼き直し。"

    "あの夜に見た悪夢は私の記憶だと思っていた。"

    "私が電車の中で爆発に巻き込まれ、命を落とした因果の刻。"

    "なかったことになっている、可能性の一つ。"

    "この、瞬間まで。"

    "私が一つの決着を迎えたからだろうか。"

    "それに合わせて、世界が再び改変されたからだろうか。"

    "答えは分からない。"



    hide lete with std_out

    show rnk paj nor nor up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あの夢は、違う。あの時の記憶じゃ……ない」"

    "だとすれば、それはもっと原初の記憶なのだろうか。"

    "私が生まれてすぐ両親が火事で死んだこと、焼け跡の中に私がいたこと、その話をした直後だから、気付いたのだろうか。"

    "だが、それにも違和感があった。"

    "夢の中で私は、目の前の出来事を理解していた。"

    "生後間もない赤ちゃんが、あんな風に記憶できるとも思えない。"

    show rnk paj nor que up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「なら、あの夢は一体……？」"


    stop music fadeout 1

    show lete normal at cat_r with std_in


    voice get_voice_filename("cat")
    lete "「にゃーお」"

    show rnk paj arm lie up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あんたに問い掛けたんじゃないって」"

    "呟いても、返ってきたのは猫の鳴き声だけ。"

    "なんだか、気が抜けてしまった。"

    "私はレテを撫でてから、朝の仕度を始めることにした。"






    python:
        set_info_scene("118")
        set_info_time("noon")
        set_info_location("15")


    stop music fadeout 1
    scene bg schoolrooftop noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show mao uni sel glo rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「――ってぇ、今日はまたりーたんと二人だねぇ」"

    "昼休み、私は真央と屋上へ来ていた。"

    "悪夢のせいで早く目が覚めてしまったので、今日は珍しく手作り弁当だ。"

    "真央のご飯は、フルーツサンドとあんパン。いちご牛乳も。"

    "……見ているだけで胸やけしそうだ。"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「今日は甘党の気分なのだよ」"

    "そう言うと真央は、むしゃむしゃとご飯を食べ始めた。"

    "海晴はというと、今日は欠席。"

    "軽い言い合いをした後だから心配だったけれど、チャットアプリでは「心配いらないよ」と連絡が来ていた。"

    "理由も書かれていないのに心配するなというのは無理な話だ。"

    "とはいえ海晴はスケールたちとやり取りをしているのだから、私が出しゃばれば迷惑をかけてしまうに違いないので、大人しくしていることに決めたのだった。"

    "放課後は直未と図書室へ行く約束をしている。"

    "誘われた時は行こうか迷ったが、うちの高校はそれなりに歴史が古いため、参考になる資料などがあるかと思ったのだ。"

    "もっともお店の仕事があるので、デザイン関係の本を何種類か借りていくだけの予定ではあるのだけれど。"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたん、また難しい顔してる」"

    show rnk sun arm lie at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ああ、ごめんごめん」"

    "言って、私はお弁当に口をつけた。"

    "作り慣れていないとはいえ、今日は中々うまくできたと思う。"

    "真央と話しながらお弁当を食べていると、私はまだちゃんと日常にいるのだと実感できる。"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ね、りーたんさ」"

    "日常会話を割って、真央が静かなトーンで呼びかけてきた。"

    "私はそれまでしていた少女漫画の話をすっかり忘れて、真央に耳を傾けていた。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんやみはるん、なおりんがみんなで何をしてるかって知らないし、ハブられてるわけじゃないからどーでもいいんだけどさぁ」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ゴールデンウィークが明けてからずーーーーーっとみんなの様子が変なのは分かってるけどさ」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「みんなで映画とカラオケとボウリングと水族館に遊びに行く約束もなくなっちゃたりしてたけどさ」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……ボウリングと水族館が増えてるよ」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「いやぁ、次に持ち越し的な？　したいことはいっぱいあった方がいいしぃ」"

    "そして真央は少しだけ躊躇ってから、続けた。"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「うーん、いいや。ここまで。話の腰折られたしぃ」"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、やめとこ」"

    "私たちは二人で、頷いた。"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「どーせほとんど毎日、ずーっと顔合わせるんだもんねぇ」"

    "そして私たちは、また他愛のない話に戻った。"

    "予鈴が鳴って片付けを始めてからも、教室へ戻っている間も。"








    python:
        set_info_scene("119")
        set_info_time("evening")
        set_info_location("17")


    stop music fadeout 2
    scene bg shinjukugyoen evening with fade_longest
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "学校を休んだ海晴は、新宿にある大きな公園にいた。"

    "ライオン館から近い場所であり、獅子舞凛火の思い出の場所。"

    "ただし海晴が一緒にいるのは、凛火ではなかった。"

    show ode noj arm smi rev at std_cl with std_in

    voice get_voice_filename("ode", 421)
    odette "「かぁー、来ちまったな。運命の終着点ってのによ」"

    show mhr sun nor rea at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「――いつからここがその場所だと気付いていたんだい？」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「気付くわきゃねえだろ。調べたんだよ。あの時計台はこの国じゃあ珍しいからな。そう時間はかからなかったさ」"

    show mhr sun sco con with std_change

    voice get_voice_filename("mhr")
    miharu "「さすがの君も、勘だけで見知らぬ土地を当てられるわけはないね。くすっ。おかしな質問をしてしまったよ」"

    scene ecg odettomiharupark b with dissolve_long

    "海晴とオデットは、ベンチに座ることもなく、その時計台を眺めて話していた。"

    "こうなったいきさつは、オデットを知る者であれば驚くようなものではなかった。"

    "海晴が登校しようとしたとき、オデットが彼女の前に現れたのだ。"

    "ちょっと付き合ってもらうぜ――そんな言葉で、海晴は逆らう間もなく連れて行かれた。"

    "その時初めてフェデリーコがどんな扱いを受けていたか海晴は知ったのだが、そんなことよりも警戒心で一杯だった。"

    "だが直後、彼女の言葉に拍子抜けすることとなる。"

    "オデットは美術館に行きたがっていたのだ。"

    "オデットの言葉は断る方が体力を使うという予感があったので、海晴は大人しく従い、美術館へと足を運んだ。"

    "そこで見たのは常設展ではなく、期間限定の特設展の方だった。"

    "あまりにも有名で偉大な画家、ゴッホにスポットを当てた展覧会だ。"

    "海晴は絵画というものを知識でしか知らなかったので、美術を楽しむというよりかは知識を学ぶ、といった調子だった。"

    "しかし、オデットの方は明らかに違った。"

    "普段の豪快な態度とは打って変わり、彼女の瞳は郷愁に満ちていたのだ。"

    "ゴッホはオランダ生まれだが、その多くをフランスで過ごしてきた。"

    "描かれているモチーフにも、フランスを舞台としたものは多い。"

    "しかし海晴には、オデットの見せた瞳の理由が絵画の向こうに故郷を感じているから、というだけとも思えなかった。"

    "そしてオデットは、『収穫』という農村を描いた絵画の前で立ち止まった。"

    "30分以上も見入っていて、まるで心を奪われたかのようだった。"

    "その間の彼女に、海晴は声をかけることはしなかった。"

    "逃げ帰ることもできたが、それもしなかった。"

    "オデットが何を考えているのか、海晴には結局読めないまま。"

    "けれども確実に、オデットという女性に人間を感じていたのだ。"

    "ソーニャに見せた甘さと、その感覚はそっくりだった。"


    voice get_voice_filename("ode")
    odette "「意外だったろ。あたしがあんな風に絵を見るなんてよ」"


    voice get_voice_filename("mhr")
    miharu "「そうだね。君の知識が幅広いことは知っていたけれど、芸術はもっと斜に構えて見るのかと思っていた。でも、君はまるで子供のような目をしていたね」"

    show ecg odettomiharupark a with ecg_change


    voice get_voice_filename("ode")
    odette "「当たり前だ。優れた芸術の前じゃ、誰だって『今』を忘れちまう」"

    "オデットは空を見上げ、そう言った。"

    "風が吹き、空の青色を数羽のカラスが横切った。"

    "海晴はオデットが強調した単語から、ある推測をする。"

    show ecg odettomiharupark c with ecg_change


    voice get_voice_filename("mhr")
    miharu "「君は……自分の未練がぼくたちに知られそうになっていることに気付いているね？　まさか、その件でぼくを……」"

    show ecg odettomiharupark d with ecg_change


    voice get_voice_filename("ode")
    odette "「ああ、そうさ。あたしの≪未練≫が割れそうになっていることはもう分かってる。フェデリーコの奴も、そろそろ≪死因≫に思い当たってるだろう」"


    voice get_voice_filename("mhr")
    miharu "「そこで、一番話しやすそうなぼく、ということかい？　交渉……いや、それは君らしくない……」"

    "海晴はオデットに向けて目を細め、警戒心を高めた。"

    "それは、緊張の裏返しでもあった。"


    scene bg shinjukugyoen evening
    show ode noj arm smi rev at std_cl
    with dissolve_long

    voice get_voice_filename("ode")
    odette "「いや、てめーをどうこうするつもりはねーよ」"

    show ode noj nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「あたしにとっちゃ≪女神の選定≫なんてのは所詮ゲームだ。勝ったら生きる、負けたら死ぬ」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「もう詰みだってんなら、せめてそれまで楽しめればそれでいいさ」"

    show mhr sun sco thi at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「君が脱落させた人は、そんなつもりではなかったと思う。ソフィアも……いや、そんなことを言う資格はぼくにはないね」"

    "海晴は途中まで言いかけて、首を横に振った。"

    "原因を作ったのはオデットたちかもしれないが、ソフィアを指名して脱落させたのは他でもない海晴だった。"

    "そうしなくてはいけない理由があったとはいえ、いずれはそうしなくてはいけなかったこととはいえ、事実は変わらない。"


    play music audio.commit
    scene ecg odettomiharupark c with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「君は――生きたくないのかい？」"

    show ecg odettomiharupark d with ecg_change


    voice get_voice_filename("ode")
    odette "「かかっ、そんなわけねーだろ。楽しいことは多い方がいいに決まってる」"


    voice get_voice_filename("ode")
    odette "「だがよ、あたしの未練は決して叶うモンじゃねぇ。だったら、死んだって別に構わない。あたしにとっちゃもう、人生ですらゲームみたいなもんだ」"

    show ecg odettomiharupark c with ecg_change


    voice get_voice_filename("ode")
    odette "「どんなにレベルを上げても、現実じゃ何も変えられねぇからな」"


    voice get_voice_filename("mhr")
    miharu "「ならやはり、ぼくの抱えていた違和感は正しかったということだね。つまり……君の体は、もう……」"


    voice get_voice_filename("ode")
    odette "「勿体ぶるつもりもねぇ。冥土の土産なんてわけでもねぇが、話してやるよ」"


    voice get_voice_filename("ode")
    odette "「あたしの生まれは、ゴッホの収穫のような風景が続く、時代遅れの田舎だったのさ」"

    scene ecg odettopast with dissolve

    "そしてオデットは、自らの過去を語り始めた。"

    "海晴はその間ずっと、何も言わずに聞いていた。"

    "オデットに、感傷的な様子は一切なかった。"

    "誰かのおもしろおかしい小噺を話すような口調で、ある意味では淡々と、自分の過去と未練のことを話した。"

    "話を終えてもしばらく、海晴は言葉を発することはできなかった。"

    "同じ女性として、オデットの話は辛い過去という言葉で片付けられるものではなかったのだから。"


    scene bg shinjukugyoen evening
    show mhr sun nor ser at std_cr
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「……これじゃ、凛火のことを馬鹿とは言えないな」"

    "出てきたのは結局、自分への皮肉だった。"

    "オデットはそれを聞き、かかかと高笑いをする。"

    scene ecg odettomiharupark b with dissolve_long


    voice get_voice_filename("ode")
    odette "「同情してくれてんのかい？」"


    voice get_voice_filename("mhr")
    miharu "「――ただ、君にかける言葉を持たないだけさ」"

    "海晴は、本当に何の感傷もなさそうなオデットに恐怖すら感じていた。"

    "自分の過去に対して悲しむことも、怒ることもしていない。"

    "壊れているんだ、と思った。"

    "未練に執着しても決して叶わないという事実は、オデットという女性の心の一部を、長い時間をかけて壊して、壊し続けてしまったのだろう。"


    voice get_voice_filename("mhr")
    miharu "「何故、ぼくに君の話を？」"

    show ecg odettomiharupark a with ecg_change


    voice get_voice_filename("ode")
    odette "「てめーは、強さの意味を履き違えちゃいないからだ」"


    voice get_voice_filename("mhr")
    miharu "「……意味が、分からないよ」"

    "海晴も、ここまで来るとお手上げだった。"

    "楽しいか、楽しくないか。"

    "今を楽しむという言葉の裏に隠された意味を知ってしまったから。"

    "そんなもの、予想できようはずもない。"




    play music audio.impatience
    scene bg shinjukugyoen evening
    show ode noj arm ser rev at std_cl
    with dissolve_long

    voice get_voice_filename("ode")
    odette "「スケールは、次の選定でてめーを指名する」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「奴はてめーとリンカが仲違いしてないことなんざ、恐らく気付いているだろう。その上で泳がせていたってわけだ」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「８度目の選定じゃあ、フェデリーコがあたしを指名、スケールがてめーを指名で二人の脱落。てめーからアランの≪死因≫のカードを取得すれば、スケールの目的は達成される」"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「ま。用済みってわけだな」"

    show mhr sun pai irr at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「なんだって……？」"

    "唐突に告げたオデットに、海晴は驚きを隠すことができなかった。"

    "それはスケールが海晴を用済みと思っていることに、ではない。"

    scene ecg odettomiharupark e with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「彼がぼくの≪未練≫のカードを持っているのは知っている。けれども、いつの間にぼくの≪死因≫まで……？」"


    voice get_voice_filename("ode")
    odette "「抜け目ないことが仇になったってことだ。てめーが手首を隠し続けていること、それ自体が答えだろ？」"


    voice get_voice_filename("mhr")
    miharu "「……そんな……」"

    "海晴は反射的に自分の手首を押さえていた。"

    "海晴は普通の長袖よりも、少し長くなるように気を遣っているし、半袖の時には手袋を着用していた。"

    "腕を曲げて袖が引っ張られても、手首が見えないように。"

    "もしちらりとでも見えそうな時は、もう片方の手や鞄、カードブックなどで手首を隠してきた。"


    voice get_voice_filename("ode")
    odette "「てめーは所詮、思春期のガキだ。手首に傷を作るなんて珍しくはないだろ。そこから連想したことと身辺調査で、死因を見つけるなんてのは難しいことじゃねぇ」"


    voice get_voice_filename("ode")
    odette "「スケールのような奴には殊更、な」"


    voice get_voice_filename("ode")
    odette "「なんとか喫茶、だっけか。てめーがアルバイトしている場所の制服では手袋の着用が認められている。これは飲食店としちゃ稀だ」"


    voice get_voice_filename("ode")
    odette "「あいつはそれを確かめるためにも、てめーのアルバイト先まで顔を出したんじゃねーのか？」"


    play music audio.commit
    show ecg odettomiharupark c with ecg_change


    voice get_voice_filename("mhr")
    miharu "「……全部お見通しってわけか。怖いな……」"


    voice get_voice_filename("ode")
    odette "「あたしの些細な判断から≪未練≫まで辿り着いた奴が何を言ってやがる」"


    voice get_voice_filename("mhr")
    miharu "「しかし、やはり不可解だ。どうしてスケールに狙われていることを教えてくれたんだい？　君の脱落の原因となるぼくも脱落した方が君は楽しいのではないかな？」"

    show ecg odettomiharupark d with ecg_change


    voice get_voice_filename("ode")
    odette "「かかっ、何言ってる。あたしはな、てめーに自分の弱さを見抜かれて気持ちいいくらいに感じている」"


    voice get_voice_filename("ode")
    odette "「スケールは人の弱味に敏感だ。だからこそ情報収集もできてるわけだが、てめーは似ているようで違う」"


    voice get_voice_filename("ode")
    odette "「あたしは好きだぜ、てめーのこと。恋愛的な意味でな」"


    voice get_voice_filename("ode")
    odette "「てめーは、人の弱さに敏感だった。そこに惚れちまったってわけよ。もっとも、４度目の選定で出し抜かれた時から気になってはいたんだ」"


    voice get_voice_filename("ode")
    odette "「そんな相手に生き残ってもらいたいってのは、てめーもよく分かる感情だろ？」"

    show ecg odettomiharupark f with ecg_change


    voice get_voice_filename("mhr")
    miharu "「な、な、いきなり何を言い出すんだい？　冗談はやめてくれないか？」"

    "突然の告白に、海晴は冷静さを失い、怒り混じりに動揺した。"

    "海晴がわずかに頬を膨らませるような表情を浮かべ目を逸らすのを見て、オデットは続ける。"


    scene bg shinjukugyoen evening
    show ode noj arm ser rev at std_cl
    with dissolve_long

    voice get_voice_filename("ode")
    odette "「冗談じゃねぇさ。てめーもあたしも弱いんだ。弱い奴らは惹かれ合うんだよ」"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「それにあたしはどっちもいけるクチだぜ？　顔も体も、好みな部類だ。その点じゃフェデリーコとは気が合うかもしれねーな」"

    show mhr sun sco sh1 at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「駄目だよ。仮に君が本気で言っていたとしても、受け入れられないさ。ぼくが愛するのは、凛火だけだからね」"

    show ode noj nor sur rev with std_change

    voice get_voice_filename("ode")
    odette "「その片想いってのも、弱い証拠だよなぁ。言っておくがよ、たぶんあの女にそのケはないぜ？」"

    show mhr sun sco sh2 with std_change

    voice get_voice_filename("mhr")
    miharu "「やめてくれ、そういうんじゃないんだ。ぼくは……」"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「かかっ、分かってるよ」"

    "オデットは皮肉混じりに言うと、真剣な表情を浮かべた。"

    "海晴は彼女が突然見せた冷徹な目に、ひやりとしたが、毅然とした態度で向き合っている。"

    show ode noj nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「好きになった奴がいるなら、そいつを悲しませるな。言っている意味、分かるな？」"

    show mhr sun sco sh1 with std_change

    voice get_voice_filename("mhr")
    miharu "「……痛いほど」"

    "海晴は頷いて、そう答えた。"

    "海晴自身も導き出した、答え。"

    "凛火に命を捧げることが、凛火の幸せに直接繋がりはしないということ。"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「しかし、このままフェデリーコに指名されるのも面白くねぇ。フられちまった借りを返してもらうためにも、ひとつ協力してもらうぜ」"

    "オデットはそう言うと、海晴にその内容を話した。"

    "海晴は彼女の突拍子もない意見に驚きながらも、頷いた。"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「それでこそ、だ。てめーにだからこそ、頼めるってモンだ」"

    show mhr sun nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「……ああ」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「さて、と。てめーは最後まで、地獄に来るんじゃねーぞ」"

    show mhr sun sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「……当然さ。地獄でも天国でもない。凛火の隣に行くだけさ」"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「かかっ、妬けるねぇ。じゃ、あばよ」"

    hide ode with std_out

    "オデットはそう言い残すと、海晴の元から去って行った。"

    "海晴は気持ちを落ち着けるため、一度ベンチへと座り込んだ。"

    hide mhr with std_out

    "その後日が暮れるまで、ずっとその場所で考え込んでいたのだった。"

    "オデットの語った、弱さについて。"

    $ add_seen_chapter("8-2")








    python:
        set_info_scene("120")
        set_info_date(6, 20, "wed")
        set_info_time("evening")
        set_info_location("15")

    stop music fadeout 2
    scene bg schoolrooftop noon with fade_longest
    pause 1

    $ show_hud()

    "翌日の放課後、海晴は屋上に直未を呼び出していた。"

    "今にも雨が降りそうな曇り空の下、二人は向き合っている。"

    "直未は海晴から呼び出されることなどほとんどないし、二人で話すというのもあまりいい思い出はなかった。"

    show nom sun hes sor rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「あの……、未島先輩。今日は、どうしたんですか？」"

    "遠慮、というよりも怯えの混ざった声で、直未は何も言わない海晴へと問いかけた。"

    show mhr sun nor ser at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「まだ遊園地に行く前。君とライオン館の前で話した時のことは覚えているよ。だからぼくは、日辻さん、君がぼくを避けていることは仕方がないと思っている」"

    show nom sun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「避けている、だなんて……ううん、ご、ごめんなさい。わ、わたし……未島先輩のこと……、確かに、避けていました」"








    stop music fadeout 1
    scene bg lion02 noon with wfade_long
    play music audio.shadowmiharu
    pause 1

    "それは５月３日、≪因果の刻≫の翌日であった。"

    "12人が死ぬと同時に、その死がなかったことになった運命の日。"

    "海晴は、凛火の顔を見るためにライオン館を訪れていた。"

    "凛火と会うことで自らの生を実感し、遊園地へ行く約束の念押しをした。"

    "海晴は凛火と行く遊園地を境に、本格的に≪女神の選定≫へ身を投じる覚悟をしていたのだ。"

    "ライオン館を出た直後の道で、日辻直未とすれ違った。"

    show nom gci nor lau rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「あ、未島先輩っ」"

    "直未は何も気にせず、海晴を見かけたので声をかけた。"

    "対照的に、海晴は振り返ったあとしばらく無言で直未のことを睨みつける。"

    show nom gci hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、あの……」"

    show mhr uni nor ser at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「君は、凛火のことが好きなのかい？」"

    show nom gci nor sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「へっ！　え、えと……凛火先輩のことは尊敬してますし、先輩としてすごく好き、ですけど……」"

    show mhr uni pai irr with std_change

    voice get_voice_filename("mhr")
    miharu "「その程度なら、ぼくから凛火を奪うのはやめて欲しい」"

    show nom gci hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「えっ……、う、奪う……？」"

    show mhr uni pai ten with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは凛火が好きだ。友人としてではなく、一個人として」"

    "海晴はそれだけ言うと、直未の前から立ち去った。"

    "この後直未はライオン館へ入っていく。その胸にはもどかしさを感じたまま。"




    stop music fadeout 1
    scene bg schoolrooftop noon with wfade_long
    play music audio.growapart
    pause 1

    show nom sun hes tr1 rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「で、でも今なら、未島先輩の気持ちも分かりますから……。怒ったりはしていません。あの時は、≪女神の選定≫の参加者になってしまった直後だったんですもんね」"

    show mhr sun nor ser at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「君に理解されるほど、ぼくの想いは浅くない」"

    "歩み寄った直未も、海晴はまた拒絶した。"

    "しかし海晴は口元に手を当てて、「違う、そうじゃないんだ」と呟いた。"

    show mhr sun sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは君が嫌いだ。君の人格はこの際どうでもいいけれど、君は確実に、凛火がぼくと過ごす時間を奪っていったから」"

    show nom sun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「……は、はい……」"

    "直未は真正面から言われた言葉に、ただ下を向くことしかできなかった。"

    "海晴が先輩であるというだけではない、面と向かって嫌いと言われることなど、直未にとってはこれが初めてだったから。"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「高校生活が始まってからの１年間は、凛火とぼくと真央との３人で過ごすものだった。真央はぼくが凛火を好きなことを分かっていたから、一歩引いてくれることが多かったんだ」"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「けれど、君は突然にぼくの前に現れた。後輩という立場を利用して、{rb}庇護欲{/rb}{rt}ひごよく{/rt}をかき立てて、凛火の興味を引いた」"

    show nom sun har ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「そんなこと……わたし、思っていないです……」"

    show mhr sun sco vig with std_change

    voice get_voice_filename("mhr")
    miharu "「君はぼくの恋心を知っていた。けれどもぼくに気を遣うことはなく、あまつさえ、≪女神の選定≫を利用してさらに距離を縮めた」"

    show nom sun har con rev with std_change

    voice get_voice_filename("nom")
    naomi "「ち、違います……わたしだって未島先輩の気持ちを分かっていたから……でも、凛火先輩はいつも、みんなでって言ってくれて……」"

    show mhr sun pai irr with std_change

    voice get_voice_filename("mhr")
    miharu "「君はぼくを差し置いて、凛火にとって大切なものになっていたんだ」"

    "何故ここまで言われなくてはいけないのかと、直未は困っていた。"

    "しかし、怒ったり言い返したりできる性格ではなかった。"

    "直未はひたすら海晴の誤解を解こうとすることしかできない。"

    show nom sun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「未島先輩は……それを言うためにわたしを屋上へ呼んだんですか？　わたしに、どうして欲しいんですか？」"

    "雲はさらに分厚くなっていて、屋上に影を落とす。"

    "二人の人影は、重苦しい湿気に押し潰されそうだ。"

    show mhr sun pai ten with std_change

    voice get_voice_filename("mhr")
    miharu "「構わないさ。そのままでいればいい」"

    show nom sun hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「……で、でも！　わたしがいることで未島先輩に嫌な想いをさせてしまっているなら……、わたし、できる限り、改善しますから……」"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは君以上に、自分のことが嫌いだ。この嫉妬深い性格も嫌味な性格もね」"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「醜い心が自分の親と似ていると自覚する度、ぼくという存在が親からもたらされたものであるとことを思い知らされて、無性に死にたくなるんだ」"

    "海晴は冷たい声でそう言うと、左手の手袋を外し、手首を直未へ見せつけた。"

    "新しい傷はそこには刻まれていなかったが、すでに痕になった傷はいくつもあった。"

    show mhr sun sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくの死因は、こういうことさ。本来なら自ら選んだ道。生きようとする資格はぼくにはないはずなんだ」"

    show nom sun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「せんぱい……それは……」"

    "海晴はすぐに、手袋をつけ直した。"

    "そして直未に向けたのは、悲しい微笑み。"

    show mhr sun pai lie with std_change

    voice get_voice_filename("mhr")
    miharu "「こんなぼくでも、死んだら凛火を悲しませてしまう。それはぼくにとって、許されることではないんだ」"

    show nom sun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「わたしはやっぱり、未島先輩のことが苦手です……でも！」"

    show nom sun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「もし死んでしまったら、悲しいです。想像するのも、恐ろしいくらい。真央先輩だって、悲しむに決まっているじゃないですか」"

    show nom sun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「誰に――狙われているんですか？」"

    "直未の問いかけに、海晴は驚いた顔を浮かべた。"

    "しかし、すぐに納得をした。"

    "直未は凛火のために、きっと四六時中≪女神の選定≫のことを考えていたのだろうと、想像がついたからだ。"

    "ゆえに、この会話で海晴が直未に何を伝えたかったのか、すぐに分かったのだ、と。"

    show nom sun har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「凛火先輩に直接言ったら、きっと何をしてでも未島先輩のことを守ろうとするから、わたしに伝えたんですね」"

    show mhr sun nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「スケール・ジョーンズ。Ⅸの男性さ。ぼくは彼の≪氏名≫と≪死因≫を持っている」"

    "海晴は直未に、オデットから伝えられたことを補足した。"

    "直未はさっきまで嫌い、とはっきり言われたことなど気にしていないような真剣な瞳で、食い入るように聞いていた。"

    "そして自分は自分で探すから、直未にもできる限り協力して欲しいことを。"

    show nom sun har sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「≪未練≫……なら、なんとかなるかもしれません。≪Ⅸ・未練≫のカードは、凛火先輩がすでに、持っていました」"

    show mhr sun sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「本当かい？」"

    show nom sun hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい。カードに書かれていたのは、≪金メダル≫。でも、カードの情報を知っただけでは、未島先輩のところにカードは作られない……んですよね？」"

    show mhr sun pai lie with std_change

    voice get_voice_filename("mhr")
    miharu "「そうだね。けれどそれだけ分かれば……きっと大丈夫さ。ぼくはスケール本人とも会っている」"

    "分厚い雲は風に流されて、晴れ間を作っていた。"

    "強い西日が、雲の隙間から海晴を照らす。"

    show mhr sun sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「……ありがとう、日辻さん。君は本当に――強いね」"

    hide mhr with std_out

    "海晴はそう言って、校舎へと戻って行った。"

    "直未は狐につままれたような顔を浮かべ、しばらく屋上で立ち尽くしていた。"










    python:
        set_info_scene("121")
        set_info_time("night")
        set_info_location("34")


    stop music fadeout 2
    scene bg bar with fade_longest
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "スケールの奴の呼び出しは、今日はまだなかった。"

    "だがオレはどうにも落ち着かず、≪MILK CROWN≫で一人酒を飲んでいた。"

    "今日飲んでいるのは、日本のなんとかってウイスキーだ。"

    "漢字一文字の名前で、カードブックを持っているオレは読めないことはないが、馴染みのない名前なので忘れちまった。"

    "そういえば、最近はワインを飲んでいなかった。"

    "ここ最近じゃワインを飲むのはオデットと一緒の時ばかりだったから、あいつのことを思い出しちまうからかもしれない。"

    "これがいいあれはよくないと話しながら飲むのは、まあ悪くなかった。"

    "だが、あいつを裏切ったのはオレの方だ。"

    show fed sta nor irr rev at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「今更になって罪悪感？　ちっ、馬鹿らしい」"

    "後ろめたさなんて、感じている場合じゃない。"

    "オレはオレが生きるために、正しい方法を選んだのだ。"

    "現にオレは奴の≪死因≫を見つけ、間もなく≪未練≫も手に入る算段。"

    "これを順調と言わず何と呼べばいい。"

    "オレをコケにしたアランの奴も、順番に処理すればいい。"

    "スケールと組んだ今、オレはこの≪女神の選定≫において圧倒的に有利なポジションにいる。"



    voice get_voice_filename("ode")
    odette "「ならよ、スケールはどうやって倒す？　ちゃんと先のことまで考えてんのかぁ、てめー」"

    show fed sta nor ir1 with std_change

    voice get_voice_filename("fed")
    federico "「なっ！」"

    "しかし周りを見ても、オデットの姿はどこにもなかった。"

    "オレはまた、舌打ちをしていた。"

    "いくら酔っているからといって、幻聴とは。"

    "確かにあいつの言いそうなことではあった。"

    "スケールと組んだときは、オデットがいた。"

    "あいつと組んでおけばスケールはどうにかなるとたかをくくっていたんだ。"

    "しかしどうだ、スケールからの誘いを受けた今、オレはあの男の情報を名前以外に何も知らない。"

    show fed sta nor pa1 with std_change

    voice get_voice_filename("fed")
    federico "「だが、オレの≪死因≫も≪未練≫もあいつは知らねーだろ」"

    "オデットなら、あるいはオレの≪死因≫には見当がついているだろう。"

    "オレがあいつの≪死因≫に気付いているわけだから、そう考えるべきだ。"

    "しかし、オデットを指名するのはオレであるから、スケールに≪オレ自身のカード≫を取得されることはないだろう。"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「それどころか、オデットならスケールの情報もつかんでるかもしれねぇな。もしそうなら、ラッキーだ」"

    "そう思い当たり、オレはウイスキーをロックで追加注文した。"

    show ode noj arm smi rev at std_cl with std_in


    voice get_voice_filename("ode")
    odette_unk2 "「そいつは取り消しだ。代わりにあたしが注文するさ」"

    show fed sta nor pa2 with std_change

    voice get_voice_filename("fed")
    federico "「何だァ、あん……オデット！？」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「独りで飲む酒は美味いかい？」"

    "オデットはオレの隣にどっかりと座ると、ワインリストの中からフランスの赤を選び、ボトルで注文した。"

    "グラスに、真っ赤な液体が注がれる。"

    "透き通った宝石のような色合いに、つい魅了されてしまう。"

    "正直なことを言うと、料理もワインもイタリアが最高だが、２番目はフランスだと思っている。"

    "こいつを裏切ったその後も、変わらない考えだった。"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「ま、まずは世間話でもしよーや」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「あんたと話すことなんてねーんだけどよ」"

    "しかしオレたちは、ワインを飲みながら他愛のない話をしてしまっていた。"

    "１ヵ月以上、行動を共にしていたのだ。"

    "こいつとの会話の仕方を覚えてしまっていた。"

    "習慣はそう簡単に抜けるものでもない。"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「お前さ、あたしのこと好きだったろ？」"

    "１本目のボトルが空く頃、オデットが突然こんなことを言い出した。"

    "まるで学生みたいなことを言う、と思った。"

    "そんな言葉で動揺するほど、オレは子供ではない。"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「馬鹿言え。てめーといたら、自由なんざなくなっちまう」"

    show ode noj nor sur rev with std_change

    voice get_voice_filename("ode")
    odette "「そうかぁ？　てめー、まるで尻に敷かれ慣れているみたいだったがよ」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「――まるで、昔似たような相手といた経験があるような」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「それこそ馬鹿なことだ。あいつとあんたは似てもにつかな……」"

    "オレはそこまで言って、オデットを睨みつけた。"

    "ちらつく店内の照明が、鬱陶しく感じ始めていた。"

    show fed sta nor bad with std_change

    voice get_voice_filename("fed")
    federico "「カマかけやがったな……？」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「じゃあな。お代はこいつにつけておいてくれ」"

    hide ode with std_out

    "オデットはそのまま、バーを立ち去った。"

    "オレはワイングラスのフットを握りしめたまま、震えていた。"

    show fed sta nor ang with std_change

    voice get_voice_filename("fed")
    federico "「あいつ……、あいつ……」"

    "心地よかった酔いは、一気に醒めちまった。"

    "オデットの突然の来訪の意味を、ようやく理解したからだ。"

    show fed sta nor pa1 with std_change

    voice get_voice_filename("fed")
    federico "「オレの過去を調べやがった。つまり≪未練≫にも気づいてる……そのことを伝えに来たんだ……！」"

    "苛立ちに任せて紙幣をテーブルに叩きつけ、扉を乱暴に開け、オレはバーを出て行った。"







    $ set_info_location("35")


    stop music fadeout 1
    scene bg hotel japan with fade_long
    play music audio.impatience
    pause 1

    $ show_hud()

    show fed sta dar imp at std_c with std_in

    voice get_voice_filename("fed")
    federico "「畜生っ！　クソッ！」"

    "ホテルに帰ったオレは我慢することができず、そう叫んでいた。"

    "ソファーを蹴り飛ばし、ベッドに枕を投げつける。"

    "感情そのままをぶつけていた。"

    show fed sta dar imp with std_change

    voice get_voice_filename("fed")
    federico "「やべぇっ……、これはやべぇっ……」"

    show fed sta dar imp with std_change

    voice get_voice_filename("fed")
    federico "「スケールの奴、ちゃんと情報の裏付けを見つけてるんだろうな……じゃなきゃマジ、やべぇ……」"

    show fed sta dar imp with std_change

    voice get_voice_filename("fed")
    federico "「情報を３つ揃えてれば、最低限、指名の防御はでき――」"

    "焦った思考のまま一人呟き、口ごもった。"

    show fed sta dar bad with std_change

    voice get_voice_filename("fed")
    federico "「それじゃ駄目だろ、オレの野郎……」"

    "結局、オレはあいつを越えられないまま終わるのか？"

    "３枚のカードを揃えてお互いに指名し合った場合、恐らくお互いに防御の状態をとれば、指名は無効になる。"

    "防御をとった代償に、オレの持つオデットのカード、オデットの持つオレのカードは消え、今後の指名ができなくなる。"

    show fed sta nor cla with std_change

    voice get_voice_filename("fed")
    federico "「それじゃ一生、あいつに怯え続けるだろうが！」"

    "オレのすべきことが今、分かった。"

    show fed sta nor ama with std_change

    voice get_voice_filename("fed")
    federico "「あいつは必ず、オレが脱落させなきゃならねぇ……！」"

    "それこそが、オレにとって必要なことだ。"

    "オデットを越えれば必ず、スケールも踏み潰すことができる。"

    "オレは部屋を片付けながら、そう決意を固くしたのだった。"

    $ add_seen_chapter("8-3")










    python:
        set_info_scene("122")
        set_info_date(6, 21, "thu")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "昨日は店を閉めた後、図書室で借りた本を読んでいた。"

    "昔の本の装丁について書かれた本だったが、これといってめぼしい情報はなかった。"

    "このカードブックの装丁の雰囲気と、特に近いものはなかったのだ。"

    show rnk paj nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「でも……まだこれからだよね」"

    "そんなにすぐ、情報が集まるとは思っていない。"

    "私は気持ちを切り替えて、顔を洗いに行くことにした。"

    $ add_seen_chapter("8-4")










    python:
        set_info_scene("123")
        set_info_date(6, 22, "fri")
        set_info_time("night")
        set_info_location("34")

    stop music fadeout 2
    scene bg bar with fade_longest
    pause 1

    $ show_hud()

    "オデットと話した日から一日空けて、オレはスケールに呼び出されていた。"

    "ミハルの奴も来ていたが、相変わらずつれない顔をしている。"

    show sca sta nor ser rev at std_l with std_in

    voice get_voice_filename("sca")
    scale "「……以上がおれの調査結果であり、オデットの≪未練≫を裏付けるための情報だ」"

    "スケールは自分の調べた情報を全て話すと、重いトーンでそうしめた。"


    play music audio.disclose
    scene ecg odettopast with dissolve_long

    "オデット・マランソンの過去。"

    "農家の娘として生まれたオデットは、早くに母親を亡くしていた。"

    "妻の死により父親がおかしくなってしまったのかは、今となっては誰にも分からない。"

    "ただ今残っている事実は、オデットは父親から虐待を受けていたということ。"

    "第二次性徴が始まってすぐの虐待が原因で、オデットは癒えない傷を負った。"

    "彼女の肉体は、子供を作ることができなくなってしまったのだ。"

    "その時にオデットの心は壊れてしまったのだろう。"

    "農機具を使って父親を半殺しにして、故郷を出て行った。"

    "農村を忘れるためにも、オデットは港に住むことに決めた。"

    "そこで海洋運送会社を経営する男性と出会い、彼女は多くを船上で生活することになった。"

    "オデットは彼に気に入られ、オデットもまた彼を育ての親のように慕っていた。"

    "危なっかしいほど豪快な性格と要領の良さで、次第に彼女は少女ではなく一人前の船員として信頼を勝ち取っていった。"

    "その船にはオデットの無鉄砲さはただ、生きることへの執着のなさから来ていることを知る者はいない。"

    "大人になるにつれて強くなっていくその≪未練≫を振り払うかのように、オデットはますます働き、目の前の人生を全力で楽しむようになった。"

    "――と、ここまでがあの女の≪未練≫を知るための前提情報ってわけだ。"


    scene bg bar
    show sca sta nor nor rev at std_l
    with dissolve_long

    voice get_voice_filename("sca")
    scale "「この父親というのがまだ生きていてね。話を聞くことができたそうだ」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「もっとも娘の反抗がよっぽどトラウマになっているのか、彼は今精神病院で暮らしているようだけれどね」"

    "同じ女ということもあり、堪えるものがあるんだろう。ミハルは下を向いて話を聞いていた。"

    show fed sta nor nor at std_c with std_in

    voice get_voice_filename("fed")
    federico "「≪出産≫……か。よし、カードが出た。間違いない」"

    python:
        add_character_cards("fed", ["11_regret"])
        add_character_cards("sca", ["11_regret"])
        add_character_cards("ode", ["11_regret"])

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「あれだけ大口を叩いていた彼女にしては、くだらない未練だな……」"

    "スケールがぼそりと何か言ったが、よく聞こえなかった。"

    "そんなことより、オレはついに揃えたんだ。"

    "生成されたカードを見て、ふつふつと喜びを感じる。"

    "ついに、ついに！"

    show fed sta nor ela with std_change

    voice get_voice_filename("fed")
    federico "「これで揃ったぜ……、あいつのカードが全て！」"

    "オレは３枚のカードを手に持って、口元がにやつくのを抑えていた。"

    "あいつにどんな過去があろうが、別にどうでもいい。"

    "それでオデットの評価や見方が変わることはない。"

    "今のあいつを乗り越えなければ、きっとオレに未来はない。"

    show fed sta nor bad with std_change

    voice get_voice_filename("fed")
    federico "「だが、これで……」"

    "オレはオデットと対等な立場に立つことができた。"

    "あとは選定の日に、奴を指名するだけ。"

    "あいつが防御をしても指名がかち合っても、ここで引くわけにはいかねぇ。"

    show mhr sun sco thi at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「しかしスケールさん。君の友人というのはすごいね。たった数日でここまで情報を集めるなんて」"

    show sca sta nor lau rev with std_change

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡ、それはどうも。おれの素性にも繋がってきてしまうから、詳細を教えられないのが残念だ」"

    "ミハルは黙って頷いた。"

    "疲労が蓄積しているのか、よく見ると表情には疲れが浮かんでいた。綺麗な顔が台無しだ。"

    "とはいえ、ミハルの言葉の通りだ。"

    "スケールにどんなツテがあるのか知らないが、確かにとんでもない情報収集能力というべきだろう。"

    "オレはあること、に思い至った。"

    "こいつの人脈が広いのであれば、反対にこいつを知っている人間も多いはず。"

    "スケールもミハルも、余裕ぶっていられるのは今のうちだ。"

    "オレがオデットを越えたら、すぐに――！"

    $ add_seen_chapter("8-5")










    python:
        set_info_scene("124")
        set_info_date(6, 23, "sat")
        set_info_time("noon")
        set_info_location("08")


    stop music fadeout 2
    scene bg schoolroom noon with fade_longest
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "結局土曜日になっても、私は進展らしい進展を得ることができていなかった。"

    "≪女神の選定≫が何か、そのものの正体を暴くために調べ物をしていたけれど、世の中にあるデザインの情報は膨大過ぎる。"

    "元々歴史にも詳しくないし、はっきり言ってお手上げ状態に近い。"

    "カードブックを写真に撮って画像検索というのも試したが、ヒントは何も得ることができなかった。"

    "限られた時間の中で限界を感じ始めていたが、ここで立ち止まるわけにもいかない。"

    "別の方法が思いつかないなら、このまま調べた方がマシという状況だ。"

    show mao uni nor irr rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「りーたん、ちゃんと寝てるぅ？」"

    show rnk sun arm ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「１限と２限はちょっと寝てた」"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「……うちみたいな返事だねぇ」"

    "お店も開けているので、どうしても睡眠時間が不足しがちだ。"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「そうか、常連さんなら……」"

    "思いついて、私はつい口に出していた。"

    "ライオン館の常連さんには色々な職業の人がいる。"

    "年配の方も多いし、もしかしたら詳しい人がいるかもしれない。"

    "止まらずにいられることが、私の心を安定させていた。"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「駄目だこりゃ」"

    "真央の呆れた声を聞いて、私はさらに安心していた。"

    show nom sun har sur at std_r with std_in

    voice get_voice_filename("nom")
    naomi "「あ、あのー……未島先輩はいらっしゃいますか？」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「あ、なおりん～」"

    show rnk sun arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴は……今日は休みだよ」"

    "海晴は欠席が増えていた。"

    "奨学金をもらっているので出席日数があまり少ないと問題だが、私が指摘せずともその辺りはきちんと調整していることだろう。"

    show nom sun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「そう……ですか……」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「もう帰りだよねぇ。どうだい、久々にライオン館に行くかい？」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「……真央が聞くの？　ま、いいけどさ」"

    show nom sun hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「い、いえ。とっても嬉しいお誘いなんですけど、今日はちょっと用事があるので……」"

    show mao uni nor lau rev with std_change

    voice get_voice_filename("mao")
    mao "「あいよー。じゃ、今日はうち一人で行くねん」"

    hide nom with std_out

    "直未は申し訳なさそうにぺこりとお辞儀してから、そそくさと私たちの教室を去って行った。"

    "真央は今日ライオン館へ来るというので、珍しく真央と一緒に下校することとなった。"

    "２年生の教室に来るといつも緊張している様子の直未だが、今日は少し様子が違う気がしていた。"









    python:
        set_info_scene("125")
        set_info_time("evening")
        set_info_location("09")


    stop music fadeout 2
    scene bg maidcafe with fade_longest
    play music audio.maidcafe
    pause 1

    $ show_hud()

    "直未は海晴が欠席だと聞き、嫌な予感を覚えていた。"

    "だからこそ、一人でこの場所を訪れていたのだった。"



    voice get_voice_filename("nom")
    naomi "「未島先輩ならきっと……バイトには行っているはず……」"

    "凛火から、海晴がバイト熱心なことは聞いていた。"

    "だからこの状況でも、習慣的にシフトには入っているだろうという予感はあった。"

    show mhr mai sco wic rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「おかえりなさいま――帰ってくれないか？」"

    "偶然、直未は店に入ってすぐに海晴と目が合った。"

    show nom sun hes sor at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「せんぱい……わたし、お話があるんです」"

    show mhr mai sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……あと30分で終わるから、席で待っていてくれないかい？　ここではあまり落ち着かないかもしれないけれどね」"

    show nom sun nor smi with std_change

    voice get_voice_filename("nom")
    naomi "「はい、ありがとうございます」"

    hide nom
    hide mhr
    with std_out

    "直未はメイド喫茶のテーブル席に、一人で座った。"

    "男性客は、直未に奇異の目を向けていた。"

    "その中にメイドとお話できるなんて、という羨望が含まれていることに直未は気付いてはいなかった。"




    scene bg maidcafe with fade_long
    pause 1

    "約30分後、メイド服から制服に着替えて海晴は直未の正面に座った。"

    "本を読んでいたので、直未にとってはあっという間の時間。"

    "ライオン館のように地元密着の喫茶店ではないのでアルバイト先で客として居座ることには抵抗があったが、他に場所もないということで海晴は直未とここで話すことに決めた。"

    "直未はちらちらと横目で客を見て、スケールやフェデリーコの姿がないのを確認した。"

    show nom sun nor smi at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「スケールさんの≪未練≫を、まだカード化できていないんですよね？」"

    "直未は前置きなどなしに、いきなり直球で訊ねる。"

    "直未は海晴の顔に疲労が現れていることに気が付いていた。"

    "濃いクマに、どこかぼんやりとした視線。寝る間を惜しんで調べ物をしているのがよく分かる。"

    show mhr sun nor ser rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「そうだね。≪金メダル≫という情報からしてスポーツ関連を重点的に調べているけれど、糸口がない」"

    show mhr sun pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「このままでは、今回の選定でぼくは脱落してしまう。そうなれば、ぼくの持っている凛火のカードがスケールに知られるリスクが高まる」"

    show nom sun que que with std_change

    voice get_voice_filename("nom")
    naomi "「せんぱいに……凛火先輩に相談してみませんか？　凛火先輩はオデットさんやアランさんと協力していたんですし、力になってくれるかもしれません」"


    play music audio.growapart

    "直未は今日まで、凛火に海晴のことを言わないでいた。"

    "それは、海晴が凛火に心配をかけたくないと想っていることが、痛いほど理解できたからだ。"

    "だが、それももう限界。"

    "気を遣っているだけでは大切なものを失ってしまうと、直未はよく分かっていた。"

    "失われたのが、自分自身の命だったのだから、余計に。"

    show nom sun har pin with std_change

    voice get_voice_filename("nom")
    naomi "「凛火先輩なら、何とかしてくれると思います。だって、わたしのことも助けてくれたから……」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それは駄目だ。凛火に心配をかけるわけにもいかないし、凛火の情報が他の参加者に知られるデメリットが生まれるかもしれない」"

    "海晴の淀みない回答に、直未は胸を痛くしていた。"

    "下を向いて、何度か首を振る。"

    "溜めこんだものを一気に吐き出さないように、少しずつ伝えるために、直未は少し経ってから海晴を見つめた。"

    show nom sun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「そうじゃ……ないです」"

    show nom sun har pin with std_change

    voice get_voice_filename("nom")
    naomi "「リスクとかデメリットとか、そういうのはもう、いいです。凛火先輩は未島先輩を助けるためなら、そんなの構わないって言います」"

    show nom sun har ser with std_change

    voice get_voice_filename("nom")
    naomi "「わたしだって、せんぱいが危険な目に合うのは嫌です。でもそんなのお構いなしに、失いたくないもののため、どうにかしてくれるのが凛火先輩です」"

    show nom sun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「本当はわたしも、凛火先輩が頑張る姿を見ているのは辛いです。もっと力になれたらって、ずっと思っています」"

    show nom sun hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「でも、未島先輩がいなくなって悲しんでいる凛火先輩を見る方がきっと、もっと……辛いです。わたしじゃ、耐えられないほど」"

    "海晴は直未の言葉にはっとしていた。"

    "直未がいなくなり、絶望していた凛火。"

    "海晴はそんな凛火のことを見ていられなかったからこそ、自分でユウを脱落させるためにスケールと交渉をしたのだ。"

    "ユウを脱落させたときの凛火は危険な目にあっていた。"

    "これ以上凛火を危険にはさらせないという想いを、海晴はその時より強固なものにした。"

    "しかし、一方では。"

    "生きている直未を見て安心しきっている凛火の姿に、心底ほっとしていた。"

    "凛火の幸せを、海晴は素直に実感していたのだ。"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それでもぼくは、凛火の命と自分の命を天秤にかけたとき――」"

    "海晴はその言葉を、下を見ながら言っていた。"

    "自信なさげな口調は、直未がほとんど見たことのないようなもの。"

    "直未はそんな海晴に、優しく告げる。"

    show nom sun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「何より、このままじゃわたしが嫌です。海晴先輩がいなくなっちゃったら、こうして過ごした時間もなかったことになったら……」"

    show nom sun har ser with std_change

    voice get_voice_filename("nom")
    naomi "「そんなの、そんなの……ぜ、絶対に……」"

    "一呼吸おいて、続けた。"

    show nom sun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「泣いて泣いて枯れて果てて、わたしが死んじゃいます」"

    show mhr sun pai ten rev with std_change

    voice get_voice_filename("mhr")
    miharu "「――洒落にもならないな」"

    "海晴は、直未が自分のことを名前で呼んでいたことに気がついていた。"

    "そして同時に、そのことに直未自身が無意識だっただろうということも。"

    "悟ったような笑顔を見せて、海晴は深く頷いた。"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「もしかすれば君が一番、変わったのかもしれないね。この後、ライオン館へ行こう」"

    show mhr sun sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、君の涙に興味はないけれど、凛火を悲しませるわけにはいかないからね」"

    show nom sun nor smi with std_change

    voice get_voice_filename("nom")
    naomi "「――ありがとう、ございます」"

    "直未はほっとした顔で、海晴にお礼を言った。"

    "注文していたカフェオレを一気に飲み干して、目じりに浮かんだ涙の粒を拭う。"







    python:

        set_info_time("night")
        set_info_location("18")

    stop music fadeout 1
    scene bg lion02 nightclose with fade_long
    pause 1

    $ show_hud()

    show mhr sun nor ser rev at std_l
    show nom sun que que rev at std_c
    with std_in

    "海晴と直未の二人は、ライオン館の前まで足を運んでいた。"


    voice get_voice_filename("nom")
    naomi "「いない……」"

    "しかし、ライオン館に明かりはついていなかった。"

    show nom sun hes sor with std_change

    voice get_voice_filename("nom")
    naomi "「まだ閉店時間には早いのに……」"

    "直未は昼間に凛火と真央が話していたのを聞いていたからこそ、疑問を深めていた。"

    "何かあったのかもしれない――そんな不安が胸をよぎる。"








    python:
        set_info_scene("126")
        set_info_location("36")


    stop music fadeout 2
    scene bg warehouse with fade_longest
    play music audio.odette
    pause 1

    $ show_hud()

    "私は、先週ユウのテロを阻止する時に拠点で使った倉庫を訪れていた。"

    "殺風景な廃倉庫には、今日も乾いた風が吹き込んでくる。"

    "正確には、突然ライオン館を訪れたオデットさんに連れて来られたのだった。"

    "もっとも最終的に行くことを決めたのは私なので、完全に強制とは言えないのだけれど。"

    show ode noj nor lau at std_c with std_in

    voice get_voice_filename("ode")
    odette "「よう、アラン」"

    show aln sta nor nor rev at std_l with std_in

    voice get_voice_filename("aln")
    alan "「……何の用だ？」"

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「とか言って、もう分かってるんだろ？　スケールの野郎が動かしてるパパラッチ仲間は、てめーともコネクションがあるみたいだしよ」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「……フン」"

    "ここまで来る途中、オデットさんからは事情をほとんど聞いていなかった。"

    show ode noj arm smi with std_change

    voice get_voice_filename("ode")
    odette "「あたしはもうすぐ脱落だ。だからよ、アラン。てめーと決着をつけにきた」"

    "これが、私もオデットさんから聞いたことであった。"

    "彼女はアランさんにも、同じことを告げる。アランさんはいつも通りの無表情で、何も答えなかった。"

    show rnk sun sur su2 at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「決着……」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「ああ、そうさ。こいつとはジジイの家で一度戦ったきり。どっちが強いのか、まだ証明していなかったからな」"

    show ode noj nor irr rev with std_change

    voice get_voice_filename("ode")
    odette "「リンカ、てめーにはこの勝敗を見届けてもらう。先におねんねした方が負けだ。ま、勝つのはあたしだけどな」"

    show aln sta nor que rev with std_change

    voice get_voice_filename("aln")
    alan "「僕と戦う？　僕が貴様の挑戦を受けるとでも？　何もメリットがない。あの時は、必要だったからそうしただけだ」"

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「理由なんていらねぇよ。一度きりの人生――あたしたちにとっちゃその言葉は皮肉でしかないが、楽しまなきゃ損だぜ？」"

    show ode noj gra gla with std_change

    voice get_voice_filename("ode")
    odette "「それにもし背中を向けて逃げるってんなら、それはそれでてめーが再起不能になるだけだ」"

    show ode noj arm smi with std_change

    voice get_voice_filename("ode")
    odette "「最後なんだ。ちったあ付き合ってくれよ、お坊ちゃん」"

    "オデットさんの言葉に含まれる冷たさに、私はぞくり、と恐怖を感じていた。"

    "話せば通じると分かった今も、この人が見せる冷徹な瞳は恐い。"

    "あるいはこれが殺気というものなのかもしれない。"

    "しかし、私には気になる事があった。"

    show rnk sun arm imp with std_change

    voice get_voice_filename("rnk")
    rinka "「オデットさんが、脱落……？」"

    show ode noj nor inn rev with std_change

    voice get_voice_filename("ode")
    odette "「何を驚いてるんだ？」"

    show rnk sun arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、だって、そんな……、オデットさんが？」"

    "それは、驚きに他ならなかった。"

    "海晴からフェデリーコさんやスケールさんの話を聞いていたけれど、彼らがオデットさんを脱落させられるとは思えなかったのだ。"

    "確かにオデットさんには、常に危ない橋を渡っているような印象がある。しかしそれでも、彼女がその橋から落とされる姿は想像できない。"

    "あえて想像するなら、笑いながら飛び降りる姿くらいだろうか。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「この女に同情しているのか。君らしいな」"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「そういうわけじゃないけど……」"

    show ode noj arm smi with std_change

    voice get_voice_filename("ode")
    odette "「てめーもこいつには随分甘い口調だよなぁ」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「……フン」"

    "オデットさんの平然とした態度を見ても、今回の選定で脱落するとはとても思えなかった。"

    "しかしオデットさんがわざわざ最後と口にしたということは、偽りなく、彼女自身も覚悟しているということだろう。"

    "オデットさんが、死ぬ。"

    "彼女は敵だとは、分かっている。でもいざ脱落するのだと思うと、ユウのテロを阻止し、直未を助けた時の記憶が蘇ってくる。"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私……スケールさんの≪未練≫を知ってる」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「だから何だ？」"

    show rnk sun arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「私は助けてもらった。だから、せめて……！」"

    show ode noj nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「だから何だってんだ？」"

    "オデットさんは、私を睨んで重たい口調で答えた。"

    "私は、これ以上言葉を続けることができなくなってしまった。"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「あたしを侮辱するつもりだったら、てめーからやってやろうか？」"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「……そんなんじゃっ……！」"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「お人好しも大概にした方がいい。僕がいることを忘れているのか？」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「スケール・ジョーンズの≪未練≫は僕も欲しいカードだ。力ずくでも、教えてもらおう」"

    show ode noj nor gla with std_change

    voice get_voice_filename("ode")
    odette "「ちっ、そうかい。そこまでてめーは≪理由≫にこだわるってわけだ」"

    "何の話をしているのか、私は徐々に理解し始めていた。"

    "私の発言がきっかけとなってしまったのだ。"

    "アランさんは別にオデットさんと戦う理由などないけれど、今、生まれたということ。"

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「守ってやるよ、クソガキ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「目的があるならば、僕は躊躇わない」"

    "オデットさんを倒して、私からスケールさんの≪Ⅸ・未練≫を聞き出すこと。"

    "その目的を、生んでしまった。"


    scene bg warehouse with fade_long
    pause 1

    "私は倉庫の外から、二人が戦う様子を覗いていた。"

    "彼らは拳銃も所持しているだろうから、撃ち合いが始まる前に外に逃げて来たのだ。"

    "死なないといっても、怪我はする。少なくともこの倉庫くらいの壁の厚みがあれば貫通することはないだろう。"

    "それでも私は、完全に目を逸らすわけにはいかず、彼らの戦いを見ることに決めていた。"

    "決着をつけること。"

    "オデットさんにとってはそこに理由なんていらないのだろう。ただ自分を満足させるために、強者と認めたアランさんに勝ちたいだけ。"

    "理解なんて微塵もできやしない。"

    "でも、それでも、私は彼らの決着を見届けなければならないと思っていた。"

    "――なぜならきっと、この戦いはオデット・マランソンという女性の生き様そのものだから。"




    stop music fadeout 1
    scene bg warehouse with fade_long
    play music audio.battle
    pause 1

    "30分以上が経過したが、未だに彼らの戦いは終わる気配がなかった。"

    "お互いに、決定打になる攻撃を与えられてはいないようだ。"

    "だからこそ２人とも精神を削り続けているのだと思う。"

    "迫真の形相がそれを物語り、私はその展開から目を離すことができない。"

    "格闘技に興味はないけれど、もし競技でもこんな風に引き込むものがあるのであれば、魅力だけは理解できるかもしれない。"

    scene ecg alanbt gla with dissolve_long


    voice get_voice_filename("aln")
    alan "「……くっ」"

    scene ecg odettobt ser with dissolve


    voice get_voice_filename("ode")
    odette "「……ちいっ」"


    scene bg warehouse with dissolve_long

    "すでに拳銃は叩き落とされ、お互いの肉体によって破壊されていた。"

    "一度触ったことがあるからその質感を実感できるけれど、あんな固いものをどうやったら壊すことができるのか分からない。"

    "刃物も持っていたようだが、それもへし折られていた。"

    "アランさんもオデットさんも、銃弾を受けていなければ、切り傷も作っていない。"

    "汗だくになりながらも、まだ体力は底をつきそうになかった。"




    stop music fadeout 1
    scene bg warehouse with fade_long
    play music audio.kinpaku
    pause 1

    "さらに、約10分が経過した。"

    "疲労というのは一気にくるものなのだろう。状況は少しずつ変わってきていた。"

    "お互いに積極的に攻めるのをやめ、一定の距離をとりながら牽制し合っている。"

    scene ecg odettobt fun with dissolve_long

    "膠着状態を崩そうと最初に踏み込んだのは、オデットさんの方だった。"

    "わずかに回復した体力を注ぎ込んだのだろう。"

    play se "swing"

    "アランさんの間合いの外から、大きく飛び込むようにして蹴りを放つ。"

    "しかしアランさんは、皮一枚でそれを避ける。直後、アランさんの拳が、オデットさんの顔面をとらえた――かに見えた。"


    voice get_voice_filename("aln")
    alan "「ぐ……」"

    play se "punch02"
    with quake_fast

    "オデットさんは彼のパンチを、額で受けていた。"

    show ecg odettobt mad with ecg_change

    "明らかに痛そうな顔をするアランさんのお腹を、オデットさんが膝で思い切り蹴りあげた。"


    scene bg warehouse with dissolve_long

    "アランさんがひるんだ隙に、オデットさんはさらに猛攻を仕掛ける。"

    "パンチやキックなど、私が食らったらどれも一撃で気を失ってしまいそうな荒々しい攻撃を、アランさんは何発も受けていた。"

    scene ecg alanbt gla with dissolve_long

    "しかしアランさんもその間隙を縫い、オデットさんの首に手刀を当てる。"

    play se "punch01"


    voice get_voice_filename("ode")
    odette "「かはっ……」"

    "筋肉のつけようがない喉に、その攻撃はよく効いたようだ。"

    "オデットさんは一瞬、完全に動きを止めた。"

    "今度はアランさんが攻撃をする側だ。"

    "流れるような連続攻撃は、猛獣のようなオデットさんの攻撃とは違い、舞踊のように滑らかな動きだった。"

    "先ほどまでとは、アランさんの体の動きは変わっていた。"


    scene bg warehouse with dissolve_long

    "だがオデットさんも、ただ攻撃を受けているだけではなかった。"

    "追撃の手刀を避けるのではなく、防御するでもなく、噛みついて見せた。"

    "血が滲むほど、深く噛みついている。"

    scene ecg odettobt mad with dissolve_long


    voice get_voice_filename("ode")
    odette "「おもしれえ……」"



    scene bg warehouse with dissolve_long

    "彼らの戦いは、まだ終わらない。"









    python:
        set_info_scene("127")
        set_info_location("18")


    stop music fadeout 2
    scene bg lion02 nightclose with fade_longest
    play music audio.shadowmiharu
    pause 1

    $ show_hud()

    "人通りもすっかり減ってしまった午後10時過ぎ。"

    "直未と海晴の二人は、未だライオン館の前で凛火の帰りを待っていた。"

    "６月の夜はすでに蒸し暑さと冷えでは前者が勝っていた。"

    "肝心の凛火からチャットの返事はなく、電話をかけても電源が切れているというアナウンスが聞こえてきてしまった。"

    show mhr sun nor ser at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「いい加減、帰ってもいいんだよ、日辻さん。もっともぼくは凛火が心配だから――帰りを待つけれどね」"

    show nom sun har pal rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「だ、大丈夫です。うまく言い訳しますから。わたしだって凛火せんぱいのこと、心配ですもん」"

    "直未の返事を聞き、海晴は静かに頷いた。"

    show mhr sun sco sh1 with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火も大変だな。あれだけ自信満々に凛火を諭したぼくに、頼られてしまうのだからね」"

    show mhr sun nor nor with std_change

    voice get_voice_filename("nom")
    naomi "「大変なんて思わないですよ、せんぱいは。海晴先輩だって分かっていますよね？」"

    show mhr sun sco smi with std_change

    "直未は海晴に問い掛けたが、返事はなかった。"

    "ただ穏やかな微笑みを見て、直未は安心をしていた。"








    python:
        set_info_scene("128")
        set_info_location("36")

    stop music fadeout 2
    scene bg warehouse with fade_longest
    pause 1

    $ show_hud()

    "さらに30分程度経過したときに、状況はほとんど終わりかけていた。"

    "動きのキレは落ちていた。"

    "私ですら逃げ切れると思うほど、二人とも弱っていた。"

    "そして最後に、オデットさんの左頬にアランさんの右拳が、アランさんの左頬にオデットさんの右脚が、同時に激突した。"

    "アランさんは気を失っているのか起きているのか分からないような虚ろな目をしている。"

    "オデットさんは目をつぶり、にやりと笑う。"

    show ode noj nor gla at std_cr with std_in

    voice get_voice_filename("ode")
    odette "「このまま死ねりゃあ、幸せだったのによ」"

    play se "taoreru08"
    hide ode with std_out

    "オデットさんは細々とした声で言い残すと、そのまま倒れ込んだ。"

    show aln sta nor nor rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「……フン……」"

    hide aln with std_out

    "感情の分からない目で、アランさんはオデットさんが倒れるのを確認した。"

    play se "taoreru08"

    "そしてそのまま、アランさんも倒れ込んでしまった。"

    show rnk sun sur su2 at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「ち、ちょっと！」"

    "私は二人の元へ急いで駆け寄った。"

    "呼吸はしているが、意識はないようだ。"

    "限界を超えた疲労困憊で、意識がシャットダウンされてしまったようだ。"

    "決着がついたのかついていないのか、私にはよく分からない。"

    "ただ長く立っていたのは、アランさんだ。"

    show rnk sun arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「オデットさんが、負けた……」"

    "決着はスマートなんてものではなかった。"

    "お互いが体力を使い果たすまで殴り合って、共倒れ。"

    "私が拳銃を持っていたら、この状況で勝つのは私だ。"

    show rnk sun arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「そんなことより……、どうして、私が……」"

    "こうなったら私が、二人の怪我の手当をしないといけないということだろう。"

    show rnk sun nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「うわ、スマホの充電切れてる」"

    "私は自分の記憶を頼りに、コンビニを探すこととなった。"




    stop music fadeout 1
    scene bg warehouse with fade_long
    play music audio.nichijo03
    pause 1

    "私は近くのコンビニまで往復で１時間ほどかけて行き、救急セットとお水などを買ってきた。"

    "戻ってきたとき、そこにオデットさんの姿はなかった。"

    "目を覚ましてすぐにこの倉庫を立ち去ったということか。体力なんて残っていなかったはずなのに、信じられない。"

    "ただ一つ言えるのは、彼女が倒れるあの瞬間こそ、私が現実世界でオデットさんの姿を見る最後になるのだろう。"

    "本当に最後まで――自由な人だ。"

    "そんなオデットさんとは対照的に、硬い床の上で――。"

    show rnk sun arm ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「寝てる……のかな？」"

    "対照的にアランさんはまだ、床に倒れたままだった。"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「はぁ、帰っちゃえばいいのに……」"

    "私は自嘲しながら、買ってきたタオルでアランさんの顔の汗をふき、額に風邪の時によく使う冷却用ジェルシートを貼った。"

    "別のタオルを頭の下に敷き、枕代わりにした。"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「オデットさんに負けず劣らず、この人も無茶な人だな」"

    "未だ汗だくで顔を真っ赤にしている彼が、心配になってしまったから。"

    "彼の目的は分かっているけれど、どうしても見捨てることはできなかった。"

    "長身で筋肉質な彼もこうして横になっていると、どこか幼く見える。"

    "スマホの充電も切れているし、今が何時かも分からない。"

    "とりあえず空腹を紛らわせるために、私はアランさんから離れた倉庫の端で、買ってきたお弁当を食べることにした。"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「この状況、他の人が見たらなんていうんだろう」"

    "すっかり普通じゃなくなってしまった自分を省みながら、私はお弁当を食べ始めた。"







    $ set_info_scene("129")

    stop music fadeout 2
    scene black with dissolve_longest
    pause 2
    scene ecg amrita hid with wfade_long
    play music audio.memories
    pause 1

    "アランは、夢を見ていた。"

    "彼にとって≪運命の大広間≫とは無関係のただの≪夢≫を見るのは、とても久し振りなことであった。"

    "――お兄ちゃんは、いつも無茶ばっかりするんだから。"

    "過去の記憶が見せた夢。"

    "それはそう、大切な――。"








    python:
        set_info_scene("130")
        set_info_location("36")

    stop music fadeout 1
    scene white with dissolve_long
    pause 1
    scene bg warehouse with fade_long
    pause 1

    $ show_hud()

    show aln sca nor lee at std_cr with std_in

    voice get_voice_filename("aln")
    alan "「――アム……リタ……？」"

    "アランさんは私がお弁当を食べ終える頃に、目を覚ました。"

    "思ったよりずっと早い目覚めに、少しびっくりしてしまった。"

    "アランさんが何を言いかけたのかは分からないが、誰かに呼びかけるような口調だった。"

    "もっともこの状況でも、それを問うのが得策とは思えなかった。"


    play music audio.thebonds

    show aln sca nor nor with std_change

    voice get_voice_filename("aln")
    alan "「君か……」"

    "彼は私の姿を見ると、額のシートや頭の下のタオルに気付き、「そうか」と状況を理解したようだ。"

    show aln sca nor gen with std_change

    voice get_voice_filename("aln")
    alan "「僕を置いて帰ることもできただろうに」"

    show rnk sun arm lie rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「お弁当を食べたら、帰ろうと思ってたよ」"

    show aln sca nor tre with std_change

    voice get_voice_filename("aln")
    alan "「……フン。もっと前の時点での話だ」"

    "私はお弁当のゴミをビニール袋に入れて、アランさんにはペットボトルの水を持って行った。"

    show aln sca nor clo with std_change

    voice get_voice_filename("aln")
    alan "「僕は……負けたのか？」"

    show rnk sun arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「僅かだけど長く立ってたのは、アランさんだったよ」"

    show aln sca nor nor with std_change

    voice get_voice_filename("aln")
    alan "「覚えていなければ、僕の勝ちとは言い切れないな」"

    "アランさんは淡々と言い、受け取った水を一気飲みした。"

    "体を起こすと、やはり彼は大きかった。"

    "――この後、何を話せばいいのか。"

    "私は少し迷ってから、ある提案をすることにした。"

    show rnk sun nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……取引をしよう。アランさんが調べたスケール・ジョーンズさんの情報を教えて。代わりに私は、≪未練≫のカードに書かれている単語を教える」"

    "突然の私の提案に驚いたのか、さすがのアランさんも即答はしなかった。"

    "私にとっては、最善と思える行動だ。彼とオデットさんとの会話の中では、アランさんがスケールさんの情報を知っていると示唆されていた。"

    "私が彼を指名するかは分からないが、いつ私の情報が向こうに知られるかは分からない。"

    "彼の≪死因≫を知っておけば、少なくとも指名された時に身を守ることはできるのだ。"

    "その手掛かりがあれば、聞いておいた方がいい。"

    show aln sca nor irr with std_change

    voice get_voice_filename("aln")
    alan "「――いいだろう」"

    "その後私は、アランさんからスケールさんについての調査情報を聞いたあと、≪Ⅸ・未練≫に書かれている内容を教えた。"

    "――金メダル。"

    "アランさんから聞いた話から、その裏付けになることが少し分かった気がする。"

    "今は彼の方にカードが生成された形跡はなかったが、アランさんならばすぐに情報同士を結びつけることだろう。"

    show rnk sun nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「それじゃあ、私もう行くから」"

    "明日は日曜日だけれど、できればお店は開けたいと思っていた。"

    "スマホも充電しないと不安だし、何より疲れた。"

    show aln sca nor lee with std_change

    voice get_voice_filename("aln")
    alan "「…………強さ、か」"

    show rnk sun nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「はい？」"

    "聞き返しても返事はなかったので、私は諦め、そのまま倉庫を後にした。"

    "最寄りの駅まで30分以上はかかる。また同じ道を歩くのかと思うと気が遠くなった。"

    $ add_seen_chapter("8-6")










    python:
        set_info_scene("131")
        set_info_date(6, 24, "sun")
        set_info_time("night")
        set_info_location("18")


    stop music fadeout 2
    scene bg lion02 nightclose with fade_longest
    play music audio.growapart
    pause 1

    $ show_hud()

    "深夜１時。"

    "大都会新宿といえど、終電がなくなってくる時間帯だ。"

    "海晴と直未は、ライオン館の前で凛火の帰りをまだ待っている。"

    show nom sun que que rev at std_c with std_in

    voice get_voice_filename("nom")
    naomi "「せんぱい……戻って来ないですね。こうなると心配を通り越して、その、か、彼氏さんとかと一緒にいたりって考えちゃいます……」"

    show nom sun hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「今日は土曜日ですし、せんぱいにお付き合いしてる人がいるかどうかって聞いたことないですし……」"

    show mhr sun nor ser rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「日辻さん？」"

    show nom sun har con with std_change

    voice get_voice_filename("nom")
    naomi "「は、はいっ」"

    show mhr sun pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そのくだらない想像は今すぐやめてくれないかい？」"

    "直未は背筋がぞくり、とするのを感じた。"

    "別に冗談で言ったつもりではないのだが、この話題はもうやめようと心に誓った。"

    show mhr sun nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「しかし、これ以上遅くまでここにいると、やがて警官に声をかけられてしまうかもしれない。終電もなくなってしまったし、困ったものだ」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「もっとも、日付でいう今夜にぼくがこのまま死ぬのであれば、帰ろうが帰るまいがもうどちらでもいいね」"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「あるいは――凛火へ向けた遺書を書き始めた方がいいのかもしれないね」"

    show nom sun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「み、海晴先輩……」"

    "真剣な表情で言う海晴に、直未はうまい言葉が見つからなかった。"

    "凛火に頼ろうと提案したのは自分である。待っていた時間をちゃんと調査に使っていればもしかしたらスケールの情報が集まったかもしれないと思うと、責任を感じていた。"

    "しかも海晴が仮に脱落すれば、その記憶も直未の中からは消えてしまうかもしれない。"

    "少なくとも、今よりずっと曖昧な、幼い頃の記憶よりもずっとぼんやりした、夢に変わってしまう。"

    "海晴と本音をぶつけ合った瞬間すらも。"

    "そう思うと、怖かった。"

    show nom sun har pin with std_change

    voice get_voice_filename("nom")
    naomi "「だ、大丈夫です。せんぱいなら、凛火先輩なら……」"

    "直未は震えた声でそう言った。"

    "根拠などどこにもないことを、二人とも分かっていた。"

    show mhr sun sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……君は、泣き虫だな。その素直さは時折、羨ましくもあるよ」"

    "海晴は不思議と、穏やかな気持ちになっていた。"

    "凛火が直未に対して抱いている感情は、こういう想いなのだろうか――今更になって、少しだけ――。"

    show rnk sun sur su2 at std_r with std_swap

    voice get_voice_filename("rnk")
    rinka "「え、ええっ」"

    "突然の声に、直未も海晴も目を円くしていた。"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴？　直未？　こんな時間に、なんでうちの前にいるの？」"

    show nom sun har ser rev with std_in

    voice get_voice_filename("nom")
    naomi "「せんぱいっ……！」"

    "直未は思わず、凛火に飛びつこうとした。"

    show nom sun fal sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「わきゅっ」"

    hide nom with DissolveMoveOut(0.5, yoffset(200), easein)
    play se "taoreru08"
    with quake_fast

    "暗がりで急に動いたせいで、そのまま転んだ。"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それはこちらの科白でもあるね。まさか、男性といた……ということはないのだろう？」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「うーん、途中まで男の人といたけど……って、何で知ってるの？」"

    show nom sun nor sur rev at std_c with std_in

    voice get_voice_filename("nom")
    naomi "「ええっ！？」"

    show mhr sun pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「――――――――――」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「と、とりあえずライオン館に入ろう。二人とも、私が来るのを待ってたってことだよね？」"

    "動揺している直未、放心状態の海晴、そして状況が全然分かっていない凛火の３人は、ライオン館へと入っていった。"

    "彼女たちの話が一直線に繋がるのは、１時間が経過してからのことだった。"

    $ add_seen_chapter("8-7")



label sentei8:

    call set_replay










    python:
        set_info_date(6, 24, "sun")
        set_info_scene("132")
        set_info_time("night")
        set_info_location("06")


    stop music fadeout 2
    scene bg fatalhall01 up large with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    show dia sta fro no2 big at std_c with std_in

    voice get_voice_filename("dia", 170)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "女神の声が、≪運命の大広間≫に響く。"

    "８度目の、女神の選定。"

    "残っているのはすでに当初の半分、Ⅰ・Ⅱ・Ⅲ・Ⅸ・Ⅺ・Ⅻの６人のみ。"

    "そして今夜はもう、一人減ることが確定している。"

    "オレの初指名。が、オデットを脱落させるのだ。"

    scene bg fatalhall01 up with dissolve

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「皆サマ、本日はおしゃべりなさらないのですわね。ワタクシ、退屈ですわよ？」"

    show ode sta nor lau rev ci at ci_l with ci_in

    voice get_voice_filename("ode", 487)
    odette "「かかっ、じゃーてめーが喋ってくれよ。何か面白い話をなァ」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「面白いお話、でございますか？」"

    "これから脱落が待っているというのに、オデットの態度は相変わらず平然としていた。"

    "オレはそれがとても、腹立たしかった。"

    show fed sta nor cla ci at ci_r with ci_in

    voice get_voice_filename("fed", 242)
    federico "「どうでもいいだろ、そんなのよ！　早く指名にうつってくれ！」"

    "オレは痺れを切らして、そう叫んでいた。"

    "オデットが余裕の表情でにやりと笑い、オレを一瞥した。"

    "その表情が、オレの心を乱すんだ。"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「あらあら。まるで早く指名したいと、そういう風にお見受けされますわね」"

    show fed sta nor irr ci with ci_change

    voice get_voice_filename("fed")
    federico "「くぅっ……」"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「いいでしょう。それでは、今宵も選定を始めますわ」"

    "女神は高らかに、そう宣言した。"

    "オレに恥をかかせやがって、女神とはいえこいつもムカつくガキだ。"


    voice get_voice_filename("dia")
    parca "「廻りなさい。運命の大時計」"

    "女神のこの言葉の後には、一人ずつ指名の意志確認が始まる。"

    "もうすっかり慣れた流れだ。"




    play music audio.restlessness
    scene bg fatalhall01 up
    show rnk uni nor nor ci at ci_r
    with dissolve_long

    voice get_voice_filename("rnk", 1253)
    rinka "「私は、ない」"

    hide rnk with ci_out

    "Ⅰ番の女を通り過ぎる。"

    "次のⅡはミハルだ。今までの流れからいって、こいつも今日は指名がないだろう。"

    "オレ、ミハル、スケールの協力関係の中では、今日の指名はオレだけがすることになっているのだから。"

    show mhr uni sco smi rev ci at ci_l with ci_in

    voice get_voice_filename("mhr", 550)
    miharu "「ぼくは――Ⅺ番、あなたを指名するよ」"

    $ add_character_cards("mhr", ["11_death", "11_regret"])

    show fed sta nor pa1 ci at ci_r with ci_in

    voice get_voice_filename("fed")
    federico "「なっ、何ぃぃっ」"

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「うふふふ。承知いたしましたわ」"

    hide mhr with std_out

    "ど、どういうことだ。"

    "オレは全くの予想外の出来事に、動揺を隠すことができなかった。"

    "焦る心で、Ⅺの床の上に立つオデットの姿を見た。"

    "相変わらずのにやけた顔でこっちを見てやがる。まるでこうなることが分かってたとでも言いたげな顔だ。"

    "ミハルがオデットを指名するんだったら、オレの指名は必要ないんじゃねぇか？"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「Ⅲ番サマは、いかがなさいますか？」"

    show fed sta nor pa2 ci with ci_change

    voice get_voice_filename("fed")
    federico "「オレはし――」"

    "言いかけて、すぐにその言葉を訂正した。"

    show fed sta nor smi ci with ci_change

    voice get_voice_filename("fed")
    federico "「いや、オレもⅪ番を指名だ」"

    "危ないところだったぜ。動揺していたせいで、オデットがオレの情報を持っているのを忘れるところだった。"

    "ミハルがオデットを脱落させれば、オレのカードがミハルに取得されちまう。"

    "まさか、それを狙って……。"

    show sca sta nor bit rev ci at ci_l with ci_in

    voice get_voice_filename("sca", 168)
    scale "「…………何？」"

    "スケールの表情を見るに、奴もこの展開を予想できなかったらしい。"

    "スケールが海晴にオデットを指名させたって線は……さすがにないか。メリットがない。"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら、重複してしまいましたわね。けれど少々お待ちください。このまま、時計の針が一周してからまたおうかがいいたします」"

    "人数が減っちまった今の状況だと、オレの次はスケールだ。"

    show sca sta nor nor rev ci with ci_change

    voice get_voice_filename("sca")
    scale "「……Ⅱ番を指名だ」"

    show fed sta nor pa3 ci with ci_change

    voice get_voice_filename("fed")
    federico "「何っ」"

    "こいつも、指名？"

    "それも指名する相手は、ミハル。"

    "スケールはいつものわざとらしい笑いではなく、口角が震えていた。邪悪な含み笑いを堪えているのだろう。"

    "こいつら、揃いも揃って。"

    "信用しているわけじゃなかったが、それでも申し合わせくらいはするもんだと思っていた。"

    show fed sta nor irr ci with ci_change_wait

    "Ⅰのリンカは、ミハルが指名されても絶望した様子はない。どうやらこいつらは完全に仲違いしちまっているらしい。"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「承りました」"

    hide sca with ci_out

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「おあとは……Ⅺ番サマはどうなさいますか？」"

    show ode sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("ode")
    odette "「あたしはなし、だ。分かってんだろ？」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシはあくまで選定の管理者。貴女サマの本来の運命は見えていても、これから待ち受ける可能性は分かりませんわ」"

    show ode sta arm smi rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「かかっ、御託はいいんだ」"

    hide ode with ci_out

    "パルカは不機嫌そうに頬を膨らませてから、Ⅻのアランへと問いかけた。"

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln", 256)
    alan "「僕も指名は――しない」"

    hide aln with ci_out

    show dia sta fro no2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでは、まずはⅡ番サマとⅢ番サマの指名の重複について、対応いたします」"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「ご自分のカードを１枚オープンにすることで、指名の優先権を取得することができますわ。いかがなさいますか？」"

    show fed sta nor ang ci with ci_change

    voice get_voice_filename("fed")
    federico "「オレは自分の≪氏名≫をオープンにするぜ。これで優先権はオレのものだ」"

    "どうせ、オレの指名はすでにここにいる全員に割れてしまっている。"

    show mhr uni nor ser rev ci at ci_l with ci_in

    voice get_voice_filename("mhr")
    miharu "「……待ってくれ。優先権を取得する意志確認は、番号の若いぼくからするものではないのかい？」"

    show mhr uni sco thi rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「ぼくも優先権を取得させていただくよ。今度は≪死因≫。そのカードをオープンにするさ」"

    show dia sta nor nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「承知いたしましたわ。これでお互いに１枚ずつカード公開の意志をお見せいただきました」"

    show mhr uni sco wic rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。ぼくはこれ以上カードを見せることはしないさ。どうするんだい、Ⅲ番さん？」"

    show fed sta nor bad ci with ci_change

    voice get_voice_filename("fed")
    federico "「てめー……！」"

    hide mhr
    hide dia
    show ode sta nor tro rev ci at ci_l
    with ci_swap

    "オレは、オデットの方へ視線を向けた。"

    "すでにあいつは、笑っていなかった。獣の目、とでも言うべきだろうか。"

    "ただ真っ直ぐに、オレを睨みつけている。身のすくむような眼光。思えばそれがオレに向けられたのは、これが初めてかもしれない。"

    "このまま指名が流れれば、どうなる？"

    "次回の選定でオデットはオレを指名するだろう。その時に防御された場合、オレはもう１枚カードを公開しなければならない。"

    "仮にオレが指名をしなかったら、今度はオデットがオレを指名するはずだ。"

    "オレが防御を選択しても、あいつはまだ選定では一枚も≪自身のカード≫を公開していないから、確実に防御を破壊してくるだろう。"

    "お互いが同時に指名すれば、そのまま二人とも脱落して終了……か。"

    hide ode
    show dia sta nor smi rev ci at ci_c
    with ci_swap

    voice get_voice_filename("dia")
    parca "「Ⅲ番サマも、指名はなしでよろしいでしょうか？」"

    "女神が不敵な笑みを浮かべ、オレに問い掛けてくる。"

    "いや、もはや選定をどう戦うかっていう計算の話じゃない。"

    "ここでいかなきゃ、オレはオデットに一生勝てない。今があの巨星を落とす最大のチャンスだ。"

    "あいつに勝てさえすれば、オレは他の誰にも、きっと――！"

    show fed sta nor pa3 ci with ci_change

    voice get_voice_filename("fed")
    federico "「待て」"

    "だが、オデットはオレのカードを３枚集めているはずだ。とすれば、選定に入っても防御されちまうんじゃねぇか。"

    "そうなったら、オレは≪未練≫も公開しないといけなくなる。"

    "唇が停止する。"

    "瞬間、オレの頭はこれまでにないくらい巡り始める。"

    "長く共に過ごしてきたからこそ分かる。オレに指名をされて、黙っている女じゃねぇ。"

    "あいつがオレを指名しないのは、オレを指名できないからだ。"

    "オレの≪未練≫に繋がる話は、カマをかけてきただけ。"

    "ならば、行動は決まっている。"

    show fed sta nor ang ci with ci_change

    voice get_voice_filename("fed")
    federico "「オレの≪死因≫もくれてやる。だからオレに、あいつを倒す権利をくれ」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「承りましたわ」"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それではこれより、Ⅲ番サマによるⅪ番サマの指名を行いますわ」"

    show fed sta nor pa1 ci with ci_change

    voice get_voice_filename("fed")
    federico "「うおっ」"

    hide fed
    hide dia
    with ci_out

    "突然の地響きに、オレは一瞬うろたえた。"

    "オレの立っている床は、この大広間の中を垂直に上昇していく。"

    "天井も果てもない、上層へと。"







    $ set_info_location("16")

    scene bg fatalhall02 up with fade

    show fed sta nor int ci at ci_r with ci_in

    voice get_voice_filename("fed")
    federico "「ほとんど変わらないんだな……{rb}下層{/rb}{rt}した{/rt}と」"

    "運命の大広間の上層。オデットから話では聞いていたが、確かに、下層とほとんど変わらない造りになっていた。"

    "唯一違うのは、ここではオレとオデットの二人が向かい合っているということだ。"

    "浮遊する床の上に、オレとあいつだけだ。"

    show ode sta arm smi rev ci at ci_l with ci_in

    voice get_voice_filename("ode")
    odette "「まさか、てめーに指名されちまうとはな」"

    show fed sta nor irr ci with ci_change

    voice get_voice_filename("fed")
    federico "「強がりのつもりか？　少しはビビってみせろよ。これから死ぬんだぜ、あんたは」"

    show ode sta nor tro rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「何を言ってる。あたしもてめーも、元々すでに死んじまってるんじゃねぇか」"

    show ode sta nor lau rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「怖がることなんてありはしないさ。ゲームに負けちまって悔しいなぁ……その程度だ」"

    show ode sta nor inn rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「最期だから言っておくぜ。てめーと駆け回るのは、退屈はしなかったさ。ま、どちらかといえば楽しい日々だった」"

    "オデットはしんみりとした口調で、言ってきた。"

    show fed sta dar dar ci with ci_change

    voice get_voice_filename("fed")
    federico "「……楽しいかそうじゃないかの二択なら、楽しい方に傾くよ。あんたと飲むワインはまあ、悪くなかったな」"

    show ode sta nor lau rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「かかかかっ！　てめー、何つられてやがるんだ！　っとーに甘えな。裏切りなんて向いてねーんだよ。いやぁ、最期にしんみりとしたフェデリーコくんっていう面白いモンを見させてもらった」"

    show fed sta nor pa4 ci with ci_change

    voice get_voice_filename("fed")
    federico "「この野郎っ……！」"

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「あらあら、仲良しさんですわね」"

    show fed sta nor pa1 ci with ci_change

    voice get_voice_filename("fed")
    federico "「うわっ、どこから」"

    "オデットに気を取られていたせいで、女神の存在をすっかり忘れていた。"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「女神の選定では皆サマ、≪因果の刻≫という運命の糸で繋がっています」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「これまでも――今までの選定の際も、貴女方のように仲良しさんたちはいらっしゃいました」"

    show dia sta nor smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「うふふふ、ワタクシ、その瞬間を見るのがとても、心地よいのですわ」"

    show ode sta arm ser rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「……いい趣味してるな」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「ありがとうございますわ」"

    show fed sta nor bad ci with ci_change

    voice get_voice_filename("fed")
    federico "「勘違いするな。オレたちは別に仲良しなんかじゃねぇ。利害関係で繋がっていて、旨味がなくなったからこいつを脱落させるってだけだ」"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「あらあら、素直じゃありませんね」"

    show fed sta nor cla ci with ci_change

    voice get_voice_filename("fed")
    federico "「うるせぇっ！　いいから、とっとと指名させてくれ」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「そうですわね。今宵はもう一組指名がございますし、あまり時間をかけてもいられませんね」"


    play music audio.electing

    "パルカがそう言うと、オレのカードブックが光を放つ。オレの所持しているカードが、空中に浮かび出す。"

    "オデットから指名の手順を聞いていたから、迷うことはない。この中から、あいつの３枚のカードを選び取ればいいのだ。"

    show fed sta nor irr ci with ci_change

    voice get_voice_filename("fed")
    federico "「氏名――オデット・マランソン」"

    show ode sta nor nor rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「最期にてめーにひとつ聞いておきたいことがある」"

    show fed sta nor bad ci with ci_change

    voice get_voice_filename("fed")
    federico "「死因――圧死」"

    show ode sta nor lau rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「あたしはよぉ、人生を楽しむために生きてきた。てめーは何のために生きたいんだ？」"

    show fed sta nor ama ci with ci_change

    voice get_voice_filename("fed")
    federico "「オレは……」"

    "オデットの質問を受けて、オレはカードを選び取る手を止めた。"

    "しかしその回答に逡巡することもなく、答えた。"

    show fed sta nor ang ci with ci_change

    voice get_voice_filename("fed")
    federico "「生きるのに理由なんて、いらないだろ」"

    show ode sta nor nor rev ci with ci_change

    voice get_voice_filename("ode")
    odette "「――そうかい。てめーも案外、はき違えちゃいないってわけだな」"

    show fed sta nor irr ci with ci_change

    voice get_voice_filename("fed")
    federico "「……戯言だな。あんたらしくない」"

    show fed sta nor irr ci with ci_change

    voice get_voice_filename("fed")
    federico "「未練――出産」"

    "３枚のカードを選び取ったことで、カードはオレの手を離れて動き始めた。"

    scene ecg trianglecard cover with dissolve_long

    "この空間の中心で三角に並び、動きを止めた。"

    "カードが蓄えていた光が爆発するかのように、空間ごと光が覆いつくす。"

    "オデットの表情は、クソ、今までにないくらい穏やかでありやがった。"




    stop music fadeout 2
    scene white with Dissolve(3)
    play music audio.death
    pause 2

    scene black with dissolve_longest

    "襲撃を受ける船の上。"

    "相手は、時代遅れの海賊だ。要は武装船。"

    "この船は武器や違法流通している宝石類を積んでいるから、それを奪いにきたってわけだ。"

    "相手が１隻なら、この運送会社が後をとることはない。何故ならオデット・マランソンがいるからだ。"

    "だが今回は違った。"

    "彼女を疎ましく思う連中が協力して、元より船を撃沈し、乗員を皆殺しにするつもりで攻めてきたのだ。"

    scene ecg ontheship a with dissolve

    "８隻の船に囲まれ、手も足も出なくなっていた。"

    "オデット以外の乗員はすでに殺されていた。もっとも敵の船員も多くはすでに死亡している。"

    "船上は、阿鼻叫喚の様相を呈していた。"

    "偶然乗り合わせたイタリアン・マフィアの男がいた。彼が逃亡中だということを、オデットは知っていた。"

    "その時、船体に重い衝撃がのしかかる。"

    "攻撃を受けた船が崩壊を始めたのだ。"

    "マフィアの男はオデットにとって一般人も同様だ。海のプロかそうでないかが、船の上での彼女の基準だからだ。"

    "彼に向かって、割れた舟板が飛んで行く。"

    show ecg ontheship with ecg_change_wait

    "それを、オデットは自らの腹で防いだ。"

    "きっと永遠に本人は認めないだろう。仮に生きていれば、自分のいたところに偶然、舟板が飛んできたと主張するだろう。"

    "だがそこにある事実は、オデットがマフィアの男をかばったということだった。"

    "直後、船は大きく揺れ、完全に崩壊をむかえた。"

    "オデットとマフィアの男は、崩れた船に押し潰された。"


    scene bg fatalhall02 up
    show fed sta dar dar ci at ci_r
    with fade_longest
    pause 1


    voice get_voice_filename("fed")
    federico "「嘘……だろ」"

    "意識が戻ってきたとき、オレは胸をおさえていた。"

    "動悸が激しくなって、夢の中にもかかわらず汗が止まらない。"

    "オレはオデットの死の瞬間の映像を見ていた。"

    "あいつは、あいつは――っ。"

    show fed sta dar dar ci with ci_change

    voice get_voice_filename("fed")
    federico "「オレを、オレを守っていた……？」"

    "眼球が乾いていく。"

    "湧き上る屈辱が、オレの全身から水分を蒸発させていく。"

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「くすっ」"

    "まるでミハルの口癖ように微笑むとパルカが再びそこに現れた。"

    "パルカはオレにオデットの持っていたカードを教える。その中から１枚を選び、取得できる。"

    show fed sta dar dis ci with ci_change

    voice get_voice_filename("fed")
    federico "「そんな、わけが……」"

    "その中には、オレの≪氏名≫≪死因≫≪未練≫全てがあった。"

    "あいつはオレが３枚のカードを選び取った時点で、防御しようと思えばできたんだ。"

    show dia sta fro no2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでは、きちんと選んでおいてくださいね」"

    "パルカの声が遠くなるのと同時に、オレの立っている床は垂直に下降し始めた。"

    "今度はその動きにふらつくことはない。すでにオレ自身の意識がふらついてしまっていたからだ。"



    show fed sta dar dar ci with ci_change

    voice get_voice_filename("fed")
    federico "「≪Ⅱ・死因≫でいいさ……」"

    "オレが取得することができたのは皮肉にも、ミハルがこれからオープンにするカードであった。"

    python:
        add_character_cards("mhr", ["2_death"])
        add_character_cards("fed", ["2_death"])

    "もうそんなこと、どうでもよかった。"

    "オデットは死に際、オレを助けた。"

    "オデットはオレの予想を外れ、カードを揃えていた。防御できたのに、しなかった。"

    "その真意をオレは一生知ることはできない。"

    "あいつを脱落させたにもかかわらず、オレは、オレは……。"

    show fed sta nor cla ci with ci_change

    voice get_voice_filename("fed")
    federico "「クソがぁっ！　畜生っ！　畜生っ！」"

    hide fed with ci_out

    "オレは目の前に設置された書見台を蹴ろうとしたが、うまく蹴れずに転んでしまった。"

    show dia sta fro gl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「夢の世界の物ですもの。攻撃しようとしても無駄ですわ」"

    $ set_info_location("07")

    scene bg fatalhall01 normal with fade_long
    pause 1

    "下層へ戻ってきたパルカは、にやりとした顔でそう言った。"

    "クソ、こいつもムカつく。"

    "全てが、クソだ。"

    scene bg fatalhall01 up with dissolve

    show dia sta nor ama rev ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「それでは、まずはオープンになったカードをいただきます」"

    "パルカはオレから２枚、ミハルから１枚カードを受け取った。"

    "オレ以外の参加者のカードブックが光る。"

    "オレはオデットを脱落させた時にミハルのカードを取得しているから反応しない。"

    show fed sta dar imp ci at ci_r with ci_in

    voice get_voice_filename("fed")
    federico "「畜生……」"

    "オレの声はもう誰にも聞こえないだろう。"

    "底のないこの夢の世界で、虚しく落ちていく。"








    $ set_info_scene("133")

    stop music fadeout 2
    scene bg fatalhall01 up with fade_longest
    play music audio.fatalhall
    pause 1

    python:
        add_character_cards("rnk", ["2_death","3_death"])
        add_character_cards("mhr", ["3_death"])
        add_character_cards("fed", ["3_death"])
        add_character_cards("sca", ["2_death","3_death"])
        add_character_cards("aln", ["2_death","3_death", "3_name"])

    show sca sta nor imp ci rev at ci_l with ci_in

    voice get_voice_filename("sca")
    scale "「ぐ……」"

    show mhr uni sco smi ci at ci_r with ci_in

    voice get_voice_filename("mhr")
    miharu "「くすっ」"

    "フェデリーコさんの指名が終わったあとは、海晴がスケールさんに指名される番だった。"

    "正直かなり心配だったが、無事、海晴は戻ってきた。"

    "土曜日の深夜、ライオン館の前で海晴と直未が待っていた時はびっくりした。"

    "事情を聞いて、あの時戻って来て本当によかったと思った。そして、勇気を出してアランさんと交渉をしてよかったとも。"

    "日曜日を一日使って、スケールさんの≪死因≫と≪未練≫にまつわる背景情報を導き出した。"

    "カードに書かれた単語は分かっていたので、難しい作業ではなかったはずだが、それでも丸一日かかった。"

    "海晴と直未がいなかったら、成し遂げることはできなかっただろう。"

    "現実世界で、今も二人は私の隣で寝ているはずだ。"

    "私もスケールさんを指名することができたがそうしなかったのは、「どうせ脱落するなら」と海晴の防御の破壊を行う危険性があったからだ。"

    "次回の選定までに他の参加者に情報を知られるリスクは高まるが、安全策をとった。"

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「おやおや、大波乱と申し上げた方がよろしいでしょうか？」"

    hide mhr
    show aln sta nor irr ci at ci_r
    with ci_swap

    voice get_voice_filename("aln")
    alan "「好きにしろ。どうせ貴様には関係ないのだろう、女神？」"

    show sca sta nor smi rev ci with ci_change

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡ……、やられたねぇ」"

    hide sca
    show fed sta dar dar rev ci at ci_l
    with ci_swap

    voice get_voice_filename("fed")
    federico "「畜生……」"

    "残念だが女神の言う通り、大波乱という他はない。"

    "現に今も私の心臓はどきどきしている。"

    "慎重なスケールさんが万が一大胆な行動に出たら、私は海晴を失っていたのだ。"

    "そんなの、絶対に嫌だ。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro no2 big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者は１名。これをもって、選定を終了といたしましょう」"

    "女神の澄んだ声が、高らかに響く。"

    "私の意識は、現実へと戻っていくのだった。"

    "一つの可能性、まだ思いつきに過ぎない一つの方法を抱いて。"

    $ renpy.end_replay()
    $ add_seen_chapter("8-8")

    $ persistent.sentei8_clear = True
    $ grant_achievement("divine_selection_08")

    jump f009
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

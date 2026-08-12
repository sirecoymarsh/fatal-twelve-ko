

label f010:






    python:
        set_info_scene("156")
        set_info_date(7, 2, "mon")
        set_info_time("emorning")
        set_info_location("01")


    stop music fadeout 2
    scene ecg pattern nor a with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    show let sta nor sm1 at std_c with std_in


    voice get_voice_filename("let")
    lete_unk1 "「ひとまずお疲れ様、と言っておこう。今宵は君も一人の運命を終わらせた」"

    show let sta nor tro with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君の見えないところで、君の心には大きな負担になってしまったようだけれど」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「もっとも、君はすでに自分が一人ではないことを知っているね。それは、君にとってもっとも大きな力だと私は思っているよ」"

    "≪女神の選定≫の夢から覚めると思ったのに、どうやら運命とやらは私をまだ起こしてはくれないらしい。"

    "すでに顔見知りになるほど私の夢に現れた男性が、今日も現れていた。"

    "相変わらず私はぼんやりと思考するだけで、体を動かしたり何か言い返したりという反応はできない。"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「さて、君は一つ新しいカードを手に入れたね。それは新しい記憶を手に入れたのにも等しい」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「今夜は階段をまた一つ上った君へのお祝いだ。君の忘却を呼び戻してあげよう」"










    stop music fadeout 1
    scene bg shinjukugyoen evening large with wfade_long
    play music audio.memories
    pause 1

    "幼い頃の記憶。"

    "私は子供の頃、近くの公園へ行くことがあった。"

    "公園といっても、そこは観光スポットにもなっている有名な場所。"

    "おばあちゃんが喫茶店で忙しく一人で遊ぶことの多かった私は、子供ながらにしてよくそこへ遊びに行っていた。"

    "きっと、私が小学校にあがる前のことだったと思う。"

    "私はその場所で、同い年くらいの女の子と出会った。"

    show rnk kid nor que at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「……どうしたの？」"


    show mhr kid nor ave rev at std_cr with std_in

    "女の子は、私の質問には答えてくれなかった。"

    "年の近い子供が一人でいるのは珍しかったから、私は遊びたかったんだと思う。"

    "しつこく、声をかけた。"

    "その全部を、女の子は無視した。"

    "私は諦めて、女の子の隣に座った。"

    "女の子は私が声をかけている間もずっと、どこか遠くを見つめていたのだ。"

    "私も同じように、何も言わずに遠くを見てみることにした。"

    "閉園時間がきて、私たちは外へ出た。"

    show rnk kid nor smi with std_change_wait

    "私は「またね」と言ったが、女の子は何も答えなかった。"

    scene black with dissolve

    "――次の日。"

    scene bg shinjukugyoen evening large with dissolve

    show mhr kid nor ave rev at std_cr with std_in

    "女の子はまた同じ場所で同じように座って、同じように遠くを見ていた。"

    show rnk kid nor spa at std_cl with std_in

    "私は今度は声をかけずに、隣に座った。"

    "今思うと、よく我慢できたものだ。きっとその子の真似っこをしているから、何も言わずに座っていられたのだろう。"

    "その日も閉園時間まで、ずっと隣にいるだけで過ごした。"

    "またねと言って、別れた。"

    "――さらに、その次の日もその子は同じように過ごしていた。"

    "もちろん、私も。"

    "この日も別れ際に、私は「またね」と言った。"

    "――そして、さらにもう一日が経った日。"

    show mhr kid nor anx rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼく、明日からとおくへ行くんだ」"


    "その時、女の子なのにぼくなんて珍しいなぁ、と思った記憶がある。"

    "３日間も無視をされた女の子がようやく声をかけてくれて喜んだり怒ったりするべきだったんだろうけど、その辺りが子供らしい。"

    show rnk kid nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「遠くに？」"


    show mhr kid nor ave rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そうさ。ぼくのお父さんは、くるまでじこをおこして、ひとをころしちゃったんだって。まわりの人の目があるから、ひっこさなきゃいけないんだって」"


    show mhr kid nor anx rev with std_change

    voice get_voice_filename("mhr")
    miharu "「とおくへ行くのって、こわいよ」"


    "その意味を、私はよく分かっていなかった。"

    "だから、私はあっさりと答えていた。"

    show rnk kid nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「だいじょうぶだよ。さびしくなったら、またくればいいんだよ。わたしはいるよ。きっと、ずっと、ここに」"


    show mhr kid nor anx rev with std_change

    voice get_voice_filename("mhr")
    miharu "「なら、名前をおしえて」"


    show rnk kid nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「りんか。わたしはししまいりんかだよ。あなたは？」"


    show mhr kid nor smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「みはる。ぼくの名前はみはるだよ」"


    show rnk kid nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「うんっ」"


    "名字なんて、どうでもよかった。"

    "当時の私は名字と名前という概念をよく分かっていなかったのだ。"

    "おばあちゃんに名前を聞かれたらこう答えなさいと口癖のように言われたのを、丸暗記していただけなのだから。"

    "この日、私たちはたくさんお話しして、たくさん遊んだ。"

    show mhr kid nor anx rev with std_change

    voice get_voice_filename("mhr")
    miharu "「きょうは、さよなら、なのかな？」"


    "別れ際、女の子は不安げな声で訊ねてきた。"

    "きっと例によって、私は何も考えていなかったんだと思う。"

    "だから答えた。"

    show rnk kid nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「ううん。またね、だよ！」"


    "それ以来、あの場所で女の子と会うことはなかった。"

    "できたばかりの時計台がよく見える、あの場所で。"

    "そう、その場所は≪運命の終着点≫であり、きっと私たちの≪ハジマリ≫の場所でもあったのだ。"









    python:
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 1
    scene bg myroom morning large:
        zoom 1.5
        align (0.0, 0.6)
    with wfade_long
    play music audio.myroom_refreshing_morning
    pause 1

    $ show_hud()

    show rnk paj nor que up rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「なんでこんな記憶を、忘れてたんだろう」"

    "目を覚ましたとき、悪夢を見たという印象はなかった。"

    "あの男性が夢に出てきたとき、大体嫌な汗をかいて起きるのに。"

    scene bg myroom morning with dissolve

    show lete normal at cat_c with std_in


    voice get_voice_filename("cat")
    lete "「にゃーん」"

    "黒猫のレテが、私の布団をはいでいたらしい。それで妙に涼しかったのか。"

    "いや、きっと温度の問題じゃない。"

    "――だって、あの男性が夢に出てきたということを、目を覚ました今も覚えているのだから。"

    "そのことさえ、忘れていた。分からなかった。"

    "こうして思い返してみると、私は何度もあの男性に眠っていた記憶を呼び覚まされていた。"

    "人は寝ているとき脳で記憶の整理をしていて、その一部を夢として見るという説がある。"

    "忘れていた過去の記憶を夢で見るというのはあり得ることなのかもしれないが、私の見た記憶はどちらかというと、追体験といえるほど生々しいものだった。"

    "――夢。"

    "運命の女神パルカは、夢の世界は可能性の世界であるとも言っていた。だとすれば、これは単なる記憶ではなく、すでに通り過ぎた世界でもあるのかもしれない。"

    "あの男性は、一体――。"


    voice get_voice_filename("cat")
    lete "「にゃ？」"

    "レテの方を見てみても、何も答えてくれるはずはない。"

    "もしかしたらこの黒猫も、一緒に過去の記憶を夢で見ているのかもしれないけれど。あれ、そもそも猫って夢見るのかな。"


    scene bg myroom morning large:
        zoom 1.5
        align (0.0, 0.6)
    show rnk paj arm sad up rev at std_l
    with dissolve

    voice get_voice_filename("rnk")
    rinka "「しかし最低だな、私。あんな大事なこと、忘れてたなんて」"

    "海晴はあの公園でのことを覚えているのだろうか。"

    "海晴のことだから、覚えているに違いない。"

    "きっと私が忘れていることにも気付いていて、あえて口にしなかったのだ。"

    "思い出してしまえば、海晴の告白にはより重みが出る。あるいは――あの数日間からずっと、海晴は私を好きでいてくれたのかもしれない。"

    "それはさすがに、思い上がりかな。でも「さよなら」が嫌いで「またね」が好きな海晴だから――。"

    show rnk paj nor shy up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「返事、かぁー……」"

    "思い出すと、また顔が熱くなってきてしまう。"

    "告白されてから、もうすぐで１週間が経とうとしている。告白された側って、返事をする期限とかあるのかな。そんなの誰も教えてくれない。"

    "もう少し、もう少し待ってもらおう。もし聞かれたら、ちゃんと謝って説明しよう。"

    "今はまだ――アランさんとフェデリーコさんがいる。だから彼らとの決着がつくまでは、まだ答えられない、と。"





    python:
        set_info_scene("157")
        set_info_location("08")

    scene bg schoolroom noon with fade_long
    pause 1

    $ show_hud()

    show mao uni nor lau at std_c with std_in

    voice get_voice_filename("mao", 256)
    mao "「あ、りーたん。おはよ～」"

    "最近はいつも、月曜日の朝に学校へ行くと安心するようになっていた。"

    "今日も、無事ここに来ることができた、と。"

    "海晴もすでに登校していて、私たちは授業が始まるまでしばらく話をした。"






    python:
        set_info_time("noon")
        set_info_location("15")

    scene bg schoolrooftop noon with fade_long
    pause 1

    $ show_hud()

    "昼休み、私たちはいつも通り屋上でお昼ご飯を食べる。"

    "真央は５限に提出しなくてはならない宿題をやるため、教室に残っている。先週の木曜日に出た宿題だ。"

    "私は出たその日に終わらせているので、真央のように焦ることはなかった。"

    "ご飯を食べながらしばらく世間話をした後、この話題は私から切り出した。"


    play music audio.gimon

    show rnk sun nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ねえ、海晴。昨日の≪運命の大広間≫での話なんだけどさ……」"

    "それは、フェデリーコさんと女神パルカが話していたことだ。"

    "女神の力を使用することができるのかどうか、という話。器になった人が女神の力を使用することはできないが、女神は器の中からでも運命を変えることができると言っていた。"

    "その時、海晴は何かに気付き驚いたような反応をしていたのだ。"

    show mhr sun sco cau rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「君はすでにぼくの≪未練≫を知っている。だからこそ話そう。女神パルカも恐らく、ぼくが君を想っていることを知っていた」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくが君とこの学校で再会できたのは、女神が運命を変えたからかもしれない、と思ったからさ」"

    "あの時――公園での出会いから海晴は私とずっと再会したいと思っていてくれたらしい。"

    "しかし、家庭の事情もあり、それは叶わなかった。"

    "海晴はあの直後、田舎へと引っ越したらしい。"

    "お父さんが事故を起こして幼い子供の命を奪ってしまったことが根本的な原因だ。"

    "近隣の人たちから避けられたり嫌がらせを受けたりするようになり、とても海晴を近所の小学校に通わせられる状態ではなくなったらしい。"

    "田舎に引っ越し、海晴の家族は夫の姓を名乗るのをやめ、母方の姓を名乗るようになったらしい。"

    "しかし、海晴のお父さんは事故直後から精神を病んでしまい、働くことができなかった。"

    "そして海晴が小学校６年生の時、自ら命を断った。"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「父親は自分の罪の重さに押し潰されたんだ。ぼくは彼を、無責任だとは思わない――もっともその心の弱さは、はっきりと遺伝しているけれどね」"

    "海晴の死因は≪自殺≫。カード化されているのでその情報こそ知ってはいたが、理由は聞いていなかった。"

    "知らないということは、それは知らなくてもいいことかもしれない。"

    "海晴はそのまま、話を続けた。"

    "父親の自殺をきっかけに、再び彼の過去の事故の噂が立った。"

    "田舎という小さなコミュニティの中で、それはもっと厳しかったという。海晴たち家族は、同じ理由で再び引っ越すことを余儀なくされた。"

    "再び首都圏に戻ってきた海晴は、大学受験も視野に入れ、進学校かつ、中等部から特待生制度を行っている飴茶を選んだ。"

    "ししまいりんか、という名前しか分からない状況ではとても再会は望めない。特に私は部活もやっていなかったし、どこかに名前が載ることもなかった。"

    "――それでも海晴は、ずっと私と会いたいと思っていてくれた。東京の学校なら、いつか会えるかもしれないと思っていたそうだ。"

    show mhr sun nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「希望は潰えたと思ったとき、高校でぼくは君と再会することができた。君は記憶よりもずっと凛々しく、可愛く、とても魅力的だった」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「偶然、もしくは奇跡と思っていたけれど、ぼくの想いを知っている女神が、君と出会うように運命を変えたとしたら――？」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……何のために？」"

    show mhr sun pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくたちがそれぞれ≪因果の刻≫に命を落とすことを知っていて、≪女神の選定≫で蹴落とし合う姿を楽しむために」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「飴茶女子は進学校で、高校から入学するには偏差値がかなり高い。君の中間テストの順位は一般的な内部進学組以下だった。運命が改変されでもしなければ、君が受かるとも思えない」"

    show rnk sun nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「……あの、真顔で失礼なこと言わないでくれない？」"

    "海晴の過去から一転して、ふざけているのかとも思った。"

    "しかし海晴はあくまで真面目にそう語っていて、私はちょっと傷ついた。"

    "もっとも入学してからの成績の悪さを海晴は知っているので、そう思うのも無理はないと思うと、怒りを通り過ぎて余計に傷ついた。"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……食事時にする話ではなかったね。失礼したよ」"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「ううん、大丈夫。それに、心配し過ぎだよ。私だって、ちゃんと勉強すればそれなりの点数はとれるしね。高校受験の時は頑張ったし、自分の実力だって言い切れるよ」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「それに……もし女神が運命を変えて私たちが再会したんだとしてもさ、今日まで過ごしてきた事実がなくなるわけじゃない」"

    "私は自信をもって、そう答えることができた。"

    "≪女神の選定≫における運命の改変は本物だ。記憶の辻褄合わせは完全ではないにしろ、私たちの理解の及ばない力が働いているのは間違いない。"

    "でも、それでも、この日々は嘘じゃない。"

    show mhr sun sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……ああ、そうだね。余計な心配だった」"

    "海晴はそう言うと、毒気の抜けた顔で笑ってくれた。"

    "晴れた空の下、かすかに吹く風に海晴の髪が揺れる。"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ところで、ぼくに疑われないように、期末テストはちゃんと勉強するんだよ？　こんな状況だけれど、君にはこれからも学校生活があるんだから」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴も――でしょ。私の意見は変わらないよ」"

    "長話をしていたので、直後に予鈴のチャイムが鳴った。"

    "私たちは急いで片づけをして、教室へ戻ることにする。"

    "二人きりであったが、告白の返事については聞かれなかった。私はそのことに、ちょっぴり罪悪感を覚えていた。"









    $ set_info_scene("158")

    scene bg schoolrooftop noon with fade_longest
    pause 1

    $ show_hud()

    "未島海晴は、教室へ戻る凛火の背中を見ていた。"

    "海晴は、凛火が子供の頃に自分と出会ったことを忘れていると思っていた。"

    "凛火の様子を見るに覚えていたようだが、恐らくは自分の告白か、≪未練≫のカードを見たことかをきっかけに思い出しただけだろうと分かっていた。"

    "子供の頃の話だし仕方ないと割り切っていたし、覚えていてあの態度ならそれはそれでどうなのだろうと思っていた。"

    "凛火がどんなに何をしても、許してしまうのが海晴なのだけれど。"

    "そして何より、実は海晴だって最初は凛火のことに気づかなかったのだ。"








    stop music fadeout 1
    scene bg schoolrooftop noon with wfade_long
    play music audio.memories
    pause 1

    "高校１年生の時。"

    "成績優秀で容姿端麗なのを自覚していて鼻につく――当人たち以外には理解し難い理由で中等部の頃から避けられていて、真央しか友達がいなかった海晴は一人になる時が多かった。"

    "高校生活が始まってすぐ、真央が用事でいない日。海晴は一人で屋上にいた。"

    show mhr uni nor ser at std_cr with std_in

    "すでに海晴の手首に傷痕はあった。"

    "けれど一人だったから、海晴は袖で手首を隠すことを忘れていた。"

    show rnk uni nor que rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「痛くないの？」"

    "学校が始まったばかりで、声をかけてきた相手の名前を海晴はまだ覚えていなかった。"

    "最初は身長も小さいので中等部かと思ったが、制服を見るに同じ高等部の１年生だと分かった。"

    "いきなり声をかけてきた同級生の無神経な質問に、海晴は答えなかった。その時は、手首の傷を見られた焦りもあった。"

    "時折、それは噂になっていたから。"

    show rnk uni arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ま、いいけどさ。ここ、開放されてたんだね。私も、ちょっと風を浴びたかったから」"

    "そう言うとこの無神経な同級生は、海晴の隣に座った。"

    "海晴は意地でも喋らないと腹を決め、遠くを見ることにした。"

    "何分経っても、その同級生は話しかけてこなかった。"

    "根負けした海晴は、隣の少女の横顔を見た。"

    "自分と同じようにぼーっとして、どこか遠くを見ていた。"

    "その瞬間、海晴の記憶は一本の線に繋がった。"

    "間違いないと確信してからも、海晴から声をかけることができなかった。"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、予鈴だね」"

    "無神経な同級生――はそう言うと、一人で立ち上がった。"

    "海晴は自分でも予想外の緊張に胸が張り裂けそうになりながら、何も言うことができずにいた。"

    show rnk uni nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「じゃ――またね」"

    "たったこれだけのことで、海晴は救われた。"

    "その同級生の名前が獅子舞凛火だと知ったのは午後のことで、クラスの違う二人と真央が一緒にお昼を食べたり下校したりする友達になったのは翌日のことだった。"



    scene black with wfade_long
    pause 2

    "未だ、告白の返事はない。"

    "――海晴はそれでも、凛火の背中を笑って見ることができていた。"








    python:
        set_info_scene("159")
        set_info_time("evening")
        set_info_location("14")

    stop music fadeout 2
    scene bg schoolgate noon with fade_longest
    pause 1

    $ show_hud()


    "一日の授業を終えて、私は帰宅することにした。"

    "海晴はバイトがあるので急いで帰っていて、直未は用事があるとのこと。"

    "真央はまあ、一緒に来るときは向こうから声をかけてくるので放っておいた。"

    "帰ろうとしたところで、後ろの方からたったったという足音が聞こえた。"


    play music audio.nichijo02

    show mao uni sel glo rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「りーたんっ」"

    "どうやら真央が私のことを追いかけてきたらしい。"

    show rnk sun nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……どうしたの？」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんさ、みはるんにまだ返事してないでしょ～」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ま、りーたんらしいですな。ちゃんと考えてるってことだもんねぇ」"

    show mao uni nor nor rev with std_change

    voice get_voice_filename("mao")
    mao "「きっと色んなこと考えてるでしょ。みはるんの告白のことだけじゃなくて――色んなこと」"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんの今一番考えないといけないこと、やらなくちゃいけないこと。それが終わるまで、答えは出せないってことだもんねぇ」"

    show mao uni nor lau rev with std_change

    voice get_voice_filename("mao")
    mao "「おっけー。だから返事はもうしばらく時間かかりますーってみはるんにそれとなく伝えておくね」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「真央……」"

    "こういうことを言われると、真央は本当は≪女神の選定≫について知っているのではないかと思ってしまう。"

    "でも、それは違うのだとも分かっている。"

    "真央は大雑把に見えて、実は細かいところをよく見ている。私たちの所作や仕草の変化について、私たち以上に詳しいかもしれない。"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「だいじょーぶ。真央様に任せなさいっ！」"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「だから、時間がかかっても答えはちゃんと決めること。どっちに転んでも、うちらは変わんないからさ！　いや、付き合った場合は……って、あれ、これ２回目だねぇ」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「あ、ついでに言っておくと、なおりんも勘づいてるっぽいよ」"

    show rnk sun sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「……まじ？」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「大マジ。ま、だからどうってことでもないんだけどねぇ。んじゃ。まった明日～」"

    hide mao with std_out

    "そう言うと真央は、早足で私を追い抜いていった。"

    "気の遣い方が、とても真央らしい。だから私は安心していた。じっくり考えて、答えられるときに返事をして大丈夫なんだって。"

    "だって私にとってもっとも大きな問題は海晴と付き合うことになってもならなくても――どうやったら二人が生き残れるか、ということなのだから。"







    $ set_info_location("05")

    stop music fadeout 1
    scene bg myroom morning with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "家に帰ってきた私は自室に行き、汚れてもいい部屋着に着替えた。"

    "今日はお店を休みにして、おばあちゃんから頼まれたことをやる日に決めていた。"

    "――おばあちゃんの部屋の掃除だ。"

    "スケール・ジョーンズがおばあちゃんに手を出さなければ今週戻ってくる予定だったのだが、変わってしまった。"

    "次はいつ戻ってこられるチャンスが訪れるか分からないので、掃除を頼まれたのだ。"

    "むしろ、今日まで掃除をしていないことを注意されてしまった。私としては、勝手に物をいじってはいけないと思っていたからなのであるが。"

    "これからは定期的に掃除をすることになり、今日がその第１回目だ。"

    "そしてもう一つ、おばあちゃんの部屋に入ってやるべきことがあった。"









    $ set_info_location("09")



    stop music fadeout 2
    scene bg maidcafe with fade_longest
    play music audio.maidcafe
    pause 1

    $ show_hud()

    show mhr mai sco wic rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「お帰りなさいま……行ってらっしゃいませ」"

    "バイト中の海晴は来客に対しいつも通りの接客をしようとしたはいいものの、客の顔を見てかける言葉を切り替えた。"

    "長身で細身の男性、Ⅲの床に立つフェデリーコだったのだ。"

    "彼が来るということは間違いなく、自分に用があるということだ。"

    "海晴はとりあえず彼を席へ案内してから、水を持っていく。"

    "他のスタッフに任せるのも心配なので、結局自分で行くことに決めたのだった。"

    show fed sta nor nor at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「相変わらずあんたは美人だ。今日の仕事は何時までだ？」"

    show mhr mai sco vig rev with std_change

    voice get_voice_filename("mhr")
    miharu "「店長に言って、出入り禁止にしてもらおうか？」"

    show fed sta dar phi with std_change

    voice get_voice_filename("fed")
    federico "「そいつは困る。事情があってな、あの店はもう出入り禁止になっちまったんだ。あんたと話をしたくて、ここまで来たんだ。そう邪険にするなよ」"

    "あの店――≪MILK CROWN≫のことだとすぐに分かった。原因は分からないし、海晴はどうせ泥酔が原因に決まっていると思っていた。"

    "それよりも、海晴は彼に対し何か違和感のようなものを感じていた。"

    "妙に、落ち着いている――これまでとは、まとっている雰囲気が異なっていたのだ。"

    show fed sta dar ser with std_change

    voice get_voice_filename("fed")
    federico "「どうした？」"

    show mhr mai sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「何でもないよ。そうだな……あと１時間ほど待っていてくれないかい？　そうすれば休憩に入るから、ぼくがここに来よう」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「……ああ。そうだな、とりあえずワインリストをもらえるか？」"

    show mhr mai sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「残念ながらそんなものはこの店にはないよ。あるのは偽物の愛情がこもった不味いコーヒーだけさ」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「んじゃあ、そいつを一つ」"

    "フェデリーコは静かに言うと、一冊の本を取り出した。"

    "彼に――絵面としてはすごく似合っているが中身を知っていると、という意味で――似合わない有名な画家の展覧会の図録であった。"

    "海晴はその画家の絵を、オデット・マランソンと観に行ったことを思い出していた。"









    $ set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "１時間ほど経過して、私は一旦自室へ戻ってきていた。"

    "およそ２ヵ月分の汚れは、結構なものになる。掃除機と雑巾がけ、本棚の埃を払って小物の埃を拭いて……と、かなりの大仕事だ。"

    "おばあちゃんの部屋は整理整頓こそされているが物が多いので、定期的に掃除しないとなるほど、これは厄介だ。"

    "そんなこんなで、半分ほど片付いたところで休憩しに戻ってきたのだ。"

    show rnk jer nor apo at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「おばあちゃん……」"

    "私は思わず、そう呟いていた。"

    "掃除することは、別に構わない。"

    "ただ本来であればそろそろここでおばあちゃんと会えると思っていただけに、残念な気持ちになった。"

    "正直に言って、スケールさんに対する怒りや憎しみも、ゼロとは言えない。けれどそれらはほんの僅かなもので、実際はおばあちゃんが戻ってこない寂しさの方が大きかった。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「よし、続きだ」"

    "私はスポーツドリンクを半分まで飲み干して、作業を再開することにした。"









    $ set_info_location("18")

    stop music fadeout 2
    scene bg lion02 noon with fade_longest
    play music audio.alan
    pause 1

    $ show_hud()

    "アラン・スコーピオンは、喫茶ライオン館の前に立っていた。"

    "本日臨時休業の貼り紙を見て、ため息をついた。"

    show aln ban nor nor at std_c with std_in

    voice get_voice_filename("aln")
    alan "「……そうか」"

    "この店の常連にとっては見慣れた貼り紙ではあるのだが、アランは運が悪かったと諦めていた。"

    "彼は、獅子舞凛火とあらためて話がしたかった。"

    "スマホの番号は控えてはいるが、電話越しではなく、彼女の瞳を見ながら話がしたかったのだ。"

    show aln ban nor gen with std_change

    voice get_voice_filename("aln")
    alan "「……仕方ない、か」"

    "アランは心の中でそう呟くと踵を返し、空腹を満たすため手頃な飲食店を探し始めた。"











    $ set_info_location("09")


    stop music fadeout 2
    scene bg maidcafe with fade_longest
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    show mhr sun nor nor rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「待たせたね」"

    "海晴がフェデリーコの席へ来る頃、彼はとっくにコーヒーを飲み干していた。"

    "図録を閉じると、フェデリーコはすぐに本題へ入った。"

    show fed sta dar ser at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「アラン・スコーピオンの≪死因≫を教えてくれ」"

    "軽口の彼がいきなり本題に入ったことに、海晴は驚いた顔を浮かべていた。"

    "彼はそのことに気がつきながらも、そのまま話を続けた。"

    show fed sta dar phi with std_change

    voice get_voice_filename("fed")
    federico "「スケールと組んでいたとき、ユウを脱落させたら教えてもらうって約束をしていたはずだろう」"

    show fed sta dar ser with std_change

    voice get_voice_filename("fed")
    federico "「オデットが独自で動いたことやスケールがあんたを指名したことでなあなあになっていたが、オレにはその情報を知る権利があるはずだ」"

    "落ち着いた物言いに、海晴は驚かされていた。"

    "彼の印象と言えば、もっと軽くて迂闊で、残忍になりきれないというものだ。"

    "直近の選定でも、海晴はその印象のままだった。"

    "だが現実世界で久々にあったフェデリーコは、最初こそ元のイメージ通りとはいえ、着席してからはもはや別人のようだった。"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「なるほど――それも一理ある、か」"

    "海晴は少し考えてから、そう答えた。"

    "全く無視をするという手もあるのだが、彼は海晴に敵意を向けていたわけではない。"

    "それに、今の彼となら話す気分にもなったのだ。"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「問題は２つある。ただし、どうやらここで話す話題ではないようだ。君が出禁になってしまったあの店、どうにかして交渉できないかい？」"

    show fed sta dar irr with std_change

    voice get_voice_filename("fed")
    federico "「ちっ……しかし、それもそうか。分かった、何とかする」"

    "内容が内容なのだ、ここで話すのは相応しくないどころではない。"

    "彼ならどうにかするだろう、という確信が海晴にはあった。一方で彼に対してそんなことを思うのに、不思議な気持ちももっていた。"

    "今度は３時間後に落ち合う約束をしてから、フェデリーコは会計を済ませていった。"









    python:
        set_info_scene("160")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    show rnk paj nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……ふう」"

    "結局、おばあちゃんの部屋の掃除は夜までかかってしまった。"

    "しかしどうにか一日で終わらせることができたし、かなり綺麗になったので満足だ。"

    "あとは土日の昼に窓の掃除をすれば、完璧だ。"

    "汗もかいたので私はシャワーを浴びて、さっぱりしたところだった。"

    "このまま一息ついて寝たいところだが、私にはもう一つやらなくてはならないことがあった。"

    "私は深呼吸してから、その本へと向き合った。"

    show rnk paj nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「本当に、同じだ」"

    scene ecg lindadiary clo with dissolve_long

    "私は机の上に、カードブックとほとんど同じ見た目の本を置く。"

    "大きな違いはこちらの本がとても年季が入っていて、雑に扱えばすぐにばらばらになってしまいそうなほどボロボロということだ。"

    "色や装飾の形は、まったく同じと言ってもいい。あえてそれらに違いをあげるなら、カードブックとは異なり、手作りのような歪つさがあることだ。"

    "先日田舎へ行った時、たまたま私の持っているカードブックを見たおばあちゃんが、「あ！」と声をあげたのだ。"

    "これを≪女神の選定≫で使用するカードブックだと認識する前、私はおばあちゃんにこれを写真で撮って送っていた。"

    "その時に似たものが部屋にあるかもと言っていて、深くは気にしていなかったのだが、今度は違った。"

    "カードブックの実物を見たおばあちゃんは、自分の部屋にこれとまったく同じ装丁の本があることを思い出したのだ。"

    "私の方も、それを聞き逃すわけにはいかなかった。"

    "掃除のついでにその本を見てもいいと許可をもらったので、私はその本を探すことにした。"

    "探すといってもおばあちゃんがちゃんと場所を覚えていたので、私がやったのは本棚の一番下にある古い箱を丁寧に開けることだけ。"


    scene bg myroom night
    show rnk paj nor que at std_c
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「おばあちゃんの、おばあちゃんの物……」"

    "だと、おばあちゃんは言っていた。"

    "祖母の祖母、100年以上昔からある可能性もある。この本の危うさを見れば、それも納得だ。"

    "歴史だけでも、とても貴重なものだ。"

    "私は意を決して、その本を開いた。"

    scene ecg lindadiary op1 with dissolve_long

    "中の文章は全て英語で書かれていた。話を聞いたときに知ったが、どうやらおばあちゃんのおばあちゃんはイギリス人であり、実はおばあちゃんはクォーターだったのだ。"

    "16年間聞かされてこなかった事実に、私は驚きを通り越して呆れていた。"

    "おばあちゃんにどうして教えてくれなかったのかと聞いたら、「聞かれなかったから」と答えた。"

    "となると私は16分の１だけイギリス人の血が入っているわけだが、どうやらこの黒髪に混ざっている金髪がその名残のようだ。"

    "それはそれとして、おばあちゃんは英語がからっきしなのでこの本を読む気にならなかったらしい。"

    "とはいえおばあちゃんのおばあちゃんの思い出の品であり捨てるわけにもいかず、装丁も綺麗だったので、ずっと大切に保管していたそうだ。"


    voice get_voice_filename("rnk")
    rinka "「これ、日記だ」"

    "１ページ目はすっかり茶色に焼けた遊び紙で。２ページ目からが本文だ。"

    "それは手書きで書かれていて、インクはところどころ滲んでいた。"

    "英語の筆跡は分からないが、何となく、女性が書いた文字の気がした。"

    "となると、これはおばあちゃんのおばあちゃんの日記、ということだろうか。"

    "私はカードブックを傍らに置いて、日記を読むことにした。"

    "カードブックが一定範囲の中にあれば、私たち選定の参加者は言語の壁を超えることができる。"


    scene bg myroom night
    show rnk paj nor que at std_c
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「でも文字がかすれてるせいなのか……、あんまり頭に入ってこないな」"

    "２ページ読むのに、30分くらいかかってしまった。"

    "印刷された活字とは違うらしく、日本語で不明瞭な印刷物を読むのに感覚は似ている。"

    "途切れ途切れになって、ちゃんと文章が頭に入ってこないのだ。"

    "内容はいわゆる普通の日記で、今日は何を食べた、誰と話した、そんな他愛のないことが書かれている。"

    "もっとも私の予想は正しく、1910年頃と100年以上前の日記のため、今と違う文化を読むのはそれはそれで面白い。"

    "しかし、これは全部読むのにかなりの時間がかかりそうだ。そもそもただの日記ならば、≪女神の選定≫とは何も関係ないだろう。"

    "ぱらぱらめくってみて得られる情報がなさそうなら、この年代に似たような日記が売られていなかったかを確かめる方が有用かもしれない。"

    show rnk paj arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「まだ判断するには早い……かな」"

    "とりあえず、今日はあと１ページだけ読んで寝ようと決めた。明日もう数ページ読んでみてから、この日記をどれくらい読むか判断しようと思う。"

    "そんな風に思っていきなり、興味深いことが書かれていた。"

    "――『そうそう、この日記帳は妹のダイアナが、私の誕生日プレゼントに手作りしてくれた日記帳なんだ』"

    "手作りの日記帳。この本の装飾に感じた歪さは正しかったということだ。てっきり、古いから装丁が雑なのかと思い込んでいた。"

    "こうなると、カードブックとの関係性が気になる。"

    "この日記帳は世界で一冊のもののはずだ。当時はインターネットもないから、作り方が公開されていてみんな真似した、というものでもないだろう。"

    "私は10分前の自分の考えをすぐに否定することになった。"

    show rnk paj arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「この日記には何か――ある」"

    "私はそう直感していた。"

    "ここまで謎が与えられれば、誰だってそう思うに違いない。"

    "今日は勉強をしようと思っていたけれど、そういうわけにはいかなそうだ。"

    "私は長丁場になると予感し、集中して本を読むために１階へ移動することにした。"









    $ set_info_location("34")


    stop music fadeout 2
    scene bg bar with fade_longest
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "海晴は、およそ２週間ぶりにバー≪MILK CROWN≫を訪れていた。"

    "高校生がバーに行きつけているのもおかしな話ではあるが、海晴はもうすっかりこの店に慣れていた。"

    show fed sta nor smi at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「どうにかなったぜ？」"

    "フェデリーコはすでに店にいて、酒を注文していた。"

    "薄くて綺麗なグラスには、透き通った琥珀色の液体が店内の光を乱反射させていた。"

    show fed sta nor ela with std_change

    voice get_voice_filename("fed")
    federico "「店で一番高いウイスキーだ。こいつを入れるって約束で、出禁を解除してもらったんだ。さすがにうまい。あんたも飲むか？　この酒なら、マスターだって見逃すぜ？」"

    show mhr sun sco cau rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「はぁ。だからぼくはお酒を飲まないよ。君にとっては残念かもしれないけれど、またミルクをもらってもいいかい？」"

    "フェデリーコは残念そうな顔を浮かべて、結局店のマスターとそのウイスキーで乾杯していた。"

    "一度は出禁にした客ではあるが、マスターの顔はそんなことを気にも留めていなかったので、現金な人だと海晴は呆れていた。"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「さて、ここからはオレたちの時間だ」"

    show mhr sun pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「誤解を招くような言い方はやめてくれ。じんましんが出そうだよ」"

    "そういえば、お酒を飲んでいる時のフェデリーコは、海晴の知っている彼と同じだった。"

    "そのことに、奇妙な安心感を覚えていた。"

    show fed sta dar ser with std_change

    voice get_voice_filename("fed")
    federico "「ちっ……まあいい。アランの≪死因≫を教えるにあたって２つ問題があると言っていたな。まずそれを教えてくれ」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……ああ。１つ目は、ぼくはアラン・スコーピオンの≪死因≫をカードに書かれている情報でしか知らないということだ」"

    "つまり、裏付けになる情報までは知らない、と海晴は補足を加えた。"

    "その情報を教えるだけでは、フェデリーコにはカードが生成されないという意味だ。"

    show fed sta dar phi with std_change

    voice get_voice_filename("fed")
    federico "「構わねぇ。先に言っちまうが、オレはこれからインドに行く予定だ。何としてもあいつの情報を集めたいんだ」"

    show fed sta dar ser with std_change

    voice get_voice_filename("fed")
    federico "「スケールから聞いた情報はあくまで、紙の上の情報だ。奴の家族にも会ってみて、≪死因≫と≪未練≫の詳細を探す」"

    show fed sta dar smi with std_change

    voice get_voice_filename("fed")
    federico "「カードの情報だけでも知ってれば、大分楽になるからな」"

    show mhr sun sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「正気かい？」"

    show fed sta dar ser with std_change

    voice get_voice_filename("fed")
    federico "「ああ。あのゴリラ女なら、手詰まりになれば迷わずそれくらいはやってのけるだろうからな。もっとも、第一にあいつがそこまで手詰まりになる状況が想像つかないけどな」"

    "そして彼は、海晴に２つ目の問題を話すように促した。"

    "海晴が話し始める前に彼は一度グラスを空にして、同じものをもう一つもらっていた。"

    show mhr sun sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君が情報を集めなくても、アラン・スコーピオンは脱落する。恐らく彼は――凛火に敗北するつもりだ」"

    "日曜日の時点で、海晴は凛火からスケール・ジョーンズが凛火の祖母に手を出したこと、その状況からアランが祖母を救ったことを聞いていた。"

    "海晴はこれまでのアランの話と合わせて、彼が凛火に執着しているのを知っている。"

    "同時に、彼の行動が≪女神の選定≫の勝者になるための行動とは思えないことも。"

    show fed sta nor ela with std_change

    voice get_voice_filename("fed")
    federico "「なるほど。だが、それは問題にならねぇ。何故ならオレの目的は、あのスカした野郎をオレの手で脱落させることだからだ」"

    show mhr sun sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「意地、というわけかい？　ぼくはアラン・スコーピオンを無視して、凛火やぼくを狙った方がいいと思うよ」"

    show fed sta dar smi with std_change

    voice get_voice_filename("fed")
    federico "「かかっ、悪いな。あんたの体に興味はあるが、あんたらにもう興味はねーんだ」"

    "海晴は、高笑いしながらはっきりと言ってのけた彼に、一人の女性の影を見ていた。"

    "そして海晴は、夕方にフェデリーコへ感じていた違和感の正体を知った。"

    show mhr sun sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「どちらにせよ。君にアランの≪死因≫を教えてもぼくたちにデメリットはないだろう。それに、約束を破るのは気が引けるからね」"

    show mhr sun nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「彼の≪死因≫は≪毒死≫さ。詳細は分からないが、有名若社長のアラン・スコーピオンなら想像もつく。君がこの情報をカード化するのは、そう遠くない未来だろう」"

    python:
        add_character_cards("mhr", ["12_death"])
        add_character_cards("aln", ["12_death"])

    show fed sta nor ser with std_change

    voice get_voice_filename("fed")
    federico "「……ありがとよ。さて、オレは明日の朝一の便でインドへ向かう。それまで世間話に付き合ってくれよ」"

    show mhr sun pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「断る。高校生をなんだと思っているんだい？」"

    "海晴は一呼吸置いてから、続ける。"

    show mhr sun pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「しかし、今日は喉が渇いていてね。もう一杯ミルクを飲む間くらいは、君の話に付き合おう」"

    "何故こんなことを言ったのか、海晴はその理由をはっきりと分かっていた。"

    "予感がしたからだ。"

    "フェデリーコ・カルミナーティと会うのは、これがきっと最後だと――。"


    scene black with dissolve

    "この日は帰ってからシャワーも浴びずに寝てしまい、海晴がフェデリーコの≪未練≫のカードを取得したのは、１日後。"

    $ add_character_cards("mhr", ["3_regret2"])

    "火曜日の夜、浴槽で昨夜のことを振り返っていた時のことだった。"










    $ set_info_location("04")



    stop music fadeout 2
    scene bg lion01 night with fade_longest
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "全体の６分の１ほど読んだところで、私は眠気の限界を感じた。"

    "元々本を読むのは遅い方だし、古い本のため文字が読みにくいこともあり、さらに倍近く時間がかかってしまったのだ。"

    show rnk paj nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「――日記、だね」"

    "それが、ここまで読んでみての感想だった。今のところはまだ普通の日記の域を出ない。"

    "人の生活を覗き見しているようで、罪悪感と恥ずかしさの両方があった。"

    "おばあちゃんのおばあちゃんの名前は、リンダというらしい。リンという響きが入っていることに、少しだけ親近感が湧く。"

    "リンダさんのお父さんは、イギリス出身の時計技師だそうだ。"

    "リンダさんが生まれる前に、彼女の両親は日本へ移住してきた。"

    "なんでも、時計の技術指導のため日本に招かれた際にこの国を気に入り、その企業から正式に技術顧問としての依頼をされたことをきっかけに、奥さんと一緒に日本へ住むことを決めたらしい。"

    "日本に来てすぐに、リンダさんが生まれ、その１年後には妹のダイアナさんが生まれたそうだ。"

    "おばあちゃんのおばあちゃんの妹、となるともはやおばあちゃんもよく覚えてはいないだろう。"

    "カードブックに対していい印象がなかったのであまり気にすることはなかったけれど、改めて見るとこの本の装丁は素敵だ。"

    "こんな素敵な手作りの日記帳をプレゼントするくらいだから、ダイアナさんはいい妹さんなのだろう。"

    "リンダさんの日記を見ても、とても仲が良い姉妹だとうかがえる。"

    "私は兄弟姉妹がいないので、少し羨ましくもなった。"

    "海晴も直未も一人っ子で、私の周りだと兄弟がいるのは弟のいる真央くらいか。"

    "さて、と。"

    "私は時計に目を遣ってから、日記を閉じた。勢いよく閉じると壊れてしまいそうなので、丁寧に。"

    show rnk paj nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「これは、今週いっぱいかかりそうだな」"

    "続きは明日読むことにして、私は自分の部屋へと戻ることに決めた。"

    $ add_seen_chapter("10-1")










    python:
        set_info_scene("161")
        set_info_date(7, 3, "tue")
        set_info_time("emorning")
        set_info_location("03")

    stop music fadeout 2
    scene bg train normal with fade_longest
    play music audio.badguys
    pause 1

    $ show_hud()

    show fed sta dar phi at std_c with std_in

    voice get_voice_filename("fed")
    federico "「ちっ、柄にもなく清々しい気分だ。あれだけ飲んだくせに二日酔いもありゃしねぇ」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「しかし、ミハルは本当に１杯で帰りやがったな。あいつを好きになる男がオレ以外に現れたら、さぞかし苦労するんだろうなァ」"

    "ほとんど客のいない車内で、彼はそんな風に悪態づいていた。"

    "空港に向かうため。電車に乗っていたのだ。"

    "晴れた空に想いを馳せながら、フェデリーコは自分の人生を思い出していた。"

    "イタリア南部で生まれた一人の男の人生は、敗北にまみれたものだった。"

    "子供の頃、彼はいじめられていた。"

    "今と同じように体が細く、今と違って背の低かった彼は抵抗することもできなかった。"

    "殴り返そうとすれば殴られたし、言い返そうとすれば数の暴力に負けた。"

    "彼は子供ながらに、いじめに敗北したという実感を与えられた。"

    "ほとんど同じ頃、元々不仲だった両親は離婚を決めた。"

    "フェデリーコは、母親について行きたかった。"

    "深い理由はない。ただ幼い彼は母親の方が好きだっただけだ。"

    "しかし、彼はここでも敗北した。"

    "離婚の決め手は母親の不貞であり、正確にはフェデリーコ自身に原因があるわけではなかったが、彼にとってそれは敗北の記憶として定着した。"

    "母親は相手の男と同棲し、再婚することに決めていた。"

    "婚約指輪はフェデリーコに託したのではなく、ゴミ箱からこぼれ落ちていたものを拾ったものだった。"

    "いつか再会したいという≪未練≫から、その婚約指輪を肌身離さず持ち歩くことになった。"

    "それは母親の愛を勝ち取れなかったという敗北の象徴であることを、フェデリーコ自身理解するのに20年以上の時間がかかったのだが。"

    show fed sta dar smi with std_change

    voice get_voice_filename("fed")
    federico "「大切な指輪かと思っていたが、捨てちまってみると、大して感傷も湧かないぜ」"

    show fed sta dar dar with std_change

    voice get_voice_filename("fed")
    federico "「かーちゃんがゴミ箱に捨てたときも、こんな気持ちだったのかもしれないな。一人の相手に一途になれない気持ち、今ならよーく分かるけどよ」"

    "ちなみに初めてのガールフレンドは、高校に上がる頃にできた。"

    "はっきりとものを言う女子であり、彼をぐいぐい引っ張っていく性格でうまくいっているように見えたが、転校によって自然消滅してしまった。"

    "この一件を敗北と数えるかはさておき、高校に上がるといじめこそなくなったが、彼の敗北はさらに増えた。"

    "クラブでやっていたサッカーでは、どんなに努力しても必ず自分よりも上の人間がいて、彼らには敗北するほかなかった。"

    "机を並べて行う勉強では、たまに頑張って勉強してみても、１位をとることはできず、敗北するほかなかった。"

    "幼い頃の経験から敗北が染みついてしまったフェデリーコは、自覚のないまま本気になれない子供になっていた。"

    "彼の敗北は、無自覚のまま負の連鎖を続けていた。"

    "フェデリーコは大学に行くことをしなかった。この頃、大学受験で敗北することを恐れていたのだが、フェデリーコは自分でそれを認めなかった。"

    "代わりに、彼はビジネスを始めた。"

    "同じ時期にフェデリーコの父親が死に、それなりの金額の遺産が入ってきたから、それが元手だった。"

    "現金があれば誰にでもできる簡単なビジネスだ。"

    "社会的に行き詰まった人に金を貸し、高額な金利を乗せて回収するだけ。"

    "警察に泣きつくことのできない多重債務者や犯罪者、誰からも相手にされないクズが彼のビジネスパートナー。"

    "自分よりも敗北し続けた相手を、客に選んだのだ。"

    "返済しない相手は他のヤミ金から借金をさせるか、金目のものを回収すること、あるいは腹いせに暴力を振るうことで解決した。"

    "フェデリーコのビジネスは利益という点である程度の成功をしていたが、金で解決できない大きな問題にぶち当たった。"

    "マフィアのシマで、このビジネスを成功させてしまったのだ。"

    "フェデリーコは、マフィアに目をつけられることになる。"

    "こうなると、朝食のトーストにバターを塗るくらいの手軽さで、彼は命を狙われることになるのだ。"

    show fed sta dar smi with std_change

    voice get_voice_filename("fed")
    federico "「かかっ、今思えばあのゴリラ女の方がよっぽど恐ろしかったぜ……物理的にな」"

    "フェデリーコは自分で立ち上げた最初の≪ビジネス≫も結果的に敗北で終えることとなる。"

    "彼が助かる方法は１つだった。"

    "ビジネスで得た利益をマフィアの幹部へと献上し、自らもマフィアの一員となることだった。"

    "彼は下っ端ではあったがそれなりに優秀で、多額の利益を組織へともたらした。"

    "金融だけでなく地上げ屋のような仕事も受け、社会的地位と引き換えに金を得るようになる。"

    "だが一方でフェデリーコは、自分の稼いだ金が高い割合で上へと持っていかれていることに嫌気が差した。"

    "彼は組織の金を持ち逃げし、スイスの銀行へと移した。"

    "そしてある海運業者に目をつけた。取引のあった海運業者だ。"

    "もっとも、マトモな海運業者のはずがない。武器や表では売れない盗品なども取引する、違法な業者。"

    "無国籍船とうたってはいるが、実態はフランス人の女性が指揮をとる独立傭兵集団のような連中だった。"

    show fed sta dar ser with std_change

    voice get_voice_filename("fed")
    federico "「今思えば、オレみたいのをよく乗せてくれたもんだ」"

    "その船長をやっていたフランス人の女性――オデット・マランソンに事情を話し、彼は海外逃亡を決意したのだった。"

    "マフィアの実態は家族経営の企業。血の繋がっていないフェデリーコはどんなに頑張ってもトップにはなれないだろう。"

    "しかし、それでも構成員には血の誓いと掟がある。辞めても待っているのは監獄で、そもそも生きたままマフィアを辞めることは不可能なのだ。"

    "フェデリーコは再び敗北者になることを恐れ、逃げた。"

    "そして、船旅の途中、海賊の襲撃に遭いオデットともども死亡する――というのが彼の運命。"

    show fed sta dar phi with std_change

    voice get_voice_filename("fed")
    federico "「死んでからも負けてばっかじゃ、ざまあねえな」"

    hide fed with std_out

    "こうして過去を思い出した彼は、乗換の駅につくまで眠ることにした。"

    "日曜日の朝、日本へ戻るまでの間に、アランの情報を見つけると強い決意を胸に秘めて。"

    "彼は、自分自身で気付いていなかった。"

    "敗北者の人生であると同時に――彼は決して挫けず、心の奥底まで他人に取り込まれることなく、常により大きなものへと抗い続けてきたことに。"

    "フェデリーコ・カルミナーティは、真正の敗北者ではないことに。"








    python:
        set_info_scene("162")
        set_info_time("night")
        set_info_location("04")

    stop music fadeout 2
    scene bg lion01 night with fade_longest
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "今日の放課後は、ちゃんとお店を開けていた。"

    "おばあちゃんの部屋の片付けも終えていたので、清々しい気分だ。"

    "閉店後、一通りの片付けも終えてから、私は再び日記帳を１階へ持ってきた。"

    "テーブルの上に日記帳を置き、慎重な手つきで開く。"

    "リンダさんとダイアナさんの日常に、私はさらに潜っていくのだった。"









    $ set_info_location("23")

    stop music fadeout 2
    scene bg hotel japan with fade_longest
    play music audio.alan
    pause 1

    $ show_hud()

    "この日、アランはホテルに宿泊をしていた。"

    "アランは横浜の倉庫で寝泊まりするときと、このようにホテルで過ごす日を不定期で切り替えていた。"

    "彼にとって、居心地の良さは問題ではない。"

    "スマートフォンやパソコンの充電をする場所が必要だったのだ。"

    "それでも柔らかいベッドで眠る日は、彼のひと時の安らぎに変わりはなかった。"

    show aln ban nor gen at std_c with std_in

    voice get_voice_filename("aln")
    alan "「……今日は行かなかった、な」"

    "昨日は獅子舞凛火に会う決心をしたはいいものの、運悪く店が閉まっていた。"

    "しかし、アランはどうもこの日に向かう気にはなれなかった。"

    "タイミングを逃すと、うまくいかないこともある。"

    "普段のアランならばまったく気にすることはないのだが、今や獅子舞凛火のこととなると彼は冷静さを欠くようになっていた。"

    show aln sta nor clo with std_change

    voice get_voice_filename("aln")
    alan "「恐らく、今度が最後の――」"

    "ベッドに寝転んで言いかけて、彼は自分が最初に脱落させた相手のことを思い出していた。"










    scene bg warehouse with wfade_long
    pause 1

    show cha sta nor smi rev at std_cl with std_in

    voice get_voice_filename("cha")
    chan "「ようやく会えたわね！」"

    "≪因果の刻≫――５月３日から３日が経過した日曜日。"

    "アランは一人の女性に呼び出されていた。"

    "アランは夢の中で女神から≪女神の選定≫のことを聞いてはいたが、１度目の選定――つまり他の参加者との邂逅が終わってから日本へ向かおうと思っていた。"

    "そんな彼が日本に行く予定を早めたのが、目の前に立つ女性、チャン・チャンの呼び出しだった。"

    "宝石会社の社長である彼は、知らない相手からのアポの連絡も多い。"

    "普段なら無視するところだが、彼は電話越しの≪女神の選定≫という言葉に反応せずにはいられなかった。"

    "まだ半信半疑だった彼だが、この時少なくとも自分と似た状況の者はいると知ったのだ。"

    show cha sta nor nor rev with std_change

    voice get_voice_filename("cha")
    chan "「来てくれて嬉しいわ。ミスター・アラン」"

    "チャンはアランと数メートル離れて立ち、自信に溢れた声で言う。"

    "いかにも旅行者風の彼女は、動きやすそうな服装だった。身だしなみも整えていて、ごく普通の20代前半の女性……彼は彼女にそんな印象を持っていた。"

    show aln sta nor nor at std_cr with std_in

    voice get_voice_filename("aln")
    alan "「何故僕のことを知っている？　いや、僕が選定の参加者であることを知っている？」"

    show cha sta nor que rev with std_change

    voice get_voice_filename("cha")
    chan "「貴方の名前が有名なことくらい、自分で分かっているんじゃないの？」"

    show cha sta nor smi rev with std_change

    voice get_voice_filename("cha")
    chan "「２つ目の質問には……そうね！　答えてあげるわ！　あたしの初期カードのうち１枚が、あんたの≪氏名≫。あんたみたいな変な名前、そう多くはいないものね」"

    show cha sta nor que rev with std_change

    voice get_voice_filename("cha")
    chan "「でもね、あんたのことは昔から知っていたのよ。ウィリアム・リュウという男を知っているかしら？」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「……知らないな」"

    show cha sta nor nor rev with std_change

    voice get_voice_filename("cha")
    chan "「そうだと思ったわ！」"

    show cha sta nor gla rev with std_change

    voice get_voice_filename("cha")
    chan "「ウィリアム――ビルは貴方の会社とも取引がある広告会社の営業担当よ」"

    show cha sta nor gla rev with std_change

    voice get_voice_filename("cha")
    chan "「貴方とも会ったことがあると言っていたけれど……どうやら社長様は取るに足らない下請け業者のことなんて覚えていないようね」"

    "アランはこの時点で、厄介さよりも面倒臭さを感じていた。"

    "この手の女性は苦手だった。どんどん関係ない方に話題が移っていき、一向に話が進まない。"

    "もし彼女が営業であれば、この時点でアランは席を立っていただろう。"

    show cha sta nor nor rev with std_change

    voice get_voice_filename("cha")
    chan "「あたしはそのビルの婚約者よ！」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「……用件を早く話してくれないか？　ミセス・チャン」"

    $ add_character_cards("aln", ["6_name"])

    show cha sta nor ups rev with std_change

    voice get_voice_filename("cha")
    chan "「あれ……あれ？　どうしてあたしの名前をあんたが知ってるのよ？　あたし、名前話してないよね？」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「君はわざわざ僕の会社に電話をしてきただろう？　偽名を使ったようだが、せめて非通知でかけてくるべきだったな」"

    show cha sta nor que rev with std_change

    voice get_voice_filename("cha")
    chan "「……はい？」"

    "アランはそう言うと、１枚のカードを取り出した。"

    "それは、チャンも見たことのある、自分も持っているものと同じデザインのもの。"

    "表面には≪Ⅵ・氏名――チャン・チャン≫と書かれている。この番号の意味をチャンはまだ理解してはいなかったが、自分の名前が書かれていることは一目瞭然だった。"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「新しくカードが生まれる瞬間を、僕はすでに目撃している」"

    show cha sta nor gla rev with std_change

    voice get_voice_filename("cha")
    chan "「ち、ちょっとぉっ！　そんなのずるくない！？　個人情報とかどうなってんのよ！」"

    "慌てるチャンに対して、アランは何も言わない。"

    "真面目に相手をしても自分は得をしないと、彼はすでに分かっていた。"

    show cha sta nor nor rev with std_change

    voice get_voice_filename("cha")
    chan "「で、でも名前でしょっ。あたしなんてありふれた名前だし、どうせすぐにばれちゃうよ」"

    show cha sta nor que rev with std_change

    voice get_voice_filename("cha")
    chan "「そんなことより……」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「チャン・チャン。貴様の≪死因≫は≪転落死≫だな？」"

    show cha sta nor ups rev with std_change

    voice get_voice_filename("cha")
    chan "「えっ……うううう、嘘！　どうしてあんたが知ってんのよ！」"

    "からくりは簡単だった。"

    "アランの初期カードの中に、≪Ⅵ・死因・転落死≫というものがあった。"

    $ add_character_cards("aln", ["6_death"])

    "運命の大広間で顔合わせもしていないので、これだけでは一体誰のカードなのか見当もつかない。"

    "しかし、チャンの≪氏名≫のカードが作られた時、アランはそれぞれの参加者に番号が割り当てられていることに気がついた。"

    "≪自身のカード≫に≪Ⅻ≫という番号が振られている時点で予測はしていたが、確信に変わった。"

    "そして≪Ⅵ≫がチャンだと分かれば、彼女の≪死因≫と結びつく。"

    show cha sta nor que rev with std_change

    voice get_voice_filename("cha")
    chan "「あたしもしかして、大事なこと言っちゃってた？」"

    "いまいち危機感のない目の前の女性に、アランは苛立ちすら感じていた。"

    show aln sta nor clo with std_change

    voice get_voice_filename("aln")
    alan "「……氏名を軽んじているならば、その考えは改めた方がいい。ただし、来世ではな」"

    "アランはすでに無宗教になっているが、思わずその言葉を使っていた。幼い頃、家族からそんな概念があることを聞いたことがあった。"


    play music audio.impatience

    show cha sta nor gla rev with std_change

    voice get_voice_filename("cha")
    chan "「は、はぁ？　なっ、何よ！　あんたはまだあたしの≪未練≫を分かっていないはずっ、それに……」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「婚前旅行というのか、ただの旅行なのか知らないが、貴様はウィリアムと登山を楽しんでいた。登山といえど本格的なものではなく、ほとんどピクニック」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「しかし貴様たちは好奇心に負け、ルートを外れて崖の方へと向かった。そちらの方が景色がいいと思ったようだな」"

    show cha sta nor que rev with std_change

    voice get_voice_filename("cha")
    chan "「え？　え？　あんた、なんで知ってんのよ！　まさか……ストーカー？」"

    show cha sta nor ups rev with std_change

    voice get_voice_filename("cha")
    chan "「やだやだ！　あんた顔は悪くないと思うけど、根暗っぽいから無理！　そもそもあたしはビル一筋なんだから！」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「恐らくこの転落死というのは、その時に足を滑らせたか何かだろうな。わざわざ立ち入り禁止の場所へ行ってその結末というのは……愚かという他はない」"

    show cha sta nor gla rev with std_change

    voice get_voice_filename("cha")
    chan "「うっさいわね！　っていうか、早くなんであたしのことをそんなに知ってるのか教えなさいよ！」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「心当たりがないのか、動転して見失っているのか」"

    "アランはチャンの名前を知った時点で、彼女の情報を調べ上げていた。"

    "≪女神の選定≫というのが実際にあるのか完全には信じることはできていないが、光の中からカードが作られるという現象や、言語の壁を容易く超えるカードブックの存在を認めれば、少なくとも半分は信じなければならなかった。"

    "相手のことを知っておけば、どんな交渉をする際にも有利になる。アランはそう考えていた。"

    "だから、チャンのことは徹底的に調べ上げた。口には出さないが、当然、婚約者のウィリアムのことも。"

    "もっとも先ほどアランが話した情報は、途中まではチャン自身が自分でＳＮＳにアップしていた内容だった。"

    "転落したこと自体は目の前の彼女を見るに≪なかったこと≫になっていると分かるが、これまでの情報から旅行での好奇心が死因に繋がったと推測するのは難しい話ではない。"

    show cha sta nor cal rev with std_change

    voice get_voice_filename("cha")
    chan "「いいわ……もう遊びは終わりにしましょう」"

    "チャンは額の汗を拭ってから、懐から包丁を取り出した。"

    "いわゆる牛刀であり、刃渡りは20センチ程度。彼女が何に使おうとしているか、明白だった。"

    show cha sta nor gla rev with std_change

    voice get_voice_filename("cha")
    chan "「あたしは生き残りたいのよ……ビルとの新婚生活が待っているんだから！」"

    hide cha
    hide aln
    with std_out

    "チャンはその包丁の刃を上に向けて構えると、アランに向かって突進していった。"

    "二人の間の距離は５メートルもないので、女性の足でも一瞬でアランまで辿り着く。"

    "それにチャンは子供の頃からテニスのプレイヤーであり、脚力には自身がある方だった。"

    "彼女は自分の突然の行動に金持ちのボンボンであるアランが対応できるはずがない――とそう思っていた。"

    show aln sta nor ang at std_cr with std_in

    voice get_voice_filename("aln")
    alan "「≪女神の選定≫の参加者は死なないと、女神から聞いていないのか？」"

    "アランは半身で包丁を避け、チャンの手首を捻りつつ包丁を奪い取った。"

    "そしてチャンの腕を片手で極めつつ、包丁の切っ先を首筋に向ける。"

    show cha sta nor que rev at std_cl with std_in

    voice get_voice_filename("cha")
    chan "「え？　あれ？　なんでこんな状況？　ち、ちょっと待とうよ」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「信じていない、というところか。もっともこの点に関しては僕も試していないから、信じてはいない」"

    show cha sta nor ups rev with std_change

    voice get_voice_filename("cha")
    chan "「あ、あたしやばくない？　この状況やばくない？」"

    show cha sta nor dis rev with std_change

    voice get_voice_filename("cha")
    chan "「だってさ、それで首の血管を切られたらあたし……死ぬよ？　あんた、人殺しになっちゃうよ」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「――フン」"

    "直前に自分を刺そうとしたことを棚に上げて何を言う、とアランは思っていた。"

    "だが、チャンに何を言っても無駄だ、というのは分かり切っていることだった。"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「試してみるか？」"

    show cha sta nor dis rev with std_change

    voice get_voice_filename("cha")
    chan "「嫌だ、嫌だよ」"

    show cha sta nor dis rev with std_change

    voice get_voice_filename("cha")
    chan "「助けて、助けてええ！」"


    stop music fadeout 1

    "この後は、悲惨という他なかった。"

    "チャンの声に合わせるようにして、隠れていたウィリアムが飛び出してきたのだ。"

    "アランに飛びかかってきたが、アランはチャンを盾にして防ぐ。"

    "包丁は邪魔になるので投げ捨てて、チャンを目の前にして立ち止まったウィリアムに向けて、チャンの背中を押す。"

    "ウィリアムの上にチャンが乗っかるような格好になり、アランは二人を見下ろした。"

    show aln sta nor tre with std_change

    voice get_voice_filename("aln")
    alan "「ミスター・ウィリアム。今晩は最後の時を過ごすことだな」"

    "アランは冷たい声でそう言うと、１枚のカードをチャンに見せた。"

    "――Ⅵ・未練・新婚生活。"

    $ add_character_cards("aln", ["6_regret"])

    show cha sta nor dis rev with std_change

    voice get_voice_filename("cha")
    chan "「ああ……あ……あたしの、み、未練……」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「12人の中で、君がもっとも愚かな参加者であろうな」"

    "冷酷な目はもう、チャンへの興味を失っていた。"

    "アランはわざわざ床から拾い、二人に包丁を返した。"

    "日本に来たばかりのアランがこんなものを持っていたら職務質問でもされた時に不利になるからだ。"

    "チャンもウィリアムも、これをチャンスだとは思えなかった。"

    "たとえ彼らが拳銃を持っていたとしても、この男には敵わない。本能に恐怖として刻まれてしまっていた。"

    "この二人がこの後どう過ごしたのかについて、アランは微塵の興味も持っていなかった。"

    show aln sta nor lee with std_change

    voice get_voice_filename("aln")
    alan "「この倉庫は……使えるな」"

    "すでに使われていないし、人の出入りもない。"

    "都内からは近過ぎず遠過ぎずのほどよい距離。"

    "数日様子見をして問題がなければ、彼はここを拠点にしようと決めた。"





    scene bg hotel japan with wfade_long
    pause 1

    show aln ban nor nor at std_c with std_in

    voice get_voice_filename("aln")
    alan "「今なら、あの必死さだけは理解できなくもない……か」"

    "天井を見上げながら、アランはそう呟いた。"









    $ set_info_location("04")

    scene bg lion01 night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "２時間ほど経過して進んだのは、昨日と同じく全体の５分の１くらいだった。"

    "明治末期の少女の日記というのはとても貴重だろうし、面白いは面白いのだが、小説と違って山場を作って書かれているわけではないので、飽きがくるのは否定できない。"

    "≪女神の選定≫と無関係ではあったが、興味深い記述があった。"

    show rnk paj arm lie at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「リンダさんたちも黒猫を、飼ってたんだな」"

    "マイペースな猫で、リンダさんよりもダイアナさんに懐いていたらしい。"

    "好きな時に現れて好きな時にいなくなる……同じ黒猫だし、もしかしたらレテの祖先かもしれない。"

    "名前はレオというらしい。名前まで、レテに似ている。"

    "日記には割れたガラスを踏んで、右の前足の肉球に傷が残ってしまったというエピソードが書かれていた。"

    show lete normal at cat_l, xoffset(-100) with std_in


    voice get_voice_filename("cat")
    lete "「にゃ？」"

    "心の中で噂をしていたからか、偶然レテが通りかかった。"


    voice get_voice_filename("rnk")
    rinka "「あんたも、ガラスには気をつけてね。実は踏んじゃってたり、しないよね？」"


    voice get_voice_filename("cat")
    lete "「にゃー」"


    hide lete
    hide rnk
    with std_out

    "私が近付こうとすると、嫌な予感を察知したのかレテはとことこと走ってどこかへ消えてしまった。"

    "あれだけ元気なら、心配はいらないだろう。"

    "私は日記帳を丁寧に閉じて、自室へ戻ることにした。"







    $ set_info_location("05")


    scene bg myroom night with fade_long
    pause 1

    $ show_hud()

    "寝る準備を終えて横になった私は、これからどうすればいいのか、について考えていた。"

    "問題を整理しよう。大きな問題は３つある。"

    "海晴と私が二人とも生き残る方法を、どう見つけるか。"

    "これが一番大事で、まだ出口が何も見えない。しかし≪女神の選定≫を紐解くという方針は間違っていないはず。"

    "少なくともリンダさんの日記帳を読み終えるまでは、進展がないとは言い切れない。"

    "次は、アランさんの情報をどう集めるか。"

    "このことは私にとって気の重い問題であった。彼の真意が、全然分からなかったからだ。"

    "アランさんは私を敵視していない、それは分かる。けれどだからと言って、脱落してもいいとは思っていないはずだ。"

    "だから必要なことは――話すこと。"

    "連絡手段はないが、近いうちに彼の方からまた接触してくるのではないかという予感がした。"

    "最後の問題は、フェデリーコさんの情報をどう集めるかだ。≪氏名≫と≪死因≫は分かっているが、≪未練≫についての情報はまだない。"

    "彼とは直接会ったこともないし、糸口がない。"

    play se "phone_message01"
    pause 2

    show rnk paj nor ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……あれ」"

    "その時、私のスマートフォンにチャットの着信がある音がした。"

    "海晴だ。"

    "――フェデリーコ・カルミナーティの情報が揃った。明日のバイトは少し遅い時間から開始だから、放課後、ライオン館へ寄ってもいいかい？"

    "文章は簡潔だったが、その連絡のタイミングの良さに感嘆していた。"

    "私はすぐに「大丈夫だよ」という返信をした。丁度いい。海晴が来るなら、その時に日記帳を見つけたことだけは話しておこう。"

    "まだ手詰まりではない。"

    "そのことで無理矢理自分を安心させて、私は眠ることに決めた。"

    $ add_seen_chapter("10-2")








    python:
        set_info_scene("163")
        set_info_date(7, 4, "wed")
        set_info_time("evening")
        set_info_location("14")

    stop music fadeout 2
    scene bg schoolgate noon with fade_longest
    play music audio.nichijo02
    pause 1

    $ show_hud()

    "授業が終わり、私たちはライオン館へ向かおうとしていた。"

    show mhr sun sco cau rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「あれ、今日は日辻さんはいないのかい？」"

    show rnk sun nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「用事があるみたい。必要なことなら、明日にでも伝えておくよ」"

    "海晴から直未のことを聞かれるのは、珍しい。"

    "≪女神の選定≫において私たちが運命と戦うために、海晴にとっても直未は大きな存在に変わっていたのだろう。"

    "些細な言葉のやり取りだったが、私は小さな変化を感じていた。"

    "となると、海晴と２人きり。"

    "真央はすでに告白の返事にまだ時間がかかることは伝えてはいるだろうけれど、どうしても、若干の気まずさを感じずにはいられなかった。"







    $ set_info_location("04")

    stop music fadeout 1
    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "ライオン館についてから僅か30分ほどで、海晴はバイトへ向かうことになった。"

    "話した内容はとても短く、海晴が月曜日の夜にフェデリーコさんと会い、その時の会話から≪未練≫に辿り着いたということ。"

    "すぐには分からなかったが、火曜日の夜に海晴の中で思考が繋がり、カードが作られたらしい。"

    "内容について詳しくは聞かなかったが、フェデリーコさんが私の情報を集めている可能性もゼロではないので、後日きちんと私の方もカード化するようにと話した。"

    "海晴の様子だと彼が私を指名するとは思えないらしいが、保険も大切である。"

    "私も、おばあちゃんの部屋にあった日記帳のことを話した。"

    "海晴はカードブックとそっくりなその日記帳を見て、驚きを隠せてはいなかった。"

    "この日記は私が読んでいて、読み終わったら手に入れた情報を教える、と伝えた。"

    "去り際、海晴は真剣な表情で言った。"

    show mhr sun nor ser at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「その日記帳は、ぼくにはどこか切り札のようなものに見える」"

    "何の根拠もないけれど、と補足していたが、私も同感であった。"

    "海晴が帰ってから、私は今日もお店を開けた。"

    $ add_seen_chapter("10-3")








    python:
        set_info_scene("164")
        set_info_date(7, 5, "thu")
        set_info_time("morning")
        set_info_location("08")


    stop music fadeout 2
    scene bg schoolroom noon with fade_longest
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show rnk sun nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「おはよう、真央」"

    show mao uni nor dis rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「おはよ～。はぁ、来週から期末とか、鬱になりそ」"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「その話はやめて……」"

    "自慢ではないが、中間テストの時以上に勉強をしていなかった。"

    "≪女神の選定≫が始まって間もないということもあり、私の中で中間テストは≪なかったこと≫にしていたが、期末はそうもいかない。"

    "英語だけはカードブックのおかげで何とかしてしまおうか――いや、それをやったらカンニング、人として最低の行為だ。"

    "でも、勉強している時間がないのも事実。"

    "と思っていると、スマホに連絡が入る。校内でスマホをいじるのは禁止ではあるが、それくらいの規則は破らせてもらっている。"

    "おばあちゃんだ。"

    "――『先生から聞いたよ。期末試験の前なんだって。お店はいいから、ちゃんと勉強しなさい。次はちゃんと、試験結果をおばあちゃんのところへ送ること』"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……エスパー……？」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「なになに？　おばあちゃんから怒られた？」"

    show rnk sun nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「真央までエスパーしないで……」"

    "社長からの連絡に、一従業員が逆らうわけにはいかない。"

    "おばあちゃんに連絡をしないでお店を営業するのは不可能だ。"

    "お店を開けることはいい気分転換になっていたので、私は一気に憂鬱な気分になった。"

    "木、金、土、日。"

    "日記帳を読む時間は減らせないが、お店を開けている時間を勉強にあてれば赤点は回避できる。"

    "最悪英語は捨ててカードブックを――いや、だからそれは駄目だって。"

    "普通の日常というのは、案外大変なものだった。"







    python:
        set_info_time("evening")
        set_info_location("04")


    stop music fadeout 1
    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "放課後、私は直未とライオン館で勉強をしていた。"

    "お店は再来週まで強制終了なので、その旨を貼り紙しておいた。"

    "どうやら私の生活態度から今回も勉強をしていないと踏んだ先生が、おばあちゃんに連絡をしたらしい。"

    "私の家庭事情は先生もある程度なら分かっているとはいえ、成績が悪いのを放置することができないのもよく分かる。"

    "≪女神の選定≫が終わってから――生き残ってからもちゃんと勉強をしないと、お店を続けられなくなってしまう。"

    scene ecg girlstalkR1 tro with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「直未ー、そろそろ休憩しない？」"

    scene ecg girlstalkT1 sur with dissolve


    voice get_voice_filename("nom")
    naomi "「だ、ダメですっ！　まだ30分しかやってないじゃないですか！」"


    voice get_voice_filename("rnk")
    rinka "「なんか今日の直未厳しい……」"

    show ecg girlstalkT1 tro with ecg_change


    voice get_voice_filename("nom")
    naomi "「あ、す、すいません。でもせんぱいがそこまで勉強が苦手だったとは、知らなくって……」"


    voice get_voice_filename("rnk")
    rinka "「受験の時は目的があったから良かったんだけど、日々のテストのためっていうとどうしても……」"


    voice get_voice_filename("nom")
    naomi "「ちょっと意外です。まあでも、前に英語の問題を出したとき……悲惨でしたもんね」"

    "今日の直未の言葉には、棘がある。"

    "私が先輩としてあまりに情けない姿を見せてしまっているので、仕方ないのだけれど。"

    scene ecg girlstalkR1 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「海晴は今日もバイト。≪女神の選定≫のことを考えながら、いつ勉強してるんだろ」"


    voice get_voice_filename("nom")
    naomi "「もう、人それぞれ、です！　せんぱいっ、１時間頑張ったら休憩ってことにしませんか？」"

    show ecg girlstalkR1 ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「うん、頑張る」"

    "私は観念して、教科書とノートに向かうことにした。"

    "１年生の時は真央と勉強することも多かったが、大体はおしゃべりで終わる。"

    "なので向かい合って真剣に勉強するというのはある意味、真剣だった。"

    "直未にあんまり呆れられるのも嫌なので気持ちを切り替えて、まずは１時間、集中することにした。"


    scene bg lion01 noon with fade_long
    pause 1

    show nom sun nor smi rev at std_c with std_in

    voice get_voice_filename("nom")
    naomi "「さすがです、せんぱい！　じゃ、少し休憩にしましょう」"

    hide nom with std_out

    "１時間30分が経過して、直未は休憩しようと声をかけてくれた。"

    "きっちり１時間のところで気づいていたのだが、自分からは言い出しにくく、直未が言ってくれるのを待っていたのだ。"

    "直未は私が集中していると見て気を遣ってくれたのだろう。なんとも空しいすれ違いだ。"

    "コンビニで買ってきたお菓子を食べながら、私たちは話していた。"

    "話は途中で、≪女神の選定≫の話になった。"

    "海晴がフェデリーコさんの情報を揃えたこと、そしておばあちゃんの部屋から日記帳が見つかったこと。"

    "私は２階から、その日記帳を持ってきた。"


    play music audio.investigation

    scene ecg lindadiary clo with dissolve_long

    "私のカードブックと２冊、並べてみる。新品と古本で、ビフォーとアフターのようになった。"


    voice get_voice_filename("rnk")
    rinka "「これなんだけど……」"


    scene bg lion01 noon
    show nom sun har sur rev at std_cl
    with dissolve_long

    voice get_voice_filename("nom")
    naomi "「ひ、100年以上前の本っ……！　はわわわっ。ほ、本当に同じ装丁ですね。それも手作りなら、わたしたちが調べても見つからないわけです」"

    show nom sun har hen rev with std_change

    voice get_voice_filename("nom")
    naomi "「そ、それであの……においを嗅いでみてもいいですか？」"

    show rnk sun sur su1 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……え？」"

    show nom sun hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「ち、ちょっとだけなので……。あ、触る時に手袋とか、いらないんですか？」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「そこまで気にしてなかったけど。今、読んでるしね」"

    show nom sun har hen rev with std_change

    voice get_voice_filename("nom")
    naomi "「せんぱい！　も、もっと大事にしましょうよ……そ、それであの、読み終わったら私も読んでいいですか？」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「いいけど、私が読み終わったら内容話しちゃうよ？」"

    show nom sun nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「いいんです！　そんな昔の本を読めるだけで幸せなので……」"

    hide nom
    hide rnk
    with std_out

    "私は直未が急に興奮したように見えて、驚いていた。"

    "同時にこの本をこれ以上ここに置いておくのは危険だと判断し、自分の部屋へと戻しにいった。"

    "その間、直未はずっと本を目で追っていて、本好きだというのをあらためて実感した。それもかなり濃い方の。"

    show nom sun hes sor rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「す、すみません……。つ、つい……」"

    show rnk sun nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あ、いつもの直未だ。よし、じゃあそろそろ勉強再開しよっか」"

    "私たちはまた１時間と決めて、教科書とノートに向かうのだった。"









    python:
        set_info_time("night")
        set_info_location("04")

    stop music fadeout 2
    scene bg lion01 night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "休憩を挟みながらではあるが、凛火と直未の二人は８時頃まで勉強していた。"

    show nom sun nor smi rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「わたし、そろそろ行きますねっ」"

    "そう言うと、直未は帰る仕度をし始めた。"

    "凛火の勉強嫌いの一面を見て、直未は微笑ましくなっていた。尊敬できる先輩に変わりはないが、こんな一面があるのは意外だったからだ。"

    "――楽しい、と思った。"

    "直未は最近、日々を重ねるごとに強く大きくなっていく想いを抱えていた。"

    "――失いたくない。想い出を失いたくない。"

    "≪女神の選定≫の参加者ではない直未にとって、記憶の改変が行われないということと、凛火と海晴の二人が生き残ることは同義だった。"

    "何度も口にしたその想いは留まることを知らず、直未の心を押し潰しそうなほどに大きくなっていく。"

    show nom sun que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「よかったら、明日も一緒に勉強しませんか？」"

    show rnk sun nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「――もちろん。明日は、真央と海晴も来るかもね」"

    "凛火は微笑んで、直未にそう答えていた。"

    show nom sun nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「はいっ！」"

    "直未も精一杯の笑顔を凛火に向けるのであった。"







    $ set_info_location("18")

    stop music fadeout 1
    scene bg lion02 night with fade_long
    pause 1

    $ show_hud()

    "ライオン館を出て少し歩いたとき、直未はライオン館の前で見知らぬ男性が何か呟いているのを見た。"

    "振り返って声の主の顔を見て、直未の瞳孔はくっと縮む。"

    show aln sta nor nor rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「……何？　しばらく休みだと」"

    "アラン・スコーピオン。"

    "≪女神の選定≫のⅫ番に位置する参加者であり、残り４人のうちの一人。"

    "直未も桂子さんの一件があった時に病院でその顔を見たことがあった。"

    "桂子……さん？"

    "病院……？"


    play music audio.kinpaku

    show nom suw wea wea at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「つっ――」"

    "直未の頭の中に、２つの記憶が同時に走る。"

    "瓶淵桂子という名前だけ知っていて、直未は自分が体調不良で病院に行ったとき、貧血で倒れてしまったという記憶。"

    "凛火とともに病院へ行き、瓶淵桂子という女性に出会い、境遇を知り、同じように彼女のことを調べに来たアランに襲われたという記憶。"

    "さらには自分が体験したのではなく、凛火から聞いた話も混ざってきた。"

    "直未は思わず、膝をついていた。"

    "どの記憶が真実で、どの記憶が嘘なのか、直未は混乱する頭が処理落ちするのを感じていた。"

    show aln sta nor que rev with std_change

    voice get_voice_filename("aln")
    alan "「……君は……」"

    "直未の異変に気がついたアランが、直未の方へ駆け寄ってきた。"

    "彼の方ははっきりと直未のことを覚えているらしい。"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「大丈夫か？」"

    "直未は、アランがどうして自分のことを気に掛けるのかが分からなかった。"

    "いや凛火の後輩だから気にするのは当然だけれど、何故そんなに心配そうな声を出すのかが分からなかった。"

    "直未の記憶のどこかに眠っているアランの姿は、そんな優しい人ではなかったのだから。"

    "そんな風に思うと、直未は余計に苦しくなる。"

    show nom suw wea wea with std_change

    voice get_voice_filename("nom")
    naomi "「な……かに……まだ……、せんぱい……が……」"

    "直未はどうにか、その言葉を捻り出した。"

    "この男性をライオン館に近づけない方がいい、とは、不思議とこの時は思っていなかった。"








    python:
        set_info_scene("65")
        set_info_location("04")

    scene bg lion01 night with fade_longest
    pause 1

    $ show_hud()

    play se "bell02"

    "直未がライオン館を出て10分くらいしてから、再びライオン館に来客があった。"

    "それは、意外な人であり、予想外の状況であった。"

    show aln sta nor ang rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「――水と、ベッドを」"

    show rnk sun sur su2 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「え、ええっ？」"

    "アランさんが直未を抱えて、ライオン館へ入ってきたのだ。片腕で首から直未の頭を支え、片腕で膝からふとももを支えている。いわゆるお姫様だっこの格好だ。"

    "驚いたのも束の間、顔を赤くして息を荒げる直未を見て、何か体調に問題があることに気がついた。"

    hide rnk
    hide aln
    with std_out

    "詳しい事情を聞く前にお水を用意して、直未は２階のベッドに寝かせた。"

    "さすがにアランさんを私の部屋に入れるのは抵抗があったので、彼には１階で待っていてもらうことにした。"


    stop music fadeout 1
    scene bg lion01 night with fade_long
    play music audio.myroom_night
    pause 1

    "１階に戻ったとき、アランさんは椅子にも座らず仏頂面で立っていた。"

    show aln sta nor irr rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「どうだった？」"

    show rnk sun nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「意識はあるけど、頭痛がするみたい。頭痛薬とお水を飲ませたから、１時間くらい様子を見る」"

    "念の為、直未のお母さんには私から連絡をした。"

    "具合が悪いみたいなのでうちで寝かせています、心配しないでください、と。"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ありがとう……ございます。でも、どうして直未を？」"

    show aln sta nor tre rev with std_change

    voice get_voice_filename("aln")
    alan "「この店の前でいきなり倒れたようだ。目の前で倒れられたら、見捨てるわけにはいかない」"

    show rnk sun arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「親切なことに、正直、驚いた。ごめんなさい、もっと冷酷な人だと思っていたから」"

    "病院で看護師さんたちを昏倒させたり、冷酷な目で他の参加者を脱落させるような人にかける言葉ではない、とも思った。"

    "しかし私を助けてくれたし、直未も助けてくれた。"

    "だから自然と私の口から出た言葉だった。"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「やっと話して――くれるんだね」"

    "ライオン館まで来たということは、間違いなく私に用事があるということ。"

    "私も、彼が私と話をしに来ると予感はしていた。選定の直前、つまり土日のどちらかだと思っていたので、予想よりは早いが。"

    scene ecg alantalk normal with dissolve_long


    voice get_voice_filename("aln")
    alan "「……ああ」"


    voice get_voice_filename("aln")
    alan "「君は何度も、僕の行動を不可解だと思ったことだろう。その答えを、与えにきた」"


    voice get_voice_filename("aln")
    alan "「あの日。夜の病院で華奢で無力な君が僕に立ち向かう様を見て、その瞳を見て、思ったことがある」"


    voice get_voice_filename("aln")
    alan "「君の瞳は――君は、僕の妹に似ている」"


    play music audio.memories

    "アランさんは穏やかな表情で、そう言った。"


    voice get_voice_filename("aln")
    alan "「僕には４人の弟と、一人の妹がいる。弟たちはまだ小さいが、妹の歳は丁度、君と同じくらいだ」"


    voice get_voice_filename("aln")
    alan "「妹の名前はアムリタ。僕と違って、妹たちは両親から受け継いだ氏名を名乗り続けている」"

    "オデットさんとアランさんが戦った後、目を覚ます前に呟いていた単語を思い出した。"

    "アムリタ、それは彼の妹の名前だったのか。"

    show ecg alantalk close with ecg_change


    voice get_voice_filename("aln")
    alan "「ちなみに君よりも顔立ちも発育も良く、聡明だ」"


    voice get_voice_filename("rnk")
    rinka "「……ちょっと」"

    show ecg alantalk normal with ecg_change


    voice get_voice_filename("aln")
    alan "「だが、君たちは根源的に似ている。誰よりも意志の強い瞳も、感情的になったときの迂闊さも」"


    voice get_voice_filename("aln")
    alan "「弟たちは僕と同じように、強く成長するものと確信している。僕は男だ。血の繋がりというのは強い。それに、男の気持ちはよく分かる」"


    voice get_voice_filename("aln")
    alan "「だが心配なのはアムリタだ。あの性格では仕事も結婚も、不器用にしかできないだろう」"

    scene ecg cardbook bli with dissolve

    "アランさんがそう言うと、私の傍らに置いたカードブックが光を放った。"

    "そこに生まれたのは、１枚のカード。"

    "――≪Ⅻ・未練・妹の将来≫と書かれたカードだった。"

    python:
        add_character_cards("rnk", ["12_regret"])
        add_character_cards("aln", ["12_regret"])

    "時折見せる穏やかな表情が想うものが彼の妹のことだと思うと、このカードは意外だとは思わなかった。"

    "そこまで理解できるほどに、いつの間にか、私はアランさんのことを知っていた。"


    scene bg lion01 night
    show rnk sun nor que at std_cr
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「どうして、私に自分の≪未練≫を教えたの？」"


    show aln sta nor nor rev at std_cl with std_in
    voice get_voice_filename("aln")
    alan "「君に生きて欲しいと思ったからだ」"

    show rnk sun arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「だって――」"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「構わない。これが僕の結論でもある」"

    show aln sta nor lee rev with std_change

    voice get_voice_filename("aln")
    alan "「だが、君にはこれから僕の人生を背負ってもらい――僕たちの物語に、終止符を打ってもらおう」"

    scene ecg alantalk normal with dissolve_long

    "そしてアランさんは、彼自身の過去を語り始めた。"

    "母親が幼い頃に病死し、宝石商を営んでいた父親は副業で始めた金融で恨みを買って殺された。"

    "その後にアランさんがお父さんの商売のルートを利用する一方で、改名をし、宗教も捨て、自国の伝統的な文化さえも彼にとって非効率なものを全て切り捨て――。"

    "一から会社を立ち上げ、今のように大きな会社にし、財をなした。"


    voice get_voice_filename("aln")
    alan "「だが、僕は会社を大きくする過程で、多くを切り捨ててきた。物も……人も。恨みを買うという性質は、姓を捨てたくらいでは変わらなかった」"


    voice get_voice_filename("aln")
    alan "「僕の≪死因≫は≪毒死≫だ。皮肉にも父と近しい方法で暗殺をされた」"

    "アランさんはいつもと変わらない調子でそう言うと、淡々と自分が殺された方法を話す。"



    scene ecg cardbook bli with dissolve
    pause 2
    show ecg cardbook op3 with dissolve

    "私の手元には、アランさんの≪死因≫のカードが生成された。"

    $ add_character_cards("rnk", ["12_death"])


    voice get_voice_filename("rnk")
    rinka "「殺された……だなんて……」"


    voice get_voice_filename("aln")
    alan "「君が想像している以上に、世の中には不審死というまま処理される暗殺が多い。僕が脱落した場合も、恐らく暗殺とは処理されないだろう」"

    "アランさんは、死を迎えた時、つまり≪因果の刻≫の状況から自分の≪死因≫を推測したのだという。"

    "毒による暗殺など、実際に毒を服するまでは気づくことはできないだろうから。"


    scene bg lion01 night
    show aln sta nor nor rev at std_cl
    with dissolve_long

    voice get_voice_filename("aln")
    alan "「僕はずっと、君にアムリタの姿を重ねて見ていた。困っている人がいたら放っておけないお節介さや流されやすさもあったな」"

    show aln sta nor tre rev with std_change

    voice get_voice_filename("aln")
    alan "「一方で、友人のために邁進する気概も持ち合わせている。君のお婆様がスケールに襲われた時もそうだ。君は彼女たちを救うことしか考えていなかったはずだ」"

    show rnk sun arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「でも、私は私。アランさんの妹じゃ、ない」"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「無論、分かっている。だが、根本は同質だ」"

    "私はアムリタさんのことを知らないので、否定することも肯定することもできなかった。"

    "アランさんはそんな私の戸惑いを分かっているのだろうが、特に気にすることなくそのまま話を続ける。"

    "きっと、彼にとって私がどう思うかは関係ないのだ。"

    "私は今、アランさんの理論的ではない部分、感情的な話を聞いているのだから。"


    play music audio.thebonds
    scene ecg alantalk normal with dissolve_long


    voice get_voice_filename("aln")
    alan "「僕は会社の人間を信用していない。あらかじめ僕が死んだ際には、家族を次の社長に据えるように文書を残していた」"


    voice get_voice_filename("aln")
    alan "「つまり年齢的に言って、僕の妹――アムリタが次の社長だ。心配だったよ。アムリタは優しく脆い。人の悪意と欲望が渦巻く中で、うまくやっていけるか、とね」"


    voice get_voice_filename("rnk")
    rinka "「私と同い年で、社長に……」"


    voice get_voice_filename("aln")
    alan "「ああ。だが、君を見ていたら少しだけ安心することができた。自分の弱さを自覚しているけれど、無自覚に強い芯を持っている」"


    voice get_voice_filename("aln")
    alan "「人の心を動かすことができる――信用できる{rb}人間{/rb}{rt}とも{/rt}を作ることができる。自分の瞳の力を疑うのであれば、目の前にいる僕を証拠にすればいい」"

    "アランさんは真っ直ぐに私を見つめて、言った。"

    "目を合わせてはいるけれど、きっと私を見ていない。その向こうに、大切な妹の姿を見ている。"


    voice get_voice_filename("rnk")
    rinka "「買いかぶり過ぎ。それに、私はそんな責任持てない」"

    show ecg alantalk close with ecg_change


    voice get_voice_filename("aln")
    alan "「……フン。構わないさ。これは、僕の決断だ」"

    show ecg alantalk normal with ecg_change


    voice get_voice_filename("aln")
    alan "「もっとも利益を生み出すという意味で、アムリタが僕より上を行くことはないだろう。失敗も多くするかもしれない。だが、僕とは違った成長を生むはずだ」"


    voice get_voice_filename("aln")
    alan "「そして何より、僕のように暗殺されることはないだろう。究極的に言えば、アムリタが長生きしてくれればそれでいい」"


    voice get_voice_filename("rnk")
    rinka "「アランさん……」"

    show ecg alantalk smile with ecg_change


    voice get_voice_filename("aln")
    alan "「無論、まだまだ心配は尽きない。けれどそこに希望を見ることができた。この僕が、希望を見たんだ。その意味が分からない君ではないのだろう？」"

    "アランさんは穏やかな顔で――微笑んだ。"

    "ああ、この人は。"

    "こんな風に笑うことができたんだ――場違いかもしれないけれど、私はそう感じていた。"

    "アランさんから感じる朗らかな愛情は、きっとお兄さんならではのものなのだろう。"

    "私には両親も兄弟もいないため比較するものはないけれど、きっとそうだと確信していた。"


    voice get_voice_filename("aln")
    alan "「何が可笑しい？」"

    "言われて、私も笑っていることに気がついた。"

    "厳しいけれど、優しくて頼りになる。"

    "頭が良くて余裕があるはずなのに、何故かいつも焦って見える。"

    "こんなお兄ちゃんを持っているアムリタさんが、少し羨ましくなった。"

    "おかしい。ああ、私はおかしい。"



    scene bg lion01 night
    show rnk sun nor smi at std_cr
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「……何でもない」"


    show aln sta nor nor rev at std_cl with std_in
    voice get_voice_filename("aln")
    alan "「……そうか」"

    "この人に対して、こんな風に思うなんて。"

    "いや、違う。"

    "桂子さんの情報を集めていた時の病院での一件があったから、私はアランさんをきちんと見ようとしていなかっただけなのだ。"

    "茂継さんの家に行ったときも、ユウくんのテロを止めたときも、スケールさんからおばあちゃんを助けてくれたときもずっと――彼は、優しかったじゃないか。"

    "目を閉じていたのは、私なのだ。"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「私の生き方がどこまで通用するのか、見届けるんじゃなかったの？」"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「言っただろう。君の生き方が通用した結果が、今の僕だと」"

    "アランさんは一呼吸おいてから、私の胸に刺さる質問をした。"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「ミハル・ヘビナタとの決着はどうするつもりだ？」"

    "胸に刺さったのは、彼がやはり私のことをよく理解していると分かったからだ。"

    "質問に答えるのに、迷うことはない。"

    "答えを一つしか持ち合わせてはいないから。"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「生き残る――二人で」"

    show aln sta nor lee rev with std_change

    voice get_voice_filename("aln")
    alan "「ああ、いい答えだ。アムリタも――獅子舞凛火なら、そう答えるはずだから」"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「私の淹れるコーヒー、美味しいんです。最後に飲んでいきませんか？」"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「……ああ。頂こう」"

    "私は無意識のうちに、最後と言っていた。"

    "アランさんも、聞き逃してはいないだろう。"

    show rnk sun arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっとだけ、待っていてくださいね」"

    "私は精一杯の気持ちを込めて、最高の一杯を淹れるために集中をした。"




    play music audio.nichijo01
    scene bg lion01 night with fade_long
    pause 1

    "彼がコーヒーを飲んでいる間、私たちは何も言葉は発しなかった。"

    "ただ、無言の時間に会話がないわけではなかった。"

    "アランさんと私の関係は、≪女神の選定≫の参加者同士という以上でも以下でもない。"

    "仲間でもないし、友達でもないし、恋人でもないし、敵でもないし――兄妹でもない。"

    "だが、だからこそ――。"

    show aln sta nor gen rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「ごちそうさま。僕はコーヒーがあまり好きではないが、美味しいと思ったよ」"

    show rnk sun arm lie at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ありがと」"

    "アランさんは立ち上がり、続ける。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「そろそろ、君の後輩の様子を見に行った方がいい」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、そのつもり」"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「君は何人もの人生を託されてきたのだろう。それでも強く生きたいと望むのは、君にしかできないことだ。他人の人生など、重荷に過ぎないだろうに」"

    show rnk sun arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私は一人じゃないから。重荷じゃなくて、力に変わった」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「……フン。肉体において、人間は常に一人だ。だからこそ一人ではないと信じられることが君の強さなのだな」"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「アランさんだって、ずっと一人じゃなかったはず。でしょう、お兄ちゃん？」"

    show aln sta nor tre rev with std_change

    voice get_voice_filename("aln")
    alan "「冗談はよしてくれ。言ったはずだ。アムリタは君よりも才気煥発で器量もよいと」"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「……何より僕は、君の生き方を認めるまで、アムリタを信じてやれなかった。その意味で、僕はやはり一人だった」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「君に、頼みがある」"

    show rnk sun arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「……はい」"

    show aln sta nor lee rev with std_change

    voice get_voice_filename("aln")
    alan "「僕は日本へ来るとき、僕のルーツに関わるあらゆるものを置いてきた。だから君に預けられる物は何もない」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「しかし、刻んでくれ。君の人生の軌跡に、僕を。歪んだ運命の中で、君と出会えた奇跡を」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「アムリタさんに、会いには行かないんですか？」"

    show aln sta nor tre rev with std_change

    voice get_voice_filename("aln")
    alan "「君には関係のないことだ。君は獅子舞凛火だろう？」"

    "問い掛けたアランさんに、私は頷いた。"

    "彼がちゃんと質問に答えていたら、その答えがどちらでも、私はきっと彼を指名するのを躊躇っていたことだろう。"

    "最後の最後で、彼は私を突き放した。"

    "だけど私は知っていた。"

    "この距離は優しさの距離だ。"

    hide aln with std_out

    "それ以上何も言わず、アランさんはライオン館を後にした。"

    "私は彼の背中が見えなくなっても、しばらく暗闇の中を目で追っていた。"

    "確信があったからだ。"

    "アラン・スコーピオンと現実世界で会うのは、これが最後なのだと。"







    python:
        set_info_time("lnight")
        set_info_location("04")

    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    "アランさんがここを去ってから間をおかずに、直未が２階から下りてきた。"

    show rnk sun arm imp rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「直未！　具合は大丈夫？」"

    show nom sun nor ser at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「は、はい。心配かけてすみません……、大丈夫です。それより、ごめんなさい……」"

    "直未は一呼吸おき、私から目を逸らして言った。"


    play music audio.naomi

    show nom sun hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「聞いちゃいました。アラン・スコーピオンさんと話していたこと。わたし、勘違いしてました。彼は、あんなに優しい人だったんですね」"

    show nom sun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「お礼も言わなきゃいけないのに、もう……」"

    show rnk sun arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……大丈夫」"

    "直未に対して、私はこの言葉しか出てこなかった。"

    show nom sun hes sor with std_change

    voice get_voice_filename("nom")
    naomi "「彼は、海晴先輩がフェデリーコ・カルミナーティさんの情報を揃えていることに気が付いていたんでしょうか。次の選定でせんぱいと海晴先輩と、２人が残るようにするために」"

    show rnk sun nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そうだね、きっと」"

    show nom sun hes tr2 with std_change

    voice get_voice_filename("nom")
    naomi "「彼が脱落したら、わたしは忘れちゃうんですね。今日助けてもらったことも、やっと知った彼の優しいところも」"

    show rnk sun arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「だから私が、刻むんだ。彼のことを、心に」"

    show nom sun nor nor with std_change

    voice get_voice_filename("nom")
    naomi "「そしたら必ず、教えてください。わたしが忘れてしまっているはずのことを」"

    show rnk sun arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「もちろん……だって私一人じゃ、背負いきれないから」"

    "直未は私の手をぎゅっと握った。"

    "≪女神の選定≫の参加者ではないのに、私と行動を共にしているからこそ、直未の記憶は不安定なものになる。"

    "何故、記憶の改変は完璧ではないのだろう。"

    "このシステムを作ったのが女神だとしたら、私は抗議をしたい。"

    "だって、残酷過ぎる。"

    "心臓の鼓動だけが生きることではない。心に自分を刻むこともまた、生きることなのだ。"

    "だから記憶を塗り替えるなんて、思い出を忘れさせてしまうなんて、人を殺すのに等しいじゃないか。"

    show nom sun que que with std_change

    voice get_voice_filename("nom")
    naomi "「わたし、まだ具合が悪いみたいです……だから、今日は泊めてもらえませんか？」"

    show rnk sun nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。いいよ。ただ、お母さんにはちゃんと連絡しておきなね」"

    "それが仮病だと、すぐに分かった。"

    "だけど、私は直未を咎めることはしない。"

    "今夜は、独りじゃきっと辛いから――。"

    $ add_seen_chapter("10-4")








    python:
        set_info_scene("166")
        set_info_date(7, 7, "sat")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_refreshing_morning
    pause 1

    $ show_hud()

    "２日が経って土曜日。"

    "昨日は特に何事もなく、一日が終わった。"

    "放課後は直未と海晴と真央と私の４人で勉強をして、夜は日記帳を読み進めた。"

    "海晴には、アランさんのことは話してある。"

    "次の選定で、海晴はフェデリーコさんを、私はアランさんを指名する。"

    "結果だけ見れば、比較的容易に海晴と私が残るという形が出来上がるように見える。"

    "ユウくんの時のような大きな事件や、オデットさんの時のような駆け引きはない。"

    "だけど、心は違った。"

    "私たちはそれぞれ指名する予定の相手のことを知ってしまったからこそ、彼らの変化を見届けてしまったからこそ、より重く、その事実を背負うこととなるのだ。"

    "けれども、時が来るまでずっと落ち込んでいても仕方がない。"

    "私は気持ちを切り替えて、学校へ行く準備を始めた。"







    $ set_info_location("08")

    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    "登校すると、真央は何故かにやにやして私を待っていた。"

    show mao uni sel glo rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「おはよーりーたん！　今日は何の日か分かるかな？」"

    show rnk sun nor nor std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「え。７月７日だから、そっか、七夕だね」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「せいかーい！　食堂の方に笹があるから、短冊飾りに行こ～」"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「んー、ちょっと恥ずかしいけど、いいよ。真央が学校のそういうのに興味持つって、珍しいね」"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「別にぃ。気分だよ、気分。みはるんもだからねっ」"

    show mhr sun sco con at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「……凛火が書くなら、ぼくも書くよ」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「けってーい。んじゃ、なおりんにも連絡しとこ」"

    "きっと、朝にテレビで七夕特集でもやっていたのだろう。"

    "それでも、真央の元気な姿を見ると安心する。"

    "いや、真央の場合は夜更かしして眠そうな姿でも安心するかな。"







    python:
        set_info_time("noon")
        set_info_location("42")

    scene bg schoolcorridor normal with fade_long
    pause 1

    $ show_hud()

    "短冊を書き終えた私たちは、教室へ戻る廊下を歩いていた。"

    "真央の言う通り、大学と共通の食堂には笹竹が飾られていた。"

    "意外にも書かれていた短冊の数は多く、ちらりと見てみると恋愛の悩みが多かった。"

    show mao uni sel lau rev at std_cl, xoffset(100) with std_in

    voice get_voice_filename("mao")
    mao "「いやあ、みんな何を書いたのかなぁ？」"

    show rnk sun arm ama at std_cr, xoffset(-140) with std_in

    voice get_voice_filename("rnk")
    rinka "「秘密にするって約束だったでしょ」"

    "短冊に書いたことは、それぞれ内緒にすることにしていた。"

    "理由は単純、恥ずかしいからだ。"

    show mhr sun nor ser behind rnk at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「日辻さん。故意ではないにしても君はぼくの短冊を見た。もしそれを誰かに話したら、どうなるか分かっているね」"

    show nom sun har pin rev behind mao at std_l with std_in

    voice get_voice_filename("nom")
    naomi "「ご、ごめんなさい……。わたし、言いません！」"

    show mao uni sel irr with std_change

    voice get_voice_filename("mao")
    mao "「おっ、なおりん、みはるんのお願い事を見ちゃったんだー。ほれほれ、真央様だけに教えてみなさい～」"

    show nom sun hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「真央先輩でも無理ですぅー！」"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「ははは……」"

    "海晴は慌てる直未をわざとらしく睨みつけたあと、微笑んだ。"

    "ちなみに私はというと――いや、自分で書いたお願い事を思い返すこともないだろう。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「もういくつか寝ると、夏休みだねぇ」"

    show mhr sun sco con with std_change

    voice get_voice_filename("mhr")
    miharu "「ああ、そうだね。２ケタをいくつかと言うには多い気もするけれど」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんは覚えてる？　花火大会。ちょうど来月の今頃じゃなかったぁ？」"

    show rnk sun nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「――うん」"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「行こうね、４人でさ」"

    "真央は、ちょっとだけしんみりした声で言った。"

    "真央がそんな声を出すのが意外で、私たちは黙ってしまった。"

    "その沈黙を破ったのは、直未。"

    show nom sun nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい！　行きましょう！　わたし、花火、大好きです！」"

    "海晴も私も頷いただけで、言葉にすることはできなかった。"

    show mao uni sel glo with std_change

    voice get_voice_filename("mao")
    mao "「んじゃ、なおりんは朝一で場所取りだねぇ」"

    show nom sun har sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「が、頑張ります！」"

    show rnk sun arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「みんなで一緒に、ね。行こう、きっと」"

    show mhr sun pai lie with std_change

    voice get_voice_filename("mhr")
    miharu "「…………凛火がそう言うのなら、ぼくも」"

    "言葉にするのを躊躇うからこそ、私は頑張って口に出した。"

    "短冊に書いた願いよりも、もっと身近で、だけど切実な願い事を。"







    python:
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "一日を終えて、私は寝る支度を整えていた。"

    "日記帳も、ページでいうとほとんど最後の方まで来ていた。"

    "残り２時間程度で読み終わるだろう。"

    "日記の２冊目は見当たらなかったので、いよいよ明日でリンダさんとダイアナさんの記録の最後の１ページを目にすることになる。"

    "私はそう思いながら、昼間のみんなとの会話を思い出していた。"

    show rnk paj nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「花火……か」"

    "花火大会。"

    "遊園地で海晴と二人になったとき、その話をした。"

    "私だけが≪女神の選定≫について知らなかった頃だ。"

    "あっ、駄目だ。"

    "突然、走馬灯のように想い出が頭の中を駆け巡ってしまった。"

    "夜に、負けた。"

    "溢れてくる感情を抑えることができず、私は目の奥の方が熱くなるのを感じていた。"


    stop music fadeout 1

    show rnk paj sur scr with std_change

    voice get_voice_filename("rnk")
    rinka "「いきたい！　いきたいよ！」"

    "思わず、大声で叫んでいた。"

    "深夜であることを思い出して、すぐに口元に枕を当てる。"

    show rnk paj arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「――――――っ！」"

    "そのまま、声にならない声をあげていた。"

    "唐突だった。"

    "この濃密な日々を失うかもしれないという恐怖が、湧き上ってしまったのだ。"

    "全部なかったことになるなんて、嫌だ。"

    "気持ちの整理なんてつかないまま、私はいつしか眠りについていたらしい。"

    $ add_seen_chapter("10-5")










    python:
        set_info_scene("167")
        set_info_date(7, 8, "sun")
        set_info_time("morning")
        set_info_location("03")


    stop music fadeout 2
    scene bg train normal with fade_longest
    play music audio.badguys
    pause 1

    $ show_hud()

    "日本時間で日曜日の朝、フェデリーコはインドから日本へと戻ってきていた。"

    show fed sta dar dar at std_c with std_in

    voice get_voice_filename("fed")
    federico "「手に入れたのは≪死因≫まで、か……。畜生……」"

    $ add_character_cards("fed", ["12_death"])

    "彼はインドに行き、アランの会社を訪問し、またアランの家も訪問していた。"

    "アランはどうやら極秘の出張ということになっているらしく、社長業に関しては最低限の連絡だけが行くようになっているそうだ。"

    "重要な事項の決定は暫定的に副社長が行っているとのこと。"

    "そこで彼は、アランを疎ましく思っている勢力が社内にあることを知った。"

    "その勢力は別の企業との繋がりがあることも。"

    "ミハルから聞いていたカードの情報と合わせて推理して、フェデリーコは≪Ⅻ・死因≫を手に入れたのだった。"

    "しかし彼の会社関係者にはアランの≪未練≫に繋がる情報を知っている者はいなさそうだった。"

    "次いでアランの家を訪問したフェデリーコだが、それもほとんど無意味に終わった。"

    show fed sta dar irr with std_change

    voice get_voice_filename("fed")
    federico "「まさかあんな奴がいるとはなぁ」"

    scene ecg amrita normal with dissolve_long

    "アランのことを詮索しようとしていることに気が付いた少女がいた。"

    "アムリタとかいう名前で、苗字は違うがアランの妹らしい。"

    "彼女はフェデリーコを見ると「お兄ちゃんのことで教えることなんて何もない！　おじさんは帰って！」と面と向かってきっぱりと言われてしまった。"

    "フェデリーコは、アランは毒殺されるくらいだから、敵も多いと理解していた。"

    "当然、家族であるアムリタのところに、アランの弱味がないか探りに来る人がいるだろうことも。"

    "フェデリーコはそんなアムリタに対して、脅しをかけた。"

    "だが彼に怯むことなく、アムリタは毅然とした態度でフェデリーコを睨んだ。"

    "その瞬間、彼は少女が恐怖を忘れていると思った。"

    "他人に慈悲なく、徹底した実力主義で仕事を失った者が多くいることなど、兄の悪い面も、アムリタは恐らく知っている。"

    "しかし聡明な彼女は兄の悪い面も知った上で、兄の敵になりうる者に詮索されるのを拒否したのだ。"

    "矛盾を抱えたまま、それでも、真っ直ぐな瞳でフェデリーコの前に立ち塞がったのだ。"

    "マフィア時代のフェデリーコなら、彼女をひどい目に合わせてでも情報を聞き出していただろう。"

    "だが彼女がアランの≪未練≫を知っているという確信も組織の後ろ盾もない彼は、その少女から情報を引き出すのは諦めた。"

    "そもそも普通の説得では動かないことは、目を見たときに直感していた。"


    scene bg train normal
    show fed sta dar phi at std_c
    with dissolve_long

    voice get_voice_filename("fed")
    federico "「誰かに似てる気がしたんだよなぁ。けど、オデットとも違うしよ」"

    "少女の見せた凛とした瞳。"

    "フェデリーコはその正体が思い出せない不快感と苛立ちとを感じていた。"

    show fed sta dar smi with std_change

    voice get_voice_filename("fed")
    federico "「ま、いーか。顔こそ美人だが、まだまだちんちくりんだったしよ。しかしあの性格じゃ、将来が心配だぜ」"

    "かくして、彼はアランの≪未練≫を手に入れられずにいた。"

    "インド滞在に期限をつけたのは自分の気持ちが逃げることを防ぐためと、最後の足掻きの時間を作るためであった。"

    "敗北者の彼ができることと言えば、あとは一つ。アランを探して直接問い詰めることだった。"

    show fed sta dar ser with std_change

    voice get_voice_filename("fed")
    federico "「さぁて、あの野郎はどこにいやがる」"

    "そんなことを思いながら、フェデリーコは再び電車に揺られるのであった。"

    $ add_seen_chapter("10-6")








    $ set_info_location("05")

    stop music fadeout 1
    scene bg myroom morning with fade_long
    pause 1

    $ show_hud()

    show rnk paj arm sad at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「そっか、寝ちゃってたのか……」"

    "気持ちが破裂してしまってから迎える朝は、心地の良いものではなかった。"

    "それでも前向きに考えるならば、私の心が思ったよりも疲弊していることを自覚できた、というところか。"

    "とりあえず窓を開けて、外の空気を胸一杯に吸い込んだ。"









    python:
        set_info_time("night")
        set_info_location("26")


    stop music fadeout 2
    scene bg road night with fade_longest
    play music audio.growapart
    pause 1

    $ show_hud()

    show fed sta dar phi at std_c with std_in

    voice get_voice_filename("fed")
    federico "「あーあ、結局オレらしいっつーかよ」"

    "敗北者に相応しい最後だと、フェデリーコは自嘲していた。"

    "スケールという協力者がいない今、彼はアランに連絡する手段を持たない。"

    "東京タワーや牛塚茂継の家があった場所、念のためオデットたちと落ち合ったという横浜の倉庫まで出向いたが、彼はアランと遭遇することはできなかった。"

    "最後にフェデリーコは≪運命の終着点≫である新宿御苑を訪れた。"

    "何故そこに大層な名前がつけられているのか彼は知らなかったが、理由などどうでもいいと思っていた。"

    "大切なのは、そこでもアランには会えなかったということだ。"

    show fed sta dar irr with std_change

    voice get_voice_filename("fed")
    federico "「オレたちは運命では繋がってないってわけだ。おえ、それはそれで虫唾が走るぜ」"

    "今でこそガニ股でのんびり歩いているが、時間が少しでも惜しい今日、彼は自分の足で移動するときは全て走っていた。"

    "代謝のいい方ではない彼が、汗だくになるほどに。"

    "彼はアランに勝つため、努力をしていたのだ。"

    "フェデリーコにとって努力とは、久しく忘れていたことでもあった。"

    "だから報われなかったとしても――奇妙な清々しさを感じていた。"

    show fed sta dar phi with std_change

    voice get_voice_filename("fed")
    federico "「酒でも飲んで、寝ちまうかな」"

    "彼はそう言うと、最後の夜を歩き始めた。"







    $ set_info_location("18")

    scene bg lion02 night with fade_long
    pause 1

    "１時間ほど歩いたところで、彼は新宿御苑の近くまで戻って来ていた。"

    "歩いている途中、一軒のカフェが目に入った。"

    show fed sta dar smi at std_c with std_in

    voice get_voice_filename("fed")
    federico "「まずコーヒーってのも悪くねぇか……」"

    "彼は旅の途中、エスプレッソを飲んでいなかった。"

    "故郷の味には程遠いかもしれないが、久し振りに飲みたいという欲が湧いたのだ。"

    "その店は電気もついていたので、まだ営業中だろう。"

    "彼は意気揚々と、店の前へと向かっていった。"









    $ set_info_location("04")

    stop music fadeout 2
    scene bg lion01 night with fade_longest
    pause 1

    $ show_hud()

    "夜になって、私はテーブルに日記帳を出していた。"

    "読書のお供のために、コーヒーも淹れている。こぼしたら大変なので、細心の注意を払っている。"

    "溜まっていた家事があったので丸一日勉強していたわけではないが、どちらにせよやっと肩の力を抜ける。"

    "そう、リラックスできるのだ。"

    "リンダさんの日記を読むことは≪女神の選定≫の情報を探す以上に、読書の楽しみも生んでいた。"

    "直未の本好きも、今なら前より理解できる。"

    show rnk paj nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「さて……」"

    "私はコーヒーを一口飲んでから、日記帳のしおりを挟んだページを開いた。"

    "ライオン館の前で誰かの叫ぶ声が聞こえたのは、その直後だった。"


    play music audio.impatience


    scene bg lion02 night large at zoom(1.5), align(0.3, 0.7)
    show fed sta nor ang rev up at std_c
    with wipe_lr


    voice get_voice_filename("fed")
    federico_unk1 "「なんだ！　せっかく雰囲気のあるカフェかと思えば、休みかよ！　電気がついてるくせによ」"

    "扉越しでも何を言っているのかはっきりと聞こえた。それも、聞き覚えのある声だ。"

    "私は日記帳を閉じてカウンターの裏に隠すと、慎重に扉の外を覗いた。"

    "フェデリーコ・カルミナーティさんがそこにいた。"

    scene bg lion01 night
    show rnk paj arm ten at std_c
    with wipe_rl

    voice get_voice_filename("rnk")
    rinka "「どうして……」"

    "彼は海晴と話して、ひとつの決着をつけたはずではなかったのか。"

    "私は警戒心を強めつつ、彼の言葉に違和感を覚える。"

    "そもそも、私を呼んでいるわけではなさそうだ。"

    "発言からして、偶然ここに来たということだろう。そして店が閉まっているから悪態をついている。"

    "つい遠回りしていたが、難しく考えることはない。"

    scene bg lion02 night large at zoom(1.5), align(0.3, 0.7)
    show fed sta dar su1 up rev at std_c
    with wipe_lr

    voice get_voice_filename("fed")
    federico "「あれ、て、てめぇ……」"

    scene bg lion01 night with dissolve

    "どうやら、彼の方も私の存在に気がついたらしい。"

    "まさか私がこの店の店長代理を務めてはいるが、今はただ本を読もうとしていただけという事情など、まったく分からないだろう。"

    "彼は私を見て、何も言わずに驚いた顔を浮かべていた。"

    "私の方も黙っている彼に対して、何か声をかけることはしなかった。"

    "やがて彼は、口角をあげてにやりと笑った。"

    "その笑い方は何故か――誰かに似ている気がした。"









    $ set_info_location("18")


    stop music fadeout 2
    scene bg lion02 night with fade_longest
    play music audio.odette
    pause 1

    $ show_hud()

    "フェデリーコは、驚愕していた。"

    "偶然立ち寄ろうとした喫茶店の中に、彼がちんちくりんと称した選定の参加者、獅子舞凛火がいたからだ。"

    "彼とリンカが現実世界で会うのは、これが初めてだった。"

    "何の因果か、彼は最後の日にリンカと出会った。"

    "施錠されている喫茶店の中にいるということは、従業員か恐らくはこの上に住んでいる子供だろうと、彼は思っていた。"

    "だが彼にとってそれは多くの面倒事と同様で、どうでもいいことであった。"

    "それ以上にフェデリーコは、高揚していたのだ。"

    show fed sta nor pa3 at std_c with std_in

    voice get_voice_filename("fed")
    federico "「こいつは――！」"

    "獅子舞凛火は警戒心を強めた真剣な表情でフェデリーコを見据えていた。"

    "その瞳に、フェデリーコはあることを連想する。"

    "インドで見たアランの妹、アムリタの瞳。"

    "強い意志を孕んだその瞳は、目の前の少女と同質のものだったのだ。"

    "フェデリーコは、アランが妙にリンカを気に掛けると疑問に思ってはいたが、それは彼の≪未練≫とは無関係の事情だろうと思い込んでいた。"

    "だが、違う。"

    "彼は自分の発見がやがて確信に変わるのを感じていた。"

    "アラン・スコーピオンの≪未練≫はここにあったのだ。"

    $ add_character_cards("fed", ["12_regret"])

    show fed sta dar smi with std_change

    voice get_voice_filename("fed")
    federico "「ははは、はははは！」"

    "彼は高揚を通り越して、これまでの人生で感じたことのない喜びを得ていた。"

    "――勝利。"

    "最後の最後、彼はアランのカードを３枚揃えることができた。"

    "自分が勝ちたいと思った相手に対し、勝利を手にした。"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「どーもな、ちんちくりん」"

    hide fed with std_out

    "フェデリーコはライオン館へと入ることなく、その場を去っていった。"

    "状況をつかめていない凛火の疑問符を浮かべた表情だけが、そこに残されていた。"









    $ set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    show rnk paj arm ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「なんだったんだろう……」"

    "私が黙っていると、何故かフェデリーコさんはライオン館の前から去っていってしまった。"

    "一体どういう状況なのか、よく分からないままに。"

    "ただ彼は、とても嬉しそうな顔を浮かべていた。"

    show rnk paj nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと、色んな意味で怖かった」"

    "怒りから驚き、そして喜びという彼の表情の変化は、妙な怖さがあった。"

    "もっとも彼の喜びは私の情報を得ることができた、という風には見えなかった。"

    show rnk paj arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「今日はやめておこうかな……」"

    "万が一戻ってくる可能性もあるし、今日はこの日記帳を読むのはやめにする。"

    "もう少しで読み終わったというのに残念だが、私は自分の部屋に戻ることにした。"

    "そして間もなく始まる今夜の選定に向け、心の準備を始めるのだった。"

label sentei10:

    call set_replay








    python:
        set_info_date(7, 8, "sun")
        set_info_scene("168")
        set_info_time("lnight")
        set_info_location("07")


    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall
    pause 2
    scene bg fatalhall01 up large with dissolve
    pause 1

    $ show_hud()

    show dia sta fro nor big at std_c with std_in

    voice get_voice_filename("dia", 241)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "もう、この声を聞くのは10回目になる。"

    "女神パルカは、運命の大広間でそう言った。"

    "綺麗で高貴な声に、残酷さが含まれていることを私は知っている。"

    "その残酷さを、私も持っていることも知っている。"

    scene bg fatalhall01 up with dissolve

    show dia sta fro cl1 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「残り４名。さて、どなたがこの≪女神の選定≫で残るのでしょうか」"

    show fed sta dar smi ci at ci_r with ci_in

    voice get_voice_filename("fed", 364)
    federico "「あんたの入れ物になるんだったらよ、女の方がいいんじゃねぇか？」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシ男女差別はしませんわ」"

    show fed sta dar su1 ci with ci_change

    voice get_voice_filename("fed")
    federico "「おい。オレに酒臭そうって言ってたじゃねぇか」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら？　記憶にございませんわ」"

    show fed sta dar irr ci with ci_change

    voice get_voice_filename("fed")
    federico "「こいつは……！」"

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln", 394)
    alan "「――フン。もういいだろう」"

    show aln sta nor gen rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「いや、構わないか」"

    show fed sta dar ser ci with ci_change

    voice get_voice_filename("fed")
    federico "「なんだこいつ、笑ってやがる。気持ち悪いぜ」"

    "アランさんとフェデリーコさんは、女神パルカとよく喋る。"

    "割と最初の方から、彼ら、主にフェデリーコさんはよく喋っていたと思う。"

    "ああ、思えば。"

    "この光景も、今日が最後になるのだ。"

    "寂しいとは違う。ただ、虚しい。"

    "海晴がどんな気持ちなのかは分からない。"

    "でも、私と同じように何も言わないことは事実であった。"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「今夜の選定で、ついに２ケタの大台を迎えました。皆サマの運命がどう紡がれていくのか――ワタクシをどうか楽しませてくださいませ」"


    voice get_voice_filename("dia")
    parca "「それでは、今宵も選定を始めましょう。運命の大時計、廻りなさい」"

    "女神が不敵に笑うと、この空間の中心にある大時計の針が動き出す。"

    "Ⅰ番というのを、憎まずにはいられない。"

    "どんな時も、一番最初に宣言するのは私なのだから。"


    scene bg fatalhall01 up
    show dia sta fro sm2 ci at ci_c
    with dissolve_long

    voice get_voice_filename("dia")
    parca "「Ⅰ番サマ。いかがなさいますか？」"

    show rnk uni arm nor ci at ci_r with ci_in

    voice get_voice_filename("rnk", 1514)
    rinka "「私は――Ⅻ番を指名する」"

    "アランさんをしっかりと見て、私はそう言った。"

    "彼の命を、私は踏み台にする。"

    "どんな理由があれど、この事実は変わらない。受け止めることから、もう逃げる気はない。"

    "彼は穏やかに微笑んで、頷いた。"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「お次はⅡ番サマ。いかがなさいますか？」"

    show mhr uni nor ser rev ci at ci_l with ci_in

    voice get_voice_filename("mhr", 673)
    miharu "「ぼくはⅢ番を指名する」"

    "予定通りの展開だ。"

    "フェデリーコさんは満足そうな顔で嫌そうな顔が混ざった何とも言えない表情で、頷いていた。"

    "その余裕の凄さが、今なら分かる。"

    show dia sta fro gl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「さて、お次はⅢ番サマでございます」"

    hide rnk
    hide mhr
    show fed sta nor smi ci at ci_r
    with ci_swap

    voice get_voice_filename("fed")
    federico "「オレか？　オレは――アラン、てめーを指名するぜ！」"

    show dia sta fro fee ci with ci_change

    voice get_voice_filename("dia")
    parca "「あっ、もう。番号でお呼びなさってくださいな」"

    show fed sta nor nor ci with ci_change

    voice get_voice_filename("fed")
    federico "「いいじゃねぇか、どうせここにいる全員が全員の名前を知ってんだ。しかしまあ、ルールに従うよ。Ⅻ番。あんたを指名する」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「かしこまりましたわ」"

    "女神が頷いて、次に声をかける前に、アランさんは静かな口調で叫ぶ。"

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln")
    alan "「僕はフェデリーコ・カルミナーティを指名しよう」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「あ、貴方サマまでっ。ワタクシがお尋ねしてから、でございます。Ⅻ番サマ、いかがなさいますか？」"

    show aln sta nor irr rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「……フン。安い挑発に乗っただけだ。僕はⅢ番、君を指名しよう」"

    $ add_character_cards("aln", ["3_regret"])

    show dia sta fro cle ci with ci_change

    voice get_voice_filename("dia")
    parca "「承知いたしましたわ。もう、皆サマちゃんと決まりは守ってくださいませ」"

    scene bg fatalhall01 normal with dissolve

    "私とフェデリーコさんがアランさんを指名。"

    "海晴とアランさんがフェデリーコさんを指名。"

    "お互いに、指名が重複した形になる。"

    "この状態は、完全に予想外であった。"

    "フェデリーコさんがアランさんを重複してでも指名したいのは分かるが、カードを揃えているとは思っていなかった。"

    "アランさんに至っては、海晴がフェデリーコさんを指名しているのに、自分も指名する理由が分からない。"

    "私は軽い混乱状態であった。"

    "まさか重複指名で私たちを引かせようという作戦にも思えない。"

    "今の段階では、私が優先権の取得を躊躇わないことくらい分かっているはずだ。"

    scene bg fatalhall01 up with dissolve

    show rnk uni nor que ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「これは、どういう……」"

    show dia sta fro glo ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「おやおや、大混戦でございますわね。それでは、指名の重複について順番に処理を行いましょう」"

    show fed sta dar ser rev ci at ci_l with ci_in

    voice get_voice_filename("fed")
    federico "「ああ、頼むぜ。おいミハル。分かってるな？　オレはこのヤローにトドメを刺されるのはお断りだ」"

    show fed sta dar smi rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「てめーと一晩相手できなかったのは残念だが、せめて幕引きだけは相手してくれよ」"

    show dia sta fro fee ci with ci_change

    voice get_voice_filename("dia")
    parca "「ああっ、だからワタクシが進行いたしますから、勝手にお話ししないでくださいませっ！」"

    "困った様子の女神をよそに、フェデリーコさんは「よろしくな」と付け加えた。"

    "さらにはアランさんも、私に向けて話しかけてくる。"

    hide rnk
    show aln sta nor clo ci at ci_r
    with ci_swap

    voice get_voice_filename("aln")
    alan "「同感だ。彼は品がなくてね。彼に指名されて脱落させられたとなれば、アムリタの兄として恥ずかしい」"

    "私は無意識のうちに拳を握っていた。"

    "彼らの意図が、ようやく理解できた。それは意図というには、あまりに論理的ではないことだろう。"

    hide aln
    show mhr uni sco con ci at ci_r
    with ci_swap

    voice get_voice_filename("mhr")
    miharu "「くすっ。男ってホントバカ……とでも言って欲しいのかい？」"

    show fed sta dar phi rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「そういう趣味はねーが、ま、悪くない理解だ」"

    hide mhr
    show rnk uni arm lie ci at ci_r
    with ci_swap

    voice get_voice_filename("rnk")
    rinka "「アランさんまでそんな風に思うなんて、意外です」"

    hide fed
    show aln sta nor gen rev ci at ci_l
    with ci_swap

    voice get_voice_filename("aln")
    alan "「……そうか。だが、ただの兄に戻った僕は、こんなものだ」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「はい、ちゃんとワタクシの進行に従ってくださいませ！」"

    "珍しく、女神は声を張り上げて言った。"

    "ただ私には、彼女が怒っているようには思えない。この異常な状況を、交差する感情の連鎖を目の当たりにして高揚しているようにも思えるのだ。"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「それではまずは、Ⅰ番サマとⅢ番サマによる、Ⅻ番サマの指名についておうかがいいたします」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「ご存知の通り、ご自分のカードを１枚開けることで、指名の優先権を取得することができますわ。Ⅰ番サマは、どういたしますか？」"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「私は、自分の≪氏名≫を公開する」"

    hide aln
    show fed sta dar ser rev ci at ci_l
    with ci_swap

    voice get_voice_filename("fed")
    federico "「オレはオレの≪未練≫を公開してやる」"

    "はやるフェデリーコさんに何か言っている女神を無視して、私は目をつぶった。"

    "結果を見れば、彼に助けられたにもかかわらず、恩を仇で返すことになる。"

    "けれど、それでいい。"

    "私は自分の意志をもって、続く言葉を口にした。"

    show rnk uni nor nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「私は自分の≪死因≫も公開するよ」"

    show fed sta nor smi ci with ci_change

    voice get_voice_filename("fed")
    federico "「かかっ、これじゃあ形無しだ。オレはもう公開するモンがねーからな。譲るぜ、あいつを堕とす権利をよ」"

    show fed sta nor int rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「ヤローのカードを３枚集めた時点で、オレの勝ちだった。最後の答えをくれたあんたには、感謝くらいしてやるか」"

    show rnk uni arm sad ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「……そっか」"

    "ようやく、昨日の彼の表情の意味が分かった。"

    "アランさんの妹のことを、彼はどこかで知ったのだろう。"

    "自分では到底分からないが、きっとこの瞳は、本当に似ているに違いない。"

    "彼に感謝されても困ってしまう。"

    "私が何かしたわけではなく、あくまでフェデリーコさんが自分の力で手にしたものだろうから。"

    show dia sta nor nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「承知いたしました。それでは、次はⅡ番サマとⅫ番サマによるⅢ番サマの指名でございます」"

    hide fed
    hide rnk
    show aln sta nor irr rev ci at ci_l
    with ci_swap

    voice get_voice_filename("aln")
    alan "「……フン。ついぞ、君と顔を合わせることはなかったな」"

    show mhr uni sco cau ci at ci_r with ci_in

    voice get_voice_filename("mhr")
    miharu "「そうだね。でも、君は凛火を助けてくれたのだろう？　ならば、お礼は言わなければいけないね」"

    show aln sta nor tre rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「よしてくれ。そんな柄ではないことを、聞いているのだろう？」"

    show mhr uni sco con ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「女神。指名の優先権は、ぼくがもらおう。君はどうするんだい？」"

    show aln sta nor gen rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「僕はまだカードを３枚残しているが……今優先権を取って彼を指名したら、呪われそうだ。僕を呪うのは許容できるが、アムリタを呪われてはたまらない」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「ここで引こう。勝負は持ち越し……と言っておこうか。どうだい？　フェデリーコ・カルミナーティ？」"

    hide mhr
    show fed sta dar irr ci at ci_r
    with ci_swap

    voice get_voice_filename("fed")
    federico "「ちっ、納得いかないぜ。ここはお互いに勝ちってことでどうだい？」"

    show aln sta nor clo rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「――断る」"

    show fed sta nor pa1 ci with ci_change

    voice get_voice_filename("fed")
    federico "「なんでだよ！」"

    show dia sta fro fee ci with ci_change

    voice get_voice_filename("dia")
    parca "「もう、皆サマ！　勝手にお話ししないようにと、何度申し上げれば分かりますの？」"

    "いつまでも終わらなそうな会話を、女神の一声が終わらせた。"

    "そして、彼女は高らかに謳い上げる。ここに始まる、２つの終わりを――。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro smi big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それではこれより、Ⅰ番サマによるⅫ番サマの指名と、Ⅱ番サマによるⅢ番サマの指名を、順番に執り行いますわ」"

    "女神の言葉に続き、運命の大広間には地響きが鳴り始める。"

    "まずは私だ。"

    "足下の床が、上層へと浮かび上がっていく。"

    "目の前に立つ、アランさんと一緒に。"







    $ set_info_location("16")

    scene bg fatalhall02 normal with fade_long
    pause 2
    scene bg fatalhall02 up with dissolve

    show aln sta nor clo rev ci at ci_l with ci_in

    voice get_voice_filename("aln")
    alan "「フン」"

    "運命の広間の上層で、私はアランさんと向かい合っていた。"

    "彼は穏やかな顔を浮かべ、粛々と立っている。"

    show aln sta nor lee rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「今さら、君と語り合うこともあるまい。あの夜、僕は全て君に話した」"

    show rnk uni arm sad ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「……はい」"

    "アランさんの言うあの夜とは打って変わって、沈黙の時間が流れた。"

    "そしてそれを打ち破ったのは、女神の声。"

    show dia sta nor ama rev ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「おやおや、もうお話はよろしいのですか？　Ⅰ番サマは、もっと惜しまれるかと思っていましたのに」"

    show rnk uni arm nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「意外でしょ。みんな結構、意外な一面を持ってるんだよ」"

    show aln sta nor gen rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「……ああ」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「あらあら。けれども淀みなく進むことは、ワタクシにとってはよいことでもありますわ」"

    show dia sta nor sm2 rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでは、指名を始めていただきましょう」"


    play music audio.electing
    scene ecg senteirinka gentle with dissolve_long

    "女神がその言葉を言い終えてから、私はカードブックを開いた。"

    "私の所持するカードが、光を放って空中に現れる。この中で有効なカードも、随分と減ってしまった。"


    voice get_voice_filename("rnk")
    rinka "「氏名――アラン・スコーピオン。死因――毒死」"


    scene bg fatalhall02 up
    show aln sta nor tre rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("aln")
    alan "「宝石商として、君の所得では一生買えないようなダイヤでも贈ればよかったと後悔している」"

    show rnk uni nor que ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「……ここで嫌味？」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「代わりに、魔法の言葉を教えよう。僕は僕の亡き後、アムリタが社長を務めていると信じている」"

    show aln sta nor gen rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「いつか宝石が必要になる時が君にも来るだろう。その時に格安で買える魔法の言葉さ」"

    "アランさんは自分で先に笑ってから、続きを言った。"

    show aln sta nor tre rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「アムは13歳の８月までおねしょをしていた――これをアムリタに伝えれば、君はどんな宝石も手に入れることができる」"

    show rnk uni arm lie ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「何それ」"

    "私もつい、微笑んでいた。"

    "私が思っている以上に、この人は妹想いだ。兄バカだ。"

    "だからちょっと、アムリタさんが羨ましい。"

    show aln sta nor gen rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「こう爽やかならば、指名される側も悪い気分ではない。そろそろ、最後の言葉を告げてくれ」"

    scene ecg senteirinka gentle with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「……うん。未練――妹の、将来」"

    scene ecg trianglecard small with dissolve

    "私の言葉に呼応して、３枚のカードはさらに強い光を放ちながら、この大広間の中心部へと移動し始めた。"

    show ecg trianglecard cover with ecg_change_wait

    "そしてやがて、視界が見えなくなるほどに白い光が空間を覆いつくしたとき、最期の言葉が聞こえた。"


    voice get_voice_filename("aln")
    alan "「フン。しかし君たちに宝石は不要だったか。その瞳に、何よりも輝かしい光を持っていた」"







    stop music fadeout 2
    scene white with Dissolve(3)
    play music audio.death
    pause 2

    scene black with dissolve_longest

    "どこかのホテルだろう。"

    "そこで、彼は資料に目を通していた。"

    "紙の資料とパソコンに映された資料、タブレットに映された資料と、たくさんの文字が並んでいた。"

    "ホテルに、ルームサービスが運ばれてくる。"

    "それは、眠気覚ましのコーヒーだった。アランにコーヒーを飲む習慣はないが、秘書に勧められたのであった。"

    "ここのコーヒーは美味しい、と。"

    "彼はデスクに置いたコーヒーに、口をつける。"

    "身体の自由が利かなくなったのは、その直後のことであった。"

    "彼はその時、すぐに気が付いた。"

    "どこまでの人間が手を組んで自分を貶めたのか、すぐに分かった。"

    "だが、それを糾弾する命は、もう残されてはいなかった。"

    "そして、思う。"

    "あらゆるものを切り捨ててきた自分の終わりとしては、呆気なく終わるのが相応しいのかもしれないと。"

    "唯一、後悔したことがあった。"

    scene ecg amrita hid with dissolve_long

    "最愛の妹に、もう半年も会っていないこと。"

    "半年もあれば、子供の成長は著しい。"

    "少しでも大人に近付いた妹を見たかったと、彼は悔いるのであった。"






    scene bg fatalhall02 normal with fade_longest
    pause 1

    "私の意識は、体感５分ほどで現実世界へと戻ってきた。"

    "驚きはなかった。"

    "それは、アランさんから聞いた情報とほとんど同じものだったから。"

    "だが、冷たさがあった。あんなに優しい人なのに――どうして、理解されなかったのだろう。"

    scene bg fatalhall02 up with dissolve

    show rnk uni nor ama ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「これはさ、あなたにも見えてるの？」"

    show dia sta nor ama rev ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「残念ながら。記憶はワタクシの担当外ですから」"

    show rnk uni nor que ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「……どういうこと？」"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでは、Ⅻ番サマの持っていたカードを貴方にお教えいたします。どのカードを取得するか、お選びくださいませ」"

    show rnk uni arm ang ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと待ってよ！」"

    hide dia with ci_out

    "私の制止など聞かず、女神はまたどこかへ消え去ってしまった。"

    "そして私の立っていた床が振動し、下層へと下りていく。"








    python:
        set_info_scene("169")
        set_info_location("07")

    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall
    pause 1

    "海晴がしばらく待っていると、獅子舞凛火だけが上層から戻ってきた。"

    "言葉は交わさず、海晴は彼女と目を合わせて、頷く。"

    "それだけで、彼女たちには十分だった。"

    "海晴の乗った床が、動き出す。"

    "左隣の床に立つ、フェデリーコ・カルミナーティとともに。"







    $ set_info_location("16")

    scene bg fatalhall02 up with fade_long
    pause 1

    "上層へ行くと、二人は向かい合う格好となった。"

    "あらためて向き会う海晴とフェデリーコ。"

    "先に口を開いたのは、フェデリーコの方だった。"

    show fed sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("fed")
    federico "「なあ、最後にあんたに聞いておきたいことがあるんだ」"

    show mhr uni sco cau ci at ci_r with ci_in

    voice get_voice_filename("mhr")
    miharu "「なんだい？」"

    show fed sta nor int rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「あんたさ、レズなのかい？　あのちんちくりんが好きなんだろ？」"

    "フェデリーコの言葉は、海晴の予想とは完全に違う方向のものだった。"

    "海晴は怒りたいと思ったが、はっきりと言葉にされてしまった恥ずかしさで赤面し、うまく話すことができなかった。"

    show fed sta dar smi rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「ま、どうでもいいか。どっちにしろオレはこれで終わりだ」"

    show mhr uni pai irr ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「君は別れ際に自分の顔に泥を塗るのが趣味なのかい？」"

    show fed sta nor phi rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「恥じるこたあないだろ。人それぞれだ。同性愛ってのはオレは理解できないが、いておかしいとも思わない」"

    show fed sta nor smi rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「むしろ、それならそうと早く言ってくれれば、別の遊び方を教えてやれたのによ」"

    "フェデリーコが軽口で言うと、海晴は彼に呆れた冷たい視線を浴びせる。"

    "しかし、その冷たい視線は彼の軽口とほとんど同じ意味だった。"

    show mhr uni sco cau ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「話はそれで終わりかい？」"

    show dia sta nor ama rev ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「もう少しだけならば、お話しても構いませんわよ？」"

    show fed sta dar phi rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「いや、いいぜ。もう話すこともないだろ？」"

    show mhr uni sco con ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「……そうだね」"

    "いつの間にか現れた女神に対し、二人は平然と対応していた。"

    "そのことにいささか不満そうな顔を浮かべながら、女神は続ける。"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「それではⅡ番サマ。カードをお選びくださいな」"


    play music audio.electing
    scene ecg senteimiharu ser with dissolve_long

    "海晴は女神に促され、カードブックを開く。"


    voice get_voice_filename("mhr")
    miharu "「氏名――フェデリーコ・カルミナーティ」"


    scene bg fatalhall02 up
    show fed sta dar ser rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("fed")
    federico "「そうだ。オレのことじゃないが、一応言っておかなくちゃならないことがあったな」"

    show fed sta dar phi rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「あのゴリラ女。あいつはそれなりに大変な人生を歩みながらも、楽しむことを忘れてなかった。最後はオレなんかを庇って、助かる命を捨てちまった。オレも死んじまったしな」"

    show fed sta dar ser rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「何が言いたいかってぇと、そうだな。あいつやオレみたいな奴でも生きてたってことを覚えていてくれ」"

    show fed sta nor smi rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「楽しむか、楽しまないかだ。もう自殺なんてすんじゃねーぞ」"

    scene ecg senteimiharu ser with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「死因――圧死」"


    scene bg fatalhall02 up
    show fed sta dar smi rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("fed")
    federico "「前回の選定で、女神は運命を変えることができるって言ったんだ。もしあんたやちんちくりんが選定に勝利したら、存分に使っちまえ」"

    show fed sta dar ser rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「あんたはもっと、欲望に忠実になった方がいい。綺麗でなくっていい。元々、十分過ぎるほど綺麗なんだからよ」"

    scene ecg senteimiharu bea with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「未練――勝利」"

    "海晴は唇を噛んでいた。"

    "それがどんな感情の表れなのか、海晴自身も分からない。"

    scene ecg trianglecard small with dissolve_long


    voice get_voice_filename("fed")
    federico "「あんたの恋に勝利が待ってることを、どっかで祈っておいてやるよ」"

    show ecg trianglecard cover with ecg_change_wait

    "そして３枚のカードが光を放ち、運命の大広間を覆いつくすのであった。"






    stop music fadeout 2
    scene white with Dissolve(3)
    play music audio.death
    pause 2

    scene black with dissolve_longest

    "襲撃を受け撃沈寸前の、船。"

    "目の前にはこの船の船長である女性が力を失い、自分の方へと倒れ込んでいた。"

    "彼女と彼の肉体がぶつかるのは、その直後であった。"

    scene ecg ontheship c with dissolve

    "同時に、船を構成するあらゆるものが崩壊し、彼のことを押し潰した。"

    "彼はまた負けかと、何かを恨みながら命を失った。"







    scene bg fatalhall02 up with dissolve_longest
    pause 1

    show mhr uni pai lie ci at ci_r with ci_in

    voice get_voice_filename("mhr")
    miharu "「……余計なお世話だ。君に祈られるのは、疫病神に憑かれるようなものだろう？」"

    show dia sta fro cl1 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「嘘をつくのはいけませんわよ、海晴サマ？」"

    show mhr uni nor ser ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「やめてくれ。ぼくをそう呼んでいいのは、ぼくが君の器だった頃の話だろう？」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「くすっ。そうでしたかしら？」"

    show mhr uni sco thi ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「――待ってくれ。今まで君はぼくを通じてこの世界を見てきた。だが、君はぼくの体を通すことでしか世界を見ることができない」"

    show mhr uni nor ser ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「君は今日まで、どうやって現実世界を俯瞰してきた？」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「{rb}下層{/rb}{rt}した{/rt}では、お友達がお待ちですわよ」"

    "女神は答えることなく、海晴の足下の床が動き始めた。"

    "海晴は感じていた。"

    "あとたった数歩で――どこかへ届くと。"









    $ set_info_location("07")


    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall
    pause 1

    "選定が終わり、上層からは海晴だけが戻ってきた。"

    "私の横に、海晴は再び立つことになった。"

    "そして、私たち二人と女神を除き、この≪運命の大広間≫には誰もいなくなった。"

    "元々果てのないはずのこの空間を、より広く感じていた。"

    scene bg fatalhall01 up with dissolve

    show dia sta fro gl2 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「さあ、ご苦労様でしたわ。取得するカードは、もうお決まりになりましたか？」"

    show rnk uni nor nor ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「って、言ってもね。なら私は、≪Ⅵ・氏名≫にしようかな」"

    $ add_character_cards("rnk", ["6_name"])

    "アランさんに最初に指名された女性だ。"

    "名前は知らないし会ったこともないはずだが、これで、彼女のことを胸に刻むことができる。"

    show mhr uni nor rea rev ci at ci_l with ci_in

    voice get_voice_filename("mhr")
    miharu "「凛火にならって、ぼくは≪Ⅶ・氏名≫をもらおう」"

    "海晴も私の意図を理解してくれたのだろう。２回目の選定でオデットさんが指名した男性のカードだ。"

    "後で、海晴にその人の名前を聞こう。そうすれば、私は全ての参加者の名前を知ることができる。"

    "この胸に刻むことができる。"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「おやおや。どうやらもう、おふたりのカードは不要なようですわね」"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「……どうだか」"

    show mhr uni nor ser rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「さあ、早く選定の終わりを告げてくれ。少しでもゆっくり眠りたい」"

    show dia sta nor nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「はいはい、分かりましたわ」"

    hide dia with ci_out

    "気だるげに言い、女神は大広間の中心へと戻っていった。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro sm2 big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者は２名。これをもって、選定を終了といたしましょう」"

    "彼女にいい感情を持てなくても、その声だけは綺麗だと思う。"

    "女神の選定。"

    "その残酷な儀式は、間違いなく、間もなく終わりを迎えるだろう。"

    $ renpy.end_replay()
    $ add_seen_chapter("10-7")

    $ persistent.sentei10_clear = True
    $ grant_achievement("divine_selection_10")

    jump f011_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

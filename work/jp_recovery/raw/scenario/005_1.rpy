

label f005_1:












    python:
        set_info_scene("49")
        set_info_date(5, 28, "mon")
        set_info_time("morning")
        set_info_location("23")


    stop music fadeout 2
    scene bg hotel japan with fade_longest
    play music audio.badguys
    pause 1

    $ show_hud()

    "ホテルでオデットと合流した時、オレは夢の世界で見た光景での興奮が抑えきれていなかった。"

    show fed sta nor nor at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「なあ、あいつら見たか？　ⅠとⅡのガキ。仲間割れしてたぜ？」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「ああいうのはなんか、ゾクゾクするもんがあるよな」"

    "オレが言うと、オデットは心底面倒くさそうな声で答えた。"

    show ode sta arm irr rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「ったく、朝からうるせえ奴だな。んなことより朝飯だ。ここのホテルのバイキングにはもう飽きちまったが、味は悪くねえからな」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「――ったく。今後あいつらを脱落させにいくときに、役に立ってくるかもしれないだろ？」"

    "言いかけて、オレはオデットが不機嫌であることに気付いた。"

    "ガキ同士が見せる汚い争いに興奮して、昨日の選定であったことをすっかり忘れていたのだ。"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「あたしを出し抜いたんだ……ミハルってのは侮れねぇ」"

    "だが明らかに不機嫌ではあるのだが、オデットの声はどこか楽しそうでもあった。"

    show ode sta gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「くく……面白くなってきたぜ」"

    "ロシアのガキの時といい、こいつの感情と行動パターンは相変わらず読めない。"

    "だが一つ言えるのは、面白さを感じているのはオレも同じということだった。"











    python:
        set_info_scene("50")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "思えば、一人で目を覚ますのは数日ぶりだった。"

    "目が乾いている。"

    "寝ている間に、また泣いてしまっていたのかもしれない。"

    show rnk paj arm sad up at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「本当に弱いな、私は……」"

    "ソーニャと過ごした数日間は、私にとっても楽しいものだった。"

    "緊迫した選定の期間の中で、彼女との時間は一種の清涼剤のように思える。"

    "こみ上げてくる想いを噛み締めて、私は机の上に置いたカードブックを手に取った。"

    "昨晩の選定で生成されたカード。"

    "それは、海晴がソーニャの指名の優先権を得るために全員に開示した情報だった。"

    "{rb}蛇鉈{/rb}{rt}へびなた{/rt}海晴。"

    "それが、海晴の氏名カードの内容だった。"

    "その苗字に聞き覚えはない。だが海晴の家庭環境を考えれば、何があったかの想像はつく。"

    "そしてもう一つ、海晴は昨晩の選定で私の≪死因≫を手に入れた。"

    "私自身もまだ知らない、私の情報だ。"

    "あの時、動揺する私に海晴は冷たい態度をとった。"

    "だが、その言葉の内容が気になっていた。"

    "今はもう、君と話すことは何もない――というその言葉が。"

    show rnk paj arm vig up with std_change

    voice get_voice_filename("rnk")
    rinka "「そういうことだよね、海晴――」"

    "私は呟いてから、学校へ行く仕度を始めた。"





    stop music fadeout 1
    scene bg myroom morning with fade_long
    pause 1

    "テレビをつけっぱなしにして準備をしていると、気になるニュースが耳に入ってきた。"

    "――渋谷駅付近で、山手線の車内に不審物が持ち込まれたらしい。網棚に不自然に大きなリュックが置かれていたとか何とか……。"

    "――ただし、それはどうやら空のリュックだったようだ。テロの疑いもあり警察騒ぎになったが、結局何もなかったらしい。"

    "まさか選定の参加者と関係があるのかとも思ったが、ニュースを見る限り関係性は見つからなかった。"

    show rnk paj arm imp at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……痛っ」"

    "そのニュースを聞いているうち、頭痛が走った。"

    "自分の体にも心にも、疲労とストレスが溜まっている。"

    "ニュースを見て、ついテロの現場などを想像してしまったからだろう。"

    "電車が遅れているらしいので早めに出られるよう、私は準備を急ぐことに決めた。"








    $ set_info_location("14")

    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show nom uni har sur rev at std_l with std_in

    voice get_voice_filename("nom")
    naomi "「あ、先輩っ」"

    "校門まで来たとき、直未の姿を見かけた。"

    "普段は直未の方が早く登校しているので会わないが、電車が遅れていたのでタイミングが重なったのだろう。"

    "先に気付いたのは直未で、校舎に向けていた体をくるりと私の方へと向け直した。"

    show nom uni fal sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「わとっ」"

    "焦って動いたからか、直未はバランスを崩した。"

    show rnk uni cat sma behind nom at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「ち、ちょっと！」"

    "私は直未の手をとって、体を支える。"

    "直未が転ぶところを見るのは久し振りだ――そもそも直未と会うこと自体がずいぶんと久し振りな気がする。"

    show nom uni hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「あははは……すみません……」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「もう、大丈夫？」"

    "直未は体勢を整えてから、はにかんだ。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「どう？　文化祭の準備は進んでる？」"

    show nom uni nor nor rev with std_change

    voice get_voice_filename("nom")
    naomi "「そこそこ……って感じです。まだ内装の飾りつけとかをどうするか、全然決まってなくて……」"

    show nom uni nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、でも、コーヒーはばっちりですよ！　最優先でみんなに教えています」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「……よかった。元気そうで。文化祭はもう来週だから……あっという間だね」"

    "私のクラスは、今どうなっているのだろうか。"

    "当日何かしらの手伝いくらいはするかもしれないが、状況は全然聞いていないので分からなかった。"

    show nom uni hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「先輩は……その……」"

    "直未が言いかけたところで、後ろから「やあ」と声をかけられた。"

    show mhr uni nor rea at std_r with std_change

    voice get_voice_filename("mhr")
    miharu "「おはよう凛火……と日辻さん」"

    "どうやら、海晴も丁度登校してきたところらしい。"

    "髪の毛をさらりと風になびかせていた。"

    "昨晩、夢の世界で言ったことなどなかったかのように、海晴は普段通りに声をかけてきた。"

    "直未もいるので、私も普通でいるようにした。"

    show nom uni nor sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「未島先輩……。あ、じゃあそろそろわたし、行きますね。チャイム鳴りそうですし」"

    hide nom with std_out

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、私たちも……」"

    "私の言葉を待たずに、直未は校舎の方へと歩いて行った。"

    show mhr uni sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「……ぼくはやはり、避けられているみたいだね」"

    "答えにくいことを、海晴の方から言われてしまった。"

    "私がどう答えようか考えていると、海晴が先に言葉を続けた。"

    show mhr uni sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「まあ、仕方ない。元々原因を作ったのはぼくの方だってことは、分かっているよ」"

    show rnk uni sur su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「え！　直未と何かあったの？」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。大丈夫。大したことではないよ。さあ、ぼくたちも教室へ行こう。遅刻ぎりぎり」"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと待って。あのさ、昨日のことだけど……」"

    show mhr uni sco con with std_change

    voice get_voice_filename("mhr")
    miharu "「うまく話題を逸らしたつもりだったんだけどね。放課後バイトが終わったら、ぼくからライオン館へ行くよ。それでいいかい？」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「話を逸らすっていうの、嘘。海晴、元々そのつもりだったんでしょ？」"

    "私がため息混じりに言うと、海晴は微笑んだ。つまり、それが答えだ。"

    "ちゃんと話したがっていることを、海晴は分かっていた。"

    "その後人の流れに逆らわず、私たちは校舎へ向かった。"







    python:
        set_info_time("noon")
        set_info_location("08")

    scene bg schoolroom noon with fade_long
    pause 1

    $ show_hud()

    show mao uni sel glo rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「さあさありーたん、お昼ご飯の時間だよぉ～」"

    "昼休みのチャイムが鳴った直後、真央が私の机までやって来た。"

    show mao uni nor dis rev with std_change

    voice get_voice_filename("mao")
    mao "「今朝は朝ごはんを食べてなかったから、お腹が空いてもう限界……」"

    show rnk uni arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「朝ごはん食べてないのはいつもでしょ……じゃあ海晴にも声を」"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「んにゃ。みはるんは今日、奨学金の説明か何かで先生のところに行かなくちゃいけないんだってー」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「って、さっき先生がみはるんのこと呼んでたの聞いてなかったかー」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、そういえば先生に呼ばれてたような……」"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんは相変わらず、変なところで抜けてるなぁ」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「ま、なので今日は二人だよぉ～」"

    "真央に手を引かれ、私たちは購買へ向かった。"







    $ set_info_location("15")

    scene bg schoolrooftop noon with fade

    show mao uni nor que rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「りーたん、今日はパンじゃないんだねぇ」"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あー、なんとなく。真央もだね」"

    show mao uni nor sle rev with std_change

    voice get_voice_filename("mao")
    mao "「うちは、りーたんがご飯系にしたから合わせたのだよ」"

    "真央が買ったのは、購買のから揚げ弁当だった。私が買ったのは、今日はカレーだ。"

    "普段は屋上まで持ち運ぶということもあり、あまり選ばないメニューだ。"

    "ほとんど無意識だったけれど、今日は味の濃いものが食べたいと思っていた気がする。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんは辛いの苦手だと思ってたけど、カレーなんだねぇ」"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、辛いのも甘いのも好きだよ。極端に辛かったりやたら甘かったりするのが好きじゃないだけ」"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「うんうん、知ってたよ」"

    "わざとらしく何度も頷く真央を見て、私は呆れた笑いを浮かべた。"

    "真央と話しているとご飯を食べ始めるタイミングを見失ってしまいそうなので、私はここでカレーのビニールパックをとった。"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「にははははは、疲れてるんだねぇ、りーたんも」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「どうしたの、急に」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「いや、だってスプーン忘れてるからさ～」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「…………あ」"

    "購買では、割りばしやスプーンはセルフサービスで持って行くことになっているのだが、すっかり忘れていた。"

    "手元にあったのは、おしぼりのみ。"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「では、そのおしぼりとこれを交換したげよう」"

    "真央はビニールの影に隠していたプラスチックのスプーンをさっと取り出し、手渡してきた。"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「さて、真央様と呼びなさい」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「どうもありがとう、真央様」"

    show mao uni sel mor rev with std_change

    voice get_voice_filename("mao")
    mao "「うぬぬ……こうも平然と言われると面白味がないというか……」"

    "どうやら私は真央の予定とは違う反応をしたらしい。私が渋るのを見てからかおうとしたのだろう。"

    "それが分かっていたから、あえてあっさりと言った。"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「本場のインドカレーみたいに手で食べることになっちゃうとこだったねぇ」"

    "インドという言葉で、スコーピオンさんのことが一瞬浮かんだ。"

    "過敏かとも思ったが、あまり洒落にならない真央の冗談に、私は苦笑いを浮かべるだけだった。"

    "こうして、真央と他愛ない会話をしながら昼休みを過ごしていた。"

    "ほとんど食べ終わったところで、真央は突然に話題を切り出した。"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「そういやさ、りーたんは気付いてないかもしれないけど、ここ最近、なおりんはずっとりーたんのこと気にしてるよ？」"

    "私がどういうことか聞き返すと、真央は「いやあ」と勿体ぶってから続ける。"

    show mao uni nor glo rev with std_change

    voice get_voice_filename("mao")
    mao "「あれは完全に恋する乙女の瞳ですな」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「馬鹿。そういう言い方は直未に失礼でしょ」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「いやあ、まあいいんだけどさ、最近なおりんほったらかしにされて寂しそうだよ～？」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「ほったらかしって……。直未も文化祭の準備で忙しいって言ってたからさ」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「みはるんに比べればなおりんは我慢しちゃう子だからねぇ」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「ともかくさ、りーたん自身が最近ずーっと疲れちゃってるからさ、ちょっとは休んだ方がいいよ？」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんが元気ないと、基本的にうちらみーんな元気なくなるしねぇ」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんが今どれくらい元気がないかって言うと、スプーンを忘れるだけじゃなくて、カレーを食べながら口の周りを汚しちゃうくらい」"

    "真央は私がさっきスプーンと交換したおしぼりを開けて、私の方に手渡してきた。"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「ほれ。おしぼりあげるから真央様と呼びなさい」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「真央様」"

    show mao uni sel mor rev with std_change

    voice get_voice_filename("mao")
    mao "「くっ、またか……」"

    "拭いてみると、確かに左の方にカレーがついていたようだ。"

    "真央が言う通りだ。"

    "きっと私は、疲れている。"

    "だが、私が心から休める日なんて、しばらくは来ないだろう。"

    "だって――。"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ま、とは言ってもりーたんには真央様のどんなアドバイスも無駄無駄無駄なのは分かっておるよ」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……あんたね」"

    "真央は食べ終わったゴミをビニール袋にまとめると、ぴょん、と勢いよく立ち上がった。"

    show mao uni nor glo rev with std_change

    voice get_voice_filename("mao")
    mao "「だからせめて、りーたんの好きなようにすればいいさ」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「……ありがと」"


    "真央の言葉は、単純に嬉しかった。"

    "選定のことなんて、何も知らないに決まっている。海晴が真央に話すはずはない。"

    "それでいいのだ。"

    "だからこそ、真央の言葉を聞くと安心する。"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「んじゃ、これ捨てといてねん。うちはみはるんのとこ遊びに行ってくる～」"

    hide mao with std_out

    "まとめたゴミを私に渡すと、真央は屋上から去って行った。"

    "私はまず、少しだけ残ったお弁当を完食することにした。"






    python:
        set_info_scene("51")
        set_info_time("evening")
        set_info_location("14")

    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    pause 1

    $ show_hud()

    "授業も終わり、私は帰宅しようと思って校門へ向かった。"

    "ふと見ると、直未が下を向いたまま、校門の塀に寄りかかっていた。直未は私に気付いていないらしいので、私の方から「どうしたの？」と声をかける。"


    play music audio.naomi

    show nom uni hes shy rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「あ、先輩……。実は、先輩を待ってたんです」"

    show rnk uni nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「私を？　あれ、文化祭の準備はいいの？」"

    show nom uni hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい。今朝飾り付けがまだって話をしてたと思うんですけど、小物とか全然決まっていなくって……」"

    show nom uni hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「カップとソーサーをたくさん揃えると予算オーバーなので、紙コップなんですけど、せめてコースターとかマドラーとかお砂糖入れとかは可愛いのがいいって」"

    show nom uni hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「……それで、もしお時間あれば……買い物に付き合ってくれませんか？」"

    "予算面もそうだが、人手も足りないだろうし、カップを一々洗うのは大変だろう。"

    "それに衛生的にも、学園祭ならば使い捨ての方が安全だ。"

    "私がよく行く店に、使い捨てのコースターなど可愛い商品が置いてあるところがある。"

    "海晴との約束は夜だし、あまり遅くなり過ぎなければお店も大丈夫だろう。"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。大丈夫だよ。でもそれくらいならメッセージで教えてくれればよかったのに」"

    show nom uni hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「事前に言ったら、先輩に予定を空けさせちゃうんじゃないかなーって思ったので……本当に時間があれば、でいいですから……」"

    "直未は目を逸らしてそう言った。"

    "気を遣わせてしまっているのは私が原因なので、直未の言葉を否定することもできない。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「もう、気にしなくていいのに。じゃ、行こうか。とりあえず渋谷に知ってるお店があるから、そこから見てみよう」"

    show nom uni nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい！　ありがとうございます！」"

    "言って、私たちは駅へ向かった。"






    $ set_info_location("02")


    play music audio.nichijo03
    scene bg station01 with fade

    "渋谷で買い物を終えた私たちは再び電車に乗り、家路についた。"

    "乗り換えのため、新宿駅で電車が来るのを待っている。"

    show nom uni nor smi rev at std_cr, xoffset(-150) with std_in

    voice get_voice_filename("nom")
    naomi "「ありがとうございます！　さすが先輩ですね、可愛いのがたくさん買えました」"

    show rnk uni nor smi at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「うん、ならよかった」"

    "一応今日は下見で、直未の気になったものを３種類ずつ購入していた。"

    "その中から、みんなで最終的に使うものを選ぶらしい。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「でも直未は偉いね。リーダーって感じ？」"

    show nom uni hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「いえ……。ただわたし以外に仕切る人がいないから、流れでわたしがリーダーみたいになっているだけです」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「そういうところが偉いねってことだよ」"

    "直未は恥ずかしそうに顔を赤らめて、目を逸らす。"

    "話を聞いている限りでは、私と違ってちゃんとクラスメイトと仲良くしているようだ。"

    "きっと、文化祭の出し物を主導しているのが大きく影響しているのだろう。"

    "出会ってすぐの私を怖がっていた時期と比べると、ずいぶん成長したんだな、と思う。"

    "そういう意味では、私とは正反対だ。"

    "電車に乗ろうとしたところで、直未は急に真剣な目を見せる。"

    "そして、私に耳打ちをした。"


    play music audio.gimon

    show nom uni nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「……先輩、あの人」"

    show yuu sta eml war rev at std_l with std_in

    "直未は自分の体で手を隠しつつ、遠くに見える人影を指差した。"

    hide yuu with std_out

    show nom uni nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「あの……銀の髪の……」"

    $ gameinfo_cardbook_yuu_unlocked = True

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「えっと……銀……銀……あっ！」"

    "私はその姿を見て、ぴくり、と肩を強張らせた。"

    "電車は、まだ来ない――。"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「直未、先帰ってて」"

    show nom uni har pal rev with std_change

    voice get_voice_filename("nom")
    naomi "「待ってください。先輩がそんなに焦るってことは……あの子、選定の参加者なんですよね？　確か、子供が２人混ざっていたって言ってました」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん」"

    "子供といえば、ⅣとⅩの位置の２人。ソーニャは脱落してしまったから、今はⅣの子供のことだ。"

    "私はあの子の≪死因≫のカードを持っているが、他の情報はまだ何もない。完全にノーマークだった。"

    "まさかこんなところで会うなんて――いや、この考え方は間違っているかもしれない。"

    "ソーニャやスコーピオンさんたちも新宿周辺に来ていたということは、何らかの理由があるに違いない。"

    "私が忘れている記憶――死因、そして最初に女神に会い、選定の説明を受けた時に聞いていた、何かのはずだ。"

    "しかし、それを今考えても仕方がない。"

    show nom uni hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「――ぱい、聞いてますか？」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめん。ちょっとあの子のことを考えてた……ってあれ、そういえばどうして直未があの女の子を知ってるの？」"

    show nom uni hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「どこかで見たことがあるような気がして……。でも、そんなはずはないですよね」"

    show nom uni que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「先輩から聞いていた情報から、何となく想像していたんですかね……？　って、あれ……あの子、男の子じゃないですか？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「男の子……かなぁ？　華奢だし、顔も女の子っぽいけど……。あれ、この会話をどこかでしたような……」"

    show nom uni hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、わたしが言いたかったのはそうじゃなくて……」"

    show nom uni nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「向こうはまだ、こちらに気付いていないみたいです。だったら、後をつけた方が――いいと思います」"

    "直未は表情を変え、真剣な声で言った。"

    show nom uni hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「少しでも情報を持っておいた方が……いいかと……あっ、ごめんなさい……。わたし、余計なことを……」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ううん、ありがとう。私もそのつもりだったから」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、一人で行く。だからさっき先帰ってって言ったんだ。ごめんね、言葉足らずで」"

    "直未は下を向いて何かを考えるように目をつぶってしばらくすると、ゆっくりと頷いた。"

    show nom uni har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい……。危険があるのは、分かっていますから。でも、もし写真を撮ったりして、それを元に家での調べ物とかがあれば……わたし……いつでも先輩の協力をします。させてください」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「気持ちだけでも、すごく嬉しいよ。ありがとう」"

    show nom uni nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「……はい。気を付けて、ください」"

    hide nom with std_out

    "私はしっかりと頷いて、直未に別れを告げる。"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめんね、直未……」"

    "一人になってから、私は小さな声で呟いた。"

    "そして、少女の姿を見失わないように、早足で追いかけた。"








    python:
        set_info_scene("52")
        set_info_time("evening")
        set_info_location("24")

    stop music fadeout 1
    scene bg shigetsugu01 noon with fade_long
    play music audio.investigation
    pause 1

    $ show_hud()

    "私は少女を追いかけて、結局30分程度は歩いていた。"

    "新宿駅から中央線沿いに歩いたとある住宅街の中にいる。"

    "少女の足取りは慣れていることから、きっと家が近くにあるのだろう。"

    "日本人には見えないが、この辺りにホテルはない。ソーニャのように家族で日本に来たわけではないだろう。"

    "となると、元々住んでいたということだろうか。"

    "この地域は外国人も多いから、珍しくはない。"

    show rnk uni arm ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あっ、あの家だ」"

    "少女はとある民家の前で足を止め、家の中に入って行った。"

    "かなり昔からありそうな家だ。この辺りは古い建物が多いが、その中でも一際歴史を感じる。"

    "大きな地震があったら崩れてしまいそうなほど、ボロボロだった。"

    "人を尾行したことはなかったけれど、恐らく気付かれてはいないと思う。"

    "だがこれ以上踏み込むこともないだろうと思い、私は少女が家に入ったのを確認してから入り口の表札を見た。"

    "ところどころ字は欠けていたが、判別できないほどではない。"

    "――牛塚。"

    "この家の住人の苗字は、{rb}牛塚{/rb}{rt}うしづか{/rt}というらしい。"

    "あの子の名前――なのだろうか。"

    "だが、そうも思えない。"

    "空き家をホテル代わりに使っているという可能性もある。"

    "隣家の塀の陰から、聞き耳を立ててみる。"

    "壁が薄いせいだろう、内容は分からないが、話し声だけは聞こえてくる。"

    "少なくとも２人以上いるらしい。"

    "一人は恐らくあの少女で、もう一人はおじいさんの声だった。"

    "おじいさんは、元から住んでいた人だろうか。となると、少女がこの家に居候しているという方が可能性が高い。"

    "カードブックは、選定の参加者以外との会話にも効果を発揮するのだろうか。"

    "まだちゃんとは検証していなかったが、自分が選定の参加者であることを自覚する前にライオン館へ訪れた観光客と英語で会話できていたことから、機能すると考えていいだろう。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「そろそろ、戻ろう……」"

    hide rnk with std_out

    "話している内容も分からないし、私は住所を控えて戻ることに決めた。"

    "その時、偶然通りかかった女性に話しかけられた。"

    "40代前半といったところだろうか。スーパーのビニール袋を持っていることから、夕飯の買い物をした帰りだろう。"




    voice get_voice_filename("other")
    other_female_1 "「あら、牛塚さんに用事かしら？」"

    show rnk uni arm ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「い、いえ……」"

    "いきなり声をかけられて驚いたが、近所の人ということは、あの少女についても何か知っているかもしれない。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「この家って、昔から外国人の子供が住んでいたんですか？」"




    voice get_voice_filename("other")
    other_female_1 "「あら、あなたも気になる？」"

    "私の質問を聞くと、女性はにやりとした表情を浮かべた。"

    "分かりやすい噂好きな人のようだ。こういう表情の変化は、同級生が人の噂話をするときとほとんど変わらない。"




    voice get_voice_filename("other")
    other_female_1 "「牛塚さん、家族と縁を切ったのか、ある時期からずっと独り暮らしだったのよ」"




    voice get_voice_filename("other")
    other_female_1 "「あんまり家から出ないもんだから、近所では餓死したんじゃないかって噂も頻繁に立ってたの。数日経ってふらふらしているところを見かけて、ああ、大丈夫だったなんてことよくあったのよ」"




    voice get_voice_filename("other")
    other_female_1 "「高齢者の孤独死って最近増えてるらしいし、大変よねぇ」"




    voice get_voice_filename("other")
    other_female_1 "「でも一月前くらいかしら。急にあの女の子の姿を見るようになって。近所では何か複雑な事情があったんじゃないかって、噂になってるのよ」"




    voice get_voice_filename("other")
    other_female_1 "「昔は夜の店での遊びが激しくって、隠し子かいたとか……あら、こんな話はあなたに聞かせる話じゃないわねぇ」"

    "と言うが、女性の顔にはもっと話したいと書かれていた。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「じゃあ、あの子のことはみなさん知らないんですね」"




    voice get_voice_filename("other")
    other_female_1 "「ええ。牛塚さんが海外で悪い事をしてたんじゃないかって勘繰る人もいて、みんな関わりたがらないのよ」"




    voice get_voice_filename("other")
    other_female_1 "「通報して、恨まれたりしたら嫌だものねぇ」"




    voice get_voice_filename("other")
    other_female_1 "「それにあの子、病気を持ってるんじゃないかって噂もあるくらいだから、みんな近寄りたがらないのよ」"




    voice get_voice_filename("other")
    other_female_1 "「あなたも気を付けなさいね。最近あの人が気になってる人が多いみたいだけど……」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「すみません、ありがとうございました」"

    "女性の話を聞いて、私は段々苛立ってきていた。"

    "色々推測するのは仕方がないと思うが、それで悪い方、けなす方へばかりというのは気分のいいものではない。"

    "そして一人暮らしのおじいさんなんて珍しくもないのに、それを笑い者にするのはもっと気分が悪い。"

    "私は女性にお礼を言って、話を打ち切る。"

    "少なくとも、私の予想が当たっていたことは分かった。"

    "牛塚さんという男性に話を聞くことができれば、あの少女のことも分かるかもしれない。"

    "お店もあるし、今日は家に帰ることに決めた。"






    $ set_info_location("03")



    stop music fadeout 1
    scene bg train normal with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "帰りの電車に乗ってから、私は直未にスマホからメッセージを送ることにした。"

    "今日は急に別れたから、心配させてしまったかもしれない。"

    "私は簡潔に状況を打ち込んで、直未に送った。"

    "すぐに、「分かりました。何でも相談してください」という内容の返信が来た。"

    "別れ際に直未が言ったのと同じだ。"


    voice get_voice_filename("nom")
    naomi "『でも……あの子と住んでいるのっておじいさん、ですよね。妙に気になるような……』"

    "直未の返信はさらに続いた。"

    "直未の気になることについてもっと聞きたいが、それでは結局前と同じになってしまう。"

    "私は直未に、「大丈夫だよ」とさらに返信を返す。また数秒でスタンプが返ってきて、会話はそこで終わった。"

    "きちんと自分で考え、調べよう。"






    python:
        set_info_scene("53")
        set_info_time("night")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    "帰ってすぐに準備をしてお店を開けた。"

    "何人かのお客さんが来てくれたが、平日の夜ということもあり、長居する人はいなかった。"

    "９時を回る頃、私はお店の看板を“close”に変えた。"

    "丁度その頃、約束通り海晴が訪ねてきた。"


    play music audio.miharu

    show mhr uni nor nor rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「やあ、凛火」"

    show rnk uni nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「お疲れ様。コーヒー、淹れてあげるね」"

    show mhr uni nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ありがとう。いいのかい？」"

    "少し長話になるかもしれないから、と私は頷いた。"


    play music audio.nichijo01

    "自分の分のコーヒーも淹れ、いつものテーブルに座る。"

    scene ecg nighttalkD2 nor with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「話といっても、ほとんど確認だろう？」"


    voice get_voice_filename("rnk")
    rinka "「……うん」"

    "私が席についてすぐ、海晴はそう問い掛ける。"

    "そして、コーヒーを一口。"

    show ecg nighttalkD2 smi with ecg_change

    voice get_voice_filename("mhr")
    miharu "「今日も美味しいよ」"

    scene ecg nighttalkA2 nor with dissolve

    voice get_voice_filename("rnk")
    rinka "「ありがと……って、そうじゃなくて。先週のあの夜、ソーニャと話していたのは――私の死因のカードについても、だったんだね」"

    scene ecg nighttalkD2 nor with dissolve

    voice get_voice_filename("mhr")
    miharu "「そうさ。君は、ソフィアが君のカードを持っていることを想定していなかっただろう？」"

    show ecg nighttalkD2 ser with ecg_change

    voice get_voice_filename("mhr")
    miharu "「しかし、ソフィアは悪意があってそれを言わなかったわけではないらしい。君に必要以上に疑われることはしたくなかったそうだ」"

    scene ecg nighttalkA2 nor with dissolve

    voice get_voice_filename("rnk")
    rinka "「分かるよ。私は初めソーニャのことすごく疑ってたから」"

    scene ecg nighttalkD2 nor with dissolve

    voice get_voice_filename("mhr")
    miharu "「仕方のないことだよ。もっとも、だからこそぼくはソフィアに確認をした。正確には、ぼくたちのカードを持っているかということを」"


    voice get_voice_filename("rnk")
    rinka "「そして実際、海晴の氏名のカードも持っていた」"

    show ecg nighttalkD2 ser with ecg_change

    voice get_voice_filename("mhr")
    miharu "「ああ。だがソフィアは信頼されないことを恐れずに、最初に言っておけばよかったと、後悔はしていたようだよ」"

    scene ecg nighttalkA2 sad with dissolve

    voice get_voice_filename("rnk")
    rinka "「……あの子らしいね」"

    scene ecg nighttalkD2 sad with dissolve

    voice get_voice_filename("mhr")
    miharu "「そうだね。その点についてはぼくも同意だ。悲しいくらい、彼女は純粋だった」"

    "このテーブルで話したときのことを思い出す。"

    "３人で、まるでお泊り会のような時間を過ごしていた。"

    show ecg nighttalkD2 ser with ecg_change

    voice get_voice_filename("mhr")
    miharu "「ぼくとしては、Ⅺの女性のように積極的に相手を脱落させている相手に≪ぼくのカード≫を取られるのは避けたかった」"


    voice get_voice_filename("mhr")
    miharu "「そしてそれ以上に、君のカードを選ばれるのが恐かった」"

    scene ecg nighttalkA2 ser with dissolve

    voice get_voice_filename("rnk")
    rinka "「だから、ソーニャを指名したんだね」"

    "私は、この先の言葉を続けるかどうか、逡巡した。"

    "それは、海晴がこの話をしているときも、いつも通り冷静なことに対する疑問だった。"

    "聞いてしまえば、聞きたくない答えが返ってくるかもしれない。"

    "だがこうやって考えているうちに、私の質問は口をついて出ていた。"


    stop music fadeout 1

    show ecg nighttalkA2 ser with ecg_change

    voice get_voice_filename("rnk")
    rinka "「海晴は――どうしてそんなに冷静でいられるの？」"

    scene ecg nighttalkD2 tro with dissolve

    voice get_voice_filename("mhr")
    miharu "「悲しむことが、本当に必要なことかい？」"


    play music audio.growapart

    "反対に海晴に問い掛けられて、私は答えることができなかった。"

    "それは、やっぱり私が聞きたくない答えだった。"

    "私だって、分かっている。"

    "悲しんでいても仕方がないって、分かっている。"

    scene ecg nighttalkA2 ser with dissolve

    voice get_voice_filename("rnk")
    rinka "「海晴はそれで、いいの？」"

    scene ecg nighttalkD2 ser with dissolve

    voice get_voice_filename("mhr")
    miharu "「構わないよ。君が選定の参加者だと知った時から、ぼくの気持ちは変わっていない」"


    voice get_voice_filename("mhr")
    miharu "「君のために、ぼくの命を捧げさせてくれ」"

    scene ecg nighttalkA2 ang with dissolve

    voice get_voice_filename("rnk")
    rinka "「もういい。もうそれは、分かったよ」"

    "海晴に言われて、私はつい強い口調で言ってしまった。"

    "そんなことが聞きたかったのではない。"

    "でも、補足や言い訳をする元気は出てこなかった。"

    scene ecg nighttalkD2 nor with dissolve

    voice get_voice_filename("mhr")
    miharu "「気持ちの整理がつかないのも、無理はない。昨日の今日だからね。そうやって悩めるのがきっと、凛火の強さだからね」"

    "海晴は変わらない口調で、続ける。"

    show ecg nighttalkD2 smi with ecg_change

    voice get_voice_filename("mhr")
    miharu "「今日はもう、終わりにしよう。しかし……存外早く話が終わってしまったけれど、ぼくはまだコーヒーを飲み終えていない。もう少しここにいていいかい？」"

    scene ecg nighttalkA2 ser with dissolve

    "私は黙って頷いた。"

    "海晴に指摘された通り、私は自分の気持ちに何も整理がついていないのだ。"

    "夜が、私の気持ちをかき乱した。"

    "しばらく座ったまま、私はコーヒーカップが空になるのを待った。"

    "その間ずっと、海晴と目を合わせることができなかった。"


    stop music fadeout 1
    scene bg lion01 night
    show mhr uni nor nor rev at std_cl
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「では、ぼくはそろそろ行くよ」"

    show rnk uni cat sma at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……ごめん、ちょっと待って」"

    "私は帰ろうとする海晴を引き留めた。"

    "聞きたかった大事なことをもう一つ、まだ聞けていなかったから。"


    play music audio.gimon

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴の名前は――その、色々あるのは分かってるけど、前の苗字は蛇鉈……なんだよね？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「私は海晴の名前を知っているのに≪未島海晴≫でカードは作られなくて、≪蛇鉈海晴≫が海晴の氏名のカードだったよね」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「戸籍上の名前は、ぼくは未島海晴だよ」"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「つまり、その、私の疑問っていうのは、カードが作られる基準がよく分からなくって……」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ああ。君の疑問はもっともだ。そして、きっとそれは選定において女神の説明不足な部分であり、ルールの穴と言うべきかもしれない」"

    "海晴は一瞬、辛そうな顔を浮かべた。"

    "この話題は、海晴にとってあまり心地いいものではないはずだ。"

    "だがそれでも、私のために我慢して平静を装っているのが分かる。"

    "私がそれに気付いていることを、当然海晴は分かっているだろう。その上での行動だから、私は海晴の言葉を遮ることはしなかった。"


    play music audio.shadowmiharu

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「――謝ろう。君には嘘を教えていた」"

    "追い詰められたような表情で、海晴はそう告げた。"

    "話を聞いている私の方まで、胸が痛くなる。"

    show mhr uni pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「このことを説明するには、ぼくのことをもういくらか詳しく話さなければならない」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくの苗字は両親が離婚して変わったわけじゃないんだ。別の理由で……ぼくは蛇鉈から未島になった」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「だが――ぼくの母親は君の知っている通り、あまり褒められた人間ではなくてね。いや、この際はっきりと言おう。ぼくは母親が嫌いだ」"

    "海晴の母親については以前、断片的にだが聞いている。"

    "金遣いが荒く、家事もしないという。"

    "だから海晴はアルバイトを多く入れ、家事もこなしている。"

    "飴茶に通う多くの生徒のように裕福ではなく、学費も海晴が特待生に選ばれる才女だから払うことができているのだ。"

    show mhr uni pai irr rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくはできることなら、父親の姓を名乗っていたかった。今でも、そうできなくなってしまった運命を呪っている」"

    "海晴は詳細は語らなかったが、私が知っているよりもさらに複雑な事情があることは分かる。"

    "海晴の抱える傷も、きっとこれらのことに起因しているのだろう。"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「この選定における≪カード≫のルールは、ぼくは全てが論理的なものではないと思う。いわゆる認知というものに頼り過ぎている」"

    "死因や未練がカード化されるには、きちんとその背景の情報を知っている必要がある。"

    "それもある意味での認知。"

    "一方で、絶対的な基準の用意されていないという欠陥がある。海晴が言いたいのはそういうことだ。"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「今回の場合も、そうだ。ぼくは自分の名前が≪未島海晴≫だということを受け入れていない」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「だから、海晴のカードは≪蛇鉈海晴≫なんだね」"

    show mhr uni pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「きっとぼくの心の奥深く――夢に現れる深層心理でも、同じことを思っているのだろうね」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私は、論理的かもって思うよ」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「そもそも名前って絶対的なものじゃない。生まれたばかりの赤ちゃんには名前がないもんね……名前は誰かがつけるものだから」"

    "桂子さんの一件がなければ、私は海晴の言葉にそのまま納得していただろう。"

    "だが、今の私の意見はこれだった。"

    "結婚すればほとんどの人は苗字を変えるし、法律上でも改名はできる。"

    "簡単ではないけれど、個人の意志が反映される曖昧なものでもあるのだ。"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「なるほど。認識自体が認知の上に成り立っているということか……その考えには及ばなかった」"

    show mhr uni sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは自分の名前に縛られていたからね。視野が狭くなっていたよ」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「大げさ、だよ。でも……疑問は解消したって感じかな」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君を混乱させてしまっていたね」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「ううん。みんなそれぞれ、色々あるでしょ。けど私にとって海晴は海晴だから。それは、何にも変わることはないよ」"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「――くすっ」"

    "私の言葉を聞き、海晴は微笑んだ。"

    "安堵したような、安らかな微笑だった。"

    show mhr uni sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「話は変わるけれど、運命の大広間であんなことを言ったから、君に避けられないか心配していたよ」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「本当に？　私は分かってたよ」"

    show mhr uni sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「これで、参加者のうちの何人かにはぼくたちが仲間割れしたと思い込ませることができたはずだ」"

    "今はもう、君と話すことは何もない――という言葉。"

    "私たちは一度目の選定の時から、知り合いとして会話しているところを他の参加者に見られている。"

    "ソーニャも私たちが友達だと思っていたらしいし。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「タイミングはばっちり……だったね」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")





    menu:
        miharu "「では、そろそろ行くよ」"
        "「うん、じゃあまた明日学校で」":

            $ flags_mhr_koukando += 1

            $ persistent.s9_1_seen = True
            $ grant_hear_all()
            jump f005_1.s1_1
        "「うん、じゃあ気を付けてね」":

            $ persistent.s9_2_seen = True
            $ grant_hear_all()
            jump f005_1.s1_2

label f005_1.s1_1:

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk", 614)
    rinka "「うん。また明日学校で」"

    hide mhr with std_out

    "海晴はにっこり笑うと、優雅な足取りでライオン館を後にした。"

    jump f005_1.s1_end

label f005_1.s1_2:


    show rnk uni nor que with std_change

    voice get_voice_filename("rnk", 615)
    rinka "「うん、じゃあ気を付けてね」"

    hide mhr with std_out

    "海晴は少し怪訝な表情を浮かべてから、静かな足取りでライオン館を後にした。"

    jump f005_1.s1_end



label f005_1.s1_end:


    hide rnk with std_out

    "結局、コーヒーを飲み終わってからの方が長い話になってしまった。"

    "私は空になったカップの底を見つめながら、もうちょっとだけテーブルに座ったままでいた。"

    $ add_seen_chapter("5-1")







    python:
        set_info_scene("54")
        set_info_date(5, 29, "tue")
        set_info_time("emorning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    pause 1

    $ show_hud()


    voice get_voice_filename("rnk", 616)
    rinka "「んっ……朝か……」"

    "この日は、夢を見ない深い眠りだった。"

    "夢。"

    "私にとってもう一つの意味を持ってしまった、夢。"

    "思えば夢の中に世界が広がっているなんて考えたこともなかった。"

    "人々の意識が女神の力で繋がっている。"

    "見知らぬ他人と、夢の中で出会うなんて。"

    "少女漫画だったら、運命的でロマンチックかもしれないのに。"

    "選定の参加者たちのことを思い返す。"

    "そして私は、あることを思い出した。"


    play music audio.investigation


    voice get_voice_filename("rnk")
    rinka "「おじいさん……！」"

    "昨日の直未とのメッセージのやり取りを思い出す。"

    "おじいさんのところに居候というのが気になる、と直未は言っていた。"

    "選定の参加者の中に、日本人の男性がいた。"

    "Ⅴに位置している男性だ。"

    "可能性は、ある。"

    "むしろ、本来ならすぐに気付くべきことだった。"

    "まだ登校までには時間の余裕があった。"

    "試したいことがある。"

    "私はあのおじいさんの家へ向かうことに決めた。"






    python:
        set_info_time("morning")
        set_info_location("24")



    stop music fadeout 1
    scene bg shigetsugu01 noon with fade_long
    play music audio.gimon
    pause 1

    $ show_hud()

    "私は再び、住宅街の中にある古い一軒家の近くに来ていた。"

    "複雑な道ではあったが、昨日来たときに住所をメモしておいたので迷うことはなかった。"

    "それに必死だったからか、実際は行き方を記憶していた。"

    show rnk uni nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「ここだ」"

    "少し離れた位置から、様子をうかがう。早朝ではあるが、人通りはちらほらあった。"

    "人がいなくなったタイミングをうかがい、郵便受けを見た。"

    "明らかに悪いことで心は痛むが、仕方がないと割り切った。"

    "郵便受けには大量の手紙が詰め込まれている。一日分ではなさそうだ。"

    "内容は何らかの督促状が多い。"

    "一種類ではなく、複数のところから送られているようだった。"

    "そのうちの一枚を取り出し、光の下まで持ってくる。"

    "見るのはそう、宛名だ。"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「牛塚{rb}茂継{/rb}{rt}しげつぐ{/rt}……さん」"

    "この家に住むおじいさんの名前で間違いないだろう。"

    "念のため、他の手紙もいくつか見てみることにした。宛名のないものを除いて、私の見た全てに同じ名前が書かれていた。"

    "あとは、このおじいさんの顔を見ることができれば確信が持てる。"

    "待ち伏せをしてみるか――とそう思ったが時間が時間だ。"

    "あまりのんびりはしていられない。"

    "今となっては、私は学校にいる方が安全かもしれないのだ。"

    "電車のぎりぎりの時間まで粘ろうと思ったその時、遠くに人影が見えた。"

    "どこか見覚えのある二人が歩いていた。"

    "二人とも背が高い、外国人男女の組み合わせだ。"


    play music audio.kinpaku

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「あの二人っ……！」"

    "私の視力では、まだはっきりと見えない距離だった。"

    "だがシルエットを見ただけで、それが彼らだと直感することができた。"

    "選定の参加者の二人であり、もっとも警戒すべきであろう二人組。"

    hide rnk
    show ode sta nor nor at std_cl
    show fed sta nor nor at std_cr
    with std_swap

    "Ⅲの男性――フェデリーコ・カルミナーティとⅪの女性だ。"

    hide ode
    hide fed
    with std_out

    "私は反射的に近くの塀に身を隠す。"

    "彼らもあの少女を追っている。"

    "あるいは私と同じように、おじいさんと少女の関連性を探っている。"

    "仮におじいさんが予想通りに選定の参加者だとすると、おじいさんを追ってこの場所を突き止めた可能性もある。"

    "女性の方が、何かメモ書きのようなものを手にしていた。"

    "つまり、どこかで住所を手に入れたのだろう。"

    "であれば、あの少女はここに住所を持っていないだろうから、私の想定したおじいさんを追って来たという可能性が一番高い。"

    "私がこのまま様子をうかがうか学校へ向かうか迷っているとき、家の扉がわずかに開いた。"

    "その時、あの二人組も近くの路地に身を隠した。"

    "女性の方からカルミナーティさんに指示をしたように見えた。"

    "Ⅺの女性はチャンスがあれば突撃する、といった印象があったので、彼女の慎重な行動は意外だった。"

    "あの少女であろうがおじいさんであろうが、自分の置かれている状況は分かっている。"

    "家を出るときに周りを警戒するのは当然だ。"

    "大丈夫だと判断したのか、ゆっくりと扉が開いた。"


    play music audio.investigation

    scene bg shigetsugu01 noon large at align(1.0, 0.6)
    show rnk uni sur su1 up at std_c
    with wipe_rl

    voice get_voice_filename("rnk")
    rinka "「あれは……」"

    "その瞬間、私の鞄から光が漏れた。"

    python:
        gameinfo_cardbook_sig_unlocked = True
        add_character_cards("rnk", ["5_name"])
        add_character_cards("sig", ["5_name"])

    "家から出て来たおじいさんを見たのとほぼ同時。"

    "牛塚茂雄が彼だと確信した瞬間である。"

    "夢の世界で見たのと同じ、頑固そうに見える。"

    "セーターにゆるいズボンという簡素な出で立ちは、かえって生活感がある。"

    "Ⅺの女性とカルミナーティさんはどういう意図があるのか、まだ隠れたままのようだ。"

    "やはり牛塚さんが選定の参加者だった。"

    "そのことを知れたのが大きな収穫であり、私はこれ以上ここにいてもリスクの方が大きいと判断した。"

    "例の二人と鉢合わせないように周りを警戒しつつ、駅へと向かった。"







    python:
        set_info_scene("55")
        set_info_time("morning")
        set_info_location("24")


    stop music fadeout 2
    scene bg shigetsugu01 noon with fade_longest
    play music audio.badguys
    pause 1

    $ show_hud()

    show fed sta nor smi at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「どうやらビンゴだぜ」"

    python:
        add_character_cards("fed", ["5_name"])
        add_character_cards("ode", ["5_name"])

    "民家から出て来る老人の姿を見て、オレは傍らのオデットにそう呟いた。"

    show ode sta arm irr rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「馬鹿、声がでかいんだ」"

    "オデットはオレの足を踏みながら囁く。"

    "図体はでかいくせに、こういう時は妙に慎重だ。あのジジイに見つからないように、あの民家からかなりの距離をとっていた。"

    "どうやら、自分が隠れるのに適していないことはよく分かっているらしい。"

    "ここに至るまでの経緯をざっくりと説明しよう。"

    "三度目の選定、スリム過ぎる日本人の女性が脱落した後、オレはオデットと次は誰を狙うかを話し合った。"

    "魯についてはオデットの勘と予想から情報を得たこともあり、オレたちはまだ初期から持っているカードを有効利用していなかった。"

    "そこで、次の脱落させる相手はオレの初期カードで氏名を知っている奴を選ぶことになった。"

    "オレの手持ちを知らせるのは癪だが、オデットが魯を脱落させて手に入れたカードをいきなり教えてきたら、それはそれでオレにメリットばかりで怖い。"

    "ま、当然そんなことはなかったわけだが。"

    "ソフィアなんちゃらとかいう、長い名前のロシア出身のガキだ。"

    "不幸っちゃ不幸な境遇だが、オレには関係ない。両親を人質にとり、そいつのカードをオデットが手に入れた。"

    "この時、ソフィアはオデットのカードを持っていたらしい。それもあってか、あいつはソフィアに時間を与えた。"

    "未練を叶える時間を。"

    "その理由は謎だが、元々考えの読めない奴だ。"

    "オレだけでは名前の情報だけでソフィアの動向を調べることができなかったのも事実なので、強く文句も言えないのだし。"

    "本来ならそのままオデットがソフィアを脱落させる流れではあったが、ミハルにより邪魔されちまった。"

    "ただまあ、オデットは意外なことがあったからと言って行動を止める女じゃない。"

    "その点についてはオレも同感だ。"

    "イタリアにいた頃も予想外なんてのはしょっちゅうあることで、むしろそういう場合には人同士の汚い本質が見えるのを楽しまないといけない。"

    "運命の大広間で暴露しちまった通り、オレの初期カードは不運なことに３枚中２枚が初期に脱落しちまった奴らのものだったので、もうない。"

    "順番として、ロシアっ娘の次はオデットの持っていた≪Ⅴ・氏名――牛塚茂継≫のカードを手掛かりに調査をし、ここまで来たってわけだ。"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「おい、ぼーっとしてんじゃねえ。撤退するぞ」"

    show fed sta nor ang with std_change

    voice get_voice_filename("fed")
    federico "「は？　何でだよ？　相手はジジイだ。とっ捕まえて情報を吐かせりゃいいだろうが」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「それか、あいつのいないうちに家に入っちまえばいいだろ」"

    show ode sta arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「馬鹿かってんだ。これから通勤ラッシュの時間に入る。ただでさえあたしらは目立つんだ、通報でもされたら厄介だろ？」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「早朝か深夜にもう一度来る必要がある。ここは住宅街だからな。ソフィアや魯の時よりも慎重にいかねーと」"

    show fed sta nor ama with std_change

    voice get_voice_filename("fed")
    federico "「オレより目立つのはあんただけどな」"

    "オデットはオレの足を踏みながら、「てめーも十分目立つんだよ」と無言の圧力をかけてきた。"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「だけどさ、結局新しい情報は得られなかっただろ？」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「いや、あの家がジジイの住み家だって分かれば死因は予想できる」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「ボロっちい家だが、それで分かるのか？　いや――なるほどな。だからか」"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「珍しく察しがいいじゃねえか。言ってみろ」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「ちっ」"

    "思わせ振りなことを言えば、オデットの方から勝手に話すかと思ったが、読みが甘かった。"

    "くだらない見栄を張ろうとしたことを後悔する。"

    "オデットはオレの肩を小突きながら、続けた。"


    play music audio.investigation

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「他に身寄りがないジジイだ。日本じゃそういう連中が孤独死してしばらくしてから発見されるってのは問題になってるらしいじゃねえか」"

    show ode sta nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「日本は特に閉鎖的なコミュニティ――ムラ社会だっつうから起こりやすいのかもしれねーな」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「腐った死体やらの清掃なんかを専門にしてる業者すらあるらしい……まあ、それはいい」"

    show ode sta gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「てめーが話を聞いた主婦の言葉を思い出しな」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「まあべらべらと喋る、太った主婦だったな……」"

    "そいつと話している時のことを思い出す。"

    "あのジジイは家から出ないことも多く、よく餓死でもしたんじゃないかって噂されていた。"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「餓死……か。しかし、いくら孤立したジジイでも先進国で餓死はないんじゃないか？　金の補助は国から受けてたんだろうし」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「そうでもないさ。あの主婦は、ジジイが腰を痛めてることも話してただろ？」"

    "言われてみれば、そんなことを言っていたような気がする。"

    "どうして直接話を聞いたオレよりもオデットの方が覚えているのかは分からないが。"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「ひどい腰痛ってのは、自力で動けなくなることがある。あたしが船に乗ってたときにも、そうなっちまった乗組員はいた」"

    show ode sta arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「ジジイが家で突然そのレベルの腰痛に襲われたとしよう――元から患ってたんなら突発ではねえけど――とにかく」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「孤立しているから、助けを求められない。近所の連中も、ジジイが家から出て来ないのは慣れっこだから気にしない。金だけもらって介護を受けてるわけじゃねえから、短期間じゃ訪問もねえ」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「人間は、７日飯を食えなかったら、あるいは３日水が飲めなければ死ぬんだ。あたしはよく知ってる」"

    "オデットの声は、真剣味溢れる切迫感のあるトーンだった。"

    "確かにこいつなら、餓死寸前になった経験があるかもしれない。あるいは、仲間が餓死する様を見ていてもおかしくはない。"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「重度の腰痛で動けなくなっちまい、助けも呼べず、そのまま餓死――か。あり得ない話じゃないと思うが、そんな早く……うわ」"

    "持ち歩いていた本が、光を帯びる。"

    scene ecg cardbook bli with dissolve_long

    "カードが生まれる時の光だ。"

    python:
        add_character_cards("fed", ["5_death"])
        add_character_cards("ode", ["5_death"])
        add_character_cards("sig", ["5_death"])

    "オデットも、同じくカードを手にしていた。"


    scene bg shigetsugu01 noon
    show ode sta arm smi rev at std_cl
    with dissolve_long

    "口元が、にやりと不敵に笑っていた。"

    "気持ち悪いほどに、こいつは察しが良過ぎる。"

    show fed sta nor nor at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「だけど、動けないほどの腰痛があっても、さっきジジイは外に出てたな」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「ソフィなんちゃらの時もそうだったが、選定の間は体がある程度回復してるってことなのか」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「……てめーの予想の通りだろうな。肉体の状態はどこかの時点まで戻されるって考えた方がよさそうだ」"

    "オデットは確かめるように繰り返し、頷いた。"

    "てっきり「知るか」とでも答えると思ったので、意外だった。"

    "すぐに元通りの表情になり、オデットは振り返った。"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「ほらよ、十分収穫はあった。いい加減戻るぞ」"

    "オレたちはジジイに見つからないようにしながら、来た道を引き返した。"









    python:
        set_info_scene("56")
        set_info_time("morning")
        set_info_location("24")


    stop music fadeout 1
    scene bg shigetsugu01 noon with fade_long
    play music audio.alan
    pause 1

    $ show_hud()

    "ここ数日間、凛火の様子をうかがっていたアランは、牛塚茂雄――あの老人の氏名をアランはまだ知らないが――の自宅の近くで彼女を見張っていた。"

    "獅子舞凛火は気付いていないが、アランは彼女の自宅であるライオン館や通っている飴茶高校の位置も把握していた。"

    "アランは凛火が老人の自宅で氏名を手に入れ、学校へ向かったところまでで尾行はやめていた。"

    "アラン・スコーピオンは静かにその背中を思い出していた。"

    show aln sta nor nor at std_c with std_in

    voice get_voice_filename("aln")
    alan "「リンカ……」"

    "自分が本気で脱落させようと思えば、彼女を脱落させるのは容易だ。"

    "アランはそう思っていたが、いくつかの理由から脱落させにかかってはいない。"

    "一つはⅡの少女――海晴が、現実世界で凛火と知り合いだからだ。"

    "夢の世界では仲間割れしたように見せていたが、アランは彼女らが喫茶店で仲良く話していたのを見ていて、実際は協力関係にあることには気付いていた。"

    "獅子舞凛火を相手どるということは蛇鉈海晴とも敵対することだ。"

    "彼女の初期カードがまだ読めていない以上、手を出しにくいというのが本音だった。"

    "脱落させた相手は海晴よりもさらに年下の少女ではあったが、指名の優先権を取得するなど、あなどれないところがある。"

    "それよりも切実な理由は、アランが日本の警察に目をつけられているということだった。"

    "瓶淵桂子を脱落させるとき、アランは大胆な行動に出過ぎてしまった。"

    "病院に侵入する前に監視カメラの位置を把握し、避けられないものはコードを切断するなどの対策をとってはいたが、見落としがあったのだ。"

    "鮮明に映っていたわけではないが、アランは病院を襲撃した容疑者としてリストアップされていた。"

    "裏から手を回して対策を取りただちに逮捕されることはないものの、今のアランはそうやすやすと違法行為ができない状況にあった。"

    "自分の会社があるインドならともかく、日本ではアランの権力が行き届く範囲は限定的。"

    "もう少し無茶はできないでもないが、まだその時ではないと判断している。"

    "だが、それらは結局、アランが自分を納得させるためにこじつけた理由だった。"

    "彼が気付かないようにしている理由、それは一度はアラン自身が直感してしまった単純なもの。"

    "彼女の瞳が、似ていたから。"

    "潤沢な財産の裏付けも強靭な肉体の説得力もないにもかかわらず、意志だけで煌々と輝くその瞳が、とても――。"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「それよりも」"

    "凛火と同じ方法で老人の名前を知ることもできたが、アランはそれをしなかった。"

    "いや、できなかったと言った方がいいだろう。"

    "老人の自宅を遠くから見張っている二人組を発見したのだ。"

    "Ⅲの男性と、Ⅺの女性だ。"

    "凛火が立ち去った後に来たので、彼らは凛火も来ていたことに気付いていないようだった。"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「Ⅺの女は、確か≪Ⅴ・氏名≫を取得していたな」"

    "そのことを覚えていたので、アランは彼女がここにいることに疑問は持たなかった。"

    "氏名さえ分かれば、アランのようにたくさんのコネをもつ者にとって相手の自宅を特定するのはそう難しいことではない。"

    "だから彼が意外に思っているのは、Ⅲの男とⅪの女が協力していることだった。"

    "運命の大広間で間抜けさを披露したⅢの男は後回しでも問題ないと思っていたが、Ⅺの女と組んでいるとなると別だ。"

    "アランは自分以外に参加者を脱落させた者については高く評価している。"

    "一人は海晴であり、もう一人がⅪの女だ。"

    "特にアランはⅪの女に対して、ただならぬものを感じていた。"

    "いくつもの修羅場を乗り越えてきた風格があったからだ。"

    "様子を見る限り、やはりⅪの女が主導権を握っているようだった。"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「男の方は手足か、あるいは鉄砲玉といったところか」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「まあいい。今すべきは――」"

    "アランは狙いを老人からⅢとⅪの二人組に切り替えることにした。"

    "この二人の動向に注目していれば、Ⅴの老人の情報はおのずと分かってくるはずだ、と予想をして。"

    "自分の存在を察知されていないうちに相手の滞在先などを突き止められれば、アランはその分有利となる。"

    "自身の知名度による不利をくつがえせるかもしれない。"

    "アランは息を殺し、長身の二人組の尾行を始めた。"









    scene bg shigetsugu01 noon with fade_long
    pause 1

    "アランは再び住宅街へと戻って来ていた。"

    "ⅢとⅪの女性の二人組を尾行したはいいが、結局まかれてしまった。"

    "自分の尾行に気付かれた可能性は低い、とアランは思っていた。"

    "その点について、アランは自分を信用しているからだ。"

    "だが、彼女らは無意識のうちに尾行を振り切る歩き方をしているのだろう。"

    "一瞬車の影が出来たと思ったら、そのまま見失ってしまったのだ。"

    show aln sta nor irr at std_c with std_in

    voice get_voice_filename("aln")
    alan "「やはり、あの女が優先か」"

    "アランは人通りの増えてきた住宅街で目立たぬよう、小さな声で呟いた。"

    "そして、彼もまた自分の滞在先へ戻ることにした。"

    "時間的にも内容的にも、潮時だ。"








    python:
        set_info_scene("57")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "一日を終え、私は自分の部屋で一息ついていた。"

    "学校でもお店でも、特に変わったことはない。"

    "強いて言うならば、私のクラスもどうやら少しずつ文化祭の準備を始めているくらいだ。"

    "出し物は、占いの館らしい。"

    "うちのクラスの実行委員があらかじめ何種類かの占いを用意して、来場客に実践するというものだ。"

    "実行委員の方が色々な占いを試してみたいから、この企画に決めたのだろう。"

    "占い――運命。"

    "企画の立ち上げに関わっていないのに、皮肉なものだ。"

    "海晴や私は特に意見が求められず、当日何かしらの手伝いをするだけでいいとのこと。"

    "真央はどうやら興味があるらしく、事前の準備を手伝ったり、当日は私たちよりも長くシフトに出ることになるそうだ。"



    voice get_voice_filename("mao")
    mao "『真面目な顔して思わせ振りなこと言っておけばいいんだよねぇ。うち、得意な気がする』"

    "という真央らしいちょっとずれた適当なことを言っていた。"

    "文化祭は再来週だが、今頃企画が決まって間に合うものなのだろうか。"

    "きっとここまでぐだぐだなのは全校でもうちのクラスだけだろう。"

    show rnk paj nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「ふぁ……」"

    "まだ10時頃だが、もう眠くなってしまっていた。"

    "今朝はかなり早くから行動していたのだから、無理もないか。"

    "――牛塚茂継。"

    "あのおじいさんの名前を、私は心の中で反芻していた。"

    "残る情報は≪死因≫と≪未練≫だが、どうやって知ろうか。"

    "それにあの少女のことも気になる。"

    "彼女の≪死因≫のカードこそ持っているが、分かっているのは≪焼死≫という情報だけで背景情報は他に何も知らない。"

    "初めに配られたカードだからこそ、こういう食い違いが起きてしまう。"

    show rnk paj nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「問題は、ここからどうすればいいか……だね」"

    "さらに、Ⅺの女性とカルミナーティさんまで関わってきている。"

    "昨日今日でうまくはいったが、私は張り込みや尾行を得意としているわけではないのだ。"

    "それを続けてもいつボロが出て、かえってこちらが不利な状況に陥るかは分からない。"

    "とはいえ彼らに先を越されればその分、彼らが有利になるだけだ。"

    "直接訪ねるという選択肢もなくはないが、最もリスクが高い。"

    "おじいさんとあの子、そして私の３人まとめてⅪの女性の標的になってしまうというパターンも想定できる。"

    "苦し紛れに『牛塚茂継』という名前を検索してみるが、情報は何も出てこなかった。"

    "全くの他人でお金の貸し借りなどもしていない私では、役所に行っても戸籍をとることはできないし、リスクの少ない方法で彼を調べるのは難しそうだ。"

    "ここで私は、考え方を変えてみることにした。"

    "私が彼らより勝っていることを考える。"

    "参加者に日本人が多く、それも地方ではなく新宿周辺に固まっている以上、私が普通の女子高生であること自体がアドバンテージ。"

    "ある程度までなら何をするにも目立たず、自然。"

    "だが結局思いつくのは、近所の人への聞き込みくらいだった。"

    "いや、それでいいのかもしれない。"

    "今朝は通学通勤のラッシュよりもかなり早い時間に牛塚さんの家に行った。"

    "だから、例の二人と遭遇したのだ。"

    "彼女たちは人のいない時間を選んでいる。"

    show rnk paj arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私なら、人が多い時間でも――」"

    "女子高生が赤の他人であるおじいさんの聞き込みをしているのは自然ではないが、見るからに只者でない外国人がやるよりはマシだ。"

    "私なら、離婚した元妻の孫とか、そういう言い訳もつける。"

    "桂子さんの入院していた病院で直未がしてくれたのと同じことをすればいい。"

    "ならば狙いは買い物客が増える、夕方。"

    "聞き込みできる対象も増えるし、人通りの中に紛れることもできる。"

    "そうと決まれば、少しでも長く寝て体力を回復させよう。"

    "電気を消そうとしたところで、足元から「にゃーん」という声が聞こえた。"

    "ライオン館に居ついている風来坊、レテがちょこんと座っていた。"

    show rnk paj nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、レテ。どうしたの？」"

    "エサと水はちゃんと皿に入れたはずだから、お腹が空いたというわけではないだろう。"

    "当然私の質問に返事はない。まあ、あったらそれはそれで怖いけれど。"

    show rnk paj nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「私、もう寝るからね」"

    "レテには悪いが、私は疲れているのだ。"

    scene black with dissolve

    "電気を消して、ベッドに入った。"

    "するとレテは珍しく、私の布団に潜り込んでくる。いつもは大抵布団の上、それも私のお腹の上で寝るくせに。"

    "私はレテの小さな頭をひと撫でしてから、目をつぶる。"

    "こんなに小さな体だけれど、ちゃんと体温を持っていて、布団の中がじんわりと温かくなった。"




    python:
        set_info_scene("58")
        set_info_time("lnight")
        set_info_location("01")

    stop music fadeout 2
    scene ecg pattern nor a with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    "夢を見ているという自覚がある夢を明晰夢というらしい。"

    "女神の選定が始まってから、私は最低一週間に一回は明晰夢を見ることになってしまった。"

    "もっとも、運命の大広間での出来事を夢とくくっていいのかは、微妙なところではあるけれど。"

    "そして今日もまた、私はちゃんと眠りに落ちたという自覚を持ちながら、現実とは違う映像を見ていたのだった。"

    show let sta nor sm1 at std_c with std_in


    voice get_voice_filename("let")
    lete_unk1 "「やあ」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「お久し振り……でもないのかな。私は人間の時間の感覚がよく分からなくてね」"

    "いつか夢の中で見た男性だ。"

    "彼が出て来る夢を見たこと自体、今の今まで私の記憶から抜け落ちていた。"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「私のことは覚えているかい？　いや、今思い出したのだろうね」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君が君の大事な記憶を忘れてしまっているように、この夢の中での出来事も、忘れてしまうという必然性があるからね」"

    "何か答えようと思ったが、私の方は声を出すことができなかった。"

    "彼が一方的に話すばかりだ。"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君はコーヒーのお店をやっているそうだけれど、私は紅茶の方に興味があってね」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「一度アフタヌーンティーというものを楽しみたいと思っているのだけれど」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「もっともこの夢の世界では、一緒に語り合う相手がいないどころか、ティーセットというものが存在しないこと自体が残念だよ」"

    "男性は、現実世界での私を知っている。"

    "もっともその事実が分かったところで、きっと彼の言うようにこの夢で聞いたことは全て忘れてしまうのだろう。"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「さて、そろそろ雑談もいいだろう。今夜はもう一つ、君の抜け落ちていた記憶が舞い戻って来たのだからね」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「お祝いの言葉を告げるために、わざわざ出向かさせていただいたよ」"

    show let sta nor tro with std_change


    voice get_voice_filename("let")
    lete_unk1 "「どんな記憶かって？　おっと、君が夢の中で記憶を取り戻す前に出て来てしまったね」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「やはり人間の時間の概念は難しい。一方的に流れるだけではあるのだけれど、感覚が掴みにくいよ」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「では、朝を迎える前に少しだけ君の記憶を思い出すといい」"











    scene bg fatalhall01 up large with wfade_longest
    pause 1

    "私は、運命の大広間に一人で立っていた。"

    "いつもの≪Ⅰ≫と書かれた床の上ではあるのだが、他の参加者の姿はなかった。"

    show dia sta fro smi big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「ごきげんよう、運命の奴隷となってしまった哀れな子羊サマ」"

    "私に向かって、真っ白な少女が話しかけていた。"

    "女神パルカだ。"

    "私の床の正面、つまり何もない宙にもかかわらず、彼女は平然と立っていた。"

    "二人が向き合う姿を、私は俯瞰的に眺めていた。"

    "主体がそこにはないということを理解して、私はこれが自分の記憶であると気が付いた。"

    show dia sta fro sm1 big with std_change

    voice get_voice_filename("dia")
    parca "「命を落としてしまった貴女サマの精神は今、運命を彷徨ってらっしゃいますわ」"

    show dia sta fro nor big with std_change

    voice get_voice_filename("dia")
    parca "「ですが貴女サマは、改変された運命の中で≪女神の選定≫の参加者になっていただきます」"

    "女神は淡々と、≪女神の選定≫について語り出した。"

    "ルールについても、細かく。"

    "私が強い口調で何かを言っても、全く相手にしていない。"

    "話している内容は、一度目の選定のときに聞いたのとほとんどが同じ内容だった。"

    "私が一度聞いたはずの、記憶。"

    "つまりこの記憶は、私が火事で死んでしまった直後のものだろう。"

    "これだけしっかり説明していたのだから、呆れられるのも無理はないと、今になって思う。"

    "だが一度聞いたことの繰り返しだからといって、思い出したことは無駄にはならなかった。"

    show dia sta fro cl2 big with std_change

    voice get_voice_filename("dia")
    parca "「ただし、忘れてはいけないことが一つございます」"

    show dia sta fro cl1 big with std_change

    voice get_voice_filename("dia")
    parca "「貴女サマ方12人はみな、12週間後の同じ時、同じ場所にいた可能性を持っていました」"

    show dia sta fro cle big with std_change

    voice get_voice_filename("dia")
    parca "「一度は失われてしまった未来で到達していたはずの場所――その場所こそ、貴女サマ方の≪運命の終着点≫となりますわ」"

    show dia sta fro no2 big with std_change

    voice get_voice_filename("dia")
    parca "「選定で最後の一人となられましたら、必ずその時までにその場所へ向かってくださいませ」"

    show dia sta fro glo big with std_change

    voice get_voice_filename("dia")
    parca "「運命の終着点に辿り着いて初めて、あなたが死の運命を回避し、生き残ることができたという運命が定着いたしますわ」"

    show dia sta fro gl1 big with std_change

    voice get_voice_filename("dia")
    parca "「もし運命の終着点に辿り着かなければ――それは、その時のお楽しみ、ということにいたしましょう」"

    "パルカは具体的な時間と場所を語ることはなかった。"

    "パルカは私の額に触れ、目を閉じる。指先に、小さな光が一瞬だけ灯った。"

    "語られなくても、私たちは女神に教えられていたのだ。"

    "運命の終着点とやらを――。"

    $ add_seen_chapter("5-2")









    python:
        set_info_scene("59")
        set_info_date(5, 30, "wed")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene black with wfade_longest
    pause 2
    scene bg myroom morning with dissolve
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "私は、はっと目を覚ました。"

    "夢の内容ははっきりと覚えていた。"

    "私が事故に巻き込まれ命を落とした直後、運命の大広間に連れて行かれて、女神と話したときの記憶を見ていたのだ。"

    "私が一度目の選定の際に聞いたことを、パルカがすでに説明していたというものだ。"

    "彼女が呆れたのにも納得だ。"

    "その時の自分の≪死因≫と≪未練≫を聞いたはずではあるが、内容までは思い出すことはできなかった。"

    "しかし、何より重要なのは――。"

    show rnk paj nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「運命の、終着点」"

    "女神の語った、この内容だった。"

    "選定が終わり最後の一人になった後、私がいなければならない場所のことだ。"

    "その場所は、私のよく知っている場所だった。"

    show rnk paj nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あの公園の、直未と話した、あの場所――」"

    "新宿という大都会の中にある巨大な庭園だ。"

    "時計台のようなビルが見える広場は、私のお気に入りだ。"

    "まさにその場所が、女神が私に――私たち選定の参加者に見せた運命の終着点だったのだ。"

    show rnk paj arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「まさか……そんなことって……」"

    "驚かずにはいられなかった。"

    "その場所は、私の家からとても近い場所なのだ。"

    "選定の始まった週から数えて12週間後、今から数えて約7週間後、天気がよいからと散歩に行ってもおかしくはない。"

    "同時に、有名な観光地にもなっている。"

    "ソーニャは、日本に観光に来る予定があったと言っていた。"

    "あの公園を訪れていても、おかしくはない。"

    "他の参加者は分からない。"

    "だが有名な場所であるからこそ、誰もが訪れている可能性はある。"

    "同時に、直未と話した日に感じた既視感の正体も明らかになった。"

    "私はあの光景と同じものを、女神から見せられていたのだ。"

    "その感覚をどう言葉にすればいいのか分からない。"

    "まさに夢を見る時のような、頭の中に直接映像が浮かぶような感覚だ。"

    show rnk paj nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「そういう……ことだったんだ……」"


    stop music fadeout 1

    "やっと、気持ちが落ち着いてきた。"

    "選定の参加者に日本人が多いこと、参加者が日本へ集まっていること、そのどちらの疑問にも回答を得ることができた。"

    "何故あの場所が≪運命の終着点≫なのかという理由は、女神は語ってはいなかった。"

    "≪女神の選定≫がどうして存在しているのか、どうやって存在させているのかを語らないのと同じように、参加者にとって不要な情報だからなのだろう。"

    "ともかく、私は≪女神の選定≫において重要な記憶を取り戻すことができた。"

    "頭の中が整理できた頃、私は自分の隣に熱を感じないことに気が付いた。"

    "昨晩、レテが私の布団に潜り込んできていたが、いつのまにか姿を消していた。"

    show rnk paj nor smi with std_change


    voice get_voice_filename("rnk")
    rinka "「まったく、自由な奴だにゃ……うわ」"

    "猫の姿を思いながら呟いたせいか、無意識のうちに語尾がおかしくなっていた。"

    "念の為に入り口の方を見てみるが、誰もいない。"

    "一人の時でよかったと、心底思う。"

    "さて学校にと思ったところで時計を見て、一時停止してしまった。"

    "よっぽど深い眠りについていたのだろう。"

    "私は、本来起きる時間よりも30分以上も寝坊していた。"








    python:
        set_info_scene("60")
        set_info_time("morning")
        set_info_location("24")

    stop music fadeout 2
    scene bg shigetsugu01 noon with fade_longest
    play music audio.badguys
    pause 1

    $ show_hud()



    "オレたちは再び、牛塚茂継の家の前に来ていた。"

    "朝は散歩に出るのが、あのジジイの日課らしい。"

    "腰が多少よくなっているから歩くのに支障はないんだろうが、ただ同じ道を歩くだけの何が楽しいのかオレには理解ができない。"

    "ともかく、奴がその間家を空けるのは事実だ。"

    "そこでオレたちは、あいつの家に忍び込む計画をしていた。"

    "家に入って何をするのかと聞けば、オデットは簡潔に答えた。"

    show ode sta arm ser rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「痕跡を探す」"

    "まあ、オレも何をするのかくらいは分かっていた。"

    "オレたちが持っていないのは、あのジジイの未練のみだ。"

    "ボロっちい家ということは、恐らく奴がずっと住んでいる家だ。"

    "昔から置きっぱなしの物というのは必ずあるだろう。"

    "そういった物が未練と繋がっているかもしれない。"

    "つまり痕跡とは、ジジイがあのボロ家で生き続けてきた痕跡ということだ。"

    show fed sta nor int at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「だが、鍵はどうするんだ？」"

    show ode sta nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「窓を割ればいいだろ」"

    "現実的な問題を、オデットは堂々とした犯罪予告で答えた。"

    "いや、こんな住宅街の真ん中でそれをやったら駄目だろ。"

    "ただでさえ、家に侵入するのはベストは深夜なのにもかかわらず、オレたちは早朝に実行しているんだ。"

    "通勤通学の時間よりもさらに早い分人通りは少ないが、それでもゼロじゃない。"

    "オデットに聞こえるようにため息をつき、オレは言った。"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「まあ、いい。鍵はオレに任せてくれ。マフィアの下積み時代にピッキングの技術は覚えてるからな」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「ほう、意外じゃねーか」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「最新式の鍵なんかは無理だろうがな。三分程度でいい。人が来ないかを見張っててくれ。あのジジイは孤立してるが、さすがにオレみたいなのが鍵をこじ開けてたら通報される」"

    show ode sta nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「オーケー。ま、たまにはてめーにも見せ場を作ってやろう」"

    hide ode
    hide fed
    with std_out

    "オデットがにやりと笑った直後、家の方に動きがあった。"

    "予想通り、奴が散歩へ出かけるところだ。"

    "振り返っても自宅が見えないくらい歩いていったのを確認し、オレたちは牛塚茂継の家の扉の前へと向かった。"

    scene bg shigetsugu01 noon large at align(0.0, 0.8) with dissolve

    show fed sta nor ela at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「よし。オレの出番だ。道の方を見ててくれよ」"

    show ode sta arm ser rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「任せた。しかしよ、てめー、あのジジイが出て来るところ見てたろ？」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「……ああ」"

    show ode sta nor inn rev with std_change

    voice get_voice_filename("ode")
    odette "「あいつ、鍵閉めてたか？」"

    show fed sta nor bad with std_change

    voice get_voice_filename("fed")
    federico "「……あ」"

    "言われてみて、ようやく気がついた。"

    "確かに牛塚茂継は家を出るとき、振り返って鍵を閉めるという行動をしていなかった。"

    "思い返せば、昨日の朝に奴を見たときも鍵を閉めてはいなかった。"

    "オデットはそれを確認していたからこそ、鍵のことを口にしなかったのだろう。"

    "オレは畜生という言葉を嚙み殺して、ボロ家の扉に手をかけた。"









    $ set_info_location("25")

    stop music fadeout 1
    scene bg shigetsugu02 noon with fade_long
    pause 1

    "鍵が開いていたので、オレの見せ場はなかったことになる。"

    "オレが前へ行き靴を脱ぎ、手に持ったまま家の中へと侵入した。"

    "いかにもなボロ家という感じで、木製の机や椅子、新聞紙や雑誌など物で一杯であった。"

    "ともかく、狭い。"

    "日本の家というものをオレはよく知らないが、大量の物をなしにしてもここは窮屈だ。"

    "オデットとオレが並ぶと廊下は定員オーバーになってしまうほど、幅がない。"

    show ode sta arm smi rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「さて、家宅捜索と洒落込もうぜ」"

    "両手を閉じたり開いたりしながら言うオデットは、にやりと好奇心に満ちた表情を浮かべている。"

    "ジジイは留守なので声のボリュームは気にしなくていいとはいえ、オデットは普通に話していた。"

    scene bg shigetsugu02 noon large at align(0.0, 0.1), zoom(1.3)
    show yuu sta war war up at std_c
    with wipe_rl


    voice get_voice_filename("yuu")
    yuu_unk3 "「…………誰？」"

    scene bg shigetsugu02 noon with wipe_lr

    "完全に気を抜いていたオレたちは、家の奥から聞こえた声を聞いた。"

    "子供の声だ。"

    show fed sta nor pa1 at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「……ああん？」"

    "聞き覚えのない声だ。"

    "ここのジジイは一人暮らしと聞いていたから、誰かいるのは妙だ。"

    "だが、聞き間違いではないだろう。"

    "確実に、人の声がこの家の奥から聞こえたのだ。"


    play music audio.impatience

    show ode sta arm ser rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「厄介だな」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「は？」"

    scene bg shigetsugu02 noon large at align(0.0, 0.1), zoom(1.3)
    show yuu sta war war up at std_c
    with wipe_rl


    voice get_voice_filename("yuu")
    yuu_unk3 "「二人いるんだね」"

    scene bg shigetsugu02 noon with wipe_lr

    "今度は、さっきよりもはっきりと聞こえた。"

    "少年か、少女か。"

    "とにかく子供の声だった。"

    scene bg shigetsugu02 noon large at align(0.0, 0.1), zoom(1.3)
    show yuu sta war cla up at std_c
    with wipe_rl


    voice get_voice_filename("yuu")
    yuu_unk3 "「聞いたことがある声だ。夢の中で……おまえたちの声は知っている！」"

    "夢の中と聞き、ピンと来た。"

    "間違いない、こいつは選定の参加者だ。"

    "声から推測すると、このガキはⅣの位置にいる――。"

    scene bg shigetsugu02 noon
    show ode sta nor gla rev at std_cl
    with wipe_lr

    voice get_voice_filename("ode")
    odette "「blank……てめーが白紙のガキだな」"

    scene bg shigetsugu02 noon large at align(0.0, 0.1), zoom(1.3)
    show yuu sta war sur up at std_c
    with wipe_rl


    voice get_voice_filename("yuu")
    yuu_unk3 "「――ⅢとⅪの人たち。まさか二人が協力していたなんて……」"

    scene bg shigetsugu02 noon
    show fed sta nor pa2 at std_cr
    with wipe_lr

    voice get_voice_filename("fed")
    federico "「ジジイとⅣのガキが協力していたなんて……」"

    hide fed with std_out

    "オレとガキは、ほとんど同じタイミングで驚いていた。"

    show yuu sta war su rev at std_l with std_in

    "白熱灯の光を浴びながら、そいつは家の奥から姿を現した。"

    "身長は、160センチそこらだ。"

    "ヨーロッパや欧米とは系統が違うが、くっきりと整った顔立ち。"

    "ただしかなり若く、13歳か14歳くらいだろうか。成長期真っ只中といった容貌だ。"

    "まだ声変わりしていないせいもあり、男女がはっきり分からない。"

    "線の細さからすると恐らくは――女か。"

    show fed sta nor nor at std_r with std_in

    voice get_voice_filename("fed")
    federico "「なあ、さっきのどういう意味だ？　blankってのがこいつの氏名なのか？　それに、そもそもどうして名前を……」"

    show ode sta nor gla rev behind fed at std_c with std_in

    voice get_voice_filename("ode")
    odette "「あー、言ってなかったな。こいつの≪氏名≫はあたしの初期カードの一枚だ」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「だが言った通り、内容は≪blank≫、白紙で何も書かれちゃいなかった。直接会えば分かるとも思っていたが……残念、まだ分かってねーな」"

    "ガキはオデットの言葉を聞き、目を細める。"

    "いかにも警戒しているって視線だった。"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「blankってのは、名前がないってことなのか？」"

    show ode sta arm smi with std_change

    voice get_voice_filename("ode")
    odette "「さあな。どうなんだ？」"

    show yuu sta war war rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「教えると思う？」"

    show ode sta gra smi with std_change

    voice get_voice_filename("ode")
    odette "「はぁん」"

    "ガキが挑発的にオデットを睨みつけると、オデットはわざとらしく鼻で笑ってみせた。"

    show yuu sta war war rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「まあそれは……ボク自身知らないから答えられないんだけど」"

    show yuu sta war sad rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「選定に参加しているのは分かっているけど、どうして死んだのか、それまでにどうやって生きてきたのか――自分の名前さえも分かっていない」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「……記憶喪失ってやつか？」"

    show ode sta arm irr with std_change

    voice get_voice_filename("ode")
    odette "「はんっ……女神は不親切だな。その状態で選定に参加させるとは……肉体だけマトモにすりゃいいわけじゃなかろうに。公平性なんてありゃしねぇ」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「妙に同情してるな？」"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「同情じゃねぇよ。憐れみだ」"

    "そう言うと、オデットはガキの方に視線を移した。"

    show ode sta arm ser with std_change

    voice get_voice_filename("ode")
    odette "「ジジイとは協力しているのか？」"

    show yuu sta war war rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「協力？　知らないよ。ボクたちはただ普通に生活しているだけだ。選定に参加する気はないからね」"

    show ode sta arm ser with std_change

    voice get_voice_filename("ode")
    odette "「……なんだって？」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「大人しく死んでもいいってことか？」"

    show yuu sta war cla rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「そうじゃない。おまえたちが脱落させあってくれれば、最後に残るのはボクたち二人だ」"

    show ode sta arm irr with std_change

    voice get_voice_filename("ode")
    odette "「二人残ったら、どうする？」"

    show yuu sta war sad rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「おじいちゃんに生きて欲しい」"

    show yuu sta war war rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「おじいちゃんは迷子になっているボクを助けてくれた。選定の参加者だと分かっているのに、家に引き取ってくれた」"

    show yuu sta war war rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「記憶がないから、未練も分からないんだよ」"

    show yuu sta war sad rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「でも、おじいちゃんと暮らすのは楽しいから。ボクは少しでも長い時間、この生活を続けたい」"

    "ガキはオレたち二人に睨まれ続けているにもかかわらず、怯むことなく言ってのけた。"

    "純粋で真剣なこいつの表情は、話したこと全てが本心だと語っていた。"

    show ode sta arm ser with std_change

    voice get_voice_filename("ode")
    odette "「もう察しはついてると思うけどよ、あたしらはこの家にジジイの未練の手がかりになるものがないかを探しに来たんだ」"

    show yuu sta war war rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「未練……？　おじいちゃんの≪死因≫じゃなくて……？」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「残念だったな。てめーの大切なジジイの死因はもう見つけてるんだ」"

    show yuu sta war war rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「そう。なら、おじいちゃんの情報に関わるものは絶対に見つけさせちゃいけないね」"

    show yuu sta war cla rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「だから、おまえたちをおじいちゃんの家には入れさせない」"

    "ガキは声のトーンを落として、凄む。"

    "まるで別人になったかのようだ。だが所詮、ガキなことに変わりはない。"

    show ode sta gra smi with std_change

    voice get_voice_filename("ode")
    odette "「はぁん、つまりジジイの未練に繋がるものがこの家にはあるわけだ。あるいは、てめー自身が知っている、か」"

    show yuu sta war sur rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「えっ……ど、どうして……？」"

    show ode sta nor gla with std_change

    voice get_voice_filename("ode")
    odette "「てめーは一々迂闊なんだよ。喋り過ぎだ」"

    show yuu sta war war rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「そっか……おじいちゃん以外の参加者に初めて会ったけど、必死なんだね。だからボクの一言一言を注意して聞いている」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「おい、もういいだろ？　これ以上このガキと話してても仕方がない。ここまで来ちまったんだから、力づくで押し入るしかないだろ」"

    "オレはオデットに向かってそう訊ねた。"

    "オデットはにやりと笑い、頷く。"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「たまにはてめーとも気が合うな。こうなっちまった以上こいつを黙らせて、ジジイが戻ってくる前に家を捜索する」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「ジジイが帰ってきたところで黙らせるのは問題ねえが、選定までまだ数日ある。その間に警察を呼ばれたら面倒だ」"

    "オデットの言う通りである。"

    "この住宅街の真ん中で人を呼ばれれば厄介なことになる。"

    "オレたちは一応パスポートやらの書類を偽造とはいえ用意しているが、警察に目を付けられれば動きにくくなるのは間違いない。"

    "元々が、マトモな生き方をしてきていないオレたちだ。ちゃんと調べられればすぐに埃だらけになっちまう。"

    show ode sta gra smi with std_change

    voice get_voice_filename("ode")
    odette "「この家には監視カメラもないんだ。てめーを喋れない状態にしちまえば……それで十分だ」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「言っておくが、オレたちに敵うと思うんじゃねーぞ？　今どいたら、許してやる」"


    show ode sta gra smi rev with std_change
    voice get_voice_filename("ode")
    odette "「てめーは自分より弱そうな相手に対しては強気だな……」"

    show fed sta nor ang with std_change

    voice get_voice_filename("fed")
    federico "「るっせえ！」"


    play music audio.battle
    hide ode
    hide fed
    hide yuu
    with std_out

    "そして、オレたちはガキの方に詰め寄る。"

    "ガキは真剣な表情を変えずに、真っ直ぐな声で言った。"

    scene bg shigetsugu02 noon large at align(0.0, 0.1)
    show yuu sta bat ser up rev at std_c
    with wipe_rl



    voice get_voice_filename("yuu")
    yuu_unk3 "「おじいちゃんは、ボクが守るよ」"


    scene bg shigetsugu02 noon
    show ode sta arm irr at std_c
    with wipe_lr

    voice get_voice_filename("ode")
    odette "「いい度胸だ。おい！　あたしは入り口の方を見てるから、てめーで片付けろ」"

    show fed sta nor ela at std_r with std_in

    voice get_voice_filename("fed")
    federico "「……任せなっ！」"

    hide fed
    hide ode
    with std_out

    "黙らせるには、喉を潰しちまえばいい。"

    "死にはしないし、数日間は喋れなくなる。"

    "細い廊下をガキの方へ踏み込み、オレはその細い首を狙って手を伸ばした。"

    with quake_fast

    "ガキはオレの手の下をくぐって避けた。"

    show fed sta nor pa2 at std_cr with std_change

    voice get_voice_filename("fed")
    federico "「すばしっこいな！」"

    "的が小さいと、こういうこともある。"

    "だが、所詮はガキ。"

    "リーチはオレの方が長いし、体格差は語るまでもない。"

    show yuu sta war sur rev at std_cl with std_in


    voice get_voice_filename("yuu")
    yuu_unk3 "「……っ」"

    play se "landing1"
    hide yuu with std_out

    "ガキはそのまま背中を見せ、部屋の奥へと走った。"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「逃げるのか」"

    "廊下から別の部屋に入っただけだ。"

    "ニンジャ屋敷でもなければ、この狭い家は物音がよく響くので、見つけるのは容易い。"

    scene bg shigetsugu02 noon large at align(0.0, 0.1), zoom(1.3)
    show yuu sta bat coo up rev at std_c
    with wipe_rl



    voice get_voice_filename("yuu")
    yuu_unk3 "「逃げないよ」"

    "ガキは入った部屋からすぐに顔を出す。"

    "オレはガキに向かって左足を振り上げた。"

    "ガキからは絶対的に手の出せないリーチ差が生まれる。"

    show yuu sta bat cla up rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「こんなのっ」"

    "ガキはその蹴りも、ひょいとしゃがんで避ける。だが、それは問題にならない。"

    play se "kick-middle"
    with quake_fast

    "オレは足を引き戻すのと同時に、かかとで攻撃をくわえた。"


    scene bg shigetsugu02 noon
    show yuu sta war sur rev at std_c
    with dissolve_long



    voice get_voice_filename("yuu")
    yuu_unk3 "「ぐっ」" with quake_fast

    "肩に当たり、ガキが一瞬ふらついた。"

    "頭を狙ったが、小癪にも避けられたらしい。"

    "足を下ろしたオレは、今度こそと思い首に向かって手を伸ばした。"


    stop music fadeout 1

    show ode sta arm irr rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「おい馬鹿！　下がれ！」"

    show fed sta nor pan at std_r with std_in

    voice get_voice_filename("fed")
    federico "「は？」"


    play music audio.kinpaku

    hide fed
    hide ode
    hide yuu
    with std_out

    "ガキはいつの間にか、オレの真下に移動していた。"

    "オレのかかとを食らった反動で、こいつは距離を詰めていたのだ。"

    "まさか、わざと食らって……。"

    "気付いた時には、すでに遅かった。"



    voice get_voice_filename("fed")
    federico "「――――――――――！！！！！」" with quake_fast

    "声にならない悲鳴が、オレの口から出ていた。"

    "止めることはできなかった。"

    "ガキはオレの股間に思い切り、パンチを食らわせやがったんだ。"

    "激痛を感じる前に、全身の力が抜ける。"

    "時間差で、股間の少し上の内臓を直接握られているかのような痛みが走った。"

    "反射的に股間を押さえ、膝をつく。"

    show fed sta nor pan at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「ぐっ……！」"

    play se "knife"
    with quake_fast

    "次の痛みは、肩だった。ガキは、攻撃の手を緩めなかったのだ。"

    "だが、それは打撃の痛みとは違う。"

    "鋭い刃物によるものだった。"

    show yuu sta eml war rev at std_cl with std_in


    voice get_voice_filename("yuu")
    yuu_unk3 "「……外したか」"

    "ガキは右手に包丁を持ち、オレの肩を刺していた。"

    show fed sta nor cla with std_change

    voice get_voice_filename("fed")
    federico "「ってええええ！」"

    "ジャケットの縫い目部分に当たったおかげで、刃は皮膚の表面を切り裂かれただけで済んだ。"

    "あの部屋は台所で、包丁を取りに寄ったのだろう。"

    show yuu sta eml sur rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「おかしいな。頸動脈を狙ったんだけど」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「ちっ……」"

    hide yuu
    hide fed
    with std_out

    "オレはすぐに体勢を整えようと思ったが、股間の痛みが抜けていないせいでうまく動くことができなかった。"

    "ガキは包丁を抜き、二撃目を狙う。"

    "包丁の先端が迫ってくるのを見て、オレはどうにか身をよじり、避けた。"

    "無様にも、廊下の床にキスをする格好になっちまった。"

    "ガキに向き直るが、躊躇する様子はなかった。"

    "ようやく痛みが引いてきた。"

    "ナイフを避けるため、オレは立ち上がろうと膝を立てた。"

    "しかし、ガキが狙ったのはナイフによる一撃ではなく、再びオレの股間だった。"

    show fed sta nor cla at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「ひぃっ」"

    "無意識のうちに、オレは伏せて避けようとしてしまった。"

    show yuu sta bat ser rev at std_cl with std_in


    voice get_voice_filename("yuu")
    yuu_unk3 "「今度こそ」"




    play music audio.odette

    "だがその時、オレの上を巨大な影が通り過ぎた。"

    scene ecg odettobt ser with dissolve_long

    "オデットがその筋肉で膨れ上がった足を振り回していた。"

    play se "tackle"
    with quake_fast

    "ガキは両手で蹴りを受け止めるが、衝撃を吸収しきれずに廊下の端まで吹っ飛んだ。"


    voice get_voice_filename("ode")
    odette "「てめーは馬鹿か。あんなガキに負けやがって」"


    voice get_voice_filename("fed")
    federico "「ま、負けてねー」"

    "口ではそう言ってみるが、さすがに無理があった。"

    "オレは股間を集中狙いされて、完全にビビってしまっていた。"


    voice get_voice_filename("ode")
    odette "「おっと」"

    "ガキは後ろに吹っ飛びながら、包丁を投げて抵抗していた。"

    "オデットが飛んでくる包丁を避けると、包丁は床に刺さる。"

    "ガキが投げた包丁は、回転せずに真っ直ぐ飛んでいた。"


    scene bg shigetsugu02 noon
    show fed sta nor ang at std_r
    with dissolve_long

    voice get_voice_filename("fed")
    federico "「てめー、何者だ……？」"

    show yuu sta war war rev at std_l with std_in


    voice get_voice_filename("yuu")
    yuu_unk3 "「ボクも分からないよ。でも、体が勝手に動くんだ」"

    show ode sta arm smi behind fed at std_c with std_in

    voice get_voice_filename("ode")
    odette "「記憶喪失だろうが、体に染みついた技術ってのは体が覚えてるらしいからなぁ！」"

    hide yuu
    hide ode
    hide fed
    with std_out

    "オデットは床に刺さった包丁を引き抜き、投げ返す。ガキが投げたよりも鋭く速く、飛んで行く。"

    play se "metal1"
    with quake_fast

    "少年がその包丁をどこからか持ち出したフライパンで弾くと、包丁を持って来たのとは反対側の部屋へ消えていった。"

    "一瞬の隙をつき、少年は再び台所の方へ姿を消した。"

    show ode sta arm smi rev at std_c with std_in

    voice get_voice_filename("ode")
    odette "「また武器かぁ……おい、早く立て！」"

    "オデットの怒号を聞き、オレはすぐさま立ち上がった。"


    play music audio.battle

    show fed sta nor irr at std_r with std_in

    voice get_voice_filename("fed")
    federico "「ちっ……今度は何だァ？」"

    hide ode with std_out

    show yuu sta eml war rev at std_l with std_in


    voice get_voice_filename("yuu")
    yuu_unk3 "「さっきは、殺そうとしたから駄目だったんだ……選定中は、脱落以外では死ねないから……」"

    "姿を現したガキは、ぼそぼそと呟く。"

    show yuu sta bat cla rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk3 "「これでどう？」"

    play se "swing"
    with quake_fast

    "ガキは両手に何かを持ち、再び投げてきた。"

    "狙いは――オレだ。"

    show fed sta nor cla with std_change

    voice get_voice_filename("fed")
    federico "「当たるかよ！」"

    hide fed
    hide yuu
    with std_out

    "投げてきたのは、ドライバーだ。"

    "10センチ程度の細長いドライバーを計４本、投げつけて来た。"

    "だが、包丁と違って目や口の中に命中しなければダメージも少ない、武器とはいえない武器だ。"

    "オレに当たることなく、ドライバーは床に刺さった。"

    "オレが後ろに一歩下がったのと同時に、オデットが飛び出した。"

    scene ecg odettobt ser with dissolve_long


    voice get_voice_filename("ode")
    odette "「こっちは二人だ。忘れちゃいけねぇ」"

    "オデットは半回転しながら、後ろ回し蹴りの体勢をとる。"


    voice get_voice_filename("ode")
    odette "「ああん？」"

    "ガキはその軌道をしっかりと見ていたのだろう。"

    "蹴った方の足の膝に左手をつき、そのまま飛び上がる。オデットの膝の上で、片手で逆立ちをしている。"

    "低い天井なので、その位置から逆立ちをすればすぐ天井に足が届く。"

    "そのまま、ガキは天井を蹴り、オレの方へと飛びかかって来た。"

    "手にはさっきのよりも大きい包丁が握られていた。"


    scene bg shigetsugu02 noon
    show fed sta nor pan at std_r
    with dissolve_long

    voice get_voice_filename("fed")
    federico "「狙いはオレかよっ」"

    "だが、一直線に来る相手を避けられないほど間抜けではない。"

    "身体能力の高さには驚かされたが、この攻撃は避けられる。"

    "ガキを避けるため、俺は右足を後ろに引いた。"

    show ode sta arm irr rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「ああもう、どうしててめーはそんなに馬鹿なんだ！」"

    play se "taoreru01"
    with quake_fast

    "オデットの罵声は戦っているはずのガキではなく、オレに向けられていた。"

    "一歩下がったオレの足は、うまく着地できずにもつれてしまったのだ。"

    show fed sta nor ang with std_change

    voice get_voice_filename("fed")
    federico "「なんだとっ」"

    "オレ自身が原因でバランスを崩したわけではない。"

    "足元にある固い何かに引っかかっていた。"

    "さっきガキが投げつけたドライバーだ。"

    show yuu sta bat coo rev at std_c with std_in


    voice get_voice_filename("yuu")
    yuu_unk3 "「今度は外さない」"

    play se "knife"
    with quake_fast

    "ガキはそのまま、オレの脇腹に包丁を突き立てた。"

    show fed sta nor cla with std_change

    voice get_voice_filename("fed")
    federico "「ぐああああっ」" with quake_fast

    "さっき肩にかすったのとは違い、右わき腹に数センチ、食い込んでいる。"

    "ガキは瞬時に包丁を抜くと、オデットを警戒して距離をとった。"

    "オレのジャケットに、溢れた血の染みが広がっていく。"

    "あばら骨に当たったので内臓は無事だが、その骨はヒビが入ってるかもしれねぇ。"

    "ガキにもう少し力があったら、致命傷になっていた。"

    show ode sta nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「ちっ……足引っ張りやがって……退散だっ」"

    "オデットの声を聞いたとき、オレの意識はすでに朦朧としていた。"

    "わずかに聞こえる物音から、ガキが追って来ていないことだけが分かった。"








    python:
        set_info_time(None)
        set_info_location("01")


    stop music fadeout 1
    scene black with dissolve_long
    pause 2
    scene black with wfade_long
    play music audio.memories
    pause 1

    "夢を、夢を見ていた。"

    "あんまりにリアルで、これももう一つの世界なのかもしれないと思っていた。"

    "オレにとってほとんど唯一の大切なもの。"

    "オレにとって、きっとまだオレしか知らない未練のこと。"

    "夢の中でもこれが夢だって分かるのは、単純だ。"

    "それは――もうありえないことだから。"

    "失ってしまった可能性だから。"

    "オレの見た夢は、もうどこかへ置いてきたはずの願望だったから。"

    "だが、こうして夢に見るのだからこそ、それが未練になっているのだろう――。"







    python:
        set_info_date(5, 30, "wed")
        set_info_time("morning")
        set_info_location("26")



    stop music fadeout 1
    scene black with wfade_long
    pause 2
    scene bg road noon with dissolve_long
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "尻が硬い、と思った。オレは、道路脇に座っていた。"

    "オデットはビニール袋を提げ、オレの横に立っている。"

    "聞けば、オデットはオレを担いだまま、再び人気のない道へと移動して来たのだった。"

    "途中、必要なものを買いに一度コンビニに寄ったらしい。"

    "脇腹には鋭い痛みが残っていたが、包帯で応急手当がされていた。"

    show fed sta nor irr at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「あんた……」"

    show ode sta arm ser rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「船上では、応急手当が重要だ。菌が入って化膿しちまうと、手遅れなことが多い」"

    show fed sta dar dar with std_change

    voice get_voice_filename("fed")
    federico "「……悪いな」"

    show ode sta arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「ったく弱過ぎるんだよ、てめーは」"

    "否定する言葉を持たなかったオレは、舌打ちすることしかできなかった。"

    "ガキと甘く見ただけではない。"

    "オレは完全に、出し抜かれていた。"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「だがまあ、あのガキは記憶喪失とかいってたが、ありゃ昔に訓練でも受けてたんじゃねーかな。それこそ……おい、どうした？」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「あんたは、オレを見捨てればよかったんじゃないか？」"

    show ode sta nor tro rev with std_change

    voice get_voice_filename("ode")
    odette "「何しおらしくなってんだ、気持ち悪い。それにな、協力するって言ったんだ。てめーにはまだ利用価値があると思ってる。あたしは約束は守るぜ、基本的にはな」"

    show fed sta dar phi with std_change

    voice get_voice_filename("fed")
    federico "「基本的にって、なんなんだよ」"

    show ode sta gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「ま、これでも飲んでろ」"

    "オデットが渡してきたのは、ペットボトルに入ったハーフサイズのワインだ。"

    "怪我人に酒は渡さないのが普通だが、こいつは普通じゃない。証拠に、オデットはすでに一本開けているようだった。"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「……チリ産か。ま、オレの国の上物が道端で売られてても困るけどよ」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「減らず口が言えるなら、余裕そうだな。ま、てめーは今週くらいは、安静にしておいた方がいい」"

    "てめーは、か。"

    "まあ、オレが何を言っても通用しないのは知っているので、ここは黙っていることにする。"

    "案の定オデットがそれ以上話さないのを見て、オレは水代わりにくいと半分くらいワインを飲んだ。チリ産のワインは値段の割にそこそこいけると知っていた。"

    "赤ワインの渋みを帯びた味は、気持ちを落ち着かせた。"

    "道端でワインを直飲みして楽しむというのはオレの国では中々ない光景だが、悪いものでもなかった。"

    "オレたちはしばらくそこでワインを飲みながらサンドイッチを食べて、ホテルへ戻ることにした。"

    show ode sta nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「次は、あたしがあいつをぶっ倒す。あのガキは、楽しめそうだったからな」"

    "白い歯をむき出しにして笑うオデットの言葉には、オレの仇をうつとかそういう気持ちは全く感じ取れない。"

    "あったらあったで気持ち悪いが――ともかく、こいつの個人的な感情だ。"

    "選定が始まってから１ヵ月以上ともなると、何を考えているのか読めるようになってくる。"

    "しょうもないことだが――オデットはあのガキと戦うのを楽しみにしていた。"








    python:
        set_info_scene("61")
        set_info_time("evening")
        set_info_location("24")



    stop music fadeout 2
    scene bg shigetsugu01 noon with fade_longest
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "学校が終わり、私は寄り道をせずに牛塚さんの家の周辺まで来ていた。"

    "道はもう完璧に覚えていて、周辺もある程度把握していた。"

    "仮に昨日の二人と鉢合わせても、路地裏を通って人通りの多いところまで逃げることはできそうだ。"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……よし、始めよう」"

    "私は気合を入れる意味も込めて、そう呟いた。"

    "今日の目的は、聞き込みだ。牛塚さんとあの女の子についての情報を少しでも多く手に入れるのだ。"

    "そう思った矢先だった。"

    show sig sta nor squ rev at std_cl with std_in


    voice get_voice_filename("sgt")
    ushizuka_unk1 "「……もしや、選定の参加者かのう？」"

    "私は背後から、声をかけられた。"


    play music audio.impatience

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「……………………え？」"

    "振り返ると、まさに今から情報を集めようとしていたご老人が立っていた。"

    "体は小さいが、いかにも頑固そうな顔だった。"

    "何かのビニール袋を持って、じーっと感情の読めない目で私を見ている。"

    "彼と視線が合い、私は硬直してしまった。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「やはり。おぬしの顔は見たことがある。そんなに目付きの悪い高校生もそう多くはない」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたは……」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬし、まさかわしのことを調べに来たのか？」"

    "牛塚さんは、脱力した立ち方をしている。"

    "選定の参加者にばったり出くわしてしまったにもかかわらず、全く動揺してはいないようだ。"

    "彼がⅪの女性に≪氏名≫を知られたときも、同じように表情を変えていなかったことを思い出す。"

    "言葉こそ意外そうな声を出しているが、その実、興味の薄そうな反応だった。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……そう警戒しないでよかろう。わしはおぬしらと敵対するつもりはないんじゃ」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしの戦場は別にあるのじゃ。今日は勝利の凱旋じゃがの」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……戦場？」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「そう、戦いじゃ」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「まさか、別の参加者と？」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「そんなことはない。わしの戦場は駅前にあるんじゃ」"

    "牛塚さんの言葉に、私は首を傾げていた。"

    "だがそれ自体、相手の会話のペースに乗せられていると焦りを感じる。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「朝早くから並んで、いい場所をとるところから戦いが始まっとるんじゃ。それで台の争奪戦に勝ったら、そこから真剣勝負じゃ」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「大当たりの演出が入ったときは最高に盛り上がるわい」"

    "場所……台……大当たり……演出……。"

    "そして駅前。"

    "大きな駅ではなかったが、駅周辺で一通りのお店は揃っていそうだった。"

    "喫茶店やファミレス、いくつかの専門店のある商店街そして……。"

    stop music fadeout 1

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「……パチンコ……ですか？」"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「はっはっは。正解じゃ」"

    "牛塚さんは胸を上下させて笑っていた。"

    "しかめ面のまま笑っているので、どうやらこのおじいさんはそもそも感情が表情に出にくい人らしい。"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「では、ご褒美にチョコレートをあげよう」"

    "牛塚さんはそう言うと、ビニール袋から板チョコを取り出し、手渡してきた。"

    "私はそのチョコを数秒見て、拒否した。"

    play music audio.impatience

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「私を油断させようとしてるんですか？」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「残念じゃの。今時の子はチョコ程度じゃ喜んでくれんか。あの子は目をキラキラさせてくれるのにのう」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたの家に住んでる、女の子のことですか？」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「はて……？　女の子は住んでいないがのう」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「とぼけないでください」"

    "私はわざと冷たい声を彼に浴びせていた。"

    "これ以上会話の主導権を取られてはいけない。ただでさえこのおじいさんの感情は読めないのだ。"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おお、怖い怖い」"

    "からかうおじいさんを、私はじっと見つめていた。"

    "迂闊に喋らない方がいい、と思ったからだ。この人が関係ないことを話すのは、会話のペースに乗せて私から情報を引き出そうとしているからかもしれない。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「さっきも言ったろう。端的に言って、わしはおぬしらと争う気はないんじゃ」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「老い先短いジジイだからの。こうやって少しだけ寿命が延びただけでも幸せモンじゃ」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おかげでしばらく行けんかったパチンコにも行けるしの。すごいぞ。選定が始まってからわしは収支がプラスなんじゃよ」"

    "彼はまた色々と話しかけてくるが、私は答えなかった。"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ただの、おぬし、帰ってくれぬか？」"

    "黙っている私を見て変化球が通用しないと判断したのか、牛塚さんはいよいよ直接的な言葉に変わった。"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしはいいんじゃが……生かしたい子もおってな」"

    "恐らく、あの女の子のことだろう。"

    "一緒に暮らしていることについては、もう裏がとれている。"

    "やはり、さっきはとぼけたのか――。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子がおのずから戦う意志を持ってくれるまでは、静かに暮らしていたいんじゃ」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「隠居したジジイの頼みじゃから、聞いてはくれんかの？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「それは、その子を勝たせたいってことですよね？　だったら……聞けない」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ま、そうじゃの。しかし、こういうのはどうじゃろう」"

    "牛塚さんはしかめ面からさらに目を細めて、喉の奥から出したような重い声で言った。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬしとは会わなかったことにしてやる。それなら、あの子もおぬしを脱落させることはないじゃろう」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「してやる、ですか？　あなたの方が年上ですけど……この状況で上から目線は間違いです、牛塚茂継さん」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしの名前を知った程度で、いい気になっておるのか？」"

    "強い口調で返した私に怯むことなく、牛塚さんは挑発的な答えを返してきた。"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「なーんての。さっきも言ったろう？　わしはおぬしらと敵対するつもりはないんじゃよ」"

    "くだけた喋り方に戻ったが、表情は変わらずしかめ面であった。"

    "結局、膠着状態が続いてしまっていた。"

    "さすがに人生経験が豊富なのだろう。私のペースには乗ってくれない。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「特におぬしは……一部の参加者と違って、何の変哲もないいたいけな婦女子じゃ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「若いうちに死んでしまったのは残念じゃが……少しでも長く生きるためには、他の参加者と関わらないのが一番じゃぞ」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「……けんな」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「なんじゃ？」"

    "私は叫びたいのをなんとか押し留めた。"

    "牛塚さんの偉そうな上から目線にうんざりしていたのだ。"

    show rnk uni ang an2 with std_change

    voice get_voice_filename("rnk")
    rinka "「私は、少しでも長く生きるためにこうしているんじゃない。答えを見つけたいから――じっとなんてしてられない」"

    "私が人の命を踏み台にして生きるべきなのか。"

    "記憶の海に消えてしまっている、自分の未練は何なのか。"

    "海晴に対して、私は最後にどういう結論を出せるのか。"

    "運命とは、本当に抗えないものなのか。"

    "その全ての答えを見つけるまで、死ぬことなんてできない。"

    "その全ての答えが見つからないなら、静かに長生きしたいなんて思わない。"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「答え……か。おぬしがどんな疑問を持っているのかは知らんが、容易いことではないぞ」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「だから……何？　あなたに何が分かるっていうんですか！」"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「はっはっは。懐かしいのう。その科白、わしの元を去ってしまった娘たちにもよく言われたものじゃ」"

    "彼が家族に見捨てられて独り暮らししていることは、この前話した主婦から聞いていた。"

    "彼の態度からすれば、かつて言われたことがあるのも納得だ。"

    "相手のことを分かった風に、上から目線で話すのだから。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……今日は、帰ります。でも、あなたのことは調べますから。忠告しておきますけど、私だけじゃないです」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「牛塚さんが思っている以上に、みんな、生きるために必死なんだと思います」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「まだまだ子供じゃが頑固で真っ直ぐじゃな。よいよい」"

    show rnk uni ang an2 with std_change

    voice get_voice_filename("rnk")
    rinka "「だから、そういう態度が！」"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「はっはっはっは……おや」"

    hide sig
    hide rnk
    with std_out

    "帰ろうとしたとき、じゃりという足音が私の前で止まった。"

    "私は、足音の主に視線が動いていた。"

    show yuu sta lau que at std_cr with std_in


    voice get_voice_filename("yuu")
    yuu_unk4 "「おじいちゃん、その人誰？」"

    show yuu sta war war with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「まさか……選定の参加者？　いや、絶対そうだ。どうして今日は、こんな……」"

    "声の主は、一昨日私が後をつけ、牛塚さんの家に住んでいると判明した女の子だった。"

    "買い物帰りなのか、大きなビニール袋を提げていた。"

    "外にはねる癖のある銀髪に、大きな瞳。"

    "毒気のない、純粋そう雰囲気をまとっていた。"

    "だが一瞬にして、彼女の瞳は氷のような冷たさを帯びる。"

    show yuu sta eml war with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「この人も、おじいちゃんの敵なの？」"

    "その時、私は頭の芯の方から痛みが駆け上って来るのを感じていた。"

    "これまでにない頭痛に、思わず頭を伏せていた。"

    show rnk uni arm imp rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「う、うわあああっ！」"

    "まずい、と思った。"

    "原因不明の頭痛だが、動けなくなれば彼らに隙を見せることになる。"

    "だが、意外にも。"

    show yuu sta hea cla with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「う、うわあああっ！　痛い！　頭が痛いよっ！」"

    "頭痛に苦しんでいるのは、私だけではなかったようだった。"







    python:
        set_info_time("night")
        set_info_location("27")


    stop music fadeout 1
    scene bg shigetsugu03 with fade_long
    play music audio.badguys
    pause 1

    $ show_hud()

    "…………その部屋の真ん中で、私はため息をついていた。"

    "自分がどういう状況にあるか、理解しているつもりだ。"

    show sig sta nor gla at std_c with std_in

    voice get_voice_filename("sgt")
    ushizuka "「言っておくが、このお茶には何も入っとりゃせんからの」"

    show rnk uni nor que rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「いえ……結構です」"

    show sig sta inn smi with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬしの身に着けている身分証やらを調べるなら、さっきとっくにやっておるよ。安心せい、これはただの親切じゃ」"

    "私は戸惑いながらも、牛塚さんから湯呑を受け取り、お茶をすすった。"

    "色からして緑というよりかほとんど黄色だった。案の定、薄い。"

    "頭痛に襲われた私は、牛塚さんに家の中まで連れて行ってもらった。"

    "そこで横になり、痛みが引くまで安静にしていた。あの子も同じようだが、まだ目を覚ましてはいなかった。"

    "少女がぴくりと動いたのを横目で見て、私はお茶を一気に飲み干した。"

    show sig sta inn lau with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ……これはこれは……」"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「助けてもらったことには感謝してます。ありがとうございました。もう、帰ります」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ふむ。好きにするがいい。言っておくが、わしの構え方は変わらんよ」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「――はい、分かっています」"

    "敵意を向けていなくても、牛塚さんが競うべき相手であることに変わりはない。"

    "それにこっちの女の子は、間違いなく私に敵意を向けていた。"

    "この子の姿を最初に見た時に起きた頭痛の理由は知りたかったが、牛塚さんの家の中に居続けるのは危険だ。"

    "目を覚ます前に離れたい。"

    "壁の薄さからして大声を出せば外には聞こえそうだが、それで誰かが助けに来てくれるわけでもない。"

    show yuu sta nor tro at std_r with std_in


    voice get_voice_filename("yuu")
    yuu_unk4 "「ああ……おじいちゃん」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「具合は……大丈夫かのう？」"

    show yuu sta nor nor with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「大丈夫。心配かけて、ごめんね」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしに謝ってどうする。ほれ、お茶でも飲んで落ち着けい」"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「ふふ……ありがと」"

    "私は、彼らのそのやり取りを見てしまっていた。"

    "短い会話だが、牛塚さんとこの子はまるでおじいさんと孫のような関係に見える。"

    "だってその子を見る牛塚さんの目は、おばあちゃんが私を見る目に似ていたから――。"

    "だから、つい立ち止まってしまったのだ。"

    "その時、少女の注意は私に向いた。"

    show yuu sta eml war with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「おまえは……」"

    "声をかけられたが、私は何も答えなかった。"

    "返事をする義務はない。このまま帰った方が、私のためだ。"

    show sig sta nor app with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おや、まだいたんじゃな」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おい。このお嬢さんは選定の参加者じゃが、わしらの敵というわけではないぞ。おまえ呼ばわりは良くないし、さっき表で睨んだじゃろう？」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「それは、失礼なことじゃよ。帰る前に謝りなさい」"

    show yuu sta nor tro with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「……うん、分かった。昼間に、この家に敵が来たんだ。二人も、おじいちゃんの家を調べに」"

    show yuu sta nor sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「だから仲間かと思って、つい警戒しちゃったんだ」"

    show yuu sta nor ser with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「ごめんなさい、お姉さん」"

    "少女は心底反省したような顔で、頭を下げた。"

    "おじいちゃんから言われて、謝る孫。"

    "二人が選定の参加者と知らなければ、見た目の違いなど気にならず、家族にしか見えない。"

    "それも作って演じているのではなく、あくまで自然にそうなっている。"

    "これじゃ、やっぱり私のペースが狂ってしまう。"

    show rnk uni arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、大丈夫……。別に怒ってはないし……仕方がないことだよ」"

    "現に私も、牛塚さんに対しては敵意をむき出しにしていた。"

    "今も決して、彼らを警戒していないわけではない。"

    "むしろこうして入り口の側に立っていることが、いつでも逃げられるようにと気を張っている証拠だ。"

    "彼女は、気になる事を言っていた。"

    "私は帰る前にそれを確認しなければならない。"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「敵が来たって言ってたよね？　それって……背の高い男女の二人組だった？」"

    show yuu sta war war with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「どうして、それを？」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私も……その人たちを警戒しているから」"

    "私が言うと、彼女は目を丸くした。"

    "牛塚さんは私たちの会話を静観している。"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたは……知ってるの？　あの人たちのこと」"

    show yuu sta nor ser with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「うん。だって今朝来たのは、その人たちだよ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……なんじゃと？」"

    show yuu sta nor tro with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「そっか。おじいちゃんにはまだ言ってなかったね。部屋が荒れてるのはそのせいなんだ」"

    "確かに、言われてみれば物が散乱しているが、私にはそれらが元々そうなっているようにしか見えなかった。"

    "生ごみや空き缶など臭いの出るゴミはほとんどないが、雑誌や新聞、衣服などが散乱していた。"

    show yuu sta nor que with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「ⅢとⅪの人。おじいちゃんも分かるでしょ？」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「顔は覚えておるが……詳しく聞かせておくれ」"

    "その時私は、帰るタイミングを完全に逸していた。"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬしも聞いて行けばよい。ただし、情報交換じゃよ」"

    "牛塚さんもそのことに気付いたのだろう、近くに座りなさいと促した。"

    show yuu sta nor ser with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「おじいちゃんのことを探しに来たあの二人が、この家に入って来たんだ」"

    show yuu sta war war with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「おじいちゃんが出掛けた、直後」"

    "Ⅺの女性とカルミナーティさんは、この家を見張っていた。恐らく、何日か様子をうかがっていたのだろう。"

    "そして、牛塚さんが朝に出掛けたことをつきとめた。だから、今日も早朝に外出すると予想をした。"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「だから、ボクが追い返したよ。女の人の方は強かったけど、男の人はそうでもなかった」"

    show rnk uni sur su2 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「追い返した！？　だって……あの二人だよね？」"

    "この子は身長こそ私と近いが、幼いし、何より華奢だ。"

    "強かったということは、少なくとも口で言って追い返したわけではないに違いない。"

    "ソーニャにあんな脅迫をした人たちがこの子に言われて納得するようにも思えない。"

    show yuu sta nor nor with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「うん。逃げられちゃったけど、Ⅲの男には深手を負わせたよ。あれなら数日間はこの家に来られないと思う」"

    show sig sta nor app rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……また暴力を使ったのか？」"

    show yuu sta nor tro with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「仕方がなかったんだ。この家を守るためにはそうするしかなかった。それに、先に手を出してきたのはむこうだよ」"

    show rnk uni nor su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと待って。君が……戦った、の？　どうやって？」"

    show yuu sta nor nor with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「分からない。体が勝手に動いたっていうか、戦い方を知ってたっていうか……」"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そんなことって……あり得るんですか？」"

    "私は、再び警戒の目を彼女たちに向けた。"

    "嘘をついているのかもしれない。この子も、私から何か情報を引き出そうとしているのではないか。"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「この子は、記憶喪失なんじゃよ」"

    show yuu sta nor que with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「おじいちゃん？」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「構わんじゃろう。それにこれを聞いたところで、おぬしは不利にはならんじゃろうて」"

    show yuu sta nor nor with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「ボクはいいけど、おじいちゃんが……まあ、大丈夫、かな」"

    show sig sta nor tro with std_change

    voice get_voice_filename("sgt")
    ushizuka "「選定が始まったとき、この子は行く当てもなく彷徨っていたんじゃ」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしと出会って、それでうちで暮らすようになったんじゃよ」"

    show yuu sta nor tro with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「ボクは自分の名前も、今まで何をやってきたかも、どうして選定の参加者になったのかも覚えてないよ」"

    show yuu sta elm war with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「だから、ボクは≪自身のカード≫の内容も覚えていない。死因や未練を探そうとしても、無駄だよ」"

    show yuu sta nor tro with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「ボクはどうしてこの国にいるのかも、忘れてしまったんだ。いや、この国が自分の国じゃないというのも、結局おじいちゃんに会ってから分かったんだけどね」"

    "記憶喪失。"

    "それは、私と共通しているものだった。"

    "異なっているのは、私と違い彼女は今までの記憶もなくしてしまっているということ。"

    "私の抜け落ちた記憶は選定の前後だけであるから日常生活に支障はないが、彼女の場合はそうもいかない。"

    "自分がどこにいるのかさえ分からないのは、想像するだけで怖ろしい。"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「でもね、すぐおじいちゃんと会えたから、ボクは苦労はしてないよ」"

    "そう言うと、彼女はにっこりと笑った。"

    "こんな笑顔のできる人が、あの屈強な女性たちを追い返したとはにわかに信じ難い。"

    "記憶喪失の場合でも、身に着いた習慣や身に着けた技術は記憶とは別の領域に保存されていて、いわゆる体が覚えている状態があると聞いたことがある。"

    "しかし、それは記憶を喪失する前から、彼女がカルミナーティさんたちと対等に戦えたということになる。"

    show sig sta nor gla with std_change

    voice get_voice_filename("sgt")
    ushizuka "「さて、まだ聞きたいこともあるじゃろうが……おぬしの番じゃよ」"

    "牛塚さんは話を打ち切り、私を細い目で見つめた。"

    "話を聞く前、確かに情報交換だと彼は言っていた。"

    "私も覚えていたので、彼らについての情報をいくつか話すことにした。"




    stop music fadeout 1
    scene bg shigetsugu03 with fade_long
    play music audio.investigation
    pause 1

    show sig sta nor nor at std_c with std_in

    voice get_voice_filename("sgt")
    ushizuka "「当然、手段を選ばない者もいるじゃろうな。彼奴らの場合、非道な手段を選んだとも言えるが」"

    "私が話したのは、彼らがソーニャとソーニャの両親にしたことだ。"

    "両親を殺すと脅し、情報を吐かせる。"

    "暴力での支配だ。"

    "私はカルミナーティさんの≪氏名≫のカードを持っているが、そのことは話さなかった。"

    "彼らは他人のカードについては話さなかったので、ここまでで等価だ。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「となると、この子が反撃したのも仕方ないことじゃな」"

    show yuu sta nor pun at std_r with std_in


    voice get_voice_filename("yuu")
    yuu_unk4 "「もう、分かった？　ボクだって、ちゃんと考えがあったんだからね！」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「分かっておる分かっておる。ほれ、撫でてあげよう」"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「えへへー」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃが、お前が怪我をするかもしれなかったんじゃ。気を付けるんじゃぞ」"

    show yuu sta nor kir with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「分かってるよっ。でも心配しないで。ボク……負ける気がしないから」"

    "見た目よりも子供っぽい、というのが私の感想だった。"

    "褒められて撫でられて、調子に乗っているように見える。"

    "だが、この子が本当にあの二人を退かせたというのであれば、その発言も相応なものになる。"

    "読めない、分からないというのが本音だった。"

    "あるいは選定に向き合っているという意味で、ソーニャの方がしっかりしていたかもしれない。"

    "この子は、そして牛塚さんも、ただ暮らしているだけにしか見えなかった。"

    show sig sta nor app with std_change

    voice get_voice_filename("sgt")
    ushizuka "「これで分かったであろう？　わしらは争う気はない。じゃから、もう関わらんことじゃ」"

    "私の考えを見透かしたかのように、彼はそう言った。"

    "偶然か意図してか分からないけれど、それはあまりに的確で、私は怯んでしまった。"

    "そして思った。"

    "歪だと。"

    "選定中にもかかわらず、彼らは本当の家族ではなく、ましてや選定の参加者同士であるのに、こうも自然に家族の形を作れるなんて――歪んでいる。"

    show rnk uni arm vig rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「でも、きっとあの人たちは諦めません。怪我が治ったら――治らなくたって、必ずまた来ると思います」"

    show yuu sta nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたや私を脱落させないと、あの人たちは生きられないから」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしらを心配しているのかな？」"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「くっ……」"

    show sig sta nor gla with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬしは、わしらの情報を集めに来たのじゃろ？　心配してどうする？」"

    show rnk uni arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……分かりません。でも、ただ、思っただけで」"

    "そう。"

    "歪なのは私も同じだったのだ。"

    show sig sta nor app with std_change

    voice get_voice_filename("sgt")
    ushizuka "「答えを知りたいと豪語していた割には、随分と曖昧な答えじゃの」"

    show rnk uni arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……嫌な人なんですね、牛塚さんって」"

    "でも、確かに彼は一貫していた。"

    "だから落ち着いているし、私も本気で敵視されているわけではない。"

    show yuu sta eml war with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「おじいちゃんを馬鹿にするの？」"

    show rnk uni nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、そうじゃなくって」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、気にするでない。ところで……さっきは何を買っておったのじゃ？」"

    show yuu sta nor que with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「これ？　さっきあいつらが来たときに、洗うやつが壊れちゃって……。よく分からないんだけど、お店の人が勧めてくれたんだ」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「洗うやつ……ああ、洗濯機の。ホース……？」"

    show yuu sta nor sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「おうちの人に聞けば分かるって言ってたけど、おじいちゃん分からない？」"

    "彼女が傍らに置いているのは、洗濯機のホースだ。"

    "私も見覚えのあるチェーン店のビニール袋に入っているので、近所のスーパーで買って来たものだろう。"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……分からんのう。どうにも機械は苦手での」"

    show yuu sta nor tro with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「洗うやつが壊れたらどうするつもりだったの？」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ここならコインランドリーは遠くないからの」"

    show yuu sta nor que with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「こいんらんどりー？」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「お金を払って洗濯機を使える場所じゃよ」"

    show yuu sta nor pun with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「もう、おじいちゃんったら！　ぱちんこをやるために節約するって言ってたでしょ！」"

    "それはどうかと思う、と私は言わなかった。"

    "この子は牛塚さんの言葉を信じてパチンコを戦場だと思っているのではないだろうか。"

    "牛塚さんは少女からホースを受け取ったあと、視線を私へ移してきた。"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「のう、おぬしならできるじゃろ？」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「…………ま、そうなるよね」"

    "二人のやり取りを見て気が抜けていたから、何となく私に話が向けられる気はしていた。"

    show rnk uni sur su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「分かりました。ホースを取り換えるくらいなら私でもできます。ただ、それだけやったら帰りますからね」"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「ありがとうおねえちゃん！」"








    stop music fadeout 1
    scene bg shigetsugu03 with fade_long
    play music audio.nichijo03
    pause 1

    show rnk uni arm ang at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「この洗濯機、全然掃除してない……ああ、もう、ちょっとビニール手袋取って来て」"

    show rnk uni nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「はー、なんでこんなに本格的にやってるんだろ」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「排水溝も……はあ……」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと、水出してもらえる？」"

    show yuu sta lau lau rev at std_cl with std_in


    voice get_voice_filename("yuu")
    yuu_unk4 "「うん、分かったよ」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、違っ、そっちじゃなくて！　お風呂場とかから持って来て」"


    stop music fadeout 1
    hide rnk
    hide yuu
    with std_out



    voice get_voice_filename("rnk")
    rinka "「――きゃあっ！」"

    "かくして、私は洗濯機の横から溢れた水でびしょ濡れになってしまったのである。"






    python:
        set_info_scene("62")
        set_info_time("evening")
        set_info_location("28")



    scene bg sentou with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "洗濯機から溢れた水は汚れも溜まっていて、私は最悪な状況になってしまった。"

    "それについてはもう思い出したくない。"

    "学校から持ち帰っていたジャージに着替えていたので、制服は無事だったことが不幸中の幸いだが、その幸いは微々たるものだ。"

    "濡れるし、臭いし、物理的な被害で言えばこの選定中で一番大きい。"

    "なんて、情けない。流されやすいのも大概にしないから、こんな目にあうのだ。"

    "牛塚さんの家でお風呂に入るのはさすがに嫌だったので、私は近くの銭湯に来ていた。"

    show yuu sta lau lau rev at std_c with std_in


    voice get_voice_filename("yuu")
    yuu_unk4 "「わーい！　大きなお風呂に入れる！」"

    show rnk jer nor que at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「……まさか直未が正解だったとはね」"

    show yuu sta lau que rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk4 "「なんのこと？」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、何でもない」"

    "彼女――いや、彼は男の子だった。"

    "一人称はボクだったし、ボーイッシュな服だとは思っていたけれど、顔の印象だけで女の子だと思っていた。"

    "私の場合、海晴が近くにいるから感覚が鈍っていたのかもしれない。"

    "確かに自分のことを『僕』と呼ぶ女の子は珍しいし、『僕』というならまず男の子だと思わなければならない。"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「はあ……」"

    "自分で自分がいたたまれなくなって、ため息をついていた。"

    show sig sta nor nor rev at std_l with std_in

    voice get_voice_filename("sgt")
    ushizuka "「若いのにため息をつくでないぞ」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あんたたちのせいだから！」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、怖い怖い……」"

    "そう、結局流れで牛塚さんとこの子も一緒に銭湯に来ていたのだ。"

    "彼が男の子だったから、お風呂で二人になることはないのは救いだった。"

    "何を話していいか分からないし、やっぱりまだ彼のことが恐かった。"

    "それに彼の姿を最初に見たときの頭痛――何かが引っ掛かっている。"

    "私が失った記憶と関わっている――ような。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほれ、お前も行くぞ」"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「うん！」"

    hide yuu
    hide sig
    with std_out

    "少年はとことこと、牛塚さんの後ろをついていった。"

    "そういえば、牛塚さんは彼の名前を呼んではいなかった。"

    "私に氏名のカードを取得されないようにしているのかもしれないが、そもそも知らない可能性がある。"

    "どうして、そんなことを思ったのだろうか。"

    "私の感じた歪さは、きっとこれも一つの理由だろう。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「名前も知らないのに、家族、か……」"

    "と、こんなことを銭湯の入り口で呟いていたら変な目で見られてしまう。"

    "私は考えるのをやめて、今は体を綺麗にすることにした。"







    stop music fadeout 1
    scene ecg rinkasento rel with fade_long
    play music audio.relaxtime
    pause 1


    voice get_voice_filename("rnk")
    rinka "「……ふぅ」"

    "温かいお湯の中で、私はため息をついていた。"

    "さっきのとは違う、リラックスした方のため息だ。"

    "家ではシャワーを浴びることがほとんどなので、こうやってゆっくり湯船につかるのは久し振りかもしれない。"

    "銭湯に来るのは、もっと久し振りだ。"

    "私が小学生くらいの頃、おばあちゃんと来た記憶がある。"

    show ecg rinkasento lon with ecg_change


    voice get_voice_filename("rnk")
    rinka "「おばあちゃん……」"

    "私は蛇口から流れるお湯よりも小さな声で、そう呟いた。"

    "時々電話やチャットはしているけれど、結局今年の３月以来一度も会っていない。"

    "私にとっての、唯一の家族。"

    "おばあちゃんの家族は私だけではないから仕方がないけれど、時々寂しくもなる。"

    "もっともおばあちゃんが田舎にいるおかげで、Ⅺの女性やⅫの男性のようなおっかない人たちに人質にされる心配が低くなっているのは事実なのだけれど。"

    show ecg rinkasento smi with ecg_change


    voice get_voice_filename("rnk")
    rinka "「……あ、レテもいたね。でもあの子は自由だし、言葉が通じないからなぁ」"

    "次に会えるのは、きっと夏休みだ。"

    "私から、会いに行こう。"

    "夏休み。"

    "私が途中で脱落しなければ、選定は夏休みの中頃に終わる計算になる。"

    "つまり生き残らなければ、おばあちゃんに会うことはできない。"

    "でも私が生き残るってことは、海晴が――。"

    "ソーニャの言葉を思い出す。"

    "――オネエサマもミハルも、ずっと生きることのできる運命もあるかもしれないであります。"

    "今はまだ何も分からないけれど、私が見つけるべき本当の答えは、きっと。"

    "ソーニャのことを思い出して涙ぐみそうになってしまったが、どうにか堪えることができた。"

    "まずは目の前のことに集中しないといけないのだ。"

    show ecg rinkasento lon with ecg_change


    voice get_voice_filename("rnk")
    rinka "「流されちゃったなら流されたなりに、この状況をうまく使うしか――ない」"

    "私は、そう思っていた。"

    "茂継さんとⅣの少年の情報をまず集めようと思っていたが、それは後回しにしていいかもしれない。"

    "彼らは私に悪い感情は持っていない――と思う。"

    "ならば、協力関係を結ぶという手もある。"

    "ⅪやⅫの人たちと対等に渡り合える≪力≫があるなら、その点での不利はなくなる。"

    "だが、仲良くなってしまったとき、私は最後に彼らを指名できるのか。"

    "今ですら、危ういっていうのに。"

    "私には海晴のような強さはない。"

    "私がソーニャに自分を脱落させるように頼まれていたとしても、実行できたとは思えない。"

    show ecg rinkasento rel with ecg_change


    voice get_voice_filename("rnk")
    rinka "「……もっと、楽しいことを考えよう」"

    "そう、例えば夏休みに見ると約束した花火大会のこととか。"

    "――あれも結局、選定が終わったあとのことだったな。"

    "何を考えても選定からは逃れられないので、私は自分の髪から垂れる水滴を数えることにした。"










    stop music fadeout 1
    scene bg sentou with fade_long
    play music audio.nichijo03
    pause 1

    show rnk jer nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……どうして待ってるんですか？」"

    "私が番台の方へ戻ってくると、牛塚さんとⅣの子がソファに座っていた。"

    "少年の方は、背もたれに体を預けて眠っていた。"

    show sig sta nor nor rev at std_cl with std_in

    voice get_voice_filename("sgt")
    ushizuka "「この子がの。ま、待ってるうちに眠ってしまったがのう」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「この体ででっかい異人さんたちと戦ったんじゃ。疲労も溜まるじゃろう」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「別に、待たなくてよかったのに」"

    show sig sta nor que rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「そう言うでない。この子は年の近いおぬしと話せて嬉しかったんじゃよ」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「恐らくかつていた場所では友達がいなかったんじゃろう。今も――近所からは避けられてるしの」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「年、近いかなぁ」"

    "身長は近いけれど、行動や表情はこの子の方が幼く見える。"

    "あらためて、少年の寝顔に目をやった。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……信じられないです。こんな小さいのに、あの人たちに負けないどころか退散させたんだなんて」"

    show sig sta nor aqu rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「信じられない……が、前にも似たようなことがあっての」"

    "私が話を待っていると、牛塚さんはにやりと笑った。"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「その前に、喉が渇いたの。コーヒー牛乳を買って来てくれんか？　わしが動いてこの子を起こしちゃ悪いしのう」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……いいですけど」"

    "自分の分と合わせて二本を買い、牛塚さんに一本を渡した。"


    voice get_voice_filename("sgt")
    ushizuka "「おっと、入浴料しか持ってきとらんかった。すまんが後で返すから許してくれんか？」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……わざとですよね？」"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、そんなことはないわい」"

    "女子高生にたかるとは、このおじいさん……呆れながらも、私は話を促した。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「この子と会って間もない頃の話じゃ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「深夜……この子が目を覚ましてしまっての。散歩につれ出してわしがこの子と歩いているときじゃった」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「急に催してしまったんじゃが、たまたま近くに公園があっての、わし一人で便所へ行ったんじゃ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「この子は好奇心旺盛での、ネズミか何かを追って公園から離れていたらしいんじゃ。わし一人できょろきょろしていると、ガラの悪い若者が３人、近付いて来ての」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「オヤジ狩り……というやつじゃの。こんなジジイが金を持っているように見えんじゃろうが、自分より弱そうな相手なら誰でもよかったんじゃろ」"

    show rnk jer nor gla with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしは一発殴られたんじゃ。それで、金を出せと言われた。連中の中には、バットを持ってる奴もおったの」"

    show rnk jer nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「ひどい……！」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃが、そこにこの子が帰って来た。この子は状況を見るなり一言、こう聞いたんじゃ」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「『その人たちは、おじいちゃんの敵？』とな」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしは、その時、肯定の返事をしてしまったことをほんの少しだけ後悔しておる」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「この子は直後、若者３人を病院送りにしたんじゃ」"

    "その手口は、あまりに流麗だったという。"

    "バットで殴りかかってきた若者の一撃を避け、バットを奪った流れで顔面に一撃。"

    "その奥にいた男性の足をバットで払って転ばせたあと、また顔面に一撃。"

    "最後、おじいさんを殴った人は逃げようとしたけれど、少年が体ごと一回転して勢いをつけてからバットを投げつけ、後頭部に命中。"

    "怯んだ隙に足を持って押し倒して、馬乗りになったあと絞め落とした。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしが止める暇もなかった」"

    "もっとも、この子が来なければ牛塚さんはもっとひどい目にあっていただろう。"

    "お金を出そうが出すまいが、暴力を振るわれた可能性は高い。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「驚くわしに近づいて、この子は平然と帰ろうと言ったんじゃ」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃがわしは、怖い――とは思わんかった。頼もしいと思ったよ。この子は、暴力で屈することがないと安心した」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「そんな戦い方を、体が勝手に動いたとでも？」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃろうな。この子は自分の体が小さいことを、力が弱いことを分かっておるんじゃろうな」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「きっと、忘れている記憶は壮絶な人生のはずじゃ。訓練と実戦の経験がなければ、子供があんな動きをできまいて」"

    "紛争地域の少年兵、というのが思いついた。"

    "ニュースの世界でしか知らないけれど、武器を持ち、戦争に参加する子供たちの写真を見たことがある。"

    "牛塚さんの話が本当ならば、彼はそういう地域の出身かもしれない。"

    "彼の死因である≪焼死≫の意味も、そのような地域なら身近なのかもしれない。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃがな、この子は良い子じゃ。純粋で……優しい。戦うのだって、わしのためじゃ」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「ⅢやⅪの人たちとは違うってことですか？」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「その人らをわしは知らん。誰かと比べてでなくての、この子のことを言っとるんじゃよ」"

    "私はこの子のことをよく知らない。"

    "だが、彼の言うことはなんとなく、分かった。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「さて、あまり長居するのもいかんし、そろそろ行こうか」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「起こすのも可哀想じゃし、この子をおんぶしてやってくれんかの？」"

    "このおじいさんは、どこまでずるいのだろうと思っていた。"








    python:
        set_info_time("night")
        set_info_location("26")

    scene bg road night with fade_long
    pause 1

    $ show_hud()

    "私は結局、この少年をおんぶして歩いていた。"

    "私とそう体格が変わらないので、休み休みだ。"

    "背中に当たる彼の体は、意外と筋肉質だった。"

    show sig sta nor nor rev at std_cl with std_in

    voice get_voice_filename("sgt")
    ushizuka "「すまんの。わしはどうも腰痛があっての」"

    show rnk jer nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……はぁ。もう、喋らないでください」"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、怖い怖い」"

    "牛塚さんは基本的に、あまりいい性格をしていないようだ。"

    "それはそうとして、この子は本当に眠りが深い。それこそ、子供のようだ。"

    show yuu sta lau sle behind rnk at std_cr, xoffset(180) with std_in


    voice get_voice_filename("yuu")
    yuu_unk5 "「むにゃ……母さ……何故死んでしまった……の…………むにゃ……」"

    hide yuu with std_out

    "少年の寝言が、かすかに耳元で聞こえた。"

    "その口調は、牛塚さんと話すときとは少し異なっていた。"

    "私ははっとして、足を止めていた。"

    "これは、まさか。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「どうしたんじゃ？」"

    show rnk jer nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「……私だって疲れます」"

    "そう答えて、視線を外した。"

    "彼に気付かれてはいない、と思う。"

    "歩きながら、私は少年の言葉を脳内で再生していた。"

    "きっと、それこそが彼の未練。"

    "夢の中では、彼が記憶喪失なことなど関係がないのかもしれない。"

    "これは想像でしかないけれど、紛争地域に生まれた彼は、幼くして母親を失ったのかもしれない。"

    "だから彼の未練は――。"

    "私は今、カードブックを持っている。確かめるのは家に帰ってからにしようと、思考を止めた。"

    "私の予想が正解でありここで本が光ってしまえば、牛塚さんに≪Ⅳ・未練≫のカードを取得したことを気付かれてしまうかもしれない。"

    "できれば穏便に、彼らの警戒心に火はつけたくない。"

    "額が汗ばむのを感じた。"

    "これは、お風呂に入った後なのに運動をした汗だ。"

    "帰ったらまたシャワーを浴びないとと思いながら、私は牛塚さんと夜道を歩いた。"






    python:
        set_info_scene("63")
        set_info_location("27")

    scene bg shigetsugu03 night with fade

    $ show_hud()

    show sig sta nor nor rev at std_cl with std_in

    voice get_voice_filename("sgt")
    ushizuka "「２階が寝室じゃ。すまんがこの子を布団に横にならせてもらえるかの？　わしはお茶を淹れとるよ」"

    show rnk jer nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……はぁ、分かりました」"

    "この期に及んで２階まで運ばないといけないのか、と思わずため息をついていた。"

    "今日はため息ばかりだ。"



    scene bg shigetsugu02 night with fade


    show rnk jer nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ここか……」"

    "寝室の扉は半分開いていて、すぐに分かった。"

    "私はこの子を布団に寝かせようと、背中から下ろした。"

    show yuu sta lau sle rev at std_cl with std_in


    voice get_voice_filename("yuu")
    yuu_unk5 "「ん……」"

    "名残惜しいのか、彼は私の腕をつかんだ。"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「ひゃっ」"

    show yuu sta lau sle rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「母さ……むにゃ……」"

    hide yuu with std_out

    "夢の中で、私を母親とでも思ったのだろうか。"

    "すぐに眠気に負け、手を離した。"

    "その力が思ったより強く、私は驚いていた。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「男子なんだよね、この子も」"

    "あらためて見る寝顔はやはり女の子のようだった。"

    "自分で言うのもなんだが、勘違いするのも無理はないと思う。"

    "もっともこの子が年相応の男子らしかったら、私は緊張してしまっていたかもしれない。"

    "恐らく２歳は年下だから、大丈夫かと思うけれど。"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あれは……」"

    "私は視界の端に、半開きになった棚を見つけた。"

    "牛塚さんの足音が聞こえないのを確認してから、私はその棚まで近づいた。"


    play music audio.memories

    "半開きになっていた引き出しだが、光が足りずよく見えないのでゆっくりと開いた。"

    "木の軋む音で少年が起きないか心配だったが、大丈夫そうだ。"

    "８割くらい開いてもまだ暗いので、スマホの明かりを当てた。"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「写真だ……」"

    "引き出しの中にあったのは、古ぼけた写真だった。"

    "数十枚、いや百枚以上かもしれない。"

    "よく見れば比較的新しいものとかなり古いものが無造作に入っていた。"

    "写真に写っているのは、ほとんどが家族写真だ。"

    "おじいさんとおばあさん、そして両親と息子という写真が多い。"

    "おじいさんはきっと――牛塚さんに違いない。"


    stop music fadeout 1

    show sig sta nor squ rev at std_cl with std_in

    voice get_voice_filename("sgt")
    ushizuka "「思った通り、抜け目ないのう」"

    "小さな声が聞こえ、私は肩を強張らせた。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「お茶が入ったんじゃが、遅いんで呼びに来たんじゃ。まあ、下へ来なさい」"

    "私は返事をせず、彼の言葉に頷いていた。"









    play music audio.nichijo03
    scene bg shigetsugu03 night with fade

    "私は昼間と同じように、牛塚さんからお茶をすすめられた。"

    "今度は一気飲みはせず、ゆっくりといただくことにした。"

    "とはいっても相変わらず、薄い。"

    show rnk jer nor apo at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「すみません。勝手に……写真を見てしまって」"

    show sig sta nor nor rev at std_cl with std_in

    voice get_voice_filename("sgt")
    ushizuka "「構わんよ。引き出しを開けっ放しにしていたのはわしじゃしのう。それに、わしを脱落させたかったらそうすればいいんじゃ」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……？」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「この老いぼれが長生きできればそれに越したことはないかもしれんが、別段これからの人生に執着もしとらんからのう」"

    "その言葉で、私は彼の引き出しの中にあった写真たちの意味を知った。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「あれはあなたの……未練なんですね」"

    "仲の良かった家族。"

    "そういえば写真の中には、旅行先で撮ったようなものもあった。"

    "今でこそ一人暮らしだが、きっと、かつてはこの家で家族仲睦まじく暮らしていたのかもしれない。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしも年じゃ。未来に希望なんぞ持たんよ。じゃからか、あの写真を見ると時々思うてしまうんじゃ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの頃に戻りたいのう……とな」"

    "未来や現在でなく、過去にある未練。"

    python:
        add_character_cards("rnk", ["5_regret"])
        add_character_cards("sig", ["5_regret"])

    "女神は未練を未来の象徴と言っていたけれど、必ずしもそうではないのだ。"

    "未練とは、諦めきれないこと。"

    "昔に戻りたいと諦められないこともまた、未練になりうるのだろう。"

    show rnk jer nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「……無理ですよ」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、分かっておるよ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「それにのう、今はあの子がいるから、寂しくないんじゃ。あの頃を思い出せるしの」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「でも……必ず終わりは来ます」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬしとでは価値観が違うかもしれんがの、終わりなぞ怖くはないぞ」"

    "牛塚さんは、あくまで平然と言ってのけた。"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「もっともあの子のことは気がかりじゃが……ふぅむ、選定が終わった後も生き残って幸せになれるか、わしにはよう分からんよ」"

    show rnk jer nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「…………私に言われても、もっと分かりません」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子の未練のことなら、おぬしも想像がついておるだろう？」"

    "牛塚さんの言葉に、私は眉をぴくりとさせた。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子の寝言は、わしも聞いたことがあるからのう。あれはきっと、あの子の眠っている記憶……まぁ、深層心理みたいなものから出たものだと思っておる」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「帰路で足を止めたとき、おぬしは何かに驚いていたからのう」"

    "気付かれていないと思っていたが、彼はわざとあの時に言わなかったらしい。"

    "やはり、まだ彼の真意は分からない。"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子の未練はきっと――叶わんことじゃ。わしと同じ……過去に向けられた未練じゃ」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「それで、選定が終わった後も幸せかどうかを気にしていたんですね」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「まさか、私にあの子をおんぶさせたのって……！」"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、さすがにそれは想定外じゃ。わしもそこまでひどいことはせんよ」"

    "牛塚さんは笑いながら言ったが、私は疑いの目を向けずにはいられなかった。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたは……何が目的なんですか？」"

    "この人の話に付き合っていると、いつまで経っても結論に辿り着かない。"

    "それが意図的なのか性格なのかは分からないけれど、私は痺れを切らしていた。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子にご飯を、作ってあげてくれんかのう？」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……わけ、分からないんですけど」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ならばこうしよう。一度でいい。このお願いを聞いてくれたら、わしの≪死因≫をおぬしに教える」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、そうじゃなくって！」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「せめて少しでも、この子の未練を叶えてあげたいんじゃ」"

    "牛塚さんは間を置いてから、私に自分の発言の説明を始めた。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしは料理がからっきしでのう。あの子が来てから食べたものと言えば、コンビニやスーパーで買ったものばかりじゃ」"

    show rnk jer nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「牛塚さんが……作ってあげればいいんじゃないんですか？」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、わしの息子の嫁にも似たようなことを言われたことを思い出したわい」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「やっぱり……一緒に住んでいたことがあるんですね」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「息子が結婚してから数年間だけじゃがのう。わしの妻は早くに死んだから、わしと息子夫婦３人で暮らしていたんじゃ」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「孫が生まれる前に息子たちは家を出て、ほとんどそれっきりじゃがのう」"

    "少しだけ切なそうに、彼は語った。"

    "彼の未練は息子さんたちと暮らした数年の中にあったのかもしれない。"

    "今まで見せなかったほど感傷的な表情を見れば、その過去が未練として刻まれているのも分かる。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おっと、話が逸れてしまったのう」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ともかく、じゃ。これに関しては、わしが料理を作っても無理なんじゃよ」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「いや……あ、もしかして」"

    "私はそこで、どうして彼が手料理にこだわるのかようやく気が付いた。"

    show rnk jer nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「あの子の未練はもしかして……、≪母親の手料理≫？」"

    "私が聞いたとき、鞄の中から光が漏れ出した。"

    "Ⅳの少年の未練に気がついたために、カードが生成されたのだろう。"

    python:
        add_character_cards("rnk", ["4_regret"])
        add_character_cards("yuu", ["4_regret"])
        add_character_cards("sig", ["4_regret"])

    "もう決して叶うことのない、彼の未練。"

    "牛塚さんは一瞬だけ私の鞄に目をやると、悟ったような表情で眉間に皺を作り、再び口を開いた。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子が母親に料理を作ってもらったことがあるのかないのか、わしには分からん」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃがあるとき、定食屋でテレビを見ていたことがあったんじゃ。他愛のないドラマじゃったかのう」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ドラマの登場人物に母親がいてのう、丁度あの子と同じくらいの息子もおった」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「その母親の作った料理を、嬉しそうな顔で食べておったんじゃ。よくある、日常の場面じゃよ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「それを見ていてのう、あの子は泣いていたんじゃ。自分でも理由はよく分からないと言っていたんじゃが……記憶の奥で思うところがあったんじゃろうな」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「テレビは時々見ておったが、あの子があんな反応を見せたのはその時だけじゃった」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「それに気付いたとき、わしの本が光って、あの子のかぁどができたんじゃ」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私に、母親の代わりをさせるってことですよね。そんなの……無茶ですよ」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……そんなことは分かっておる。じゃからおぬしも得をするよう、わしの≪死因≫を教えると言っておるんじゃ」"

    "牛塚さんは私を威圧するように、迫力のある声で凄んだ。"

    "少年のことを話していたときの朗らかな様子からの突然の変化には驚いたが、私は怯むことなく牛塚さんの目を見ていた。"

    "目を逸らさなかったのは、驚きや恐怖以上に理不尽な彼に対する怒りがあったからだ。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「きっとあなたの未練は、あなたのせいで失ったんですね」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「――分かっておる」"

    "寂しそうに吐き捨ててから、彼は頭を下げた。"

    "彼はあぐらで座っていたから、頭は私の目線よりもずっと低くくなった。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「取引のようなやり方は、おぬしに通じんことはよく分かった」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ただのジジイのお願いじゃ。気休めかもしれん。わしの自己満足かもしれん」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……あの子に、手料理を作ってやってくれんか？」"

    "私は、考えていた。"

    "一体どう答えるのが正解なのだろうと。"

    "Ⅳの少年は、選定で生き残ってもその未練が叶わないかもしれない。"

    "そもそも、私が料理を作ったところで叶うはずもないのだ。"

    "そして料理を作ったとして、その後はどうする？"

    "牛塚さんの死因を聞き、仮に私が彼を脱落させた後、あの子はどうする？"

    "彼はそこまで考えているのだろうか。"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしは、できることはやっておきたいんじゃ」"

    "この言葉で、私は彼がそこまで考えていないことを悟った。"

    "考えていないからこそ――それが彼の想いだと分かった。"

    "私がソーニャに対して思ったのと、同じことだったのだから。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……分かりました」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……本当か？」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「ただし、それっきりです。今日は遅いので……明日。明日の夜ご飯を作りますから、それっきり関わらない」"

    show rnk jer nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「牛塚さんからも、あの子にそう伝えてください――そして今後、私があなたやあの子を脱落させても、恨まないでください」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「うむ。約束しよう。わしは元々、おぬしら他の参加者を狙うつもりはなかったんじゃ」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃが……あの子が自分の意志で他の参加者を脱落させようと動き出したとき、わしは止めることはできん」"

    "彼がそう言ったのを聞き、私は黙った。"

    "ぴりりとした緊張感が走る。牛塚さんは、確かに本音を言っている。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「構いません。それは、今の状況でも同じですから」"

    "今度はあまり迷うことなく、そう答えた。"

    "こうなってしまった以上、余計な刺激をしては私が狙われる可能性もある。"

    "もっとも、私はそういった計算は抜きにしても、すでに彼の頼みは聞くことに決めている。"

    "彼のお願いが、どうしても心に響いてしまったから。"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「昔もこうできれば、わしは孤独にはならんかったかもしれんのう……」"

    "牛塚さんはぼそりと呟いた。"

    "私に聞かせるつもりはなかったのだろう、とても小さな声だった。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「では、今度こそもう帰ります。明日の夕方６時過ぎに、また来ます。買い物もして来ちゃいます」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「分かった。わしはそろそろあの子を起こすとするかの」"

    "私は牛塚さんが立ち上がるのをしばらく眺めていた。"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……どうかしたかの？」"

    show rnk jer nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「お金。さっきのコーヒー牛乳の分と、明日の買い物の分前払いしてください。お釣りはちゃんと返しますから」"

    show sig sta nor app rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ケチじゃの」"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「当然です！」"

    "料理は作ると言ったが、ご馳走するつもりはさらさらない。"

    "後払いだとまたごまかされてしまうだろうから、ちゃんと先にもらっておかないと。"

    "牛塚さんはしぶしぶではあったが、くたびれた財布から千円札を３枚ほど私に渡した。"

    "最後に挨拶をしてから、私は牛塚さんの家を後にした。"







    $ set_info_location("05")



    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "自室に入って気が抜けた私は、ジャージのままベッドへ倒れ込んでいた。"

    show rnk jer nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あー、もう！」"


    "と、枕に顔をうずめて叫んでいた。"

    show rnk jer nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴に話したら、『馬鹿かい？』では済まないな……」"

    "思わず、私はそう呟いていた。"

    "牛塚さんの情報を調べようとしていたら、そのこと自体を知られただけでなく、一緒に住んでいる少年とも出会ってしまった。"

    "しかも、何故か明日料理を作ることになってしまった。"

    "だが、これは流されたのではなく、私の意志で返事をしたことだ。"

    "選定の参加者と関わるという危険よりも、もっと重要なことがある。"

    "――こんなに感情移入してしまって、私は彼らを脱落させることができるのか？"

    "いずれ、彼らのカードを揃えたときに、その決断ができるのだろうか。"

    show rnk jer nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「シャワー、浴びよ……」"

    "考えても答えが出ない結論を後回しにすることに、慣れてきてしまっていた。"

    $ add_seen_chapter("5-3")

    jump f005_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

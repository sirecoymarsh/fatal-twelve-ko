

label f006:










    python:
        set_info_scene("75")
        set_info_date(6, 4, "mon")
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

    show rnk paj arm ten rev up at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「はぁっ、はぁっ……」"

    "目覚めた時、私は汗をかいていた。"

    "ねっとりと肌に絡みつく、嫌な汗だった。"

    "起き上がってみると、すでにレテはどこかへ行ってしまったことに気が付いた。"

    "あれは、なんだったのだろうか。"

    "アランさんにカードが行き渡った瞬間、砕けるように消滅してしまった。"

    "選んだのは≪Ⅳ・未練≫のカード。"

    "嫌な予感がする。それは、私も持っているカードなのだ。"

    "恐る恐る、私は自分のカードブックを開いた。"

    show rnk paj arm imp rev up with std_change

    voice get_voice_filename("rnk")
    rinka "「これは……嘘、どうして……！」"

    "自分で自分の声が震えている自覚があった。"

    python:
        remove_character_cards("rnk", ["4_regret"])
        remove_character_cards("aln", ["4_regret"])
        remove_character_cards("yuu", ["4_regret"])

    "≪Ⅳ・未練≫のカードが、私のカードブックから失われていたのだ。"

    "こんな現象は、今までなかった。"

    "カードが消える……未練が消える？"

    "いや、彼の未練は母親の手料理だったから、私が料理を作ってあげたところで消滅するものではないはずだ。"

    "それにもしそうなら、昨日までの時点で私のカードは減っていたはずで、牛塚さんの所持カードには含まれないだろう。"

    "とすれば、もしかして――。"

    "可能性は、ある。"

    "確かめるためにも、私は放課後に再び牛塚さんの家を訪れることを決めた。"







    python:
        set_info_time("noon")
        set_info_location("08")


    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    "学校に行くと、いよいよ文化祭に向けて忙しくなっている雰囲気があった。"

    "私のクラスはスタートがあまりに遅かったせいもあるけれど、クラスの実行委員は昼休みも多目的室かどこかで装飾の準備をしているらしい。"

    "前もってやっておけばいいのにと思いはするけれど、私たちは積極的に関わっているわけではないのであまり強くは言えない。"

    "もちろん頼まれたら手伝いはするけれど、実行委員たちからは自分たちだけでどうにかしたいというのが伝わってくる。"

    "仲良しグループ内で充実感を味わいたいという気持ちは、分からないでもない。"

    "そうなると、やはり直未のクラスはうちに比べて随分いい雰囲気なのだろう。"

    show mao uni nor che rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「んじゃ、りーたん、お昼行こっか」"

    show rnk uni nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「真央はマイペースだなぁ」"

    show mhr uni sco con at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「今のクラスはあまり居心地がいいものではないからね。今日も屋上へ向かおうか」"

    show rnk uni sur su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと、そんなはっきり言う？」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「構わないだろう。真央は手伝うことを打診したけれど、ぼくたちがいるからと無下に断ったのは彼女たちの方なんだからね」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「うちは楽だから気にしてないよーみはるん」"

    "海晴はもしかしたら、少し怒っているのかもと思った。"

    "真央の好意がどう扱われたのかは、何となく想像がつく。"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「それに、うちらの手伝いの時間はまとめてもらったしぃ。ま、感謝感謝」"

    show mhr uni sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「真央がいいならいいけれどね。さあ、凛火もそろそろ行こう」"

    "私は頷いて、二人の後についていった。"







    $ set_info_location("15")

    scene bg schoolrooftop noon with fade

    show mao uni nor no1 at std_c, xoffset(-100) with std_in

    voice get_voice_filename("mao")
    mao "「いただきます～」"

    "いつもと同じように、私たちは屋上でお昼を食べていた。"

    "この変わらない日常は、何より安心できる。"

    "買ってきたカツサンドを食べていると、屋上の扉が開き、聞き慣れた声が私を呼んだ。"


    play music audio.comicaldays

    show nom uni que que at std_r with std_in

    voice get_voice_filename("nom")
    naomi "「あ、凛火先輩いらっしゃいますか？」"

    show mhr uni nor ser rev behind mao at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「日辻さん……」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「お、なおりん！　何か久し振りだねぇ」"

    show nom uni nor smi with std_change

    voice get_voice_filename("nom")
    naomi "「真央先輩！　……未島先輩も、こんにちは」"

    "海晴は直未を見ると、つん、と視線を送っただけで言葉はなかった。"

    "その理由は何となく分かるし、恐らく直未も察しているので、そのまま本題へと入った。"

    show nom uni nor nor with std_change

    voice get_voice_filename("nom")
    naomi "「これ、先輩たちに届けに来たんです。文化祭の、コーヒー券です！」"

    "直未が手渡してきたのは、３枚つづりのチケットだった。"

    "COFFEEという文字が大きく書かれていて、下の方には小さい字で私立飴茶女子大学付属高校文化祭と書かれている。"

    show nom uni nor lau with std_change

    voice get_voice_filename("nom")
    naomi "「校長先生が私たちの企画に興味を持ってくださって、受付でこのチケットを販売してくださることになったんです。何枚かもらったので、先輩もどうぞっ」"

    show mao uni nor glo rev with std_change

    voice get_voice_filename("mao")
    mao "「おおー、すごいねぇ。せっかくなら、たくさんの人に来てもらおうってことか～」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「うちのクラスのように気の抜けた出し物をするところが多いから、日辻さんのように真剣にやるところは珍しく、学校の宣伝になるというわけだね」"

    show rnk uni nor smi rev at std_cr, xoffset(-90) with std_in

    voice get_voice_filename("rnk")
    rinka "「……そうかもしれないけど。でも、直未すごいね！　頑張った甲斐があった」"

    show nom uni nor smi with std_change

    voice get_voice_filename("nom")
    naomi "「ほ、本番はまだですけどね……。で、でも凛火先輩のおかげです！　先輩がコーヒーを教えてくれたから、わたしものめり込んで……」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「なおりんはさ、コスプレとかしないのぉ？」"

    "話の流れを断ち切って、真央が直未にそう訊ねた。"

    "直未は顔を赤くすると、あわあわしながら答える。"

    show nom uni hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「ここ、コスプレですか？　あ、あの未島先輩みたいな……」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくのはバイトの制服だよ」"

    show nom uni hes tr2 with std_change

    voice get_voice_filename("nom")
    naomi "「すす、すみません！」"

    show nom uni hes sor with std_change

    voice get_voice_filename("nom")
    naomi "「え、えっと……。そういうことしようって言ってた子はいましたけど、わたしは別に……。たぶん、似合わないですし……」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「なおりん、フラグって言葉を知ってるかい？」"

    show nom uni que que with std_change

    voice get_voice_filename("nom")
    naomi "「フラッグ……旗ですか？」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「まー、そんな感じ？　当日を楽しみに待ってるよ～」"

    "真央は戸惑う直未に向かって、にやりと笑って見せた。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「そういえばなおりん、文化祭の次の週だから……再来週の土曜日って空いてる？　またこのメンバーで遊びに行こうって話をしてるんだけど、どう？」"

    show nom uni hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「さ、再来週……大丈夫ですけど……わたしが行ってもいいんですか？　そ、その……」"

    show mhr uni nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは構わないよ。ねえ、凛火？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。まだどうするか決めてないけど、久しぶりに出掛けよっか」"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたん、うちのカラオケって案はどこ行ったの……？」"

    show nom uni nor smi with std_change

    voice get_voice_filename("nom")
    naomi "「わたし、楽しみにしてます！　あ、でもでも、ちゃんと文化祭の時は来てくださいね！」"

    show rnk uni arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「直未……あ、いや、大丈夫。残り１週間だけど、頑張ってね」"

    show nom uni nor lau with std_change

    voice get_voice_filename("nom")
    naomi "「はいっ！」"

    hide nom with std_out

    "私は自分が言いかけたことをなかったことにして、直未の背中を見送った。"

    "海晴がなんとも言い難い視線を私にちらりと見せる。そこに込められた想いは、いくつもの感情が重なっているのだと思った。"

    show mao uni nor nor rev with std_change

    voice get_voice_filename("mao")
    mao "「おふたりさん、早く食べないと昼休み終わっちゃうよぉ」"

    "ふと考え込めば女神の選定のことを考えてしまう私を、真央の気の抜けた声が引き戻してくれるのだった。"

    "晴れた空の下、今日も私は日常と非日常の境界線の上を歩いていた。"







    python:
        set_info_time("evening")
        set_info_location("14")


    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    play music audio.miharu
    pause 1

    $ show_hud()

    "放課後、私は帰宅しようとしている海晴を呼び止めた。"

    show mhr uni sco cau rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「どうしたんだい？　凛火の方からぼくに声をかけてきてくれるなんて」"

    "Ⅺの女性が来襲してきたとき海晴に助けてもらったこともあり、すでに牛塚さんたちのことを話していた。"

    "中途半端で終われるはずもなく、土曜日の夜、すでに事の顛末も話していた。"


    play music audio.investigation

    show rnk uni arm nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「昨日の……消えたカードのこと」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……残念だね。この後お茶でもと思ったけれど、ぼくはバイトがあるから付き合えないんだ」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「分かってる。だから、簡潔に。Ⅳの少年のこととか、海晴には話してるから、意見が聞きたくって」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火は≪Ⅳ・未練≫のカードを取得したと言っていたね。Ⅻの男性が取得したものと同じだ。つまり君のカードも、消えたんだね？」"

    "私が頷くと、海晴は話を続ける。"

    "その後、海晴と私は、カードが消滅した理由について、お互いの予想を言い合った。"

    "私たちはどちらも、同じ予想をしていたのであった。"

    "海晴が駅へ向かおうとしたところを、私は再び引き留める。胸につっかえていたことのうちの一つを、海晴へと話すことにした。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「それとね、もう一つ。この前の選定で脱落した……牛塚さんの話を聞いていて思ったことがあるんだ」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「彼の話……それはどんな内容かな？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「人と人の関係の話、かな。私たちは生きてる限り色んな人間関係の中にいるけど、誰かに行動を強要することはできない」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「日辻さんのことかい？」"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「どうして分かったの？」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君のことだからね。半ば無理矢理、日辻さんを選定に関わらせないようにしたことについて、迷っているんだろう？」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「先に伝えておくよ。ぼくの意見は変わらない。日辻さんが選定に関わることは、危険に足を踏み入れるということだ」"

    show mhr uni pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「でもね、凛火。確かに君の言う通りだ。君たちの行動も――心も、ぼくには強制することはできない」"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。そもそも、ぼくが凛火のために命を捧げると決めたのも自分の意志で、凛火が数度しか会っていない選定の参加者のためにお節介するのも自分の意志なのにね」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん、そうだよね」"

    "言われてみれば、当たり前のことなのだ。"

    "みんながみんな、自分の意志で行動している。"

    "私は海晴にどんなに馬鹿と言われても、桂子さんに関わり、ソーニャに関わり、牛塚さんやユウくんに関わった。"

    "そう決めた。"

    show mhr uni nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「とはいえ、日辻さんは文化祭に向けて大事な時期だ。大切なことを話すつもりなら、せめてその後をおすすめするよ」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「分かってる。ありがとね」"

    "予想はしていたけれど、やっぱり海晴は私が直未を引き留めた理由を見抜いている。"

    "思い立ったらすぐ行動しがちな私だけど、それくらいはわきまえているつもりだ。"






    python:
        set_info_scene("76")
        set_info_time("evening")
        set_info_location("26")



    scene bg road noon with fade

    $ show_hud()

    "海晴と別れたあと、私は再び牛塚さんの家の近くまで来ていた。"

    "ここに来ることは伝えていたので、「十分注意するように」と忠告されていた。"

    "失われた≪Ⅳ・未練≫のカード。"

    "ユウくんをすぐに指名できるかどうか分からなかったけれど、それを持っているか持っていないかでは大違いだ。"

    "いつかは必ず、覚悟しなければならない時が来る。"

    "それにユウくんが私の情報を集めた時に、守ることができなくなってしまう。"

    "私たちの推測が正しいかどうかの答えが、あの場所にある気がしたのだ。"

    "――だが、私は直後に自らの認識の甘さを味わうことになった。"







    python:
        set_info_time("evening")
        set_info_location("29")

    stop music fadeout 1
    scene bg shigetsugu01 ruin with dissolve

    "牛塚さんの家の前についた私は、思わず口を開けたまま立ち尽くしてしまっていた。"

    "牛塚さんの家の前――正確には、その言葉自体が違っている。"

    "私の知っている家は、もうそこにはなかったのだ。"

    "あったのは、ただの空き地のみ。"

    "あの好々爺の面影も名残もなく、残骸すらもなかった。"

    "空しさを助長するように、一陣の風が吹く。"

    "風上には、逆光で影を作る少年の姿があった。"


    play music audio.impatience

    show yuu awa nor no2 rev at std_cl with std_in

    voice get_voice_filename("yuu")
    yuu "「――どうして、ボクを指名してくれなかったの？」"

    "Ⅳの少年、ユウくん。"

    "かつてここにあった牛塚さんの家で話したのと同じように、彼の声は見た目よりも少し幼く聞こえる。"

    show yuu awa nor rev urg with std_change

    voice get_voice_filename("yuu")
    yuu "「どうして、お姉ちゃんはボクを殺してくれなかったの？　殺して欲しいって――お願いしたのに」"

    "少年の嘆願は、土曜日の別れ際に聞いたときよりもさらに、切実さが増していた。"

    show yuu awa nor qu2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「次の選定の時は、ボクを殺してくれる？」"

    show rnk uni arm ten at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……分からない」"

    "ようやく出た言葉は、それだった。"

    "私の言葉を噛み締めるように下を向いてから、彼は答える。"

    show yuu awa nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「やっぱり。このままだったら、未練を教えてもお姉ちゃんはボクの指名に踏み切れないよね」"

    "さっきよりも、彼の声は一段低くなっていた。"

    "その瞳は、運命の大広間で目にしたのと同じく虚ろであった。"

    show yuu awa nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「今は、まだお姉ちゃんは迷ってるけど……お姉ちゃんには必ずボクを殺してもらうからね」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ユウくん……記憶が戻ったんだよね？　だから、ユウくんの持っていた本当の≪未練≫がカードに変わったから、私たちの持っていたカードが消えた」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「眠っていた≪記憶≫には、何があったの？」"

    show yuu awa nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「地獄、だよ」"

    "意味が分からなかったが、彼はそれだけ言うと、一人で納得したように私に背を向けた。"

    show yuu awa nor qu2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「お姉ちゃんにも、覚悟をしてもらうよ」"

    show rnk uni arm imp with std_change

    voice get_voice_filename("rnk")
    rinka "「待って……もっと……」"

    "引き留める私の声を、彼は無視した。"

    hide yuu with std_out


    voice get_voice_filename("yuu")
    yuu "「ボクは、お前に必ず――」"

    "彼が別れ際に何を言ったのか、よく聞こえなかった。"

    "だが、彼の声音はさらに変わっていた。"

    "氷でできたナイフのように、冷たく突き刺さる。"

    "夕焼けの向こうに消えていくユウくんの姿は、まるで炎の中へ飛び込んで行くようだった。"






    python:
        set_info_scene("77")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "帰宅してからの私は、ずっとユウくんの言葉の意味を考えていた。"

    "私が彼を指名するための、覚悟。"

    "頼まれたのは確かに事実だ。だが今日は、彼の望みを達成できなかったことを謝る隙もなかった。"

    "私は再びカードを確認する。"

    show rnk paj nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「これは残ってるんだ」"

    "私たちの予想通り、彼は記憶が戻ったのだろう。"

    "≪母親の手料理≫という未練はあくまで彼が記憶を失ってからの未練。"

    "深層心理で思っていたのには違いないかもしれないけれど、記憶を失う前に未練になるほど強く思っていた何かとは違う。"

    "もし彼に記憶が戻っているのであれば、≪Ⅳ・氏名≫も一緒に消えていないとおかしいと思っていた。"

    "だが、このカードは残っている。"

    "認知の問題だというのなら、納得できないこともない。"

    "可能性は二つ。"

    "一つは、元々名前がなかったということ。"

    "もう一つは、元々あった名前を自分の名前だと思っていないこと。こちらの方が可能性は高いと思っている。"

    "例えば何か嫌な経験があって、過去の自分を捨てたい、とか。"

    "彼が異常に高い戦闘技術を持ち合わせていたのは、そうならざるをえない環境にいたからだと、牛塚さんとも予想をしていた。"

    "だとすれば、私が想像すらつかない壮絶な経験をしているに違いない。"

    show rnk paj arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「残酷だったのかな、私は――」"

    "辛い記憶を思い出したくないのであれば、記憶が戻る前に脱落したかったのも理解できる。"

    "彼は今、自分の過去と戦っているのかもしれない。"

    "私は自分の迷いのせいで、ユウくんを苦しめてしまっている。"

    "少し考えれば容易に想像がついたことだろうに、私は無意識にその想像を避けていた。"

    "誰かを脱落させる――殺す。"

    "罪を背負うことは、怖いから。"

    show rnk paj arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「直未がいたら、なんて言うかな……」"

    "一緒に罪を背負ってくれると言ってくれた直未がいたら。"

    "あの時とは違う。"

    "誰かを脱落させる一歩手前の状況に直面している今なら、なんて言うだろうか。"

    show rnk paj arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「考えても仕方ない、か。誰にも……分からないことだから」"

    "私はまた、自分で自分の心にフタをしてしまった。"

    "逃げた。"

    "未来を見落としていることにすら、気付かず。"

    $ add_seen_chapter("6-1")








    python:
        set_info_scene("78")
        set_info_date(6, 8, "fri")
        set_info_time("evening")
        set_info_location("17")

    stop music fadeout 2
    scene bg shinjukugyoen evening with fade_longest
    pause 1

    $ show_hud()

    "結局、私は文化祭があるということ以外は別段今まで変わらない日常を過ごしていた。"

    "女神の選定の情報集めも、一旦はストップしていたのだ。"

    "ユウくんの言葉が気になっていたからだ。"

    "彼が私に対して何か行動を仕掛けてくるのではないかと警戒をし、消極的に。"

    "海晴にも、そのことは話していた。"

    "協力関係は結ばないとはいえ、海晴とは実質協力している。"

    "お互いの≪自身のカード≫も含めた所持カードの情報を共有していないだけで、現状については把握していたのだ。"

    "海晴の方も、言わば攻めあぐねているらしい。"

    "アランさんともⅪの女性とも、あれ以来顔を合わせていない。"

    "アランさんは彼女たちの情報を探っていると言っていたから、私の知らないところで彼らと探り合いをしているのかもしれない。"

    show rnk uni nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「はー、全然駄目だ」"


    play music audio.nichijo03

    hide rnk with std_out

    "気分転換のために、私は公園を散歩しに来ていた。"

    "明日明後日は文化祭だ。"

    "今回の選定で私は誰も指名しなければ、誰かに指名されることもないだろう。"

    "ここのところ根詰めていたから、文化祭ではちょっと気持ちを落ち着けたい。"

    "文化祭で楽しむ心構えをするためにも、今日の内に気持ちをすっきりさせておいた方がいい。"

    "私はお気に入りのベンチに座り、遠くに見えるビル群を眺めていた。"

    "その中で一際目立つ時計台は、眼前を横切る一羽のカラスも魅力的に引き立てていた。"

    "――≪運命の終着点≫とやらがこの場所だなんて、信じられない。"

    "私にとってはあくまで、子供の頃の記憶が染みついた場所で、直未に自分の弱さを暴露した思い出の場所だ。"

    "月曜日、海晴が私を頭ごなしに否定しなかったのは意外だった。"

    "海晴は選定の途中、何か変わったのかもしれない。"

    "――いや、違う。"

    "変わったのは私もか。"

    "私がちゃんと聞いて、話すようになった。"

    "海晴もまた同じというところだろう。"

    "気付けば少しずつ、お互いの隠し事は減っている。"

    "人を強制することはできないけれど、自分が変われば相手の接し方は変わる。"

    "でも私が冷たく突き放したけれど、直未は変わらなかった。"

    "頑張って変わらずに、いてくれた。"

    "私の罪を一緒に背負うと言ってくれたその言葉の重みは、今ならもっと、ずっと。"

    show rnk uni nor apo at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「直未……」"

    hide rnk with std_out

    play se "phone_vibration1"

    "呟いた私に返事するように、スマホが振動した。"

    "誰だろうと思いメッセージを開くと、どんな偶然だろう、直未から来ていた。"

    "そこには、『何ですか？』という短文が書かれていた。"

    "おかしい。"

    "まるで私の声を聞いていたかのようなメッセージだ。通話が繋がっているわけでもないのに。"


    play music audio.naomi

    show nom uni nor lau at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「せーんぱいっ」"

    "その声は私の後ろから聞こえた。"

    "まるで幻聴かのように。"

    show rnk uni sur su2 rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「うわぁっ、直未！」"

    show nom uni har pal with std_change

    voice get_voice_filename("nom")
    naomi "「すす、すみません！　そんなに驚かせてしまうなんて思いませんでした……」"

    show rnk uni sur su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「い、いやそれはいいんだけど……あれ？　どうして？　準備は大丈夫？」"

    show nom uni nor smi with std_change

    voice get_voice_filename("nom")
    naomi "「は、はいっ！　準備も大部分が終わってるので、今日はみんなで早く帰ったんです」"

    show nom uni nor nor with std_change

    voice get_voice_filename("nom")
    naomi "「その分、明日は早朝からなんですけどね」"

    show nom uni que que with std_change

    voice get_voice_filename("nom")
    naomi "「凛火先輩って、遠足の前日にそわそわして眠れないって経験ありませんでしたか？」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私は……あんまり」"

    show nom uni nor sur with std_change

    voice get_voice_filename("nom")
    naomi "「せ、先輩らしいです。え、えと、わたしはそんな子だったんです」"

    show nom uni hes shy with std_change

    voice get_voice_filename("nom")
    naomi "「それで、あの……緊張とか不安とか、そういうので落ち着かなくって……。ここに来れば落ち着くかなって思ったら、先輩がいて」"

    show nom uni nor lau with std_change

    voice get_voice_filename("nom")
    naomi "「あ、そ、その、実はわたしたまにこの場所に来てたんです。凛火先輩が教えてくれたこの場所、わたしもすごく、好きだから」"

    "直未はそう言うと、頬をピンクに染めてはにかんだ。"

    "私もその顔につられて、つい口角が緩んでしまう。"

    show rnk uni nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「直未はリーダーだしね。大変だ」"

    show nom uni har pin with std_change

    voice get_voice_filename("nom")
    naomi "「も、もうプレッシャーかけないでくださいっ」"

    show nom uni hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「わたしって地味だから、ただでさえこういうの初めてで……。昔から、引っ込み思案だったから……」"

    show rnk uni arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ふふっ、大丈夫だよ」"

    "笑っちゃいけないのは分かっているけれど、何だか直未のことがとても可愛らしく見えた。"

    "等身大に、一生懸命に悩んでいる姿が、うらやましくもあった。"

    "でも、私がつい微笑んでしまった一番の原因は――。"

    show rnk uni nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「初めて会ったときからは、考えられないね」"

    show nom uni hes shy with std_change

    voice get_voice_filename("nom")
    naomi "「も、もうっ。恥ずかしいから思い出さないでください！」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「懐かしい。あれはまだ４月の最初で……」"












    stop music fadeout 2
    scene bg schoollibrary with wfade_longest
    play music audio.memories
    pause 1

    "それは、新入生は入学式、私たち２年生は始業式のあとすぐの土曜日。"

    "その日、午前授業で終わった私だが、宿題の提出率があまりに悪かったせいで居残りでやるようにきつく注意されていた。"

    "好きで宿題をする時間がなかったわけじゃない。"

    "３月末からおばあちゃんが長期にわたって田舎へ行くから荷物の整理と、これから始まる私の一人暮らしの準備をしていただけでなく、ライオン館の仕事も教えてもらっていて、時間がなかったのだ。"

    "もっとも、そんなのは私の事情。"

    "言い訳するようで悔しかったので、私は先生にそのことは話さず、図書室にこもろうと決めていた。"

    "新学期が始まったばかりなので生徒はほとんどいなかったが、一人、先客がいた。"

    show nom gun nor nor rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「…………っと……」"

    "それが今年の新入生である、日辻直未だったのだ。"

    "入学してすぐなのに図書室に来るなんて、よっぽど本が好きなのだなと思ったものだ。"

    "私は空いている机に座って、溜まった宿題を広げた。"

    "直未は少し離れた席で、本を何冊か机に重ねて読んでいた。"

    "今思えば、それらはその時に読むつもりでいたものだから、かなりの速読家という片鱗はあった。"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……楽しいのかな」"

    "私はそんなことを考えていた。"

    "借りていって家で読んだ方が、コーヒーを飲みながらとか寝っ転がりながらとか、自由にできるだろうに。"

    "とはいえ、新学年早々に残った宿題を片付けている私が言える科白ではない。"

    "その後、何時間くらい図書室にいただろうか。"

    "外はとっくに暗くなっていたと思う。"

    "閉館時間も過ぎ、追い出される前に出ようと思った私は、直未がまだいることに気が付いた。"

    "ただし今度は読書をしているのではなく、本棚を探しているようだった。"

    "ずらりと何百冊も並んだ本の背表紙を、一つ一つじっくりと。"

    show nom gun har con rev with std_change

    voice get_voice_filename("nom")
    naomi "「……あわわ」"

    "実際に口にしていたか定かではないけれど、慌てた声が聞こえてくるようだった。"

    "表情も態度も、困っていますと主張していた。"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「ねえ、どうしたの？」"

    show nom gun hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「…………あ……す、すみません……、もう、帰りますから」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、私別に図書委員とかじゃないし。困ってるように見えたけど？」"

    show nom gun hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「あの…………え、えっと、その……」"

    "私は、自分の悪評を思い出した。"

    "真央が、私は歩いているだけで噂になると言っていた。１年生に届いていてもおかしくはない。"

    "髪に金色のメッシュが入っていて、目付きが悪くて、背が小さい――自分で言っていて悲しくなるが、それだけ特徴が揃っていれば私だとすぐに分かるだろう。"

    "つまりこの子は私に話しかけられて怖がっているのだと、時間差で理解した。"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「まあいいや。何か探してるんでしょ。それだけ教えて。勝手に手伝うから」"

    show nom gun hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「えっ……、そ、その、でも……」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「もうちょっとすると、見回りの先生来て追い出されるよ。手伝うなっていうなら帰るけど、困ってるんでしょ？」"

    "この時の直未は、面白かった。"

    "上を見て下を見て左右を確認してから上目遣いで私を見て、「えっと……」と口を開いたのだ。"

    show nom gun hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「じ、自分の手帳を……文庫本と間違えて……しまっちゃって……」"

    show nom gun hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「本を読みながら歩いてたら、間違えたことにも気づかなくって……その……」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「おっちょこちょい？」"

    hide rnk
    hide nom
    with std_out

    "どうやらその手帳は、入学祝に母親からもらったものらしい。"

    "それを新学年早々なくすとは、中々だ。"

    "しかも本棚に間違えて戻すというのは、斬新な物のなくしかただ。"

    "とはいえ可哀想だし、図書館の蔵書数を考えると誰かが見つける可能性も低いだろう。"

    "日が経てば経つほど本の入れ替わりなどで紛れてしまうに違いない。"

    "私は直未と二手に分かれて、本を探した。"

    "まだ帰宅していない私たちを、先生が注意しに来た。"

    "私は先生の前に立ち塞がって、時間稼ぎをした。"

    "どうにか１時間程引き留めることができたのだっけか、正確なところは覚えていないけれど、そのうちに直未が手帳を発見した。"







    python:
        set_info_time("night")
        set_info_location("14")

    scene bg schoolgate night with fade_long

    show nom gun nor smi rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「ほほ、本当にご迷惑をおかけしましたっ！　ありがとう……ございました。先生も、説得してくれて……」"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「説得って言うのかな、あれ。まあでも、見つかって良かったね。さ、帰りな」"

    show nom gun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、あの、駅まで……一緒に……」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「私と一緒にいるところを見られたら、変な噂でも立つかもよ？」"

    show nom gun que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「う、噂……？　ど、どうしてですか？」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「だってさっき、私のこと怖がってなかった？」"

    show nom gun har ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「怖がって……た？　い、いえ！　あれは……その……恥ずかしくって」"

    show nom gun hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「あんななくし方、普通しないじゃないですか……」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「それもそうだね」"

    "気にしていた私が、馬鹿らしくなってしまう。"

    "この子は私の噂なんて知らなかったし、外見で私を怖がってなんていなかったのだ。"

    "単純なことだけど、その時、私は不思議な気持ちになっていたような気がする。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「獅子舞凛火。よろしくね」"

    show nom gun nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「獅子舞先輩……。わたしは日辻直未ですっ。よ、よろしくお願いします……」"

    "この日から直未が私を凛火先輩と呼ぶようになるまで、一週間もかからなかったかもしれない。"

    "ちなみに帰り道、直未は何もないところで転んだ。"

    "こんな何でもない出会いだったけれど、私にとっては印象深い想い出になっていた――。"











    stop music fadeout 2
    scene bg shinjukugyoen evening with wfade_longest
    pause 1



    "想い出話をした私たちは、お互いに笑い合っていた。"


    play music audio.naomi

    show rnk uni nor que rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「そういえばさ、なんで図書室で手帳を出してたの？」"

    show nom uni hes shy at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「読んだ本の題名とか感想とかを、書くようにしてるんです。わたしにとってはそれが日記の代わりで……、同じ本でも、読む日によって感想が変わることもありますし」"

    "２ヵ月越しで、私の疑問は解決した。"

    "なるほど、几帳面な直未らしいなと思っていた。"

    show rnk uni arm ama rev
    show nom uni har sur
    with std_change

    voice get_voice_filename("rnk_nom")
    rinka_naomi "「ねえ、直未。月曜日に言おうと……」\n「あの、先輩。月曜日に言った……」"





    "二人同時に話そうとして、言葉同士がぶつかった。"

    "恥ずかしくなって口を閉じ、今度は沈黙が流れる。"

    show rnk uni nor que rev
    show nom uni hes sor
    with std_change

    voice get_voice_filename("rnk_nom")
    rinka_naomi "「えっと……」\n「あの……」"





    "今度は一言だけで、直未はほぐれた表情で笑う。"

    show nom uni hes shy with std_change

    voice get_voice_filename("nom", 309)
    naomi "「えへへ、どうぞっ」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk", 878)
    rinka "「……うん。文化祭が終わったら話そうって考えてたんだけどさ、この機会だし、言うね」"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私が直未を、突き放しちゃったこと。謝ろうと思って」"

    show rnk uni nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめんね。私の勝手で、遠ざけちゃって」"

    show nom uni nor sur with std_change

    voice get_voice_filename("nom")
    naomi "「そ、そんなっ。だって凛火先輩はわたしのこと、心配してくれたから……それは分かってるから、そんな、謝らなくっても、その……」"

    "あわあわとする直未の目を、私はしっかりと見据えた。"

    "今は気を遣わなくていい――そのことを伝えたくて。"

    "直未は口を一文字に結んで、頷く。"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私は、やっぱり弱いまま。だからね……もし、もし直未がよければ……」"

    "私が言いかけたところで、直未は私の体に腕を回して抱きついてきた。"

    "強く引き寄せるように、直未の指が私の背中をつかんだ。"

    show nom uni nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「答えなんて……決まってるじゃないですか……」"

    show rnk uni arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「――ありがと」"

    show nom uni har ser with std_change

    voice get_voice_filename("nom")
    naomi "「ああっ、すみません、ついっ」"

    "直未はすぐに私の体を離し、行き場をなくした両手を宙ぶらりんにさせていた。"

    "私はそんな両手を右手で握ってから、左手も重ねた。"

    show rnk uni nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……まあでも、まずは明日と明後日の文化祭、頑張ってね」"

    show nom uni nor lau with std_change

    voice get_voice_filename("nom")
    naomi "「はい！」"

    "それからしばらく、私たちは他愛のない話をした。"

    "閉園時間を告げるアナウンスを聞いて、公園を後にする。"

    "本当に、不思議だ。"

    "こんな短い時間だけど――私はさっきよりもずっと、心強さを覚えていたのだから。"

    $ add_seen_chapter("6-2")








    python:
        set_info_scene("79")
        set_info_date(6, 9, "sat")
        set_info_time("noon")
        set_info_location("31")



    stop music fadeout 2
    scene bg schoolcorridor festival with fade_longest
    play music audio.nichijo04
    pause 1

    $ show_hud()

    show mhr uni nor nor rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「おはよう、凛火」"

    show rnk uni arm nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あ、おはよう」"

    "私が今週のことを思い返していると、海晴が登校して来た。"

    "私たちはクラスの出し物の手伝いをするため、待ち合わせをしていた。"

    "厄介者は３人まとめられているので気楽だ。あとは真央だけ。"

    show mhr uni sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「今週ずっと考え込んでいるように見えたけれど、少しすっきりしたようだね。何かあったのかい？」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「何か……ううん。ちょっとお散歩しただけ」"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ……そうかい。難しい顔をする凛火も魅力的だけれど、今日くらいは気分転換をした方がいい。日辻さんの頑張りの成果も、見に行くのだろう？」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「意外だね。海晴が直未のこと気にするなんて」"

    show mhr uni nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そうかな？　ぼくも、ちゃんと彼女が頑張っていたことは認めているよ」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「そうだね」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「やっと笑ってくれたね。ぼくでも君を笑わせることができて、安心しているよ」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「大げさなんだから、もう」"

    show mao uni sel irr at std_r with std_in

    voice get_voice_filename("mao")
    mao "「おはよう～。いやぁ、寝坊しちゃったよぅ」"

    "５分ほど遅れて、真央がやって来た。"

    "目の下にはうっすらとクマを作り、眠そうな顔をしている。"

    show mao uni nor sle with std_change

    voice get_voice_filename("mao")
    mao "「文化祭だからよゆーと思って、つい家にあるマンガを読み返しちゃってたよ……あー、ねむ」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「平日だって同じでしょ。ま、ちょっと早めに待ち合わせしておいたし大丈夫。行こうか」"








    scene bg schoolcorridor festival with fade_long
    pause 1

    show mao uni nor glo at std_c with std_in

    voice get_voice_filename("mao")
    mao "「お疲れ～」"

    show mhr uni sco dis rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「……何とも形容し難い中途半端さだったね、ぼくたちのクラスの企画は」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「占いの館という安直な名前なのはともかくとして、部屋を暗くして水晶を置いておけば雰囲気が出ると思っているようだね」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「予算がないから衣装が黒い布をまとうだけというのは仕方がないけれど、ぼくたちの仕事がお客さんの占い結果を印刷して渡すだけというのは面白みに欠けるよ」"

    show rnk uni arm ama at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「海晴、今日毒がすごいね」"

    show mao uni nor glo with std_change

    voice get_voice_filename("mao")
    mao "「まあまあ、うちはそれなりに楽しめたよー」"

    "海晴の言う通り、私たちのクラスの出し物である≪占いの館≫ははっきりいって微妙だった。"

    "占い自体はＰＣゲームに詳しい子が購入したソフトをダウンロードしたものを使っていたので、楽しいは楽しい。"

    "画面に生年月日や情報を入力すると、星占いをベースにした占い結果が表示される。"

    "希望者には、それを印刷して渡すというものだ。"

    "恐らくゲームの開発者に許可をとっていないので、かなりグレーな企画だ。というか１回100円でお金を取っているのでブラックかもしれない。"

    show mao uni sel glo with std_change

    voice get_voice_filename("mao")
    mao "「しかし、これでやっと文化祭を堪能できるねぇ」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「日辻さんの喫茶店へ立ち寄ったら、ぼくは図書室で午後まで時間を潰して帰宅させてもらうけどね」"

    show mao uni sel glo with std_change

    voice get_voice_filename("mao")
    mao "「うちも～。まあでもみんな頑張ってるし、せっかくだし校内一周はしとかないとねぇ」"








    scene bg schoolcorridor festival with fade_long
    pause 1

    show mao uni sel irr at std_c with std_in

    voice get_voice_filename("mao")
    mao "「あー、疲れたねぇー」"

    "私たち３人は、本当に校内を一周したのだった。"

    "真央のいいところなのかも分からないが、文化祭は自分が興味がなくても誰かしら頑張っている人がいるのだから、無碍にはできないらしい。"

    "はっきりと口には出さないが、去年から行事の度にこんな調子だったので、海晴も私も不満はない。"

    "もっとも講堂で行われる吹奏楽部の発表や、校庭のステージで行われる企画へは参加しないので、自己満足と言われればそれまでなのだけれど。"

    "とにもかくにも、飾りつけがされ浮ついた雰囲気の校内を回ってみると、新たな発見があるのは事実だった。"

    "そしてもう一つ、気付いたことがある。"

    show mao uni sel lau with std_change

    voice get_voice_filename("mao")
    mao "「校内、カップ持ってる人が多いよねぇ」"


    show mhr uni nor nor rev at std_l with std_in
    voice get_voice_filename("mhr")
    miharu "「プラスチックのキャップのついた紙コップだね」"

    show mao uni nor no1 with std_change

    voice get_voice_filename("mao")
    mao "「繁盛してるってことですなぁ。校内で持ち運べるようにしたのは正解かもだねぇ」"

    show rnk uni nor que at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「直未、頑張ってるかな」"

    show mao uni nor lau rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんも気になる？　んじゃ、そろそろなおりんの教室に突撃しよ～」"

    "校内を回っている時に一度通り過ぎたので、場所は分かっている。"

    "廊下には、徐々に人が増え始めていた。"

    "私たちはいつもとは違う賑やかな雰囲気の校内を、再び歩き出すのだった。"







    $ set_info_location("32")


    scene bg schoolroom festival with fade_long
    pause 1

    show mao uni sel lau at std_c with std_in

    voice get_voice_filename("mao")
    mao "「お～、飾りつけしてある～」"

    "１年生の教室は３階で、廊下の奥の方に直未のクラスがある。"

    "受付でチケットを販売している効果なのか、お客さんは多いようだった。"

    "片方の扉を入り口、片方を出口としている。出口からは紙コップを持ったお客さんが何人か出てきている。"

    "その光景は、まさにチェーン店さながらだった。"

    "とはいえ、メインは休憩所のような役割だ。"

    "ドリップするところは見られるようになっていて、それも一つの出し物になっている。"

    "入る前からコーヒーのいい香りがしていたので、期待できる。"

    "学校の中で普段嗅ぐことのないこの香りが人を惹きつけているのも繁盛の理由だろう。"

    "私はチケットをちぎって、海晴と真央に渡した。"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「あれ、なおりんは？」"

    show rnk uni nor que at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「見当たらないね」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ちょっとうち聞いてみるよぉ」"

    hide mao with std_out

    "受付の子に、真央が直未のことを尋ねる。"

    "チケットを持っていない人は、ここでお金を支払うらしい。"

    "一杯200円という価格は、かかっている予算を考えれば妥当だろう。"

    show mao uni nor che rev at std_c with std_in

    voice get_voice_filename("mao")
    mao "「なおりん、資材が足りないってことで友達と一緒に追加の買い物に行ってるみたい。さっき出たばっかりだから、ちょっと時間かかるかもって」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「予想外に人が来てるみたいだよぉ」"

    show mhr uni sco con rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「日辻さん、場を任せられるようにきちんとしていたんだね。さすがだよ」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「どうする？　また後で来る？」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「せっかく来たし、いただいてこっか。またちょっとしたら来ればいいし」"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「そうだねぇ。うちも座りたかったしぃ」"

    "という結論に、海晴も頷いた。"

    "私たちはチケットを渡して、コーヒーを淹れてもらうことにした。"




    stop music fadeout 1
    scene bg schoolroom festival with fade_long
    play music audio.comicaldays
    pause 1

    "椅子こそ授業で使うものと同じだが、テーブルクロスや小物で雰囲気が演出されていて、文化祭の賑やかさに疲れた時でもリラックスできる空間になっていた。"

    "コーヒーも、香りが立っているし、かなり頑張っていると思う。"

    "一生懸命みんなに教える直未の姿が目に浮かぶ。"

    "戻ってきたら、直未に淹れてもらったコーヒーも飲んでみたい。"

    show mhr uni nor nor at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「日辻さんも、ライオン館が好きみたいだね」"

    show mao uni sel glo rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「言われてみれば、小物とかのセンスも似てるよねぇ。出張版？」"

    show rnk uni arm ama at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「直未はうちに通ってたし、小物を一緒に買いに行ったりしてたからかな」"

    show mhr uni sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。そうだね。きっと凛火の影響だ」"

    "真央はお砂糖を一個追加して、ミルクも追加した。"

    "ちらりと見えるカップの中の液体は、ほとんど白になっている。"

    "カップに口をつけながら、真央は話題を変えた。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「そいやさ、最近１年に転校生来てたりしてったっけ？　白い髪の小さい子なんだけど、見覚えがなくって」"

    show mao uni nor lau rev with std_change

    voice get_voice_filename("mao")
    mao "「朝来るときにちらーって見かけたんだよねー」"

    show mhr uni sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「転校生……かい？　分からないよ。ぼくはあまり他の学年のことは知らないからね」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「私も。真央、よく見てるね」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「いや、あの子は一回見れば覚えてるはずだよぉ。りーたんに負けず劣らず尖ってたからねぇ」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「高１にしてはちょっと幼い感じだけど、ボーイッシュな顔つきで可愛い感じ。あれはバレンタインにチョコもらいまくりですなぁ」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「――そんなに、印象的だったのかい？」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「そうだねぇ。なおりんのとこに遊び行くとき、どのクラスの子か聞いてみよっか？」"




    play music audio.gimon

    show rnk uni arm imp with std_change

    voice get_voice_filename("rnk")
    rinka "「ま……さか……」"

    "真央の話す見覚えのない１年生の外見が、パズルのピースがはまるように私の脳内で輪郭を作っていく。"

    "白い髪で、ちょっと幼いボーイッシュな顔つき。"

    "私の知っている中で、そんな子は一人しかいない。"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、考え過ぎかな。制服を着てたんでしょ？」"

    show mao uni nor no1 rev with std_change

    voice get_voice_filename("mao")
    mao "「そ。だから１年生の子って分かったんだけど……お、帰ってきたみたいだよ～」"

    "入り口の方から、大きなビニール袋を提げた女子生徒が入ってきた。"

    "しかし、そこに直未の姿はなかった。"

    hide mao with std_out

    "真央は聞いてくるねと言って、また裏側を覗きに行った。"

    show mao uni nor lau rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「なんか、なおりん知り合いがいるかもって挨拶しに行ったんだって」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「しかもぉ、今話した１年の子みたいなんだけど、挨拶って何があったのかなぁ？」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「――――嘘！」"

    "私は思わず、そう叫んでいた。"

    "考え過ぎではない。"

    "理由は知らない、だけど。"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめん、どっかで待ってて」"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたん？」"

    show mhr uni nor ser rev with std_change_wait

    "私は海晴に目配せをした。"

    "海晴も、私と同じことに思い当たったらしい。"

    hide rnk with std_out

    "言い訳と真央のことは海晴に任せて、私は走って教室を飛び出した。"

    "いる。"

    "――ユウくんがこの校内に、いる。"









    $ set_info_location("31")

    play music audio.impatience
    scene bg schoolcorridor festival with fade

    $ show_hud()

    "廊下に出ると、相変わらずの賑やかな空間が広がっていた。"

    "人もさらに増えたようで、ここの模擬店に並ぶ列も長くなっている。"

    show rnk uni ang an2 at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「直未はっ――！」"

    hide rnk with std_out

    "近くにはいないようだが、遠くは見えない。"

    "特徴的な白髪も見当たらないということは、この階にはいないのかもしれない。"

    "その直後だった。"

    "鼓膜を震わせるような轟音が、浮ついた空気を吹き飛ばした。"

    "校舎全体が、振動した。"

    "地震にしてはあまりに短く、弱い。"

    "しかし、何かトラブルが起こることなど想定していなかった生徒やお客さんたちは、騒然とし始めた。"

    "今の音が一体何のかという、不安混じりの疑問が飛び交う。"

    "ぴしりと、頭痛が走った。"

    "この頭痛は、ユウくんと再会した時に走ったのと似た痛みだ。"

    "再会――そうだ、牛塚さん宅の前で彼と鉢合わせたのは、再会であった。"

    "私が忘れている記憶はまだ戻って来てはいないけれど、深層心理が警鐘を鳴らしている。"

    "とにかく、音のした方に行ってみるしかない。"

    "すでに収まり始めたざわめきの中を、私は駆け抜けていった。"

    "突然の避難指示を促す放送が流れたのは、私が階段を駆けている時だった。"








    $ set_info_scene("80")


    stop music fadeout 2
    scene bg schoolcorridor festival with fade_longest
    play music audio.investigation
    pause 1

    $ show_hud()

    "直未が名前も知らない少年を追いかけたのは、彼の瞳に見覚えがあったからだった。"

    "もし必要なものが売り切れていた場合の判断や、買い物の見落としを防ぐため、直未は友人とともにリーダー自ら買い出しに出掛けた。"

    "案の定、あらかじめ用意していた小物と同じものはなかったが、代替品になるものを購入することができた。"

    "初日はある程度トラブルが起こることは、直未も予想していた。"

    "もちろん気持ちは万全だったが、初めてのことで予想外の事態が起きない方が珍しい。"

    "模擬店の様子も気になるため、早足で学校まで戻った――そこまではよかった。"

    "生徒に混じり、白髪の少年が校内を歩いていたのだ。"

    "彼は飴茶の制服を着ていた。"

    "少年とはいえ幼く中性的な顔つきのせいで、一見すればただの女子生徒にしか見えない。"

    "しかし、直未は彼が選定の参加者だということを知っている。"

    "凛火の敵になりうる人物だということを知っている。"

    show yuu uni nor qu2 at std_c with std_in


    voice get_voice_filename("yuu")
    yuu_unk6 "「…………」"

    "彼はきょろきょろとしながら、校内の様子を見ていた。"

    "直未は、あるいは彼は人を――凛火を探しているのだと思っていた。"

    "凛火は校内にいるはずだから、彼のことを連絡しようと考えたが、スマートフォンの電源は切れていた。"

    "準備万端だったにもかかわらず、直未は携帯の充電だけを忘れてしまっていたのだ。"

    show yuu uni nor no2 with std_change


    voice get_voice_filename("yuu")
    yuu_unk6 "「…………」"

    "直未はこの時点でもう、自分が何とかしないと、と周りが見えなくなってしまっていた。"

    "一緒にいた友人に言い訳をして、少年を尾行することに決めた。"

    scene bg schoolcorridor festival large at align(0.0, 0.5)
    show nom uni nor ser rev up at std_l
    with wipe_lr

    voice get_voice_filename("nom")
    naomi "「あの子……違う……」"

    "少年の、獲物を探す獣のような瞳。"

    "駅で見かけたときとは、全く様子が違っていた。"

    "直未は直感で、彼が何か事を起こすつもりだと確信したのだった。"

    "心臓の音は、痛いくらいにどんどん速さを増していく。"

    "そして直未は、頭痛を覚えていた。"

    "凛火にも話した、凛火が炎に包まれて死んでしまう夢のこと。"

    "それは、「なかったこと」になった事故の記憶だ。"

    "だが、どうにも腑に落ちないことが多かった。"

    "事件の詳細、原因、犯人、その全て。"

    show nom uni nor ser up rev with std_change

    voice get_voice_filename("nom")
    naomi "「――犯人？」"

    "直未は少年を追いかけながら、自らも記憶に追い立てられていた。"

    "どうして、犯人などという言葉に思い当たったのだろう？"

    "答えは簡単だ。"

    "――あの少年の、瞳を見たからだ。"


    voice get_voice_filename("nom")
    naomi "「あの子との因縁は、凛火先輩だけのものじゃない。わたしも……わたしも！」"

    "頭痛が激しくなるにつれて、直未の脳に焼き付いていた夢が現実の記憶へと変わっていく。"

    scene bg schoolcorridor festival
    show yuu uni nor no2 at std_c
    with wipe_rl


    voice get_voice_filename("yuu")
    yuu_unk6 "「…………」"

    "人を探しているはずなのに、彼は人気のない方へと向かっているようだった。"

    "こうなると、尾行は難しくなる。"

    "それでも直未は、彼の後についていっていた。"

    show yuu uni nor no2 with std_change


    voice get_voice_filename("yuu")
    yuu_unk6 "「…………」"

    hide yuu with std_out

    "やがて、彼はとある教室へ入った。"







    $ set_info_location("08")

    scene bg schoolroom empty with dissolve

    "少年が入って行ったのは、文化祭で使われていない空き教室だった。"

    "模擬店や出し物で使わない机や椅子などは、一時的にこの教室に集められている。"

    "そのおかげで、直未は隠れる場所を見つけることができていた。"

    "だが、直未の期待はすぐに打ち砕かれることとなる。"

    show yuu uni nor no2 rev at std_cl with std_in


    voice get_voice_filename("yuu")
    yuu_unk6 "「もう、隠れなくていい」"

    show nom uni har pal at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「はにゃっ！」"

    "いきなり声をかけられて、直未は驚きの声をあげた。"


    play music audio.kinpaku

    "間抜けな声ではあったが、今はそれを恥ずかしがっている場合ではないと彼女自身分かっている。"

    "しかしどんなことを話せばいいのか分からず戸惑っていると、また彼の方から口を開いた。"



    voice get_voice_filename("yuu")
    yuu_unk6 "「お前がⅠ番の大切なものだということは、分かっている」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「あの時――電車の中でⅠ番は、お前をかばって死んだから」"

    show nom uni har pin with std_change

    voice get_voice_filename("nom")
    naomi "「り……先輩の――死！」"

    "直未はぞくりと背筋が凍っていくのを感じていた。"

    "自分の記憶が間違っていなかったと思うたびに、悪寒は酷くなっていく。"



    voice get_voice_filename("yuu")
    yuu_unk6 "「お前自身に恨みはない。だけど、お前には犠牲になってもらう」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「あの人は、ボクを殺さなくてはならないんだ」"

    show nom uni nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「あなたは……何を言っているんですか？」"


    stop music fadeout 1

    show yuu uni nor qu2 rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk6 "「あの人はボクを生かしてしまった。ボクを目覚めさせてしまった」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「ボクは生きていてはいけない人間だ――たった一つの生き方しかできないから」"

    hide yuu
    hide nom
    with std_out

    "直未が少年の言葉の意味を理解しようと思っていたとき、狭い教室の中に閃光が走った。"

    "ほとんど同時に、空気を震わせるほど大きな音が轟いた。"




    play se "bomb2"
    scene white with dissolve_fast
    pause 1
    play ambient "fireloop" fadein 2
    scene bg schoolroom enjo with Dissolve(3)
    pause 1

    "部屋中の空気が振動し、窓ガラスは膨れ上がった空気に叩きつけられ、ひび割れる。"

    "叫ぶ間もなく、直未は吹き飛ばされていた。"

    "爆弾――それが自分自身の因縁でもあることを、直未はとうに思い出していた。"




    play music audio.death
    scene ecg nomdeath with dissolve_long


    voice get_voice_filename("nom")
    naomi "「い……た……い……」"

    scene ecg yuufire obscurity:
        subpixel True
        yalign (1.0)
        linear 20 yalign (0.0)
    with dissolve



    voice get_voice_filename("yuu")
    yuu_unk6 "「お前の尾行には気が付いていた。元々お前をこの教室に連れて行こうと思っていたから、助かったよ」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「この部屋の机の中に、複数の爆弾を仕掛けていたんだ。お前を――殺すために」"

    scene ecg nomdeath with dissolve


    voice get_voice_filename("nom")
    naomi "「い……た……、ど……う……し……て…………」"

    "至近距離で爆風を浴びた直未の体は左半身が焼けただれていた。"

    "爆散した破片は肉体の至る所に突き刺さり、衝撃で腹部の骨も折れていた。"

    "呼吸は荒かったが、いつ消えてもおかしくはないほど細い。"

    scene ecg yuufire obscurity at topleft with dissolve



    voice get_voice_filename("yuu")
    yuu_unk6 "「選定の参加者っていうのは、皮肉だね。こんな狭いところで爆発させればボクだってただでは済まないはずにもかかわらず、傷は頬の切り傷一つ」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「風向きや壁になった机に偶然助けられ、守られている」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「……もう、喋れないようだね」"





    scene bg schoolroom enjo with dissolve_long

    "教室には、火種となった破片がまばらに飛び散っている。"

    "ひび割れた窓はやがて崩れ落ち、外から空気と大量の酸素の供給を受ける。"

    "焚き火にもならないほどの小さな火は、一瞬にして燃え上がった。"

    "動くことのできない直未は、自分の体が熱に包まれていくのを感じることしかできなかった。"

    "徐々に弱くなっていく、感覚の中で。"

    scene ecg yuufire obscurity at topleft with dissolve_long



    voice get_voice_filename("yuu")
    yuu_unk6 "「これだけ派手にやれば、あっちの方も問題なさそうだね」"

    scene ecg nomdeath with dissolve


    voice get_voice_filename("nom")
    naomi "「な……ん……で……」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「……まだ喋れたのか。さっきからそればっかりだね、お前は」"

    "燃え広がっていく炎の中、少年は冷たい声で続けた。"

    scene ecg yuufire obscurity at topleft with dissolve



    voice get_voice_filename("yuu")
    yuu_unk6 "「ボクは死ななければならない。生きていちゃいけない人間なんだ」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「でもね、せめてその死には意味があると信じたい。あの人に殺されれば、ボクの死にも意味があったと思えるんだ……きっと」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「あの人はボクを殺せなかった。このままではずっと同じ。だから、覚悟してもらう」"

    scene ecg nomdeath with dissolve


    voice get_voice_filename("nom")
    naomi "「ど……し……て……」"

    scene ecg yuufire obscurity at topleft with dissolve



    voice get_voice_filename("yuu")
    yuu_unk6 "「……しつこいな。もう間もなく死ぬだろうけれど、余計なことを話されると厄介かもしれない」"



    voice get_voice_filename("yuu")
    yuu_unk6 "「一思いに、殺してあげるよ」"


    scene bg schoolroom enjo with dissolve_long

    "少年は直未に近寄ると、首元を両手で握った。"

    "彼の声に、迷いや不安や躊躇いはなかった。"

    "だが、それでも――。"

    scene ecg yuufire sad at topleft with dissolve_long


    voice get_voice_filename("nom")
    naomi "「な……ん……で……、あな……たは…………かなし……い……顔……を…………してい……る……の……」"

    "直未は死の淵で、獣のような瞳の奥にある哀しみを見ていた。"







    stop music fadeout 1
    scene bg schoolroom enjo with dissolve_long




    voice get_voice_filename("yuu")
    yuu_unk6 "「黙れ」"


    scene black with dissolve
    play se "bone_crunch" 
    pause 2

    "そして少年は直未の喉を潰したあと、首を90度以上曲げてみせた。"

    "骨が潰れていく音は、燃え盛る炎がかき消していた。"

    scene bg schoolroom enjo with dissolve

    show yuu uni eml wa2 rev at std_cl with std_in



    voice get_voice_filename("yuu")
    yuu_unk6 "「ん……？」"

    "少年は、部屋の入口で足音が止まるのを聞いた。"

    "反射的に、教室の扉に視線を送る。"

    show rnk uni ang an2 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「直未！」"

    show yuu uni nor no2 rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk6 "「……丁度いいところに来たね」"

    "汗だくになった凛火の叫び声もまた、地響きのようにうなる炎の音にかき消されていた。"








    $ set_info_scene("81")

    stop music fadeout 2
    scene bg schoolroom enjo with fade_longest
    pause 1

    "火災報知器が鳴ったのだと、放送で流れていた。"

    "しかし、もうそんなの必要ない。"

    "私の目の前では、視界が真っ白になるほどの炎の海が広がっていた。"

    "そして部屋の中心近く、二人の影が炎に照らされている。"

    show rnk uni arm uil at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あっ、ああっ…………」"

    "状況を理解することが、すぐにはできなかった。"

    show rnk uni arm uil with std_change

    voice get_voice_filename("rnk")
    rinka "「ああああっ、なおっ、あっ」"

    "声がうまく出せず、煙がさらに喉を焼いた。"

    show rnk uni arm uil with std_change

    voice get_voice_filename("rnk")
    rinka "「ああっ……なおっ……なっ……あっ」"

    "何が起きているのか、分からない方がよかったかもしれない。"

    show rnk uni sur scr with std_change

    voice get_voice_filename("rnk")
    rinka "「直未ぃ！」"


    stop ambient fadeout 1
    play music audio.kinpaku

    hide rnk with std_out

    "電池の切れた人形のように、その体は宙ぶらりんになっていた。"

    "少年――ユウに支えられてようやく、足を伸ばしていた。"

    "彼が手を離した瞬間に、彼女の体が崩れ落ちた。"

    "私は直未の体を受け止めようと走った。"

    "だが、間に合うはずもない。"

    "直未の体が床に落ちるのとほとんど同時に、燃え広がった炎が彼女の制服に引火した。"

    "それでも、私は直未に向かっていた。触れたかった。"

    "自分の体が尻餅をついていたことに気付く。"

    "ユウはいつの間にか目の前にいて、私を転ばせていた。"

    show rnk uni ang an2 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「お前が……お前がやったのか！」"

    show yuu uni nor no2 rev at std_cl with std_in

    voice get_voice_filename("yuu")
    yuu "「ボクは昔から、英雄になるようにと刷り込まれてきた」"

    show yuu uni nor urg rev with std_change

    voice get_voice_filename("yuu")
    yuu "「英雄なんていうのは、使う側にとって都合のいい言葉に過ぎない――そんなことは分かっていたけど、ボクにはそれしかない」"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「両親を知らず、友人を知らず、仲間も知らなかった。かつてのボクにあったのはただ、すべきことだけ」"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「継続的に与えられる命令をこなしていれば、ボクは生きることができた。無価値な毎日だ」"

    show rnk uni sur scr with std_change

    voice get_voice_filename("rnk")
    rinka "「わけわかんないこと、言うなよ！　直未は！　直未に何をした！」"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「お前を殺したときも、ボクにとっては命令の一つだった。無価値な毎日の延長で、ボクは死ぬ」"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクには、ボク自身にとって無価値な英雄という言葉が贈られるはずだった」"

    show yuu uni nor urg rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクは変わってしまったんだ」"

    show rnk uni arm imp with std_change

    voice get_voice_filename("rnk")
    rinka "「救急…………直未……助けなきゃ…………直未、直未ぃ……っ」"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「価値ある人生というものを知ってしまった。でも、記憶を取り戻したボクはそんなものは望めない」"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ならせめて――ボクはお前に価値ある死を贈られたい。そう死ねるのは、人間だけだ」"

    show yuu uni nor urg rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクは、人間だ。人形なんかじゃないんだ」"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクを殺して、運命に決着をつけてみせろ」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「ふざけんな！」"

    "ユウの言葉なんて、一切が耳に入って来なかった。"

    "私の視界には、ただ直未だけしか映っていない。炎すら見えない。"

    "熱も感じず、私は立ち上がる。"

    "煙の中を這うように、直未に手を伸ばした。"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「好きにすればいい。ボクたちはこれで死ぬことはない」"

    show yuu uni nor no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「最後にこれだけ言っておくよ」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「直未を……！」"

    show yuu uni nor urg rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクだって、簡単に殺されるつもりはないよ」"

    show rnk uni ang an3 with std_change

    voice get_voice_filename("rnk")
    rinka "「直未を返せえええっ！」"

    "私の視界には、ユウは映っていない。"

    "だから彼がいつ姿を消したのかなんて、どうでもいい。"

    "ただ、一つ言えるのは。"

    "直未に触れたとき、気付いてしまったということ。"

    "――もう、手遅れだっていうことに。"




    python:
        set_info_scene("82")
        set_info_time("lnight")
        set_info_location("01")



    stop music fadeout 2
    scene ecg pattern nor a with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    show let sta nor sm1 at std_c with std_in


    voice get_voice_filename("let")
    lete_unk1 "「こんばんは、お嬢さん」"

    show let sta nor tro with std_change


    voice get_voice_filename("let")
    lete_unk1 "「辛かったようだけれど――これも一つの運命だ」"

    "やめて。"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「炎の中で、君はやっと真実を思い出したのだろう？」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「もう見ない振りはできないね」"

    "いらない。"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「ふふ、今夜は多く喋るのは無粋なようだね。それでは、簡潔にいこう」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「ようやく、運命と向き合う刻だ」"





    stop music fadeout 2
    scene ecg bomb nor with wfade_longest
    play music audio.kinpaku
    pause 1

    "私は、リュックの中に爆弾を見つけていた。"

    "よく分からないけれど、筒と袋で構成されたものだった。"

    "スローモーションのように、覚えている。"

    "火花が散り、袋の中の液体に引火する。"

    "爆音とともに、炎へと引火したのだ。"

    "リュックの持ち主は、今やはっきりと思い出せる。"

    scene bg train enjo with dissolve




    voice get_voice_filename("yuu")
    yuu "「ボクは、英雄になるんだ」"

    "この時、私は本を持っていなかったから、彼が何を言ったのか分からなかったはずだ。"

    "けれども、今はどうしてか理解していた。"

    "まずは、少年が吹き飛ばされた。"

    "ほとんど同時に、近くにいたサラリーマンが巻き込まれる。"

    "帰宅ラッシュで満員だったから、きっと彼にとっては被害が最大になる好機だったことだろう。"

    "焼けた脂の匂いが、漂う。"



    voice get_voice_filename("rnk")
    rinka "「直未っ！」"

    "私はまず第一に、直未に覆い被さった。"

    "自分の背中に衝撃を感じ、そのまま私の体は直未ごと宙に浮いた。"

    "異状を感知した電車はすぐに停止したが、その頃にはもう車内は大パニックだった。"

    "私の体は、爆風によって破壊されてしまっていた。"

    "どこの骨が折れたとか、難しいことはよく分からなかったけれど、もう助からないことだけは分かっていた。"

    "熱風を浴びながら、案じるのは直未のことだけだった。"

    "自分が助からないと分かっているのだ、私にはもう直未を守ることしか残されていない。"

    "直未は頭を打って、意識を失っていた。"


    play music audio.firedeath



    voice get_voice_filename("yuu")
    yuu "「…………くっ…………」"

    "偶然なのかは分からない。"

    "あの少年は、私の目の前に吹き飛ばされていた。"

    "私たちは二人とも、業火に焼かれ続けていた。"


    voice get_voice_filename("yuu")
    yuu "「………………やった…………ボク……は…………英雄に…………」"


    voice get_voice_filename("rnk")
    rinka "「ふざ…………け…………る……な…………」"

    "言葉を交わしたかどうか、定かではない。"

    "このやり取りは、私の心が生み出した妄想かもしれない。"


    voice get_voice_filename("rnk")
    rinka "「お前は…………英雄なんかには……なれ…………ない……」"


    voice get_voice_filename("rnk")
    rinka "「人間ですら………………ない……」"


    voice get_voice_filename("rnk")
    rinka "「ただ…………の……人形…………だ…………がっ」"

    "少年は、恐らく最後の力を振り絞り私の首を掴んだ。"

    "そのまま親指に力を入れ、私の喉を潰した。"

    "その瞬間、燃え上がった炎により発生した熱風で、彼は車外へと弾き飛ばされた。"


    voice get_voice_filename("nom")
    naomi "「せんぱい！　せんぱい！　凛火せんぱい！」"

    "私は今際の際に、直未の叫び声を聞いていた。"

    "燃え広がっていく炎とは対照的に、命の灯が消えるのは一瞬だった。"


    scene black with wfade_longest
    pause 1

    "私の忘れていた過去。"

    "深層心理が目を背けていた真実。"

    "火事に巻き込まれたと思い込んでいるだけでは、どうりでカードが出ないはずだ。"

    "私の死因は、喉が潰れたことによる窒息死だったのだから。"

    $ add_seen_chapter("6-3")








    python:
        set_info_scene("83")
        set_info_date(6, 10, "sun")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom rain with fade_longest
    pause 1

    python:
        show_hud()
        add_character_cards("rnk", ["1_death"])
        add_character_cards("mhr", ["1_death"])

    "目覚めた時、雨音が聞こえた。"

    "窓を見ると、朝にもかかわらず外は暗く、細い雨粒が無数に降り注いでいた。"

    "梅雨の始まりの朝だった。"

    "雨を嫌がったであろうレテが、部屋の隅で丸くなっていた。"




    play music audio.rain

    "昨日から今にかけてのことは、あまりよく覚えていなかった。"

    "炎の中で気を失っていた私は、海晴に助けられたらしい。"

    "どうやって家に帰ってきたかは記憶にないが、私は制服すら脱がずに、しかも床の上にそのまま倒れ込んで朝まで眠っていたらしい。"

    "文化祭を悲劇に仕立てた炎は、夢ではなかったらしい。"

    "スマートフォンで調べると、小さなニュースになっていた。"

    "どうやら、爆弾テロとは報道されていないらしい。"

    "理由なんか知らない。"

    "単純に、まだ現場検証が終わっていないだけなのだろうか。"

    "どんな風に報道されているかなんて、私には関係ない。"

    "だって、もう――。"

    "火事は結局、甚大な被害になる前に消火された。"

    "軽い火傷を負った私以外に、被害者は一人しかいない。"

    "かけがえのない、たった一人。"

    "直未しか、いなかった。"

    "死者、一名。"

    "その一人が――直未なのだ。"

    "頭の中で繰り返すたび、私自身が現実を拒絶した。"

    "嫌だ、嫌だ、嫌だ。"

    "そんな想いが、私の中でぐるぐる回る。"

    show rnk uni sur scr at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「私の、せいだ」"

    "私のせいで、直未は死んだ。"

    "私が選定に巻き込んだから。"

    show rnk uni arm uil with std_change

    voice get_voice_filename("rnk")
    rinka "「私の、せいで」"

    "直未が死んだ。"

    "私が直未を拒絶していれば。"

    "一緒に罪を背負ってなんて、言わなければ。"

    "私がもっと、強ければ"

    "全ては泡沫の夢に過ぎない。"

    "失われてしまった可能性に過ぎない。"

    "だってこれが、現実。"

    "だってこれは、運命。"

    "体には、どんどん力が入らなくなっていく。"

    "この日、私はライオン館無期限休業の貼り紙をした。"

    "喫茶ライオン館開業以来、初めてのことだった。"

    $ add_seen_chapter("6-4")

label sentei6:

    call set_replay








    python:
        set_info_date(6, 10, "sun")
        set_info_scene("84")
        set_info_time("lnight")
        set_info_location("07")



    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall
    pause 2
    scene bg fatalhall01 up large with dissolve
    pause 1

    $ show_hud()

    show dia sta fro no2 big at std_c with std_in

    voice get_voice_filename("dia", 132)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "女神の声が、煩かった。"

    "運命の大広間へと連れて来られた私は、黙ってただ下を向いていた。"

    "何も言わず、何も見ず。"

    scene bg fatalhall01 up with dissolve

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln", 168)
    alan "「…………異様だな」"

    show fed sta nor ama ci at ci_r with ci_in

    voice get_voice_filename("fed", 141)
    federico "「お前のしかめっ面がか？」"

    show aln sta nor tre rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「……フン」"

    show fed sta nor ang ci with ci_change

    voice get_voice_filename("fed")
    federico "「何だてめえっ、その反応！」"

    show dia sta fro glo ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「あら、威勢がよろしいですわね。もしかして今宵は貴方サマが……」"

    show aln sta nor clo rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「虚勢だろう」"

    hide aln
    hide fed
    hide dia
    show sca sta nor joy ci at ci_r
    with ci_swap


    voice get_voice_filename("sca", 1)
    scale_num "「おいおい、いい加減あんたたちだけの空気にするのはよしてくれよ」"

    $ gameinfo_cardbook_sca_unlocked = True

    show sca sta nor nor ci with ci_change


    voice get_voice_filename("sca")
    scale_num "「そろそろ、おれも混ぜてくれよ」"

    show yuu sta nor non rev ci at ci_l with ci_in

    voice get_voice_filename("yuu", 238)
    yuu "「…………ん」"

    show sca sta nor joy ci with ci_change


    voice get_voice_filename("sca")
    scale_num "「ちなみに、おれもⅫのお兄さんに一票だ。職業柄、人の嘘には敏感でね」"

    hide yuu
    show aln sta nor irr rev ci at ci_l
    with ci_swap

    voice get_voice_filename("aln")
    alan "「…………探偵か何かか？」"

    show sca sta nor smi ci with ci_change


    voice get_voice_filename("sca")
    scale_num "「ＨＡＨＡＨＡ、さあね。それは内緒さ。おれが不利になっちゃうのはお断り」"

    hide aln
    show ode sta arm irr rev ci at ci_l
    with ci_swap


    voice get_voice_filename("ode", 193)
    odette_num "「ったく、うるせー連中だ。いい加減もういいだろう。とっとと始めてくれ」"

    show ode sta nor nor rev ci with ci_change


    voice get_voice_filename("ode")
    odette_num "「この連中の会話ってのは、知性が足りなくていけねぇ」"

    show sca sta nor joy ci with ci_change


    voice get_voice_filename("sca")
    scale_num "「言うねぇ、マダム」"

    show ode sta gra smi rev ci with ci_change


    voice get_voice_filename("ode")
    odette_num "「メルシーボク、とでも答えておこうかい？　ま、そこはセンキューの方がいいかな」"

    show sca sta nor nor ci with ci_change


    voice get_voice_filename("sca")
    scale_num "「お好きな方でどうぞ」"

    show ode sta nor gla rev ci with ci_change


    voice get_voice_filename("ode")
    odette_num "「かかっ、食えねぇ奴だが、歯ごたえは良さそうだ」"

    hide ode
    hide sca
    show rnk uni arm uil ci at ci_r
    with ci_swap

    "煩い。"

    "煩い煩い。"

    "もう、どうだっていい。"

    show mhr uni nor ser rev ci at ci_l with ci_in

    voice get_voice_filename("mhr", 313)
    miharu "「…………君は……」"

    "海晴の声だって、聞こえない。"

    "何を話しかけられたって、届かない。"

    show dia sta fro no2 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「賑やかなのは結構ですけれども、終わりがなさそうですわね。この辺りで始めますわよ、皆サマ？」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでは、今宵も女神の選定を始めますわ」"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「廻りなさい。運命の大時計」"

    "時計が回り出し、女神が一人ずつに指名の意志確認を始めた。"

    "私は反応もせず、無視をした。"


    voice get_voice_filename("dia")
    parca "「おや、おやおや」"

    "確認は、あっという間に一周してしまった。"



    scene bg fatalhall01 up
    show dia sta nor ama rev ci at ci_c
    with dissolve_long


    voice get_voice_filename("dia")
    parca "「６度目の選定にして、ついに脱落者ゼロですわね」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「皆サマが健闘なさっている証拠……なのでしょうか？」"

    show sca sta nor smi ci at ci_r with ci_in


    voice get_voice_filename("sca")
    scale_num "「ＨＡＨＡＨＡ、かもしれないねぇ」"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro glo big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者はなし。これをもって、選定を終了といたしましょう」"

    "私はただ無感情のまま、夢の世界から現実へと引き戻されるのであった。"

    "いっそこれが夢なら醒めなければいいのにと、思っていたにもかかわらず――。"

    $ renpy.end_replay()
    $ add_seen_chapter("6-5")

    $ persistent.sentei6_clear = True
    $ grant_achievement("divine_selection_06")

    jump f007_1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

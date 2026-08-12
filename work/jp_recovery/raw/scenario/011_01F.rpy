

label f011_01F:







    python:
        set_info_scene("175")
        set_info_time("evening")
        set_info_location("04")


    scene bg lion01 evening with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    show rnk apr nor nor at std_cr with std_in

    voice get_voice_filename("rnk", 1587)
    rinka "「……ふぅ」"

    "一日の仕事を終えて、私は一息ついていた。"

    "机に座って勉強ばかりやっていたから、久々の立ち仕事はちょっぴり疲れる。"

    "といっても、やっぱりライオン館でのお仕事は楽しい。"

    "今日は土曜日ということもあり、常連さんも多く来てくれた。"

    "食事のメニューがほとんどないのでお昼時は空いていたが、それでも常に半分以上の席が埋まっているという、私が店長代理を始めてから一番混んだ日となった。"

    play se "bell02"

    "私が客席に座っていると、扉の開く鐘が鳴った。入ってきたのは、見慣れたお客さんだった。"

    show nom sun que que rev at std_cl with std_in

    voice get_voice_filename("nom", 504)
    naomi "「……あ。もしかしてもう閉店でしたか？」"

    show rnk apr nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、直未。直未なら気にしなくていいよ」"

    show nom sun hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「す、すみません」"

    "私は直未にいつものテーブルに座ってもらった。"

    "キッチンでコーヒーを２杯淹れて、私も直未の正面に座った。"

    scene ecg girlstalkR2 smi with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「はい、今日はサービス」"


    voice get_voice_filename("nom")
    naomi "「あ、ありがとうございますっ。せんぱい、ご機嫌ですね」"


    voice get_voice_filename("rnk")
    rinka "「そう？　やっと期末試験が終わってお店を開けられたからかな」"

    show ecg girlstalkT2 uwa with ecg_change


    voice get_voice_filename("nom")
    naomi "「あ、あの。実は今日、クッキーを焼いてきたんです」"


    voice get_voice_filename("rnk")
    rinka "「ありがとう。私、このクッキー好きなんだ」"

    "一目で、前に作ってくれたのと同じものだと分かった。"

    "包みのリボンは、私の好きな赤色。"

    "クッキーとコーヒーのお供に、二人で他愛のない話をした。"

    scene ecg girlstalkT2 ser with dissolve


    voice get_voice_filename("nom")
    naomi "「そういえば先輩、昨日のあの後……」"

    "直未から聞かれて、私は昨日あったことを話した。"

    "海晴の過去の話や細かい会話の内容はもちろん伏せて、告白の返事を求められたけれど、私はまだ返事をできなかったということだけを。"

    "直未は妙にほっとしたような表情を浮かべていた。"

    "きっと、海晴が自分も生き残る覚悟を決めてくれたことも話したからだろう。"

    show ecg girlstalkT2 nor with ecg_change


    voice get_voice_filename("nom")
    naomi "「前に見せてくれた日記帳は、もう読み終わったんですか？」"

    scene ecg girlstalkR2 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「期末試験が始まっちゃったから止まってたけど、今日から再開。それでさ、たぶん今日読み終わる」"

    scene ecg girlstalkT2 anx with dissolve


    voice get_voice_filename("nom")
    naomi "「……分かりました。明日の閉店後、ご迷惑じゃなければまた来ても大丈夫ですか？　海晴先輩にも、来てもらって」"

    scene ecg girlstalkR2 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「そうだね。何の情報も得られなくても、日記に書いてあったことを話すよ。百年前の日記だから、それだけでも面白かったしね」"


    voice get_voice_filename("rnk")
    rinka "「明日の夜の選定で何もできなくても、もう一度機会は来る」"


    voice get_voice_filename("rnk")
    rinka "「落ち着いて行こうと、思うんだ」"

    scene ecg girlstalkT2 uwa with dissolve


    voice get_voice_filename("nom")
    naomi "「――はい。それでえっと……日記帳、明日貸していただくことはできますか？」"

    "直未は頷いた後、恥ずかしそうに訊ねてきた。"

    "状況次第かな、と私が答えると、直未は嬉しそうに笑ってくれた。"







    python:
        set_info_time("night")
        set_info_location("04")

    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    "どうやら、私は本を読むときは夜の方がいいらしい。"

    "自分でドリップしたコーヒーを傍らに置いて、日焼けした匂いの残る日記帳を開く。"

    show lete normal at cat_c with std_in


    voice get_voice_filename("cat")
    lete "「にゃーお」"

    "黒猫のレテが、足元で丸くなっている。"


    hide lete with std_out

    "もう７月ともなると、夜でも蒸し暑い。ライオン館の床はひんやりとしているから、涼みに来たのだろう。"

    "仕方がないから、ミルクの皿を近くに持ってきてあげた。"

    "この日記を書いた私のひいひいおばあちゃん。"

    "ダイアナさんのお姉さんのリンダさんも、レオという黒猫を飼っていたという。"

    "こんな風にコーヒーを飲みながら、猫と一緒に日記を書いていたのだろうか。"

    "人間というのは、時代と環境こそ変わってもやっていること自体はそう変わらないのかもしれない。そんなことを思っていた。"

    "あらためて、私は日記帳からしおりを取った。挟んでいたしおりは、奇しくも猫の形をしていた。"







    stop music fadeout 1
    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    "２杯目のコーヒーを飲み終えるのと、私がその日記帳を読み終えるのはほとんど同じタイミングであった。"


    play music audio.gimon

    show rnk paj sur su1 at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「これは……！」"

    "私はこの日記帳に書かれた情報を見て、コーヒーの味が分からなくなってしまっていた。"

    "信じられない、というのが先に立つ。"

    "明日、海晴と直未に会う約束をしていてよかった。"

    "もし今日のうちにその話をしていなかったら、私は二人に声をかけるのを忘れてしまっていただろう。"

    "それほどの、衝撃があった。"

    "明日の選定の前に、話せてよかったと思う。"

    "少なくとも、私が一人で暴走するリスクは減らせるからだ。"

    show rnk paj sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「信じられない、けど」"

    "海晴の言った通り、切り札になり得る――≪女神の選定≫という超常現象の前提を切り崩してしまう可能性すらあった。"

    "痛いくらいに心臓が速く動く。"

    scene ecg dianapicture normal with dissolve_long

    "日記帳を閉じた私は、最後のページに挟まっていた写真を手に取った。"

    "写真は全部で３枚あり、リンダさんが一人で写っているもの、家族で写っているもの、もう一人別の女の子が写っているものだ。"

    "これは私のおばあちゃんのおばあちゃんである、リンダ・ハリソンの日記だ。"

    "私が注目したのは、リンダさんではない別の女の子が写っている写真だ。"

    "古ぼけたその写真には、この日記を書いた本人ではなくその妹が写っていた。"

    "セピア色に変色しているので鮮明ではないにもかかわらず、妹のダイアナさんの姿がはっきりと分かった。"


    voice get_voice_filename("rnk")
    rinka "「この女の子は、ダイアナ・ハリソンさんは――女神パルカと、同じ顔をしている」"

    "当時らしいシンプルで可愛らしい服だし、夢の中で現れるパルカほど長い髪ではないけれど。"

    "似ているとか、そうじゃない。同一人物というほかなかった。私の本能のような何かが、そう告げているのだ。"

    "あり得ない、ことである。"

    "だがあり得ないはずの二人の関係を結びつける情報が、日記の最後の最後に書かれていた。"

    scene ecg cardbook bli with dissolve

    "もう一つ、もっとも信じられないことが起きた。"

    "私の手元には、新しいカードが生成されたのだ。"

    $ add_character_cards("rnk", ["13_name"])

    "――ⅩⅢ・氏名・ダイアナ・ハリソン。"

    "あるはずのない、ⅩⅢ番が振られたカード。"

    "これは、つまり――。"


    scene bg lion01 night
    show rnk paj arm vig at std_c
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「女神の、カード」"

    "思わず、そう呟いていた。"

    "とても受け入れきれない目の前の現実を、わずかでも受け止められるように。"

    $ add_seen_chapter("11_2-2")








    python:
        set_info_scene("176")
        set_info_date(7, 15, "sun")
        set_info_time("evening")
        set_info_location("04")

    stop music fadeout 2
    scene bg lion01 evening with fade_longest
    pause 1

    $ show_hud()

    play se "bell02"

    show rnk apr nor smi at std_r with std_in

    voice get_voice_filename("rnk", 1600)
    rinka "「ありがとうございましたー」"

    "最後のお客さんを見送って、今日もお店は閉店。"

    "今朝は８時から開けていたので、今日も16時閉店と少し早い。"

    "休日に通しで開けるときは大体これくらいの時間なのだ。"


    play music audio.nichijo01

    show mhr sci sco smi rev at std_c with std_in

    voice get_voice_filename("mhr", 770)
    miharu "「お疲れ様」"

    show nom sci nor lau rev at std_l with std_in

    voice get_voice_filename("nom", 512)
    naomi "「お疲れ様ですっ！」"

    "海晴と直未はすでにライオン館に来ていて、私の仕事が終わるのを待ってくれていた。"

    "私は営業後の片付けを終えてから、いつものテーブルについた。来てもらったお礼に、コーヒーを淹れて持ってくる。"

    scene ecg girlstalkQ2 nor nor with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「11回目の選定の前に二人と会えて、よかった」"

    "私はまず、そう話した。"

    "日記帳をテーブルの上に置き、開いた。"

    "まず見せたのは、その写真であった。"

    show ecg girlstalkQ2 nor tro with ecg_change


    voice get_voice_filename("mhr")
    miharu "「これは――嘘だろう？」"

    scene ecg dianapicture normal with dissolve

    "海晴は写真を見て、第一声でこう聞き返した。"

    "私は首を傾げる直未に、驚きの理由を説明した。"

    "写真の少女はダイアナ・ハリソンであること。そしてそれは、女神パルカと同じ姿をしているということ。"

    scene ecg girlstalkU2 sur with dissolve


    voice get_voice_filename("nom")
    naomi "「め、女神……様と同じ？」"

    "聞き返してきた直未に対して、私は頷いた。"

    "そして私は今度は自分のカードブックから、ⅩⅢのカードを取り出した。"

    scene ecg girlstalkQ2 ser ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「女神の、カード……」"

    "ここまでを前提情報として話を始めるつもりだったが、その前提が重すぎたのだろう。"

    "すでに空気はひりつき、緊張感に満ちていた。"


    voice get_voice_filename("rnk")
    rinka "「じゃあ、聞いてね。この日記はまず、私のおばあちゃんのおばあちゃん、リンダ・ハリソンさんのものなんだけど……」"

    "この話をきっかけに、私は日記に書かれていた内容を話始めた。"






    stop music fadeout 1
    scene ecg dianapicture normal with fade_long
    play music audio.firedeath
    pause 1

    "結論から言うと、ダイアナ・ハリソンは12歳の時に火事で死亡している。"

    "リンダさんの日記の結末には、妹の死に対する無念が書かれていたのだ。"

    "目の前で助けを求めているのに、助けられなかったという後悔。"

    "そして問題は、ダイアナが死に至るまでの11週間にあった。"

    "彼女が火事に遭う11週間前、ダイアナの父親を師匠と慕う青年が、階段から転落し、頭を打って死亡した。"

    "その翌週、ハリソン家に出入りしていたお手伝いさんが、食中毒で死亡した。"

    "さらにその翌週。２週間前に死亡した青年の母親が、高熱を出して死亡した。"

    "その後、一週間に一人ずつ、ダイアナと何かしらの関係がある人物が死亡していった。"

    "身内ほど近い者、ただの知人ほどの者、法則性はない。"

    "ハリソン家は次第に恐怖を覚えていた。"

    "そして、当然思う。"

    "次は我が家の誰かかもしれないと。"

    "その悪い予感は、12人目の時に当たってしまう。"

    "そう。"

    "最初に話した通り。"

    "ハリソン家を焼失させた火事により、ダイアナが死亡した。"

    "火事による崩壊で、倒れてきた本棚に下半身を潰された。"

    "同室にいたリンダは、彼女を助けようとしたが、本棚はリンダの力では到底動かせない。"

    "今ほど消火の技術や防護服が発達しているはずもなく、子供部屋でリンダとダイアナを見つけた母親は、選ばなくてはいけなかった。"

    "だが答えは決まっていた。"

    "母親とリンダの力を合わせても、本棚は動かなかったから。"

    "頼みの父親は煙を吸って意識不明の重体。"

    "他に助けを呼びに行ったら、その間に火がダイアナを覆いつくすだろう。"

    "切羽詰まった状況でついに、母親は決断した。"

    "確実に助かる命だけを、助けるという判断を。"

    "ダイアナを見捨て、リンダを助けることを。"

    scene ecg lindadiary clo with dissolve

    "リンダはそのことを戒めのように、日記帳に記した。"

    "最愛の妹からもらった手作りの日記帳に、リンダはこの事実を書かなくてはいけないと使命感に駆られていた。"

    "日記には、さらに詳しくダイアナへの想いが書かれていた。そこには読むだけで胸が痛くなるほど、悲惨な感情がつづられていた。"






    stop music fadeout 1
    scene ecg girlstalkQ2 ser ser with fade_long
    play music audio.disclose
    pause 1


    voice get_voice_filename("rnk")
    rinka "「これが、私が日記帳で読んだ中で一番重要だと思ったこと」"

    "話し終えて、テーブルはさらに重い空気になっていた。"

    "無理もないだろう。"

    "写真に写っている可愛らしい女の子は、おそらくこの写真を撮って間もなく亡くなったから。"


    voice get_voice_filename("mhr")
    miharu "「とにかく、これが切り札足り得るというのは正解と思う。間違いなく――」"


    voice get_voice_filename("rnk")
    rinka "「うん。女神は、元人間だ。ダイアナ・ハリソン――私のひいひいおばあちゃんの妹」"

    scene ecg girlstalkU2 ser with dissolve


    voice get_voice_filename("nom")
    naomi "「話の途中で予想はしていましたけど、驚かずにはいられないです」"

    "私たちの認識はそう一致していた。"

    show ecg girlstalkU2 sad with ecg_change


    voice get_voice_filename("nom")
    naomi "「12週間という期間と12人の参加者。ダイアナさんが死に至るまでに起こったことが……≪女神の選定≫の原型になっているんだと思います」"

    scene ecg girlstalkQ2 ser sad with dissolve


    voice get_voice_filename("mhr")
    miharu "「ああ。これは――悲劇だね」"

    "海晴は寂しそうな声でそう言った。"

    "海晴でも、これを悲劇と言うほかなかったのだろう。"

    scene ecg girlstalkU2 tro with dissolve


    voice get_voice_filename("nom")
    naomi "「人間が神様になったってことですよね。もう……信じられないです」"

    scene ecg girlstalkQ2 ser ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「でも、≪運命の大広間≫も≪女神の選定≫も、存在する。記憶の改変っていう、超常現象も」"


    voice get_voice_filename("rnk")
    rinka "「人間が女神に変わるっていうことも、信じないわけにはいかない」"


    voice get_voice_filename("mhr")
    miharu "「これはあくまでぼくの予想だけれど、≪運命の大広間≫で出会った女神パルカには人間としての記憶はないように思える」"

    scene ecg girlstalkU2 sur with dissolve


    voice get_voice_filename("nom")
    naomi "「そ、そうなんですか？」"

    show ecg girlstalkQ2 ser ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「確かに、そうだね。人間をあくまで自分より下の存在として接していた」"

    "そこに自分が元人間だから、という同族嫌悪のようなものは感じなかった。"

    "あくまで、自分が女神であることを当然に思っているように見えたのだ。事実、私も海晴の意見に賛成だ。"

    "私たちは再び、下を向いてそれぞれ考え始めた。"

    scene ecg girlstalkU2 anx with dissolve

    "直未が「せんぱいたちも気付いていると思うんですが」と恐る恐る、口を開く。"

    show ecg girlstalkU2 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「女神様のカードができたってことは――女神様を、指名できるってことですよね？」"

    scene ecg girlstalkQ2 ser ser with dissolve

    "海晴も私も真剣な顔をして、直未を見た。"

    "カードとは私たち選定の参加者の情報であり、現在過去未来の象徴であり、何より、相手を指名して脱落させるためのものだ。"

    "女神のカードがあるということは、女神を指名するためとしか思えない。"


    voice get_voice_filename("mhr")
    miharu "「けれど、まだ謎も多い。ぼくもカードブックを持ってきているけれど、ぼくの方にカードは生成されない」"


    voice get_voice_filename("mhr")
    miharu "「ダイアナ・ハリソンという氏名ははっきり認識しているし、顔も分かっている」"

    scene ecg girlstalkU2 ser with dissolve


    voice get_voice_filename("nom")
    naomi "「凛火先輩が何か特別……ってことでしょうか？」"

    scene ecg girlstalkQ2 tro ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「特別かどうかは分からないけど、理由があるのは確かだね」"

    "私も気になっていたことだった。海晴のカードブックはダイアナの名前を聞いても一切反応がないのだ。"

    "そして気になることはまだあった。それは、直未が代弁してくれた。"

    scene ecg girlstalkU2 ser with dissolve


    voice get_voice_filename("nom")
    naomi "「ダイアナさんの……し、死因も明らかになっていると思うんです。それは凛火先輩の方にもカード化されていない……」"

    scene ecg girlstalkQ2 ser ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「この日記帳から読み取れるのは火事による≪焼死≫か煙による≪窒息死≫」"

    show ecg girlstalkQ2 tro ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「でも、リンダさんはダイアナさんが亡くなるのを見届けたわけじゃないはず。だから、彼女の見ていない何かがあったんだと思う」"

    show ecg girlstalkQ2 tro tro with ecg_change


    voice get_voice_filename("mhr")
    miharu "「直接の死因だね。屋根が崩れてきたとか、出血多量だとか、可能性はいくつもある」"

    "私たちは驚くほど冷静に、百年前の出来事を想像していた。"

    "これは、女神に迫ることのできる唯一の方法。"

    "きっかけは最初から私の近くにあったにもかかわらず、最後の最後で私の手に降りてきた可能性なのだ。"

    show ecg girlstalkQ2 ser tro with ecg_change


    voice get_voice_filename("rnk")
    rinka "「本当に指名できるかはともかく、指名するとしたら、≪未練≫も必要」"

    "そして、それが一番難しいはずだ。"

    "女神自身に聞いても答えるはずはないだろうし、そもそも私たちは彼女が人間だった頃の記憶を覚えていないと予想している。"

    "女神パルカが元はダイアナという少女だということはあくまで類推だが、それはすでに前提条件だった。"

    "単なる思い込みではないと、信じたい。"

    show ecg girlstalkQ2 nor ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「でも、希望は見えた。女神の指名……それがきっと、海晴と私が生き残るための唯一の方法だ」"

    show ecg girlstalkQ2 nor nor with ecg_change


    voice get_voice_filename("mhr")
    miharu "「希望には変わりないけれど、唯一かどうかは分からない。次の選定で、確かめる必要はあるよ」"

    scene ecg girlstalkU2 sad with dissolve


    voice get_voice_filename("nom")
    naomi "「凛火先輩が海晴先輩を指名して、海晴先輩が防御したらどうなるか……ですね」"

    show ecg girlstalkU2 anx with ecg_change


    voice get_voice_filename("nom")
    naomi "「試してみるって、ことですか？」"

    scene ecg girlstalkQ2 ser nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「それは駄目。指名できる人がいなくなって、もしその時点で指名以外の方法で強制的に決着をつけさせられる――なんてことになったら手遅れだ」"

    scene ecg girlstalkU2 anx with dissolve


    voice get_voice_filename("nom")
    naomi "「つまり、女神様に聞いて確かめることも危険なんじゃないですか？　せんぱい達の意図が知られて、対策をとられたら……」"

    scene ecg girlstalkQ2 ser ser with dissolve


    voice get_voice_filename("mhr")
    miharu "「そうだね。希望が近づいて少し焦っていたようだ。次回の選定での正解は、何もしないことかもしれない」"


    voice get_voice_filename("mhr")
    miharu "「12回目の選定の時に手の打ちようがない場合に、初めて試せばいいことだ」"


    voice get_voice_filename("rnk")
    rinka "「そうだね。そして私たちは、≪女神のカード≫を持っていることを知られてはいけない、だね」"

    scene ecg girlstalkU2 smi with dissolve


    voice get_voice_filename("nom")
    naomi "「もう少し……もう少しですね。本当に！」"

    "直未の言葉が、心に染みた。"

    "希望は見えた。"

    "あとはその希望を確実な勝算まで昇華させる必要がある。"

    "皮肉なものだ。"

    "相手が運命の女神なら、勝利の女神が微笑むことは期待できないのだから。"

    show ecg girlstalkU2 uwa with ecg_change


    voice get_voice_filename("nom")
    naomi "「そそ、それで……この日記帳、借りてもいいですか？」"

    "申し訳ない気持ちと興味津々な気持ちが半々なのが、見ていてよく分かる。"




    scene ecg girlstalkQ2 smi nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「いいよ。ただ、おばあちゃんの大事なものだから汚したり傷つけたりしないようにね」"

    scene ecg girlstalkU2 lau with dissolve


    voice get_voice_filename("nom")
    naomi "「ありがとうございます！　石橋を叩いて壊すくらいに、慎重に……」"

    scene ecg girlstalkQ2 ang nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「いや、だから壊しちゃ駄目だって」"

    "この日記はおばあちゃんのおばあちゃんの大切なものではあるが、直未になら貸しても安心だろう。"

    "私にとってこの日記帳は、情報源でもある。直未が読むことで、私が見落としていた情報を手に入れることができるかもしれない。"


    if False:

        voice get_voice_filename("rnk")
        rinka "「ごめんね。やっぱりおばあちゃんのものだから、貸すのは無理かな」"


        voice get_voice_filename("nom")
        naomi "「あ、謝らないでください！　わたしが無理を言っているだけなので……」"

        "いくら直未といえども、おばあちゃんの大事なものを勝手に貸すわけにはいかない。"

        "貸すにしても許可を取ってからだし、それは選定が終わった後からでも遅くはないだろう。"


    scene black with dissolve

    "その後は暗くなるまでのんびりと過ごし、二人はライオン館を出て、帰路へついた。"

    "海晴と直未の後姿を見送りながら、二人が楽しそうに話しているのを見てとても――ほっとしていた。"







    python:
        set_info_time("night")
        set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    "部屋に戻ってきてからの私は、まだ高揚していた。"

    "選定が始まったときからは考えられない状況だ。"

    "海晴も積極的に生きることを考え、二人が生き残る可能性を見出した。"

    show rnk paj nor que at std_c with std_in

    voice get_voice_filename("rnk", 1617)
    rinka "「女神様……か」"

    "彼女が元人間だというのは、ほとんど確定的だろう。"

    "死の淵に、一体何があったのか。人間が女神――概念上の存在に変わることができるのか。"

    "謎は増えたけれど、それは前に進んでいる証拠だった。"

    "必ず、私は――。"

    "決意を新たにして、今夜の選定へと望むため、眠りにつくことにした。"

    $ add_seen_chapter("11_2-3")

    jump f011_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

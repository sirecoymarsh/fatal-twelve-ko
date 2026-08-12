

label f012_01GH:









    python:
        set_info_scene("200")
        set_info_date(7, 16, "mon")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "朝の光を浴びて、ワタクシは目を覚ましました。"

    "体に直接浴びる光というのは、こんなにもひりつくものだったのでしょうか。"

    "太陽の光はまるで神話のように、人間の体を焼いていくということでしょうか。"

    "けれどその感覚を不快とは思いません。"

    "生きることは痛みを伴うもの。破瓜の痛みも知らないワタクシですけれども、これこそ真理だと思いますわ。"

    show lete normal at cat_r with std_in

    voice get_voice_filename("cat", 26)
    lete "「にゃー」"

    show rnk paj nor 9qu rev at std_cl with std_in

    voice get_voice_filename("rnk", 1833)
    rinka "「あら？　レオじゃありませんの。お元気でいらっしゃいましたか？」"

    show lete angry with std_change

    voice get_voice_filename("cat")
    lete "「しゃー」"


    hide lete with std_out

    "黒猫のレオはワタクシを見るなり、威嚇して去っていってしまいました。"

    "ワタクシには懐いていたはずですけれども、おかしいですわね。"

    "いえ、落ち着きましょう。"

    "ワタクシは獅子舞凛火。"

    "ということはここは獅子舞凛火の家。"

    "あの猫はレオちゃんではございません。"

    show rnk paj nor 9pc rev with std_change

    voice get_voice_filename("rnk")
    rinka "「気をつけないといけませんね。うーん、学校に行くはずですけれども……」"

    show rnk paj nor 9sm rev with std_change

    voice get_voice_filename("rnk")
    rinka "「まあ、大丈夫ですわね。行ってみればきっと、なんとかなるでしょう」"

    hide rnk with std_out

    "学校に行くには、制服を着るのですね。"

    "ぼんやりとした記憶を頼りに、ワタクシは制服を探します。"

    "他にも、外出するには準備がいるようです。これは習慣だからでしょう。記憶をたどらなくても、自然と体が動きました。"

    scene bg myroom night large at zoom(1.3), align(1.0, 0.6) with dissolve

    "ワタクシは鏡を見て、自分の姿を確認しました。"

    "獅子舞凛火は赤いルビーのような目をしていましたけれど、今はワタクシのアメジストのような美しい瞳に変わっています。"

    "だいぶお上品になってしまいましたけれど、そこまで注目する方も多くはないでしょう。"

    scene bg myroom night with dissolve

    "ま、何とかなりますわね。"

    "今のワタクシの目の色は、これが本物なのですから。"







    python:
        set_info_time("morning")
        set_info_location("14")


    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show nom sun har sur rev at std_cl with std_in

    voice get_voice_filename("nom", 617)
    naomi "「り、凛火先輩どうしたんですか、カ、カラコンですか？」"

    "あら、困りましたわ。"

    "記憶を頼りに学校に来てみましたけれど、早速、瞳のことを指摘されてしまいました。"

    "さて、こういう時はあれです。"

    "開き直りです。"

    show rnk sun nor 9pc at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あら？　どこかおかしくて？」"

    show nom sun nor sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「いやいやいや……。せんぱい、喋り方がなんかいつもより上品ですし……違和感が……」"

    show nom sun que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、あれ、もしかしてひ、人違いですか？」"

    "これは困りました。"

    "獅子舞凛火の生活は、これからもずっと続くのです。"

    "目の前で慌てる可愛らしい女の子は、日辻直未。ワタクシの一つ下の後輩で、とても仲が良いそうです。"

    "せめて口調くらいは合わせないといけないかもしれません。"

    "ええと、獅子舞凛火は確か。"

    show rnk sun nor 9qu with std_change

    voice get_voice_filename("rnk")
    rinka "「どうしたの、直未。変だよ？」"

    show nom sun har pal rev with std_change

    voice get_voice_filename("nom")
    naomi "「凛火先輩なのは間違いなさそうだし……でも……ああ、おかしくなりそうです……」"

    show nom sun que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「って、その、今日はお休みのはずですけど、せんぱいはどうして学校に？」"

    "やはり、堂々としていて正解ですわね。"

    "考えても無駄だと思ったのか、考えるのをやめたようです。"

    "さて、問題はこの質問の答えです。"

    "多少強引に体をいただいたので、記憶を引き出すのにまだ慣れていません。"

    "少し時間を置いて、獅子舞凛火の記憶を引き出します。"

    show rnk sun arm 9no with std_change

    voice get_voice_filename("rnk")
    rinka "「……忘れてた」"

    show nom sun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「せんぱいらしいというか、なんというか……。先週まで期末試験だったじゃないですか。だから今週は木曜日まで試験休みですっ」"

    show rnk sun nor 9no with std_change

    voice get_voice_filename("rnk")
    rinka "「あれ、何で貴女サ……直未は来てるの？」"

    show nom sun hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「わたしは、図書室に本を返しに来て……そのついでに、また何か借りようかなーって」"

    show rnk sun nor 9sm with std_change

    voice get_voice_filename("rnk")
    rinka "「そっか。私も行こうかな。せっかく学校に来ちゃったんだし」"

    show nom sun nor sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「え……せんぱいがですか……珍しい……」"

    show rnk sun arm 9li with std_change

    voice get_voice_filename("rnk")
    rinka "「ふふ、たまにはね」"

    "段々、獅子舞凛火の話し方にも慣れてきました。"

    "感情表現を３分の１くらいにおさえてみれば簡単です。"

    "ワタクシは、本があまり好きではないようです。"

    "ワタクシとは正反対なので、内心ウキウキです。"

    "一体どんなご本がワタクシを待っているのでしょうか。"







    python:
        set_info_time("noon")
        set_info_location("30")

    scene bg schoollibrary with fade_long
    pause 1

    $ show_hud()

    "図書室というのは、ご本を貸し借りするための学校の施設のようです。"

    "図書というくらいですからご本があると思ったので、ワタクシ正解です。"

    "お休みなのに、司書サマがいらっしゃいました。"

    "まず直未サマが本を返して、次に借りるご本を探し始めます。"


    scene bg schoollibrary with fade_long
    pause 1

    "30分ほど経過して、ワタクシたちは図書室のテーブルに座って話します。"


    play music audio.naomi

    show nom sun nor lau rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「せんぱい、随分じっくり選んでましたね」"

    "時間の概念にもまだ慣れないので、直未サマが少し驚いていらっしゃいました。"

    show nom sun nor smi rev with std_change

    voice get_voice_filename("nom")
    naomi "「シェイクスピア……せんぱい、好きなんですか？」"

    show rnk sun nor 9no at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「まあね」"

    "ワタクシは好きではないけれど、ワタクシは好きです。"

    "趣味趣向というのは怪しまれても、ワタクシのものに変えていく方がよいでしょう。"

    "我慢は体にも心にも毒ですから。"

    "その後は、他愛のない話をします。"

    "実のところワタクシは、他愛のない話ってなんだろうと思っていました。"

    "直未サマと話しているととても勉強になります。"

    "普段あった些末なことを語り合ったり、毒にも薬にもならず何の解決もしない議論をしたりする。"

    "世間話というのは、こういうものなのですね。"

    "誰かの陰口で盛り上がらないことには、とても好感が持てます。"

    show nom sun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「あの……せんぱい……」"

    "少しして、直未サマが神妙な顔をして言います。"

    "神妙というのも面白い言葉ですね。"

    "ワタクシも彼女にならって、神妙な顔をしてみましょう。女神が神妙な顔です。元、ですけれども。"

    show nom sun que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「そろそろ……遊園地に行きませんか？　あの……未島先輩のことを忘れたわけではないんです」"

    show nom sun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「でも、真央先輩もずっと寂しそうで、遊びに誘われることもなくて……だから……」"

    show nom sun har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「行く予定だった遊園地に行って……悲しんで、惜しんで……泣いて。でも３人は一緒だって、実感して」"

    show nom sun har ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「もちろん、わたしじゃ未島先輩の代わりになれるなんて思っていません。でも、凛火先輩にも真央先輩にも、ちょっとずつ前を向いて欲しいです」"

    "あら、なんていい子なのでしょう。"

    "直未サマもⅡ番サマのことがお好きでしたのね。"

    "ワタクシは獅子舞凛火になりましたし、Ⅱ番サマというのはやめましょう。"

    "ここは、５月３日に海晴サマが自殺した世界。"

    "すでに２ヵ月以上も経過しているのに、まだ悲しみを引きずっているのですね。"

    "もっとも、そんなことは口にはしません。獅子舞凛火ならどう答えるのがどう正解か、概ね分かってきましたから。えっへん。"

    show rnk sun arm 9li with std_change

    voice get_voice_filename("rnk")
    rinka "「……そうだね。気を遣わせちゃったね、ごめん。でも、ありがとう。真央には、私から声をかけるよ」"

    show nom sun nor nor rev with std_change

    voice get_voice_filename("nom")
    naomi "「せんぱい……！」"

    "直未サマが顔を上げて目を輝かせています。"

    "付き合いが短い分、悲しみを乗り越えるのもお二人サマに比べて早いのですね。"

    "けれども落ち込んでいる皆サマには、こうやって無理矢理にでも外へ連れ出す方が必要な時もあります。"

    "おばあちゃんという人が、よく言っていたようです。"

    "こうして私は本を借りて、おうちへ帰ります。"

    "瞳の色なんて、堂々としていればやっぱり大丈夫なんですね。"

    "問題は中身。うん、いい言葉です。"

    "ワタクシ、よくやっています。花マルです。"




    if flags_route_H:
        jump fBAD_04







    python:
        set_info_scene("201")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()



    "さて家に帰ってきたワタクシは、まず部屋着に着替えます。"

    "肌の露出が多くて少し恥ずかしいですが、とても動きやすいです。"

    "借りてきた本を、机の上に置いてみます。"

    "机の上には物が多いです。"

    "ワタクシは片付けが苦手ではないのですけれど。"

    "クマのぬいぐるみ、何も書いていない手紙、鍵のキーホルダー。"

    show rnk sun nor 9no at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……痛いですわ」"

    "なぜか、頭に痛みが走りました。"

    "びっくりしたので、ついワタクシの口調になってしまいました。"

    "気をつけないといけません。"

    "何故だか、机の上のものはあまり視界に入れたくありません。"

    "ワタクシにとって大切なものだからでしょう。思い出そうとしても、まだ心が閉じているような感覚がします。"

    "ということで、１階へ行って本を読みましょう。"

    "ライオン館は喫茶店です。"

    "本を読むにはとてもいい環境に違いありません。"







    $ set_info_location("04")

    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    show rnk sun nor 9pc at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「にがにがですわね……」"

    hide rnk with std_out

    "おっといけない。"

    "またワタクシになってしまいました。"

    "それもこれも、コーヒーという飲み物がいけません。"

    "喫茶店と言えば紅茶でしょうに、ここには紅茶がありませんでした。"

    "コーヒーという苦い飲み物ばかりです。体が覚えている通りに淹れてみましたが、美味しさが分かりません。"

    "どうやら、ワタクシはこのお店の店長サマをやらないといけないようです。"

    "明日からが憂鬱ですけれど、楽しみでもありますわ。"

    "どうやらしばらくお店を閉めていたようなので、片付けをしないといけません。"

    "ワタクシは洗い物をしたり、伝票の準備をしたりしました。この辺りの作業も、やはり体が覚えています。"

    "ワタクシはとても仕事熱心で真面目だったようです。"

    "さて、と。"

    "足りない食器などがないか、確認しないといけません。"

    show rnk sun nor 9qu at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あれ……これ……」"

    "食器棚を見ると、未開封の箱があります。"

    "持ってみると中々に重いので、やはりこれは食器でしょう。"

    "新しい食器を出しておかないといけないですね。"

    "ワタクシはその箱を、開いてみました。"


    play music audio.kinpaku

    show rnk sun arm 9te with std_change

    voice get_voice_filename("rnk")
    rinka "「――――つっ」"

    hide rnk with std_out

    "先ほどのよりも鋭い痛みが、ワタクシの頭を走ります。"

    "頭痛というものですね。"

    "ワタクシは頭痛持ちではないはずですが。"

    "体の方が馴染んでいなくて、疲れているのかもしれませんね。"

    "早く仕事を終わらせて、今日は早く寝てしまいましょう。"

    "ワタクシの人生は、まだ始まったばかりなのですから。"



    voice get_voice_filename("rnk")
    rinka "「――して」"

    "早速、箱からカップを取り出してみましょう。"

    "可愛らしい２つのカップですが、キャラクターものですね。子供用にも見えません。"

    "お店用ではないのでしょうか。"



    voice get_voice_filename("rnk")
    rinka "「――して」"

    "よく見ると、ローマ字で名前が彫ってあります。"

    "一つはRinka Shishimai。ワタクシですね。"

    "もう一つはMiharu Mishima。これは、海晴サマのことですね。"

    "お揃いのカップは、お友達のものだからでしょうか。"

    "記憶を思い出したいところですけれど、頭痛がひどくなりそうなので今日はやめておきましょう。"



    voice get_voice_filename("rnk")
    rinka "「返して」"

    "どこからか声が聞こえます。"

    "いいえ、いい加減無視するのはやめましょう。"

    "この声は、ワタクシが出しています。"

    show rnk sun arm 9no at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「返しませんわ」"



    voice get_voice_filename("dia", 485)
    parca "「貴女サマとはもう、ワタクシのことですもの」"

    "一層ひどくなった頭痛に負けて、私はその場に倒れこんでしまいました。"





    python:
        set_info_time(None)
        set_info_location("01")

    stop music fadeout 2
    scene ecg mindbattle normal with fade_longest
    pause 1




    voice get_voice_filename("rnk")
    rinka "「ちゃんと守れた」"


    voice get_voice_filename("dia")
    parca "「何をおっしゃっていますの？」"


    voice get_voice_filename("rnk")
    rinka "「私だけが知っている海晴と、海晴だけが知っている私」"


    voice get_voice_filename("dia")
    parca "「残念ながら、時間の問題ですわ」"


    voice get_voice_filename("dia")
    parca "「貴女サマが見られたくない記憶があったとしても、ワタクシが貴女サマの体に完全に馴染んでしまえば、記憶に蓋はできません」"


    play music audio.rinka
    show ecg mindbattle hand with ecg_change


    voice get_voice_filename("rnk")
    rinka "「ううん、させない。これは私の体。だから、返してもらう」"


    voice get_voice_filename("dia")
    parca "「もう、物分かりが悪いですわね。貴女サマの意識にはすでに、ワタクシの意識が上書きされています」"


    voice get_voice_filename("rnk")
    rinka "「物分かりが悪いのはどっち？　私があなたに話しかけている、話しかけることができている理由は分かるはず。だってあなた自身がヒントをくれたから」"


    voice get_voice_filename("rnk")
    rinka "「運命の捻じれ……だっけ。それで私にも元からあなたの力に似たものがあるっていうなら、あなたと同じこともできるはず」"


    voice get_voice_filename("dia")
    parca "「まさか……。いえ、でもそれは不可能ですわ」"


    voice get_voice_filename("dia")
    parca "「あなたの意志をワタクシの意志で上書きするために、≪運命の大広間≫に蓄積した力を使いましたもの」"


    voice get_voice_filename("rnk")
    rinka "「力っていうのは、変わっただけ。あなたに。自分の体の中のことだから、分かるよ」"


    voice get_voice_filename("dia")
    parca "「お止めなさい。もし貴女サマの意志があるなら、それは≪器≫の中にいるワタクシと同じ状態」"


    voice get_voice_filename("dia")
    parca "「とても幸運でございますわ。ワタクシに完全に支配されることなく、意識を保っているのですから」"


    voice get_voice_filename("dia")
    parca "「もし仮に、貴女サマがワタクシの意識を再び上書きしようとしているのであれば、それは――」"


    voice get_voice_filename("rnk")
    rinka "「失敗なんてしない。だってあなたの力は、あなたのものじゃないんでしょ」"


    voice get_voice_filename("dia")
    parca "「選定の参加者の想いの欠片が力に変わったから、と言いたいのでしょうか？」"


    voice get_voice_filename("dia")
    parca "「力はあくまで力。エネルギーに意志などありませんわ。貴女サマも、電気とお話しできると思ったことはないでしょう？」"


    voice get_voice_filename("rnk")
    rinka "「やってみなきゃ、分からない」"


    voice get_voice_filename("dia")
    parca "「失敗すれば、貴女サマの意志は完全に消えますわ。≪夢の世界≫ですら現れることはできなくなってしまいます」"


    voice get_voice_filename("dia")
    parca "「こうして少しでも意識が残った幸運を噛み締めるべきですわ。ワタクシの中から、世界を見ることはできますもの」"


    voice get_voice_filename("dia")
    parca "「それに……、それに……」"


    voice get_voice_filename("dia")
    parca "「ワタクシはとても、楽しかったですわ。だからワタクシはワタクシを譲るわけにはいきません」"


    voice get_voice_filename("rnk")
    rinka "「――もう、黙って。返してもらう。私だけの、私を」"


    voice get_voice_filename("dia")
    parca "「いいでしょう。文字通り全身全霊で、今宵、貴女サマを完全に消滅させましょう」"

    if flags_route_G:
        $ add_seen_chapter("12_2-1")
    if flags_route_H:
        $ add_seen_chapter("12_3-1")







    python:
        set_info_scene("202")
        set_info_date(7, 20, "fri")
        set_info_time("noon")
        set_info_location("08")


    stop music fadeout 2
    scene bg schoolroom noon with fade_longest
    play music audio.nichijo02
    pause 1

    $ show_hud()

    "期末試験の結果の返却と通知表の配布をもって、私の私立飴茶女子大学付属高校２年生の１学期は終了を告げる。"

    "どきどきしながら試験の結果を見ると、真央が楽しそうに食いついてきた。"

    show mao uni sel glo rev at std_cl with std_in

    voice get_voice_filename("mao", 329)
    mao "「お疲れりーたん～。どうだった？」"

    show rnk sun nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「どうにか、全教科60点は越えた。頑張った甲斐があったよ」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「さ、さいですか」"

    "私が自信満々に答えると、真央は露骨に目を逸らした。"

    "これはきっと、真央は私より点数が低かったに違いない。"

    "私は真央の隙をついて、成績表を奪い取った。"

    "結果を見て、私は目を丸くした。"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「いやあ、りーたんあれだけ頑張ってたのに、真央様以下だったのはかわいそうだしぃ……」"

    "真央の点数は、私よりも全体的に10％以上は高かった。"

    "口ではかわいそうとか言っているが、きっと違う。真央は私が意気揚々と自分の成績表を見るのを待って、ショックを大きくしようとしたのだ。"

    "証拠に、にやにやと笑っている。"

    show mao uni nor lau rev with std_change

    voice get_voice_filename("mao")
    mao "「まあまあ、これでどうにか試験が終わったねぇ。夏休み、どうしよっか？」"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「なおりんは８月の最後の方で家族旅行するみたいだって。あ、あと塾も行くって言ってたねぇ。若いのに大変だのう」"

    "実は、来週の金曜日には遊園地、スターダストキングダムに行くことが決まっている。"

    "ただ、決まっている予定はそれだけ。"

    "部活をやっていない私たちは、理由がなければ学校へ来ることはない。"

    "直未は図書室へ行くだろうけれど、私はそこまで頻繁に図書室へ行く予定はない。"

    "家に置いてあったシェイクスピアの本を読んでみたけれど、あまり楽しくはなかった。"

    "真央とはそれなりに会うだろうけれど、遠出するならやはり３人で行きたい。"

    "でも、実は聞かれるまでもなく決まっている答えがあった。"

    "私たちには行きたいところ、行かなければいけないところがあるのだ。"

    "あの日、あの場所で、約束したこと。"

    show rnk sun nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「花火大会。これは、絶対行かないと。約束したからね」"

    "海晴とも。"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「あれ、そんな約束したっけ？」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「してたよーな、してたよーな」"

    show rnk sun nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「両方してるよ。大丈夫。たぶん、直未も覚えてるから」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「なおりんも？　そっかー。なら、大丈夫かー」"

    "この日、私たちは久し振りにライオン館で集まった。"

    "私はまだ、どこまでが正しい記憶なのか分からないままだったけれど。"

    "この世界に海晴がいないという真実が変わらない限り、今までのことはどうでもよかった。"

    "私に残されたのはもう、未来しかないから。"

    if flags_route_G:
        $ add_seen_chapter("12_2-2")
    elif flags_route_H:
        $ add_seen_chapter("12_3-2")









    python:
        set_info_scene("203")
        set_info_date(7, 22, "sun")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "今日はお店を夕方まで開けて、夕方からはまったりと過ごしていた。"

    "あの夜。"

    "11回目の選定直後、私は≪夢の世界≫でパルカと対話した。"

    "きっと私という火は消えかけていたんだ。"

    "でも、海晴が私を燃やしてくれた。"

    "私だけが知っている海晴と、海晴だけが知っている私がいたからこそ、私は自我を保つことができた。"

    "他の理由なんてしらない。"

    "そんなものは、いつか女神パルカが語ってくれるだろう。"

    "もっとも彼女はもう私の中にいないのかもしれないけれど。"

    "獅子舞凛火は今日も、獅子舞凛火だ。"

    show rnk paj nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「さて、寝るかな」"

    hide rnk with std_out

    "冷房をつけたくなるような暑い夜にも嫌気が差す頃だ。"

    show lete normal at cat_c with std_in

    voice get_voice_filename("cat")
    lete "「にゃにゃっ」"

    "ベッドに寝転がると、黒猫のレテがとことことやって来た。"

    "威嚇なんてすることなく、私の隣で丸くなる。"


    hide lete with std_out

    "本来ならば、この夜が12回目の選定だった。"

    "結局、海晴と私とが指名しあったらどうなったのか分からずじまい。"

    "日記帳も、最後まで読む気にはなれなかった。"

    "もっともカードブックは≪運命の大広間≫の崩壊の時に一緒に消えてしまったから、今となってはあの英語を読むのは至難の業だ。"

    "直未もどういうわけか≪女神の選定≫に関する記憶をほとんど失っているため、日記帳を貸したところで喜びはしな……いや、直未なら喜びそうだ。"

    "女神の選定という儀式の存在自体を、もはや私くらいしか知らないのだろう。"

    "それでいい。"

    "それで十分だ。"

    "私が覚えているだけでも、きっと誰かが救われる。"

    "私は、救われる。"

    "涙？"

    "もう出ないよ。"

    "だって散々泣いて、枯れちゃったから。"






    python:
        set_info_time("lnight")
        set_info_location("01")

    stop music fadeout 2
    scene ecg pattern nor a with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    "夢を見たかと思えば、それは夢の世界だった。"

    "すっかり聞き慣れてしまった男性の声。"

    show let sta nor sm1 at std_c with std_in


    voice get_voice_filename("let", 171)
    lete_unk1 "「やあ。まさか人間が、瞬き程の短い時でも自分の力で私たちの領域に踏み込んでくるとは思わなかった」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「かつて到達した人間もいなくはないが、あれはまったく特殊なケース。もっとも、君もよっぽど特別ではあるけれど」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「≪女神の選定≫というシステムを遂行しながら、女神を消滅させる」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「これを偉業と言わず、何と言おう」"

    show let sta nor tro with std_change


    voice get_voice_filename("let")
    lete_unk1 "「おっと、消滅というべきではなかったね」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「それが何を意味するのか、君はすでに分かっているのかもしれないけれど」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「おっとその前に、君に全ての真実を話すべきだったかな」"

    "いらない、と思った。"

    "もう終わったことに興味はない。大切なのは未来なのだ。"

    "私の心の声はどうやら彼に伝わるらしく、ふふ、と微笑む声が聞こえる。"

    show let sta nor tro with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君と会うのもこれが最後だから、もう少し長く話をしたかったけれどね」"





    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    menu:
        lete_unk1 "「さてそれでは質問だ。君は君の中に残っているものに気付いているかい？」"
        "気付いている":

            $ persistent.s19_1_seen = True
            $ grant_hear_all()
            jump f012_01GH.s1_1
        "気付いていない":

            $ persistent.s19_2_seen = True
            $ grant_hear_all()
            jump f012_01GH.s1_2


label f012_01GH.s1_1:

    show let sta nor ser with std_change


    voice get_voice_filename("let", 180)
    lete_unk1 "「そうか……やはりというべきかな」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「ここまで辿り着いた君のことだ。気付いていてあえて、普通の生活を望んだのかな。あるいは、私が来るのを待っていたのかもしれないね」"

    jump f012_01GH.s1_end

label f012_01GH.s1_2:


    show let sta nor tro with std_change


    voice get_voice_filename("let", 182)
    lete_unk1 "「さすがの君も、そこまでは見抜けないか」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「いや、落胆はしていない。繰り返しになるけれど、君はここまで辿り着いたことがすでに偉業なのだから」"

    jump f012_01GH.s1_end


label f012_01GH.s1_end:

    show let sta nor ser with std_change


    voice get_voice_filename("let", 184)
    lete_unk1 "「君の中にあるもの。それは、≪女神の力≫というべき力だ」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「女神は≪{rb}想い{/rb}{rt}ユメ{/rt}の欠片≫と表現していたけれど、紛れもなく人智を超えたエネルギーと言われるもの」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「11度目の選定の時に事が終わって、本当によかった。≪運命の終着点≫にたどり着いてしまったら、これから起こるはずの奇蹟は起こせなかっただろう」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君は一度だけ、運命を変えることができる」"

    "私は驚くことはなかった。"

    "なぜなら、そんな予感がしていたからだ。"

    "自分の体の中に、自分のものじゃない何かが残っている感覚。"

    "女神が私へ侵入してきたときと似た感覚が、この一週間ずっとあった。"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「ただし、運命を変えるためには条件がある」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「運命が戻ろうとする力の存在は、君はすでに知っていると思う。君が運命を変えようと、世界は元に戻ろうとする」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「そこで、私の出番だ。私は忘却の川に等しき存在。ただ一度の奇蹟のために世界の認知を騙すくらいなら、喜んで手を貸そう」"

    "こういう時、回りくどい言い方をしないで欲しい、と思った。"

    "超常現象なんて想像できるはずもないんだから、はっきり言って欲しい。"

    show let sta nor tro with std_change


    voice get_voice_filename("let")
    lete_unk1 "「……君は一層手厳しくなったね。長きにわたる選定を乗り切ったならば当然かもしれないけれど」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「君に与えられた選択肢は２つ」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「一つ目は≪女神の選定≫に参加した全員が生きている世界を紡ぎ、≪因果の刻≫そのものを≪なかったこと≫にしてしまうこと」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「その代償として、世界からその間の記憶は忘却される。もちろん、君自身も。君が覚えていれば、世界は元に戻ろうとしてしまうからね」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「そして、二つ目。何もしないこと。君は≪女神の力≫を持ちながら、何もしないことだ」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「しばらくは他人の≪夢≫と同調することくらいはあるかもしれないが、いずれ君は体内の異物感にもなれ、自分が力を持っていることすら忘れてしまうだろう」"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「その頃には、私も君のことを忘れているだろう。何しろ私の知能は猫なみだ。パンダの君よりも知能が低い」"

    "何故、彼が真央との会話を知っているのかはこの際不問だ。"

    "とにかく、彼の提示した二択ならば分かりやすい。"

    "どうやら、選ばなければいけないらしい。"





    menu:
        "私は――。"
        "運命を変える":

            $ persistent.s20_1_seen = True
            $ grant_hear_all()
            jump f012_01GH.s2_1
        "何もしない":

            $ persistent.s20_2_seen = True
            $ grant_hear_all()
            jump f012_01GH.s2_2

label f012_01GH.s2_1:




    voice get_voice_filename("rnk", 1865)
    rinka "「変えるよ。運命ってやつを。私が自分の意志で、全てをなかったことにする」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let", 198)
    lete_unk1 "「よく言った。それでは、君のすることは一つ、夢見る乙女のように願うことさ」"

    "言われた通り、私は願った。"

    "生きていればそれだけでいい。"

    "私だけが知っている海晴も、海晴だけが知っている私も消えてなくなる。"

    "桂子さんも、ソーニャも、茂継さんも、ユウくんも、スケールさんも、フェデリーコさんも、アランさんも。"

    "罪を背負うと言ってくれた直未も。"

    "私が初めて恋をした海晴も。"

    "みんなと過ごした記憶は、全て消える。"

    "でも、いい。"

    show let sta nor ser with std_change


    voice get_voice_filename("let")
    lete_unk1 "「それでは、お別れだ。君の未来に、幸あれ」"

    "生きてさえいれば、いいことあるよね、きっと。"


    jump fUNHAPPY

label f012_01GH.s2_2:




    voice get_voice_filename("rnk", 1866)
    rinka "「決まってる。そのままでいい」"

    show let sta nor ser with std_change


    voice get_voice_filename("let", 200)
    lete_unk1 "「よく言った。それでは、君のすることは一つ、ただ悲しみに耐え忍ぶことだ」"

    "苦しいだけの、何が苦しい？"

    "苦しめるのも、命なのだ。"

    "私は一人では私を認識できない。"

    "恋をしたから、自分を知ることができた。"

    "みんながいるから、獅子舞凛火でいることができた。"

    "それでいい。"

    "それがいい。"

    "だから消えないで。"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「それでは、お別れだ。君の軌跡を、大切に」"

    "私の、想い出たち――。"

    if flags_route_G:
        $ add_seen_chapter("12_2-3")
    elif flags_route_H:
        $ add_seen_chapter("12_3-3")


    jump fMIHARU
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc



label f004:



    python:
        set_info_scene("38")
        set_info_date(5, 21, "mon")
        set_info_time("morning")
        set_info_location("05")







    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    "目が覚めた時、私は久しぶりにぐっすりと眠れたことに気が付いていた。"

    "桂子さんが、脱落した。だが、私に残ったのは悲しみではなく、空しさだった。"

    "私はふと机の上を見た。"

    "桂子さんから受け取った手紙と私の書いた手紙の二つが置かれていた。"

    "だが桂子さんから受け取った手紙の中身を見てみると、それはただの白紙だった。"

    "「桂子さんが手紙を書いた」という行動とその結果が……消えている。"

    "まだ封をしていなかったので、私が書き写した手紙も確認してみた。こちらには、きちんと昨日のままの文面が残っていた。"

    "選定参加者の記憶には残っているが、期間中に起こした行動がなかったことになるというのは証明された。"

    "だが――。"

    show rnk paj nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「世界は完全には変わらない……」"

    "桂子さんから私に渡された便箋は、私の家から消えていない。"

    "考えられるのは、私が脱落したときにも手紙の文面だけが消え、私の机から手紙は消えないということだ。"

    "女神による世界の≪書き換え≫とやらは完璧ではない。"

    "直未に≪なかったこと≫になった火事の記憶があるのも、そのせいかもしれない。"

    "直未は、桂子さんのことをどこまで覚えているのだろうか。"

    "選定になるべく関わらせたくないから、私から聞くことはしないけれど。"

    show rnk paj arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴……！　直未……！」"

    "でも、私は二人の名前を口にしていた。"

    "そうせずにはいられなかったから。"

    "奥歯を噛み締めてから、私は今朝も学校へ行く準備を始めた。"









    $ set_info_location("14")

    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show rnk uni sur su1 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あっ……」"

    "校門まで来たとき、丁度直未と鉢合わせた。"

    "先週あんなことがあったばかりだから、ちょっと気まずい。"

    "でも、私は普通を装おうと、「おはよう」と挨拶をした。"

    show nom uni nor lau rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「おはようございます、せんぱい。わたしも今日から本格的に文化祭の準備を始めることにしました。看板とか装飾とか、考えないといけませんし」"

    show nom uni har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「もちろん、みんなにコーヒーの淹れ方も教えますっ。頼りないかもしれないですけど、頑張ります」"

    show nom uni nor smi rev with std_change

    voice get_voice_filename("nom")
    naomi "「だから来月の文化祭にはせんぱいも――絶対来てくださいね？」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、もちろんだよ」"

    "直未の顔を改めて見て、私は目元に土曜日までとの相違点に気付いた。よくみると髪型も少し変わっている。"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「そういえば、直未、コンタクトにしたの？」"

    show nom uni hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい。元々コンタクトにしようって思ってましたので、眼鏡割れちゃったのが偶然いいきっかけになりました」"

    "それだけの会話を交わすと、私たちは別々に校舎へ入って行った。"

    "直未に……気を遣わせちゃったな。"








    python:
        set_info_scene("39")
        set_info_time("evening")
        set_info_location("19")

    stop music fadeout 1
    scene bg hospitallounge on with fade_long
    play music audio.investigation
    pause 1

    $ show_hud()

    "学校にいる間、気になっていることがあった。"

    "それは、桂子さんの息子は無事産まれているかどうか、ということだった。"

    "病院に行けばそれくらいは教えてくれるはずと思い、ここまで足を運んでいた。"

    "結果、桂子さんの子供はちゃんと産まれているとのことだった。同時に私はその時、桂子さんが３週間前に亡くなっていることも聞いたのだった。"

    "話を聞いた私は、ラウンジに座ってひと休憩していた。"

    "人が死んだという話を聞くと、どうしても気が重い。"

    show rnk uni sur su2 at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あれ……うそ……」"

    "その時、私の前をスーツ姿の男性が通り過ぎた。赤ちゃんを抱えていて、診察を終えた後だろう。"

    show rnk uni cat sma with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、あの……」"

    "以前見かけた桂子さんの夫だ。"

    "私は直接話したことはないが、勇気をもって声をかけてみることにした。"





    stop music fadeout 1
    scene bg hospitallounge on with fade_long
    play music audio.nichijo03
    pause 1

    "あまり引き留めては悪いので、話したのは５分程度だった。"

    "彼は近くに住む母親に子供を預けているらしいが、今日は診察があるため仕事を早く上がって来たそうだ。"

    "子供のことはできるだけしてあげたい、と言っていた。"

    "桂子さんから義母が今風のキラキラした名前をつけたいという話を聞いていたので心配だったが、話に聞く彼女はいい人そうだ。"

    "そして何より意外だったのは――子供の名前だった。"

    "瓶淵春樹くん。"

    "あの子の名前は、奇しくも桂子さんがつけたがっていた名前と同じだった。"

    "生前、桂子さんは夫に自分の名前に込められた想いについて語ったことがあるらしい。"

    "桂子の桂は中国ではキンモクセイに代表されるモクセイ科、日本では木材に使用されることの多いカツラ科の植物を表している。"

    "香りが良いという特徴から誠実さを連想させる。もう一つ、カツラの木のように健康で丈夫に育って欲しいという意味もあるそうだ。"

    "旦那さんは桂子さんの死後そのことを思い出し、自分で名前をつけたいと母親に言ったらしい。"

    "桂のように何か樹木の漢字をつけると決めたそうだが、いいものが思いつかなかったそうだ。"

    "だから彼は、真っ直ぐな子に育つようにと「樹」そのものの漢字を選んだ。春に産まれた樹だから、春樹。"

    "私は桂子さんの手紙に書かれていた言葉を思い出した。"

    scene black with dissolve


    voice get_voice_filename("kik")
    keiko "『私は桂の木のように健康で丈夫ではいられなかったけれど、そうありたいと願い続けていました』"


    voice get_voice_filename("kik")
    keiko "『名前は、親から子に与える願いであり希望です。あなたにつけられた名前の意味を、ずっと大切に想い続けてください』"

    "私は立ち上がり、ライオン館に戻ることに決めた。"

    "いつまでもうじうじはしていられない。私は、凛としていなければならないから。"

    $ add_seen_chapter("4-1")








    python:
        set_info_scene("40")
        set_info_date(5, 24, "thu")
        set_info_time("evening")
        set_info_location("04")

    stop music fadeout 2
    scene bg lion01 evening with fade_longest
    play music audio.nichijo01
    pause 1

    $ show_hud()



    "桂子さんの脱落から、３日間。私は特に新しい情報を手に入れることができていなかった。"

    "アラン・スコーピオンのことを調べようと思っていたけれど、店を開けているということもあり、中々時間はとれなかった。"

    "時間の問題だけでなく、私の調べものへの苦手意識が大きいというのも理由の一つだ。"

    "このままではいけない、というのは分かっている。"


    show rnk uni nor nor at std_c with std_in
    voice get_voice_filename("rnk")
    rinka "「……よし」"

    "今日はお店を休みにして、図書館へ行くことに決めた。スコーピオンさんのことが書かれたビジネス書やインタビュー記事を探す。"

    "直未がいれば……と思いかけたところで、私は頭から振り払うようにして私服に着替えた。"









    $ set_info_location("18")

    stop music fadeout 1
    scene bg lion02 evening with fade_long
    play music audio.gimon
    pause 1

    "お店から出たときに、私は衝撃的な光景を目にした。"

    "店の正面の道に、一人の少女が横たわっていたのだ。というか、彼女は倒れていた。"

    show son sta wea clo rev at std_cr with std_in


    voice get_voice_filename("son")





    menu:
        sonya_unk1 "「…………」"
        "声をかける":

            $ flags_mhr_koukando += 1

            $ persistent.s7_1_seen = True
            $ grant_hear_all()
            jump f004.s1_1
        "声をかけない":

            $ persistent.s7_2_seen = True
            $ grant_hear_all()
            jump f004.s1_2

label f004.s1_1:



    show rnk uni arm nor rev at std_cl with std_in
    voice get_voice_filename("rnk", 425)
    rinka "「あ、あの……」"

    "心配になり、肩を叩いて声をかけてみた。"

    show son sta wea pek rev with std_change


    voice get_voice_filename("son", 2)
    sonya_unk1 "「…………きゅ～」"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……は？」"

    "声をかけて反応があったので、意識があるのは分かった。救急車を呼んだ方がよいのだろうかとも思ったが、どうにも緊迫感がなかった。"

    show son sta wea sta with std_change_wait

    "しばらく待ってみると、少女はこちらを振り向いた。"

    jump f004.s1_end

label f004.s1_2:


    "私がすべきこと、それは選定で生き残ること。"

    "そのためにはなるべく目立つ行動は控えなければならない。"

    "だが、倒れている人を見て放っておくこともできない。"

    "彼女を助ける方法は、何も私が直接声をかけることだけではないのだ。"

    "私はとにかく警察に連絡しようと思い、スマホを取り出した。"

    show son sta wea sta with std_change


    voice get_voice_filename("son", 3)
    sonya_unk1 "「…………じー」"

    "少女はわざとらしく言い、私の方へと顔を向けた。"

    show rnk uni arm nor rev at std_cl with std_in

    jump f004.s1_end


label f004.s1_end:

    "その顔を見て、私は血の気が引くのを感じた。"

    show rnk uni arm vig rev with std_change

    voice get_voice_filename("rnk", 427)
    rinka "「あなたは……！」"

    "彼女の顔を、私はもう３度目もにしている。夢の世界で。運命の大広間で。"

    "選定の参加者、彼女は“Ⅹ”の少女だ。"

    show rnk uni arm ang rev with std_change

    voice get_voice_filename("rnk")
    rinka "「どうしてっ……。まさか、名前があなたにも知られて……！」"

    "だとすれば、まずい。私はあまりに悠長に暮らし過ぎていたことになる。"

    "スコーピオンさんにばかり気をとられ、他の参加者に気が回っていなかった。"

    show son sta wea nor with std_change


    voice get_voice_filename("son", 4)
    sonya_unk1 "「ハイ。ソーニャはソフィア・プリズニェツィ・アレクセーエヴナと申す者であります。長いから、ソーニャと呼んでください」"

    $ gameinfo_cardbook_son_unlocked = True

    "少女は横になったまま、自己紹介をした。"

    show rnk uni arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、それはおかしいだろ」"

    "思わず、言葉が汚くなっていた。"

    "だが実際、選定の参加者がいきなり自己紹介するなどあり得ない。"

    show son sta wea sta with std_change

    voice get_voice_filename("son")
    sonya "「一つ、お願いがあります」"

    "私が答えないでいると、彼女の方が勝手に続けた。"

    show son sta wea pek with std_change

    voice get_voice_filename("son")
    sonya "「お腹が空いて動けなくなってしまったのであります。何か、ご飯を食べさせてください」"

    "彼女はカタコトでそう告げた。"

    "見れば、金髪で青い目の彼女はきっと北欧やロシアの出身だろう。日本語は分からないだろうから、本を通さないと会話はできないはずだ。"

    "しかし、スコーピオンさんは違ったのに、彼女はカタコトで話している。"

    "そもそも私は今、本を持っていない。ということは、考えられるのは一つだ。"

    show rnk uni sur su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「日本語が……分かる？」"

    show son sta wea nor with std_change

    voice get_voice_filename("son")
    sonya "「ハイ。ニッポンは大好きであります」"

    show son sta wea pek with std_change

    voice get_voice_filename("son")
    sonya "「スミマセンが、空腹が限界を迎えそうであります。あと５秒くらいでおしゃべりできなくなります」"

    show rnk uni cat sma rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ええっ、ちょっとちょっと！」"

    "私が驚いていると、彼女はそのまま電池が切れたかのように口を閉じてしまった。"






    python:
        set_info_time("night")
        set_info_location("21")



    stop music fadeout 1
    scene ecg familyrestaurantB1 nor with fade_long
    play music audio.comicaldays
    pause 1

    $ show_hud()

    "少女があまりに可哀想だったので、私は結局彼女を近所のファミレスに連れて行っていた。"

    "うちにも食べ物はあるが、ソーニャと名乗った彼女が選定の参加者である以上、さすがにライオン館に入れるのはまずいと思ったので、ファミレスを選んだ。"

    "ちなみに彼女の名前は、どうやら本当らしい。ファミレスに来る前、カードブックを確認したらきちんとカードが作られていた。"

    python:
        add_character_cards("rnk", ["10_name"])
        add_character_cards("son", ["10_name"])

    "彼女はカウントダウンをしてから喋らなくなってしまったため、店に着いて私はまずミートソーススパゲッティとハンバーグを注文した。"

    "この子くらいの年なら、嫌いな子はいないと思ったからだ。"

    "食べ物が運ばれてくると、今まで机に体重を預けていたソーニャはしゃき、と背筋を伸ばした。"

    show ecg familyrestaurantB1 ele with ecg_change

    voice get_voice_filename("son")
    sonya "「イタダキマス！」"

    scene ecg familyrestaurantA1 nor with dissolve

    voice get_voice_filename("rnk")
    rinka "「……喋れてるし！」"

    scene ecg familyrestaurantB1 hun with dissolve

    "思わず言ってしまった私をよそに、ソーニャはばくばくとご飯を食べ始めた。"

    "一気にかき込むのかとも思ったがそんなことはなく、きちんとパスタは巻いて、ハンバーグはちゃんとナイフとフォークを使っていた。"

    "鉄板の上のコーンも一粒ずつ器用に食べ終えている。"

    "皿の端にソースを飛び散らせたり、周りにこぼしたりすることもなく、空腹で倒れていた割には上品な食べ方だった。"

    show ecg familyrestaurantB2 ele with ecg_change

    voice get_voice_filename("son")
    sonya "「ゴチソウサマデシタ、であります。ニッポンのご飯、とっても美味しいでありますね！」"

    show ecg familyrestaurantB2 nor with ecg_change

    voice get_voice_filename("son")
    sonya "「感謝するであります。餓死寸前でありましたので」"

    scene ecg familyrestaurantA1 que with dissolve

    voice get_voice_filename("rnk")
    rinka "「いや、選定期間中はそういう理由じゃ死なないんだよね……？」"

    "そういえば、もし私が助けなかったら彼女はどうなっていたのだろう。"

    "その仮定こそ無意味なものか。きっと私ではない誰かが彼女を助けるだけだ。"

    "子供が倒れていたら、いくら冷たい都会とはいえ必ず誰かが手を差し伸べる。"

    show ecg familyrestaurantA1 ser with ecg_change

    voice get_voice_filename("rnk")
    rinka "「食べて元気が出たなら、色々教えて。あなたのことを」"

    scene ecg familyrestaurantB2 ele with dissolve

    voice get_voice_filename("son")
    sonya "「あなたではなく、ソーニャであります！」"

    show ecg familyrestaurantB2 que with ecg_change

    voice get_voice_filename("son")
    sonya "「そしてつかぬ事をお伺いしますが……」"

    "カタコトなのに、時々は難しい言葉を使えるらしい。"

    "私も家から持って来たし、ソーニャの鞄はカードブックが十分入りそうなサイズだったので、今はお互いカードブックを持っていると思う。"

    "それでもソーニャのカタコトが残っているということはつまり、やはり彼女は日本語で話しているということだろう。"

    "ロシア語で話していれば、きっと流暢な日本語に聞こえているはずなのだから。"

    show ecg familyrestaurantB2 ele with ecg_change

    voice get_voice_filename("son")
    sonya "「まだ、お腹が空いているであります。他のものも注文してよいでありますか？」"

    "パスタとハンバーグを食べているのだからもう十分、断ろうと思ったが、ソーニャは透き通った大きな目で見つめてきた。"

    scene ecg familyrestaurantA1 smi with dissolve

    voice get_voice_filename("rnk")
    rinka "「もう、分かった。ちょっとだけだよ？」"

    "お財布の中身を確認してから、ため息をつく。"

    "どうして選定の参加者――競うべき相手に優しくしているのか、自分でも分からなかった。"

    scene ecg familyrestaurantB2 smi with dissolve

    voice get_voice_filename("son")
    sonya "「おーっ、メニューがたくさんあります！」"

    "ソーニャはファミレスのメニューを開いて、興奮の声をあげる。"

    show ecg familyrestaurantB2 ele with ecg_change

    voice get_voice_filename("son")
    sonya "「ソーニャは、ファミレスというところに初めてきたであります！　色々目移りしてしまって、選べないでありますよ！」"

    show ecg familyrestaurantB2 que with ecg_change

    voice get_voice_filename("son")
    sonya "「洋食も和食も中華も、どれもあるなんて……。ボルシチまであります！　東の地で食す母国料理がどんな味か興味も湧いてきたであります」"


    voice get_voice_filename("rnk")
    rinka "「時々、変な言葉になるよね……。って、ボルシチが母国料理ってことは、ソーニャはロシアの出身ってこと？」"

    show ecg familyrestaurantB2 ele with ecg_change

    voice get_voice_filename("son")
    sonya "「ハイ！　ボルシチは正確にはウクライナ料理でありますが、ロシアでも一般的な料理であります」"


    voice get_voice_filename("rnk")
    rinka "「でもさ、ロシアにもファミレスはあるんじゃないの？　だったらそこまで珍しがらないでも……」"

    show ecg familyrestaurantB2 smi with ecg_change

    voice get_voice_filename("son")
    sonya "「ソーニャ、家にいることがほとんどでしたから……あ、決めました。ネギトロ丼と親子丼とカツ丼にします！」"

    scene ecg familyrestaurantA1 nor with dissolve

    voice get_voice_filename("rnk")
    rinka "「あ、ボルシチ頼まないんだ……っていうか全部丼物でいいの？　お米の量が凄いことになるよ」"

    show ecg familyrestaurantA1 sur with ecg_change

    voice get_voice_filename("rnk")
    rinka "「いや、そもそも３つも追加注文するの？　ちょっとって言ったよね？」"

    scene ecg familyrestaurantB2 que with dissolve

    voice get_voice_filename("son")
    sonya "「駄目……でありますか？」"

    "ソーニャはお腹を撫でながら首を傾げてきた。"

    scene ecg familyrestaurantA1 que with dissolve

    voice get_voice_filename("rnk")
    rinka "「……頼んだんだから、ちゃんと食べ切ってね」"

    "店員さんを呼んで、注文をする。ブザーを押すところを、ソーニャは興味津々といった調子で見つめていた。"

    "どうやらこれも知らないことらしい。"

    show ecg familyrestaurantA1 nor with ecg_change

    voice get_voice_filename("rnk")
    rinka "「はぁ～」"

    "ソーニャが美味しそうにご飯を食べているのを見ながら、私は若干の自己嫌悪に陥って、またため息をついていた。"

    "有り体に言えば、ちょろい。あるいは自分が子供であることを利用したソーニャの作戦なのかもしれないのだ。"

    "こうやって油断させて、私から情報を引き出そうとしているのかもしれない。"

    show ecg familyrestaurantA1 que with ecg_change_wait

    "だが、彼女からは全然そんな雰囲気が漂っていない。しかも、ソーニャの方が自分から個人情報を晒してしまっている。"

    "訳が分からなくて、私はまたため息をついていた。"

    "うう、頭が痛い……。"

    scene ecg familyrestaurantB3 smi with dissolve

    voice get_voice_filename("son")
    sonya "「ほふぅ～。お腹いっぱいであります。ごちそうさまでしたであります」"

    "見ると、３つの丼は全て綺麗に空になっていた。"


    voice get_voice_filename("rnk")
    rinka "「お箸……使えるんだ？」"

    show ecg familyrestaurantB3 ele with ecg_change

    voice get_voice_filename("son")
    sonya "「ハイ。ソーニャはニッポンが大好きでありますから。言葉も文化も、たくさん勉強しました」"

    show ecg familyrestaurantB3 nor with ecg_change

    voice get_voice_filename("son")
    sonya "「ニッポンは侍と魔法少女の国であることは、ばっちり勉強してきたであります。ぜひ一度会ってみたいものであります」"

    show ecg familyrestaurantB3 que with ecg_change

    voice get_voice_filename("son")
    sonya "「ところでそこのオジョウサマ」"


    voice get_voice_filename("rnk")
    rinka "「お嬢様っていうのは……違うかな。名前を教えるわけにもいかないし、お姉さんの方がいいかな」"

    show ecg familyrestaurantB3 smi with ecg_change

    voice get_voice_filename("son")
    sonya "「ではあらためまして、オネエサマ！　お願いがあります」"

    "さん、ではなく様になってしまっていることの指摘は諦めた。"

    scene ecg familyrestaurantA1 tro with dissolve

    voice get_voice_filename("rnk")
    rinka "「この流れだと、デザート？　もういいよ。その代わり、デザート食べたらちゃんと話してね。これは約束」"

    scene ecg familyrestaurantB3 smi with dissolve

    voice get_voice_filename("son")
    sonya "「アリガトウゴザイマス！　約束、ソーニャ約束したでありました！」"

    show ecg familyrestaurantB3 ele with ecg_change

    voice get_voice_filename("son")
    sonya "「あ、そのボタンはソーニャに押させてください！」"

    "結局、ソーニャはデザートにパフェとケーキを両方頼んだ。"

    "身体は小さいのに、どれだけ大食いなのだろう。"

    "つられて私も、デザートに小さなパフェを頼んでしまっていた。"





    scene ecg familyrestaurantB4 smi with fade_long
    pause 1


    voice get_voice_filename("son")
    sonya "「ゴチソウサマデシタ！」"

    "デザートまで綺麗に平らげてから、ソーニャは元気よく言った。一つをゆっくりと食べている私よりも、彼女の方が早く食べ終わってしまった。"

    scene ecg familyrestaurantA2 ser with dissolve

    voice get_voice_filename("rnk")
    rinka "「もう……いいでしょ？」"

    "分かってるよね、という確認を取ったつもりだ。"

    "相手は子供だけれど、これは取引でもあるのだ。"

    "この子が満腹になったら、どうしてライオン館の前で倒れていたのか、何故にすぐ名前を明かしたのか――他にも、全て話してもらう。"

    scene ecg familyrestaurantB4 ser with dissolve

    voice get_voice_filename("son")
    sonya "「ワカリマシタ」"

    show ecg familyrestaurantB4 ele with ecg_change

    voice get_voice_filename("son")
    sonya "「ソーニャは、ソフィア・プリズニェツィ・アレクセーエヴナと申す者であります。長いので、ソーニャと呼んでください」"


    voice get_voice_filename("rnk")
    rinka "「いや、それさっき聞いたから！」"

    show ecg familyrestaurantB4 nor with ecg_change

    voice get_voice_filename("son")
    sonya "「……オネエサマは面白いであります！」"

    scene ecg familyrestaurantA2 que with dissolve

    voice get_voice_filename("rnk")
    rinka "「からかってる……？」"

    scene ecg familyrestaurantB4 tor with dissolve

    voice get_voice_filename("son")
    sonya "「声も怖いであります……」"

    scene ecg familyrestaurantA2 ser with dissolve

    voice get_voice_filename("rnk")
    rinka "「『も』ってことは他に何が恐いの？」"

    scene ecg familyrestaurantB4 smi with dissolve

    voice get_voice_filename("son")
    sonya "「顔、でありますね。初めてお会いした時から、恐い方だなぁと思っていましたであります」"

    "ソーニャは、満面の笑みで言ってみせた。"

    "あまり気にしていないとはいえ、目付きが悪い自覚はあるので、こうもはっきり言われると少し傷付く。"

    scene ecg familyrestaurantA2 ser with dissolve

    voice get_voice_filename("rnk")
    rinka "「――って、話を逸らさないで」"

    scene ecg familyrestaurantB4 ser with dissolve

    voice get_voice_filename("son")
    sonya "「スミマセン、オネエサマはいい人だったので、もう少しお話をしたかったんでありますけれど、ご迷惑でしたね」"

    show ecg familyrestaurantB4 sm2 with ecg_change

    voice get_voice_filename("son")
    sonya "「心配しなくて大丈夫であります。今週末のセンテイ――次の脱落者は、ソーニャでありますから」"

    "彼女は笑顔で、だけど少しだけ翳りのある表情で、告げた。"

    "言っている意味を理解するのに、私は時間を要していた。"






    python:
        set_info_scene("41")
        set_info_time("night")
        set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    pause 1

    $ show_hud()

    "自分でも、どうしてこうなるのかよく分かっていなかった。"

    "都心ということもあり、ファミレスは混雑していた。待っているお客さんもいたらしい。"

    "店員さんに、「そろそろご退店をお願いします」と声をかけられてしまった。"

    "話の途中にもかかわらず、だ。"

    "ソーニャの言葉の意味を、私はまだちゃんと分かっていなかったのだ。"

    "だから――。"


    play music audio.nichijo01

    show son sta nor la1 rev at std_cl with std_in

    voice get_voice_filename("son")
    sonya "「はわー、すごくいい雰囲気のお店でありますね」"

    "私はソーニャを、ライオン館まで連れて帰って来てしまった。"

    "他にゆっくり話ができるところも思いつかなかったし、ソーニャはよくて中学一年生にしか見えない。"

    "しかも私は制服だし、日も落ちているので、外を歩いていると警察に声をかけられるかもしれないからだ。"

    show lete normal at cat_r with std_in


    voice get_voice_filename("cat")
    lete "「にゃーお」"


    voice get_voice_filename("son")
    sonya "「にゃ、にゃんこ！」"


    voice get_voice_filename("rnk")
    rinka "「なんでそんな言葉知ってんの……。って、レテ、あんた来てたんだね」"

    "随分と久しぶりにレテの姿を見た気がする。"

    "エサ箱は毎度空になっていたので、無事なのは分かっていたけれど。"


    hide lete with std_out

    show son sta exp exp rev with std_change

    voice get_voice_filename("son")
    sonya "「にゃんこ♪　にゃんこ♪　日本の猫さんも可愛いであります。ほぅらパサジール、猫さんでありますよー」"

    show lete normal at cat_r with std_in


    voice get_voice_filename("cat")
    lete "「にゃお」"

    scene ecg pasajiru nor with dissolve_long

    "パサジールというのは、ソーニャが持っているぬいぐるみのことのようだ。"

    "雑貨屋によくある、ストラップになっているような手のひらサイズのぬいぐるみ。熊がモチーフだから、テディベアと言ってもいいだろうか。"


    scene bg lion01 night with dissolve_long

    "そのぬいぐるみと一緒に、ソーニャはレテの首の皮を引っ張ったり、ほっぺたをぐにぐにしてじゃれている。"

    "気難しい猫なので私が同じことをすれば引っかかれそうだが、相手が子供と分かっているのか、目を細めて何とも言えない表情でされるがままにしていた。"

    show rnk uni arm ama rev at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「仕方ない。今日はミルクも用意してあげるよ」"

    show son sta ban lau rev at std_cl with std_in

    voice get_voice_filename("son")
    sonya "「ソーニャにもお願いするであります！」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「はいはい。ちょっと待っててね」"

    hide rnk
    hide son
    with std_out

    "自分の家ということもあり、私の方も自分のペースで行動することができた。"

    show lete normal at cat_c with std_in

    "私はソーニャの牛乳を机の上に置き、レテのミルク皿を机の下に置いた。"

    "そして、ソーニャが座った後、私は向かい側に座った。レテはと言うと、ソーニャから解放されるやいなやミルク皿へと飛んで行った。"

    "やはりあの扱いは嫌だったらしい。"





    play music audio.myroom_night
    scene ecg nighttalkB2 ser with dissolve_long


    voice get_voice_filename("son")
    sonya "「さっきの続きで、ありますね」"

    "ソーニャは両手でグラスを持ち、口をつけた。"

    "ファミレスの時もそうだったけれど、彼女のそういう所作には育ちの良さが出ていた。"

    "私が頷くと、ソーニャはレテとじゃれていた時とは打って変わって落ち着いた口調で続けた。"

    show ecg nighttalkB2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「言葉通りの、意味でありました」"

    show ecg nighttalkB2 que with ecg_change


    voice get_voice_filename("son")
    sonya "「ですが、オネエサマはソーニャのことを信じてくれたでありますね？　だから、ここに連れて来てくれた」"

    show ecg nighttalkB2 ser with ecg_change


    voice get_voice_filename("son")
    sonya "「ちゃんと、話すであります。ソーニャのこと」"

    show ecg nighttalkB2 que with ecg_change


    voice get_voice_filename("son")
    sonya "「でも、聞かせてほしいであります。どうしてソーニャを信じてくれたですか？」"

    scene ecg nighttalkA2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「自分の名前を教えたり、次の脱落者だって宣言したりするメリット、あなたにはないでしょ。それに、私の情報を探りたいって感じでもなかった」"

    "感覚で信じたわけではない。"

    "ソーニャが子供だからって油断したわけでもない。来る途中、わざと遠回りをした。"

    "ソーニャが万が一他の参加者と協力していた場合、尾行の可能性もあったから、それを確かめたかったのだ。"

    scene ecg nighttalkB2 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「だからね、あなたには悪いけど、あなたのことを信じたわけじゃないんだ」"

    "私が信じたのは、あくまで私だ。"

    show ecg nighttalkB2 nor with dissolve


    voice get_voice_filename("son")
    sonya "「オネエサマは顔に似合わず、優しいでありますね」"


    voice get_voice_filename("rnk")
    rinka "「……一言余計なんだけど」"

    show ecg nighttalkB2 ele with ecg_change


    voice get_voice_filename("cat")
    lete "「にゃーお」"

    "真面目な話を切り出すところで、レテがちょうど鳴き声を上げた。ミルクを飲み終わって満腹なのか、そのまま机の下で丸くなってしまった。"

    show ecg nighttalkB2 smi with ecg_change_wait

    "ソーニャはレテを見て微笑んだ。"

    show ecg nighttalkB2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「ソーニャの家も、猫を飼っていたであります。ソーニャは病気でほとんど家を出ることがなかったでありますから、猫と本とインターネットと……そしてパサジールが友達でした」"

    show ecg nighttalkB2 sm2 with ecg_change


    voice get_voice_filename("son")
    sonya "「ソーニャの死因はもう分かったでありますね？　病気です。もっと詳しく知りたければ教えますが、必要ですか？」"

    scene ecg nighttalkA2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「ううん。今はあなたの話を、続けて」"

    "カードは生成されなかったが、話を聞くことを優先する。"

    "ソーニャがこのように話したということはつまり、死因も教えていいということだからだ。"

    "本当に、ソーニャは自分が次の脱落者だと思っているのだ。その理由の方が、気になる。"

    scene ecg nighttalkB2 ser with dissolve


    voice get_voice_filename("son")
    sonya "「≪女神のセンテイ≫によって、ソーニャは一時的に生きることができています。オネエサマと同じように」"

    show ecg nighttalkB2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「ソーニャはパパとママに≪センテイ≫のことを話しました。いつもより元気なことが、その証明になりました」"

    show ecg nighttalkB2 ser with ecg_change


    voice get_voice_filename("son")
    sonya "「ですが、ソーニャの病気は≪センテイ≫の最後の一人になっても治るものではないと思います。つまり、12週間寿命が延びても、その先は長くはないと言うことです」"

    show ecg nighttalkA2 que with ecg_change


    voice get_voice_filename("rnk")
    rinka "「選定が終わっても、病気は完治するわけじゃないってこと？」"

    show ecg nighttalkB2 sm2 with ecg_change


    voice get_voice_filename("son")
    sonya "「ハイ、そういうことだと思うであります」"

    show ecg nighttalkB2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「だからソーニャは、負けてもいいと思ったであります。代わりに許された時間だけでも、外の世界を見たかったであります」"

    show ecg nighttalkB2 ser with ecg_change


    voice get_voice_filename("son")
    sonya "「家の中から世界を見て、ソーニャは日本に憧れていたであります。日本の文化……ニンジャサムライではない、現実の日本に触れてみたかったであります」"

    show ecg nighttalkB2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「カードブックを手にしたとき、少しわくわくしてしまったであります」"


    voice get_voice_filename("son")
    sonya "「ソーニャの大好きな日本のアニメでは、魔法少女はこのようなカードとカードブックを使って変身して、戦っていました」"

    show ecg nighttalkB2 smi with ecg_change


    voice get_voice_filename("son")
    sonya "「ソーニャの未練は……世界を見ること、であります。それを、叶えたかった」"

    scene ecg cardbook bli with dissolve

    "私のカードブックが光り、カードが生成された。"

    python:
        add_character_cards("rnk", ["10_regret"])
        add_character_cards("son", ["10_regret"])

    scene ecg nighttalkB2 sm2 with dissolve

    "ソーニャはそれを見て、にっこりとした表情を浮かべた。ファミレスで見せたどこか寂し気な表情だ。"

    "悟ったような彼女の顔は、まだ小学生くらいのあどけなさとは不釣合いであった。"

    show ecg nighttalkB2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「だからしばらく様子を見た後、パパとママと一緒に日本へ旅行することに決めたのであります」"

    show ecg nighttalkB2 ser with ecg_change


    voice get_voice_filename("son")
    sonya "「ソーニャが脱落したらパパもママも旅行のことを忘れちゃうかもしれないですけれど、せめて、もらった時間を有意義に使ってみたかったのであります」"


    voice get_voice_filename("rnk")
    rinka "「でも一人でいたってことは、何かあったんだね？」"

    show ecg nighttalkB2 ser with ecg_change


    voice get_voice_filename("son")
    sonya "「ハイ。その通りであります」"


    voice get_voice_filename("son")
    sonya "「ソーニャたちが様子見をしていた間に、ソーニャの≪氏名≫のカードを持っている人は、ソーニャたちの行動を見張っていたみたいなのでありました」"

    show ecg nighttalkB2 tor with ecg_change


    voice get_voice_filename("son")
    sonya "「空港についてタクシーに乗ったのですが、それこそが罠でした」"


    voice get_voice_filename("rnk")
    rinka "「罠……？」"

    show ecg nighttalkB2 ser with ecg_change


    voice get_voice_filename("son")
    sonya "「ハイ。選定の参加者さんでありました。パパとママを殺されたくなければ、情報を教えろ……そういう脅しをされてしまったのであります」"


    stop music fadeout 1
    scene ecg nighttalkA2 sur with dissolve

    "ソーニャの言葉を聞いて、私はまさか、と悪い直感が働いた。"

    "桂子さんの息子や他の赤ちゃんたちを人質にしたあの男――アラン・スコーピオンとやり方が似ている。"

    show ecg nighttalkA2 ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「その人って……Ⅻの男の人だった？」"

    scene ecg nighttalkB2 ser with dissolve


    voice get_voice_filename("son")
    sonya "「いいえであります」"

    "彼女の否定を受けて、私はほっとすることはできなかった。"

    "それはつまり、似たような手段をとる人が他にいるということだからだ。"


    play music audio.badguys

    show ecg nighttalkB2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「２人組、でした。Ⅲの男の人と、Ⅺの女の人です」"


    voice get_voice_filename("rnk")
    rinka "「その２人が！」"

    show ecg nighttalkB2 que with ecg_change


    voice get_voice_filename("son")
    sonya "「会ったこと、ありましたですか？」"

    scene ecg nighttalkA2 ser with dissolve

    "ソーニャの質問に、私は首を振って答えた。"

    "Ⅲの男性――フェデリーコ・カルミナーティ。私が氏名のカードを持っている人物だ。"

    "夢の世界で見た彼は、背の高い細身の男性だった。"

    "Ⅺの女性は、２回目の選定でⅦの男性を脱落させた人だ。Ⅻのスコーピオンさんと同じように、とても冷徹な目をしていた。"

    "まさかその２人が協力関係にあったとは。Ⅲの男性に対してはこちらが氏名を分かっているから多少有利に働くと思っていたけれど、あの女性と組んでいるのなら、有利はないのと同じだろう。"

    "私は遮ったことにごめん、と添え、ソーニャの話の続きを待った。"

    scene ecg nighttalkB2 nor with dissolve


    voice get_voice_filename("son")
    sonya "「パパとママのため、ソーニャは自分の情報を教えたであります。しかし、男性はそれだけでは済ませない、持っているカードを全部教えろと言ったのであります」"

    show ecg nighttalkB2 ser with ecg_change


    voice get_voice_filename("son")
    sonya "「ソーニャは、Ⅺの方のカードを持っていたであります。未練のカードです。だから、言ったであります」"

    show ecg nighttalkB2 que with ecg_change


    voice get_voice_filename("son")
    sonya "「教えてもいいでありますけれど、仲間割れの原因になるでありますよ、と。女性の方を見ながら」"

    show ecg nighttalkB2 ser with ecg_change


    voice get_voice_filename("son")
    sonya "「怒られるかと思ったであります。でも、Ⅺの女性は笑ったのです」"


    scene bg lion01 night with dissolve_long

    "――こいつは面白い。この年であのおっさんよりも肝が据わった交渉をしやがる。"

    "それにこいつの未練を見たか？　世界を見ることだってさ。いいじゃねえか。させてやろうぜ？"

    "あたしは中々に気に入ったぜ、このガキのことをよ。"

    "――Ⅺの女性は豪快な声でこのように話したと言う。"

    "ただし条件がある。変な気を起こさないように、最後の一日以外はソーニャは両親と別行動で観光すること、だそうだ。"

    "約束さえ守れば彼女らはソーニャのことを邪魔しないし、両親に手を出さないということである。"

    scene ecg nighttalkA2 ang with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「そんなの！　勝手な条件だ。ソーニャのためじゃない。女の人が情報を知られたことを察したから、未練と顔を手掛かりにソーニャたちが情報を集めるのを防いだだけ」"


    play music audio.myroom_night
    show ecg nighttalkA2 ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「……ごめん。いきなり大声出して」"

    scene ecg nighttalkB2 smi with dissolve


    voice get_voice_filename("son")
    sonya "「オネエサマは恐いですけど、優しいでありますね。脱落させるべき相手の、ソーニャのために怒ってくれるなんて」"

    show ecg nighttalkB2 sm2 with ecg_change


    voice get_voice_filename("son")
    sonya "「でも、いいんです。パパとママが助かるであります。それにさっきも言ったように、ソーニャはどうあっても、長くは生きられないでありますよ」"


    voice get_voice_filename("rnk")
    rinka "「ソーニャは死を受け入れているの？」"

    show ecg nighttalkB2 que with ecg_change


    voice get_voice_filename("son")
    sonya "「死を受け入れる、でありますか？」"


    voice get_voice_filename("rnk")
    rinka "「えっと……死んでも仕方がないって、思ってるってこと？」"

    show ecg nighttalkB2 sm2 with ecg_change


    voice get_voice_filename("son")
    sonya "「ハイ。選定が始まる前からです。ソーニャは、自分が病気だと分かった時からずっと、いつか死ぬって分かってましたから」"

    "これが、ソーニャの寂しげな微笑の正体だったのだろう。"

    "お医者さんからか両親からか分からないけれど、病気の彼女はきっと、何度も余命を聞かされてきたのだろう。"

    "大切に育てられたことは、ソーニャを見ていれば分かる。"

    "だが、ソーニャにとって近い将来に迫る死の運命はずっとそばに立ち続けていたことだろう。"

    "ずっと分かってたっていうことは、ずっと覚悟していたということは、ずっと怯えていたということでもあるのだろう。"

    scene ecg nighttalkA2 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「……辛かったね」"

    "私はソーニャの頭を撫でていた。"

    "桂子さんの時に簡単に同情してはいけないと学んだはずなのにもかかわらず、私はこうせずにはいられなかった。"

    "ソーニャはきっと、両親のため、周りの人のため、死を諦め、気丈に振舞っていたのだろう。"

    "だが、心から死を受け入れられるはずはない。その証拠が、顔に現れていた。"

    scene ecg nighttalkB2 ser with dissolve


    voice get_voice_filename("son")
    sonya "「死ぬのは分かっていたことであります。だから辛くないと、思っていたでありますが……」"

    show ecg nighttalkB2 tor with ecg_change


    voice get_voice_filename("son")
    sonya "「本当に辛くないのか、今は分からないであります」"

    "私は彼女を、真の意味で助けることはできない。"

    "いくらソーニャが私より年下でも、可哀想でも、自分が死ぬのと引き換えにはできないから。"

    "そもそも今日出会ったばかりなのだ。ソーニャとはまだ友達になってもいないだろうに。"

    "けれども、私はどうしてか、ソーニャのために何ができるかを考えていた。"

    "ソーニャはずっと、不思議そうな顔を浮かべていた。"

    "きっとまだ彼女は自分でも、自分の心を理解していない。おかしなことはない。私だってそうなのだから。"

    "レテの姿は、いつの間にか消えていた。空のミルク皿が、照明の光を浴びて濃い影を作っていた。"

    "私はその間ずっと、ソーニャの頭を撫でていた。"

    $ add_seen_chapter("4-2")








    python:
        set_info_scene("42")
        set_info_date(5, 25, "fri")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_refreshing_morning
    pause 1

    $ show_hud()



    show son sta ban lau at std_c with std_in

    voice get_voice_filename("son")
    sonya "「オハヨウゴザイマス！」"

    show rnk paj sur su2 rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「うわぁっ」"

    show son sta nor la1 with std_change

    voice get_voice_filename("son")
    sonya "「オネエサマ、起きてくださいでありまーす」"

    "いきなり耳元に響いた声に驚き、私は思わず声を出してしまった。"

    "声の主は、ソーニャだ。"

    "あの後ソーニャから宿をとっていないことを聞き、仕方がないのでうちに泊めることにした。"

    show son sta nor sur with std_change

    voice get_voice_filename("son")
    sonya "「しかし驚きました。マンガキッサという宿泊施設にすぐ泊まれるものかと思っていたでありますから」"

    show rnk paj nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「その偏った知識は、ネットで得たんだよね、たぶん。漫画喫茶って別にホテルじゃないからさ……」"

    "私が呆れながら言うが、ソーニャは首を傾けた。"

    "漫画喫茶に泊まる人は多いと聞くが、あの椅子だけのところで一晩過ごすのは辛いだろう。"

    "それに、子供が深夜の漫画喫茶に入れてもらえるとも思えない。"

    show son sta que tro with std_change

    voice get_voice_filename("son")
    sonya "「オネエサマ、よかったのでありますか？」"

    "ソーニャは大きな目を丸くして、再び首を傾けた。その質問の意味は分かっていた。"

    "昨日、約束をしたのだ。"

    "ソーニャと一緒に、少しだけだけれど、日本を案内してあげるって約束だ。"

    "日本語ができるとはいえ、見知らぬ文化では不便も多いだろう。それに何より――。"

    show rnk paj arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……１人よりも２人の方が楽しいでしょ？」"

    show son sta nor smi with std_change

    voice get_voice_filename("son")
    sonya "「オネエサマ……」"

    show son sta nor lau with std_change

    voice get_voice_filename("son")
    sonya "「優しい人に出会えて、ソーニャは嬉しいです。それだけでも、日本に来た甲斐があるであります」"

    show rnk paj arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「感動するのはちゃんと思い出を作ってからにしなね。日本って言っても東京だけだから案内できるところは少ないけどさ」"

    "選定の期間中、思い出を作ることには、意味がある。"

    "ソーニャが日本を――外の世界を旅したという事実は、私が最後の一人になれば、思い出として残るのだから。"

    show rnk paj arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、でも昨日言った通り学校があるから、夕方に新宿駅で待ち合わせだよ？」"

    show son sta ban lau with std_change

    voice get_voice_filename("son")
    sonya "「ハイであります！」"

    "ソーニャはにっこりと笑うと、手を伸ばして元気よく返事をした。"

    "その笑顔の裏に隠されているものに、私はまだ気がついていなかった。"







    $ set_info_location("08")

    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()



    show mhr uni sco smi at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「おはよう、凛火」"

    show mao uni nor che at std_r with std_in

    voice get_voice_filename("mao")
    mao "「おはたん～」"

    show rnk uni nor nor rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「うん、おはよう」"

    show mao uni nor no1 with std_change

    voice get_voice_filename("mao")
    mao "「あ、今の実はおはようりーたんを略したんだよぉ」"

    "最近は、学校に来ると少し安心するようになっていた。"

    "どんなに大変なことが起こっていても、私の日常はここにあると。"

    show mao uni nor irr with std_change

    voice get_voice_filename("mao")
    mao "「え、無視ぃ？」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「どんな反応を期待してたんだ……」"

    show mao uni nor sle with std_change

    voice get_voice_filename("mao")
    mao "「んじゃ、お休み～」"

    hide mao with std_out

    show mhr uni sco wic with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。相変わらずの真央を見ると安心するね」"

    "真央はその質問に答えることなく、机に伏して寝てしまった。"

    "昨日夜更かしをしていたのだろう。きっと今日は昼休みまで起きないに違いない。"

    "相変わらず自由だなあ、と私は微笑んでいた。"

    "そう、私の日常はここにあるのだ。"







    $ set_info_time("noon")

    scene bg schoolroom noon with fade_long
    pause 1

    $ show_hud()



    show mao uni nor sle at std_r with std_in

    voice get_voice_filename("mao")
    mao "「ねみぃ～。うち昼飯いらね。寝てる！」"

    hide mao with std_out

    show mhr uni nor nor at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「ということだから、二人で屋上に行こうか」"

    show rnk uni nor smi rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「そうだね。って、今日は特に眠そうだけど、何してたの？」"

    show mao uni sel glo at std_r with std_in

    voice get_voice_filename("mao")
    mao "「ネットでドラマの一挙放送を見てたら、朝だったんだよぅ」"

    show rnk uni sur su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「え、じゃあ寝てないの？」"

    show mao uni nor sle with std_change

    voice get_voice_filename("mao")
    mao "「だから今寝てるのだよ……」"

    hide mao with std_out

    "あ、もう駄目だ。"

    "海晴もそんな表情を浮かべていた。"







    $ set_info_location("15")

    stop music fadeout 1
    scene bg schoolrooftop noon with fade_long
    play music audio.miharu
    pause 1



    show mhr uni sco smi rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「二人きりになるのは、ずいぶん久し振りの気がするね」"

    "購買でパンと飲み物を買って、私たちは屋上へと来ていた。"

    "海晴は相変わらずの小食だ。"

    "今日は天気もよく、いい青空だ。"

    "にもかかわらず他の生徒がいないのは、やはり私たちが避けられているからだろう。"

    "最近では、そのことが都合よくすらあった。"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「選定が始まってからもまだこういう時間が取れることが、ぼくは嬉しいよ」"

    "海晴はそう言うと、いつもの調子で微笑みかけてきた。"





    menu:
        "私は――。"
        "嬉しい":

            $ flags_mhr_koukando += 1

            $ persistent.s8_1_seen = True
            $ grant_hear_all()
            jump f004.s2_1
        "気まずい":

            $ persistent.s8_2_seen = True
            $ grant_hear_all()
            jump f004.s2_2

label f004.s2_1:

    show rnk uni nor smi at std_cr with std_in

    voice get_voice_filename("rnk", 476)
    rinka "「私も嬉しいよ、海晴」"

    show mhr uni sco sh1 rev with std_change

    voice get_voice_filename("mhr", 96)
    miharu "「凛火……」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「きっと海晴も、選定のことで色々苦労してるよね。でもそういうのを忘れて……こうしてゆっくりお昼を食べられるっていうのはとても、嬉しい」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくはとても幸せだ。やっぱりぼくは、凛火の笑顔のためにずっと――」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「そういう話は、今はやめとこ」"

    "あの日、喫茶店で私を生かすと宣言した海晴の顔が思い出された。"

    "そのことはまだ、私の中で解決してはいないのだ。"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……失礼した。ところで、君に聞きたかったんだけれど」"

    "海晴はパンに手をつけると、話題を切り替えた。"

    jump f004.s2_end

label f004.s2_2:



    show rnk uni arm sad at std_cr with std_in

    voice get_voice_filename("rnk", 479)
    rinka "「いいのかな、これで」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr", 99)
    miharu "「何を迷っているんだい？」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私たちはさ、選定の参加者なんだ。いい加減、その実感は湧いてきたよ。でも、この毎日を最優先にしてる。本当にそれで、いいのかなって思ったんだ」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「構わないよ。たとえ君が何もしなくても、ぼくが守るさ。命に換えても――」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴！」"

    "私はそこで、自分の声が思った以上に大きくなってしまっていたことに気がついた。"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめん、大声出した」"

    show mhr uni pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ううん、ぼくが悪かった。話題を変えよう。丁度、君に聞きたかったことがあるのだけれど」"

    jump f004.s2_end



label f004.s2_end:

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr", 102)
    miharu "「日辻さんとは、最近会っていないのかい？」"

    "何気ない日常会話だったけれど、海晴の表情は真剣だった。"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk", 483)
    rinka "「もう、コーヒーの淹れ方はばっちりだから。直未の方も本格的に文化祭の準備で忙しくなるしね」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……何か、あったね？」"

    "海晴には、直未と協力していることは黙っていた。"

    "どちらにも余計な負担をかけたくないからだ。"

    "だから今の言葉に、私はどう答えればいいか分からなくなってしまった。"

    "戸惑う私をよそに、海晴は続けた。"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「日辻さんは一般人だ。ぼくが凛火に協力するというのとはわけが違うよ」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「危険なことは分かっているから、君は日辻さんを遠ざけたのだろう？　それが正解だ」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「どうしてそれを知っているか――というのは聞かないで欲しいよ。ぼくは少なくとも人間関係において、凛火ほど察しが悪くないからね」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君に会いに行く日辻さんの目はそうだな……先週から随分と変わっていた。使命感に満ちていた、と言うべきかもしれないね」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……そうだね。海晴に隠しても仕方がなかった」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「君がぼくや真央を気遣ってくれたことはよく分かっている。気にしなくていい」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「ありがと」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、でも海晴の言う通り、直未に調べものとか手伝ってもらうのはやめたよ。これからは一人で――頑張るから」"

    show mhr uni pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくに頼ってくれても……いいのにな」"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「え？」"

    show mhr uni pai ten rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ちょっと待って」"


    play music audio.gimon

    "海晴は屋上の入り口に目を向けると、声のトーンを落として言った。"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「誰かがこっちを見てる。物音がした」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「生徒じゃないの？」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「だったら問題ないよ。でも、そうじゃなかったら？」"

    "海晴の言いたいことは分かった。もし選定の参加者が学校に潜入して、私たちを見張っていたら――ということだ。"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくが扉を開ける」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、一緒に行こう。２人の方がいいと思う」"

    hide rnk
    hide mhr
    with std_out

    "海晴は頷き、私たちは帰るフリをして扉の方へと向かった。足音は聞こえなかったので、きっとまだそこにいるはずだ。"

    "私たちの予想は、概ね当たっていた結果となった。"



    play music audio.comicaldays

    show son sta wea pek at std_r with std_in

    voice get_voice_filename("son")
    sonya "「きゅ～」"

    show mhr uni pai irr rev at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「お前はっ！」"

    show son sta wea sta with std_change

    voice get_voice_filename("son")
    sonya "「お腹が、空いたであります……。お、オネエサマ……」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「どういうこと？」"

    "海晴は私の方に、疑問の視線を向けた。"

    show rnk uni nor que rev at std_l with std_change

    voice get_voice_filename("rnk")
    rinka "「えーっと、話すとちょっと長くなるんだけど……」"

    "私はあわあわとしながら、とりあえず頭を抱えた。"






    python:
        set_info_scene("43")
        set_info_time("evening")
        set_info_location("09")



    stop music fadeout 1
    scene bg maidcafe with fade_long
    play music audio.maidcafe
    pause 1

    $ show_hud()

    show mhr mai sco cau rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「凛火……今回ばかりは君を馬鹿と言わずにはいられないよ」"

    show rnk uni nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「うん。甘んじて受け入れる」"

    show son sta exp exp at std_r with std_in

    voice get_voice_filename("son")
    sonya "「はわー！　ここが噂に聞くメイド喫茶でありますね！」"

    "ソーニャはテーブルから離れて、店内を歩きながら眺めていた。ある意味こういうお店こそ、ロシアでは見られないかもしれない。"

    "私もできれば、２度目は来たくなかったのだけれど。いや、お店自体を否定するわけではなくて、雰囲気が苦手なのだ。男性客ばかりで、私たちはどうしても浮いてしまうし。"

    "日本のアニメや漫画などのコンテンツでは、学校が舞台であることが多いため、ソーニャは元々学校に興味があったらしい。"

    "だが、ソーニャ自身は病気の関係で通信制の学校だったそうで、ロシアでも経験がなくイメージが湧かなかったらしい。"

    "ソーニャにとっては学校に行ってみること自体もまた、世界を見ること。"

    "だから、飴茶に忍び込んで私の様子を観察していたらしい。"

    "普通バレるだろとも思ったが、ソーニャはこう言っていた。"

    show son sta ban lau with std_change

    voice get_voice_filename("son")
    sonya "『忍者の勉強をしていましたから、ばっちりでありますっ』"

    hide son with std_out

    "丁寧に印まで結んでいた。私が小学生くらいの頃にやっていたアニメの真似らしい。"

    show mhr mai sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「友人のぼくとしては、きみが優しい人であることを誇るべきなのかもしれないけれどね」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、もうフォローとか辛くなるからやめて」"

    "呆れた声で言う海晴に、私は小声で答えていた。"

    "あの後すぐに昼休みが終わってしまったので、ソーニャには放課後までどうにか隠れていてもらい、私たちは放課後に合流。"

    "３人で帰ることにして、私がソーニャを泊めることになった経緯を説明した。"

    "海晴はバイトがあるので後でまた話の続きを……となったところで、話題は海晴のバイトの話になった。"

    "日本に対して偏った知識を持っているソーニャからすると、メイド喫茶は清水寺のようなものらしく、連れて行く流れになってしまったのだった。"

    show mhr mai sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「もっとも、君はあの子を気にかけたことを後悔はしていないのだよね？」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん」"

    show mhr mai sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「なら、やはりぼくは凛火を誇ろう」"

    hide mhr
    hide rnk
    with std_out

    "そこまで話したところで、ソーニャがテーブルへと戻って来た。"

    "店内には装飾やコミュニケーションノートもあるので、テーブルを立つお客さんは少なくない。"

    "だが、ソーニャのような少女が店内を歩き回るのはさすがに目立つ。現に、彼女が戻って来たこのテーブルは注目を浴びていた。"

    show son sta que que at std_r with std_in

    voice get_voice_filename("son")
    sonya "「そういえばメイドさんって普通家事をするんですよね？　ミハルはどうして高校生なのにメイドさんなのでありますか？」"

    show mhr mai sco wic rev at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「ぼくはただのアルバイトだからね。そもそも、君の思うようなメイドは日本にはいないよ」"


    show rnk uni nor nor rev at std_l with std_in
    voice get_voice_filename("rnk")
    rinka "「そんな、夢を壊すようなこと……」"

    show son sta nor la1 with std_change

    voice get_voice_filename("son")
    sonya "「ほへー、なるほどであります。てっきりミハルも魔法少女なのかと思っていました」"

    show mhr mai sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それよりぼくの名前……いや、凛火が呼んでいたのを聞いたのか……」"

    show son sta que que with std_change

    voice get_voice_filename("son")
    sonya "「オネエサマ、このと・く・せ・いパンケーキってなんですか？」"

    show rnk uni sur su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「うわ……ここにもあるんだこういうの……。えーっと、パンケーキにメイドさんが絵を描いて、美味しくなる呪文を唱えてくれます……だって……」"

    show son sta exp exp with std_change

    voice get_voice_filename("son")
    sonya "「呪文！　それは面白そうでありますね！　ひとつお願いするであります！」"

    "ソーニャが言ったとき、店内がざわつくのを感じた。"

    show mhr mai sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「待ってくれ」"

    show mhr mai sco sh2 with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火。そのメニューはいささかぼくのキャラクターとは違っていてね。できることなら、断りたいところなんだ」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、そうなんだ。ま、そうだよね」"

    show mhr mai sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「ああ。このパンケーキ自体は特別美味しいものではない。5,000円の価値は毛頭ない。どこに付加価値があるか、想像はついていると思う」"

    show mhr mai sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「このメニューはまさに客単価を上げようとする店長の策略だ。経営の清浄化のために、凛火にはこの悪徳商法に加担しないで欲しいところだね」"

    show son sta que tro with std_change

    voice get_voice_filename("son")
    sonya "「ソーニャ、食べられないでありますか？」"

    show mhr mai sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「残念だけれどね。あるいは、ぼくではない他のスタッフを呼べばいい」"


    hide mhr
    hide son
    hide rnk
    with std_out

    "その時、海晴は店長に呼ばれた。どうやら、私たちのやり取りを店長も見ていたらしい。"


    play music audio.kinpaku
    scene ecg miharumaid dis with dissolve_long

    "しばらくして戻って来た海晴の表情は、怒りと絶望が混ざったよく分からないものになっていた。"

    "海晴はパンケーキを机の上に置き、チョコペンで器用に絵を描いた。"

    "ソーニャの持っているぬいぐるみがモチーフのようだ。"


    scene bg maidcafe
    show son sta exp exp at std_c
    with dissolve_long


    voice get_voice_filename("son")
    sonya "「素晴らしいであります！　ほらパサジールあなたでありますよ！」"

    show son sta que que with std_change

    voice get_voice_filename("son")
    sonya "「呪文はこの後、かけてくれるのでありますか？」"

    scene ecg miharumaid dis large at align(0.6, 0.05) with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「凛火の前で……これを……やらなくてはならないというのだね……。悪いがぼくは君を一生恨むよ……」"

    "海晴はソーニャを睨みながらそう言った。年下の少女に向ける表情ではなかった。"

    "そして、真剣な顔で私の方へ向き直る。"

    scene ecg miharumaid nor with dissolve


    voice get_voice_filename("mhr")
    miharu "「いいかい？　ぼくが今からやるのはあくまで仕事だよ。だから凛火も店を出たら見なかったことにして欲しい」"

    "海晴の顔は相当強張っている。"

    "そこまで言われると、こちらの方が身構えてしまう。どんなものか想像できるだけに、見る前から恥ずかしくなってしまった。"

    "海晴は小さく息を吸って、右手の人差し指を立てて構えた。"


    stop music fadeout 1
    show ecg miharumaid mag with ecg_change




    voice get_voice_filename("mhr")
    miharu "「おいしくなぁれ♡」"

    "指を宙で数回回してから、両手でハートの形を作り、そのまま♡を突き出す。"

    play music audio.maidcafe


    voice get_voice_filename("son")
    sonya "「日本の魔法少女を見ることができたであります！」"

    "ソーニャは海晴の笑顔の裏に隠されている感情に気が付いていないのだろう。"

    "珍しいものが見られたことをとても喜んでいた。"

    "海晴はポーズを取ったまま、停止している。"

    "ソーニャの方だけを見て私と目を合わせようとはしなかった。"


    voice get_voice_filename("rnk")
    rinka "「か、可愛かったよ……」"

    show ecg miharumaid shy with ecg_change


    voice get_voice_filename("mhr")
    miharu "「くっ……屈辱だ……」"


    scene bg maidcafe with dissolve_long

    "私も目を合わせずに言うと、海晴は顔を伏せてバックヤードへ戻って行ってしまった。"

    show son sta que que at std_cr with std_in

    voice get_voice_filename("son")
    sonya "「オネエサマ、どうしましたか？　顔が赤いですね」"

    show rnk uni arm sad rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「なんだろ。私がもっと必死で止めてあげればよかったのかな……罪悪感……」"


    scene bg maidcafe with fade_long
    pause 1



    "パンケーキを食べ終えてしばらくしてから、お会計を済ませた。"

    "ちなみにお会計はソーニャが持っていたクレジットカードで支払った。それを分かっていたからこそ、パンケーキの注文は止めなかったのだ。"

    "私たちが店を出ようとしたとき、海晴が戻って来た。メイド服から制服に着替えている。"

    "どうやらシフトを早めに切り上げてもらったらしい。理由は……聞かないことにした。"

    show son sta exp exp at std_r with std_in

    voice get_voice_filename("son")
    sonya "「ソーニャ、アキハバラの街並みも見てみたいです！」"

    show rnk uni arm nor rev at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「そっか。行きたいって言ってたもんね。でも、私よく知らないけど」"


    show mhr uni nor nor rev behind rnk at std_l with std_in
    voice get_voice_filename("mhr")
    miharu "「構わない。ぼくも付き添おう。それでいいだろう凛火？」"

    "確かに、秋葉原に通勤している海晴に案内してもらえれば安心だ。"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それに、ぼくは君を完全に信用したわけではないからね。迂闊に二人きりにはさせられない」"

    "海晴の口調は強かったが、私は諌めることはしない。"

    "ソーニャを信用したとはいえ、自分がやっていることがどういうリスクがあるのか分かってはいるからだ。"

    show son sta nor lau with std_change

    voice get_voice_filename("son")
    sonya "「ミハルが案内してくれるのでありますか？　ソーニャ、たくさん見たいものがあります！」"

    "当のソーニャは、私たちの懸念など気にも留めていないようだった。"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……あどけないね。本当に」"

    "そして、私たちはメイド喫茶を後にした。"




    python:
        set_info_time("night")
        set_info_location("02")

    stop music fadeout 1
    scene bg station01 with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()



    "帰宅ラッシュの時間であり、新宿駅のホームは混雑していた。"

    "秋葉原から総武線で新宿まで来た３人は、乗り換えのために一旦ホームへ出ていた。"

    show mhr uni pai lie at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「まさかあれほどに付き合わされるとは思わなかったね」"

    show son sta nor la1 rev at std_l with std_in

    voice get_voice_filename("son")
    sonya "「ソーニャ、ほくほくです！」"

    show rnk uni arm sad at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「はは、ははは……」"

    hide son
    hide rnk
    hide mhr
    with std_out

    "秋葉原の観光を終える頃にはもうへとへとになってしまっていた。"

    "秋葉原はこの前直未と海晴のバイト先へ行ったとき以外には、乗り換えでしか使ったことがなく、どんな様子なのかほとんど知らなかった。"

    "歩いてみれば、電気製品のお店もアニメ関連のお店もとにかくたくさんあったのだ。"

    "ソーニャは通りがかって何か気になるものがあるとすぐに立ち止まったり店の中に入ったりするので、終始振り回されっぱなしだった。"

    show son sta nor tro rev at std_l with std_in

    voice get_voice_filename("son")
    sonya "「オネエサマ！　せっかく日本にいるのに、素晴らしいアニメ文化を知らな過ぎであります！」"

    show rnk uni arm sad at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「子供の頃にはそれなりに見てたんだけど、随分たくさんあるよね。アニメじゃなくて漫画だったら、もう少し分かったんだけど……それでもソーニャたち程ではないかな」"

    show son sta nor nor rev with std_change

    voice get_voice_filename("son")
    sonya "「ミハルを見習ってください！」"

    show mhr uni sco con at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「……ぼくはバイトの関係上、積極的に勉強するようにしているからね。愛嬌を振りまくにも、話を合わせる必要がある」"

    "言われてみれば、私は最近はアニメをほとんど見ていない。"

    "元々お店の手伝いも多かったし、一人で店を開けるようになってからはさらに忙しくなってしまった。"

    show mhr uni sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「さっきも言っていたけれど、凛火は少女漫画を読んでいたよね」"

    show rnk uni nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そうだね。真央からよく借りてたし」"

    show son sta nor sur rev with std_change

    voice get_voice_filename("son")
    sonya "「オネエサマは恐く見えますが、乙女ちっくなのでありますね！」"

    show mhr uni sco sh1 with std_change

    voice get_voice_filename("mhr")
    miharu "「……そこがいいのだけれどね」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、恐く見えるってとこを否定して欲しいんだけど」"

    hide rnk
    hide son
    hide mhr
    with std_out

    "地下鉄に乗り換えようと歩いているところで、海晴がついて来ていることに疑問を持った。"

    "海晴の家は、秋葉原から反対方面へ行った方が近いからだ。"

    "そのことを尋ねると、海晴は微笑してから続けた。"

    show mhr uni nor rea at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「ぼくも君の家に泊まるからさ」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「君とソフィアを二人きりにするのはまだ、危険だと思っているからね」"

    show rnk uni arm ama rev at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……え？　だって明日平日だよ」"

    show mhr uni sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「構わないよ。明日の早朝に一度戻って、準備をすればいい。ぼくはソフィアが凛火の寝首をかかないか見届けられればいいからね」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと、そんな言い方……」"

    show son sta que que rev at std_l with std_in

    voice get_voice_filename("son")
    sonya "「かく？　オネエサマ、かゆいですか？」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「さすがの君もその言葉は知らないか。まあいい。言ったろう？　ぼくは君のことをまだ信用していない」"

    show son sta nor sad rev with std_change

    voice get_voice_filename("son")
    sonya "「……しょぼんであります」"

    "ソーニャは寂しそうな顔を浮かべると、すぐにまたぱあっと明るい表情に変わった。"

    show son sta ban exp rev with std_change

    voice get_voice_filename("son")
    sonya "「でもそのおかげで、一杯楽しいところに行けたであります！」"

    show mhr uni sco wic with std_change

    voice get_voice_filename("mhr")
    miharu "「明日も観光するのだろう？　ぼくもついて行く。明日も泊まらせてもらう。心配しなくても、観光している間は純粋に楽しめるように努力するよ……いいね？」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私はいいけど……海晴の家の人、大丈夫なの？」"

    show mhr uni nor ser with std_change_wait

    "海晴は少し躊躇ってから、頷いた。"

    "その後、私たちは翌日どこへ行こうかなど話しながら帰宅をした。"

    "帰路についている間、海晴はソーニャに敵意を向けこそしなかったが、どこか微妙な空気が流れていた。"







    python:
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    show son sta exp exp at std_r with std_in

    voice get_voice_filename("son")
    sonya "「ミハルのハンバーグ、とっても美味しかったであります！」"

    "自室に上がって来て、ソーニャはあらためてそう言った。"

    "ライオン館へ戻る前に、海晴はご飯を作ると提案してくれたのだ。"

    show rnk uni nor smi rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「うん。とっても美味しかった。話には聞いてたけど、予想以上に料理上手って感じだったな。ごちそうさま」"

    show mhr uni sco sh2 at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「大したことはないさ。毎日料理をしていると、それなりにうまくなるものさ」"

    show mhr uni sco sh1 with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火はぼくの手料理を食べたことがなかっただろう？　いい機会だと思ってね。明日は君の手料理を食べたいな」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「いいけど……あんまり期待しないでね」"

    "一応、私も毎日料理はしているのだけど。"

    "もっともお惣菜を買ってきて付け合わせだけ作るという日も多いし、そもそも簡単なメニューしか作らないのであまり上達しないのかもしれない。"

    "店で出す軽食は、おばあちゃんのレシピがあるから作れるのだし。"

    "その後、順番にお風呂に入り、テレビを見たりおしゃべりしたりと、夜のまったりとした時間を過ごした。"

    $ set_info_time("lnight")

    stop music fadeout 1
    scene black with dissolve
    pause 2

    $ show_hud()




    voice get_voice_filename("rnk")
    rinka "「んん……」"

    "今は、何時だろうか。"

    "少なくともまだ朝ではないことは分かるが、目が覚めてしまった。"



    play music audio.myroom_night
    scene bg myroom night with dissolve


    voice get_voice_filename("rnk")
    rinka "「あれ……？」"

    "違和感があった。"

    "その正体にすぐに気が付く。"

    "隣に寝ていた海晴も、ベッドで寝ていたソーニャもいない。"

    "疑問に思っていると、下からかすかに声が聞こえてきた。"

    "私は嫌な予感がして、そのままの格好で下の階へ向かった。"





    $ set_info_location("04")

    scene bg lion01 night with dissolve

    "階段の途中で、私は一度足を止めた。"

    "聞こえてくる海晴の声が、とても真剣なものだったからだ。"

    "わざわざ一階に来て話すのは、私に聞かれたくないということだ。話しているのを知られたくないということでもある。"

    "だが盗み聞きはよくないと分かっていても、自分の部屋まで引き返すことはできなかった。"


    play music audio.investigation

    show mhr uni nor ser rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「………………っているね」"

    show son paj nor nor at std_c with std_in

    voice get_voice_filename("son")
    sonya "「……ハイ」"

    "声がはっきり聞こえてきたのは、海晴が話題を変えた時であった。"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「やはり……おかしいね」"

    show son paj que que with std_change

    voice get_voice_filename("son")
    sonya "「何が……でありますか？」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火が君の前でぼくの名前を呼ぶ前から、君はぼくの名前を呼んでいた。知っていた」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「結論から聞くよ。君は……ぼくの氏名のカードを持っているね？」"

    show son paj nor sad with std_change

    voice get_voice_filename("son")
    sonya "「……すみません」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「どうして謝る？」"

    show son paj nor smi with std_change

    voice get_voice_filename("son")
    sonya "「あなたのカードを持っていたのに、黙っていたからであります」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……調子が狂うな」"

    "海晴はため息をつき、額のところを押さえる。"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「分かった、もういい。だがこれだけは覚えていて欲しい。ぼくは、未島海晴さ」"

    show son paj nor nor with std_change

    voice get_voice_filename("son")
    sonya "「ハイ。ミハルはミハル、でありますね」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……面白いな、君は」"

    "海晴の氏名のカード。"

    "フルネームを知っているはずの私が持っていないカードでもあった。そのことが示すのは、海晴の本当の名前は違っているということだ。"

    "だが、海晴の家庭環境を思えば、不思議なことではない。だからこそ――私はずっと聞くことができなかったのだ。"

    show mhr uni sco sh1 rev with std_change

    voice get_voice_filename("mhr")
    miharu "「聞いているね、凛火」"

    show rnk paj sur su1 at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「んぐっ」"

    show son paj nor sur rev with std_change

    voice get_voice_filename("son")
    sonya "「オネエサマ！」"

    "急に声をかけられて、私は口を塞ぐ。物音を立ててしまうので逆効果だと分かっていたはずだけれど。"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくが君の息遣いに気付かないはずないだろう？」"

    show rnk paj nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「……ごめん」"

    show mhr uni pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは今日、謝られてばかりだね。まあいい。どこから話を聞いていたかは知らないけれど、忘れてくれ」"

    show mhr uni sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ソフィアも深夜に起こして悪かったね。上へ戻ろう。眠れるだけ眠っておいた方がいい」"

    show rnk paj arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、そうだね」"

    "聞いていたことがばれてしまった以上、海晴とちゃんと話をしたかったが、大きくあくびをしたソーニャを見て、私たちは部屋へ戻ることに決めた。"

    "結局、海晴の氏名のカードについては、はぐらかされてしまったままで。"



    python:
        set_info_scene("44")
        set_info_date(5, 25, "fri")
        set_info_time("noon")
        set_info_location("14")






    stop music fadeout 2
    scene bg schoolgate noon with fade_longest
    play music audio.nichijo02
    pause 1

    $ show_hud()



    "一夜明け、あっという間に授業が終わった。"

    "放課後、私たちは３人で校門にいた。"

    "ソーニャがまた高校について来ても困るし、土曜日は午前授業で短いという事情もあるので、今日は大学の方を散歩してもらうことにした。"

    "キャンパス内は開放されているし、図書館もある。大学生の何人かを驚かせてしまうかもしれないが、まあそれは仕方がない。"

    "しかし合流したソーニャを見て、私は自分の行動が失敗だと悟った。"

    show son sta nor smi at std_r with std_in

    voice get_voice_filename("son")
    sonya "「ダイガク、楽しそうなところでありました」"

    show rnk uni arm sad rev at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「ソーニャ……」"

    "その一言が、ぐさりと突き刺さる。"

    "だってソーニャは、大学に通うことはできないのだ。もし選定を生き残ったとしても、病気が治るわけではない。"

    "その予想が正しいか正しくないかは分からないけれど、少なくとも彼女は正しいと思い込んでいる。"

    show mhr uni nor ser rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「凛火が気にすることではないよ。だろう、ソフィア？」"

    show son sta ban lau with std_change

    voice get_voice_filename("son")
    sonya "「ハイ！　ソーニャの知らないこと、知るのはとても楽しいです！」"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「さあ、では行こうか。今日は本格的に観光するのだろう？」"

    show son sta nor la1 with std_change

    voice get_voice_filename("son")
    sonya "「東京の街並み、楽しみでありますよ！」"

    "海晴とソーニャの二人は見る限りでは険悪さはなかった。"

    "昨日は昨日、今日は今日と割り切っているのだろうか。"

    "海晴の言う通り、今日は観光地を見てみるのだ。"

    "私たちは駅に向かって歩き出した。"







    python:
        set_info_time("night")
        set_info_location("22")

    stop music fadeout 1
    scene bg zojoji night large with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()



    "簡単には語りつくせないくらい、色々なところを見て回った。"

    "まずはスカイツリーを見て展望台に上り、次は浅草寺。仲見世通りの大混雑を抜け、雷門も見た。"

    "六本木ヒルズも遠くから見たし、ああ、その前はアニメの舞台になったとかで神保町の古書店街も歩いたんだった。"

    "街と街の間の移動には、さすがにタクシーを使った。ソーニャの両親はお金持ちらしく、メイド喫茶と同じようにクレジットカードで支払ってもらった。"

    "ここに来る直前はお台場のフジテレビと観覧車を車内から見るだけでＵターンして来たくらいのハードスケジュールだった。"

    "最後の行程は、ここ増上寺だ。"

    "仏教の浄土宗のお寺で、江戸時代の将軍である徳川家とも縁がある由緒正しいお寺だとかなんとか……。"

    "一方で日本のアーティストが境内でライブを行ったりと、オープンなところもあるらしい。"

    "入り口の大きな門は、地名の由来にもなったくらいだから、とても立派なものだった。"

    "電車でも30分圏内の場所だけれど、こんなところがあるなんて全然知らなかった。"

    show rnk uni nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「もう、くたくた……」"

    show mhr uni sco con rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「凛火もぼくも立ち仕事をしているはずだけれど、さすがにハードな行程だったね」"

    hide rnk
    hide mhr
    with std_out

    "疲れを労い合っている私たちをよそに、ソーニャはとととっと前を歩いて行った。"


    play music audio.amusementpark_night

    show son sta nor la1 at std_c with std_in

    voice get_voice_filename("son")
    sonya "「スゴイ、であります！」"

    "そしてソーニャは、遠くに見える東京タワーを指さして言った。"

    "お寺越しに、イルミネーションで飾られた東京タワーがよく見えた。真っ赤な塔を中心に白や青、黄色や緑に光り輝いている。"

    "東京タワーはもちろん知っていたが、こんなに近くから、それも夜に見ると記憶の中の姿と全く異なっていた。"

    show rnk uni nor smi at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「綺麗だ……」"

    show mhr uni nor rea rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「ああ、そうだね……」"

    show son sta nor nor rev with std_change

    voice get_voice_filename("son")
    sonya "「東京、素晴らしいであります！」"

    "そしてしばらく、三人は夜景の中に煌々と光る赤い塔に見惚れていた。"

    "私は、海晴と一緒に見た遊園地のイルミネーションを思い出していた。"

    "あの時はまだ、女神の選定のことなんて考えもしていなかった。"

    "こんな状況になるなんて、思いもしなかった。"

    "もしかしたらソーニャも、今日までの日々を同じように思い返しているのかもしれない。"

    "東京タワーを見上げるソーニャの横顔は紅潮して、切なげだった。"

    scene ecg sophiatear lau with dissolve_long


    voice get_voice_filename("son")
    sonya "「こうして綺麗なものを見ることができて、ソーニャはとっても幸せです」"

    show ecg sophiatear pai with ecg_change


    voice get_voice_filename("son")
    sonya "「幸せ過ぎて、寂しいであります」"

    "ソーニャの大きな瞳が、光を反射して震えていた。"

    "彼女は、さらに上を向いた。それでも、ソーニャが瞳に蓄えた涙は留まらず、頬を伝ってこぼれ落ちた。"


    voice get_voice_filename("son")
    sonya "「きっとこの瞬間が、ソーニャにとって一番幸せなのであります」"

    show ecg sophiatear cry with ecg_change


    voice get_voice_filename("son")
    sonya "「最初で、最期の……」"


    voice get_voice_filename("son")
    sonya "「ソーニャの見た、ソーニャが感じた、広い世界――」"


    play music audio.growapart

    "一度溢れると、涙は止まらない。"

    "その気持ちは、よく分かる。"

    "ソーニャはもう、笑顔を保ててはいなかった。くしゃくしゃになった顔で、嗚咽をした。"

    show ecg sophiatear pai with ecg_change


    voice get_voice_filename("son")
    sonya "「もう……おしまいなのであります……」"

    show ecg sophiatear cla with ecg_change


    voice get_voice_filename("son")
    sonya "「うぐっ……これでっ……今日でっ……うぐっ」"


    voice get_voice_filename("son")
    sonya "「うわああああああああんっっ」"

    "溢れた感情を受け止めて、私まで目頭が熱くなる。だが、必死に堪えた。それは、我慢した。"

    "ソーニャを抱き締めようと手を差し出すと、海晴が私を見て首を振った。"



    scene bg zojoji night
    show mhr uni nor ser rev at std_l
    with dissolve_long


    voice get_voice_filename("mhr")
    miharu "「感情移入し過ぎてはいけないよ」"

    "私にだけ聞こえる声で、そう言った。"

    "だが私は止まれなかった。一緒に泣くことが許されないならせめて、ここに私がいることを伝えたかった。"

    "そうしてあげないと、彼女の小さな体が崩れ落ちてしまいそうだから。"

    show rnk uni arm nor rev at std_c with std_change

    voice get_voice_filename("rnk")
    rinka "「ソーニャ……」"

    scene ecg sophiatear cla with dissolve_long


    voice get_voice_filename("son")
    sonya "「うわああああんっ、オネエサマ！　パパ！　ママぁっ！」"


    voice get_voice_filename("son")
    sonya "「ソーニャは、辛いであります。今なら、分かるでありますっ」"


    voice get_voice_filename("son")
    sonya "「世界には、こんなに、こんなに美しいものがあるのに……」"


    voice get_voice_filename("son")
    sonya "「もう、お別れしないといけないなんて……」"


    voice get_voice_filename("son")
    sonya "「ひぐっ……うわあああっ。」"

    "時間は、ゆっくりと過ぎて行く。"

    "こぼれる涙は、真っ赤に燃える光を浴びて輝いていた。"



    voice get_voice_filename("mhr")
    miharu "「凛火、君は……」"



    scene bg zojoji night with dissolve_long

    "海晴は言いかけて、そこで言葉を止めた。"

    "ソーニャが落ち着くのを待って、私たちはライオン館へ帰って行く。"







    $ set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()



    "私たちがライオン館へ戻って来たのは、午後９時頃であった。"

    "これから買い物をしてご飯を作り始めるとさらに遅くなってしまうので、宅配のピザを頼んでいた。"

    "もふもふ、と三人でピザを食べる。"

    scene ecg nighttalkC2 smi nor with dissolve_long


    voice get_voice_filename("son")
    sonya "「美味しいであります！　日本の食事は最高なのであります！」"

    scene ecg nighttalkA3 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「いや、宅配ピザこそロシアにもあるでしょ」"

    scene ecg nighttalkC2 nor nor with dissolve


    voice get_voice_filename("son")
    sonya "「ソーニャは、食べられるものが少なかったでありますよ。何も気にせず自由に食事できることはとても、幸せであります！」"

    "ソーニャは明るく言うが、単純な一言に重みがあった。"

    "だが、重くなりそうな空気は海晴ががらりと変える。"

    show ecg nighttalkC2 nor tro with ecg_change


    voice get_voice_filename("mhr")
    miharu "「……凛火の手料理を食べられないのは、残念だ」"


    voice get_voice_filename("rnk")
    rinka "「まあ、もう時間的にね。宅配ピザって、子供の頃以来かも」"

    show ecg nighttalkC2 nor nor with ecg_change


    voice get_voice_filename("mhr")
    miharu "「おばあ様と二人暮らしだと、特に頼む機会は少ないかもしれないね」"

    scene ecg nighttalkA3 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「うん。あんまりデリバリーするって習慣もないみたい。お蕎麦くらいかな。ピザ自体は店でも作ってたから、好きだと思うんだけど」"

    show ecg nighttalkA3 smi with ecg_change


    voice get_voice_filename("rnk")
    rinka "「そもそもおばあちゃん、好き嫌いないからね。何でも食べるのが健康の秘訣っていうのが、おばあちゃんの口癖だったから」"

    "事実、私のおばあちゃんは年齢の割にもの凄く健康だ。特に、未だ全て自前の歯であることをよく自慢していた。"

    scene ecg nighttalkC2 que smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「凛火の好き嫌いがないのも、おばあ様の影響なんだね」"


    voice get_voice_filename("rnk")
    rinka "「あはは、それは間違いないかも」"

    show ecg nighttalkC2 smi smi with ecg_change


    voice get_voice_filename("son")
    sonya "「オネエサマのオバアサマ、でありますか……きっと、素敵な人でありますね！」"

    show ecg nighttalkC2 smi nor with ecg_change


    voice get_voice_filename("mhr")
    miharu "「くすっ、よく分かっているね。凛火を育てたのだから、当たり前さ」"

    "と語る海晴は、私のおばあちゃんにまだ会ったことがないはずだ。"

    show ecg nighttalkC2 nor nor with ecg_change

    "ご飯を食べながら、私たちはまた色んな話をした。"

    "ソーニャの家族の話が多かった。ソーニャのおばあちゃんはとても優しい人で、裁縫が得意だそうだ。"

    scene ecg pasajiru nor with dissolve

    "お気に入りのぬいぐるみも、おばあちゃんが作ってくれたらしい。"


    voice get_voice_filename("son")
    sonya "「ソーニャ、家で友達がいなかったですから。本を読むときもアニメを見ているときも独りぼっちにならないように、パサジールをプレゼントしてくれたであります」"


    voice get_voice_filename("son")
    sonya "「……今日はパサジールも広い世界を見ることができて、きっと喜んでいたであります」"

    scene ecg nighttalkC2 que nor with dissolve

    "しんみりとした空気を吸い込むように、ソーニャは大きなあくびをした。"

    show ecg nighttalkC2 nor nor with ecg_change


    voice get_voice_filename("son")
    sonya "「お腹いっぱいになったら、眠くなってしまいました」"


    voice get_voice_filename("rnk")
    rinka "「今日はたくさん歩いたからね。ゆっくり……休みな？」"

    show ecg nighttalkC2 ele nor with ecg_change


    voice get_voice_filename("son")
    sonya "「ハイ！　オヤスミナサイであります！」"



    scene bg lion01 night with dissolve_long

    "言うと、ソーニャは２階へ上がって行った。"

    "１階は、海晴と私の二人になった。"

    "片づけをしているところに話を切り出したのは、海晴だった。"


    play music audio.investigation

    show mhr uni nor ser at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「ソフィアに尾行らしき影もなかった。Ⅺは相当な自信家で、酔狂な人のようだ」"

    "海晴が一日中気を張っていたのは分かっていた。私もソーニャと最初に街を歩いたとき、同じように注意していたから。"

    "普通に考えて彼女たちが二人組なら、一人が両親を見張り、一人がソーニャを見張るのが得策だろう。"

    "Ⅲの男性――フェデリーコ・カルミナーティという名前は、私がカードを持っているので分かっている――が両親を、自分の情報を知られているⅪの女性がソーニャを、だ。"

    show rnk uni nor nor rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「ソーニャのカードを３枚持っているから、自信があるっていうのは納得できる。でもどうして、酔狂って思うの？」"

    show mhr uni sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくの予想では、Ⅺはただソフィアに楽しんで欲しかっただけだと思うんだ」"

    show mhr uni sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「いいかい？　両親と協力して情報を調べることを徹底するなら、最終日だって一緒にいさせてはいけない。これは当たり前だね」"

    show mhr uni sco sh1 with std_change

    voice get_voice_filename("mhr")
    miharu "「でも、最期の時は家族と過ごすことを許した。慈悲――とそう思われるけれど、ぼくは違うと予想している」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「枷は、ソフィアではなく彼女の両親にかけられたんだ」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「どういう……意味？」"

    show mhr uni sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「ソフィアの両親は選定を心から信じているかどうか分からない。娘が一時的によくなっているだけだと僅かでも思っているなら、病気のソフィアを日本滞在中も気にかけ続けるに決まっている」"

    show mhr uni nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「それこそ、こんな脂っこいピザなんて食べさせないさ……おっと、ぼくが嫌いなわけではないけどね。客観的に見ての話さ」"

    show mhr uni sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「ソフィアが知らない世界を見るというのは、両親といては為し得ないことだと思う――ここまで言えば分かるかい？」"

    "ソーニャが口にしていた、自由という言葉を思い出した。"

    "そこから考えれば、普段は不自由を感じていたということになる。"

    show rnk uni arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「結果的に、ソーニャは私たちと違って広い世界を見ることができた……かもしれない」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「もちろんⅪにとってソフィアとぼくたちが出会うのは予想外だっただろう。だが、今まで話したことから考えて、Ⅺはソフィアの未練を叶えさせたかったと本気で思っていたように予想できる」"

    show mhr uni sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「たった２日や３日では未練が完全になくなりはしないだろうが、それでも、両親との観光では今夜見せたソフィアの涙は意味が違っていたかもしれない」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「――納得できる。正しいかどうか分からないけど、ソーニャは心から感動していたと思う」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「そして、これらの情報はⅪのパーソナルを知るために重要な情報になってくるかもしれない――おっと、ぼくが結論として言いたいのはここではないね」"

    show mhr uni sco vig with std_change

    voice get_voice_filename("mhr")
    miharu "「これからこの選定を、あらためてぼくと一緒に戦わないかい？」"

    "海晴は私の目を真っ直ぐに見つめて、そう告げた。"

    "今まで口にしてこなかったその言葉を、海晴はついに言い放った。"

    "私は海晴と目を合わせたまま黙る。"

    "思考停止していたのだ。"

    "どう答えればいいのか、分からなくて。"

    "海晴の呼吸が聞こえる。"

    "徐々にその音に緊張が高まっていくのを感じて、私は答えた。"

    show rnk uni nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……駄目だよ。だって海晴は私を最後の一人にするためにって言うでしょ？」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「凛火を最後の一人にするのは、ぼくのためでもあるけれどね」"

    show rnk uni arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「同じだよ。それじゃ、違う。私も海晴を最後の一人にするためにって思わなきゃ、平等じゃないよ」"

    show rnk uni sur scr rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私はまだ、どっちが生き残ればいいのかなんて分からない！」"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴は親友だ。それは間違いないよ。死なれるのは絶対に嫌だ。でもね……私も自分の未練をちゃんと知るまでは、自分がどうして生きているのかって知るまでは、死にたくないんだ……」"

    show rnk uni arm ten rev with std_change

    voice get_voice_filename("rnk")
    rinka "「迷いがある限り……一緒に行動しても足を引っ張ることになる」"

    "スコーピオンさんと向き合ったときのような、緊迫した事態は再び来るはずだ。"

    "その時に、決心が鈍ってしまう。"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「君の……未練……か」"

    "それだけ言うと、今度は海晴の方が黙ってしまう。"

    "海晴の表情から、葛藤しているのがすごく伝わってくる。"

    "そして顔を綻ばせ、続ける。"

    show mhr uni pai lie with std_change

    voice get_voice_filename("mhr")
    miharu "「君はあるいは、ぼくの死因に心当たりがあるはずなのにね。確信を持ったら軽蔑するはずだろうに」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「けれども――分かった。今はまだそれでいい。だが、ぼくのスタンスは変わらない。ぼくの運命はきっと、君のためにあるのだから。迷いがなくなる時を心待ちにしているよ」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴はどうして、そこまで私を生かそうとしてくれるの？　海晴にだって未練は……あるはずなのに。自分のカードをちゃんと、持っているでしょ？」"


    play music audio.miharu

    show mhr uni sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「君を愛しているからさ」"

    show rnk uni arm imp rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、あいっ？」"

    "動揺してしまったが、それは家族愛だとかの愛であろう。"

    show mhr uni nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「さて、ぼくたちももう寝よう。明日、ソフィアを見送るのだろう？」"

    show rnk uni arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「う、うん……そうだね……」"

    "海晴の性格からして、思わせ振りなことを言う時は裏にも何か考えているだろうから。"

    "言葉通りの意味ではないと分かっているはずなのに、慌ててしまい恥ずかしかった。"

    "そして、万が一があった場合。"

    "私はその言葉の受け止め方を知らないから、余計に恥ずかしいのだろう。"







    python:
        set_info_time("lnight")
        set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()



    "部屋に戻ってからも、私は中々寝ることができなかった。"

    "色々考えてしまったからだ。"

    "その中でも特に、私が海晴の死因に心当たりがあるという一節が気になる。"

    "否定しなかった理由は、自分でも察しがついていた。"

    "真剣に考えることから逃げていただけで、カード化された親友の死因なんて見たくないだけで、本当は――。"

    "でも、これだけは言える。"

    show rnk paj arm nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「軽蔑なんて、するわけないだろ」"

    "海晴はもうぐっすり眠っているようで、小さく寝息を立てている。寝顔も美人なのってすごいな、とふと思った。"

    "まくれた袖から、手首の傷痕が覗く。"

    $ add_seen_chapter("4-4")



    python:
        set_info_scene("45")
        set_info_date(5, 27, "sun")
        set_info_time("morning")
        set_info_location("04")







    stop music fadeout 1
    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()



    "朝になって、私は二人にコーヒーを淹れた。"

    "ソーニャはブラックでは飲めないと言うので、お砂糖とミルクをたっぷり入れて。"

    scene ecg girlstalkX1 smi nor with dissolve_long


    voice get_voice_filename("son")
    sonya "「初めて飲んだであります。美味しかったです、とても」"

    show ecg girlstalkX1 smi smi with ecg_change


    voice get_voice_filename("mhr")
    miharu "「……久しぶりにここでコーヒーをいただいたね。前とは少し味が変わっている」"

    scene ecg girlstalkH2 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「前の時に淹れたのは、おばあちゃんだったから。ちょっと味は落ちちゃったかな」"

    scene ecg girlstalkX1 nor smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「そんなことはない。ぼくは変わったと言ったんだ。この香りが、きっと凛火のコーヒーなんだ」"

    "私の、コーヒー。確かに私は自分なりに少しずつ方法を変えたりしている。"

    "だが、そんなことはどうでもよかった。"

    show ecg girlstalkX1 nor nor with ecg_change

    "朝日を浴びてコーヒーを飲む海晴の表情に、つい見惚れてしまっていた。すぐに昨日のことを思い出して顔を逸らすけれど。"

    "ソーニャも海晴のことを見つめていた。"

    "私の視線に気付いたのか、ソーニャは微笑んで口を開いた。"



    play music audio.commit

    show ecg girlstalkX1 sm2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「オネエサマとミハルに、ソーニャからお願いであります」"

    show ecg girlstalkX1 ser nor with ecg_change


    voice get_voice_filename("son")
    sonya "「パサジールを、預かってください」"

    scene ecg girlstalkH2 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「えっ……？　だっておばあちゃんからもらった大切なものなんでしょ？」"

    scene ecg girlstalkX1 ser smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「パサジール……ロシア語で旅人という意味だね」"

    show ecg girlstalkX1 tro smi with ecg_change


    voice get_voice_filename("son")
    sonya "「オドロキマシタ。海晴はソーニャの国の言葉を知っていたのですか」"

    scene ecg girlstalkH2 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「ソーニャの想いが――希望が名前にこもってたんだね」"

    "桂子さんの言葉を思い出し、少しだけ切なくなった。悟られないように、私は微笑む。"

    scene ecg girlstalkX1 nor nor with dissolve


    voice get_voice_filename("mhr")
    miharu "「それで、お願いというのは？」"

    show ecg girlstalkX1 smi nor with ecg_change


    voice get_voice_filename("son")
    sonya "「この子に、もっと世界を見せてあげて欲しいであります。ソーニャの代わりに、この子に」"

    "言って、ソーニャは満面の笑顔でぬいぐるみを海晴に差し出した。"

    show ecg girlstalkX1 smi tro with ecg_change


    voice get_voice_filename("mhr")
    miharu "「ぼくに渡しても意味がない。だって……」"

    show ecg girlstalkX1 nor tro with ecg_change


    voice get_voice_filename("son")
    sonya "「ソーニャのお願いは、二人へのお願いであります」"

    scene ecg pasajiru pai with dissolve

    "ソーニャはぬいぐるみを海晴のいるテーブルの上に置くと、そのまま話を続けた。"

    "海晴は、右手の指先でパサジールを撫でた。無意識の行動だったのだろう、自分がぬいぐるみを撫でていることに気付くとすぐに手を引っ込めた。"


    voice get_voice_filename("son")
    sonya "「ちょっとだけ、ソーニャの話を聞いてくださいであります」"


    voice get_voice_filename("son")
    sonya "「女神の選定は、12人がハジマリから12週間後、選定の最後の時に本来同じ場所にいるはずだったと言っていました」"


    voice get_voice_filename("son")
    sonya "「実は、ソーニャの病気が悪くならなければ、旅行が決まっていたのであります」"


    voice get_voice_filename("son")
    sonya "「行く場所はパパとママが決めることになっていたでありますが、日本――東京ということだけは決まっていたのであります」"


    voice get_voice_filename("mhr")
    miharu "「しかし運命は変わった。ソフィアの病気は悪化した。だが……そうか、君たち家族が東京に来る運命もあったというわけだね」"


    voice get_voice_filename("son")
    sonya "「ハイ。運命は≪変わった≫であります。ソーニャは旅行の前に、死んでしまいました」"


    voice get_voice_filename("son")
    sonya "「ソーニャが言いたかったのは、運命は変わるってことであります。悪いように変わるなら、きっといいようにも！」"


    voice get_voice_filename("son")
    sonya "「女神様が言うには、12人のうちの１人しか生き残れないのが運命とのことであります。でも、運命がそんなにころころ変わるものであれば……」"


    voice get_voice_filename("son")
    sonya "「オネエサマもミハルも、ずっと生きることのできる運命もあるかもしれないであります」"


    voice get_voice_filename("son")
    sonya "「ソーニャはもう、間に合わないであります。でも、オネエサマとミハルなら、パサジールにもっと広い世界を見せてあげられるかもしれないであります」"

    scene ecg girlstalkH2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「運命が変わる……可能性……？」"

    scene ecg girlstalkX1 nor nor with dissolve


    voice get_voice_filename("mhr")
    miharu "「あり得ないよ。変わったとしてそれは、生き残る者が変わるだけ。ぼくがいる限り、それが凛火であることに変わりはないけれど」"


    voice get_voice_filename("mhr")
    miharu "「ぼくらが今生きているのは、女神の決めたルールがあるからだろう？」"

    show ecg girlstalkX1 ser nor with ecg_change


    voice get_voice_filename("son")
    sonya "「ハイ。ですがソーニャは、二人にお願いをするであります」"

    "海晴の言葉を否定するかのように、ソーニャは強い口調で言う。"

    "疑いのない、透き通った瞳で。"

    show ecg girlstalkX1 ser smi with ecg_change


    voice get_voice_filename("mhr")
    miharu "「ソフィアは最後までワガママだね」"

    show ecg girlstalkX1 sm2 nor with ecg_change


    voice get_voice_filename("son")
    sonya "「ユイゴン、ですから」"

    show ecg girlstalkX1 sm2 nor with ecg_change


    voice get_voice_filename("mhr")
    miharu "「……そうか。約束はできないけれど、凛火、君はソフィアの想いを受け止めるのだろう？」"

    scene ecg girlstalkH2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「……うん」"

    "海晴の問いかけに、私は頷いて答えた。"

    "私がソーニャのために最後にできることは、きっとそれだけだから。"

    scene ecg girlstalkX1 sm2 nor with dissolve


    voice get_voice_filename("son")
    sonya "「では、ソーニャは行くであります」"

    show ecg girlstalkX1 smi nor with ecg_change


    voice get_voice_filename("son")
    sonya "「オネエサマ。ミハル。どうもアリガトウゴザイマシタ」"

    show ecg girlstalkX1 smi smi with ecg_change


    voice get_voice_filename("mhr")
    miharu "「ああ。お気をつけて」"

    scene ecg girlstalkH2 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「ソーニャ……。私は楽しかった。絶対に忘れないから」"

    scene ecg girlstalkX1 smi nor with dissolve


    voice get_voice_filename("son")
    sonya "「ソーニャも、とても幸せでした」"

    show ecg girlstalkX1 tro nor with ecg_change


    voice get_voice_filename("son")
    sonya "「はわわ、名残惜しくなってしまうので、もう行くであります」"


    scene bg lion01 noon
    show son sta nor la1 rev at std_cl
    with dissolve_long

    voice get_voice_filename("son")
    sonya "「では、サヨウナラ」"

    hide son with std_out

    "ソーニャは扉の前で、深く頭を下げた。"

    "そして、そのままお店を出て行く。彼女の背中が遠ざかっていくのを、私は窓からずっと眺めていた。"


    play music audio.miharu

    show mhr civ pai lie rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「行ってしまったね」"

    show rnk civ arm sad at std_cr with std_in

    "海晴の言葉が、随分遠くから響くような感覚があった。"

    "今夜、ソーニャは脱落する。その運命はきっと揺るがない。"

    "思えば、今の私はソーニャのカードを２枚しか持っていない。桂子さんの時に考えたような、同時に指名するという選択肢もない。"

    "もっとも、私がそれをやったところで、一時の自己満足にしかならない。"

    "でも、でも、でも。"

    "一人で去って行くソーニャの後姿は、寂し過ぎた。"

    show mhr civ sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……凛火？」"

    "気付けば、感情は止まらなくなっていた。"

    "制御の利かない想いは、涙になって溢れてきた。"

    show mhr civ nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「だから最初に君がソーニャと仲良くしているのを知った時、ぼくは君を馬鹿だと言ったんだ」"

    show mhr civ sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「でも凛火は、後悔していないと言ったね。その気持ちは今も変わっていないかい？」"

    "うまく声が出せず、私は頷いて返事をする。"

    show mhr civ pai lie rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そんな凛火だから、ぼくは愛しているんだよ」"

    hide rnk
    hide mhr
    with std_out

    "海晴はそう言って、私の隣に腰かけた。"

    "肩同士が触れ合ってから、私は海晴にしがみついてしまった。"

    "私の涙が収まるまで、海晴はずっと隣にいてくれた。"





    stop music fadeout 1
    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1

    "コップ一杯の水を飲んで、私はどうにか気持ちを落ち着けた。"

    "海晴はこれからバイトに行くとのことだ。"

    show mhr civ nor nor rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「では、また明日学校で会おう」"

    show rnk civ arm lie at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……うん。ごめんね、さっきは泣いちゃって。海晴は強いなって、思ったよ」"

    show mhr civ sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。自覚がないかもしれないけれど、ぼくからすれば君の方がよっぽど強い」"

    "微笑む海晴に、私はそんなことないと否定した。"

    show mhr civ sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「選定の期間はまだ半分にも満ちていない。凛火の迷いが消えるまで、ぼくは待っているよ」"

    show rnk civ nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「……ありがと、海晴。でも私は、海晴にもっと自分のことを大切にして欲しい、とも思うよ」"

    show mhr civ sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「その言葉、そっくりそのまま君に返したいよ……そういえばさっきはまた学校でと言ったけれど、次に会うのは夢の中だったね」"

    show mhr civ nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「それ、笑えないよね。じゃ、またね」"

    show mhr civ nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……ああ」"

    hide mhr with std_out

    "海晴はそう言って、ライオン館を後にした。"

    "一人のライオン館は珍しくないはずなのに、どうしてかあまりに静かすぎると思っていた。"

    "三人で笑い合った声が、まだ残っているからかもしれない。"

    "ほとんどお昼からになってしまうけれど、今日はお店を開けようと思っていた。"

    "今晩は久しぶりにおばあちゃんに電話をしようと、ぼんやりと決めていた。"

    $ add_seen_chapter("4-5")

label sentei4:

    call set_replay








    python:
        set_info_date(5, 27, "sun")
        set_info_scene("46")
        set_info_time("lnight")
        set_info_location("07")


    stop music fadeout 2
    scene bg fatalhall01 up large with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    show dia sta fro sm2 big at std_c with std_in

    voice get_voice_filename("dia", 76)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "そして、今日も女神の選定が始まった。"

    "大広間に響く、女神の気品高い声。"

    "パルカにどんな感情があるのか分からない。"

    "何を思い、何のために運命を語り、死ぬはずだった私たちを生かし、選定を行っているかも分からない。"

    show dia sta fro no1 big with std_change

    voice get_voice_filename("dia")
    parca "「浮かない顔をしてらっしゃいますわね」"

    "私はこれまで、女神は人ならざる者なのだからと、現実ではあり得ない存在だからと、考えることを放棄してきた。"

    "ソーニャの言葉が思い出される。"

    "運命は変えられる――。"

    "この女神の選定という儀式さえも変えられるかもしれないなどと、想像だにすることはなかった。"

    scene bg fatalhall01 up with dissolve

    show dia sta nor ama ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「皆様、つれませんわね。ワタクシと楽しくお話をしても損はしませんのに」"

    show aln sta nor irr rev ci at ci_l with ci_in

    voice get_voice_filename("aln", 48)
    alan "「……いいから、早くしろ」"

    "私の隣のスコーピオンさんが、パルカを急かした。"

    "この人は今どこにいるのだろう。"

    "ソーニャと出会ってから、調べるのを一時中断していた。"

    show dia sta nor smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴方サマはいつもせっかちですわね。何か……焦っていらっしゃるのかしら？」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「余計な話を好かないだけだ」"


    voice get_voice_filename("aln")
    alan "「それにお前は中立の立場のはずだろう？　僕との会話が他の参加者の有利になるかもしれない」"

    show aln sta nor irr rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「お前自身の行動でこの選定が平等ではなくなるが、女神としてそれはいいのか？」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら？　ワタクシは中立な立場で、平等にこの選定を取り仕切ると申した覚えはありませんけれど？」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「……フン」"

    show fed sta nor ir2 ci at ci_r with ci_in


    voice get_voice_filename("fed", 76)
    federico_num "「お、おいっ！　そりゃねーだろ！」"

    "会話に割り込んできたのは、海晴の隣の男性――私が氏名のカードを持っているフェデリーコ・カルミナーティだ。"

    "この人が話しているのを、初めて聞いたかもしれない。"

    "恐らく、選定の参加者の中で一番背が高い。比例して足も長く、スタイルがいい。"

    "スーツ姿はびしっと似合っていて、まるでモデルのようだった。"

    show fed sta nor pa4 ci with ci_change

    voice get_voice_filename("fed")
    federico "「オレたちの命がかかってんだぜ？　平等じゃないんじゃ成り立たないだろ」"

    hide aln
    show ode sta nor tro rev ci at ci_l
    with ci_swap


    voice get_voice_filename("ode", 112)
    odette_num "「……ったくこいつは……」"

    show dia sta fro cl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら。Ⅲ番サマ。いかがなさいましたか？」"

    "カルミナーティさんの言葉に、Ⅺの女性も反応をした。"

    "海晴はこちらに目配せをする。やはり、この２人は協力をしている。"

    show fed sta nor bad ci with ci_change

    voice get_voice_filename("fed")
    federico "「大体、最初に配られるカードの時点で不公平だろ」"

    show fed sta nor pa4 ci with ci_change

    voice get_voice_filename("fed")
    federico "「オレが初期カードを持ってる２人がこいつに脱落させられちまったんだ！」"

    "カルミナーティさんは、スコーピオンさんを指さしてそう言った。"

    hide ode
    show aln sta nor tre rev ci at ci_l
    with ci_swap

    voice get_voice_filename("aln")
    alan "「……なら、貴様の初期カードで有効なのは残り１枚というわけだ」"

    show fed sta nor pa1 ci with ci_change

    voice get_voice_filename("fed")
    federico "「ぬなっ」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「不平不満をこぼすのもいいが、自分から情報を開示するのは愚かなことだ」"

    show fed sta nor irr ci with ci_change

    voice get_voice_filename("fed")
    federico "「ってめー……、いい度胸じゃねぇか」"

    show aln sta nor irr rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「僕に現状不満はない。女神。君が速やかに選定を進めればそれでいい」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「うふふ。承知いたしましたわ。貴方サマも、それでよろしいかしら？」"

    "パルカはカルミナーティさんに向き直り、訊ねた。"

    "だが彼は首を縦には振らず、焦った声で話し始める。"

    show fed sta nor ir2 ci with ci_change

    voice get_voice_filename("fed")
    federico "「ちょっと待てよ！　あんたたちもそれでいいのか？」"

    "問い掛ける相手は、私たち選定の参加者全員だ。残っている９人――彼とスコーピオンさんを除いて７人か――に、両手を広げて聞く。"

    "しかし、彼の質問に誰も答えることはなかった。"

    "協力しているⅪの女性でさえも。"

    show aln sta nor tre rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「これで分かっただろう」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「不満がないわけではないが、余計なことを話して失態を見せるのは避けたいというのが総意だ」"

    show aln sta nor ang rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「貴様のようにボロを出すのは特に――愚かだ」"

    show fed sta nor ang ci with ci_change

    voice get_voice_filename("fed")
    federico "「てめえ、覚えてろよ」"

    show aln sta nor tre rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「ああ。貴様が脱落するまでは覚えているだろう」"

    "言い合いをする二人を見兼ねたのか、パルカはため息をつく。"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「もう、口喧嘩は現実世界でお願いしますわ。お会いすることがあれば……ですけれど」"

    "話を打ち切ったパルカは、そのまま大広間の中心まで移動した。"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「それでは、今宵も女神の選定を始めますわ」"


    voice get_voice_filename("dia")
    parca "「廻りなさい。運命の大時計」"



    stop music fadeout 1
    scene bg fatalhall01 normal with dissolve_long
    play music audio.restlessness



    "この言葉を皮切りに、指名の意志確認が行われる。"

    "ソーニャの言葉通りに進めば、今夜の指名はⅪからⅩへの指名になるはずだ。"

    "私は奥歯をぐっと噛み、指名の予定がないことを宣言した。"

    "次は、海晴だ。海晴も同じように、指名を行わないだろう。"

    "４回目の指名になるが、積極的に情報を集めるか様子見をするかで大きく分かれているのだろう。"

    "未だⅪとⅫだけしか指名を行っていないことが、その証拠であった。"

    scene bg fatalhall01 up with dissolve

    show mhr uni nor ser rev ci at ci_l with ci_in

    voice get_voice_filename("mhr", 206)
    miharu "「ぼくの番だね。Ⅹ――君を指名させてもらうよ」"

    show rnk uni arm ten ci at ci_r with ci_in

    voice get_voice_filename("rnk", 546)
    rinka "「えっ……！」"

    show dia sta nor ama ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「ここに来て、初めての方からのご指名ですわね」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「承りましたわ。それでは、他の皆様にも伺って参りましょう」"

    "海晴の言葉に、私は動揺を隠すことができなかった。"

    "私たちは知り合いということが知られているのだから、この行動一つが何かのヒントになってしまうかもしれない。"

    "しかし、それでも驚かずにはいられない。"

    hide dia
    hide rnk
    hide mhr
    with std_out

    show son sta nor smi ci at ci_r with ci_in

    "指名されたソーニャの方が、冷静でいるようだった。"

    "まるで、あらかじめ知っていたかのように――まさか。"

    "あの夜、海晴とソーニャが話していたのは、ソーニャが海晴のカードを持っていたからということだけではない。"

    "順番は回り、Ⅺの女性の番となった。"

    show ode sta nor gla rev ci at ci_l with ci_in


    voice get_voice_filename("ode")
    odette_num "「指名するぜ、あたしはよぉ……そこの小娘と同じ、Ⅹのこいつをさ」"

    "Ⅺの女性は、ソーニャを指さしながらそう言った。"

    "彼女にとって予想外のことが起きたに違いない。"

    "だが、彼女は笑っていた。心底楽しそうに、エサを前に牙を剥く獣のように。"

    "Ⅺの女性は、ソーニャに≪自身のカード≫を持たれていることを知っている。"

    "海晴に脱落させられれば海晴にそのカードの内容を知られる危険があるわけだから、当然避けたいはずだ。"

    "海晴も同じなのだろう。"

    "きっとお互いの狙いは膠着状態による指名の取り下げ……≪自身のカード≫１枚を守るために、≪自身のカード≫１枚を全員に公開するのでは釣り合わない。"

    show ode sta nor nor rev ci with ci_change


    voice get_voice_filename("ode")
    odette_num "「さあ女神さん。こういう場合はどうするんだっけ？」"

    show dia sta fro no2 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「指名の優先権を取得するかどうか決めていただきますわ。≪ご自身のカード≫を１枚全員に公開すれば、優先権を取得できます」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「この場合、先に決めた側が駆け引きで不利になりますから、同時に決めていただきます」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「優先権を取得する場合は、≪ご自身のカード≫を１枚、ワタクシへ差し出してください」"

    show ode sta arm irr rev ci with ci_change


    voice get_voice_filename("ode")
    odette_num "「かかっ、不利で構わねぇ。あたしから意志表示してやるよ。優先権はノーだ。いらねえ。後はてめーの方で決めてくれ」"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「もうっ、Ⅺ番サマ！　ワタクシがルールを申し上げているのですから守ってくださいな！」"

    show dia sta fro sm2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでⅡ番サマはいかがなさいますか？」"

    scene bg fatalhall01 normal with dissolve

    "パルカは海晴へ向き、ゆっくりとした口調で訊ねた。"

    "海晴は頷くと、カードブックを開く。"

    "そして、１枚のカードを取り出した。"

    scene bg fatalhall01 up with dissolve

    show mhr uni pai lie ci at ci_r with ci_in

    voice get_voice_filename("mhr")
    miharu "「ぼくは、氏名のカードを公開しよう。これをもって優先権を取得し、Ⅹ――君を、指名させてもらう」"

    "海晴がそう言ったのを聞いても、ソーニャは驚きの表情を浮かべなかった。"

    "寂しげな表情こそしていたが、それはこの選定が始まってからずっとだ。"

    "優先権を海晴にとられたⅪの女性の方が、笑顔を崩した。海晴を睨むような、厳しい目つきだ。"

    show ode sta arm ser rev ci at ci_l with ci_in


    voice get_voice_filename("ode")
    odette_num "「氏名は捨て……か。あいつ面白いじゃねえか……」"

    show dia sta nor smi rev ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「承りました」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「それではこれより、Ⅱ番サマによるⅩ番サマのご指名を開始いたしますわ」"

    "女神の言葉に応じて、大広間に地響きが鳴りわたる。"

    "そして、海晴とソーニャの立つ床がせり上がっていく。"







    python:
        set_info_scene("47")
        set_info_time("night")
        set_info_location("16")



    stop music fadeout 1
    scene bg fatalhall02 normal with fade_long
    play music audio.fatalhall
    pause 2
    scene bg fatalhall02 up
    show mhr uni nor ser ci at ci_r
    show son sta nor nor rev ci at ci_l
    with dissolve







    "運命の大広間の上層では、海晴とソーニャが向かい合っていた。"

    "せり上がって来た床の上で、お互いが視線を合わせている。二人とも、浮かない表情。"

    "だが、顔を逸らすことはしない。"

    show son sta nor la1 rev ci with ci_change

    voice get_voice_filename("son", 159)
    sonya "「……ミハル、アリガトウであります」"

    show mhr uni sco wic ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「いや、お礼を言うのはぼくの方だよ。あの夜……君の方からぼくに声をかけてきたときは驚いたけれど、その決断は間違っていないと信じているよ」"

    show son sta nor smi rev ci with ci_change

    voice get_voice_filename("son")
    sonya "「ハイ。きっとオネエサマではできない判断だったと思うであります」"

    show mhr uni sco sh1 ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは凛火のために命を捧げると決めているからね。覚悟するのは容易いよ」"

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「あらためまして、ごきげんよう」"

    "いつの間にか現れた女神が、二人に微笑みかけた。"

    "海晴は彼女に対し、露骨に迷惑そうな顔を浮かべていた。"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマ方はお知り合いでいらっしゃったのですね。それに……他の参加者たちのように敵意を向け合ってもいません」"

    "敵意はむしろ、女神に向けられていた。"

    "海晴はパルカと世間話をする気はないことを見せつけるため、話題を変える。"

    show mhr uni sco vig ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「この後、ぼくはどうすればいいのかな？」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「Ⅹ番サマのカードを３枚、お選びになってください。そしてそこに書かれている内容を読み上げてくださいませ」"

    show mhr uni sco dis ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「……ああ」"



    play music audio.electing
    scene ecg senteimiharu gen with dissolve_long

    "海晴の手元には、ひとりでに開かれたカードブックがあった。カードは光に包まれ、空中に並べられている。"

    "その中から、海晴は３枚のカードに触れた。"

    python:
        add_character_cards("mhr", ["10_name", "10_death", "10_regret"])
        add_character_cards("fed", ["10_name"])
        add_character_cards("son", ["10_death"])
        add_character_cards("ode", ["10_name", "10_death", "10_regret"])


    voice get_voice_filename("mhr")
    miharu "「氏名、ソフィア・プリズニェツィ・アレクセーエヴナ。死因……詳細は省いてここに書かれているものをそのまま読むよ……病死、だね」"


    voice get_voice_filename("mhr")
    miharu "「ソフィア、君の願いは聞いたよ。ぼくは約束できないけれど、凛火は君の願いを受け止めた」"

    show ecg senteimiharu ser with ecg_change


    voice get_voice_filename("mhr")
    miharu "「凛火が叶えたいというのであれば、ぼくも最大限協力をするよ。ただし、凛火が最後の一人に残ることが最優先なのは変わらない」"


    scene bg fatalhall02 up with dissolve_long

    show son sta nor smi rev ci at ci_l with ci_in

    voice get_voice_filename("son")
    sonya "「ハイ。分かっています」"

    show son sta nor sad rev ci with ci_change

    voice get_voice_filename("son")
    sonya "「それでもソーニャは、最後にオネエサマとミハルと会うことができて、幸せでありました」"

    show son sta nor la1 rev ci with ci_change

    voice get_voice_filename("son")
    sonya "「パサジールのことも、どうかよろしくするであります」"

    show mhr uni sco thi ci at ci_r with ci_in

    voice get_voice_filename("mhr")
    miharu "「……ああ」"

    scene ecg senteimiharu ser with dissolve_long

    "海晴はそう答えたあと、一度下を向いた。"

    "そのまましばらく目を閉じてから、ゆっくりと口を開いた。"

    show ecg senteimiharu gen with ecg_change


    voice get_voice_filename("mhr")
    miharu "「未練……広く自由に――世界を見ること」"

    scene ecg trianglecard small with dissolve

    "海晴の言葉に反応し、３枚のカードがひとりでに動き始める。"

    "空中を動いたカードは大広間の中心で三角に並び静止した。"


    scene bg fatalhall02 up
    show son sta nor sad rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("son")
    sonya "「サヨウナ……」"

    show mhr uni nor rea ci at ci_r with ci_in

    voice get_voice_filename("mhr")
    miharu "「ぼくはさよならという言葉が嫌いなんだ。願わくは、凛火とぼくの幸福を祈って欲しい」"

    show son sta ban lau rev ci with ci_change

    voice get_voice_filename("son")
    sonya "「ハイ」"

    "少女は一呼吸おいてから両手を組み、祈りを捧げた。"

    show son sta nor smi rev ci with ci_change

    voice get_voice_filename("son")
    sonya "「リンカとミハルの未来に、祝福がありますように」"

    show mhr uni nor ser ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「ありがとうソフィア。君のことは忘れない」"

    show mhr uni nor nor ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「どうか、安らかに」"

    scene ecg trianglecard small with dissolve_long

    "白い光が一気に広がり、大広間を覆いつくす。"

    "海晴はその光に眩みながらも、ソーニャの泣き顔をじっと見ていた。"






    stop music fadeout 2
    scene white with Dissolve(3)
    play music audio.death
    pause 2

    scene ecg croomcelling hos with dissolve_longest

    "後悔と空虚さという感情が、流れ込んでくる。"

    "自室のベッドの上。"

    "駆け付けた医者と、見守る両親。"

    "徐々に息苦しくなっていく中で、少女はこれまでの人生を振り返っていた。"

    "ほとんどの風景が、この部屋の天井だった。"

    "本かモニターの画面の中でのみ、見ることのできる広い世界。"

    "何度想いを馳せたことか。"

    "決して届かない、自由。"

    "あまりに無色な人生だった。"

    "最期の瞬間、少女の脳裏に浮かんだのは、憧れた広い世界ではなく、ただ寂しい生涯なのであった。"






    stop music fadeout 2
    scene bg fatalhall02 up
    show mhr uni sco dis ci at ci_r
    with fade_longest
    play music audio.fatalhall
    pause 1


    voice get_voice_filename("mhr")
    miharu "「趣味が悪いな。脱落した人間の今際の際を指名者に見せるなんてね」"

    show dia sta nor ama rev ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「ワタクシが意図したものではありませんわ。これは、儀式でございますから」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマの指名により、選定中一時的に変わっていた運命が、元の死の運命へと強制的に引き戻される」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「この場所の力を借り、儀式は行われる……その余波が貴女にいってしまうのはあくまで弊害……どうしようもないことでございますわ」"

    show mhr uni nor ser ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「待ってくれ。君の……女神の意図ではない？　これは、女神の選定だろう？　君の意図しない力が干渉しているというのか？」"

    hide mhr with ci_out

    "海晴の質問に答えが返ってくることはなく、海晴の立つ床が振動する。"

    "そのまま床は動き出し、徐々に下がって行った。"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシ、無用な詮索をする方は好きではございませんの」"

    "パルカは海晴に声が聞こえない距離になってから、呟くようにそう言った。"









    python:
        set_info_scene("48")
        set_info_location("07")





    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.badguys
    pause 2
    scene bg fatalhall01 up
    show mhr uni sco dis rev ci at ci_l
    with dissolve
    pause 1



    "オデットの代わりに、隣――Ⅱの女が指名を終え、戻って来た。"

    "選定が始まった当初から、ⅠとⅡはどうやら知り合いのようだ。それも敵対はしていないように見えるから、オレとオデットのように協力関係にあるのかもしれない。"

    "しかし、予想外だった。"

    "てっきり、オデットが一歩引いたらあいつも引くものかと思っていたからだ。"

    "オデットとしては、ソフィアの脱落よりも自分の情報が知られない方が優先だったはずだ。"

    "オレがソフィアと接触する可能性がゼロではないにしろ、オデットにとっちゃ他の参加者がソフィアの情報を得るのに比べればリスクは低い。"

    "オデットが引いたら読み合いが発生せず、安心して膠着状態を維持できる。オデットはそれを狙ったからこそ、パルカの言葉を無視して先に宣言をしたんだ。"

    "にもかかわらず、Ⅱの女は≪自身のカード≫の公開を厭わず、ソフィアの指名を決めやがった。"

    show fed sta nor irr ci at ci_r with ci_in

    voice get_voice_filename("fed")
    federico "「ちっ……分からなくなってきたぜ」"

    "Ⅱの女は、Ⅰのちんちくりんに比べれば随分と美人だ。東洋人なんだろうが胸もでかく、スタイルもいい。"

    "どうせすぐ脱落するだろうと思っていたが、意外な動きを見せた。"

    "こいつは悪くない――と思わず唾を飲み込んじまった。"

    "いい女ってのは、度胸も備えているものだ。オデットのようなゴリラは例外として。"

    show dia sta fro gl2 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「それでは、どのカードを取得するかを宣言してください」"

    "女神が、Ⅱの女にそう問いかけた。"

    "本命は、オデットのカードだろう。"

    show mhr uni nor ser rev ci with ci_change


    voice get_voice_filename("mhr")
    miharu_num "「ぼくは、≪Ⅰ・死因≫のカードをもらおう」"

    "だが、またもオレの予想は外れることになった。"

    hide fed
    show rnk uni arm imp ci at ci_r
    with ci_swap


    voice get_voice_filename("rnk")
    rinka_num "「えっ……ど、どういうこと？　ソーニャが……？」"

    "Ⅱの女の発言に一番驚いているのは、Ⅰ番だ。"

    "無理もないだろう。協力関係にあったとして、他のカードもあるだろうによりにもよって自分のカードが選ばれちまったんだから。"

    show mhr uni sco vig rev ci with ci_change


    voice get_voice_filename("mhr")
    miharu_num "「君はまだ理解が足りないようだね。これは――選定なんだ。これ以上、喋らないでくれ」"

    "Ⅱの女は、冷たい声でそう言った。"

    "Ⅰの女は、はっとして、それ以上喋ることはなかった。"

    show dia sta fro cle ci with ci_change

    voice get_voice_filename("dia")
    parca "「それではⅡ番サマ。指名の優先権を取得した代償として、貴女≪自身のカード≫をワタクシにお渡しくださいませ」"

    show mhr uni sco wic rev ci with ci_change


    voice get_voice_filename("mhr")
    miharu_num "「ああ。これでいいのかい？」"

    hide rnk
    hide mhr
    hide dia
    with ci_out

    "Ⅱの女の前まで移動して来たパルカに、直接カードを手渡した。"

    "その瞬間、オレの手元のカードブックが白い光に包まれた。"

    "――Ⅱ・氏名・蛇鉈海晴。"

    show fed sta nor nor ci at ci_r with ci_in


    voice get_voice_filename("fed")
    federico "「ミハル・ヘビナタか……」"

    python:
        add_character_cards("rnk", ["2_name"])
        add_character_cards("mhr", ["2_name"])
        add_character_cards("fed", ["2_name"])
        add_character_cards("sig", ["2_name"])
        add_character_cards("yuu", ["2_name"])
        add_character_cards("sca", ["2_name"])
        add_character_cards("ode", ["2_name"])
        add_character_cards("aln", ["2_name"])

    "ミハルってのはオレにも言いやすい名前だ。"

    "なるほど、カードはこうやって全員に公開されるというわけか。公開というより、全員が取得って感じだな。"

    "参加者はそれぞれ、自分のカードブックに目を通していた。"

    show rnk uni arm sad rev ci at ci_l with ci_change


    voice get_voice_filename("rnk")
    rinka_num "「海晴……どうして……」"

    hide fed
    show mhr uni nor ser ci at ci_r
    with ci_swap

    voice get_voice_filename("mhr")
    miharu "「今はもう、君と話すことは何もない」"

    "Ⅰの女も、こいつのカードを取得して驚いていた。ミハルは本名を教えていなかったってわけか。"

    "ここまで来れば、状況は分かる。"

    "――仲間割れだ。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro gl2 big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者は１名。これをもって、選定を終了といたしましょう」"

    "衝撃を受けたままのⅠをよそに、パルカが選定の終了を宣言した。"

    "混沌としてきたこの選定。"

    "Ⅻの野郎やオデットに先を越され続けて焦っていたが、何が起こるか分からなくなってきた。"

    "オデットが驚くところなんて特に痛快だった。"

    "ミハルがオデットの情報を取得していたら、あいつに接触しようと考えていたが……どうやらまだオデットと組んでいる方がよさそうだ。"

    "腹のところに蓄えた野心がこみ上げてくるのを、オレはどうにか抑えていた。"

    $ renpy.end_replay()
    $ add_seen_chapter("4-6")

    $ persistent.sentei4_clear = True
    $ grant_achievement("divine_selection_04")

    jump f005_1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

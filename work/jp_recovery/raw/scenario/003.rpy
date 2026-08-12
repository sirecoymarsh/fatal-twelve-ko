

label f003:














    python:
        set_info_scene("22")
        set_info_date(5, 14, "mon")
        set_info_time("noon")
        set_info_location("11")

    stop music fadeout 2
    scene bg hotel beijing with fade_longest
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "オデットが無事に魯を脱落させたのを夢の世界で見届けたオレは、気付けば朝を迎えていた。"

    "夢の世界へ移動したときに起きていたのか寝ていたのか、記憶ははっきりしていなかった。"

    "時差のために日本の０時を意識していなかったせいではあるが、今後、日曜日は気をつけなければならない。"

    "ホテルを出る準備を終えたオレたちは、ルームサービスで頼んだモーニングを食べながら話していた。"

    show fed sta nor no1 at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「でよう、結局魯の未練はなんだったんだ？」"

    show ode sta nor nor rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「何だ。まだ予想がついてなかったのか。お前が自分で言ってたんだぞ？」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「は？　オレが、か？」"

    "オレは自分の発言を思い出しながら、逡巡した。"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「やっぱり愛人関係なのか？」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「ま、いいか。それじゃ全く気付いてないみたいだしよ」"

    "オデットはカップに入ったカフェ・アメリカーノを飲み干してから言った。"

    "エスプレッソをお湯で薄めたような飲み物をよく飲めるもんだ。"

    show fed sta nor nor with std_change

    voice get_voice_filename("ode")
    odette "「犬、だよ」"

    show fed sta nor pa1 with std_change

    voice get_voice_filename("fed")
    federico "「……犬？　犬ってあの犬だよな？」"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「ああ。だが、あの愛人が飼ってた犬ってわけじゃねえ」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「あいつは犬と一生を共にしたかったんだ。子犬から育てて、成犬になれば友人になり、最期を看取る」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「ありふれた経験だが、得難い経験でもある」"

    python:
        add_character_cards("ode", ["7_regret"])
        add_character_cards("cnh", ["7_regret"])

    show ode sta nor tro rev with std_change_wait

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「ふぅん、犬ごときが未練になるもんかね」"

    show ode sta nor tro rev with std_change

    voice get_voice_filename("ode")
    odette "「んなもん、人それぞれだろうに。お前の国でもペットを飼うのは普通だろ？」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「オレの国では、な」"

    "オレの身の上話になっても嫌なので、オレは話を逸らすことにした。"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「ところで、何でそれが分かったんだ？」"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「お前が愛人のところに犬がいるって言っていたのを聞いてピンと来たんだ。もしかして――ってな」"

    show ode sta gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「んで調べてたら、魯の妻が犬アレルギーだったって判明した。はははは、そりゃ飼えないわけだ」"

    "オデットはさらに魯の情報を話した。"

    "彼は幼い頃、田舎の実家で犬を飼っていたらしい。"

    "だがある日、その犬は交通事故で死んでしまった。"

    "悲しみに暮れた魯の家族はそれ以降、動物を飼うことはしなかった。突然に失う悲しみを知ってしまったから。"

    "一方で、魯にはある後悔が生まれたそうだ。"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「今度こそ、ちゃんと死を看取ってあげたいってな」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「気持ちだけなら分からないでもないな。未練になるほどってのはオレは理解できないけどさ」"

    "オレが言うと、オデットは鼻で笑った。ああ見えて、あの女は動物好きのようだ。"

    "案外、こいつの未練も犬なんじゃないか。海の上での生活が続けば、中々動物も飼えないだろうし。"

    "ともかく、魯の話はこれでほぼ終わりだった。"

    "その後は忙しさや金銭的な問題からなかなか動物を飼えず。結婚して安定したが奥さんは犬アレルギー。"

    "都合のいい愛人を抱えてから犬を飼わせたのか、犬を飼っているから愛人にしたのか。はたまた本当は愛人ではなく犬の世話係だったのか。"

    "疑問は全て、オデットだけが知っていることになる。"

    "ま、もう脱落しちまった奴のことなんてどうでもいいがな。"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「――で、ニュースはどうなった？」"

    "女神の話では、選定中に脱落をすると「本来の歴史」に戻ると言っていた。"

    "選定期間に生きていたという事実がなかったことになるということだ。"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「ほれ、自分で見ろ」"

    "オレが言うと、オデットはスマートフォンを投げて渡してきた。"

    "あいつの反応からして、見るまでもないだろう。オレは適当に画面を流し見だけして返した。"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「２週間前、中国の有名企業の役員が会議中に脳梗塞で突然死――ぴったりだな」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「ところでよ、あの運命の大広間とやらの上はどうなってるんだ？　指名の時、上に行ってただろ？」"

    "そして同時に、オレはどうやって相手を指名するのか気になっていた。"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「あー、うーん……ちぃと説明が面倒だが、ま、教えておいた方が今後はいい、か」"

    "オデットは煮え切らない態度だったが、少し間を置いてから話し始めた。"

    "それはこの女にしては長い話となった。"














    stop music fadeout 1
    scene bg fatalhall02 normal with wfade_long
    play music audio.restlessness
    pause 1

    "オデットと魯の立つ丸い床は、それぞれ部屋の中心を基準に公転しながら上がって行った。"

    "ある高さまで上がったところで、床は停止する。"

    "そこは、下層と意匠は似ているが、ところどころが異なった空間であった。"

    "女神はいつの間にか上層に移動して来ていて、不敵な微笑みを浮かべる。"

    scene bg fatalhall02 up large with dissolve

    show dia sta fro glo big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それでは、指名をどうぞ」"

    hide dia with std_out

    "床が上層へ移動するまでの間に、オデットの本からはひとりでにすべてのカードが飛び出していた。"

    "カードは光に包まれ、何枚あるのかも、何が書かれているのかも、オデットにしか見えない。"

    scene bg fatalhall02 up with dissolve

    show ode sta nor tro rev ci at ci_l with ci_in

    voice get_voice_filename("ode")
    odette "「えー、何だ。言えばいいんだな？　こいつの情報を」"

    show cnh sta nor pan ci at ci_r with ci_in

    voice get_voice_filename("cnh")
    chanho "「貴様っ……！」"

    show dia sta fro sm2 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「貴女サマのお好きなように、カードを宣言してくださいまし」"

    "オデットは目の前に現れたカードに目を通した。"

    "自分のカードを含め、彼女が所持しているのは９枚だ。その中から、決められた３枚を読み上げる必要がある。"

    "指でなぞりながら、オデットは口を開いた。"



    play music audio.electing
    scene ecg senteiodetto nor with dissolve_longest


    voice get_voice_filename("ode")
    odette "「{rb}魯{/rb}{rt}ロ{/rt}{rb}昌鎬{/rb}{rt}チャンホ{/rt}」"


    voice get_voice_filename("cnh")
    chanho "「やめろ……やめてくれ！」"

    show ecg senteiodetto bor with ecg_change


    voice get_voice_filename("ode")
    odette "「てめーの死因は脳梗塞」"


    voice get_voice_filename("cnh")
    chanho "「私には家族がいるんだ。私が死んだら家族はどうなる？　貴様はその責任を背負えるのか？」"


    voice get_voice_filename("cnh")
    chanho "「まだ間に合う。指名をやめなさい。金はある。私は株も土地も持っている」"

    show ecg senteiodetto dow with ecg_change


    voice get_voice_filename("ode")
    odette "「みっともねぇなぁ」"


    voice get_voice_filename("cnh")
    chanho "「……いくら欲しい？　いくらでも出す。私の信用情報ならいくらでも引き出せる。一生遊んで暮らせるぞ？　どうする？」"

    show ecg senteiodetto nor with ecg_change


    voice get_voice_filename("ode")
    odette "「こいつの未練は犬……だ」"


    voice get_voice_filename("cnh")
    chanho "「ああ……終わりだ……私はおしまいだ……」"

    show ecg senteiodetto reb with ecg_change


    voice get_voice_filename("ode")
    odette "「金だろうが同情だろうが、命の対価にならねーよ」"

    show ecg senteiodetto smi with ecg_change


    voice get_voice_filename("ode")
    odette "「何より、勝負事であたしが妥協するわけないんだよ」"

    scene ecg trianglecard with dissolve

    "オデットの宣言に合わせて、３枚のカードは空中を移動した。"

    "運命の大広間の中央で静止したカードは、空中でそれぞれを頂点とした正三角形を作った。"



    stop music fadeout 1
    scene bg fatalhall02 up
    show ode sta arm smi rev ci at ci_l
    with fade_longest


    voice get_voice_filename("ode")
    odette "「じゃあな、おっさん」"

    "オデットの言葉が届いていたかは分からない。"

    show cnh sta nor pan ci at ci_r with ci_in

    "成す術のなくなった魯は、うなだれるばかりだった。"

    "カードは無機質に、一枚一枚が白い光を放つ。"

    scene bg fatalhall02 up large with dissolve

    show dia sta fro sm2 big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「散りゆく者に福音あれ」"

    "光は増幅し、空間全体を埋め尽くした。"

    "その時だった。"

    "オデットが眩しさで一瞬視界を失った直後、脳裏には夢の世界と全く異なった映像が映し出された。"

    "映像はやがて、オデットの感覚とリンクしていく。"


    stop music fadeout 2
    scene white with Dissolve(3)
    play music audio.death
    pause 2

    scene ecg croomcelling with dissolve_longest




    "視界に映っているのは、不自然に明るい会議室にいる太った男たち。誰もが高そうなスーツを着ていて、退屈そうな顔を浮かべている。"

    "青白い光は、手元に置かれた白い紙に反射し、目を突き刺そうとしている。"

    "部屋の中では会話が繰り広げられていることが分かった。声のトーンは重く、きっと深刻な話をしているのだろう。"

    "しかし、何を話しているのか理解することはできなかった。まるでノイズが飛び交っているようだった。"

    "その時だった。"

    "視界は突然に捻じれた。"

    "がん、とデスクに頭をぶつけたが、全身に力が入らない。"

    play se "body_fall01"
    with quake_fast

    "そのまま床へと倒れ伏した。"

    "ノイズは、今度は自分に向けられるのだと分かった。"

    "ふわりふわりと浮遊するような感覚のまま、頭の中が真っ白になっていく。"

    "走馬灯が走る。たくさんの人が彼に話しかけてきている記憶だが、全く理解することができなかった。"

    "その感覚の乖離で、オデットは何が起きているのかを理解した。"


    voice get_voice_filename("cnh")
    chanho "「が……は……」"




    scene black with dissolve_long

    "これは、魯の記憶だ。"

    "魂に焼き付いた、死の瞬間の出来事。"

    "最期に、魯は幼い頃に亡くした犬のことを想い出していた。"








    scene black
    pause 2
    scene bg fatalhall02 normal with dissolve_longest
    pause 1

    "フラッシュバックが終わる頃、対面に魯の姿は消えていた。"

    "オデットが投げたカードも消滅していて、部屋は元の薄暗い大広間へと戻っていた。"

    "オデットは、天から差し込む光が僅かに太くなったような印象を受けていた。"

    scene bg fatalhall02 up with dissolve

    show dia sta fro nor big at std_c with std_in


    voice get_voice_filename("ode")
    odette "「なるほどな。脱落させた方にも死を体感させるとは、お前の根性は腐ってるみたいだ」"

    show dia sta fro smi big with std_change

    voice get_voice_filename("dia")
    parca "「くすっ」"

    "パルカは何も答えず、微笑を浮かべるだけだった。"

    "その手元には、３枚のカードがあった。オデットは、それが魯の元々持っていたカードであると理解した。"

    show dia sta fro no1 big with std_change

    voice get_voice_filename("dia")
    parca "「≪Ⅴ・氏名≫≪Ⅺ・氏名≫≪Ⅺ・死因≫貴女はどのカードを選びますか？」"

    "パルカが訊ねた直後、オデットの乗った床は再び動き出す。"

    show dia sta fro nor big with std_change

    voice get_voice_filename("dia")
    parca "「下へ戻るまでに、考えておいてくださいね」"

    scene bg fatalhall02 up with dissolve

    show ode sta nor tro rev ci at ci_l with ci_in

    voice get_voice_filename("ode")
    odette "「選択肢ねーじゃねーか、それ」"

    "オデットは不満そうに呟いた。想像がついていたことではあるが、当たってしまうと嫌な内容だ。"

    "こうして、オデットは運命の大広間の下層へと戻っていった。"







    $ set_info_location("11")

    stop music fadeout 1
    scene bg hotel beijing with wfade_long
    pause 1

    show fed sta nor int at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「なるほど……な」"

    "オデットの話を、想像しながら聞いていた。"

    "脱落させた相手の死の瞬間を共有する。してしまう。"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「嫌な気分だぜ。パルカってのは、あんな顔してひどい奴だ」"

    show ode sta nor lau rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「そうか？　中々にスリルがあったけどよ」"

    "オデットの言葉を聞いて、オレはわざと聞こえるようにため息をついた。"

    "そんなことを気にも留めていない様子で、続ける。"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「んなことより、日本入りするぜ」"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「結局行かなきゃいけないから、早い方がいいってことだな。オレもそう思っていた」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「それに――あんたが取得したカードの主はどうやら日本人だったな。相当なジジイだったと思うが」"

    show ode sta gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「そういうことだ。よし、食ったら出るぞ」"

    "これでやっと２回目の選定が終わったような気がした。"

    "オレはクロワッサンをミルクで流し込み、立ち上がった。"



    python:
        set_info_scene("23")
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

    show rnk paj arm ang rev up:
        std_l
        yoffset 50
    with std_in

    voice get_voice_filename("rnk")
    rinka "「はぁっ……はぁっ……」"

    "今朝も、悪夢を見た記憶がはっきりとあった。"

    "二度目となる女神の選定。"

    "すでに、自分がその参加者であることは受け入れていた。"

    "こうして生きているから、死んでしまったことへの実感はまだないけれど、信じる信じないの問題ではなかった。"

    "ただ自分の生活が選定とはまるで切り離されたかのように今まで通りなことに、少し危機感を覚え始めていた。"

    "私の手の届かないところで、２人も脱落しているのだ。だから選定は着々と進行している。"

    "あの人たちはもう、２週間も前に死んでしまったのだ。"

    "運命の大広間で見た顔を想い出す。"

    "それだけで、胸がぎゅーっと痛くなった。"

    "私は――まだ死にたくはない。"

    "自分のカードを見ることができないのがもどかしかった。"

    "漠然と想う死への抵抗感の理由――私自身の未練が何かまだ私にも分からなかったのだ。"

    "海晴とのことがまだ解決していなかったけれど、お互いにそんなことを考える間もなく脱落させられる可能性だってある。"

    "昨晩指名した女性も、初回で指名した男性も、他の人もみんな怖かったけれど、私だって黙ってやられるわけにはいかない。"

    show rnk paj nor que rev up with std_change

    voice get_voice_filename("rnk")
    rinka "「私が、やらなくちゃいけないこと……」"

    scene ecg cardbook op3 with dissolve_long

    "私が持っている３枚のカード。"

    "調べるならきっと、この人たちを優先的に調べればいいのだろう。"

    "名前が分かっているフェデリーコ・カルミナーティさんという人は、一度ネットで検索したことがある。"

    "当然、収穫はなし。せいぜい、イタリアでよくある名前ということが分かっただけだ。"

    "残りのカードの≪Ⅳ・死因≫≪Ⅸ・未練≫は、両方とも外国の人だったってことくらいしか分からない。"



    scene bg myroom morning large:
        zoom 1.5
        align (0.0, 0.6)
    show rnk paj sur su1 rev up:
        std_l
        yoffset 50
    with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「調べようがないって、こんなの」"

    scene bg myroom morning with dissolve

    "ため息をついて、私は朝の仕度をすることにした。"

    "こちらから分からなければ、相手だって同じ可能性はある。"

    "しかし、時間がたっぷりあるわけではない。"

    "初期のカードで分配されたものの中に私の名前はあるわけで、きっと獅子舞凛火が私だと知られるのは時間の問題だからだ。"

    "一つ気になっていたのは、≪Ⅳ・死因≫となっている≪焼死≫が私の死因と同じ単語の可能性があることだ。"

    "Ⅳは確か外国人の男の子。"

    "ただ≪焼死≫だからといって火事に巻き込まれたのかどうかは分からない。"

    "火の中にいた私が≪焼死≫したのかどうかも分からないのと同じように。"

    "そもそも、電車で火事が起きた原因は何なのだろう。"

    "事故や落雷――テロ。可能性はいくつもあるけれど、「なかったこと」になってしまった事件を調べようがない。"

    "それこそ自分の記憶だけが頼りなのだ。"

    show rnk paj arm ang at std_c with std_change

    voice get_voice_filename("rnk")
    rinka "「あー、もうやめやめ」"

    "調べようがないのと同じように、思い出しようがないのだ。"

    "私が生きているこの世界に、ヒントが転がっているはずはないだろうから。"

    "私は下の階で食パンを食べてから、今日も学校へと向かった。"









    python:
        set_info_scene("24")
        set_info_time("noon")
        set_info_location("08")

    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show mao uni sel glo rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「やーっとお昼だよぉ。今日はお弁当？」"

    "昼休みになって、真央と海晴が席までやって来た。"

    "私が一人で食堂へ行こうとしていたところを、真央が引き留めた。"

    "考え事をしていたので、真央に声をかけられなかったらきっと別々にお昼を食べていた。"

    "普通にしていたつもりで、全然普通にできていないじゃないか。"

    show rnk uni arm lie at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「うん。私も今から行こうと思ってたとこ」"

    show mhr uni sco cau behind rnk at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「ぼくも今朝はちょっと寝坊してしまってね。お弁当を作れなかったんだ」"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「寝坊……」"

    "夢の世界へ行っていたからか――とは聞くことができなかった。"

    show mao uni nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「みはるんが寝坊なんて珍しいねぇ。さて、食堂へレッツゴ～」"









    $ set_info_location("15")

    scene bg schoolrooftop noon with fade

    "飴茶女子は敷地内に大学もあるため、そこの食堂を利用することができる。"

    "中等部は利用禁止だが、高等部になると使用が許可される。"

    "だが、大学生が和気あいあいとしている中で利用するのは気が引けるから、大体は購買で昼食を買って持ち帰るだけというのが多い。"

    "特に私たちは目立つので、居心地があまりよくないのだ。"

    "そんな事情があり、私たちは食堂に隣接している購買へ行って、屋上へ戻って来ていた。"

    show mao uni sel glo rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「うーん、貸し切りだ」"

    "幸いにも、今日は私たち以外には誰もいなかった。屋上は開放されていて、晴れであれば昼食をここでとる生徒も多いのだが、珍しい。"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「そういえばさ、二人は何を買ったのぉ？」"

    show mhr uni sco smi at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「ぼくはハムサンドだよ。シンプルで外れがないし、何より安いからね」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「えー、それで足りるー？」"

    show mhr uni sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「真央こそ、焼きそばパンとあんパンだろう？　量で言えばそんなに変わらないよ」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「いやいや、うちはコーヒー牛乳を買ってるからカロリーは圧勝だねぇ」"

    "真央は勝ち誇った顔で言うと、紙パックにストローを差した。"

    "500ミリリットルの紙パックだ。昼休みで飲み切るには少し多い気もする。"

    show rnk uni arm ama at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「カロリーで勝負してどうすんの？」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「うーん、太る？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「駄目だろそれ……」"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんはもう少し太った方がいいと思うけどねぇ」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「……胸見ながら言わないでくれる？」"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「おーこわ」"

    "私は呆れてため息をついた。自覚はあるから、こんな時にわざわざ言わないで欲しい。"

    "特に、海晴が隣にいると顕著だ。"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「それで、凛火は何を買ったのかな？」"

    show rnk uni nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「……カツサンド」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「はい、りーたんの優勝。やっぱりカロリー摂取する気あるんだねぇ」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「競ってないから」"

    scene bg schoolrooftop noon large:
        align (1.0, 0.0)
    with dissolve

    "私がラップを開けたところで、真央は「一口いい？」と尋ねてきた。"

    "買った本人より先に食べようとするところが真央らしい。私がカツサンドをひょいと近付けると、真央はそのまま一口かじった。"

    show mao uni nor che rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「ああっ、カツまでいかなかった……」"

    show rnk uni arm ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「一口小さいもんね、真央……って海晴どうしたの？」"

    "海晴は無表情で真央のことを見つめていた。"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「いやぁ、みはるんも欲しいんじゃない？」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「えーっと、じゃあハムサンドと交換する？　真央がかじってない方あげるから」"

    show mhr uni sco wic at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「お構いなく。ぼくは揚げ物は苦手だから、いらないよ」"

    show mao uni sel mor rev with std_change

    voice get_voice_filename("mao")
    mao "「スミマセン」"

    scene bg schoolrooftop noon with dissolve

    "真央は海晴に謝ってから、自分の焼きそばパンを一口差し出していた。"

    "海晴がそれも断ると、真央は「あはははー」と笑ってみせた。"

    "全く、何をやっているんだか。"

    "だが同時に、私はこれが日常なのだとふと思ってしまった。"

    scene bg schoolrooftop noon large:
        align (1.0, 0.0)
    with dissolve

    show mhr uni sco cau rev at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「…………凛火？」"

    show mao uni nor que rev at std_l with std_in

    voice get_voice_filename("mao")
    mao "「どしたの？」"

    show rnk uni sur su1 at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「いや、何でもない。ちょっとぼーっとしちゃってさ」"

    "私はそう答えてから、お昼ご飯を食べるのを再開した。"

    "昼休みのチャイムが鳴る直前まで屋上にいて、おしゃべりをしながらゆっくりとした時間を過ごしていた。"









    python:
        set_info_scene("25")
        set_info_time("evening")
        set_info_location("08")

    scene bg schoolroom noon with fade_long
    pause 1

    $ show_hud()

    "６時間目が終わり荷物を片付けていると、入り口から私を呼ぶ声がした。"

    show nom gun nor lau at std_r with std_in

    voice get_voice_filename("nom")
    naomi "「せーんぱい？」"

    show rnk uni sur su1 rev at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あ、直未」"

    "声の主は直未だった。"

    "文化祭の日を考えると、そろそろ直未にはクラスメイトにコーヒーを教えられるようになってもらわないといけない。"

    "なので、今週は予定が許す限り店に来てもらうように約束をしていた。"

    "これまでは校門で待っていてくれたのだが、こうして教室まで来てくれるのは珍しい。"

    "そういえば私が脱落してしまったら、直未と過ごした事実もなかったことになってしまうのだろうか。"

    "きっとそうだ。だって『私が生きた時間』そのものがなかったことになってしまうのだから。"

    "だとすれば、この行動に意味はあるのだろうか――。"

    show nom gun hes sor with std_change

    voice get_voice_filename("nom")
    naomi "「先輩、どうしました？」"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめん、何でもない」"

    "このままじゃいけない。"

    "真央からもさっき同じことを聞かれたばかりなのだ。"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「お待たせ、もう行けるよ」"

    show mhr uni nor ser rev behind rnk at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「凛火……」"

    "立ち上がったところで、海晴が私を呼び止めた。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あれ？　どうしたの？」"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「日辻さんと帰りかい？」"






    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    menu:
        rinka "「今日もうちでコーヒー淹れる練習するからさ」"
        "「海晴も来る？」":

            $ flags_mhr_koukando += 1

            $ persistent.s5_1_seen = True
            $ grant_hear_all()
            jump f003.s1_1
        "「海晴はバイト？」":

            $ persistent.s5_2_seen = True
            $ grant_hear_all()
            jump f003.s1_2

label f003.s1_1:


    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk", 210)
    rinka "「もし暇なら、海晴も来る？」"

    "どうせお客さんは少ないのだし、たまにはうちで話すのもいいだろう。"

    "海晴は少し嬉しそうな顔をしたが、すぐに残念そうな顔に変わった。"

    show mhr uni sco sh2 rev with std_change

    voice get_voice_filename("mhr", 82)
    miharu "「せっかくのお誘いなんだけれど、今日もバイトがあるんだ」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……いや、代わりを見つければ間に合うかな……」"

    "海晴は顎を引いてスマホの電話帳を確認し始めた。"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「い、いやバイトなら仕方ないよ。うちに来ても話すだけだし。また今度だね」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「うん、また今度。必ずだ」"

    "海晴は切実そうな声で言った。"

    "無理もない。次の選定の時にどちらかが脱落する可能性だってあるのだ。"

    jump f003.s1_end

label f003.s1_2:


    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk", 212)
    rinka "「海晴は今日バイトがあるんだっけ？」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr", 85)
    miharu "「ああ、そうだよ。なるべく稼がないといけないからね」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「そっか、頑張ってね」"

    jump f003.s1_end


label f003.s1_end:

    "私は海晴に「じゃあね」と言ってから教室を出た。"





    python:
        set_info_time("evening")
        set_info_location("14")

    scene bg schoolgate noon with fade

    "暇だったら真央も来るところなのだが、今日も用事があるらしかった。"

    "二人でライオン館へと向かっている途中で、直未はぼそっと呟いた。"

    show nom gun hes sor at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「未島先輩に、申し訳ない事しちゃったかな」"

    show rnk uni arm nor rev at std_cl with std_in

    voice get_voice_filename("rnk", 214)
    rinka "「海晴に？」"

    show nom gun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「はい。未島先輩も、凛火先輩と話したかったんじゃないかなと思ったので」"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私も海晴と話したかったな。でもバイトって言ってたから、直未のせいじゃないよ」"

    show nom gun hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「いや、あの、そうじゃなくて……」"

    show rnk uni nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そういえばさ、今日は教室まで来てくれたよね？」"

    show nom gun que que with std_change

    voice get_voice_filename("nom")
    naomi "「ちょっとでも早く合流できればって思ったんですけど、明日からはやめときます」"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「え？　どうして？」"

    scene bg schoolgate noon large:
        align (0.65, 0.35)
    show nom gun hes shy up at std_c
    with wipe_rl

    "私が聞くと、直未は言葉に詰まっていた。"

    show nom gun har pin up with std_change_wait

    "言葉になっていない言葉をいくつか発した後、裏返った声で「何でもです！」と答えた。"

    "私には、珍しく直未が怒っているようにも見えた。"

    $ add_seen_chapter("3-1")










    python:
        set_info_scene("26")
        set_info_time("evening")
        set_info_location("14")

    stop music fadeout 2
    scene bg schoolgate noon with fade_longest
    play music audio.shadowmiharu
    pause 1

    $ show_hud()

    "獅子舞凛火と日辻直未が並んで歩く後姿を、校門に隠れて見ている少女がいた。"

    show mhr uni nor ser at std_cr with std_in

    "未島海晴。飴茶女子の特待生であり、背が高くスタイルもいい美人。"

    "完璧過ぎるせいで、周囲の生徒からは若干浮いている。"

    "そして今は頬を伝う涙のせいで余計に、関わらないようにと避けられていた。"

    "これが海晴でなければ明日の噂の種になるだろうが、あまりに奇妙な光景過ぎて、かえって誰も話題に上げたがらないだろう。"

    show mao uni nor che rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「みはるん、まだいたんだ」"

    "誰もが見ないふりをしていた海晴に話しかけたのは、クラスメイトの小熊真央だ。"

    "音も出さずに泣いている海晴を見ても、いつもの調子を崩さなかった。"

    "海晴は真央に声をかけられても、一点を見つめたままだった。"

    "真央は視線の先にある二つの背中を見て、僅かに頷いた。"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「なるほどねぇ」"

    show mhr uni pai cry with std_change

    voice get_voice_filename("mhr", 86)
    miharu "「ねえ、真央」"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「なぁに？」"

    show mhr uni pai ten with std_change

    voice get_voice_filename("mhr")
    miharu "「もし死ぬとしたら、ぼくは凛火に愛されて死にたい」"

    "海晴は震えた声でそう言った。"

    "その切実さに、作った大げささは一切なかった。真央は、海晴の言葉が零れ落ちた本心であることを知っていた。"

    "真央は動じることなく、普段と変わらない口調で答えた。"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「んじゃ、まだ死ねないよねぇ」"

    hide mao with std_out

    "真央は海晴の返事を聞くことなく、「じゃあねぇ」と手を振って去って行った。"

    "ここで一緒に帰ったり喫茶店で話を聞いたりカラオケで大声を出したりしても、海晴には意味がないことを真央は知っていた。"

    "だから、ただ一言だけ残して去って行った。"

    "海晴もまた、真央のことを冷たいとは思っていなかった。"

    "真央に対しては、何も感じていなかった。"

    "ただ海晴の心は、遠ざかっていく凛火の後姿だけに向いているのだから。"








    python:
        set_info_scene("27")
        set_info_location("04")

    stop music fadeout 2
    scene bg lion01 noon with fade_longest
    play music nichijo01
    pause 1

    $ show_hud()

    show nom gun hes sor rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「お邪魔しまーす……」"

    show rnk uni arm lie at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「私と来てるんだから、誰もいないよ」"

    scene bg lion01 noon large:
        subpixel True
        xalign 0.0
        yalign 0.5

        linear 120 xalign 1.0
    with dissolve

    "直未はお店のカウンターに荷物を置き、自宅から持ってきたエプロンをつけた。"

    "常連さんには文化祭のことを話していて、直未のことは「気にしない」と言ってもらっている。"

    "というわけで、直未にはコーヒーの淹れ方を教えるお礼として、１時間くらい洗い物など簡単な仕事を手伝ってもらっていた。"

    "私は大丈夫と言ったのだが、直未も「大丈夫です！」と言って引き下がらなかった。"

    "何が大丈夫か分からなかったが、せっかくの気持ちを無視しても悪いので、時間を決めて手伝ってもらうようにしていた。"

    "直未が来るときの大体の流れはこうだ。"

    "平日は開店するのが大体４時くらいなので、そこから１時間弱は空いているか、ほとんど人が来ない。"

    "その間に直未と一緒にコーヒーを淹れたり、本を見ながら豆のことを勉強したりし始める。後者は、文化祭には関係なくほとんど趣味だ。"

    "６時くらいになると仕事終わりの常連さんで少しだけ混むので、そこから１時間だけ手伝ってもらう。"

    "その後は適当な時間まで客席で勉強したり本を読んだり、たまにお喋りをしたりする。"

    "先週の放課後はこんな過ごし方だった。"

    scene bg lion01 noon with dissolve

    show rnk apr arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「さ、じゃ始めようか」"

    show nom gun que que rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「あ、先輩。ちょっといいでしょうか？」"

    "私が頷くと、直未は鞄から袋を取り出した。"

    "透明なビニール袋には、星やハートの形をしたクッキーが入っていた。"

    show rnk apr sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、可愛い」"

    show nom gun nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「その……お礼の気持ち、です。昨日は日曜日だったので、うちで焼いてみたんです」"

    "私は直未から手渡された袋を受け取って、赤色のリボンをほどいてみた。"

    "ふわっと、香ばしくて甘い匂いが広がった。"

    show nom gun que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「もし甘いものが嫌いじゃなかったら……コーヒーを淹れた後、一緒に食べてみてもらえませんか？」"

    show rnk apr nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「……もちろん。ありがとう、嬉しいな」"

    "準備をしている間に水が飛んだりしないように、リボンを結び直した。"

    show nom gun nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「えへへ、リボンは凛火先輩の好きな赤にしてみましたっ」"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「え？　何で知ってるの？」"

    show nom gun hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「分からないと思ったんですか、もう」"

    hide nom
    hide rnk
    with std_out

    "見えるところにクッキーを置き、私はお湯を沸かし始めた。"





    show rnk apr nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「うん。もうばっちりじゃないかな。みんなにも教えられるんじゃない？」"

    show nom gun nor sur rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「そんな……もう少し練習したいです。初心者向けの方法ですけど、わたし、おっちょこちょいなので」"

    "謙遜しているけれど、直未は確実に上達していると思った。集中していればドジもしないし、要領がいいんだなと感心していた。"

    "おばあちゃんが直未を直接教えれば、あっという間に私を追い越してしまう気がする。"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「じゃ、そろそろクッキー食べようか。ちょっと休憩しよ」"

    scene ecg girlstalkA3 nor with dissolve_long

    "いいのか悪いのか分からないが、今はお客さんもいなかったので、休憩をとることにした。"

    "コーヒーとクッキーをいつもの席に運ぶ。クッキーはソーサーの端に置く。"

    "私は綺麗な焼き色だなと思いながら、クッキーをかじった。"

    scene ecg girlstalkC1 anx with dissolve


    voice get_voice_filename("nom")
    naomi "「ごくり」"

    "直未は眼鏡の奥から不安げな目を向けている。"


    voice get_voice_filename("rnk")
    rinka "「……おいしい」"

    "こういう時、私は大げさに表現したりするのが苦手なので、これしか言えなかった。"

    "直未はぱぁっと目を輝かせ、にっこりと笑ってくれた。"

    show ecg girlstalkC1 lau with ecg_change


    voice get_voice_filename("nom")
    naomi "「嬉しいですっ」"

    "私はコーヒーを一口すすってから、再びクッキーを口に運んだ。"


    voice get_voice_filename("rnk")
    rinka "「あ、このクッキー……」"

    show ecg girlstalkC1 lau with ecg_change


    voice get_voice_filename("nom")
    naomi "「ど、どうしました？」"

    scene ecg girlstalkA3 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「すごくコーヒーに合う、ね。なんだろ、まろやかな感じっていうか……」"

    scene ecg girlstalkC1 lau with dissolve


    voice get_voice_filename("nom")
    naomi "「はいっ。実は凛火先輩の苦めのコーヒーに合うようにバターを多めにしてみたんです」"

    "直未はほっと息を吐いて、胸を撫で下ろす。"

    show ecg girlstalkC1 uwa with ecg_change


    voice get_voice_filename("nom")
    naomi "「喜んでもらえて、よかった……」"

    scene ecg girlstalkA3 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「私のために作ってもらって、喜ばないわけないでしょ、もう」"

    "私一人では多いので、直未と一緒にクッキーを食べていた。"

    "直未はお菓子作りが好きらしい。クッキー以外にも色々作るそうだが、一番自信あるのがクッキーだそうだ。"

    "そういえば、おばあちゃんもたまにクッキーを作っていた。でも、これはおばあちゃんの焼いたクッキーとは全然違う種類の味だ。"

    "直未の素直な性格が伝わってくるような、シンプルでまろやかな味。それでいて、悪い意味での手作り感は一切ない。"

    "袋の半分ほどいただいたところで、私はふと思いついたことがあった。"

    show ecg girlstalkA3 nor with ecg_change


    voice get_voice_filename("rnk")
    rinka "「私にも作り方、教えてもらえないかな？」"

    "お菓子のメニューが増えたら、お客さんにも喜んでもらえるはずだ。"

    "独学で料理を一から覚えるのに比べれば、直未にクッキーの焼き方を教わる方が現実的だ。"

    "それに何より、常連さんにもこの美味しいクッキーを食べて欲しいと思ったのだ。"

    "――だが、目を丸くしている直未をよそに、私の頭に選定のことがちらついた。"

    "せっかく教えてもらっても、私が脱落すれば、死ねば無駄になってしまう。"



    stop music fadeout 1
    show ecg girlstalkA3 ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「――ごめん、今の忘れて」"

    "私は死ぬかもしれないから――言えるはずはないけれど、喉まで出かけていた。"

    "誰かに打ち明ければ楽になるかもしれないと、きっと心のどこかで思っている。"



    play music audio.gimon
    scene ecg girlstalkC1 tro with dissolve


    voice get_voice_filename("nom")
    naomi "「どうしてですか？」"

    "直未はさっきまで輝かせていた表情を曇らせて、顔をぐい、と近付けてきた。"

    "無意識に考える仕草をしていた。自分でそのことに気付き、焦って答えた。"

    scene ecg girlstalkA3 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「……いつまでも直未の時間をもらうわけにもいかないしね。ずっとこうしてなんて――」"

    scene ecg girlstalkC1 anx with dissolve

    voice get_voice_filename("nom")
    naomi "「違いますよね、先輩。今のは本当じゃ、ない気がします」"


    voice get_voice_filename("rnk")
    rinka "「え……？」"

    show ecg girlstalkC1 anx with ecg_change


    voice get_voice_filename("nom")
    naomi "「そもそも、わたしからお願いしたことなんですから。それに、さっきの……。えっと、その……」"

    "直未は言葉に詰まってから、続けた。"

    show ecg girlstalkC1 tro with ecg_change


    voice get_voice_filename("nom")
    naomi "「ごめんなさい。うまく言葉にまとまりませんでした」"

    scene ecg girlstalkA3 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「ううん、大丈夫」"



    stop music fadeout 1
    scene ecg girlstalkC1 anx with dissolve

    voice get_voice_filename("nom")
    naomi "「……わたし、ずっとこうしてたいです」"

    "直未は下を向いて、ぼそりとそう呟いた。"

    show ecg girlstalkC1 tro with ecg_change

    voice get_voice_filename("nom")
    naomi "「ごめんなさい。最近わたし……ちょっと変で」"


    voice get_voice_filename("rnk")
    rinka "「慣れないことを手伝わせてたから、疲れさせたかも。今日は、帰る？」"

    show ecg girlstalkC1 anx with ecg_change

    voice get_voice_filename("nom")
    naomi "「そうじゃ……ないんです。そういうことでは……」"

    "小さくを息を吸ってから、直未は私に向き直った。"

    "その表情は、いつになく切迫していた。"

    show ecg girlstalkC1 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「失礼なことかもしれないですけれど……わたしの悩みを聞いてもらってもいいですか？」"

    scene ecg girlstalkA3 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「……うん」"


    play music audio.kinpaku
    scene ecg girlstalkC1 sad with dissolve


    voice get_voice_filename("nom")
    naomi "「ここ最近、嫌な夢を見るんです」"


    voice get_voice_filename("rnk")
    rinka "「……夢？」"

    show ecg girlstalkC1 ser with ecg_change

    voice get_voice_filename("nom")
    naomi "「はい。その夢は、最初は普通の夢から始まるんです。夢の中で、先輩とわたしが一緒に電車に乗って、帰っている途中で、話していて……」"

    show ecg girlstalkC1 tro with ecg_change

    voice get_voice_filename("nom")
    naomi "「そしたら、急に……電車が燃えて、火事になって……」"


    voice get_voice_filename("nom")
    naomi "「炎は広がって、熱くって、苦しくって……」"

    show ecg girlstalkC1 ser with ecg_change

    voice get_voice_filename("nom")
    naomi "「でも、先輩がわたしを守ってくれるんです。ただ先輩はそのまま、炎に巻き込まれて……」"

    "直未は、短く区切るようにしながら話す。"

    "その声は、徐々に切迫したものに変わっていく。"

    show ecg girlstalkC1 sad with ecg_change

    voice get_voice_filename("nom")
    naomi "「凛火先輩はそのまま、し、死んで、しまって……！」"


    play music audio.gimon
    scene ecg girlstalkA3 ser with dissolve

    voice get_voice_filename("rnk")
    rinka "「……いつからか、覚えてる？」"

    "下を向いたまま、直未は首を横に振り、答える。"

    scene ecg girlstalkC1 sad with dissolve

    voice get_voice_filename("nom")
    naomi "「もうはっきり覚えていないんです……けど……最初に見たのは、きっと、初めてこのお店に来た日だったかもしれません」"


    voice get_voice_filename("rnk")
    rinka "「どうして言ってくれなかったの？　いや、怒ってるとかじゃなくて……もしここに来るのが辛いとかなら……」"

    show ecg girlstalkC1 anx with ecg_change

    voice get_voice_filename("nom")
    naomi "「そんなことないです！　わたし、先輩と一緒にコーヒーを淹れる時間が好きです。先輩と話していれば、夢は夢だって割り切れるから」"

    show ecg girlstalkC1 sad with ecg_change

    voice get_voice_filename("nom")
    naomi "「でも、たとえ夢の中でだって先輩が死んじゃうところを見るなんて嫌です！　そんなこと思うはずがないのに……本当に……本当に……」"

    "言葉の終わり際は、声が震えていた。"

    "顔を見ると、見開いた目は潤んでいた。"

    show ecg girlstalkC1 sad with ecg_change

    voice get_voice_filename("nom")
    naomi "「何度も、何度も……この夢を見るんです」"

    scene ecg girlstalkA3 sur with dissolve

    voice get_voice_filename("rnk")
    rinka "「それって――」"

    "夢じゃない。"

    "直未が話しているのはきっと、「なかったこと」になっている私の死因だ。"

    "私はいくつもの疑問を浮かべたが、何より驚いていた。"

    "今までそんな様子を見せなかった直未が、まさか私ですら曖昧だった記憶を夢に見ているなんて――。"

    show ecg girlstalkA3 nor with ecg_change

    voice get_voice_filename("rnk")
    rinka "「辛かったね……大丈夫。大丈夫だよ。私はちゃんとここにいるから」"

    scene ecg girlstalkC1 sad with dissolve

    voice get_voice_filename("nom")
    naomi "「わたし、先輩ともっといろんなことがしたいです。一緒にクッキー焼いたり、また遊園地に行ったり。他にももっと、もっと……。だから――し、死んじゃったり、するわけないですよね……？」"

    scene ecg girlstalkA3 ser with dissolve

    "私は、頷くことができなかった。"

    "だって、選定がなければ私はすでに死んでしまっているのだから。"

    "電車で起きた火事は事実で、直未の夢もまた「なかったこと」になっただけの事実なのだ。"

    "選定の参加者の死を「なかったこと」にする世界の改変というのは、記憶を書き換えているということなのだろうか。"

    "原理も原因も分からない。"

    "だが、直未の記憶の中に私の死の瞬間が蓄積され、夢になって現れていることだけは事実だった。"

    scene ecg girlstalkC1 sad with dissolve


    voice get_voice_filename("nom")
    naomi "「返事……してください……」"


    voice get_voice_filename("rnk")
    rinka "「ごめん……」"

    show ecg girlstalkC1 tro with ecg_change


    voice get_voice_filename("nom")
    naomi "「ち、違います。ごめんなさい。先輩に謝って欲しいわけじゃなくて……その……でもやっぱり、さっきの質問に返事だけしてください」"

    show ecg girlstalkC1 uwa with ecg_change


    voice get_voice_filename("nom")
    naomi "「そうすれば、また同じ夢を見ても大丈夫な気がするから……」"

    scene ecg girlstalkA3 ser with dissolve

    voice get_voice_filename("rnk")
    rinka "「ごめん、私は――」"

    "何かを言いかけて、私は必死に抑えた。"

    "私は自分で思っている以上に、嘘をつくことが苦手なようだった。謝ることしかできなかったから。"

    "下を向いた私を覗き込むようにして、直未は上目遣いで私を見た。はっきりと、目頭に涙が溜まっていた。"

    "私が、泣かせたのだ。"



    stop music fadeout 1
    scene ecg girlstalkC1 ser with dissolve

    voice get_voice_filename("nom")
    naomi "「もし悩んでいることがあるなら、わたしにも話してください。ある日突然いなくなるなんて、絶対に……嫌です」"

    "涙目になりながらも、直未ははっきりとした口調で言った。"

    "その言葉に、胸が締め付けられるように痛くなった。"

    "ここで直未に選定のことを黙っていたら、きっと直未は理由なく見る私の死ぬ夢に苦しみ続けることになる。"

    "しかし話したところで、私が選定の参加者である事実は変わらない。"

    "もし私のために何かしたら、危険に巻き込まれるかもしれない。"

    "現段階ではどんな危険があるのかなんて分からないけれど、夢の世界で会った怖い目をする人たちと、関わらせたくない。"

    "何より――海晴も選定の参加者であること、どちらかしか生きられないことを話さなくてはいけなくなる。"

    "話さなければ、冷たくあしらえば、全部私だけが抱えればいいことなのだ。"
















    scene ecg girlstalkA3 ser with dissolve

    voice get_voice_filename("rnk", 243)
    rinka "「直未にね、聞いて欲しいことがあるんだ」"


    voice get_voice_filename("nom", 125)
    naomi "「えっ……」"

    show ecg girlstalkA3 nor with ecg_change

    voice get_voice_filename("rnk")
    rinka "「直未を余計不安にさせてしまうかも、いや、そもそも信じられないかもしれないけど、聞いてくれるかな？」"

    scene ecg girlstalkC1 ser with dissolve

    voice get_voice_filename("nom")
    naomi "「はい」"

    "直未は、私の問いかけに即答した。"

    play se "bell02"

    "私が「あのね」と話し始めようとしたとき、からんからんと入り口の鐘が鳴った。"

    scene ecg girlstalkA3 tro with dissolve

    voice get_voice_filename("rnk")
    rinka "「ごめん、続きは明日でいい？」"


    voice get_voice_filename("nom")
    naomi "「閉店するまで……待っていてもいいですか？」"

    show ecg girlstalkA3 nor with ecg_change

    voice get_voice_filename("rnk")
    rinka "「ううん、それは悪いから。少し気持ちも落ち着けた方がいいしね。大丈夫。明日の放課後、必ず話すよ」"

    scene ecg girlstalkC1 nor with dissolve

    voice get_voice_filename("nom")
    naomi "「分かりました」"

    "直未は深く頷いて、食器を下げてくれた。"



























    scene black with dissolve

    "私が仕事に戻ると、直未もすぐにお店を後にした。"

    "胸に渦巻くもやもやを振り払うため、私は仕事に集中することにした。"









    python:
        set_info_scene("28")
        set_info_date(5, 15, "tue")
        set_info_time("morning")
        set_info_location("08")

    scene black
    pause 2        
    scene bg schoolroom noon with dissolve_longest
    play music audio.miharu
    pause 1

    $ show_hud()

    show mhr uni nor nor at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「おはよう、凛火」"

    show rnk uni arm ama rev at std_cl with std_in

    voice get_voice_filename("rnk", 248)
    rinka "「あ、おはよう海晴」"

    "私が学校についた時、海晴はすでに登校していた。いつも通りの微笑で挨拶をしてから、少し会話をした。"








    python:
        set_info_time("evening")
        set_info_location("14")

    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show nom gun nor lau rev at std_cl with std_in

    voice get_voice_filename("nom", 129)
    naomi "「せーんぱいっ」"

    "私のことを見つけたのか、直未は校舎側に小走りで戻って来た。"

    show nom gun fal sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「わととっ」"

    show rnk uni cat ten at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あっ」"

    "直未は転びそうになったところで、何とか踏みとどまった。油断すると相変わらず、のようだ。"

    hide rnk
    hide nom
    with std_out

    "昨日話した通り、直未は校門で待っていた。"

    "わざわざうちの教室まで来てもらうと遠回りになるので、ここで集合した方が効率的ではある。"

    show rnk uni nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「お待たせ。気分を変えて話したいから、移動しよ。うちの近くにいいところがあるんだ」"

    show nom gun que que rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「ライオン館ではなくて……ですか？」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。ちょっとね。今日は天気もいいし」"

    show nom gun nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「はいっ！」"

    "直未と並んで、下校する生徒の流れに乗り、私たちは駅へ向かった。"

    $ set_info_location("17")








    stop music fadeout 1
    scene bg shinjukugyoen evening with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "新宿から地下鉄に乗り換えて２駅のところに、この公園はある。"

    "入場料はかかるけれど、ジュースを我慢すればいい程度のものだ。"

    "東京でも一、二を争う規模であり、元々は武家屋敷の庭園だったそうだ。"

    "その名残かは分からないが、日本・イギリス・フランスの庭園が再現されている。"

    "緑が多く、気分転換には丁度いい。観光客も多いが、平日では人が少なかった。"

    "私も子供の頃は頻繁に訪れていた。"

    "この中でも特にお気に入りの場所があった。"

    scene bg shinjukugyoen evening large at align(1.0, 1.0) with dissolve

    show nom gun que que rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「ここ……ですか？」"

    show rnk uni nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ね、いいでしょ？」"

    "御苑の中にある、小さなベンチ。"

    "私たちはそこに座った。一面に広がる緑の向こうには、時計台のようなビルが見えた。"

    "通信会社か何かの建物だったと思うが、新宿のビルの中でその特徴的な形は目立っている。"

    "風が吹くと、木々が揺れ、草木がさらさらと心地よい音を立てた。"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「あれ……」"

    "突然、妙な違和感があった。"

    "来たことがあるような、ないような、不思議な感覚だ。"

    "いや、間違いなくここには子供の頃に何度も来ている。"

    show nom gun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「……先輩？」"

    show rnk uni nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「ううん、ごめん。大丈夫」"

    "私は呼吸を整えてから、直未に選定のことを話す覚悟を決めた。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「じゃあ、えっと、どこから話せばいいんだろ……。まあ、いいや。信じられないような話なんだけど――」"






    stop music fadeout 1
    scene bg shinjukugyoen evening large at align(1.0, 1.0)
    show nom gun nor ser rev at std_cl
    show rnk uni nor que at std_cr
    with fade_long
    pause 1



    voice get_voice_filename("nom")
    naomi "「凛火……先輩……」"

    "一通り話し終えたとき、直未は辛そうな声でそう言った。"

    "直未は途中から涙ぐんでいたが、私は話すのを止めなかった。きっと、中途半端なところで打ち切られるなんて嫌なはずだ。"

    "私の考えは間違ってはいなかったようで、直未は終始真剣な表情で耳を傾けてくれていた。"


    play music audio.gimon

    show nom gun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「絶対、変だと思ったんです。あの本の話をした日、先輩は英語が全然できないはずなのに、英語で会話をしてたんですもん……。そっか、すでにあの日には、もう……」"

    show nom gun har pal rev with std_change

    voice get_voice_filename("nom")
    naomi "「先輩は生きて――絶対に生きているのに」"

    "直未は強い口調でそう言うと、私の手を握った。"

    "手の表面は冷たいけれど、じんわりと熱が伝わってくる。きっと直未にも私の体温は伝わっているはずだ。"

    "この熱が、生きている証。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。私は生きてる。でも、どうやらこっちが間違っているみたいなんだ」"

    show nom gun hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「わたし、先輩が何を抱えてるかなんて知らずに、勝手なことを言ってました」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「仕方がないよ。だって、話してなかったから」"

    "直未は結局、夢の世界のことを疑わなかった。"

    "きっと私の話した「死因」が、直未の夢とシンクロし過ぎていて、信じることしかできなかったのだろう。"

    "悪夢を何度も見てしまうという疑問に対する答えだったはずだから。解決は、していないけれど。"

    show nom gun hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「しかも未島先輩も同じ状況だなんて……」"

    "私は迷ったけれど、結局海晴のことも話していた。"

    "中途半端に隠しても意味がないというのが一つと、私の方も途中からは話して楽になりたい自分の気持ちに負けていた。"

    show nom gun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「それに……未島先輩はそんなことを言ってたんですね。そんな、覚悟が……」"

    "そんなこと、とは。海晴が私にした宣言であった。"

    "――私のために、命を捧げる。"

    show nom gun har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「未島先輩みたいなこと、わたしだったら……言えないです」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「私もそうだよ。海晴に死んで欲しくない。でも、自分が死ぬのも怖い。だから海晴を最後の一人にするために潔く死ぬなんて……言えない」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「自分がどうすればいいのか正解が分からないまま、もう２週間も経っちゃった」"

    show nom gun hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「……仕方がないと、思います」"


    stop music fadeout 1

    "再び風が吹いて、私たち二人の髪を揺らした。"

    "５月にしては、冷たい風だった。"

    "遠くには夕焼けが見えていた。"

    "青と橙が混ざっていくその境界線はまるで、揺れる心のようだった。"

    show nom gun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「未島先輩は……強いですね」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、そうだね」"

    "海晴は、私と違う。"

    "どっちつかずで踏み切らずにいる私とは、違う。"

    "もしかしたら、海晴はすでに最初に受け取ったカードを元に情報集めをしているのかもしれない。"

    "いや、きっとそうしている。海晴の表情は真剣だった。"

    "普段の学校でこそ鬼気迫る顔を見せないが、あれが海晴の覚悟だ。本やネットなど手を尽くして調べものをしているはずだ。"

    "――私の、ために。"

    "最近特にバイトで忙しいのも本当はバイトではなく――いや、そこまでは考え過ぎか。海晴がバイトを多く入れていたのは昔からだ。"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「聞いてくれてありがとね。少し気が楽になったよ」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「どうすればいいのかなんてまだ分からないけど、しばらくはまたこのまま過ごしてみる」"

    "よしと言ってから、私は立ち上がろうとした。"

    "その時、直未は私の袖をつまんで引き留めた。"

    show nom gun har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「あと５分だけ、待ってください。わたし、決めたことがあります」"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「決めた……こと？」"

    "聞き返すと、直未は強く２回頷いた。"


    play music audio.thebonds
    scene ecg naomidetermination ser with dissolve_long


    voice get_voice_filename("nom")
    naomi "「わたし、凛火先輩を支えたいです」"


    voice get_voice_filename("nom")
    naomi "「このままじゃ……絶対駄目です。凛火先輩の気持ちにはなれないけれど、わたしの無責任な意見かもしれないですけれど」"


    voice get_voice_filename("nom")
    naomi "「逃げてるだけじゃ……いけないと思います」"


    voice get_voice_filename("rnk")
    rinka "「逃げてる……だけ」"

    "踏み切らないのではない。逃げている。"

    "直未ははっきりとそう言った。"

    "空っぽな荒野に、雷が落ちたような気持ちだった。"

    "私は――逃げていたのだ。生きることからも、死ぬことからも。"

    "気付けば、空は一面が橙色に染まっていた。"


    voice get_voice_filename("nom")
    naomi "「調べものくらいなら、わたしは手伝えます。顔が知られていないから、参加者に直接会うこともできます」"


    voice get_voice_filename("nom")
    naomi "「何より、先輩が一人じゃ支えきれない物を……一緒に背負う事も……できます」"


    voice get_voice_filename("rnk")
    "「直未……」"

    "直未ははっきりと言い切った。強い意志の言葉だと、声を聞くだけで分かった。"


    voice get_voice_filename("nom")
    naomi "「最後の瞬間には、先輩たちのどちらかが生き残るのか悩まないといけないかもしれません。でも今のままじゃきっと、その前に……」"


    scene bg shinjukugyoen evening large:
        zoom 1.5
        align (0.9, 0.9)
    show rnk uni arm ama up at std_c
    with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「ね、直未。私も今更自覚しちゃった気持ちがあるんだ」"

    "直未は私に向き直り、話の続きを待つ仕草を見せた。"

    "逃げていると指摘されて、ようやく見つけた本当の恐怖のこと。"

    show rnk uni nor smi up with std_change

    voice get_voice_filename("rnk")
    rinka "「私、怖いんだ。このまま生き残るには、海晴だけじゃなくて他の人も脱落させないといけない」"

    show rnk uni nor que up with std_change

    voice get_voice_filename("rnk")
    rinka "「自分が人の命を踏み台にしてまで生きるべき存在かなんて、分からないんだ」"

    show rnk uni arm lie up with std_change

    voice get_voice_filename("rnk")
    rinka "「自分の≪未練≫さえ曖昧なままだし……ね」"

    "私は夢の世界で、間もなく指名されるという人たちの表情を見ていた。"

    "後悔や諦めという言葉だけでは足りない、無力な表情。"

    "あれが、未練半ばで死ぬことになってしまった人の顔なのだ。"

    "そんな想いがあるかも分からない私が、彼らの命を踏みにじっていいのだろうか。疑問になる、までもない。"

    scene ecg naomidetermination ser with dissolve_long


    voice get_voice_filename("nom")
    naomi "「未島先輩やわたしが、凛火先輩に生きていて欲しいって気持ちじゃ足りませんか？」"


    voice get_voice_filename("nom")
    naomi "「わたしだって、他の人を脱落させて生きることが正しいかどうかは分かりません。でも、先輩が死んじゃうなんて絶対に、絶対に嫌なんです！」"


    voice get_voice_filename("nom")
    naomi "「だから、もし他の人を脱落させることが罪だとするなら、それを背負うのが恐いなら……わたしに半分、分けてください」"


    voice get_voice_filename("rnk")
    naomi "「直未……どうしてそこまで言ってくれるの？」"

    "私の、ために。"


    voice get_voice_filename("nom")
    naomi "「本来の運命で先輩は、自分の命よりもわたしを優先してくれた。口で軽々しく言えないだけで、先輩はきっとそういう人なんです。ううん、でも、そんなの関係ないです」"


    voice get_voice_filename("nom")
    naomi "「凛火先輩だから――他に理由は思いつきません」"

    show ecg naomidetermination cry with ecg_change


    voice get_voice_filename("nom")
    naomi "「あれっ……おかしいな……。どうして、涙が……これは、その、違うんですっ……」"

    "直未は、空の向こう側を見ながらそう言った。目に溜まった涙は、今にも零れ落ちそうなところで堪えていた。"

    "こんな時におかしいけれど、空は広いな、と思っていた。"

    "直未は私のコーヒーをおいしいって言ってくれた。"

    "私が逃げていることに気付かせてくれた。"

    "もっと、大事なことにも。"



    scene bg shinjukugyoen evening large at align(1.0, 1.0)
    show rnk uni nor nor at std_cr
    with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「危ないことは、しないでね」"

    show nom gun har ser rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「えっ……」"

    "直未の瞳からは、すでに小粒の涙がこぼれ始めていた。"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「私はこの期間、≪選定からの脱落≫以外で死んじゃうことはないらしいけど、直未は違う」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「だから、危険なことはなし」"

    show nom gun har nor with std_change_wait

    "直未はぐっと唇を噛み締めたまま黙って、頷いた。"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「その上で、私からお願いさせて。≪女神の選定≫で私が脱落しないように、協力してください」"

    show nom gun har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「先輩……なんで敬語なんですか……」"

    "私が直未に右手を差し出すと、直未は私の手を握り返してくれた。"

    "そして、緊張がほどけたように笑顔になった。"

    "頬には涙の筋を伝わせたままで。"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「泣き虫だね、直未は」"

    show nom gun har ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「先輩も……こういう時は泣いていいんですよ？」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「からかわないでよ、もう」"

    "直未は笑っていたけれど、まだ涙は止まっていなかった。"

    "丁度、閉園時間を告げるアナウンスが響いた。"

    "直未とは「また明日」と挨拶をして、私は家へ帰った。"




    python:
        set_info_scene("29")
        set_info_time("night")
        set_info_location("18")




    stop music fadeout 1
    scene bg lion02 night with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "直未が帰宅した後、私はライオン館に戻って少しだけお店を開けた。"

    "休憩時間を使ってチャットでやり取りをし、明日はお店を休みにして情報の整理をすることに決めた。"

    "新聞などの資料が読めるので図書館がいいとも思ったが、今の状況では何を調べればいいのかも分からないので、一旦はうちに集まることにした。"

    "図書館ではうるさくするわけにはいかないが、うちならば大丈夫だ。"

    "直未には、他の人には話さないようにお願いをした。"

    "大切な友人である真央に話すかも迷ったが、やめた。真央は直未よりもずっと海晴と付き合いが長い。"

    "きっと背負う物が違い過ぎる。今はできるだけ三人の日常を崩したくはなかったのだ。"

    scene bg lion02 night large at align(0.0, 0.5)
    show rnk uni nor nor up rev at std_cl
    with dissolve

    voice get_voice_filename("rnk")
    rinka "「……ふぅ」"

    "これまでのことを振り返りながら、私は閉店準備をしていた。"

    "閉店間際はお客さんがほとんど来なかったので、店内の片付けは大方終えている。"

    "店外の片付けは、看板や一部の植木を室内に入れたり、ゴミを出したりという仕事などがある。"

    "扉にちょっとした汚れがあり、気になったのでしゃがんで拭いていた。"

    "こちらに向かって来る足音がした。"

    "夜とはいえ珍しいことではないので気に留めていなかったが、足音はライオン館の前で止まった。"

    show rnk uni cat sma up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あの、もう閉店で……」"

    "お客さんかと思い、私は振り返ってそう告げようとした。"

    "だが、言葉は足音の主である女性を見たときに止まってしまった。"

    "私が立ち上がったのと、その相手が私の肩を掴み、ライオン館の扉に押し付けるのはほとんど同時であった。"


    play music audio.kinpaku
    show kik sta ten cla up at std_r, xoffset(550) with None

    show layer master:
        easein 0.3 xoffset -450

    pause 0.3
    show layer master at xoffset(-450)



    voice get_voice_filename("kik")
    keiko_unk1 "「あなたが獅子舞凛火さんね！」"

    python:
        gameinfo_cardbook_kik_unlocked = True
        add_character_cards("kik", ["1_name"])

    "女性は早口で、しかも大声で言った。喉が裂けそうな辛そうな声だった。"

    "彼女の形相は必死というよりも、余裕がないという印象だった。"

    "だからこそ、私は怒鳴られてもかえって冷静になることができた。"

    scene bg lion02 night
    show kik sta ten cla at std_cr
    show rnk uni arm vig rev at std_cl
    with wipe_lr

    voice get_voice_filename("rnk")
    rinka "「あなた……“Ⅷ”の人ですね？」"

    "質問には答えず、私は訊ねた。"

    "名前は知らないけれど、顔だけは知っている。彼女は夢の世界で見たことのある女性だったのだ。"

    "冷静にはなれたが、緊張はあった。額のあたりに、嫌な汗が滲む。"

    "下手なことは言ってはいけない。自分の発言の何が情報のヒントになるのか分からないからだ。"

    show kik sta ten cla with std_change


    voice get_voice_filename("kik")
    keiko_num "「どうなのっ！」"

    "女性は扉に手をつき、さらに言い寄ってきた。"

    "恐い、とは思わなった。"

    "余裕がないのも無理はないと思い出したからだ。"

    "私のことを知らないからこそ、確証がないからこそ、こうして問い詰めるしかできないのだろう。"

    "この女性は、最初の選定の時にⅫの男性に名前を知られている。彼が脱落させた女性から得たカードが、≪Ⅷ・氏名≫だったはずだ。"

    show kik sta ten cla with std_change


    voice get_voice_filename("kik")
    keiko_num "「答えなさいよ！　私はあなたのカードを持っているの！　だからあなたが獅子舞凛火だってことは知ってるのよ！」"

    "きっと、この人がⅪやⅫの人だったら落ち着いてはいられなかったはずだ。"

    "心のどこかでああいう人たちと競わなければいけないと怖がっていたからこそ、この女性に対して怯まずにいられる。"

    "彼女は、どこにでもいそうな細身の女性だったのだ。綺麗な顔立ちだが、とても疲れている。睡眠時間が足りていないのが明白だった。"

    "服装は病院着で、ストールのようなものをまとっている。"

    show kik sta ten imp with std_change


    voice get_voice_filename("kik")
    keiko_num "「ねえ！　あなたの死因は何？　未練は何？」"

    "私が黙っていると、女性はさらに激しい剣幕になった。"

    show kik sta ten cla with std_change


    voice get_voice_filename("kik")
    keiko_num "「自殺？　病気？　進学？　恋愛？　何よ！」"

    show rnk uni ang an2 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと落ち着いてください！」"

    "痺れを切らして、私は女性の肩に手を置き、引き離そうとした。"

    "だが勢いがつき過ぎてしまい、自分の体ごと押し倒してしまう形になった。"

    hide kik with DissolveMoveOut(DELAY_NORMAL, yoffset(STD_SLIDE_OFFSET), easein)
    play se "body_fall01"
    with quake_fast

    "女性はコンクリートの上に尻餅をついた。"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あっ……ごめん……なさい」"

    show kik sta wea bad at std_cr with std_in


    voice get_voice_filename("kik")
    keiko_num "「…………ごほっ」"

    "私は反射的に謝っていた。"

    "相手は選定の参加者――言ってしまえば敵かもしれないのに。"

    show rnk uni nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「大丈夫……ですか？」"

    "私は彼女に恐る恐る訊ねたが、返事はなかった。"

    "女性は私に押し倒されたままの格好で下を向き、ぶつぶつと何か口にしている。"

    show kik sta wea bad with std_change


    voice get_voice_filename("kik")
    keiko_num "「…………私がっ…………」"

    "女性はそのまま、床に倒れ込んでしまった。"

    show rnk uni cat sma rev with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ、あっ、だ、大丈夫ですか？」"

    show rnk uni sur su2 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「き、救急車……っ！」"

    show kik sta wea bad with std_change


    voice get_voice_filename("kik")
    keiko_num "「だ……大丈夫だから…………救急車はやめ……帰れま……す……から……」"

    show rnk uni sur su1 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「いやっ、だって明らかに大丈夫じゃないですし……」"

    show kik sta wea sad with std_change


    voice get_voice_filename("kik")
    keiko_num "「き……うしゃ……は……」"

    hide kik with std_out

    "女性の言葉は、そこで途切れてしまった。"

    "小さく息があり、その音は意識を失ってしまったというより眠っているようだった。"

    "倒れた時にめくれた病院着のすそに、病院の名前が書かれていた。ここから徒歩で１０分くらいのところにある病院だ。"

    show rnk uni arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あー、もう……仕方ないか」"

    "救急車には乗りたくない事情があるみたいなのだが、いつまでもここに放置するわけにもいかない。"

    "幸い女性はかなり軽そうだし、私は彼女をおんぶすることにした。"

    show rnk uni arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「思ったよりきついな……」"

    "店の鍵を閉めてから、私は遊歩道を歩き始めた。"




    $ set_info_location("19")






    stop music fadeout 1
    scene bg hospitallounge on with fade_long
    pause 1

    $ show_hud()

    "病院についた時、居合わせた看護師さんに奇特な目で見られてしまった。"

    "無理もないだろう。夜に女子高生が息を荒げて女性をおんぶして病院に来たのだから。"

    "女性はすぐに看護師さんが連れて行った。やはりこの病院に入院しているらしい。"


    play music audio.gimon

    "私はその時、彼女の名前を聞いてしまった。"

    "{rb}瓶淵{/rb}{rt}かめぶち{/rt}{rb}桂子{/rb}{rt}けいこ{/rt}さん。"

    "元々体が弱いそうで、子供を産んだ後からずっと体調を崩してしまったらしい。"

    "それ以上は聞けなかったし、教えてもくれないのだろう。"

    "ここまで教えてくれたのは、一応私が助けたのに彼女が見ず知らずの人のままでは失礼だと思ったからか。"

    show rnk uni nor que at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「そういえば、カードって」"

    "現実世界で情報を手に入れた時に生まれる、とパルカは言っていた。"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「そっか、本」"

    "きっと、あの本が手元にないからだろう。"

    "大切な物と分かってはいるが、かさばるので置いて来てしまった。"

    "どちらにせよ面会時間もとっくに過ぎているし、これ以上病院にいるわけにもいかない。"

    "あの人――桂子さんのことは気になるけれど、私は一旦戻ることにした。"








    $ set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()



    "自室に戻った私は寝る準備を済ませてから、カードブックを机に置き、座った。"
    scene bg myroom night large at align(0.5, 0.3)
    show rnk paj sur su2 up at std_c
    with dissolve

    voice get_voice_filename("rnk")
    rinka "「何か、光ってるんだけど……」"

    scene ecg cardbook bli with dissolve_long

    "本の内側が光っているのか、閉じているところの僅かな隙間から光が漏れ出していた。"

    "本がひとりでに光るなど、言うまでもなく、初めて見た光景だ。ただし、現実世界では。"

    "私は意を決して、本を開いた。"



    scene bg myroom night large at align(0.5, 0.3)
    show rnk paj sur su2 up at std_c
    with wfade_normal

    voice get_voice_filename("rnk")
    rinka "「わっ」"

    "本を開いた瞬間、光は本の上から空中に移動した。"

    show rnk paj paj su1 up with std_change

    voice get_voice_filename("rnk")
    rinka "「ち、ちょっと……！」"

    "焦る私をよそに、光は机から50センチくらい上のところで集束し始めた。"

    "そのまましばらくして、光が無形から長方形に変わる。カードの形だ。"

    "カードの形に変わってすぐに、光は消える。"

    scene ecg cardbook op3 with dissolve_long

    "瞬間、空中にはカードが現れた。支えを失い、カードは音を立てずに本の上に落ちた。"

    python:
        add_character_cards("rnk", ["8_name"])
        add_character_cards("aln", ["8_name"])
        add_character_cards("kik", ["8_name"])


    voice get_voice_filename("rnk")
    rinka "「こうやって作られるんだ……カード……」"

    "まさか現実で超常現象が起こるとは驚きだった。"

    "似たような現象は夢の世界で見たとはいえ、自分の部屋で見るとまた違った驚きがある。"


    scene bg myroom night with dissolve_long

    "私は現れたカードを手に取ってみた。"

    "形や材質、模様は他のものと同じ。"

    "唯一異なっているのはそこに書かれている情報。"

    "――Ⅷ・氏名・瓶淵桂子。"

    "私が病院に連れて行った桂子さんの情報だ。"

    "死因や未練は、まだ分からない。"

    scene bg myroom night large at align(0.5, 0.3)
    show rnk paj arm vig up
    with dissolve

    voice get_voice_filename("rnk")
    rinka "「でも出産してから入院したって言ってたよね。だったら……」"

    "間違いなく、出産が関係ある。"

    "出産に関係があることと言えば――。"

    show rnk paj arm sad up with std_change

    voice get_voice_filename("rnk")
    rinka "「いたっ」"

    "突然、頭が痛くなる。"

    "原因はすぐに分かった。"

    "桂子さんの必死な顔が脳裏によぎったからだ。"

    "彼女にはあれだけ激しい剣幕になるほどの未練がある。私がやっているのは、それを切り捨てるための行動だ。"

    "漠然と桂子さんが死ぬ瞬間を思い描いてしまったのだ。想像すればするほど、頭痛が重くなる。"

    "直未の言葉を思い出す。直未は一緒に背負ってくれると言った。"

    "私一人じゃ、まだ、その業は負えない。"

    "自分の弱さを、自分自身に教えられた。"

    "電気を消して、私は眠ることにした。"

    $ add_seen_chapter("3-2")



    python:
        set_info_scene("30")
        set_info_date(5, 16, "wed")
        set_info_time("morning")
        set_info_location("08")








    stop music fadeout 2
    scene bg schoolroom noon with fade_longest
    play music audio.nichijo02
    pause 1

    $ show_hud()

    show mao uni nor lau rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「おっすりーたん」"

    show rnk uni nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あ、真央。おはよう」"

    "登校した私の目にふと、何食わぬ顔で授業の準備をしている海晴の姿が映った。"

    "昨日自覚した自分の弱さが思い出され、私は真央に唐突に変なことを言ってしまった。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴ってさ。強いよね」"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「みはるんが？　うーん、逆だよ、きっと」"

    "真央は少しだけトーンを落とし、小声でそう言った。"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ？」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「んじゃ、今日も一日頑張りましょ～」"

    "聞き返した私の言葉を上書きするように、真央はいつもの調子で言ってみせた。"







    python:
        set_info_time("evening")
        set_info_location("04")



    stop music fadeout 1
    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "放課後に直未と合流した私たちは、まず図書館へ向かってからライオン館へ戻った。"

    "図書館は幸いにも、私の家から５分くらいのところにある。昨日行った病院までの通り道だ。"

    "下校途中に、昨日あったことをざっくりと説明したのだ。直未はまず心配してくれた。"

    "私自身には特に何もなくむしろ桂子さんの方が大変そうだったことを伝えると、直未は複雑な表情を浮かべたあと、安堵のため息をついた。"

    "図書館で借りたのは、妊婦さんに関する本だった。"

    "まるでワケありの女子高生みたいで借りるのを躊躇ったが、そんなことを言っている場合ではなかった。"

    "ライオン館のテーブルに、借りてきた本を広げた。"



    play music audio.investigation
    scene ecg girlstalkC2 smi with dissolve_long


    voice get_voice_filename("nom")
    naomi "「じゃあ……この本でまずは≪死因≫になりそうな病気や症例がないかを調べてみましょう」"

    scene ecg girlstalkA4 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「……うん」"

    "直未は平坦な声で宣言をした。"

    "努めてそうしているのが分かった。人の死因を探るなど、警察や探偵でもなければしない。"

    "人のプライベートを無理に暴くみたいで、気持ち悪くもある。昨晩はそれで頭痛もあらわれた。"

    "ましてや桂子さんは現在進行形で生きているのだ。"

    "私は近くにあった本を手に取った。カードブックよりも薄いが、開いてみると文字がぎっしりだ。"

    "医療的な知識がないのにいきなりこの本は難しいだろう。"

    "別の本に手を伸ばし、開いてみる。これも同じように、文字ばっかりだ。"

    "私は漫画以外には小説くらいしか本を読まないので、できればもう少し簡単な本があると嬉しいのだけれど……。"

    "そう思いながら本を手にとっては戻すということを繰り返していた。"

    scene ecg girlstalkC2 nor with dissolve


    voice get_voice_filename("nom")
    naomi "「あの……先輩？」"


    voice get_voice_filename("rnk")
    rinka "「えっ、どうしたの？」"

    show ecg girlstalkC2 uwa with ecg_change


    voice get_voice_filename("nom")
    naomi "「もしかして本、苦手ですか？」"

    "直未は目から下を本で隠したような状態で、じっと私の方を見た。"

    scene ecg girlstalkA4 su1 with dissolve

    voice get_voice_filename("rnk")
    rinka "「苦手ってわけじゃないんだけど……。難しくない？」"

    scene ecg girlstalkC2 nor with dissolve


    voice get_voice_filename("nom")
    naomi "「もー、そう思ってたら言ってくださいよぅ。もう少し簡単な本もありそうでしたから、そっちも借りてきたのに……」"

    "この発言からも分かるように、本選びは直未に任せていた。本が好きだというのは知っていたから、任せた方がよいと思ったのだ。"

    show ecg girlstalkC2 anx with ecg_change


    voice get_voice_filename("nom")
    naomi "「先輩ってやっぱり勉強は苦手です？」"

    "私は一呼吸躊躇ってから、頷いた。"

    "自分では苦手意識はあまりないのだが、ここで見栄を張っても仕方がない。結果が伴っていないので、苦手ということだろう。"

    scene ecg girlstalkA4 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「でも、頑張ってみる。自分のことだもんね」"

    "私はもう一度本を手に取って、目次を開いた。"

    "直未は、また本で自分の顔を隠してしまった。ちらりと見えた彼女は、眼鏡の奥の大きな瞳で食い入るように本に目を通していた。"



    scene ecg girlstalkA4 nor with fade_long
    pause 1


    "２時間ほどしたところで、集中力が切れたのが分かった。"


    voice get_voice_filename("rnk")
    rinka "「ちょっと休憩しよっか」"

    scene ecg girlstalkC2 ser with dissolve

    voice get_voice_filename("nom")
    naomi "「…………」"


    voice get_voice_filename("rnk")
    rinka "「あのー、直未さん？」"

    scene ecg girlstalkA4 sur with dissolve


    voice get_voice_filename("nom")
    naomi "「ひゃっ、何ですか？」"


    voice get_voice_filename("rnk")
    rinka "「……すごい集中力だね。ちょっと休憩しよっか」"

    scene ecg girlstalkC2 smi with dissolve


    voice get_voice_filename("nom")
    naomi "「はい、そうですね」"

    "私が言うと、直未は本を閉じた。どうやらこの本も読み終わったらしい。全部で３冊を確認し終えたことになる。"

    "私はまだ１冊目の途中なので、やはり普段から読書していると速度が全然違うようだ。"

    scene ecg girlstalkC3 nor with dissolve

    "私はコーヒーを淹れて、テーブルへ運んだ。"

    show ecg girlstalkC3 lau with ecg_change


    voice get_voice_filename("nom")
    naomi "「ありがとうございます！　そういえば、久しぶりな気がします。先輩のコーヒー」"


    voice get_voice_filename("rnk")
    rinka "「あ、そうかもね」"

    "最近は、直未に教えていることが多かった。必然的に直未にコーヒーを淹れる機会は減っていた。"

    "直未は美味しそうにコーヒーを飲んでくれる。その顔を見ることができて嬉しかった。"

    scene ecg girlstalkA5 que with dissolve


    voice get_voice_filename("rnk")
    rinka "「それでさ、何か分かったことある？」"

    "私も本を読んで分かったことはある。"

    "だが、まずは直未の意見を聞きたかった。"

    scene ecg girlstalkC3 nor with dissolve


    voice get_voice_filename("nom")
    naomi "「はい。まず分かったのは……妊婦さんの出産時の死亡率はすごく低いってことですね」"

    "これは、私が読んだ本にも書いてあった。"

    "2014年の資料では、10万人に3人程の母親が亡くなっているらしい。"

    "桂子さんは20代か30代に見えたし、30代だとしても0.003％以下の割合だ。"

    "どれくらい低いかと言うと、交通事故に遭う確率よりもずっと低い。"

    "私にもいつか関わってくることなので、文字は細かかったが興味を持って読むことができていた。"

    "確認したところ、直未も同じような資料を見ていた。まるで答え合わせだ。"


    voice get_voice_filename("rnk")
    rinka "「でも、それだけ例が少ないなら原因の予想がつきやすいんじゃないのかな？」"

    show ecg girlstalkC3 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「わたしも……そう思います。ただ気になっているのは、どこまで詳細な情報がカード化するのに必要なのかなってことです」"


    voice get_voice_filename("rnk")
    rinka "「私が持っている死因のカードに書かれているのが≪焼死≫ってだけだから、きっとそれくらいのざっくりさでいいんだと思う」"

    show ecg girlstalkC3 nor with ecg_change


    voice get_voice_filename("nom")
    naomi "「なるほど……。でも、先輩の話だと概念が実存になるって言ってましたよね？」"


    voice get_voice_filename("rnk")
    rinka "「うん。私もよく意味が分かってないんだけどさ」"

    show ecg girlstalkC3 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「だとすれば、情報がカードになるというのは、先輩がちゃんと概念として情報を持っていないといけないと思うんです」"

    "直未の言っていることがややこしくなってきたので、私は頭の中で一度整理することにした。"

    "情報という概念がカードという実存になる。ここまではパルカの言っていたそのままだ。"

    "概念として情報を持つというのはどういう意味だろう。"

    show ecg girlstalkC3 uwa with ecg_change


    voice get_voice_filename("nom")
    naomi "「すみません、分かりにくい言い方になっちゃいました」"

    show ecg girlstalkC3 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「先輩の中で論理的に行き着いた結論なのかって意味です。つまり、先輩が日常会話の中で何気なく言ったことでも誰かの≪死因≫や≪未練≫に該当していたらカードになるのか……」"

    show ecg girlstalkC3 nor with ecg_change


    voice get_voice_filename("nom")
    naomi "「それとも、例えば『この人はいつ症状が悪化したから死因はこれだろう』って証拠みたいなものを先輩が把握していないといけないのかってことです」"

    scene ecg girlstalkA5 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「そっか、なるほどね」"

    "私は少しこの２週間を思い出してみた。"

    "口数が多い方ではないと思うけれど、それでも多くの会話をしている。"

    "その中に死因や未練に該当するものもあるはずだから、私は情報を持っているはずだ。"

    "しかし、カードを新しく手に入れたのは昨日が初めてだ。"

    "ということは、直未の言う後者がカードの作られるルールなんだと思う。"

    scene ecg girlstalkC3 nor with dissolve


    voice get_voice_filename("nom")
    naomi "「やっぱりそうですよね。極端な話ですけれど、辞書を最初から最後まで読めば大体の人は≪死因≫も≪未練≫も手に入れられることになっちゃいますもんね」"


    voice get_voice_filename("rnk")
    rinka "「あんまりやりたくないけどね……」"

    show ecg girlstalkC3 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「命がかかっているなら、やるかもしれません」"

    scene ecg girlstalkA5 sur with dissolve

    "直未が言って、私は桂子さんのあの必死な顔を思い出した。"

    "きっと彼女には強い執念のようなものがある。私はそれを感じていた。"

    "それでカードを手に入れられるのであれば、桂子さんはそれこそ何冊も辞書や医学書を読むはずだ。"

    scene ecg girlstalkC3 ser with dissolve


    voice get_voice_filename("nom")
    naomi "「それに、先輩の≪死因≫のカードが作られないのも、同じ原因かもしれません。先輩の曖昧な記憶やわたしのぼんやりした夢の他に、もっと何かが……」"

    "私の≪死因≫を明らかにするための、忘れてしまっている真実。私が死に至るまでの流れ。"

    "だが、ここで考えても思い出せる気配はない。現に今日まで思い出せていないと言うことは、他のきっかけが必要なのだろう。"

    "私は直未に話を戻すよう促した。"

    show ecg girlstalkC3 anx with ecg_change


    voice get_voice_filename("nom")
    naomi "「そうですね、えっと……私の意見ですけれど、一般的な『失血死』というのが妊婦さんの――瓶淵さんの死因である可能性が高いと思います」"


    voice get_voice_filename("rnk")
    rinka "「でも、それじゃ足りないんだね。どうしてそうなのか、理由や筋道を私がちゃんと理解していないといけない」"

    "現に、今カードは現れていなかった。"

    show ecg girlstalkC3 tro with ecg_change


    voice get_voice_filename("nom")
    naomi "「ここで調べてるだけだと足りなそうですね」"


    voice get_voice_filename("rnk")
    rinka "「私がお見舞いに行ったら……まあ拒否されちゃうよね」"

    "黒髪に金のメッシュが入っているというのは目立つという自覚はあった。"

    scene ecg girlstalkA5 su1 with dissolve


    voice get_voice_filename("rnk")
    rinka "「あっ」"


    voice get_voice_filename("nom")
    naomi "「どうしました？」"

    show ecg girlstalkA5 smi with ecg_change

    voice get_voice_filename("rnk")
    rinka "「休憩するって言ってたけど、これじゃ休憩にならないね。でもさ、直未……頼りになるね」"

    scene ecg girlstalkC3 smi with dissolve


    voice get_voice_filename("nom")
    naomi "「えへへ、それならよかったです」"

    "とはいえ、無理しているというのも直未の言葉の端々から伝わってきた。"

    "普段より緊張しているようにも聞こえるし、あえて淡々と喋っているようにも聞こえる。"

    "私もそうだから、分かる。人が死ぬ、死因を探っているのだ。にこにこは話せない。"

    "しかし、一人で考えている時と異なり頭痛はなかった。直未がこの重荷を一緒に支えてくれると思うだけで、気が楽になる。"

    "問題は、どうやって桂子さんの死因を深いところまで探るか、だ。"

    show ecg girlstalkC3 nor with ecg_change


    voice get_voice_filename("nom")
    naomi "「あ、わたしお菓子持って来たんでした。今日は手作りじゃないですけど……」"

    "直未が取り出したのはチョコレートだ。一粒もらうと、じんわりと甘さが全身に広がった。思わず震えそうだ。"


    voice get_voice_filename("rnk")
    rinka "「糖分が……染みるね」"





    voice get_voice_filename("nom")
    naomi "「脳の栄養は糖分って言いますもんね。わたしが勉強してると、お母さんがよく……あ」"

    scene ecg girlstalkA5 que with dissolve


    voice get_voice_filename("rnk")
    rinka "「どうしたの？」"

    scene ecg girlstalkC3 ser with dissolve


    voice get_voice_filename("nom")
    naomi "「単純なことでした。わたしが、桂子さんの家族に会えばいいんです」"


    voice get_voice_filename("rnk")
    rinka "「直未が？　それって……危ないことじゃない？」"


    voice get_voice_filename("nom")
    naomi "「はい。でも、わたしが会いに行く分には、本人ならともかく家族ならなんとかごまかせるかもしれません。先輩が桂子さんを病院に運んだ件があるので、念のため、制服は着ないで行きます」"


    voice get_voice_filename("rnk")
    rinka "「でもさ、口止めとかされてるんじゃないの？」"

    show ecg girlstalkC3 nor with ecg_change


    voice get_voice_filename("nom")
    naomi "「夢の世界の話って大人がそのまま大人に話せはしないと思うんです。オブラートに包んだ言い方をしてる……だから、完璧じゃない気がします」"

    "直未の言葉には一理あった。"

    "私こそ直未に全て打ち明けたけれど、相手が学校の先生だったら信じてもらえると思わないし、話せない。"

    "おばあちゃんだったら大丈夫かもしれないけれど、もし両親がいたら話せないかもしれない。"

    "ましてや自分が桂子さんくらいの歳だったとしたら――。"

    show ecg girlstalkC3 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「危ないことはしません。だから、わたしにやらせてください」"


    voice get_voice_filename("rnk")
    rinka "「直未……そういう演技できる？」"

    show ecg girlstalkC3 uwa with ecg_change


    voice get_voice_filename("nom")
    naomi "「あうぅっ……それを言われると……」"

    "直未は目を逸らして、本で顔を隠してしまった。本の横から顔を出し、小さな声で続けた。"

    show ecg girlstalkC3 ser with ecg_change


    voice get_voice_filename("nom")
    naomi "「でも、頑張ります。先輩のためですもん」"

    scene ecg girlstalkA5 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「ホント頼もしいね、直未は」"


    voice get_voice_filename("nom")
    naomi "「問題はいつ行くか……ですけど、やっぱり土日がいいかなって思います」"

    show ecg girlstalkA5 que with ecg_change


    voice get_voice_filename("rnk")
    rinka "「どうして？」"

    scene ecg girlstalkC3 ser with dissolve


    voice get_voice_filename("nom")
    naomi "「平日だと、家族の人が来るのって夜になると思うんです。遅くなるなら、来られないかも……」"


    voice get_voice_filename("nom")
    naomi "「でも土日なら……少なくとも旦那さん――お父さんは来ると思うんです。早い方がいいと思うので、土曜日に行きます」"

    scene ecg girlstalkA5 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「分かった。ただ、私もついて行く。何かあった時に大声を出せば駆け付けられるところで待ってるから」"

    "私が念を押すと、直未は頷いた。"

    scene bg lion01 evening with dissolve_long

    "その後はいくつかの可能性について話したが、ほとんどが妊婦さんに関する勉強になっていた。"

    "私は直未を駅まで見送り、ライオン館へ戻った。"









    python:
        set_info_time("night")
        set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "直未と話して、予想外に情報集めが捗ったことに驚いていた。"

    "私がいかに選定のことを考えていなかったかという証明でもあった。"

    "生きること。"

    "どうやって生きるのが正しいかなんて、まだ分からないけれど。"

    "海晴や直未、もちろん真央やおばあちゃんたちも悲しませたくない。今はそれで充分だった。"

    "桂子さんも、きっと同じ想いを抱えているはずだ。いや、子供を産んだと言っていたからこそ、より強いはずだ。"

    "私は、生まれた時とほぼ同時に両親を事故で失ってしまったらしいから、両親から注がれる愛というのを知らない。"

    "想像するしかないけれど、かつておばあちゃんがお母さん――つまり自分の娘のことを話したときの顔を覚えている。"

    "孫の私に向けるのとは違う愛が、そこにはあった。"

    show rnk paj nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「考えちゃ、駄目だ」"

    "桂子さんのことを考えれば考えるほど、感情移入してしまう。"

    "彼女のことを想像してしまう。"

    "今必要なのは、きっと機械的に、理性的に彼女の情報を探ることだ。"

    "直未だって、かなり無理をしてそうしていた。直未が頑張ってるのに私ができなくてどうする。"

    show rnk paj nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「今すべきこと……か」"

    "それはきっと、休むことだ。"

    "私はベッドに入り、目を閉じた。"

    $ add_seen_chapter("3-3")








    python:
        set_info_scene("31")
        set_info_date(5, 19, "sat")
        set_info_time("noon")
        set_info_location("04")


    stop music fadeout 2
    scene bg lion02 noon with fade_longest
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "放課後、私は直未と待ち合わせてまたうちに来ていた。"

    "結局この日まで、桂子さんが私に接触してくることはなかった。"

    show rnk uni nor nor rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「桂子さんも私に名前を知られてるって気が付いてるはずだもんね」"

    show nom gun hes tr1 at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「はい……。瓶淵さんも迂闊に近付くのはリスクが高いってことだと思います」"

    show rnk uni arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「じゃ、行こう」"

    hide rnk
    hide nom
    with std_out

    "私は鞄にカードブックが入っているのを確認してから、病院まで徒歩で直未を案内することにした。"








    python:
        set_info_time("evening")
        set_info_location("19")

    stop music fadeout 1
    scene bg hospitallounge on with fade_long
    play music audio.investigation
    pause 1

    $ show_hud()

    "病院のラウンジまで来てから、私は直未がどんな言い訳で家族の人に話しかけるのかを聞いていなかったことを思い出した。"

    "私が行くのは論外にしても、直未だって知らない女子高生に変わりはないのだ。"

    "全くの他人に娘の個人情報を教えるとは思えない。"

    "私はラウンジで直未を待っていた。桂子さんの病室がある階であり、直未の姿こそ見えないが大声を出せば聞こえるような場所だ。"

    "私の前では大分治ったが、慌てん坊で恥ずかしがり屋の直未なのだ。心配はかなりある。"

    "だが、私のために頑張ってくれると言ってくれた。だからこそ、私は直未を信じていた。"




    stop music fadeout 1
    scene bg hospitallounge on with fade_long
    play music audio.nichijo03
    pause 1

    "しばらく経って、廊下を30代後半くらいの男性が通り過ぎた。"

    "桂子さんの旦那さんだと察し、私は目を合わせないようにした。"

    "窓の外を見ながら、足音が遠ざかるのを待つ。"

    show nom gun nor nor at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「先輩？」"

    show rnk uni sur su2 rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「わっ、びっくりした……」"

    "後ろから声をかけられたので、思わず大きな声を出してしまった。はっとして、左右を見渡す。変な注目は浴びていなさそうだ。"

    "直未の声には、はっきりとした陰りがあった。"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……おかえり。それで、どうだった？」"

    show nom gun har pin with std_change

    voice get_voice_filename("nom")
    naomi "「き、緊張しました。でも、分かった情報はどちらかというと外堀を埋めるようなものに近いです」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「核心には触れなかったってこと？」"

    show nom gun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「はい。瓶淵さんは元々体が弱くて病気がちだったそうですが、持病は持っていなかったみたいです。ただ切迫早産の状態が続いていて、最終的には緊急帝王切開で早産だったとのことです」"

    show nom gun hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「子供も入院が必要な状態らしくて、親子で３週間近く入院しているみたいです」"

    "３週間近くということは、選定が開始した時期とも重なる。"

    "切迫早産というのは、昨日見た本に書いてあった。"

    "子供が予定日より早く生まれるのが早産であり、生まれそうになるのが切迫早産というらしい。"

    "痛みや出血などが続き、安静にしていなければいけない状態だそうだ。"

    "そして状態が急変し、帝王切開に至ったということだろう。"

    show rnk uni arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そういえばさ、どうしてそこまで教えてくれたの？」"

    show nom gun nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「……嘘、ついちゃいました」"

    "直未は静かな声でそう言った。"

    "戻って来た時に感じた声の陰りは、きっとそれが原因なのだろう。"

    show nom gun hes tr2 with std_change

    voice get_voice_filename("nom")
    naomi "「友達が入院していて、お見舞いに来るといつも桂子さんがいた。心配していたけど、失礼かもしれないから本人に詳しくは聞けなかったんですって。近いうちお花を持っていきますって」"

    show nom gun hes tr1 with std_change

    voice get_voice_filename("nom")
    naomi "「その流れで……さっきのことを聞きました……」"

    show rnk uni nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「直未……」"

    "直未は泣きそうになっていた。"

    "娘を脱落させる――本来の死の運命に引き戻すために両親から情報を引き出したのだ。"

    "直未は自分で自分のことを責めているに違いない。優しい子だというのは、私がよく知っている。"

    "だからこそ、私はぐっと奥歯を噛み締めた。"

    "下手な慰めはしてはいけない。私のためにやってくれたのだ。"

    "さすがに死因についてここで話すのはよくないと思い、私たちは一旦ライオン館へ戻ることにした。"









    $ set_info_location("04")

    stop music fadeout 1
    scene bg lion01 evening with fade_long
    play music audio.gimon
    pause 1

    $ show_hud()

    "ライオン館に戻った私たちは、早速桂子さんの≪死因≫について話していた。"

    "空気は、重かった。"

    "無理もない。だが、お互いにそれを口には出さずにいた。"

    "早産や帝王切開というのは、母体に負担がかかるというのが本に書かれていた。"

    "元々持病などはなかったけれど、体が弱かったという桂子さん。とすればその死因はきっと――。"

    show rnk uni nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「『失血死』なのかな」"

    "しかし、本は光ることはなかった。"

    "情報が間違っているのか、情報が合っているけれどその他の条件が足りないのか、私には分からない。"

    "直未との話の中で、それなりの確信を持っていたのだけれど。"

    show nom gun hes sor rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「出ませんね……。わたしの予想が間違ってたってことでしょうか」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、持病があるなら家族の人は濁すと思う。ないって言い切ったってことは本当にないんだよ」"

    "私は、図書館で借りた本を再び持ってきた。一度見た資料に見落としがないか、もう一度見ることにした。直未も、その内の一冊を手に取った。"

    "情報は、案外すぐに見つかった。"


    play music audio.investigation fadein 1

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「もしかして、これかも」"

    "私が見つけたのは、出産時の母親の死因で多いものであった。"

    "脳出血。"

    "脳の血管が破れて脳の内部に出血している状態だそうだ。"

    "意識や感覚に障害が現れるだけでなく、血の腫瘍が大きくなると脳幹が圧迫されて死に至る、とのことだ。"

    "脳幹とは、様々な神経が集まっていて、脳の中心部と言ってもいい特に重要な部位らしい。"

    "出産時の原因不明の死因は、脳出血であることが多いらしい。"

    show nom gun hes nor rev with std_change

    voice get_voice_filename("nom")
    naomi "「なるほど……これなら筋も……」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「あっ、光ってる……」"

    show nom gun nor sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「えっ？　どこがですか？」"

    scene ecg cardbook bli with dissolve_long

    "私がこの情報を見つけたのとほぼ同時、本が光をまとった。"

    "どうやら、直未には光が見えていないようだ。私は、直未に情報がカードになる時に光を発することを教えた。"

    scene ecg cardbook op2 with dissolve

    "光はすぐに集束し、一枚のカードが生まれた。"


    scene bg lion01 evening
    show nom gun har sur rev at std_cl
    with dissolve_long



    voice get_voice_filename("nom")
    naomi "「あ、カード！」"

    "他のもの同様、カードもそこに書かれた内容自体も見えるらしい。"

    "カードは実存、つまり実際に存在する現実のものだから、ということなのだろうか。"

    "私は直未にも見えるようにカードを机の上に置いた。"

    python:
        add_character_cards("rnk", ["8_death"])
        add_character_cards("kik", ["8_death"])

    "書かれていたのは、Ⅷ・死因。その情報は脳出血であった。"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「これが、桂子さんの――」"

    "死因。"

    "あの病弱そうな女性は、出産の際に脳出血で死亡したのだ。"

    "子供も入院しているということは生まれているということ。私とは違い、その出産自体はなかったことにならなかったようだ。"

    "つまり、正確には出産の瞬間ではなくしばらく経ってから亡くなったということになるのだろう。"

    "情報を得て一歩進んでことになるが、喜びを感じることはなかった。"

    "むしろ正しい情報を知ってしまったことで、死に対してより現実的な重みがのしかかる。"

    show nom gun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「…………」"

    "直未も私と同じ気持ちなのだろう。"

    "何とも言えない顔をして下を向いていた。"

    "沈黙の次の言葉を切り出したのは私だった。"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「このまま、彼女の≪未練≫を探そう」"

    "桂子さんではなく彼女と呼んでいることを、私は自分で気が付いていた。"

    "感情移入してはいけない。意識して遠ざけないと、きっと後で後悔するとようやく理解できた。"

    "死因を知るというのは、そういうことだった。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「子供……なのは間違いないと思う。やっぱり子供の将来かな」"

    "だが、本は反応しない。当てずっぽうでは、駄目なのだ。"

    show nom gun har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「子供……。わたしも子供は関係あると思います。もう一度、病院に行ってみましょう」"







    python:
        set_info_time("night")
        set_info_location("19")



    stop music fadeout 1
    scene bg hospitallounge night with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "勢いに任せて病院に戻ってきたはいいものの、無関係の人間が新生児室に入れるはずもなかった。"

    "だよね、と直未に伝える。"

    show nom gun hes shy rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「実はわたしも薄々思ってました……すみません……」"

    show rnk uni nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「もう少し、別の方法を考えた方がいいかも」"

    show nom gun har pal rev with std_change

    voice get_voice_filename("nom")
    naomi "「でも、選定は日曜日の夜なんですよね？　明日を逃したら、また来週になってしまいます。瓶淵さんも他の参加者ももっと積極的に動き出すかもしれません……！」"

    show nom gun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「できるうちに、できることをした方が……」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「それは、そうだけど……」"

    "直未の言っていることは確かに分かる。"

    "現状はまだ他の参加者も私に接触して来てはいない。情報を探るのも探らせないようにするのも、瓶淵さんだけを気にしていればいい。"

    "だが面会時間の終了は20時だ。今は19時だから、もう間もなく病院にいられなくなってしまう。"

    "これ以上何ができるのか、今は思いつかなかった。"

    show nom gun har con rev with std_change

    voice get_voice_filename("nom")
    naomi "「やっぱり――わたし、本人に聞いてみます。疑われるかもしれないですけど、どうにかごまかして」"

    hide nom
    hide rnk
    with std_out

    "直未は立ち上がると、「先輩は待っててください」と言ってそのまま走り出そうとした。"

    "私が直未を引き留めたところで、直未はその場に転んでしまった。"

    show nom gun fal sur at std_c with std_in
    hide nom with DissolveMoveOut(0.5, yoffset(200), easein)
    play se "taoreru08"


    voice get_voice_filename("nom")
    naomi "「ふぎゃっ！」" with quake_fast

    show rnk uni nor apo at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あ、ごめん……」"

    hide rnk with std_out

    "しかし、直未はそれで少し冷静になったようだ。"

    "私も直情的な方ではあるが、直未も似ているところがあるらしい。もしかしたら私よりも、思い立ったらすぐ行動という性格なのかもしれない。"

    "コーヒーを教えるというのも、選定に協力してもらうというのも、すぐに決まったことだった。"


    play music audio.kinpaku
    show kik sta nor ser at std_r with std_in



    voice get_voice_filename("kik")
    keiko_unk2 "「病院で何を騒いでいるのかしら？」"

    "突然声をかけられて、背筋が冷える。"

    "直未に手を貸すためにしゃがんでいたので、私は声の主を見上げることになった。"

    show rnk uni arm ang rev at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あなたは……」"

    "瓶淵桂子――私たちが死因を特定し、未練を探っている選定の参加者がそこにいた。"

    "念のために彼女の病室があるのとは違う階で話していたのに、どうしてここにいるのだろう。"

    show kik sta nor nor with std_change

    voice get_voice_filename("kik")
    keiko "「丁度よかったわ。あなたを探していたのよ、獅子舞凛火ちゃん？」"

    "彼女は冷たい声でそう言った。ちゃん付けで呼ばれるような関係ではないから、含みがあることは明らかだった。"

    "私は直未をかばうようにして、一歩前へ出た。だが、瓶淵さんが気付かないはずもない。"

    show kik sta nor ser with std_change

    voice get_voice_filename("kik")
    keiko "「あなたの友達よね？　私の夫と話したみたいじゃない……いいわね、協力してくれる仲間がいて」"

    "彼女に対して、私は何も言うことができなかった。"

    "迂闊に喋ればこちらが不利になる危険性があるのは、最初に会った時と同じなのだ。"

    show kik sta nor nor with std_change

    voice get_voice_filename("kik")
    keiko "「そんなに警戒しなくていいのよ、凛火ちゃん。私はあなたと話がしたいだけだから」"


    voice get_voice_filename("rnk")
    rinka "「話……？」"

    "その内容は、選定のことで間違いがないだろう。"

    "私は聞き返した直後に、頷いた。"

    show nom gun nor sur rev at std_l with std_in

    voice get_voice_filename("nom")
    naomi "「先輩！」"

    show kik sta nor ser with std_change

    voice get_voice_filename("kik")
    keiko "「あなたはいいわ。凛火ちゃんだけでいいの」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「大丈夫。この人は話したいって言ってるだけだから」"

    "不安そうな顔を向ける直未に、私は黙って頷いた。"

    show nom gun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「気を付けて……ください」"

    show kik sta nor lau with std_change

    voice get_voice_filename("kik")
    keiko "「もう、警戒し過ぎだわ。どうにかしようって気はないの。ただ話したいだけ」"

    show kik sta nor nor with std_change

    voice get_voice_filename("kik")
    keiko "「話すのは上のラウンジがいいかしら。病室だと他の患者がいるもの。この時間なら人の往来も少ないからね」"

    show kik sta nor ser with std_change

    voice get_voice_filename("kik")
    keiko "「お友達はここで待っていてちょうだい。盗み聞きできないように……ね」"

    "不安そうな顔から変わらない直未を残したまま、私は瓶淵さんの後に続いた。"










    python:
        set_info_scene("32")
        set_info_location("19")

    stop music fadeout 1
    scene bg hospitallounge night with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "私をラウンジに座らせると、瓶淵さんは少し席を外した。"

    "戻って来たとき、彼女の手には缶コーヒーとミネラルウォーターがあった。"

    show kik sta nor nor rev at std_cl with std_in

    voice get_voice_filename("kik")
    keiko "「はい、どうぞ」"

    "私は戸惑いながら、缶コーヒーを受け取った。"

    "近くに自販機があったからそこで買って来たものだろう。だが、瓶淵さんは言わば敵。素直に受け取っていいものだろうか。"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「毒……なんて入っていないわよ」"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「女神の選定っていう映画や小説の世界みたいなものに参加してしまったけれど、毒や睡眠薬は現実ではそう簡単に手に入らないもの」"

    show rnk uni arm sad at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「いえ……そんな……」"

    show kik sta nor lau rev with std_change

    voice get_voice_filename("kik")
    keiko "「いいのよ。あなたと最初に会った時に私……かなり興奮してしまってたものね。怖がらせてしまったわ」"

    "その言葉を聞いて、私は缶コーヒーを飲んだ。"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「ふふ……度胸があるのね」"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「あなたのおうち、喫茶店なんですってね。アルバイトしているのかと思ったけど、２階に住んでいるんでしょ？」"

    "私は答えなかった。"

    "何故知っている――とは思わなかった。私の名前とあの場所を知られているのだから、調べるのは容易だろう。"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「コーヒーは好きかと思ったんだけど、それでよかったかしら？」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……はい」"

    "お礼を言うところまではできなかった。"

    "彼女はぶっきらぼうな私の返事を想定していたようで、笑みを浮かべるとミネラルウォーターを口に含んだ。"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「あの時は……ごめんなさいね」"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「焦っていたのよ。あなたの名前しか分からなくて。夢で遭った男にも名前を知られているのに、入院したまま時が過ぎて行くだけだったから」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「お体……悪いんですか？」"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「私の≪死因≫を探ろうとしてるのかしら？」"

    "瓶淵さんは、私の目をしっかりと見据えていた。"

    "落ち着いていると、彼女は底が見えないような気がしていた。大人だな、というのが新しくもった印象だった。"

    show kik sta nor lau rev with std_change

    voice get_voice_filename("kik")
    keiko "「いいえ。もう分かっているのよ。きっとあなたたちは私の≪死因≫を見つけたのよね」"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「でなければ、≪未練≫を探しはしないわ。難易度が一番高いのは≪未練≫だもの」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「会話……聞かれて……」"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「あら、会話の盗み聞きには気付いていると思っていたわ」"

    "やはり、一度ライオン館に戻った方がよかったようだ。お見舞いには多くの人が来るからと、油断していた。"

    show kik sta nor lau rev with std_change

    voice get_voice_filename("kik")
    keiko "「いいえ、これもやめましょう。私はあなたを怖がらせたいわけではないの」"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「話したかったのは、お互いこれ以上詮索するのはやめましょう、ということよ」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「どういう意味ですか？」"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「言葉通りの意味だわ。あなたは私の情報を探るのをやめる、私はあなたの情報を探るのをやめる……そういうことよ」"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「はっきり言うわ。停戦協定を結びましょう」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたの言う通り、私はあなたの氏名と死因を知っています」"

    show kik sta nor lau rev with std_change

    voice get_voice_filename("kik")
    keiko "「ええ。だから私もあなたの氏名と死因を知っている。現状はお互いに平等よ。都合がいいでしょう」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……私の……死因を……？」"

    "彼女の言葉に、私は動揺を見せてしまった。"

    "いつの間に、知られてしまったのだろうか。私自身、彼女に調べられているような感じはしなかった。"

    "電車で起きた火事というのも、調べてみたところ≪なかったこと≫になっていたのだ。"

    "可能性があるとすれば、初期カードで持っていたか、公園での会話を聞かれていたかのどちらかだ。"

    "だが、公園で直未に全てを話したときは声が聞こえるところに人がいないのをちゃんと確認した。"

    "盗聴器――いや、毒や睡眠薬が容易に手に入らないのと同じように、盗聴器だって入院中の彼女が手に入れるのは難しい。"

    "あの場所は風が強くノイズも入りやすいだろうから、高性能なものでなければいけないだろうし。"

    "とすれば、前者の初期カード。だが、36枚あるカードの中で都合よく私の情報が２枚配られるだろうか。"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「私はあなたの情報を広めて、他の参加者と取引することもできるわ。それこそ……私の氏名を知ってしまったあの男にも、ね」"

    "Ⅻの男性のことだ。この人はやはり相当意識している。"

    "当たり前だ。彼は日常生活で決して見ることができない冷酷な目をしていたのだ。"

    "桂子さんは、相変わらず余裕を持った表情だ。"

    "私は彼女のことをじっと見つめた。何かが胸に引っかかっていた。"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「本当……ですか？」"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「この状況で嘘をついて、私にメリットがあるかしら？」"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「気になるなら、カードを見せてあげてもいいわよ？　もちろんその場合、あなたにも見せてもらうことになるけれど」"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「でも、停戦協定を結ぶんだから、信頼が大事だと思うわ。あなたに嘘を……」"

    play music audio.kinpaku

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「いえ、断ります」"

    show kik sta ten imp rev with std_change

    voice get_voice_filename("kik")
    keiko "「えっ……？」"

    "私はあえて強く言った。"

    "緊張を押し殺し、彼女のペースに巻き込まれないように。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたは私を見つけたとき『死因は何？』と聞きました。つまり、初期のカードに私の死因はなかった」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「その時から今までに、あなたが私の死因を見つけられたとは思えません」"

    "私自身が自分の死因を忘れてしまっているのに。"

    "会話を盗み聞きしたところで、未知の部分は私たちと同じはずだ。"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「あなたが知らない方法で、私は情報を得たのよ」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「どんな方法ですか？」"

    show kik sta nor lau rev with std_change

    voice get_voice_filename("kik")
    keiko "「大人には色々なやり方があるのよ」"

    "彼女の口調は、少し焦りを含んでいた。"

    "私はそれで確信を持つことができた。同時に、瓶淵さんに対しての何かが冷え切ったのを感じた。"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたは嘘をついてる。信頼なんて、ハッタリだ」"

    show kik sta ten cla rev with std_change

    voice get_voice_filename("kik")
    keiko "「違う、違うわよ！　本当よ！　あなたの死因を知ってるの！」"

    "私は立ち上がり、黙ったまま瓶淵さんを見下ろした。"

    "私を見上げる目は、大きく見開いていた。"

    show kik sta ten imp rev with std_change

    voice get_voice_filename("kik")
    keiko "「自殺よね……いえ、違うわ交通事故？」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「もう、話は終わりにしましょう。せめて本当のことを言ったなら……私も考えたのに！」"

    "最後の言葉は、本心だった。"

    "桂子さんが嘘をついていると分かったから、にもかかわらず信頼を得ようとしたから、彼女への同情はなくなってしまった。"

    "彼女の死因を知り、想像した人生。その景色は、いまや他人事になっていた。"

    show kik sta ten cla rev with std_change

    voice get_voice_filename("kik")
    keiko "「待って……、待って」"

    "瓶淵さんは私を悲痛な声で引き留めた。"

    show rnk uni arm vig rev with std_change_wait

    "だが私は返事をせず、直未のところへ戻ろうとしていた。"

    show kik sta ten imp rev with std_change

    voice get_voice_filename("kik")
    keiko "「私は……生きたいの。生きなきゃいけないのよ！」"

    show kik sta wea bad rev with std_change

    voice get_voice_filename("kik")
    keiko "「子供相手に嘘までついたのに……このままじゃ、私……」"

    show rnk uni ang an2 with std_change

    voice get_voice_filename("rnk")
    rinka "「大人か子供かなんて関係ないだろ！」"

    "彼女の言葉に、私はつい大きな声を出していた。"

    "そしてどうしてだろうか。急に、目の奥が熱くなってしまった。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「失礼……します……」"

    "少し離れたところで、私は立ち止まっていた。"

    "瓶淵さんを見限ったはずなのに、どうしてか、彼女のことが気になってしまったのだ。"

    "そしてすぐに納得した。"

    "彼女の生きたいという言葉が、紛れもない本心だったからだろう。"

    "危ないところだった。気を抜けば、あのまま彼女と停戦協定を結んでいた。"

    "大人か子供かなんて関係ない。"

    "ただ素直な言葉に、私は弱いことが分かった。"

    "どうにか持ち直し、直未のいる一階下へと戻ることにした。"







    scene bg hospitallounge night with fade

    $ show_hud()

    show rnk uni sur su1 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あれ……直未……」"

    "直未を待たせている場所まで戻って来たが、そこにはいなかった。"

    "すぐ戻って来ると思い、少し待つことにした。"

    "だが、私は想定外の状況に直面し、硬直してしまう。"


    play music audio.kinpaku

    show aln sta nor nor rev at std_cl with std_in


    voice get_voice_filename("aln")
    alan_unk2 "「……君は……」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    "「ひっ……」"

    "彼のことを見た瞬間、息が止まりそうになっていた。"

    "褐色の肌に、高身長。胸板は分厚く、腕は太い。スポーツ選手でもいないような筋肉は、服の上からでもはっきり分かる。"

    "まるで、鎧のような肉体だった。"

    "だが肉体よりも、彼の冷酷な瞳に恐怖を覚えていた。"

    "夢の世界で２度会っている彼だが、現実世界で見るとより、現実離れした存在感が際立っていた。"

    "Ⅻの位置に立っていた男性。同時に、最初に参加者を脱落させた人でもあり、瓶淵さんの氏名のカードを手に入れた人でもあった。"

    show aln sta nor irr rev with std_change


    voice get_voice_filename("aln")
    alan_unk2 "「いずれ脱落させることにはなるが――今、君に構っている暇はない」"

    hide aln with std_out

    "男性は私とすれ違い、私が来た方へと歩いて行った。"


    play music audio.nichijo03

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「ぷはっ……」"

    "彼がいた間、私はまるで溺れているかのような錯覚があった。"

    "呼吸が半分以下しかできていなかったことだろう。"

    "あんな人の情報を集めなければいけないのか――。そう思うと、心が挫けそうになってしまう。"

    show nom gun hes tr1 rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「すみません、ちょっとお母さんから電話が来ちゃってて……ってあれ？　どうしたんですか？」"

    hide rnk
    hide nom
    with std_out

    "丁度、戻って来た直未が声をかけてきた。"

    "一緒でよかった。直未がこうやって声をかけてくれるのだから、まだ挫けるわけにはいかなかった。"

    "私は直未に、今あったことをざっくりと説明した。"

    show nom gun har con rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「先輩に構ってる暇はないってことは、つまり――」"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「狙いは瓶淵さんだ。あの人はカードも持ってる……追いかける」"

    "そう言った私を、直未は引き留めた。"

    show nom gun har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「何をしに行くんですか？　先輩が行く理由は……ないですっ！」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「そうだけどっ……でもっ……」"

    "私は、瓶淵さんの表情を思い出していたのだ。あの必死で悲痛な声も。"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「分からないけど、行かなくちゃ！　直未はここで待ってて。何かあったら連絡するから、すぐ警察を呼んで！」"

    show nom gun nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「先輩……」"

    "直未は力が抜けたような動きで、私の手を放した。"

    "それ以上の言葉を聞く前に、私は瓶淵さんの病室の方へ向かっていた。"






    python:
        set_info_scene("33")
        set_info_location("19")


    stop music fadeout 1
    scene bg hospitallounge night with fade_long
    play music audio.impatience
    pause 1

    "瓶淵さんの病室の前で、彼女に出てきてもらうまでに数分かかった。"

    "というのも面会時間はすでに終わっており、私は看護師さんを何とか言いくるめる必要があったのだ。"

    "最終的には大声を出している私を見兼ねて、瓶淵さんの方から出て来てくれた。"

    show rnk uni arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「無事……なんですね」"

    show kik sta nor ser rev at std_cl with std_in

    voice get_voice_filename("kik")
    keiko "「あなた……どうして？」"

    "瓶淵さんは生気のない表情を浮かべていた。"

    "無理もない。彼女をその顔にしたのは私だ。"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「気が変わったの……？」"

    "彼女は不審な声で訊ねてきた。"

    "だが、私はすぐに返事をしなかった。"

    "あの男性は、間違いなく桂子さんを狙っている。私の方が早く桂子さんのところに来たとも思えない。"

    "彼と言葉が通じたのだから、本を持っているに違いない。実際には日本語が分からなくても、標識や表示も読めるはずだ。"

    "追い抜くこともなく、私が先にここへ到着できるだろうか。"

    "まさか――！"

    show kik sta ten cla rev with std_change

    voice get_voice_filename("kik")
    keiko "「ちょっと、どうしたの？」"

    "動揺する瓶淵さんの手を引き、私は無理矢理連れて行くことにした。"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「子供が危ないんです！」"

    "初めは抵抗していた彼女だったが、この言葉でふっと力が抜けた。"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたの名前を知っている人が、あのⅫの男性がこの病棟にいます」"

    show kik sta ten imp rev with std_change

    voice get_voice_filename("kik")
    keiko "「あの……男が？」"

    show kik sta wea bad rev with std_change

    voice get_voice_filename("kik")
    keiko "「まさか、子供を人質にとろうと……！」"

    "瓶淵さんが出産して間もないということは、聞き込みをすればすぐに分かるだろう。"

    "生まれて３週間の子供に抵抗する力なんて――ない。"

    "新生児室は入れないようになっているだろうけれど、あの男性は何故だかそんな問題は容易く解決できそうな底知れなさがある。"

    "あの人のことはよく知らないけれど、目の怖さだけは知っている。"

    show kik sta wea sad rev with std_change

    voice get_voice_filename("kik")
    keiko "「ああ……そんな……駄目……」"

    "嘆きの声を漏らす瓶淵さんを先導させ、私たちは新生児室へ向かった。"







    stop music fadeout 1
    scene bg hospitallounge off with fade
    play music audio.kinpaku

    "その後、私は悲惨な光景を目にすることとなった。"

    "新生児室前の廊下はすでに消灯されていて、非常灯は壊されているようだ。"

    "その先の部屋から漏れる薄ぼんやりした光で、かろうじて状況が分かった。"

    show kik sta ten cla at std_cr with std_in

    voice get_voice_filename("kik")
    keiko "「なに……どうしたのよこれ！」"

    "先を行っていた瓶淵さんがまず声を上げた。"

    "その理由に私もすぐに気が付いた。"

    "廊下には、看護師さんたちが横たわっていた。"

    show rnk uni arm ang at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「そんな――！」"

    "近付いて耳を寄せてみると、呼吸はしている。"

    "最悪の事態を想像してしまったが、どうやら全員生きているらしい。"

    "だが私は、すぐにもっと最悪な事態を目にすることになる。"

    show rnk uni arm imp with std_change

    voice get_voice_filename("rnk")
    rinka "「直未っ！」"

    "看護師さんたちの中に混ざり、直未もそこにいた。"

    show nom gun unw wea rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「……ぱい…………。ごめんな……さい……」"

    "弱々しい声で、直未は続ける。"

    "離れたところに直未の眼鏡も落ちていた。無残にも、レンズが割れていた。"

    show nom gun unw wea rev with std_change

    voice get_voice_filename("nom")
    naomi "「…………話を聞いて……狙いは子供だって……思って……。助けなきゃって……子供は関係ないって……危ないって……」"

    show kik sta nor ser with std_change

    voice get_voice_filename("kik")
    keiko "「あなた！　くっ……」"

    hide kik
    with std_out

    "瓶淵さんは私の制止も聞かずに明かりのついた奥へ向かった。"

    show nom gun unw wea rev with std_change

    voice get_voice_filename("nom")
    naomi "「先輩は……逃げ…………」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめん。直未、少し待ってて」"

    hide rnk with std_out

    "奥歯を噛み締め、私は瓶淵さんの後を追った。"

    python:
        set_info_scene("34")
        set_info_location("20")








    play music audio.impatience
    scene bg hospitalnursery with dissolve

    show kik sta ten cla at std_c with std_in

    voice get_voice_filename("kik")
    keiko "「ねえ！　何をしてるの！」"

    "新生児室に入ったとき、悲鳴が轟いた。"

    "彼女の悲鳴で驚いたのか、眠っていた赤ちゃんが一斉に泣き出した。"

    "部屋の中にも何人かの看護師が倒れている。"

    "赤ちゃんが泣き出したのが今ということはつまり、彼が音を立てずに迅速にここまで入り込んで来たということである。"

    "過程は重要ではなく、彼がそういうことができるという事実が凄まじかった。"

    show aln sta nor ang rev at std_l with std_in


    voice get_voice_filename("aln")
    alan_num "「……黙れ」"

    "男性はベッドに寝た赤ちゃんたちに向かい、小さな声で言った。"

    "無駄だ。赤ちゃんに通用するはずがない。"

    show kik sta ten imp with std_change

    voice get_voice_filename("kik")
    keiko "「嘘……」"

    "瓶淵さんと同じように、私も驚いていた。"

    "大泣きしていた赤ちゃんたちが、一斉に泣き止んだのだ。"

    "足がすくんでいた。動物が天敵を目の前にしたのと同じだ。"

    "勢いで追いかけて来たけれど、私はただ震えることしかできない。"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「何故貴様まで」"

    show rnk uni arm ang at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「私はっ――」"

    show kik sta nor ser with std_change

    voice get_voice_filename("kik")
    keiko "「この子も私の情報を探っていたのよ。騒ぎに乗じて情報を得られないか探しに来たんじゃないかしら？」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……」"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「だろうな。さっきも言っただろう。今、君に構っている時間はない」"

    show aln sta nor irr rev with std_change


    voice get_voice_filename("aln")
    alan_num "「この国の警備がそう甘くないことは僕も分かっている。早く済ませたい」"

    "男性の声は低く、穏やかだった。"

    "この状況でそこまで落ち着いてるのが、かえって不気味だった。"

    show kik sta ten imp with std_change

    voice get_voice_filename("kik")
    keiko "「どうしてここにいるのよ？」"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「名前が分かっているんだ。調べれば分かる。そして病院まで来れば、君の入院の理由は容易に分かる」"

    show aln sta nor irr rev with std_change


    voice get_voice_filename("aln")
    alan_num "「僕の情報網などどうでもいい。早く済ませたいんだ。その意味は分かるか？」"

    show kik sta ten nor with std_change

    voice get_voice_filename("kik")
    keiko "「……分からないわ。子供たちから離れて」"

    show aln sta nor ang rev with std_change


    voice get_voice_filename("aln")
    alan_num "「分かっているからこそのその発言だ。いい。はっきり言おう」"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「カメブチ……だったな。このベッドだ」"

    "男性はすぐに瓶淵さんの子供を見つけた。"

    "ベッドには名前が書いてある。ここからでは赤ちゃんの顔は分からないが、≪{rb}春樹{/rb}{rt}はるき{/rt}≫という名前からして男の子だろう。"

    show aln sta nor irr rev with std_change


    voice get_voice_filename("aln")
    alan_num "「君の死因と未練を言え。でなければ息子は殺す」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……」"

    "淡々と、この男性は赤ちゃんを殺すと言った。"

    "顔から血の気が引いていく。人質に取るというのはそういうことだろうが、だが、でも、生まれたばかりの赤ちゃんを殺すだなんて平然と言えることではない。"

    show kik sta ten cla with std_change

    voice get_voice_filename("kik")
    keiko "「ひっ……」"

    "彼がそう来るのは、瓶淵さんも予想していただろう。"

    "だがここまではっきりと、口にされた時に冷静でいられるはずがない。それくらい、私にも分かる。赤ちゃんを――家族を殺すだなんて！"

    show kik sta wea bad with std_change

    voice get_voice_filename("kik")
    keiko "「わたっ……私はっ……」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「む……無駄……です」"

    "彼女を遮って、私は言った。"

    "勇気を振り絞って、知恵を振り絞って、交渉を行う。この場をどうにかして打開する。"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「もう少し待てば……警備員が駆け付けます。警備員が来れば、あなたもそう簡単には逃げられない。捕まれば≪選定≫の期間中、自由に動けなくなります」"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「構わない。そうなったら僕は子供をさらって逃げる」"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「数人の警備員なら、蹴散らすのは難しくない。後々、多少厄介にはなるが、ケイコ・カメブチの情報を得る結果は変わらない」"

    "男性は即答すると、さらに続けた。"

    show aln sta nor ang rev with std_change


    voice get_voice_filename("aln")
    alan_num "「30秒だ。それ以内に結論を出せ。答えなければ隣の子供を殺す。次も30秒だ。その次は君の子供をさらって僕は逃げる」"

    show rnk uni ang an2 with std_change

    voice get_voice_filename("rnk")
    rinka "「そんな、無関係な子供を！」"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「駄目よ……。あなたが感情的になれば、あなたの情報も交換条件にされるわ」"

    "瓶渕さんは、私にしか聞こえないように小さな声でそう言った。"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「Ⅰ番の子供は、ケイコに情報を知られているな。だから僕にケイコを脱落させたくないわけだ」"

    show rnk uni arm imp ten with std_change

    voice get_voice_filename("rnk")
    rinka "「ちがっ……」"

    "反射的に否定をしたが、私は瓶淵さんに氏名を知られていた。"

    "それに気付かないくらい、愚かだった。"

    show rnk uni arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「で、でも……あなたが子供をころっ、殺しても……あなたが脱落すればなかったことになります。だから――」"

    show kik sta ten cla with std_change

    voice get_voice_filename("kik")
    keiko "「もういいわ！」"

    show kik sta ten cla with std_change

    voice get_voice_filename("kik")
    keiko "「あなたの言う通りにする。私の死因と未練を話すわ」"

    show aln sta nor irr rev with std_change


    voice get_voice_filename("aln")
    alan_num "「早くしろ」"

    "男性は感情的な動きを見せずに言った。"

    show rnk uni ang an1 with std_change

    voice get_voice_filename("rnk")
    rinka "「桂子さん！」"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「なるほど。お互いにカードは取得していたのか」"

    show rnk uni ang an1 with std_change

    voice get_voice_filename("rnk")
    rinka "「くっ……」"

    "それで私は、言葉を発するのを封じられてしまった。"

    "これ以上、迂闊に喋れない。"

    show kik sta nor lau rev with std_change

    voice get_voice_filename("kik")
    keiko "「私のために……ありがとうね」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「でも！」"

    show kik sta ten nor with std_change

    voice get_voice_filename("kik")
    keiko "「確かに彼以外の人が選定で残れば、私の子供や他の子供が死んでもなかったことになるでしょうね」"

    show kik sta nor ser with std_change

    voice get_voice_filename("kik")
    keiko "「でもね、母親が自分の息子を危険にさらせるはずないじゃない」"

    show aln sta nor irr rev with std_change


    voice get_voice_filename("aln")
    alan_num "「早くしろ」"

    show kik sta nor nor with std_change

    voice get_voice_filename("kik")
    keiko "「分かっているわ。代わりに、ベッドから離れて。位置を交換よ」"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「……いいだろう」"

    hide aln
    hide rnk
    hide kik
    with std_out

    "男性が入り口側、私たちがベッド側へと移動をした。"

    "子供たちに何かあっても私たちが盾になれる反面、男性は逃げ道を確保したことになる。"



    play music audio.growapart
    scene ecg keikospeak with dissolve_long


    voice get_voice_filename("kik")
    keiko "「私の死因は、出血死。脳出血って言った方がいいのかしら」"


    voice get_voice_filename("kik")
    keiko "「運が悪かったのかしらね。日本ではお産の時に死ぬ確率なんて、もうほとんどゼロに近いのに」"



    voice get_voice_filename("aln")
    alan_num "「そんな情報はいらない、端的に話せ」"

    "男性は本を取り出し、瓶淵さんが続けるのを待った。"


    voice get_voice_filename("kik")
    keiko "「元々体が弱かった私は、体が耐えきれなかった。それだけよ」"

    $ add_character_cards("aln", ["8_death"])



    voice get_voice_filename("aln")
    alan_num "「次は未練だ」"

    "男性は生成されたカードを確認すると手早くしまう。"


    voice get_voice_filename("kik")
    keiko "「……子供の名前よ」"

    "思わず、私の方が聞き返しそうになってしまった。"

    "彼女の息子の名前は、もう決まっているはずだ。それがどうして未練になるのだろうか。"


    voice get_voice_filename("kik")
    keiko "「私が脱落して本来の死因に戻れば、この期間で起こした行動はなかったことになるわ」"


    voice get_voice_filename("kik")
    keiko "「春樹って名前は――私がつけたのよ」"


    voice get_voice_filename("kik")
    keiko "「私の義母はその名前を格好悪いと言って、別の名前を提案したわ。意味よりも読み方を重視した……流行りの名付け方よ」"


    voice get_voice_filename("kik")
    keiko "「義母がつけようとした名前は当て字なだけ、と私は思っていたわ」"

    "桂子さんはここで一度話を区切った。"

    "男性は表情を変えずに、視線で続きを話すように促した。これだけではまだ情報が足りないらしい。"


    voice get_voice_filename("kik")
    keiko "「夫は義母がつけた名前を支持したわ」"


    voice get_voice_filename("kik")
    keiko "「でも春樹が産まれた後、私は夫と話をした。生死の境を彷徨って子を産んだからか――いえ、母親っていうのは必ずそうね」"


    voice get_voice_filename("kik")
    keiko "「とにかく、夫は話を聞いてくれた。私が名前に込めた意味を聞いて納得してくれた」"


    voice get_voice_filename("kik")
    keiko "「それで、出生届を書いたの。名前って、人生に寄り添うものでしょう？　だからこそ最初の子供――長男の名前は、私にとって一生を捧げるに値するものよ」"

    "瓶淵さんは、強い口調で言い切った。"

    "彼女の言葉は、私の心にずしりとのしかかっていた。人の未練は未来そのものでもある。"

    "桂子さんが手に入れたかった未来を、私は知ってしまったのだ。"

    python:
        add_character_cards("rnk", ["8_regret"])
        add_character_cards("kik", ["8_regret"])
        add_character_cards("aln", ["8_regret"])



    stop music fadeout 1
    scene bg hospitalnursery
    show kik sta nor nor rev at std_c
    with dissolve_long


    voice get_voice_filename("kik")
    keiko "「あなたにここまで知られて、春樹は最初で最後の子供になってしまったわね」"

    show kik sta nor lau rev with std_change

    voice get_voice_filename("kik")
    keiko "「――いいえ。私が脱落する頃には、春樹の名前は春樹じゃなくなっているでしょうけれど」"


    play music audio.alan

    show aln sta nor nor at std_r with std_in


    voice get_voice_filename("aln")
    alan_num "「嘘じゃないようだな」"

    show rnk uni ang an1 rev at std_l with std_in

    voice get_voice_filename("rnk")
    rinka "「それだけ！？　何か……何か言葉はないんですか？」"

    show aln sta nor nor with std_change


    voice get_voice_filename("aln")
    alan_num "「僕はカードを手に入れられればいい。話を聞いたところで、カードを手に入れた喜び以外は何も……」"

    "私は、恐怖も忘れて彼を睨んでいた。彼の行動も発言も、瓶淵さんの人生を踏みにじるものに等しい。"

    show aln sta nor irr with std_change


    voice get_voice_filename("aln")
    alan_num "「何も考えていないだけなのか、あるいは――」"

    show aln sta nor nor with std_change


    voice get_voice_filename("aln")
    alan_num "「君が何を言おうと、僕たち全員は他人の命を踏み台にしようとしていることに相違ない」"

    show aln sta nor nor with std_change


    voice get_voice_filename("aln")
    alan_num "「しかし君の意志は、伝わった。実にいい目をしている」"



    voice get_voice_filename("aln")
    alan_num "「君は矛盾を抱えている。自覚もあるはずだ」"

    show rnk uni arm ten rev with std_change

    voice get_voice_filename("rnk")
    rinka "「何を言っているんですか……？」"

    "私が問いかけたのとほとんど同時に、廊下から足音が聞こえてきた。"

    "かすかだが話し声もする。"

    show aln sta nor nor rev with std_change


    voice get_voice_filename("aln")
    alan_num "「……潮時か」"

    show rnk uni ang an2 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「待て！」"

    show aln sta nor irr with std_change


    voice get_voice_filename("aln")
    alan_num "「断る」"

    "そう言うと、男性は部屋の入り口にあったスイッチを叩いた。"


    play se "electricity_switch"
    scene black with dissolve_fast

    "部屋が暗闇に包まれる。廊下の電気もついていなかったから、完全な闇だ。"

    "私はすぐに部屋の電気をつけ直した。"

    scene bg hospitalnursery with dissolve



    "だがその頃にはもう男性の姿はなかった。"

    show nom unw wea wea at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「先輩……大丈夫ですか……？」"

    show rnk uni cat ten rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「直未！」"

    "直未はゆっくりと部屋の中へと入って来た。"

    "怪我はないようだ。手段は分からないが、男性は直未たちを気絶だけさせたらしい。"

    "直未の手には、割れてしまった眼鏡があった。"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめん……直未。私が、巻き込んだから」"

    show nom unw wea sur with std_change

    voice get_voice_filename("nom")
    naomi "「そんな、違います。わたしが勝手に」"

    show kik sta nor nor rev at std_l with std_in

    voice get_voice_filename("kik")
    keiko "「ねえ」"

    "私たちが話していると、桂子さんはそう言って会話を止めた。"

    show kik sta nor ser rev with std_change

    voice get_voice_filename("kik")
    keiko "「今は外で倒れている看護師さんたちを診ているでしょうけれど、警備員はすぐこっちに来るわ」"

    show kik sta nor nor rev with std_change

    voice get_voice_filename("kik")
    keiko "「混乱しているうちに、早く帰りなさい。私が言い訳するから心配はしないで」"

    show nom unw wea wea with std_change

    voice get_voice_filename("nom")
    naomi "「え、えっとでも……」"

    show kik sta nor lau rev with std_change

    voice get_voice_filename("kik")
    keiko "「それに、少し……春樹と一緒に過ごさせてちょうだい」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「直未、行こう」"

    "私が言うと、直未も頷いた。"

    hide rnk
    hide nom
    with std_out

    "すぐに警備員が新生児室に入って来たが、逃げるようにして私たちも病院の外へ出た。"








    $ set_info_location("18")

    stop music fadeout 1
    scene bg lion02 night with fade_long
    pause 1

    $ show_hud()

    "病院を出た私たちは、一旦ライオン館まで戻って来ていた。"

    "帰り道、会話は最初の数分しかなかった。それは、私が新生児室で起こったことを話す、というものだけだった。"

    "当然というべきか、カードは私も取得していた。もっとも、そのカードで桂子さんを脱落させる気はなかった。"

    "私は、直未に話そうと思っていることがあった。"

    show rnk uni arm ama rev at std_cl with std_in

    voice get_voice_filename("rnk")
    rinka "「駅まで送るよ。眼鏡も壊れちゃって、帰りは危ないでしょ？」"

    show nom unw nor smi at std_cr with std_in

    voice get_voice_filename("nom")
    naomi "「はい……ありがとうございます」"

    "駅までの間に、それを言い出せるか考えていた。"

    "後回しにすればするほど言いにくくなる。だったら、先に伝えた方がいい。"

    "言い訳するかのように、私はその結論に至った。"


    play music audio.growapart

    show rnk uni arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「危ないことは駄目って、言ったよね」"

    show nom unw nor sur with std_change

    voice get_voice_filename("nom")
    naomi "「えっ……？」"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、そうじゃなくて。私が悪かったんだ。認識が甘かった」"

    "同時に、この選定が始まってから何もかも軽く考え過ぎていたのだ。"

    "自分では色々考えていたつもりだったけれど、そんなもの、つもり以上では決してなかった。"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「直未が一緒に背負うって言ってくれて、私は救われた。それだけで……十分だ」"

    show rnk uni arm ang rev with std_change

    voice get_voice_filename("rnk")
    rinka "「みんな命を懸けてる。これからもっと、他人を巻き込むことを躊躇わなくなるかもしれない。だから――」"

    show rnk uni arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ここからは私一人で、やるよ」"

    show nom unw wea sur with std_change

    voice get_voice_filename("nom")
    naomi "「せん……ぱい……それって……？」"

    "私は直未に向かって頷いた。"

    "直未の気持ちは本当に嬉しかった。この数日間、言葉にできないほど救われていた。"

    "しかし、これ以上頼ったら直未をもっと危険にさらすことになるだろう。"

    "自分の発言を撤回しようとする気持ちを押し殺して、私はこれ以上何も言わなかった。"

    show nom unw nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「……分かりました」"

    show nom unw nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「助けるって言ったのに、守るって言ったのに……わたしは足を引っ張ってただけで……」"

    show rnk uni arm sad rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ううん、そんなことはない。直未がいなかったら……私……！　でも、でもね。危険にさらすのは……嫌なんだ」"

    show nom unw nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「大丈夫です。先輩の気持ち、分かってます。危険なことは駄目って先輩が最初に言ったのを守れなかったのはわたしですから」"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ごめん――ありがとう。直未がいるって思うだけで、私は強くなれるから。ここからは一人で、大丈夫だから」"

    "じゃあ、と私は駅まで送ろうとした。"

    show nom unw nor ser with std_change

    voice get_voice_filename("nom")
    naomi "「……いいです。ううん、大丈夫です。一人で帰ります」"

    hide nom with std_out

    "と言われ、直未は駅へ向かって行った。"

    "追いかけることはできなかった。"

    "追いかけたらきっと、明日からも頼ってしまう。"

    "馬鹿だな、私は。せめて駅まで送ってから言えばよかったのに。"

    "そうすれば、直未に夜道を一人で歩かせずに済んだのだから。"

    $ add_seen_chapter("3-4")



    python:
        set_info_scene("35")
        set_info_date(5, 20, "sun")
        set_info_time("morning")
        set_info_location("05")






    stop music fadeout 2
    scene bg myroom morning with fade_longest
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()



    "目覚めた時、私は心の中にぽっかりと穴が空いたような感覚があった。"

    "夢は見なかった、と思う。"

    "もし見ていたとしたらそれはきっと悪夢で、私は自分で見なかったことにしたのだろう。"

    show rnk paj nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「店を開けよう」"

    "平常心で、活動開始することができた。きっと、働いていれば余計なことを考えずにすむと、自分で分かっていたのだろう。"



    python:
        set_info_time("noon")
        set_info_location("04")





    stop music fadeout 1
    scene bg lion01 noon with fade_long
    play music audio.nichijo01
    pause 1



    $ show_hud()

    "昼時。"

    "食事メニューが少ない今は、お客さんは一旦減る時間帯だった。"

    show rnk apr nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「いらっしゃ……あ」"

    show kik sta nor nor rev at std_cl with std_in

    voice get_voice_filename("kik")
    keiko "「１人……いいえ、２人ね。いいかしら？」"

    "瓶淵桂子さん。子供を連れて、２人だった。お客さんとして断る理由もなく、私は彼女をテーブル席に案内した。"

    scene ecg coffee sip with dissolve_long

    "コーヒーの注文を受けて、私はいつも通りにコーヒーを淹れた。同情や悲しみなど、余計な感情が注がれないように。"

    scene ecg girlstalkW1 smi with dissolve


    voice get_voice_filename("kik")
    keiko "「……美味しいわね」"

    "赤ちゃんには、何もいらないらしい。当たり前か。うちには赤ちゃんに出せるメニューもないのだし。"

    show ecg girlstalkW1 ge2 with ecg_change


    voice get_voice_filename("kik")
    keiko "「ねえ。少しお話いいかしら」"


    play music audio.commit

    "他にお客さんもいないし、これも断る理由はなかった。"

    show ecg girlstalkW1 ge1 with ecg_change


    voice get_voice_filename("kik")
    keiko "「実は私ね、カードを見たときからあなたの名前を素敵だって思ってたのよ」"


    voice get_voice_filename("rnk")
    rinka "「どうしたんですか、急に」"

    show ecg girlstalkW1 smi with ecg_change


    voice get_voice_filename("kik")
    keiko "「伝えておきたかったのよ。凛という字に……火。でも、夢の世界で見たあなたは不安げなだけの子供で、似合っていないって思っちゃったわ」"

    show ecg girlstalkW1 smi with ecg_change


    voice get_voice_filename("kik")
    keiko "「ちょっと残念だって思ったの。全然凛としてないなって」"

    "私は少しむっとしたが、言い返すことはできなかった。"

    "夢の世界での私は、よっぽど弱々しく見えたことだろう。"

    show ecg girlstalkW1 ge2 with std_change


    voice get_voice_filename("kik")
    keiko "「でもね、実際に会ったあなたは違った。あなたの瞳は、あの世界の誰よりも凛としていた。あなたの言葉は、誰よりも燃えていた」"





    voice get_voice_filename("rnk")
    rinka "「桂子さんは、名前は人に一生寄り添うものって言いましたね。実は私のおばあちゃんも、名前に恥じないようにしなって口癖のように言っていました」"

    "桂子さんの言葉を聞いて、私はそんなことを思い出していた。"

    show ecg girlstalkW1 smi with ecg_change


    voice get_voice_filename("kik")
    keiko "「……いいおばあちゃんね。ずっと大切にするのよ。あなたの名前を」"

    "桂子さんはそこまで言うと、コーヒーを最後まで飲み干した。"

    show ecg girlstalkW1 ser with ecg_change


    voice get_voice_filename("kik")
    keiko "「一つ、お願いがあるの」"


    voice get_voice_filename("rnk")
    rinka "「お願い……ですか？」"

    show ecg girlstalkW1 let with ecg_change


    voice get_voice_filename("kik")
    keiko "「ええ。この手紙を……預かって欲しいの。それで面倒かもしれないけれど、あなたに書き写してほしい」"


    voice get_voice_filename("kik")
    keiko "「夫と……子供へのメッセージを書いたの。でも、私が脱落したら消えてしまうでしょ？」"


    voice get_voice_filename("kik")
    keiko "「住所と宛名は中に書いてあるから、それを書いて送ってもらえればいいわ」"

    show ecg girlstalkW1 ge1 with ecg_change


    voice get_voice_filename("kik")
    keiko "「今晩私が脱落すれば、明日は私が死んでから３週間ということでしょう？」"

    show ecg girlstalkW1 ser with ecg_change


    voice get_voice_filename("kik")
    keiko "「この子が生まれてから１４日以内に出生届を出さないといけないから、もう名前は決まってしまっているでしょうけれど、せめて想いだけでも伝えたいの」"

    "桂子さんは、子供のことを春樹とは呼ばなかった。"

    "どんな想いがあるのかは知らない。ただ、桂子さんが脱落したとき、彼女の命名がなかったことになるのは確かだ。"


    voice get_voice_filename("rnk")
    rinka "「諦めるん……ですか？」"

    show ecg girlstalkW1 ge1 with ecg_change


    voice get_voice_filename("kik")
    keiko "「いいえ。あの男の情報を３つ探し出せば身を守れる。これまでも調べなかったわけじゃないのよ。ほとんど結果は出なかっただけで。半ば諦めていたけど、これから今日一日は探すことにするわ」"

    show ecg girlstalkW1 smi with ecg_change


    voice get_voice_filename("kik")
    keiko "「でも、きっと無理。それくらい分かるわ」"

    show ecg girlstalkW1 ge2 with ecg_change


    voice get_voice_filename("kik")
    keiko "「手伝おうなんて……言うのは駄目よ」"





    voice get_voice_filename("rnk")
    rinka "「言いませんよ。だって……もしあの人に見つかったら、今度こそ協力者だと思われます。そしたら、そのまま私も狙われる」"



    voice get_voice_filename("rnk")
    rinka "「私が脱落したら、桂子さんのお願い……聞けませんから」"

    show ecg girlstalkW1 smi with ecg_change

    voice get_voice_filename("kik")
    keiko "「ええ、ありがとうね」"

    "桂子さんは満足げに微笑んでから、続けた。"

    show ecg girlstalkW1 ge1 with ecg_change

    voice get_voice_filename("kik")
    keiko "「お礼になるか分からないけれど、私が唯一突き止めた情報を教えるわ」"

    show ecg girlstalkW1 ser with ecg_change

    voice get_voice_filename("kik")
    keiko "「あの男の名前は、『アラン・スコーピオン』。親から受け継いだ宝石会社をたった数年で世界規模の企業に持ち上げたインドの若き天才経営者だそうよ」"

    python:
        add_character_cards("kik", ["12_name"])
        add_character_cards("aln", ["12_name"])

    show ecg girlstalkW1 ge1 with ecg_change

    voice get_voice_filename("kik")
    keiko "「顔さえ分かれば……すぐに見つかる情報。インターネットにも書いてあるしね」"

    show ecg girlstalkW1 ge2 with ecg_change

    voice get_voice_filename("kik")
    keiko "「偶然よ。雑誌に目を通していたら、彼の写真が載っていたんだもの。選定が始まるずっと前に撮影したものでしょうけど」"


    voice get_voice_filename("rnk")
    rinka "「アラン・スコーピオン……。それがあの人の名前……！」"

    show ecg girlstalkW1 ge1 with ecg_change

    voice get_voice_filename("kik")
    keiko "「ええ。私が教えるのはこれだけ。あなたへのお礼よ。私の脱落が決まったわけではないものね」"

    show ecg girlstalkW1 ser with ecg_change

    voice get_voice_filename("kik")
    keiko "「それに私はあなたにお願いをしたとはいえ――あなたに賭けてもいるわ」"



    scene bg lion01 noon with dissolve_long

    "それ以上、多くの言葉はいらなかった。"

    "桂子さんが何を決意し、何を私に託したのか。"

    "そんなことは、もうとっくに分かっていたのだ。"

    show kik sta nor ser rev at std_cl with std_in

    voice get_voice_filename("kik")
    keiko "「それじゃあね。お願い……よろしくね」"

    hide kik with std_out

    "あっさりと、桂子さんは去って行った。"

    "私は、彼女から受け取った手紙を握りしめていた。"

    "ただの紙だから、決して重くなんてなかった。"

    "誰かを脱落させなければいけないと悩むことに比べれば、彼女の想いを背負う方がよっぽど前向きになれた。"

    "会話が少なかったからこそ、彼女の願いは私に届いたのだった。"

    show rnk apr nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「凛と――」"

    "私は背筋を伸ばした。"

    "自分の名前に負けないように。"

    "ここからは一人の戦いだ。"








    python:
        set_info_time("night")
        set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "夜、自室に戻ると、カードブックは強い光を放っていた。"

    "案の定、その時≪Ⅻ・氏名：アラン・スコーピオン≫というカードが作られた。"

    $ add_character_cards("rnk", ["12_name"])

    "桂子さんの言っていた通り、私はインターネットで検索をかけてみることにした。"

    "あの屈強な男性の名前は、思ったよりもずっと多い数が検索にヒットした。"

    show rnk paj sur su1 at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「こんな簡単に……」"

    "とはいえ、そこから先は容易ではなかった。"

    "16歳の頃に会社を受け継ぐまでの情報は分からなかったし、いかにして彼が３週間前に亡くなったかも当然分からない。未練なんてもっと謎だ。"

    "これはまた図書館に行き、新聞や雑誌を調べてみた方がいいかもしれない。国や職業、何より名前が分かったのだから大きな前進だ。"

    "今日中にやるべきことがある。それは、桂子さんの手紙を書き写すことだった。"




    stop music fadeout 1
    scene bg myroom night
    with fade_long
    play music audio.commit
    pause 1


    show rnk paj arm nor at std_c with std_in
    voice get_voice_filename("rnk")
    rinka "「――よし」"

    "書かれていたのは、息子や夫への想い。"

    "生前の知人を装い、伝聞の形式で書かれていた。旦那さんが受け取っても受け入れられるように、きちんと考えられていた。"

    "丁寧でしっかりとした字は、彼女の今までの生き様が現れているかのようだった。"

    "そして末文に書かれた私への「ありがとう」というメッセージが、目の奥を熱くさせた。"

    "母親が果たすべき責任を果たせなかったことへの、後悔。"

    "言葉では書かれていなかったが、手紙の裏にこめられた彼女の想いを感じていた。"

    "子供のために生きる覚悟が、母親の愛になるのだろうか。"

    "愛の次に与えられるものはきっと、名前だ。"

    "名前は一生寄り添うものだからこそ、きっと桂子さん自身から授けたかったのだろう。"

    "家庭によって色々な形はあるけれど、桂子さんの名前への思いは何よりも強かった。だからこそ、未練にまでなった。"

    "昼間の話を思い出す。私の名前。"

    "それは、私がこの命以外で唯一、母親からもらったものだとおばあちゃんは言っていた。"

    "だとすればきっと、私も母親の覚悟と愛を受けて生まれてきたのだろうか。"

    "私もいずれ、誰かにそんな愛を捧げるのだろうか。"

    "私は黙って、首を振った。"

    "このままでは答えの出ない思考の深みにはまってしまう。"

    show rnk paj nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私の、未練は――」"

    "この疑問も、同じだ。"

    "きっと私自身が自分のことをまだよく分かっていないから、未練のカードは作られないのだ。"

    "自分の未練が分かったとき初めて、私は生きる理由を誇れるのかもしれない。"

    "でも、最後まで分からなくたって。"

    "いや、だからこそ私は生きたい。"

    "桂子さんの手紙を読んで、私はようやく固い決意ができた。"

    show rnk paj arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「自分が何者か分からないまま死ぬのは……嫌だよ」"

    "もし、桂子さんが今夜脱落したのなら、私はこの手紙を投函する。"

    "まずやるべきことは……それだ。"

    "そして私は、眠りの中へと落ちていった。"

    $ add_seen_chapter("3-5")

label sentei3:

    call set_replay










    python:
        set_info_date(5, 20, "sun")
        set_info_scene("36")
        set_info_time("lnight")
        set_info_location("07")


    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    "アランは、無表情のままその場所に立っていた。"

    "運命の大広間。夢の世界が女神の力により具現化した場所だ。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro smi big at std_c with std_in

    voice get_voice_filename("dia", 68)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "透き通った声が響く。"

    "女神パルカは、純粋無垢な笑顔で選定の参加者を迎えた。"

    show dia sta fro sm2 big with std_change

    voice get_voice_filename("dia")
    parca "「この選定も今宵で３度目。順調に進んでいた選定も、そろそろ不協和音が響く頃でしょうか？」"

    scene bg fatalhall01 up with dissolve

    show mhr uni sco con rev ci at ci_l with ci_in


    voice get_voice_filename("mhr", 89)
    miharu_num "「相変わらず、君は思わしげなことを言うね。本当は何も考えていないだけなんだろう？」"

    show dia sta nor ama ci at ci_c with ci_change

    voice get_voice_filename("dia")
    parca "「あら？　そうだとして貴女サマに関係がありまして？」"

    "Ⅱの少女がパルカと会話しているのをアランは見ていた。そしてその隣のⅠの少女のことも。"

    "最初の選定の時に彼女たちが話していたのを聞いていたから、知り合いなのは分かっていた。"

    "Ⅱの少女の方は想像以上に用心深く、アランはまだ何の手がかりも得ていない。反対に、Ⅰの少女はわざわざ別の参加者のためにリスクを負った。"

    "きっと脱落させるだけなら容易だろうとアランは思っていた。だが一方で彼はⅠの少女が気になっていた。"

    "桂子を追い詰めたとき、Ⅰの少女がアランの前に立ち塞がった。その瞳はどうしてか、すごく――。"

    scene ecg parcadeclaration at top with dissolve_long

    voice get_voice_filename("dia")
    parca "「それでは、今宵も選定を始めましょう」"

    "静かな声で告げた女神に、アランは思考を遮られた。"

    "そして自分が余計なことを考えていたと判断し、目の前のことに集中した。"


    voice get_voice_filename("dia")
    parca "「廻れ！　運命の大時計よ」"






    play music audio.restlessness 
    scene bg fatalhall01 normal with dissolve_long

    "Ⅰから順番に指名の意志確認が行われる。"

    "女神は順番で有利不利がつくことはないと言っていたが、アランはそれを間違いだと思っていた。"

    "重複指名になった時、≪自身のカード≫をオープンにした方が優先権を得るルールがある。"

    "しかし番号が後であれば、そもそも重複指名を避けることができる。"

    "指名を受ける者が指名者にとって有用なカードを持っていることが判明しているときのみ、リスクを負えばいい。"

    "アランのⅫという番号は、その点では有利なのであった。"

    scene bg fatalhall01 up with dissolve

    show aln sta nor irr rev ci at ci_l with ci_in

    voice get_voice_filename("aln", 34)
    alan "「……ふん」"

    "アランは、Ⅰの少女が桂子を指名する可能性も想定していた。"

    "もし彼女が桂子のカードを３枚手に入れていれば、アランとの重複指名を起こすことができる。"

    "アランが引けば桂子の脱落を防ぎ、攻めてもアランのカード１枚を公開させられる。"

    "だから仮にⅠの少女が桂子を指名する意志を見せたら、アランは今回は指名を行わない予定だ。"

    "桂子が持っているカードを得るメリットよりも、重複指名のデメリットの方が大きい。"

    "アランは自分が有名人であることを自覚している。当然桂子が自分の名前くらいは調べていることを予想していた。桂子からⅠの少女にそれが伝わっていることも。"

    "だが反対に、桂子はアランの名前しか分かっていないとも予想している。"

    "とすれば、Ⅰの少女にとって自分が桂子を脱落させるという想定外の状況になったとして、彼女が新しく得るアランの情報はない。"

    show rnk uni nor nor ci at ci_r with ci_in


    voice get_voice_filename("rnk", 414)
    rinka_num "「私は――指名しません」"

    hide rnk with ci_out

    "Ⅰの少女は結局、指名を行わなかった。"

    "アランにとっては予想外ではない。先ほど想定した状況の方が可能性は低いと思っていたからだ。"

    "順番は回り、前回指名を行ったⅪの女性も今回はパスをした。"

    show ode sta arm smi ci at ci_r with ci_in

    "アランが現状一番警戒しているのはこの女性だ。肉体からして只者ではなく、不遜な態度も常人ではありえない。"

    "その証拠に、彼女は順番がアランに移る時にわざわざウインクを飛ばしてきた。"

    hide ode with ci_out

    show aln sta nor irr rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「……挑発には乗らない」"

    "アランは自分にだけ聞こえるような小さな声で言った。"

    show dia sta nor ama ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「貴方サマはいかがですか？」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「僕は――Ⅷの女を指名する」"

    "そして、彼は静かに告げた。"

    "地響きのような音を立て、アランの立つ床が動き始めた。"









    $ set_info_location("16")

    stop music fadeout 1
    scene bg fatalhall02 normal with fade_long
    play music audio.fatalhall
    pause 1

    "運命の大広間の上層に、アランと桂子の二人が床ごと上がって来ていた。"

    "女神は気付いた頃にはそこにいて、微笑を浮かべている。"

    "アランは、桂子が意外にも落ち着いていることに僅かの驚きを見せていた。"

    "彼が桂子の名前のカードを手に入れたとき、あれほど絶望してうなだれていたというのに。"

    "彼は、彼女が以前脱落させたチャンのように大騒ぎするものかと思っていた。"

    scene bg fatalhall02 up large with dissolve

    show dia sta fro no2 big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それでは、指名をどうぞ」"

    "２回目であるアランは、すでに手順は分かっていた。"

    "光に包まれたカードが空中に留まっていて、その中から相手のカードを読み上げる。"

    "ただし、脱落したチャンのカード３枚だけは、光をまとっていなかった。"


    play music audio.electing

    scene ecg senteialan nor with dissolve_long

    voice get_voice_filename("aln")
    alan "「ケイコ・カメブチ。死因は脳出血だ」"

    "桂子の氏名と死因のカードが、光の中で反応する。"


    voice get_voice_filename("aln")
    alan "「未練は――」"


    scene bg fatalhall02 up
    show kik sta nor nor ci at ci_r
    with dissolve_long


    voice get_voice_filename("kik", 113)
    keiko "「ねえ。あなたにも親がいるでしょう？　家族がいるでしょう？」"

    "桂子の問いかけで、アランの言葉は一瞬止まった。"

    show aln sta nor irr rev ci at ci_l with ci_in

    voice get_voice_filename("aln")
    alan "「余計なことを話すな」"

    show kik sta nor nor ci with ci_change

    voice get_voice_filename("kik")
    keiko "「私は脱落して――元の死の運命に戻るけれど、怖くはないわ。息子がいるもの。ほんの僅かな時間だったけれど、私は母親だった」"

    show kik sta nor ser ci with ci_change

    voice get_voice_filename("kik")
    keiko "「名前はつけてあげられなかったけれど……きっと強く育つわ。名前はその人の本質ではなくあくまで願望、希望だもの」"

    show kik sta nor nor ci with ci_change

    voice get_voice_filename("kik")
    keiko "「あなたにも名前を付けた両親がいるでしょう？　ご両親のためにも、せめて無関係な人を傷付けるのはやめてちょうだい」"

    show aln sta nor ang rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「両親のために？　すでに死んだ親のために何かできるとでも？」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「死んだら全てが終わり。無だ。だから生きている人間はすべからく自分の目的を達成するために生きているべきだ」"

    "桂子の言葉に、アランは怒りを覚えていた。変わらず無表情に見えるが、彼の瞳は確かに奮い立っていた。"

    show aln sta nor irr rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「自分のために。そして守るべきものを守るために。僕はなんだってする」"

    show aln sta nor ang rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「――無関係の人間を殺そうが、無関係なところでどんな嘆きが生まれようが、それこそ僕には無関係のことだ」"

    "昏い声で、アランは言った。興奮してはいるが、感情はほとんど言葉には乗らなかった。"

    "アランはあくまで冷徹に振る舞っていた。"

    "彼に対し、桂子は微笑んで言った。"

    show kik sta nor lau ci with ci_change

    voice get_voice_filename("kik")
    keiko "「あなた、無理してるわね？」"

    scene ecg senteialan nor with dissolve_long


    voice get_voice_filename("aln")
    alan "「お前の未練は子供の名前、だ」"

    "アランは桂子の言葉を遮るようにして、言った。"

    scene ecg trianglecard small with dissolve

    "直後、３枚のカードが空中を動き出す。"

    "大広間の中心まで移動したカードはそこで静止し、正三角形を作った。"

    show ecg trianglecard cover with ecg_change_wait

    "カードは一枚一枚が強い光を放ち、大広間を包み込む。"

    "アランはその後に何が起こるかを知っていた。そのため、彼は目を瞑って意識を委ねることにした。"








    stop music fadeout 2
    scene white with Dissolve(3)
    play music audio.death
    pause 2

    scene ecg croomcelling hos with dissolve_longest

    "かすんだ視界に、生まれたばかりの子供の顔が見えた。彼女のいる緊急治療室に、看護師さんがベッドに寝た赤ちゃんを連れて来ていたのだ。"

    "産声をあげる赤ちゃんはまるで天使のようで、それそのものが希望の象徴のようだった。"


    voice get_voice_filename("kik")
    keiko "「は……る……き……」"

    "最期の言葉は、言葉になっていたのかすら分からないほどか弱かった。"







    stop music fadeout 12
    scene bg fatalhall02 up
    show aln sta nor irr rev ci at ci_l
    with fade_longest
    play music audio.restlessness
    pause 1


    voice get_voice_filename("aln")
    alan "「名前は希望じゃない。人を縛る鎖だ」"

    "だからこそ、アランは相手から取得するカードに氏名を選んだのだ。"

    "選定のシステム上、未練のカードを手に入れるのが一番難しいことは分かっていた。"

    "だが、名前は人を――名付けられたものを縛る鎖だと考えている。名を知れば自ずと人自身も知れてくると信じていた。"

    "Ⅰ・氏名。"

    "Ⅲ・未練。"

    "Ⅹ・死因。"

    "Ⅻ・氏名。"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「やはり知られていたか。だが……」"

    "彼は信念に則り、どのカードを選ぶかすでに決めていた。"








    python:
        set_info_scene("37")
        set_info_location("07")

    stop music fadeout 1
    scene bg fatalhall01 up with fade_long
    play music audio.fatalhall
    pause 1



    show rnk uni arm sad ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「桂子さん……」"

    "男性は指名を終え、一人でこの大広間へと戻って来た。"

    "私の名前が選ばれた。"

    "アラン・スコーピオンという男性が選んだのは、私の氏名のカードだったのだ。"

    $ add_character_cards("aln", ["1_name"])

    "死因や未練もあっただろうが、一度現実で出会ったことのある私の方が近いと踏んだのだろう。"

    "彼と同時に桂子さんを指名するという手もあった。"

    "彼が私の指名に乗って来てくれれば、桂子さんを脱落させないか、全員に≪自身のカード≫をオープンさせるという二択を迫ることになった。"

    "だが、意志確認の順番の矛盾に気付いている。私が桂子さんを指名すれば、きっとスコーピオンさんは乗って来ない。"

    show mhr uni pai irr rev ci at ci_l with ci_in

    voice get_voice_filename("mhr")
    miharu "「君の名前を……！」"

    show rnk uni arm nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「大丈夫」"

    "海晴は、スコーピオンさんを睨んでいた。"

    "状況が逆でも、海晴のために私は同じように彼のことを睨むだろう。"

    "だが、私は彼を睨むのではなく、その瞳をじっと見つめていた。"

    "こっちも彼の名前は知っている。私は、顔を知られて住んでいる地域まで知られたのだ。私の名前はいずれ知られていただろう。"

    "自分でも意外だが、体は震えていなかった。相変わらず冷徹で屈強な彼だけれど、目を逸らさずにいることができた。"

    "これは――私にとって無言の宣戦布告だった。"

    hide mhr
    show aln sta nor nor rev ci at ci_l
    with ci_swap

    voice get_voice_filename("aln")
    alan "「やはり――似ているな……」"

    "彼に問い掛けることはしなかった。"

    "彼が何を背負っているのか分からないが、今は話す気にはならなかった。"

    show dia sta fro nor ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者は１名。これをもって、選定を終了といたしましょう」"

    "程なくしてパルカが口を開き、選定の終了を告げた。"

    $ renpy.end_replay()
    $ add_seen_chapter("3-6")

    $ persistent.sentei3_clear = True
    $ grant_achievement("divine_selection_03")

    jump f004
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

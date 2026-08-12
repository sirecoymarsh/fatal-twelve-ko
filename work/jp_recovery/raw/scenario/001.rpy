

label f001:








    python:
        set_info_scene("00")
        set_info_time(None)
        set_info_location("01")

    play music audio.maintheme
    scene black
    pause 3
    scene ecg pattern nor a large:
        zoom 1.3
        yalign 0.5
        xalign 0.0
        subpixel True
        linear 150 xalign 1.0
    show smoke at smoke_rl(100, 0.6)
    with Dissolve(5)
    pause 1



    "一つの結果に到達するまでの過程を、人は物語や人生と呼ぶ。"

    "様々な出会いがあり、別れがあり、事件があり、選択があり、そして未来の可能性の中を進み、一つの結果へ到達する。"

    "この世界というのは――運命というのは、そういう風にできている。"

    "運命は変わらないから運命なんだ。どんなに理不尽でも。"

    "これまで生きてきた私の人生の中で起きたこと、その全ては何かの過程の結果なのだ。"

    "その途中で失われた可能性のことなんて、私は考えたことがなかった。"

    "たら、れば、かもしれないに思いを馳せるほど、壮絶な人生ではなかったのだ。"

    "物語は、人生は、たった一つだと思い込んでいた。"

    scene ecg pattern nor a large:
        zoom 1.3
        yalign 1.0
        xalign 0.5
        subpixel True
        linear 150 yalign 0.0
    show smoke at smoke_rl(100, 0.6)
    with fade_long
    pause 2

    "私の名前は、{rb}獅子舞{/rb}{rt}ししまい{/rt}{rb}凛火{/rb}{rt}りんか{/rt}。"

    "都内でそこそこ有名な女子校、私立{rb}飴茶{/rb}{rt}あめちゃ{/rt}女子大学付属高校の２年生だ。"

    "トップ高に入った優等生からほとんど学校に来ない問題児まで色々な人がいた中学時代とは打って変わり、ここでは大人しいお嬢様ばかりだ。"

    "そんな中、私は周囲から不良のレッテルを貼られていた。"

    "理由のひとつが――そしてそれがもっとも大きいのだけど――黒に金色のメッシュが入った髪にあった。"

    "地毛なのだから校則や偏見でとやかく言われることもないのだけれど、どうやら小学校からずっと女子校のお嬢様たちにはアバンギャルドに過ぎるらしい。"

    "服装や容姿に関する校則が緩いからこそ私は飴茶を選んだのに、実態は暗黙のルールだか伝統だかが染みついているから校則の規定がないというだけであった。"

    "入学したての頃こそ校則違反ではないのに見た目だけで不良扱いされることに腹を立てたが、３ヵ月も経たずに気にならなくなった。"

    "私には私の世界があるように、彼女たちには彼女たちの世界があることが分かったからだ。"

    "私が彼女たちの価値観を理解できないように、彼女たちもまた私の価値観を理解することはない。"

    "実のところ、これまでの私はそんな風に理解できるものだけを理解して生きていくのだと割り切っていた。"

    "だが、ある時を境に運命の歯車が大きく動き出すことになった。"

    "それは、ゴールデンウィーク直前のある日からだった――。"

    stop music fadeout 5
    scene black
    with Dissolve(5)
    pause 3



    python:
        set_info_scene("01")
        set_info_date(5, 2, "wed")
        set_info_time("evening")
        set_info_location("02")




    $ renpy.music.set_volume(0.5, channel = "se")
    play se "train-pass1" fadein .5
    pause 2

    scene bg station01 with dissolve_longest

    $ show_hud()

    show rnk uni nor que at std_cr with std_in


    voice get_voice_filename("rnk")
    rinka "「見て。駅の時計止まっちゃってる……故障かな？」"

    "改札口を抜けた先にあるアナログ時計に目を遣って、私は{rb}直未{/rb}{rt}なおみ{/rt}に話しかけた。"

    show nom gun que que rev at std_cl
    with std_in

    voice get_voice_filename("nom")
    naomi "「本当だ……凛火先輩、よく気付きましたね！　駅の時計が止まってるなんて珍しいのに」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「だよね。あ、ごめん、直未の話、遮っちゃったよね？　何の話だっけ？」"

    show nom gun nor smi rev with std_change

    voice get_voice_filename("nom")
    naomi "「えっと、あれですよ、あれ。あの……はははー、わたしも忘れちゃいました」"



    stop ambient
    $ renpy.music.set_volume(1.0, channel = "ambient")
    stop se
    $ renpy.music.set_volume(1.0, channel = "se")
    play music audio.nichijo01

    scene bg station01 large:
        zoom 1.3
        xalign 0.0
        yalign 0.3
    show nom gun nor smi rev up at std_c
    with wipe_rl

    "はにかみながら答えたのは、一つ年下の{rb}日辻{/rb}{rt}ひつじ{/rt}{rb}直未{/rb}{rt}なおみ{/rt}だ。"

    "後輩といっても部活や委員会で知り合ったわけではなく、ちょっとした偶然で私たちは先輩後輩の関係になった。"

    "私は上下関係とか気にしないから、友達って感じだけど。"

    "直未と私は、二人でうちへ向かう途中であった。いつものように駅の改札を抜け、ホームへと向かっている。"

    scene bg station01
    show nom gun fal sur rev at std_cl
    show rnk uni nor nor at std_cr
    with wipe_lr



    voice get_voice_filename("nom")
    naomi "「わきゃっ！」"

    show rnk uni cat sma with std_change


    voice get_voice_filename("rnk")
    rinka "「ちょっと」"

    "小さな悲鳴をあげた直後、直未は何もないところで転びそうになり、体が傾いた。"

    "私は直未の手を掴んで、体を支える。"

    "私の方が体が小さいのでちょっと引っ張られたが、直未もすぐ自分で体勢を整えていた。"

    show nom gun nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「す、すみません……」"

    show rnk uni arm nor with std_change


    voice get_voice_filename("rnk")
    rinka "「別に、謝ることじゃないよ」"


    voice get_voice_filename("nom")
    naomi "「あ、ありがとうございます！」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「それもなんか大げさ」"

    "直未はいつもどこかおどおどしていて、そのせいで注意力散漫なのか分からないが――よく転ぶ。"

    "小動物みたいで、どちらかというと守ってあげたくなるタイプだと思う。"

    show nom gun hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「それで、その……」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「ん？　どうしたの？」"

    show nom gun hes shy rev with std_change

    voice get_voice_filename("nom")
    naomi "「えっと……手……」"

    "直未を支えたときからずっと、手を握ったままでいたみたいだ。"

    show rnk uni nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、ごめん。痛かった？」"

    show nom gun hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「い、いえ！　全然……痛くはない、ですけど……」"

    "直未はうつむいたまま、そう答えた。"

    "自覚はなかったがちょっと強く握り過ぎたかもしれないと思い、私は恐る恐る手を離した。"

    show nom gun har con rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ！　そ、その！」"

    show nom gun nor sur with std_change

    voice get_voice_filename("nom")
    naomi "「で、電車が来そうですし。い！行きましょう！」"

    "直未は転んだときにずれた眼鏡の位置を両手で直すと、慌てた調子でホームの方を指さした。"

    "１分前の繰り返しになるが、こういう時は大体――。"

    show nom gun fal sur with std_change_wait
    hide nom with DissolveMoveOut(0.5, yoffset(200), easein)

    play se "taoreru08"

    voice get_voice_filename("nom")
    naomi "「きゃっ！」" with quake_fast

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「もう、落ち着かないから！」"

    hide rnk with std_out

    "直未が歩き出したのと同時に通りかかった人にぶつかってしまう。"

    "しかも、今度はぶつかった相手と一緒に転んでしまった。"


    show nom gun hes sor at std_c with std_in
    voice get_voice_filename("nom")
    naomi "「す、すみません！」"

    show rnk uni nor apo behind nom at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「ごめんなさい、私の後輩が……」"

    hide rnk
    hide nom
    with std_out

    "私は、起き上がろうとする直未たちの方へ近づいた。"

    "直未にぶつかられた相手は、直未よりも年下の少女に見えた。背丈は私とそう変わらないが、顔つきがもう少し幼かった。"

    "直未も大きな目のせいで高校生ではなく中学生に間違われがちだが、それよりも明らかに幼い。"

    show yuu sta sac non rev at std_l
    with std_in



    voice get_voice_filename("yuu")
    yuu_unk1 "「…………」"

    show rnk uni arm ama at std_c with std_in


    voice get_voice_filename("rnk")
    rinka "「あ、あの。大丈夫かな？」"

    scene bg station01 large:
        zoom 1.3
        xalign 0.0
        yalign 0.6
    show yuu sta sac non up rev at std_c
    with wipe_lr

    "声をかけた時、少女と目が合った。目は薄い色をしていた。帽子で隠していたが、見れば、髪も特徴的で綺麗な白髪だ。"

    "正面からしっかり見ると、幼いながらもそのはっきりとした目鼻立ちが際立った。"

    "恐らく、日本人ではないのだろう。ということは髪の色も地毛かもしれない。"

    show yuu sta sac non up rev with std_change



    voice get_voice_filename("yuu")
    yuu_unk1 "「…………」"

    "直未と異なり、少女は背中から転んでいた。"

    "後ろからぶつかられたのだが、転んだ時に素早く身を反転させ、背負っていたリュックを抱えて守っていたようだ。"

    "ずいぶん大きな荷物だ。恐らく、旅行者だろう。"

    "鞄の中にカメラなどの壊れやすいものが入っているために、荷物をかばったのかもしれない。"

    "一人でいるということは、家族で日本に来ていてはぐれてしまったのだろうか。"

    "リュックには鍵の形をしたキーホルダーがついていた。"

    "少女はすぐにすっくと立ち上がって、自分のかばった荷物を抱えたままこちらを睨むように見つめていた。"

    show yuu sta sac non up rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk2 "「…………」"

    scene bg station01
    show rnk uni nor nor rev at std_c
    show yuu sta sac non rev at std_l
    with wipe_rl


    voice get_voice_filename("rnk")
    rinka "「直未、ほら、ちゃんと謝らないと」"

    "直未は慌てていたのもあり立ち上がるのに手間取っていたようで、結局私の手を借りて体勢を整えた。"

    show nom gun hes sor behind rnk at std_r with std_in

    voice get_voice_filename("nom")
    naomi "「ほっ、本当にごめんなさい……あれ、外国の人？　わたしの言葉通じてっ……、こういう時はその、ソーリー？　パードン？」"

    show rnk uni arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「直未、とりあえず落ち着きなって」"

    scene bg station01 large:
        zoom 1.3
        xalign 0.0
        yalign 0.6
    show yuu sta sac ten up rev at std_c
    with wipe_lr



    voice get_voice_filename("yuu")
    yuu_unk2 "「…………」"


    "少女は直未がひととおり言い終えて頭を下げるのを見ていたが、言葉は発しなかった。"

    "何やら訴えたいようだったが、彼女は黙ったままだった。"

    hide yuu with std_slide_out_lr
    scene bg station01 with wipe_rl

    "そして、結局私たちの謝罪が通じたのがどうか分からないまま、ホームの方へと早足で去っていった。"

    "少女は一度だけ振り返ったが、直未ではなく私と目が合ったようだ。"

    "人混みの中に紛れてもしばらくはその容姿のおかげで目立っていた。"

    "同じように私の髪も目立つから、見つけやすかったのかもしれない。"

    "親の元へ向かったのか、それともまさかあの歳にもかかわらず一人で日本へ来たのかなど、何も分からないままであった。"

    show nom gun hes sor rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「あの、ごめんなさい……」"


    show rnk uni nor que at std_cr with std_in
    voice get_voice_filename("rnk")
    rinka "「私に謝っても仕方ないって。ま、あの子にもちゃんと謝ったし、怪我もしてないみたいだから大丈夫じゃないかな」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「とはいえ、気をつけなね？　直未はいつも焦り過ぎなんだから」"

    show nom gun har pin rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい！　石橋を叩いて壊すくらいに、慎重に歩きます」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「それ、意識し過ぎて絶対転ぶパターンだから」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、あの子……見えなくなった」"

    show nom gun que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「さっきの男の子、どうかしたんですか？　まさか本当は怪我してたとか……」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「男の子？　いや女の子じゃなかった？」"

    show nom gun hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「あれ！　でも綺麗な顔立ちだったから女の子って言われても納得です。わたし……ま、また失礼なことを」"

    if persistent.TRUE_clear or persistent.UNHAPPY_clear or persistent.MIHARU_clear:



        show rnk uni arm nor with std_change

        voice get_voice_filename("rnk", 18)
        rinka "「そう言われると、私も男の子な気がしてくる――って、前にもこんな会話しなかったっけ？」"

        "私は「いや、まあそれはいいとして」と挟んでから続けた。"

        show rnk uni nor que with std_change

        voice get_voice_filename("rnk")
        rinka "「あの子くらいの年の旅行者っぽい人が一人でいるなんて珍しいから、ちょっと気になっただけだよ」"

        show rnk uni arm vig with std_change

        voice get_voice_filename("rnk")
        rinka "「それに、どこかで会ったことがあるような気がして」"

        show nom gun que que with std_change

        voice get_voice_filename("nom", 18)
        naomi "「……先輩、デジャブなんじゃないですか？　この路線って観光の人も多いですし、似たような会話をしててもおかしくなさそうです」"

        show rnk uni nor nor with std_change

        voice get_voice_filename("rnk")
        rinka "「あー、確かに{rb}海晴{/rb}{rt}みはる{/rt}か{rb}真央{/rb}{rt}まお{/rt}と話してるかもね」"

        "二人とも、直未と面識のある私の同級生だ。"


    "話が落ち着いたところで、電車の到着する音が聞こえてきた。直未も気付いたようで、二人の足は自然とホームへ向く。"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk", 22)
    rinka "「私たちも行こうか。今度は転ばないでね？」"

    show nom gun nor smi rev with std_change

    voice get_voice_filename("nom", 19)
    naomi "「はい！」"

    "それ以降は特に、ぶつかった彼女もしくは彼のことを気にかけることはなく、私たちは新宿方面の電車に乗った。"






    python:
        set_info_scene("02")
        set_info_time("evening")
        set_info_location("03")

    stop music fadeout 1
    scene bg train normal with fade_long
    play ambient "train-driving1" fadein 2
    pause 1

    "私たちが乗り込んだのは、{rb}王塚{/rb}{rt}おうつか{/rt}駅。"

    "そこから環状線で数駅の新宿で乗り換えて、地下鉄で２駅のところに私の家はある。"

    "時刻は午後5時頃。帰宅ラッシュと重なるせいで、環状線は大混雑だ。"

    "直未と私はほぼ密着状態で電車に揺られていた。"

    show nom gun hes sor rev at std_cl
    with std_in

    voice get_voice_filename("nom")
    naomi "「ご、ごめんなさい、わたしが遅くなっちゃったからラッシュに巻き込まれちゃって……」"

    show rnk uni nor smi at std_cr
    with std_in

    voice get_voice_filename("rnk")
    rinka "「いや直未が謝ることじゃないし。私だって慣れっこだから気にしなくていいよ」"

    show nom gun hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「す、すみません……」"

    stop ambient
    scene bg train large:
        zoom 1.5
        align (0.9, 0.35)
    show rnk uni nor que up at std_c
    with wipe_rl
    play music audio.gimon


    voice get_voice_filename("rnk")
    rinka "「ってあれ、そこにあるのって」"



    scene bg train large:
        zoom 1.5
        align (0.4, 0.5)
    with wipe_lr

    "人混みの中に、見覚えのあるリュックサックを見つけた。"

    "リュック自体はよくある形なので、正確には鍵のモチーフのキーホルダーに見覚えがあった。"

    "案の定、さっきの子の姿もそこにあった。"

    "大きなリュックを体の前に抱えて、車両の真ん中でうつむいていた。"

    "吊革に手は届かなそうだったが、人に挟まれているせいで転ぶこともなさそうだ。"

    scene bg train
    show rnk uni nor nor at std_cr
    show nom gun hes sor rev at std_cl
    with dissolve


    voice get_voice_filename("rnk")
    rinka "「同じ車両だったんだ」"

    show nom gun que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「え？　どうしたんですか？」"

    stop music fadeout 2.0
    scene ecg bomb sil with dissolve_long




    voice get_voice_filename("rnk")
    rinka "「あれ？　あの子……リュック開いちゃってるな」"

    "満員電車で揉まれているうちに、リュックのチャックが開いてしまったのだろうか。"

    "それどころじゃないのか、あの子は気付いていないようだった。"

    "周りの乗客も、その子のリュックのことなんて興味がなさそうだった。視界にすら入っていないのだろう。"

    "新聞を読んだり、中吊りを見たりして時間を潰している。一番多いのはスマートフォンではあるけれど。"

    "私も、さっき直未がぶつからなかったら意識していなかったと思う。"

    "だからあの子が何をしているのかは、私だけが目撃していた。"

    "追い詰められたような、深刻な表情も――。"

    scene ecg bomb nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「機械……？」"


    play music audio.kinpaku

    "リュックの隙間から、何か真っ黒い物がのぞく。"

    "カメラやパソコンなどではない。"

    "直感的に、私はフィクションの世界だけでしか見たことのない物の姿を思い出した。"

    scene bg train large:
        zoom 1.5
        align (0.9, 0.35)
    show rnk uni nor que up at std_c
    with wipe_rl_fast


    voice get_voice_filename("rnk")
    rinka "「爆――」"

    "私が思わず口走ったのとほぼ同時であった。"

    "リュックの中から閃光が走る。"




    scene bg train normal
    show rnk uni nor que at std_cr
    show nom gun que que rev at std_cl
    with dissolve


    voice get_voice_filename("nom")
    naomi "「ばく？」"

    show rnk uni cat ten with std_in

    voice get_voice_filename("rnk")
    rinka "「直未っ！」"

    stop music fadeout 1
    play se "bomb2"
    show layer master at quake
    scene white with dissolve_fast
    pause 3




    stop se
    play se "high_pitch" fadein 2

    "その瞬間だった。"

    "車内に身の焼けるような熱がほとばしる。"

    "直後、鼓膜を破裂させるほどの轟音が響く。"

    "私は直未に覆い被さりながら彼女を突き飛ばした。"

    "自分の体が衝撃と熱に押しのけられるのを感じた。"

    "――それは、文字通り体が焼けていく瞬間であった。"



    scene black with dissolve
    pause 2

    play music audio.firedeath fadein 2
    pause 2
    play se "fire_lite_shot_02"
    play ambient "fireloop" fadein 2
    pause 2
    scene bg train enjo
    with Dissolve(5)
    pause 2





    "炎の中に、自分の意志だけが置き去りにされていた。"



    voice get_voice_filename("nom")
    naomi_unk1 "「――ぱい！」"

    "声が聞こえる。"

    "私に感覚はなかった。"

    "衝撃を受け、痛みを感じ、体が焼かれていった記憶はあった。"

    "だが、もう、そのどれも感じなくなっていた。"




    voice get_voice_filename("nom")
    naomi_unk1 "「――ぱい！」"

    "意識も朦朧としている。"

    "いやきっと、すでに私の意識は消えてしまっているのだろう。"

    "これは、残り香のようなもの。"

    "炎に揺らぐこの世界の中で、弾けては消えていく火の粉よりも儚いもの。"




    voice get_voice_filename("nom")
    naomi_unk1 "「せんぱい！　せんぱい！　凛火せんぱい！」"

    "薄れた視界も、徐々に消えていく。"

    "落ち葉が風に吹かれていくように、私の意識もどこかへ飛んでいくのだろう。"

    "はっきりとしたその声が聞こえたことに、安堵して。"


    play se "fire_heavy_shot_04"
    stop music fadeout 5
    stop ambient fadeout 5
    scene white with Dissolve(5)
    pause 2

    "私の運命はこの時、確かに終わりを迎えた。"

    scene black with dissolve_longest
    pause 5



    $ renpy.movie_cutscene("movies/OP.mkv")
    scene white
    pause 5
    window auto




    python:
        set_info_scene("03")

        set_info_time("evening")
        set_info_location("04")

    $ show_hud()




    voice get_voice_filename("mao", 1)
    mao_unk1 "「りーたん、おーい、りーたん、凛火ぁ～？」"





    voice get_voice_filename("nom")
    naomi_unk2 "「凛火先輩？」"

    "まどろみの中から、私の名前を呼ぶ声が聞こえた。"

    "声の主は、顔を見なくてもはっきりと分かった。"



    voice get_voice_filename("mao")
    mao_unk1 "「いい加減起きれ！」"


    voice get_voice_filename("rnk")
    rinka "「……いてっ」"



    play music audio.nichijo01
    scene ecg girlstalkA1 su1 with dissolve_longest

    "おでこにぴしっという痛みを感じて、私は顔を上げた。"

    "しばらくひりひりとした痛みが残りそうだ。"

    show ecg girlstalkA1 su1 with ecg_change

    voice get_voice_filename("rnk")
    rinka "「あれ？　火事は？」"

    scene ecg girlstalkB1 smi glo with dissolve


    voice get_voice_filename("mao")
    mao_unk1 "「火事～？　何言ってんのぉ？　変な夢でも見た？」"


    voice get_voice_filename("rnk")
    rinka "「夢？　ってことは私……寝てた？」"

    show ecg girlstalkB1 uwa glo with ecg_change

    voice get_voice_filename("nom")
    naomi "「ち、ちょっとだけ……」"

    show ecg girlstalkB1 uwa blu with ecg_change


    voice get_voice_filename("mao")
    mao_unk1 "「りーたんに気なんて遣わなくていいからね～、なおりん」"

    show ecg girlstalkB1 smi glo with ecg_change

    voice get_voice_filename("nom")
    naomi "「あ、あははは……」"

    "私を起こしたのはクラスメイトの{rb}小熊{/rb}{rt}おぐま{/rt}{rb}真央{/rb}{rt}まお{/rt}だ。いつも通り、派手な色の髪を両結びにし、巻いている。"

    "もう一人が後輩の直未で、二人とも制服を着ていた。ということは学校帰りなのだろう。"

    scene bg lion01 noon with dissolve_long



    "私たち３人は喫茶ライオン館の客席に座っていた。ライオン館は私のおばあちゃんの経営する喫茶店で、１階がお店、２階が住居になっている。"

    "私はおばあちゃんと同居しているので、２階には私の部屋もあった。でも、おばあちゃんは現在親戚の介護で田舎へ行っていて、たまにしか戻らない。実質は一人暮らしみたいなものだった。"

    scene ecg girlstalkB1 sur gl1 with dissolve_long

    voice get_voice_filename("mao")
    mao "「ほれりーたん、まだ寝てるのか。真央様が目を覚ましてあげよう～うりうり～」"

    "真央は手に持ったシャーペンを私の頬に当て、ぐりぐりと押し付けて来た。"

    scene ecg girlstalkA1 ang with dissolve

    voice get_voice_filename("rnk")
    rinka "「いたたた！　起きた起きた！　だから芯は出すな」"

    scene ecg girlstalkB1 tro nor with dissolve

    voice get_voice_filename("nom")
    naomi "「真央先輩、鬼……」"

    "悪戯っぽい表情でにやりと笑う真央を見て、直未は若干引いていた。"

    "まあおかげで目は覚めたのだけれど、まだ自分がどうしてここにいるのかが思い出せない。"


    voice get_voice_filename("rnk")
    rinka "「で、ごめん。今って何してたっけ？」"

    show ecg girlstalkB1 nor glo with ecg_change

    voice get_voice_filename("mao")
    mao "「なぬ。まだ起きてないのぉ？」"

    scene ecg girlstalkA1 tro with dissolve

    voice get_voice_filename("rnk")
    rinka "「夢を見たせいか、何かぼーっとしちゃって」"

    "ただ実際は、どんな夢を見たかも覚えていない。自分で「火事」って呟いたにもかかわらず、燃える夢を見たような記憶はなかった。"

    "釈然とせず、何だか気持ち悪い感じがした。"

    scene ecg girlstalkB1 tro nor with dissolve

    voice get_voice_filename("mao")
    mao "「ふーん。変なりーたん」"

    "私が「もう」とため息をつきながら真央を睨むと、直未は「あの」と口を開いた。"

    show ecg girlstalkB1 tro nor with ecg_change

    voice get_voice_filename("nom")
    naomi "「来月の文化祭で、うちのクラスが喫茶店をやることになったんです。わたしがクラスの実行委員に、しかもリーダーになってしまって」"

    "直未の口振りからして、明らかに押し付けられたのだろう。"

    "もっとも直未は真面目だからきちんと責任は果たすだろうし、そういう意味では適任なのかもしれないけれど。"

    show ecg girlstalkB1 lau nor with ecg_change

    voice get_voice_filename("nom")
    naomi "「凛火先輩のおうちが喫茶店って聞いてたので、参考にお話を聞きたかったんです。そしたら、来て大丈夫って言ってくれたので……」"

    "直未の話を聞いて、状況に理解が追い付いて来た。"


    voice get_voice_filename("rnk")
    rinka "「落ち着いて話をしたいってこともあって、うちに呼んだんだった」"

    "おばあちゃんが不在の今は、常連さん向けにお店を開けている。たまに一見さんも来るけれど、凝ったメニューもお休みしているので私一人で十分だ。"

    "忙しくなることもないので、うちを選んだんだった。"

    scene ecg girlstalkA1 smi with dissolve

    voice get_voice_filename("rnk")
    rinka "「『ライオン館はみんなの第二のおうち』っていうのがおばあちゃんの口癖だしね」"

    scene ecg girlstalkB1 lau glo with dissolve

    voice get_voice_filename("mao")
    mao "「出た、おばあちゃんの口癖」"


    voice get_voice_filename("nom")
    naomi "「確かに……初めて来たのに、ここはすごく落ち着きます」"

    show ecg girlstalkB1 smi blu with ecg_change

    voice get_voice_filename("mao")
    mao "「落ち着き過ぎて居眠りしちゃうのは、ダメだけどねぇ～」"

    scene ecg girlstalkA1 ang with dissolve

    voice get_voice_filename("rnk")
    rinka "「もう、うるさい！　で、真央はどうしてうちにいるんだっけ？」"

    scene ecg girlstalkB1 smi blu with dissolve

    voice get_voice_filename("mao")
    mao "「……ヒマだったから？」"


    voice get_voice_filename("rnk")
    rinka "「あ、うん。だろうね」"

    show ecg girlstalkB1 nor blu with ecg_change

    voice get_voice_filename("nom")
    naomi "「先輩たちのクラスは何をやるんですか？」"


    voice get_voice_filename("rnk")
    rinka "「えっと……お化け屋敷だったか、占いの館だったか」"

    show ecg girlstalkB1 nor glo with ecg_change


    voice get_voice_filename("mao")
    mao "「要するにまだ決まってないってことなのだよ……」"

    show ecg girlstalkB1 sur nor with ecg_change


    voice get_voice_filename("nom")
    naomi "「ええっ！　大丈夫なんですか？」"


    voice get_voice_filename("mao")
    mao "「ま、なんとかするんじゃないかなぁ？　頑張ってるなおりんの前で言うのもよくないかもだけど、あんまし興味ないんだよねぇ～うちら」"

    show ecg girlstalkB1 sur glo with ecg_change

    voice get_voice_filename("mao")
    mao "「りーたんもうちもクラスから避けられてる組だしぃ。実行委員もうちらにはなるべく関わらないようにしてるってわけ」"


    voice get_voice_filename("rnk")
    rinka "「そ。だからってわけじゃないけど、直未の手伝いならするよ。私は店番あるから、できる限りになっちゃうけどね」"

    show ecg girlstalkB1 uwa glo with ecg_change

    voice get_voice_filename("nom")
    naomi "「あ……はい。ありがとうございます」"

    show ecg girlstalkB1 nor nor with ecg_change

    "直未は座ったまま小さく会釈をしたが、表情は複雑そうだった。クラスから避けられてるって聞いて、いじめとかを連想したのかもしれない。"

    "とはいえ当の本人の私たちは慣れているし、避けられているだけで露骨に無視をされるわけではない。"

    "真央なんてよくクラスで色々な子とも話しているし、私も嫌われているわけではないはずだ。"

    "必要以上に踏み込まないというか、お互いに「この子は違うタイプだ」みたいな心の壁がある。そういう意味で真央と私は避けられ組だ。"

    "ちなみにこの避けられ組には、今は恐らくバイト中の同級生、{rb}未島{/rb}{rt}みしま{/rt}海晴も含まれている。"


    voice get_voice_filename("mao")
    mao "「あ、りーたんアイスカフェラテちょうだいー」"


    voice get_voice_filename("rnk")
    rinka "「うちはラテはないの。カフェオレならあるよ」"

    show ecg girlstalkB1 nor glo with ecg_change



    voice get_voice_filename("mao")
    mao "「じゃそれで！」"


    voice get_voice_filename("rnk")
    rinka "「いいけど、真央にはちゃんとお代を払ってもらうからね」"

    show ecg girlstalkB1 nor blu with ecg_change



    voice get_voice_filename("mao")
    mao "「いらね。水で」"


    voice get_voice_filename("rnk")
    rinka "「ったく仕方ないな。一杯だけおごり。店のね。直未は何がいい？」"

    show ecg girlstalkB1 uwa nor with ecg_change



    voice get_voice_filename("nom")
    naomi "「えっと……いいんですか？」"

    show ecg girlstalkB1 uwa glo with ecg_change



    voice get_voice_filename("mao")
    mao "「もらえる時にもらっときなよ～。りーたん、普段はケチだから」"

    show ecg girlstalkB1 smi glo with ecg_change



    voice get_voice_filename("nom")
    naomi "「じゃ、じゃあホットコーヒーをいただけますか？」"


    voice get_voice_filename("rnk")
    rinka "「はい、ちょっと待っててね」"



    scene bg lion01 noon
    show rnk chara apr nor nor at std_c
    with fade_long




    "私は客席からキッチンへ向かい、手を洗ってからエプロンをつけた。"

    "キッチンに入ったなら、その瞬間にプロ――おばあちゃんの口癖を、私はちゃんと守っている。"

    "友人に出す飲み物とはいえ、ちゃんと用意をするのだ。"

    scene ecg coffee sip with dissolve_long



    "うちでホットコーヒーを注文されたら、基本的にフルシティローストのグアテマラを提供する。"

    "フルシティローストというのはやや深煎りのことで、酸味が少なめで苦味が増してくる焙煎度だ。"

    "グアテマラは酸味が少し強めで苦味とのバランスがよくコクがあるので、フルシティローストと相性がいいらしい。"

    "サイフォンを準備して、フラスコの真ん中よりも少し横のところにアルコールランプの火を当てる。"

    "沸騰したら、時折優しくかき回しながらコーヒーが落ちて来るのを待つ。全部がフラスコに落ち切ったならば、少し置いて香りが立つのを待つ。"



    scene ecg girlstalkB2 nor nor with dissolve

    voice get_voice_filename("rnk")
    rinka "「はい直未、お待たせ」"

    show ecg girlstalkB2 lau nor with ecg_change

    voice get_voice_filename("nom")
    naomi "「すごい、いい香りがここまでします」"


    voice get_voice_filename("rnk")
    rinka "「ふふ、ありがと」"



    "直未の喜んでくれる顔は素直に嬉しい。とはいえ、私はまだまだだ。おばあちゃんはサイフォン式だけでなく、豆によってはペーパードリップなどで抽出方法を変えている。"

    "私は私がやりやすいようにおばあちゃんが指示してくれたものをこなしているだけで、まだまだ知識も実践も勉強中だ。"

    scene ecg coffee ole with dissolve


    "さて、次はアイスカフェオレの準備だ。"

    "これは、あらかじめドリップした水出しのアイスコーヒーを使う。まずコーヒーを入れてから、グラスにたっぷり氷を入れ、牛乳を注ぐ。"

    "こうすると、黒と白がグラスの中で混ざり合うのが透けて見栄えがいいのだ。ストローを差してガムシロップと一緒に真央に持っていく。"



    scene ecg girlstalkB3 lau nor with dissolve

    voice get_voice_filename("rnk")
    rinka "「はい、ガムシロップ足りなかったら言ってね」"

    show ecg girlstalkB3 lau glo with ecg_change


    voice get_voice_filename("mao")
    mao "「どうもどうも～」"



    "最後に自分のコーヒーを用意して、エプロンを外して手を洗ってから、席へ戻った。"

    show ecg girlstalkB3 lau nor with ecg_change

    voice get_voice_filename("nom")
    naomi "「すっごく美味しいです。家で淹れたのとは全然違う……。凛火先輩すごいです！」"


    voice get_voice_filename("rnk")
    rinka "「喫茶店だからね。ま、私がすごいっていうか、おばあちゃんがすごいんだけどね」"

    show ecg girlstalkB3 lau blu with ecg_change

    voice get_voice_filename("mao")
    mao "「そういやさ、他に店員さんとかいないわけ？」"

    "真央はカフェオレにガムシロップを半分入れてから一口飲み、もう半分も入れた。"

    "ストローでグラスを混ぜると、からんからんという透明感のある音が心地よい。"


    voice get_voice_filename("rnk")
    rinka "「この狭さでしょ？　元々おばあちゃん一人で切り盛りしてきたから、従業員っていないんだよね」"

    show ecg girlstalkB3 nor nor with ecg_change

    voice get_voice_filename("mao")
    mao "「りーたんのおばあちゃんって、今は親戚の介護でたまにしか帰ってこないんだっけ？」"

    scene ecg girlstalkA2 nor with dissolve

    voice get_voice_filename("rnk")
    rinka "「そうだよ。お店も閉めようかって言ってたんだけど、私が無理言ってちょっとだけでも開けることにしたの。コーヒーを淹れるだけなら私でもできるかもって」"

    show ecg girlstalkA2 tro with ecg_change

    voice get_voice_filename("rnk")
    rinka "「そしたらコーヒーを淹れるってのが一番大変でさ。おばあちゃんからは１ヵ月以上かかっても結局オッケーは出なかったよ……」"

    show ecg girlstalkA2 nor with ecg_change

    voice get_voice_filename("rnk")
    rinka "「ただ、それじゃ店が開けないから、私もどうにかこうにか頑張って、おばあちゃんが行く直前にぎりぎり及第点をもらったんだよね」"

    scene ecg girlstalkB3 nor nor with dissolve

    voice get_voice_filename("nom")
    naomi "「先輩はいつから一人でお店を開けているんですか？」"

    scene ecg girlstalkA2 nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「おばあちゃんが田舎に行ったのが３月末だから、私がお店を開けるようになって大体１ヵ月になるね」"

    "言って、私はコーヒーに口をつけた。最初の頃に比べると、香りも立つようになったし、味も良くなった。"

    "元々美味しいコーヒーはおばあちゃんのおかげで飲み慣れていたので、自分で比較できたのが功を奏したのだろう。もっとも、その分まだまだだな、とも思うのだけど。"

    scene ecg girlstalkB3 smi nor with dissolve

    voice get_voice_filename("nom")
    naomi "「文化祭でこの美味しいコーヒーを出せたらいいなって思ったんですけど、さっきの話を聞くと難しそうですよね……」"

    show ecg girlstalkB3 smi blu with ecg_change

    voice get_voice_filename("mao")
    mao "「生徒がちゃんと味の違い分かるかねぇ。うちみたいに、ミルクがないと全部苦い～ってなる子も多いだろうし」"

    show ecg girlstalkB3 lau blu with ecg_change

    voice get_voice_filename("nom")
    naomi "「そういう人もいるかもしれませんけど、でもわたしは大丈夫だと思います！　文化祭なら先生や保護者の方も来ますし、喜んでくれるのは間違いないですよ」"

    show ecg girlstalkB3 tro blu with ecg_change

    voice get_voice_filename("nom")
    naomi "「でも先輩がおばあ様に教わって１ヵ月なら、わたしはどれくらいかかることやら……。わたしだけじゃなくて、担当のみんなもできるようにならないといけないし」"


    voice get_voice_filename("rnk")
    rinka "「うん。無理だと思うな。器具も安くないし……」"

    show ecg girlstalkB3 tro glo with ecg_change

    voice get_voice_filename("mao")
    mao "「おー、はっきり言うねぇ！」"

    show ecg girlstalkB3 smi glo with ecg_change

    voice get_voice_filename("nom")
    naomi "「ですよね……。やっぱり文化祭だったらインスタントコーヒーの方がよさそうです」"


    voice get_voice_filename("rnk")
    rinka "「うーん、ちょっと待って。私は、同じものを出すのは無理って言ったの」"

    show ecg girlstalkB3 sur nor with ecg_change


    voice get_voice_filename("nom")
    naomi "「えっ……？」"

    scene ecg girlstalkA2 smi with dissolve

    voice get_voice_filename("rnk")
    rinka "「豆はうちがお願いしている業者を紹介すれば、安く買える。それにハンドドリップなら器具も手軽に買えるし、学園祭の予算みたいのでも大丈夫じゃないかな？」"

    show ecg girlstalkA2 nor with ecg_change

    voice get_voice_filename("rnk")
    rinka "「淹れ方は……おばあちゃんに簡単にできるのがないか聞いてみる。いきなりお店みたいに淹れるとはいかないかもしれないけど、お客さんに喜んではもらえるはず」"


    voice get_voice_filename("rnk")
    rinka "「自信はないけど、私が教える」"

    show ecg girlstalkA2 smi with ecg_change

    voice get_voice_filename("rnk")
    rinka "「だから、あとはやる気次第じゃないかな？」"

    scene ecg girlstalkB3 nor glo with dissolve

    "私が言い終えると、隣で真央がにやにやしていた。恐らく、私がどう答えるかを予想していたのだろう。"

    "直未はしばらくしてはっとした顔を浮かべてから、うんうんと頷き、答えた。"

    show ecg girlstalkB3 uwa glo with ecg_change

    voice get_voice_filename("nom")
    naomi "「そんなに頼っちゃって、いいんですか？」"


    voice get_voice_filename("rnk")
    rinka "「直未が頑張るなら、ね。それにおばあちゃんから聞いたことは私が教えることになるから、私の勉強にもなる」"

    show ecg girlstalkB3 uwa blu with ecg_change

    voice get_voice_filename("mao")
    mao "「いいんだってぇ、なおりん。りーたんは見た目のせいでよく勘違いされるけど、実はお節介なんだよ。特に自分の家族や友達にはねぇ」"

    scene ecg girlstalkA2 ang with dissolve

    voice get_voice_filename("rnk")
    rinka "「お節介言うな！　……で、どうする？　直未？」"

    "視線を向けると、直未はどこか不安げだが、真剣な表情をしていた。"

    scene ecg girlstalkB3 nor nor with dissolve

    voice get_voice_filename("nom")
    naomi "「ぜひ……お願いします」"


    voice get_voice_filename("rnk")
    rinka "「うん、いいよ。じゃ、おばあちゃんから返事が来たらまた連絡するよ」"

    show ecg girlstalkB3 lau nor with ecg_change

    voice get_voice_filename("nom")
    naomi "「はい！　ありがとうございます！」"


    voice get_voice_filename("mao")
    mao "「うちも、たまに暇つぶしさせてもらうよぉ～」"


    voice get_voice_filename("rnk")
    rinka "「いいけど、次からはちゃんとお代もらうからね！」"

    show ecg girlstalkB3 smi blu with ecg_change

    voice get_voice_filename("mao")
    mao "「……ケチ」"


    voice get_voice_filename("rnk")
    rinka "「当然だろ……」"



    scene bg lion01 evening with dissolve

    "その後、私たちはしばらく世間話をしていた。"

    "お客さんもちらほら来ていたが、みんな思い思いに過ごすので、ちゃんと注文に対応していれば私が真央や直未と話していても気にしない。"

    "それどころか、たまにはお客さんから会話に入ってくることもある。常連さんならではというか、中には私が子供の頃から知っている人もいるくらいなので、ちょっとした親戚気分だ。"

    "喫茶ライオン館は、アットホームな場所なのだ。私にとってもおばあちゃんにとっても、第二のおうち。"

    "だからおばあちゃんが帰ってきた時にも、変わらずあって欲しいのだ。"

    "19時になる前に、二人とも喫茶店を後にした。"





    python:
        set_info_scene("04")

        set_info_time("night")
        set_info_location("05")



    stop music fadeout 1
    scene bg myroom night with fade_long
    pause 1

    $ show_hud()

    "店を閉めて後片付けをしてから、私は部屋へ戻った。ライオン館の２階にある自分の部屋だ。"

    "直未の手伝いをすることになったが、私自身も楽しみだった。"

    "コーヒーを淹れるのは好きだし、同じように好きになってくれる人が増えたら嬉しい。"

    "直未は素直だし覚えも早いだろう……慌てんぼうなところが少し不安だけど。"

    play music audio.gimon

    "しかし、今日の夢はなんだったのだろう。"

    "真央たちと話している途中からは違和感もなかったが、居眠りから目覚めた瞬間の曖昧な感じはどうにも忘れられない。初めての感覚だった。"

    "そもそも私は本当に居眠りをして夢を見ていたのだろうか――？"

    scene ecg cardbook clo with dissolve_long



    voice get_voice_filename("rnk")
    rinka "「あれ、何だろ……？」"

    "気にしても仕方ないと眠ろうとしたところで、私は机の上に分厚い本が置かれているのを見つけた。"

    "赤茶色で金の装飾がついた立派な本だった。装飾の模様は……歯車だろうか。"





    menu:
        "こういう本はおばあちゃんが好きそうだが、私の机に持ってきた覚えはない。"
        "開いてみよう":

            $ flags_mhr_koukando += 1

            $ persistent.s1_1_seen = True
            $ grant_hear_all()
            jump f001.s1_1
        "触らないでおこう":

            $ persistent.s1_2_seen = True
            $ grant_hear_all()
            jump f001.s1_2

label f001.s1_1:

    scene ecg cardbook op1 with dissolve_long

    "汚さないように慎重に開いてみることにした。"



    voice get_voice_filename("rnk")
    rinka "「なに、これ」"

    "本を開くとページをめくるのではなく、中央に細長い長方形の空洞が空いているだけだった。"

    scene ecg cardbook clo with dissolve

    "結果的に疑問が増えたまま、私は本を閉じた。"

    "日は遅いので明日にでも、おばあちゃんにチャットを送ってみようか。"

    jump f001.s1_end

label f001.s1_2:



    "見るからに高価そうだし、触らない方がいいかもしれない。"

    "今日は遅いので明日にでも、おばあちゃんにチャットを送ってみようか。"



label f001.s1_end:

    scene bg myroom night with dissolve_long
    pause 1
    play se "electricity_switch"
    scene black with dissolve_fast
    pause 1
    play se "phone_vibration1"
    pause 2

    "電気を消してベッドに寝転んだところで、スマホが震えた。チャットが来たようだ。直未からだ。"





    voice get_voice_filename("rnk", 68)
    rinka "「『今日はありがとうございました。これからよろしくお願いします！』……か。律儀だなぁ、直未は」"

    "私はスタンプで返事を送り、既読がついたかを確認する前にスマホを枕元に置き、目を閉じた。"

    stop music fadeout 2
    scene black
    pause 4





    python:
        set_info_scene("05")

        set_info_time("lnight")
        set_info_location("01")

    scene ecg pattern nor a with eyeshutter_open_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()





    "あれ……？"

    "眠ったはずなのに、意識がある。"

    "とはいえ体は動くような気がしないし、声も出せない。"

    "金縛りなのか、夢を見ているという自覚がある夢なのか。"



    voice get_voice_filename("let")
    lete_unk1 "「やあ」"

    "聞いたことのない男性の声がした。"

    "視界には、ぼんやりと姿が見えた。細身で、中性的な顔立ちをしていた。"

    "私は返事することができないので、そのまま男性が続けるのを待った。"

    show let sta nor sm1 at std_c with std_in


    voice get_voice_filename("let")
    lete_unk1 "「運命に導かれ、君の因果は決したようだ」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「ははは、悲観することはないよ。なぜなら君にはこれから12週間、再び生きることのできるチャンスが与えられているからね」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「普通じゃないよね？　そう、その通りさ」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「けれど、君が特別なんじゃない。特別なのは君の持つ運命だよ」"

    "落ち着いた声で、男性はわけの分からないことを言い続ける。"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「私かい？　私は君を――君たちをいつも見ている存在さ」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「本来、君たちに会うことはないのだけれど、何の因果か、君の夢とここが繋がってしまったみたいだね」"

    show let sta nor sm2 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「さて、せっかくだから挨拶をと思ったけれど、もう充分だろう」"

    show let sta nor sm1 with std_change


    voice get_voice_filename("let")
    lete_unk1 "「では、物語が始まる前に少しだけ君の原風景を思い出すといい」"

    "男性はそう言うと姿を消し、私の意識は再びまどろみの中へ落ちて行った。"

    stop music fadeout 2
    scene black with dissolve_longest
    pause 2

    $ add_seen_chapter("1-1")




    python:
        set_info_scene("06")




    play music audio.firedeath fadein 2
    play ambient "fireloop"
    scene bg train enjo large:
        subpixel True
        zoom 1.3
        xalign 1.0
        yalign 0.5
        linear 150 xalign 0.0
    with dissolve_longest
    pause 2




    "炎の中にいた。"

    "身を焦がすような炎だった。"

    "肌はただれ、肺は煙で焼かれている。"

    "徐々に命が灰になっていくのだと、もう指先ひとつすら動かせない私には実感があった。"


    linda_unk1 "「――――」"


    linda_unk1 "「――――！」"


    linda_unk1 "「――――！　――――！」"

    "何かを叫ぶ声が聞こえた。"

    "しきりに何かを叫んでいる。"

    "炎は広がっていき、叫び声は空気の震える音にかき消される。"

    "声が全く聞こえなくなる頃、私の意識も消えていった。"

    stop music fadeout 2
    stop ambient fadeout 2






    python:
        set_info_scene("07")
        set_info_date(5, 3, "thu")
        set_info_time("morning")
        set_info_location("05")



    scene bg myroom morning large:
        zoom 1.5
        align (0.0, 0.6)
    with fade_long
    play music audio.myroom_melancholic_morning
    pause 1

    $ show_hud()

    show rnk paj sur su1 up rev at std_l with std_in

    play se "futon_dive1"


    voice get_voice_filename("rnk")
    rinka "「うわあぁっ！」" with quake_fast

    "思わず、声を上げていた。"

    "怖ろしい夢を見ていたのだ。自分が火事に遭い、そのまま死んでしまう夢だ。"

    show rnk paj sur su1 up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「はぁっ、はぁっ」"

    "まだ息苦しく、汗もかいていた。"

    "一体どうしてそんな夢を――と疑問に思ったところで、私は自分のお腹に黒い物体が乗っかっているのを見つけた。"

    show rnk paj arm ama up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「あんたか……」"

    show lete normal at cat_r with std_in


    voice get_voice_filename("cat")
    lete "「にゃーお」"

    "猫のレテだ。おばあちゃんが買ってきたのか、もともと野良猫だったのが住み着いたのか分からないが、喫茶ライオン館に住み着いている黒猫だ。"

    "私が物心ついた時から一緒で、もうかなりの高齢のはずにもかかわらず元気だ。"

    "この猫が布団越しに私のお腹の上に乗っていたせいで、息苦しかったようだ。悪い夢を見たのはそのせいだろう。"

    hide lete with std_out

    "私が起きたのに気が付くと、レテはぴょんとベッドから飛び降り、走り去っていった。"

    show rnk paj arm ama up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「相変わらず自由だなぁ」"

    "レテは本当に自由で、普段どこにいるか私も分からない。ただお客さんに迷惑をかけないし、トイレはちゃんと覚えているので放っておいている。"

    "猫を縛ろうとするのは雲をつかむのと同じ――おばあちゃんの口癖だ。まあつまり、おばあちゃんもレテには手を焼いていたということである。"

    show rnk paj nor smi up rev with std_change

    voice get_voice_filename("rnk")
    rinka "「んん……」"

    "今日は祝日だから、朝からお店を開けなければいけない。背伸びをして、私は準備を始めた。"


    $ set_info_location("04")

    stop music fadeout 1
    scene bg lion01 noon with fade_long
    pause 1
    play se "bell02"
    pause 2

    "モーニングのお客さんが帰って落ち着いた頃に、からんからんと入り口のベルが鳴った。"

    show rnk apr nor nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「いらっしゃいま……あ、海晴？」"



    scene ecg miharu nor with dissolve_long
    play music audio.miharu fadein 2


    voice get_voice_filename("mhr", 1)
    miharu "「おはよう凛火」"

    "入ってきたのは、背が高くスタイルのいい美少女だ。長い髪はさらさらで、歩くたびに光を反射して滑らかな波を作る。"

    "未島海晴――私の仲の良いクラスメイトであり、避けられ組の一員だ。海晴の場合は、容姿端麗で成績優秀と、完璧すぎて周囲と壁があるんだと思う。"


    voice get_voice_filename("rnk")
    rinka "「あれ？　今日はバイト休み？」"


    voice get_voice_filename("mhr")
    miharu "「ううん、今日はこれからバイトだよ」"

    "言われてみれば、凛火は休みの日なのに制服を着ていた。遊びに行くときは私服だが、バイトの時は服を選ぶのが億劫だから制服にしているらしい。"

    "制服であれば、バイト帰りに変な男から声をかけられるのも防げるらしい。理由は詳しくは分からないけれど、海晴なりの対策だそうだ。"

    "ただ、海晴のバイト先は秋葉原。ここは新宿方面だから、海晴の家からバイト先に向かうには逆方向で、寄り道にもならないはずだ。何か用事があるのだろうか。"


    voice get_voice_filename("mhr")
    miharu "「ぼくはただ凛火の顔を見たかっただけだよ。昨日はほとんど話せなかったのに、今日から連休になってしまうからね。せめて今日くらいは、凛火と話しておきたくて」"


    voice get_voice_filename("rnk")
    rinka "「は、はぁ……。どうも」"

    "正直言って、海晴にはよく分からないところも多い。"

    "たぶん本当は別の用事が新宿方面であったと思うのだが、こういうからかい方をしてくるのだ。うまい返答の仕方を、私は知らない。"


    voice get_voice_filename("mhr")
    miharu "「さて、もう少し長居したいところだけど、他にお客さんが来ても困るだろうしぼくは行くよ。二人きりになれるのを待っていたら、遅くなってしまったしね」"


    voice get_voice_filename("rnk")
    rinka "「わざわざ待ってたの？　入ってくればいいのに。常連さんばっかりだから、みんな気にしないよ」"


    voice get_voice_filename("mhr")
    miharu "「今日は天気がいいからね。緑を見ながら待つのも気持ちよかったよ」"


    voice get_voice_filename("rnk")
    rinka "「うん、まあ、ならいいけどさ」"

    "確かにうちの向かいには、全国でも有名な広い公園がある。何でも昔の武家の庭園だったものを農業の実験場にして、さらに公園にしたものだとか。"

    "四季折々の花の他、日本・イギリス・フランスそれぞれを模した庭園もあり、観光の人も多く訪れる。"

    "入り口が離れていて、駅からの通り道でもないのでライオン館にはお客さんはほとんど流れてこないが、たまに外国の人が来てくれたりもする。"

    "公園に入らなくても、うちの入り口のところからは豊かな緑が見える。長時間見ていて面白いものではないけれど、海晴の感性は独特なので、楽しめるのかもしれない。"

    play music audio.nichijo01
    scene bg lion01 noon
    show mhr uni sco smi rev at std_cl
    with dissolve_long





    voice get_voice_filename("mhr")
    miharu "「では、お邪魔しました。ちゃんと休憩は取るんだよ？」"

    show rnk apr nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「分かってる。海晴もバイト頑張ってね」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「あ、そうだ思い出したよ。連休の最終日……５月６日にスターダストキングダムへ行く約束忘れてないよね？　その日はちゃんと、お店を休みにするんだよ？」"

    show rnk apr arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「もう、忘れてないよ」"

    "スターダストキングダムとは、千葉県にある有名なテーマパークだ。"

    "ゴールデンウィークの最終日、一番混みそうなのは分かっていたが、そこに遊びに行くことにしていた。"

    show mhr uni nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ。君は前科があるから、確認だよ。それじゃ、またね」"

    show rnk apr nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、ばいば……またね」"

    hide mhr with std_out

    "海晴は去り際に笑顔を浮かべ、ライオン館を後にした。"

    "ばいばいと言いかけて言い直したのは、海晴は別れ際に「さよなら」とか「ばいばい」とか言われるのを嫌がるからだ。"

    "だからいつも「またね」となる。別れの言葉になってしまうって意味で、気持ちは何となく分かる。そこまで気にするかなぁとも思うけれど、なるべく使わないようにしている。"

    play se "bell02"

    "自分用のコーヒーでも淹れて一休みしようかと思っていたところ、またからんからんとベルが鳴った。"

    show nom gci nor nor rev at std_cl with std_in

    show rnk apr nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「いらっしゃいま……あ、直未」"

    "お客さんは、またも知り合いであった。直未の私服はイメージ通りの可愛らしい服だ。"

    show nom gci nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ……おはようございます」"

    show rnk apr nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「おはよう。いいよ、気にしないで入って」"

    "海晴のことは特に触れなかったので、すれ違いにはならなかったのだろうか。"

    "直未は少し元気がないようにも見える。"

    "他にお客さんはいなかったが、やはりお店ということもあり、入るかどうか躊躇しているようだった。"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「どうしたの？」"

    "おばあちゃんには、まだ直未のことを相談していなかった。当然、初心者でも比較的簡単で、美味しく飲めるコーヒーの情報はまだない。"

    "私が一から教えるという手もあったが、中途半端な知識で教えたくなかった。"

    show nom gci hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「実は、昨日忘れ物をしてしまったみたいで……」"


    voice get_voice_filename("rnk")
    rinka "「忘れ物？　もしかして本？　分厚くて、金色の歯車みたいな飾りのついた立派なやつ」"

    show nom gci que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「本……ですか？　いえ、わたし本は忘れていないと思いますけど」"

    show rnk apr nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「そっか、だよね」"

    "聞いてみたはいいものの、私の部屋には上げていないから忘れるはずもないか。"

    "直未の忘れ物は筆箱らしい。"

    "昨晩チャットで送ってもらえればよかったのだが、今朝気付いたらしく、私がお店に立ってからメッセージを送っていたらしい。"

    "直未は新宿が定期圏内らしく、散歩も兼ねてわざわざ来てくれたそうだ。"

    show nom gci har con rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、お母さんからチャットだ。えっと、キッチンのテーブルの上に置きっぱなしだったみたいです……、すみません……」"

    "と、どうやら早とちりだったらしい。"

    "勘違いでわざわざ外出までしてしまうあたり、直未らしいというか……。"

    show nom gci que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「ところで先輩、その本ってどんなのですか？」"

    "直未は意外なところで話題を掘り返して来た。"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「本？　気になるの？」"

    show nom gci nor nor rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい！　立派な本ってどんなものか興味があるんです」"

    show rnk apr nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ふぅん、本好きなんだね。ちょっと待ってて」"

    hide rnk with std_out

    "今はお客さんもいないし、窓から見て通りも落ち着いているようなので、私は２階へ本を取りに行った。"

    show rnk apr nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「おまたせ。これだよ」"

    scene ecg cardbook clo with dissolve_long

    "赤茶の表紙に、金色の装飾。"

    "見るからに高級な本を目の前にして、直未は「おおっ」と感嘆の声をあげていた。"



    voice get_voice_filename("nom")
    naomi "「思った以上に立派ですね。結構昔の本みたいなのに、古い匂いがしません。あの、開いてもいいですか？」"



    voice get_voice_filename("rnk")
    rinka "「いいけど、その本変なんだ」"



    voice get_voice_filename("nom")
    naomi "「変、ですか？」"

    scene ecg cardbook op1 with dissolve



    "直未は本を開くと、早速不思議そうな顔を浮かべた。"

    "無理もない。本の中身はページになっているのではなく、真ん中に長方形の空洞があるだけなのだから。"

    play music audio.gimon fadein 2
    scene bg lion01 noon
    show nom gci nor sur rev at std_cl
    with dissolve_long







    voice get_voice_filename("nom")
    naomi "「確かに、変ですね。昔流行ったカードブックに似ています」"

    show rnk apr nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「カードブック？」"

    show nom gci que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「カードを使って変身して戦うって子供向けのアニメが昔やってたんですけど、知りません？」"

    show rnk apr arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「うーん、やってたような、知らないような……」"

    show nom gci nor nor rev with std_change

    voice get_voice_filename("nom")
    naomi "「この空洞の中に、おもちゃのカードが入っているんです。本はあくまで箱で……ってあれ、薄くて気付きませんでしたけど、これも下の方にカードが入っていませんか？」"

    show rnk apr nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、本当だ。模様が似ているから気付かなかったよ」"

    show nom gci que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「出してみてもいいですか？」"

    show rnk apr nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「うーん、どうしよう。おばあちゃんのかもしれないから、ここまでにしておこっか。確認とってから、見てみよう」"

    "どうやら普通の本ではないらしいので、もしおばあちゃんが秘密にしておきたいものが入っていたりしたら悪い。"

    "カードを見るのは、今晩チャットで聞いてからにすることにした。"

    "私が言うと、直未は素早い動作で本から手を離した。"

    show nom gci hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「すすす、すみません！　わたし、本のことになるとつい夢中になっちゃって……知らずにベタベタと触ってしまって」"

    show rnk apr nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、気にしなくて大丈夫。私が持ってきたんだしね」"

    "本を見ている時、直未は思った以上に積極的だった。やはり本が好きだから、この奇妙な本が気になるのだろう。"


    stop music

    show rnk apr nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「じゃあ、また上に戻して来るね」"

    play music audio.nichijo01 fadein 2
    scene bg lion01 noon large:
        zoom 1.5
        align (0.2, 0.4)
    with wipe_lr
    play se "bell02"
    show cha sta wig nor up rev at std_c with std_in



    "言って私が本を手にした時、再びからんからんと鈴が鳴った。今度は知り合いではなく、お客さんだ。"

    "それも初めて見る女性で、キャリーケースを持っている。どうやら観光で来た外国の人らしい。"

    scene bg lion01 noon
    show rnk apr nor que at std_cr
    show cha sta wig nor rev at std_cl
    with dissolve





    "女性は、私にホテルの場所を訊いてきた。新宿方面にあるホテルのようなので、行き過ぎですよ、と教えてあげる。"





    show cha sta wig smi rev
    show rnk apr nor smi
    with std_change_wait

    "どうやら彼女は日本の寺を巡るため一人で日本に来たらしい。日本語が分からず困っていた、ありがとうとお礼を言ってくれた。"

    hide cha with std_out

    "注文は特にしなかったが、愛想がとてもよかったので許してしまった。"

    show nom gci nor sur rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「凛火先輩って、英語ペラペラだったんですね！」"

    "お客さんが帰った後、直未は目を輝かせて言った。"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「全然。喋れないけど？」"

    show nom gci nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「謙遜……ですか？　だってさっきの女の人、英語だったじゃないですか？」"

    stop music

    show rnk apr sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「え……？」"


    play music audio.gimon fadein 2

    "直未に指摘された私の方が驚いてしまった。"

    "英語だった……？"

    "私としては、日本人と会話するのと何も変わらず話していたのだけれど。"

    "いや、でも。確かにあの人は日本語が分からず困っていたと言っていた。あんなに流暢に喋れるはずがない。"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「何でだろう？」"

    show nom gci hes sor rev with std_change

    voice get_voice_filename("nom")
    naomi "「えっ、わたしに聞かれても……」"

    "とりあえず本を部屋の机の上に置いてから、私は代わりに英語の教科書を持ってきた。"

    show rnk apr nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「適当に問題出してみて」"

    show nom gci nor nor rev with std_change

    voice get_voice_filename("nom")
    naomi "「分かりました。単語でいいですね？　えっと……」"

    scene bg lion01 noon with fade_long
    pause 1

    "何問か問題を出されたが、結局ほとんど答えられなかった。"

    show rnk apr arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「ね？　私英語できないでしょ？」"

    show nom gci hes tr2 rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「確かにそうですけど……ちょっとだけ先輩が心配になってきました……」"

    "オブラートに包んでいるようでストレートに私の英語のできなさを言っているのだろう。最後の方には直未は教科書を見ないで記憶で問題を出していた。"

    "一応弁明しておくと、勉強が苦手な私だが、英語は特にできないのだ。"

    show nom gci que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「そうなると、さっき先輩が話せてたのが余計に不思議です……」"

    "私としては何の違和感もなく会話をしていたので、直未に指摘される方が疑問だ。"

    "とはいえ考えても答えは出ないので、もし次また外国のお客さんが来たら気にすることにしてみよう。"

    play music audio.nichijo01

    show nom gci nor smi rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、あのそれで凛火先輩。せっかく来たので、今日もコーヒーをいただいてもいいですか？　もちろんお金は払うので！」"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「いいけど……いいの？」"

    show nom gci nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「はい！　先輩の淹れてくれたコーヒー、わたし、とっても好きです！」"

    "屈託のない笑顔で、直未はそう言った。"

    show rnk apr nor smi with std_change_wait

    "直未の言葉に、私は表現のできない嬉しさを感じていた。頬が熱くなるのを感じる。"

    "思えばお客さんも常連さんばかりでこんな風に言われたことはなかったかもしれない。"

    "常連さんによく言われるのは『凛火ちゃんも、大分マスターの味に近づいてきたわね』とかで、褒めてもらえるのは嬉しいけれど、必ずおばあちゃんとの比較があった。"

    "私にとって直未の言葉は思いがけないものだったのだ。"

    "だからお礼も言えず、ただあわあわと「ちょっと待っててね」と答えることしかできなかった。"


    scene bg lion01 noon with fade_long
    pause 1

    "直未はコーヒーを飲みながら、本を読んでいた。"

    "私はその間に来たお客さんの対応をしたり、食器の片づけをしたりしていた。"

    "１時間ほどして、直未は荷物をまとめ始めた。レジでお会計を受け取る。後輩からお金をもらうのはちょっと申し訳なかったが、直未の満足そうな顔を見て安心した。"

    show rnk apr nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あ、そういえばさ。ゴールデンウィークの最終日は暇？　日曜日なんだけど」"

    show nom gci que que rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「えっと……空いてます。どうしてですか？」"

    show rnk apr nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「真央と海晴とスターダストキングダムに行く予定でさ。奇数だとアトラクションに乗る時とか１人余っちゃうかもだから、偶数の方がいいねって話をしてて。良かったら行かない？」"

    show nom gci nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「スターダストキングダム……凛火先輩たちと……行きたいです！」"

    show rnk apr nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。じゃあ決まりだね。みんなに伝えとく。チャットのグループも作っておくよ」"

    show nom gci hes tr2 rev with std_change

    voice get_voice_filename("nom")
    naomi "「あっ、でも未島先輩……大丈夫ですか？」"

    show rnk apr nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴？　直未も仲良いと思ってたけど、何で？　こっちは気にしなくていいよ。直未の予定と、あとお小遣いさえよければ」"

    show nom gci hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「は、はい……。ならいいんですけど」"

    "少し腑に落ちなそうなところはあったけれど、６日は直未も一緒に行くことに決まった。"

    "直未がお店から出るのを見届けて、私は仕事に戻った。"





    $ set_info_time("night")
    $ set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "夜になって部屋に戻ったら、私はまずおばあちゃんにチャットを送った。"

    "文化祭で出すコーヒーについてはちょっと考えてくれるらしい。"

    "本に関しては、おばあちゃんも心当たりがないそうだ。"

    scene ecg cardbook clo with dissolve_long

    "家には似たような装丁の本があるようだが、中身はカードブックなどではなく普通の本らしい。"

    "こんな豪華な本と似ているものがうちにあるのはそれはそれで気になったが、おばあちゃんの部屋で探すほどの気もおきなかった。"





    menu:
        "あの本はどうしようか。"
        "売っちゃおう。":

            $ persistent.s2_1_seen = True
            $ grant_hear_all()
            jump f001.s2_1
        "中を見てみよう。":

            $ flags_mhr_koukando += 1

            $ persistent.s2_2_seen = True
            $ grant_hear_all()
            jump f001.s2_2

label f001.s2_1:

    "お小遣いに換えてしまおうとも思ったが、中身がないのにどこで買ってくれるのか分からない。"

    "それに売りに行くにしても、とりあえず中を見てみないと駄目……か。"

    jump f001.s2_end

label f001.s2_2:

    "そういえば、中にカードが入っていると直未は言っていた。"

    "どんなものか、見てみようか。"

    jump f001.s2_end



label f001.s2_end:

    scene ecg cardbook op2 with dissolve

    "私は本をひっくり返して、カードを取り出してみた。"

    "全部で４枚だ。どれも本の表紙の柄に似ている同じ絵柄なので、こちらが裏面だろう。"

    "カードを裏返すと、白を基調としたデザインに何か書かれていた。"

    show ecg cardbook op3 with ecg_change_wait

    "文字は英語のようだったが、何故だろう、自然と読むことができた。"

    stop music

    "――Ⅰ・氏名・獅子舞凛火。"

    "――Ⅲ・氏名・フェデリーコ・カルミナーティ。"

    "――Ⅳ・死因・焼死。"

    "――Ⅸ・未練・金メダル。"

    python:
        gameinfo_cardbook_rnk_unlocked = True
        add_character_cards("rnk", ["1_name", "3_name", "4_death", "9_regret"])
        add_character_cards("fed", ["3_name"])
        add_character_cards("yuu", ["4_death"])
        add_character_cards("sca", ["9_regret"])

    play music audio.gimon fadein 2



    voice get_voice_filename("rnk")
    rinka "「どうして、私の名前が？」"




    scene bg myroom night with dissolve_long

    "思わず、そう声に出していた。"

    "他のカードも意味が分からなかったが、死因とか未練とか穏やかではなさそうだ。"

    "番号が書いてあるので、きっと他にもたくさんカードがあるに違いない。やはり、この空洞にぴったり収まるくらいは枚数があるのだろう。"

    "いつの間にか紛失してしまったのか。そもそも、どうしてこの本は私の机の上にあったのだろう。"

    "念の為ネットで画像検索してみても、この奇妙なカードブックについてのめぼしい情報は出てこなかった。"

    show rnk paj arm ama at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「でもこれ氏名とか書いてあるし、個人情報だよなぁ。同姓同名ってわけもないだろうし」"

    "となると、売ることはできない。"

    "とりあえずカードを本の中に戻して、本棚にしまった。"

    "今度直未にも見せてみよう。一緒に調べればまた違うかもしれない。"

    show rnk paj nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「それより、真央に連絡しないと」"

    scene bg myroom night large:
        xalign 0.0
        yalign 0.6
    with dissolve

    "スマホを開いて真央に直未がスターダストキングダムに来ることを連絡すると、すぐに既読がつき、返事が来た。"


    voice get_voice_filename("mao")
    mao "『マジ？　マジで？　うわー、いやなおりんと行くのは楽しみなんだけど、んっと……んーまあいいや。みはるんにはうちから伝えておくから』"

    "真央はどこか様子がおかしかったが、話してみると直未と行くのは問題ないとのことだ。"

    "ただ、「うちが予定を立てるからみはるんにはくれぐれも連絡しなくていいからね」と念を押された。"

    "怪しいが、遊ぶ時には大体真央に任せきりなので、今回もそうすることにした。"

    "あと数日経てば、楽しいテーマパーク。"

    "明日もお店を開けるので、私は早めに寝ることにした。"

    $ add_seen_chapter("1-2")






    python:
        set_info_scene("08")
        set_info_date(5, 6, "sun")
        set_info_time("morning")
        set_info_location("06")




    stop music fadeout 2
    scene bg amusementpark noon with fade_longest
    play music audio.amusementpark_noon
    pause 1

    $ show_hud()

    "大混雑の列を抜けたのは、開園から１時間ほどのことだった。順番に案内されるのを待ち、私たちはスターダストキングダムへ入場した。"

    "開園の１時間前に待ち合わせしてはいたのだが、どうやらもう１時間は早くいた方がよかったようだ。"

    "とはいえ事前に真央にお願いをしていたので、チケットの列には並ばずに済んだ。"

    "ゴールデンウィークの混雑を甘く見ていた。"

    show mao civ nor no1 rev at std_cl, xoffset(100) with std_in

    voice get_voice_filename("mao")
    mao "「いやぁ、やっと入れたねぇ。とりあえず撮っておく？」"

    "返事を待たずに、真央はスマホで何枚か写真を撮った。海晴と入ったり私と入ったりと、自撮りも数枚撮っていた。"

    show rnk civ arm ama at std_cr, xoffset(-150) with std_in

    voice get_voice_filename("rnk")
    rinka "「写真撮ってばっかりだと電池なくなるよ？」"

    show mao civ sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「モバイルバッテリー持って来てるから大丈夫」"

    show mhr civ nor nor behind rnk at std_r with std_in


    voice get_voice_filename("mhr")
    miharu "「せっかくだから、凛火と撮りたいな」"

    show rnk civ nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「なら、みんなで入ろうよ」"

    show mao civ nor glo rev with std_change

    voice get_voice_filename("mao")
    mao "「それもいいけど、せっかくだしぃ、みはるんとりーたんのツーショットもいただき～」"

    scene black with dissolve_fast

    play se "camera_shutter"
    scene bg amusementpark noon large:
        align (0.9, 0.3)
    show rnk civ nor que up at std_l, xoffset(-50), yoffset(100)
    show mhr civ nor nor up behind rnk at std_r, xoffset(200)
    with eyeshutter_open_fastest

    pause 2

    scene bg amusementpark noon
    show rnk civ nor que at std_cr, xoffset(-150)
    show mhr civ nor nor behind rnk at std_r
    show mao civ nor glo rev at std_cl, xoffset(100)
    with dissolve

    show nom gci hes tr1 rev behind mao at std_l with std_in

    voice get_voice_filename("nom")
    naomi "「あは、はははは」"

    "直未は私たちの勢いについていけていないからか、空笑いを浮かべていた。"

    show mao civ nor lau rev with std_change

    voice get_voice_filename("mao")
    mao "「さて。じゃお土産屋さんに行こー」"

    show rnk civ arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「いきなり？　せっかく来たんだしまずは乗り物に乗ろうよ？」"

    show mhr civ sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「そうだね。ぼくは絶叫マシーンは好きではないけれど、凛火の隣なら大丈夫かな」"

    show mao civ sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「テーマパークっていったら可愛い小物とかいろいろあるのにぃ。あ、パレードも見たいな。なおりんは？」"

    show nom gci hes tr1 rev with std_change

    voice get_voice_filename("nom")
    naomi "「パレードは興味ありますけど……。わたしは、みなさんにお任せします……」"

    "直未はどうやら考えるのを放棄しているらしい。"

    "後輩だから仕方がないというか、この中で意見を言うのも難しいだろう。"

    show rnk civ nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ここからだと、あ、ブリリアントタワーっていうのが近いみたい。フリーフォール系のアトラクションだ」"

    show mao civ nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「さんざん並んだのに、また並ぶの～？」"

    show nom gci que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、枚数は限られているみたいですけど、列をパスして入れる優先チケットがあるらしいです」"

    show mhr civ nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくも並んでいる間に調べていたよ。今の混雑具合だと使えるのは一時間後くらいからのようだけれど、取っておいた方がいいんじゃないかな？」"

    show rnk civ nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「うん。なら、まずはチケットを取ろう。待っている間に、お店を見よう？　パレードは午後のもあるから、いくつかアトラクションに乗ってから考えよう」"

    show mao civ nor glo rev with std_change

    voice get_voice_filename("mao")
    mao "「お～。りーたんいいリーダーだねぇ」"

    show mhr civ nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくも賛成だ。凛火の言う通りにしよう」"

    show nom gci nor lau rev with std_change

    voice get_voice_filename("nom")
    naomi "「わたしは……みなさんにお任せします」"

    "話もまとまったところで、私たちは優先チケットの発券機へと向かった。"

    "今日は楽しい一日になると思うと、気分が高揚していった。"



    $ set_info_time("night")

    stop music fadeout 1
    scene bg amusementpark night with fade_long
    play music audio.amusementpark_night
    pause 1

    $ show_hud()

    "閉園も近くなり、空はすっかり真っ暗。園内のイルミネーションは煌々と輝いていた。真央と直未は買い忘れたお土産があると言って、一旦別行動になっていた。"

    show mhr civ sco sh2 rev at std_cl
    show rnk civ arm sad at std_cr
    with std_in

    "私たちは入り口近くのベンチに座り、休んでいた。"




    show rnk civ nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「――って、よく見たらカップルだらけ……。どうする？　移動する？」"

    "休日の夜のパークなのだから、カップルが多くても当たり前だ。"

    "とはいえ、テーマパークに来て浮かれているのだろうが、手を握ったり抱き合ったりと人前にもかかわらず平気でイチャイチャしている中にいるのは気まずい。"

    "だが、海晴は立ち上がろうとした私の上着の裾をつかんで止めた。"


    scene ecg amusement01 smi with dissolve_long






    voice get_voice_filename("mhr")
    menu:
        miharu "「いいよ。このままで、もうしばらく」"
        "「恥ずかしいから……離して」":

            $ persistent.s3_1_seen = True
            $ grant_hear_all()
            jump f001.s3_1
        "「わ、分かった」":

            $ flags_mhr_koukando += 1

            $ persistent.s3_2_seen = True
            $ grant_hear_all()
            jump f001.s3_2

label f001.s3_1:

    scene ecg amusement02 sur with dissolve

    voice get_voice_filename("rnk", 116)
    rinka "「ち、ちょっと！　恥ずかしいから……離して」"

    scene ecg amusement01 se2 with dissolve

    voice get_voice_filename("mhr", 14)
    miharu "「なら、またぼくの隣に座ってもらえないかな？　それまで……離せないよ」"

    jump f001.s3_end

label f001.s3_2:


    scene ecg amusement02 smi with dissolve

    voice get_voice_filename("rnk", 117)
    rinka "「……うん。わ、分かった」"

    scene ecg amusement01 smi with dissolve

    voice get_voice_filename("mhr", 15)
    miharu "「嬉しいな。凛火が素直に頷いてくれるのは珍しいからね」"

    jump f001.s3_end



label f001.s3_end:




    "海晴は珍しく恥ずかしそうな顔を浮かべていた。"

    "いつもははきはきと喋るのに、どこかもどかしそうな様子だ。"

    scene bg amusementpark night with dissolve_long

    "辺りには次第に夜のパレードを見に来たお客さんで混み始めた。人の集まり方を見るに、偶然にも、このベンチはいい場所のようだ。"

    "これ以上に混んでしまうと真央たちとの合流は難しそうだったので、移動しようと思っていた。"

    scene ecg amusement01 se1 with dissolve_long

    "しかし海晴はずっと私の袖を握ったままで、私は提案することができなかった。"

    "沈黙が続いた。"

    "海晴といると、会話は途切れる方が少ない。"

    "私たち以外と接する時の海晴は世間話をあまりしないから勘違いされているが、海晴はユーモア好きで、どうでもいいことでも楽しそうに喋る。"

    "けれども、今はお互い何も言わなかった。海晴の恥ずかしげで、だがどこか真剣な表情が私を話させなかった。"

    "そうこうしているうちに、ベンチの周りにはパレードの通行の邪魔にならないようにバリケードが張られてしまった。同時に列の整理も行われる。"

    "私たちはそのままでいればよかったが、ざわざわと賑わう観客の渦の中で、二人だけが静寂というのが恥ずかしかった。"

    scene ecg amusement02 sur with dissolve





    voice get_voice_filename("rnk_mhr")
    rinka_miharu "「あのっ……」\n「ねぇ……」"







    "同じことを考えていたのだろう。二人同時に声を出し、ぶつかった。"

    show ecg amusement02 smi with ecg_change

    voice get_voice_filename("rnk", 119)
    rinka "「何？」"

    scene ecg amusement01 se2 with dissolve


    voice get_voice_filename("mhr", 17)
    miharu "「ううん。凛火の話から聞きたいな」"


    voice get_voice_filename("rnk")
    rinka "「今日、楽しかったねって、それだけ」"

    show ecg amusement01 smi with ecg_change


    voice get_voice_filename("mhr")
    miharu "「とても楽しかった」"


    voice get_voice_filename("rnk")
    rinka "「せっかくだから、このままパレード見ちゃおっか。真央にはチャット送っておくよ」"


    voice get_voice_filename("mhr")
    miharu "「そうしてくれると嬉しい。ぼくは遊園地に来るのも初めてだし、夜にパレードを見るのも初めてなんだ。だから興味があるんだよ」"

    show ecg amusement01 sad with ecg_change


    voice get_voice_filename("mhr")
    miharu "「あまり家族で外出を……それも夜に遊びに行くなんてなかったからね」"


    voice get_voice_filename("rnk")
    rinka "「そうなの？」"

    show ecg amusement01 smi with ecg_change

    "聞き返したが、海晴は微笑してそれ以上何も言わなかった。"

    "海晴はまた、不自然な沈黙を作った。だが、その表情は寂しげなものから不安げなものに変わり、今度は決意の表情に変わる。"

    show ecg amusement01 se2 with ecg_change


    voice get_voice_filename("mhr")
    miharu "「あのね、ぼくが言いたかったのは」"

    "その時、わーっと歓声が上がる。"

    "パークのイルミネーションが一斉に消えたのだ。同時に、楽しげな音楽も流れ始めた。"

    scene ecg amusement02 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「パレード、始まるね」"

    scene ecg amusement01 smi with dissolve


    voice get_voice_filename("mhr")
    miharu "「……そうだね」"





    scene bg amusementpark night large:
        subpixel True
        xalign 0.0
        yalign 0.5
        linear 80 xalign 1.0
    with dissolve_long

    "その後はあたりでは大音量で音楽が響き、とても会話どころではなかった。"

    "それでも、光と音の芸術を眺めているだけで気分は高揚していた。とても楽しいものだと、きらきらしたパレードを見て素直に思っていた。"

    "パレードは３０分くらい続いただろうか。"

    "園内のイルミネーションが再点灯してからも、しばらく余韻が残っていた。"

    "観客が大体散ったあたりで、私は海晴に「行こうか」と声をかけた。"

    "海晴は私の上着の袖からそっと手を離し、立ち上がった。"



    scene bg amusementpark night with dissolve

    show mhr civ nor rea rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「とても……綺麗だった」"

    show rnk civ nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「うん、そうだね。来てよかった」"

    show mhr civ sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくたちは、またこうして出掛けられるかな」"

    "海晴は、打って変わって細い声で言う。"

    show rnk civ nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「大丈夫。みんな、ずっと一緒だよ」"

    show mhr civ nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「うん。凛火がそう言ってくれるなら、今――ぼくは満足だ」"

    show rnk civ nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「次は……花火大会かな。８月に、大きな花火大会があったはず。真央にはまだ話してないけど、絶対行こうね」"

    "だからまたみんなで、と私は続けた。"

    show mhr civ nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「必ず」"

    "海晴は短く、だがはっきりとした声でそう言った。"

    "あまりにはっきりとしていたので、私はそれを切実だと感じて少し不安になった。海晴の影が、ゆらめいたような気がして。"

    "その時、スマートフォンが震えた。真央からだ。振り返ると、ちょうど真央と直未が歩いて来ていた。"

    show rnk civ nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「あ、来たよ。行こう」"

    show mhr civ pai ten rev with std_change

    voice get_voice_filename("mhr")
    miharu "「…………」"

    show rnk civ nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴？」"

    show mhr civ nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……すまない。少しぼーっとしていた。そうだね、合流しよう」"

    "海晴の言葉を待ってから、私は真央と直未に手を振った。"





    python:
        set_info_scene("09")
        set_info_time("night")
        set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "帰宅してすぐに、私はシャワーを浴びた。"

    "家に帰るとどっと疲れが足に来て、そのままの流れで寝る支度を済ませた。"

    show rnk paj nor smi at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……楽しかったな」"

    hide rnk with std_out

    "お金もそんなに余裕があるわけではないので、お土産はそこまで買わなかったが、かけがえのない物は持ち帰っていた。"

    "それは、言葉にするまでもない。"

    "おばあちゃんからも返事があり、比較的安価で美味しい豆と、初心者でも簡単にできるハンドドリップのやり方を教えてもらえた。"

    "明日からはまた学校だ。直未の文化祭のため、ちゃんと教えてあげないと。"

    "ベッドに寝転んだとき、ふと本棚にある一冊の分厚い本が目についた。"

    "あの不思議な本のことは、まだ直未と話していなかった。コーヒーのことを教えるとき、うちに来てもらうことがあるだろう。その時に話してみよう。"

    "さて今度こそ本当に寝よう、と電気を消した。"


    play se "electricity_switch"
    scene black with dissolve_fast
    pause 2


    voice get_voice_filename("rnk")
    rinka "「すごく、楽しかった」"

    "私はまた同じことを呟いていた。８月の花火大会もまだまだ先だけど、今からもう楽しみだ。"

    "きっとそれまでにも、私たちは何度も遊びに出掛けることだろう。"

    "そう、この時は何も知らなかった。"

    "私の日常はただ平然と真っ直ぐ進んでいくのだと――疑いすらしていなかった。"

    $ add_seen_chapter("1-3")

label sentei1:

    call set_replay






    stop music fadeout 2

    if _in_replay:
        scene black with dissolve_longest
        pause 1
    else:
        scene black
        pause 1

    python:
        set_info_date(5, 6, "sun")
        set_info_scene("10")
        set_info_time("lnight")
        set_info_location("07")

    $ show_hud()


    "……。"

    "…………。"

    "…………朝かな？"

    "まだ眠りについてからほとんど時間が経ってないように思えるけれど。疲れていたから、体が休まってくれなかったのだろうか。"



    voice get_voice_filename("dia", 1)
    diana_unk1 "「ごきげんよう。運命の奴隷の皆サマ」"



    voice get_voice_filename("dia")
    diana_unk1 "「あら？　最後のおひとりですわね。“Ⅰ”番サマ？」"

    "違う。"

    "私はまだ起きていない。"

    "ここ数日間、何度か似たようなことがあった。眠っているはずなのに、意識が目覚めていることが。"

    "私はゆっくりと――目を開ける。"

    scene bg fatalhall01 normal with dissolve_longest
    play music audio.fatalhall
    pause 1


    voice get_voice_filename("rnk", 131)
    rinka "「――――っ！」"






    "眼前に広がっていたのは、見たこともないような光景だった。"

    "どこまでも広がる闇の中に、いくつもの歯車が浮いている。上を見ると、僅かな光が暗闇の隙間から降り注いでいる。"

    "そして、私は自分が立っていることに気が付いた。"

    "直径３メートル程の円い床に、裁判所の証言台のような手すりがついている。こんなもの、ニュースやドラマでしか見たことがない。"

    "しかもこの円い床は、闇の中に浮いているようだった。"

    "枠のようなものにはまっているが、床自体は独立して浮かんでいる。"

    "狭い円い床は、円になって12個並んでいる。まるで、時計の文字盤のような配置だ。"

    "それを示唆するかのように、私の立っている床には“Ⅰ”という数字が書かれていた。"

    "さらに12個の床の中心には、巨大な時計の針が空気を震わせながらゆっくりゆっくり時を刻んでいた。"


    scene bg fatalhall01 up with dissolve

    show rnk uni sur su2 ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「何……ここは……何なの？」"

    show mhr uni nor ser rev ci at ci_l with ci_in


    voice get_voice_filename("mhr", 29)
    miharu_unk1 "「どうして……君が！」"

    $ gameinfo_cardbook_mhr_unlocked = True

    "その声を聞いたとき、私は思わず息を飲んだ。"

    "私の隣の床。番号で言うと“Ⅱ”の床の上に知った顔が――海晴が立っていたのだ。"

    show rnk uni cat sma ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「み……」"



    voice get_voice_filename("dia")
    diana_unk1 "「“Ⅰ”番サマ？　その方の名前はお告げにならない方がいいですわ」"

    scene ecg parcawalk nor with dissolve_long

    "名前を呼び掛けた私を、聞いたことのない声が制した。声のした方にいたのは、ふわふわした白い髪の少女だった。"


    voice get_voice_filename("rnk")
    rinka "「え……？　床のないところを、歩いている……？」"

    "少女は、私たちと違って円の床に立っているわけではなかった。"

    "この空間の、何もないところを平然と歩いている。"

    "空中から一歩踏み出して、床がはまっている枠の縁に乗った。そこで、立ち止まった。"

    "スカートのすそがふわっと上がり、細い太ももが天から差し込む光を反射した。"

    "わたがしのような髪に似てふわふわとした彼女の服は、外国のお嬢様が着ていそうな上品なものだった。"

    "小さな頭にちょこんと乗せた帽子が、可愛らしい。"

    "私が振り返って少女を見ると、彼女も振り返り、視線が合った。"



    voice get_voice_filename("dia")
    diana_unk1 "「ワタクシは運命の女神パルカ。『女神の選定』を取り仕切る管理者であり、あなた方人間の上位にあたる存在ですわ」"


    voice get_voice_filename("rnk")
    rinka "「――――は？　ごめん、何の話？」"


    voice get_voice_filename("dia")
    parca "「はぁ……。どうやらあなたは、死のショックで記憶が一部抜けてしまっているようですわね」"


    voice get_voice_filename("dia")
    parca "「あなたにも説明をして差し上げたと思うのですけれど、仕方がないのでもう一度だけ説明しましょう」"


    voice get_voice_filename("rnk")
    rinka "「説明？　死のショック？　ごめん、そもそも全然意味が分からないんだけど……」"


    voice get_voice_filename("dia")
    parca "「黙って聞いてくださいます？」"

    "少女はため息をつき、呆れた声でそう言った。"

    "明らかに年下ではあるが、こうも上から目線で言われるのには抵抗があった。"




    scene bg fatalhall01 up
    show mhr uni nor ser rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「君は忘れていたから、この数日間普通でいられたんだね。君は君のために、このまま話を聞いた方がいい」"

    show rnk uni nor que ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「で、でも」"

    show mhr uni nor ser rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「言い方を変えよう。そうしてくれ」"

    show rnk uni nor nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「わ……分かった」"

    scene ecg parcawalk nor with dissolve_long


    voice get_voice_filename("dia")
    parca "「よろしいかしら？　もしよろしければ、他の皆サマもおさらいしてくださいな」"

    "パルカは浮遊する床の端から、針を橋にして進み、今度は巨大な時計の中心へと向かって移動を始めた。"

    "歩きながら、優雅な口調で話を続けた。"


    voice get_voice_filename("dia")
    parca "「女神の選定。それは、あなた方≪因果の刻≫を等しく持つ方々が各々の≪死の運命≫を回避するための儀式ですわ」"


    voice get_voice_filename("dia")
    parca "「先ほども申し上げましたが、ワタクシは運命の女神パルカ。これより12回の日曜日という――本日を除くと残り11回の――短い間ですが、以後、お見知りおきを」"




    scene bg fatalhall01 normal with dissolve_long

    "パルカはここまで言ったところで丁度中心へ辿り着いた。"

    "背筋を伸ばし、スカートをのすそをつまみ上げて一礼してから、再びゆっくりと口を開いた。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro nor big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「選定の終了にあたる12週間後、あなた方12人は同じ瞬間、同じ場所にいるはずでした」"

    show dia sta fro no1 big with std_change

    voice get_voice_filename("dia")
    parca "「けれども、その結果に辿り着くことなくあなた方の命は終了してしまったのです。場所こそバラバラでも、奇しくも全く同じ時間に」"

    show dia sta fro smi big with std_change

    voice get_voice_filename("dia")
    parca "「――その時こそ、≪因果の刻≫」"

    "いんがの、とき。"

    "パルカはそう言った。だが、私の理解は全く追いついていない。"

    "彼女の言葉が本当なら、海晴も私もここにいる全員が――死んでいることになる。"

    "そんなのは、おかしい。だって、私は普通に暮らしていた。"

    "実は幽霊だった？――そんなのもっと意味が分からない。"

    "混乱する思考の中、私は話の続きを聞くことにした。"

    show dia sta fro no2 big with ci_change

    voice get_voice_filename("dia")
    parca "「≪因果の刻≫において場所は重要ではないのですわ。何故なら、死の瞬間あなた方の意識は現実から乖離する。形而下の存在から、形而上の存在へと昇華したのですから」"

    show dia sta fro smi big with ci_change

    voice get_voice_filename("dia")
    parca "「生きているあなた方も時々は、形而上へと意識が移動することがあったでしょう――人はそれを時に夢と呼ぶ」"

    show dia sta fro cl1 big with ci_change

    voice get_voice_filename("dia")
    parca "「ここは――夢の世界と呼びましょうか」"

    show dia sta nor nor big with ci_change

    voice get_voice_filename("dia")
    parca "「人々の集合無意識の世界でもあり、いくつもの並行世界でもあり、あなた方それぞれの精神世界でもある――不安定で実存のないセカイ」"

    show dia sta fro sm2 big with ci_change

    voice get_voice_filename("dia")
    parca "「存在するかも不確かな世界をあなた方が認識できるように、ワタクシはこの≪運命の大広間≫を作って差し上げました」"

    "私は、周囲を見渡した。"

    "壁もない。天井もない。"

    "だがパルカが大広間と呼ぶと、確かにこの奇妙な空間は大広間であるように思えた。"

    show dia sta nor nor big with ci_change

    voice get_voice_filename("dia")
    parca "「名付けこそ、実存しないものに存在と意味を与えるもっとも単純で、もっとも強力な方法ですわ。お分かりいただけたでしょう？」"



    stop music
    scene black with dissolve



    voice get_voice_filename("aln", 1)
    alan_unk1 "「御託はいい。早く指名させろ」"

    $ gameinfo_cardbook_aln_unlocked = True

    "パルカの言葉を遮るようにして、男性の声がした。"

    "声は私の右隣、床の番号で言えば“Ⅻ”から聞こえた。"

    play music audio.restlessness
    scene bg fatalhall01 up
    show aln sta nor irr rev ci at ci_l
    with dissolve

    "褐色の肌に黒髪の男性だ。背が高く筋肉質で、目鼻立ちがくっきりしている。顔立ちからして、中東の人に見える。"

    "いや、ちょっと待って。"

    "少女も男性も、日本語がこんなにペラペラなことってあるのだろうか。"

    "この疑問は、もっと早く持つべきだった。「あ、日本語喋れるんだ」ってすぐに思わなくてはならなかった。"

    "あまりに自然で、気にしていなかったのだ。"

    show dia sta nor ama ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「焦ってもいいことはありません。説明はここからが大事なのですから」"



    "少女はあくまで落ち着いた口調で、男性を諌めた。"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「話を戻しましょう」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「あなた方12人の中で、運命の先に進めるのは１人だけです」"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「選定期間中こそ、あなた方の死因となった出来事はなかったことになっていますが、最後に残る１人以外は、結果的に本来の≪死の運命≫に戻りますわ」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「誰かが脱落した段階で、この世界は≪その人が本来の刻に死んだ世界≫に書き変わります。運命が巻き戻り、選定期間に為したことが失われるということですわね」"

    show dia sta fro sm2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「そして≪因果の刻≫から≪選定終了≫までの期間、あなた方は≪理を外れた存在≫と思っていただいて構いませんわ」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「つまり、この≪女神の選定≫以外の理由で死ぬことは決してない。死なない程度のケガなら、してしまうかもしれませんけれど」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「お間抜けの“Ⅰ”番サマ？　これであなたもお分かりでしょう？」"

    "パルカは私に視線を向け、続ける。"

    "ここまで聞けば、少女が何を言いたいのか嫌でも察してしまう。"

    show rnk uni sur su1 ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「12人が、殺し合う――？」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「90％正解ですわ。けれども、あくまで９割。実際に殺し合うなんて野蛮な方法は取りません」"



    voice get_voice_filename("dia")
    parca "「あなた方にはお互いを≪殺す≫のではなく、≪脱落させあって≫いただきます。だって――あなた方はもう死んでいるのですから」"

    hide aln
    show mhr uni pai irr rev ci at ci_l
    with ci_swap


    voice get_voice_filename("mhr")
    miharu "「…………嫌味だね」"

    scene bg fatalhall01 normal with dissolve

    "海晴と私以外の10人も、それぞれの反応をしていた。"

    "パルカや私たちの声は、この空間で反響し、全員に聞こえているのだろう。"

    "だが今の私には、この場にいる全員をしっかりと見る心の余裕はなかった。"

    "ただ一人、“Ⅵ”の人だけは落胆した様子で座り込んでいた。無気力で、眠っているかのようだった。女性だった。"

    "私は観察するよりも、わけの分からなさと言いようもない不安を解消するために、パルカの説明に耳を傾けていたのだった。"

    "信じる信じないは、その後でいい。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro no1 big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「選定の参加者を脱落させる方法は、３枚のカードを集めること」"

    show dia sta fro smi big with std_change

    voice get_voice_filename("dia")
    parca "「あなた方一人一人には≪現在≫≪過去≫≪未来≫を示す、≪氏名≫≪死因≫≪未練≫の３枚のカードが割り振られています」"

    show dia sta fro nor big with std_change

    voice get_voice_filename("dia")
    parca "「自分の情報が書かれた≪自身のカード≫をお持ちでしょうから、それは分かっていることでしょう」"

    show dia sta fro glo big with std_change

    voice get_voice_filename("dia")
    parca "「全く手掛かりがないところからでは選定が進みません。皆サマには≪自身のカード≫以外に、他の参加者のカードをランダムに３枚ずつ配っていますわ」"

    show dia sta fro no2 big with std_change

    voice get_voice_filename("dia")
    parca "「そしてこれからは、カードを自らの手で集めていただきます。選定の参加者それぞれの情報を知った時、情報という概念はカードという実存に変わります」"

    show dia sta fro gl2 big with std_change

    voice get_voice_filename("dia")
    parca "「あなた方の世界――この夢の世界ではなく現実世界で、情報を集めるのです。そうすれば、自然とカードを取得することができます」"

    show dia sta fro smi big with std_change

    voice get_voice_filename("dia")
    parca "「夢と現実を繋ぐもの――≪カードブック≫はすでにあなた方の手にあります。ほら、ここにも」"

    "言われて、私は視線を下に移した。"

    scene ecg cardbook clo with dissolve_long

    "手すりかと思っていたそれは、書見台であった。平たい部分に、一冊の本が載せられていた。"

    "赤茶の表紙に、金色の歯車のような装飾がなされている。"


    voice get_voice_filename("rnk")
    rinka "「この本……直未と見た。どうしてここに？」"

    "開いてみると、ライオン館で見たのと同じように、真ん中に長方形の空洞が空いていた。"

    scene ecg cardapp nor with dissolve


    voice get_voice_filename("rnk")
    rinka "「うわっ」"

    "その時、本から眩しい光が溢れた。"

    "私は反射的に目を閉じた。瞼越しから光が少しずつ弱まっていくのを感じ、徐々に目を開く。"

    "カードが、空中に浮いていた。４枚のカードは等間隔で並び、本の直上で静止していた。"

    "――Ⅰ・氏名・獅子舞凛火。"

    "――Ⅲ・氏名・フェデリーコ・カルミナーティ。"

    "――Ⅳ・死因・焼死。"

    "――Ⅸ・未練・金メダル。"

    "私の側に、これらの情報が書かれた面を向けている。"

    "記憶が曖昧なせいなのか、私の情報が書かれたカードは１枚しかない。それに他人のカード３枚を加えて、合計４枚だ。"

    "思わず海晴の方を見るが、本の周辺は光に包まれていてよく見えない。"




    scene bg fatalhall01 up
    show mhr uni nor ser rev ci at ci_l
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「自分以外にはカードの情報も、何枚持っているかすらも見えないってことだね」"

    show rnk uni nor que ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「だから、そっちの本の周りは光ってて見えないんだ」"

    "海晴は私の視線に気付いたのだろう、手短に発見を教えてくれた。"

    "パルカは私たちのことを気にせず、さらに説明を続ける。"

    show dia sta fro nor ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「指名の順番は、皆サマが意志表示をした後に決まりますわ。あなた方に割り振られた番号によって、指名ができなくなることはありません」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「指名した相手が自身を指名していた時、≪自身のカード≫１枚を参加者全員へオープンにした方が指名する権利を得ることができます」"

    "どちらも≪自身のカード≫をオープンにした場合、さらにもう１枚……パルカは続けた。"

    "お互いが３枚を公開した場合……優劣はつかず、指名が無効になるという。他の参加者に指名されるリスクを生むだけだ。"

    "そもそも自分の情報は三つしかないのだ。一つでも参加者全員に知られるだけでも大きなリスクになる。"

    "だが、結局そこで≪自身のカード≫を公開しなかったならば、自分が脱落してしまう。"

    "それに私は≪自身のカード≫を１枚しか持っていない。これは、どういうことなのだろうか。"

    "質問する間もなく、パルカは話を続けた。"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「他に、ご注意いただきたいこと。例えばⅠ番サマがⅫ番サマを指名、Ⅲ番サマがⅠ番サマを指名した場合、Ⅰ番サマがⅫ番サマを脱落させた後、Ⅰ番サマはⅢ番サマによって脱落させられますわ」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「指名の意志表示をした後、指名は割り振られた番号の順番に行います。これが基本のルールですわ」"

    show dia sta fro no1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「ただし、Ⅰ番サマがⅫ番サマを、Ⅻ番サマがⅢ番サマを指名した場合、Ⅰ番サマがⅫ番サマを脱落させてしまうとⅢ番サマの指名はなくなってしまいます」"

    show dia sta fro sm2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「このようにねじれが生まれる時――脱落者がもっとも多くなるように順番は入れ替わりますわ」"

    "私はあらためて、このカードの意味を理解した。"

    "知らない間に死に、女神の選定というものに参加させられ、カードを手にしていたのだ。"

    "カードを揃えて、相手を脱落させる。≪女神の選定≫と呼ばれているけれど、これではまるでゲームだ。ただし、命をかけるのは自分の未来。"

    "見知らぬ相手の情報を集めるというのは、簡単なことではない。だが、集めさえすれば……。"

    show rnk uni arm sad ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「３つの情報を知られたらおしまいってことでしょ？　そんなの……」"



    voice get_voice_filename("mhr")
    miharu "「……防御策、というのがあるらしい」"

    "私はそれを聞き、海晴をじっと見て続きを待った。"


    voice get_voice_filename("mhr")
    miharu "「自分を脱落させようと指名してきた相手のカードを３枚持っていること」"

    show mhr uni sco thi rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「その３枚のカードを捧げる――消滅させることで身を守れるらしい。指名してきた相手のカードも消滅する……ということだね」"

    show mhr uni nor ser rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「指名された側は、指名して来た相手を今後指名できなくなる代わりに、その相手にも指名されなくなる」"


    voice get_voice_filename("mhr")
    miharu "「ただしその場合、指名者は≪自身のカード≫を参加者全員に１枚オープンにすることで相手の防御を打ち破れる……合っているね？」"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「ええ。あなたはきちんと覚えていらっしゃるようで、安心いたしましたわ」"

    show rnk uni nor qu ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「もし、その二人が最後の二人になったら……どうなるの？」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「それは……その時が来たら説明しますわ」"

    "パルカはきっぱりとそう言った。"

    "私が「でも」や「それじゃ」などと食い下がっても、まるで相手にされなかった。"

    show mhr uni sco thi rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「もう一つ、指名されても脱落しない……免れるケースがあるね？」"

    "問い掛けた海晴に、パルカは不敵な笑みを浮かべた。"

    show mhr uni nor ser rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「例えばある人物を別の二人が同時に指名する場合」"



    voice get_voice_filename("mhr")
    miharu "「この時、指名の優先権の奪い合いが発生する。条件はさっきと同じ、『≪自身のカード≫を１枚参加者全員へオープンにすること』で間違いはないね？」"

    show rnk uni nor nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「どちらも≪自身のカード≫をオープンにしないで優先権をとらなかったら、指名は無効になる……？」"

    show dia sta nor sm2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「察しは……悪くはないようですわね。その通りですわ」"

    "海晴はパルカが説明を続けようとしたのを見て、本を閉じた。"

    scene ecg cardbook op1 with dissolve_long

    "私も本を閉じようとしたが抵抗があり、その間にカードがひとりでに本の中に戻っていた。"

    scene ecg cardbook clo with dissolve

    "そうなると抵抗がなくなり、元通りに閉じることができた。"

    "スマホのアプリでよくある見慣れた動作が、物理的に行われていた。"

    scene bg fatalhall01 up large
    show dia sta fro smi big at std_c
    with dissolve_long


    voice get_voice_filename("dia")
    parca "「一夜で指名を行えるのは一人につき一回まで、というのもお忘れなく」"

    show dia sta nor nor big with std_change

    voice get_voice_filename("dia")
    parca "「そして全員の指名の意志を確認してから、実際の指名に移ります」"


    voice get_voice_filename("dia")
    parca "「指名者が≪自身のカード≫をオープンにしたことにより、別の参加者がその方のカードが３枚揃ったとしても、実際に指名を行えるのは次の選定からですわ」"

    "選定にも流れというものがあるらしい。"

    "「指名するかどうか」を決めてから「実際の指名」を行うということ。"

    "パルカの語るルールは重要なものだというのは分かる。混乱する頭でも、必死についていこうとしていた。"

    show dia sta fro gl1 big with std_change

    voice get_voice_filename("dia")
    parca "「指名して相手を脱落させると、皆サマにもメリットがございますわ」"

    show dia sta fro nor big with std_change

    voice get_voice_filename("dia")
    parca "「それは、脱落させた相手からカードを１枚取得することができるということです。代わりに……」"

    scene bg fatalhall01 up with dissolve

    show aln sta nor rev irr ci at ci_l with ci_in


    voice get_voice_filename("aln")
    alan_num "「いい加減、もういいだろう？」"

    "そう言ったのは、先ほどもパルカを遮ろうとした男性だった。"

    show cha sta nor dis ci at ci_r with ci_in


    voice get_voice_filename("cha", 1)
    chan_num "「いや、やめて！　始まったら私！　私！」"

    $ gameinfo_cardbook_cha_unlocked = True




    voice get_voice_filename("cha")
    chan_num "「やだ！　ビル！　助けてえええええ！」"



    voice get_voice_filename("aln")
    alan_num "「黙れ」"

    show aln sta nor ang rev ci with ci_change


    voice get_voice_filename("aln")
    alan_num "「女神。君もこの調子では話を続けられないだろう？」"

    "悲痛に叫ぶ女性に対して、彼は何の感情も向けてはいなかった。"

    "疎ましさ、さえも。それは、女神も同じだった。"

    show dia sta nor nor ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「もう、仕方がありませんね。いいでしょう、それでは」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「――これより、今宵の選定を開始しますわ」"





    stop music fadeout 1
    scene bg fatalhall01 normal with fade_long
    play music audio.fatalhall
    pause 1

    "その後起きたことは、よく覚えていない。"

    "Ⅻの男性がⅥの女性を指名すると、二人の床はせり上がり、上の方へと消えて行った。"

    "その後しばらくして、Ⅻの男性だけが下りて来た。きっとそれが、≪指名≫とやらで、Ⅻの男性がⅥの女性の３枚のカードを持っていて、それを使って脱落させたのだろう。"

    "戻ってきた時に、男性は「Ⅷ・氏名だ」とパルカにカードを見せていた。"

    "これがきっと、さっき女神が「代わりに」と言いかけた話の続きなのだろう。"

    "誰のどのカードを取得したかという事実が他の参加者に知られてしまう。"

    scene bg fatalhall01 up large
    show dia sta fro cl1 big at std_c
    with dissolve


    voice get_voice_filename("dia")
    parca "「心配なさらなくても、この時間はあなた方の眠りの時間。現実の時間とは異なる狭間の刻ですわ」"

    show dia sta fro sm2 big with std_change

    voice get_voice_filename("dia")
    parca "「つまり目を覚ませば――いつもの朝」"

    show dia sta fro gl2 big with std_change

    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者は１名。これをもって、選定を終了といたしましょう」"

    "ぼんやりとした意識のまま、パルカのそんな声が聞こえた。"

    "意識は混濁していき、眠りに落ちる時のような感覚に襲われた。"

    "私はもう完全に思考停止していた。"



    voice get_voice_filename("rnk")
    rinka "「受け入れる方が無理だろ」"

    "――何も、かも。"

    $ renpy.end_replay()
    $ add_seen_chapter("1-4")

    $ persistent.sentei1_clear = True
    $ grant_achievement("divine_selection_01")

    jump f002
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

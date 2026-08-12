

label f011_02GH:







    $ set_info_scene("184")

    scene bg fatalhall01 up
    show rnk uni arm vig ci at ci_r
    with dissolve_long

    voice get_voice_filename("rnk", 1671)
    rinka "「私は、Ⅱ番を。海晴を、指名する」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia", 330)
    parca "「あら」"

    "私はそう言うと、パルカは少し驚いた顔を見せた。"

    "だが私たちが知り合いであることを知っている彼女は、その意図に気が付いたのか、一瞬、邪悪な笑みを浮かべる。"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「てっきり、今回はお二人とも指名なさらないのかと思いましたけれど」"

    show dia sta fro no1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「もし他に狙いがあるなら――いえ。それを邪推するのは、ワタクシの役目ではありませんね」"

    show dia sta fro no2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「Ⅱ番サマは指名を行いますか？」"

    show mhr uni nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("mhr", 827)
    miharu "「ぼくは指名をしないよ」"

    "海晴にアイコンタクトで合図をした。"

    "海晴は表情を変えず、小さく頷いた。"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「それではこれより、Ⅰ番サマによるⅡ番サマの指名を実施いたしますわ」"

    "いよいよ、私たちは賭けに出ることになる。"

    "円い床が動き出し、さっきまでいた大広間がどんどん視界の下へと移動していく。"







    $ set_info_location("16")

    scene bg fatalhall02 normal with fade_long
    pause 2
    scene bg fatalhall02 up with dissolve
    pause 1

    show mhr uni sco con rev ci at ci_l with ci_in

    voice get_voice_filename("mhr")
    miharu "「言葉はもう、多くはいらないね。話した通りだ。君がカードを３枚選んだあと、ぼくはそれを防ぐ」"

    show rnk uni nor smi ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「うん、分かってる」"


    play music audio.restlessness

    "運命の大広間に来た私たちは、パルカが来る前にそのことを話した。"

    "これで全てが終わるかもしれない。"

    "可能性がないわけではないのだ。"

    "私と海晴がお互いに指名できなくなり、≪女神の器≫になれる人はいなくなる。"

    "入れ物がなくなれば、女神が現実世界に存在できなくなる。"

    "運命の大広間にずっと居続けるのかもしれないけれど、神様のその後なんて私の知ったことではない。"

    "そうすれば私たちには未来が待っている。"

    "だから、試すのだ。"

    show dia sta fro no2 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「お二人とも、よろしいでしょうか」"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「楽しみですわね。もうすぐ、雌雄が決するのですから」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「12週間を待たずに、最後の一人が決定する。貴女サマが≪運命の終着点≫へとたどり着くまでには１週間の猶予がありますけれど、些末な問題ですわね」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「Ⅱ番サマよりは貧相な体ではございますけれど、可愛らしくて楽しみですわ」"

    show rnk uni arm nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「あなただって大して変わらないでしょ」"

    show dia sta fro cle ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら。ワタクシは女神ですわよ？　貴女サマのような人間の感覚で比べるのは浅慮が過ぎるというものですわ」"

    show rnk uni nor que ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「……ちょっと怒ってるよね」"

    "海晴が私の指名を防御すると分かっているから、その意味での落ち着きはあった。"

    "パルカの喜びようから見ると、それが裏切られたときにどんな反応をするのか恐ろしくもある。"

    "しかし、試してみなければ全てが始まらないのだ。"

    show mhr uni sco cau rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「もういいだろう。始めよう」"

    "海晴も考えていることは同じ。"

    "パルカは一瞬口を尖らせると、すぐに不敵な笑みに戻った。"

    show dia sta fro no2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それではⅠ番サマ。指名をどうぞ」"


    play music audio.electing
    scene ecg senteirinka serious with dissolve_long

    "私は頷いて。カードブックを開く。"

    "現れたカードの中から、迷うことなく３枚を選び取る。"


    voice get_voice_filename("rnk")
    rinka "「氏名――蛇鉈海晴。死因――自殺。未練――獅子舞凛火」"

    "これまでの指名のときとは違い、私は早口で３つの情報を口にした。"

    "私が言い終えたとき、海晴もカードブックを開いていた。"

    "光に覆われているからよく見えないが、海晴の手元にも同じようにカードが出現しているはずだ。"


    scene bg fatalhall01 up
    show dia sta nor ama ci at ci_c
    with dissolve_long

    voice get_voice_filename("dia")
    parca "「さて、Ⅱ番サマ。カードブックを開いていらっしゃると言うことは防御を行うということでしょうか？」"

    if flags_route_G:




        stop music fadeout 1
        scene ecg miharubye normal with dissolve_long


        voice get_voice_filename("mhr")
        miharu "「凛火、ありがとう。こうやってカードブックを開いていれば、少しだけ時間が稼げると思ってね」"


        voice get_voice_filename("rnk")
        rinka "「――え？」"

        "瞬間、背筋に嫌な寒気を感じた。"

        "海晴は一体何を言っているのだろうか。"

        "それが分かってしまうからこそ、私は頭が真っ白になりそうなところを、必死で堪えていた。"

        "だって、海晴が言っているのは、それは。"

        "それは。"





        play music audio.growapart
        scene bg fatalhall02 up
        show rnk uni arm ang ci at ci_r
        with dissolve_long

        voice get_voice_filename("rnk")
        rinka "「海晴！」"

        show mhr uni sco smi rev ci at ci_l with ci_in

        voice get_voice_filename("mhr")
        miharu "「君と特別な関係になることができて、本当によかった。幸せだった。悔いがない、とは言わないよ」"

        show mhr uni nor rea rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「でもぼくは君に言っただろう？　≪女神の選定≫におけるぼくの目的は君を最後の一人にすること。ぼくの命を捧げてでも」"

        show rnk uni arm sad ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「何言ってるの海晴？　海晴は私のカードを持ってる。だから」"

        "あまりに突然のことに、私は完全に動転してしまっていた。"

        "感情を抑えることができず、どんどん溢れてきてしまう。"

        show mhr uni pai lie rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「また君に、嘘をついてしまったね。思えばぼくは、凛火に嘘や隠し事をしてばかりだった」"

        show rnk uni arm vig ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「いいよ、そんなの。海晴がすることは一つ。今出ているカードの中から、私のカードを３枚選ぶだけ」"

        show rnk uni arm sad ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「そうすれば――」"

        show mhr uni nor ser rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「ぼくの本心を話すよ。ぼくは、凛火に確実に生きて欲しいんだ」"

        show rnk uni arm ang ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「私だって、海晴と生きたいよ！　だって私たちは、これからなんだよ？」"

        scene ecg miharubye serious with dissolve_long


        voice get_voice_filename("mhr")
        miharu "「これからだからこそ、ぼくの引き際なんだ。ぼくは自分で死を選んだ」"


        voice get_voice_filename("mhr")
        miharu "「元から、他の参加者を押しのけて生き残る権利なんてなかったんだ」"


        voice get_voice_filename("rnk")
        rinka "「海晴、言ってたよ。自分のことを許せたって……」"


        voice get_voice_filename("mhr")
        miharu "「それも、本心だよ」"


        voice get_voice_filename("rnk")
        rinka "「なら、なんで」"


        voice get_voice_filename("mhr")
        miharu "「これがぼくの答えだ。凛火の運命を変えるためなら、死ぬなんて怖くはないよ」"


        voice get_voice_filename("rnk")
        rinka "「違う、そんなの違う」"

        show ecg miharubye normal with ecg_change


        voice get_voice_filename("mhr")
        miharu "「違わないよ。ぼくは凛火を――愛しているからね」"


        voice get_voice_filename("rnk")
        rinka "「私だって好きだよ、海晴のこと。ああ私はきっとこれから、人生で初めて恋愛するんだって信じてた」"


        voice get_voice_filename("mhr")
        miharu "「ありがとう。凛火がそう想ってくれたこと、ばればれだったよ。だから、ぼくは満足できた」"


        voice get_voice_filename("rnk")
        rinka "「満足なんてしないで。だって私たち、まだキスだってしてない」"


        voice get_voice_filename("mhr")
        miharu "「ああ。だから言っただろう？　悔いがないわけではないと」"


        voice get_voice_filename("rnk")
        rinka "「なら――！」"

        "海晴は答えず、カードブックを閉じた。"

        "海晴はただ、微笑むだけだった。やっぱりその顔はとても綺麗で、素敵で、儚かった。"


        scene bg fatalhall02 up
        show dia sta nor ama ci at ci_c
        with dissolve_long

        voice get_voice_filename("dia")
        parca "「貴女サマは今、カードブックを閉じました。それが何を意味するかお分かりでしょうか？」"

        show mhr uni nor rea rev ci at ci_l with ci_in

        voice get_voice_filename("mhr")
        miharu "「ぼくに分からないと思うかい？」"

        show rnk uni cat ten ci at ci_r with ci_in

        voice get_voice_filename("rnk")
        rinka "「待って！　待ってよ！　まだ――」"

        show mhr uni nor ser rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「凛火」"

        show rnk uni arm imp ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「海晴！」"

        show mhr uni pai lie rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「さよなら」"

        show rnk uni arm uil ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「えっ」"

        show mhr uni nor ser rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「再会を望む言葉はもういらない。これはぼくの選んだ別れだ」"

        show mhr uni nor nor rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「君と特別な関係になった３日間。別れが近いと思うと、それはとても濃密な時間だった」"

        show rnk uni arm imp ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「やだ、やだやだ。私……嫌だよ……そんなの……別れなんて……」"

        scene ecg trianglecard with dissolve_long

        "私の選んだ３枚のカードは、私の意志とは無関係に動き出す。"

        "カードを掴もうと手を伸ばしても、身を乗り出しても、止めることができなかった。"


        scene bg fatalhall02 up
        show rnk uni arm ang ci at ci_r
        with dissolve_long

        voice get_voice_filename("rnk")
        rinka "「お願い！　パルカ！　女神様！　止めて。もう一度。せめて次の選定まで、保留に……」"

        show mhr uni pai lie rev ci at ci_l with ci_in

        voice get_voice_filename("mhr")
        miharu "「いいんだ、凛火。選定が始まってからの約３ヵ月間生きたぼくの記憶は、君にしか残らない。凛火しか知らないぼくがいる。それを想像するだけで、とても幸せだ」"

        show rnk uni arm sad ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「そんなの、幸せじゃないよ……」"

        scene ecg trianglecard cover with dissolve_long

        "３枚のカードは止まることなく、運命の大広間の中心で停止した。"

        "カードから溢れる光はそのまま、運命の大広間を包むほどに広がっていく。"

        scene ecg miharubye light with dissolve


        voice get_voice_filename("mhr")
        miharu "「夢の世界とはよく言ったものだよ。ぼくが過ごしてきた今日までの日々はなるほど、夢のようだ」"


        voice get_voice_filename("mhr")
        miharu "「生きて、生きて、生きて、生き続けて欲しい」"


        voice get_voice_filename("rnk")
        rinka "「あ……やだ……」"

        "私は、力を失って膝をついていた。"

        "この光は止められない。"

        "海晴が脱落していくのは、本来の死の運命に戻っていくのは――止められない。"


        voice get_voice_filename("mhr")
        miharu "「ぼくは、ぼくしか知らない凛火を知っている。この期に及んで、ぼくは君を独り占めできることを喜んでいる」"

        scene ecg trianglecard cover with dissolve

        "光は、もう海晴の姿すらかき消してしまっていた。"


        scene white with dissolve_longest


        voice get_voice_filename("mhr")
        miharu "「凛火の人生にはこれから、色々な特別が増えていくだろう。いつかぼくを超える特別が現れたら、その時は――」"


        voice get_voice_filename("mhr")
        miharu "「――なら」"

        "海晴の言葉は、最後まで聞き取ることができなかった。"


        voice get_voice_filename("rnk")
        rinka "「――――たね」"

        "そして私の意識は、混濁の中へ落ちていく。"



    if flags_route_H:



        "海晴はパルカの質問に、「違うよ」と短く答えた。"

        show mhr uni sco smi rev ci at ci_l with ci_in

        voice get_voice_filename("mhr", 853)
        miharu "「凛火、今までありがとう」"

        show rnk uni cat ten ci at ci_r with ci_in

        voice get_voice_filename("rnk", 1696)
        rinka "「ちょっと何して……」"

        "海晴はそう言うと、カードブックを閉じた。"

        "私はすぐに、その意味を理解した。"

        scene ecg trianglecard normal with dissolve_long

        "３枚のカードは私の制止も聞かず、運命の大広間の中心へと移動していく。"


        voice get_voice_filename("rnk")
        rinka "「――――――！」"

        show ecg trianglecard cover with ecg_change_wait

        "声にならない叫び声をかき消すようにして、大広間をカードから出る光が埋め尽くす。"

        "海晴とはもう言葉を交わすこともできず、私の意識は光に浸食されていく。"


        scene white with Dissolve(3)
        pause 1

        "私の――せいだ。"

        "ただその後悔だけが、脳裏に焼きついていて。"







    stop music fadeout 2
    scene ecg miharudie blue with dissolve_longest
    play music audio.death
    pause 1

    "一人の少女がいた。"

    "少女は、思い込みが強く、自分で自分の逃げ場を奪ってしまうような性格をしていた。"

    "だから、痛みを欲した。"

    "欲し続けた。"

    "ある時、邪悪を知った。"

    "人の心に巣食う嫉妬という闇を。"

    "そしてその闇は、自分の中にも潜んでいることを知ってしまった。"

    "だから、自分を否定した。"

    show ecg miharudie red with dissolve

    "元より彼女の心は、逃げ場のない牢獄の中にあった。"

    "心の牢獄の中では、自分を否定する方法は死しかなかった。"

    "眠るように死ぬことを、少女は選んだ。"

    "血に濡れた布団の上に横たわる彼女は、まるで曼殊沙華の花畑の上で眠りにつくようであった。"







    python:
        set_info_scene("185")
        set_info_location("05")




    stop music fadeout 2
    scene bg fatalhall02 up with fade_longest
    play music audio.kinpaku
    pause 1

    show rnk uni arm ten ci at ci_r with ci_in

    voice get_voice_filename("rnk", 1698)
    rinka "「み……は……る……」"

    "下層に戻ってきても私は立ち上がることができず、膝をついたまま動くことができなかった。"

    "海晴は今、脱落した。"

    "私の中には海晴が死ぬときの映像が流れ込んできたのだ。"

    "ユウくんもスケールさんもアランさんも、みんなそうだった。"

    "私が指名し、踏み台にした。"

    "とうとう、海晴まで。"

    show rnk uni arm uil ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「あ、あ……私は……」"

    "この世で一番大切なものを、踏み台にしてしまった。"

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia", 343)
    parca "「ふふ、ふふふ……」"

    "女神は、不敵に笑う。"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「ふふふふふふふ！」"

    show rnk uni ang an2 ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「何がおかしいんだっ！」"

    "私は、泣きながら怒っていた。"

    "もう何がなんだか分からないまま、怒りの言葉を口にしていた。"

    "涙は、私の激しい言葉に飛ばされるようにはじけ飛ぶ。"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「うふふふふふ！」"

    "パルカは、笑うことをやめなかった。"

    "その悪魔のような表情が私に向けられていることに気付くのに、そう時間はいらなかった。"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「やっと！　やっと！　やっとこの時が来ましたわ！」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマを、Ⅰ番サマを、獅子舞凛火サマを、ワタクシの≪器≫にできる{rb}瞬間{/rb}{rt}とき{/rt}が！」"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「この悦びを微笑み以外の一体何で表現できましょう？」"

    "怖い、と思った。"

    "私は本能的に、パルカに対して恐怖を覚えていた。"

    "それは海晴がいなくなってしまった悲しみと混ざり合い、震えとなって私の体にあらわれた。"

    show dia sta nor rev ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら。もしかして貴女サマは感じ取っているのかもしれませんねぇ」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシと同じ肉体を持つ、貴女サマであれば」"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「何を……？」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマが辿り着いていない真実であれば、ワタクシの口から語るまでもありませんわ」"

    show dia sta nor rev smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「大切なのは、ワタクシの悲願がようやく叶うということですわ」"

    show rnk uni arm sad ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「もう、どうでもいい。悲しませてよ……私は大切な人を、失ったんだ。あなたの御託に付き合っている暇はない」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「では少しだけ。≪女神の選定≫についてお話をいたしましょう」"

    "私はヤケになりながら、円い床の上で何も考えずに立っていた。"

    "その態度を彼女は私が話を聞こうとしていると判断したのか、そのまま話を続けた。"



    play music audio.restlessness
    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「はっきり申し上げましょう。≪女神の選定≫とは、運命を変える儀式」"


    voice get_voice_filename("dia")
    parca "「運命の奴隷の皆サマの≪死の運命≫を変えることのできる唯一の方法でございます」"


    voice get_voice_filename("dia")
    parca "「ワタクシは≪器≫である人間が命を落とすその瞬間、因果により結ばれた12人の運命をねじ曲げる」"


    voice get_voice_filename("dia")
    parca "「無限に存在する運命の支流。未来の可能性」"


    voice get_voice_filename("dia")
    parca "「その中から運命の奴隷である12人の皆サマが≪死ななかったこと≫になっている世界を探し、糸を紡ぐように束ねるのです」"


    voice get_voice_filename("dia")
    parca "「けれども、それは世界への反抗に等しいこと。捻じ曲げられた運命には、戻ろうとする力が働きます」"



    scene bg fatalhall02 up
    show rnk uni nor que ci at ci_r
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「戻ろうとする力……？」"

    "私は思わず、聞き返していた。"

    "知りたくなっていた。"

    "何故私たちには束の間の希望が与えられたのか。世界ってやつが覆る可能性は、まだあるのかって。"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「この世界は、認知の上に成り立っていますわ。皆サマがリンゴをリンゴだと思うからこそ、リンゴはリンゴとして存在することができるのです」"


    voice get_voice_filename("dia")
    parca "「リンゴがこの世界でミカンと認識されれば、この世界のリンゴは全てミカンになってしまいます」"


    voice get_voice_filename("dia")
    parca "「つまり。獅子舞凛火サマという貴女サマが生きているのは、貴女サマが誰かに生きていると認識されているからでございますわ」"


    voice get_voice_filename("dia")
    parca "「世界の本流――もっとも、存在する世界が違えばどれが本流かも変わってしまうのですけれど――において、≪獅子舞凛火は死んでいる≫と認識されているとしましょう」"


    voice get_voice_filename("dia")
    parca "「そこに貴女が生きているという世界を紡ぐことで、矛盾が生まれる」"


    voice get_voice_filename("dia")
    parca "「≪獅子舞凛火は死んでいる≫のに、≪獅子舞凛火が生きている≫という矛盾」"


    voice get_voice_filename("dia")
    parca "「この矛盾がある限り、世界はより広く認知されている方に戻ろうとします。これが、運命が元に戻ろうとする力」"


    voice get_voice_filename("dia")
    parca "「強引に束ねられた運命は、再びそれぞれの支流に別れようとするということでございます」"


    scene bg fatalhall02 up
    show rnk uni arm ang ci at ci_r
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「それなら、≪海晴が生きている≫支流も存在するんだよね？　海晴も私も生きている可能性が！　今からでも、その世界に変えられないの？」"

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「貴女サマであれば答えは分かっているのでしょう？　ワタクシは万能の絶対神ではございません」"

    show rnk uni ang an1 ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「なら、≪海晴だけが生きている≫世界でもいい。あんな別れ方をするくらいなら――」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシの話が、貴女サマに希望を持たせてしまったみたいですわね。残念ながら、それも不可能でございます」"

    show dia sta fro gl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマがⅡ番サマを脱落させた時点で、Ⅱ番サマが生きている世界は元に戻る……この世界から遠ざかってしまいます」"

    show dia sta fro cl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「遠ざかっていく世界を引き戻す力は、今のワタクシにはございません。もっともそれが可能でも、ワタクシは行いませんけれども」"

    show rnk uni arm imp ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「海晴はさ、あなたの元の≪器≫だったんでしょ？　夢の中で話もしたって言ってた。同情とか親近感とか、そういうものはないの？」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシには、理解できない感情ですわ。器はあくまでワタクシが現実世界に存在するためのもの」"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「一生この世界にいればいい」"

    show dia sta fro cl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それはお断りさせていただきますわ。ワタクシが器を借りず≪夢の世界≫に存在できるのもまた、12週間」"

    show rnk uni nor nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「それを過ぎると、どうなるの？」"

    show dia sta fro gl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それはすでに、この世界では存在しない可能性でございます。お話ししても、あなたには理解できない事象ですわ」"

    "パルカは≪運命の大広間≫の中心から、私に向かって一歩近づいてきた。"

    "震えは止まったが、やはり思っていた。"

    "この少女は人間ではない。女神だと。"

    "その両の目は私を釘付けにする。まるで体が石になってしまうかのような感覚だ。"

    show rnk uni nor que ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「私たちは、何{rt}・{/rt}をさせられてたの？」"

    scene ecg parcawalk nor with dissolve_long


    voice get_voice_filename("dia")
    parca "「それはお話しするまでもないことでございます。これから、ご覧いただけましょう」"

    "女神が一歩近づく度、世界が縮小していく。"

    "それは、突然の変化だった。"


    voice get_voice_filename("rnk")
    rinka "「……何？」"

    "地響きともに、≪運命の大広間≫が崩壊を始めていく。"

    "私は戦慄した。ここにいれば、私も崩壊に巻き込まれる。"

    "でも、≪夢の世界≫から帰る方法なんて分からない。"


    voice get_voice_filename("dia")
    parca "「恐れることはございません」"

    "崩壊していく世界は、光に変わっていく。"

    "光は集束して、女神パルカに集まっていった。"


    scene bg fatalhall02 up
    show dia sta fro gl1 ci at ci_c
    with dissolve_long

    voice get_voice_filename("dia")
    parca "「貴女サマに分かる言葉で説明をすると、≪運命の大広間≫とは、人間の存在を収集するためのシステム」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「選定の参加者が脱落するとき、≪死んでいる≫という認知だけが、元の世界には残ります。つまり、その方の想いは元の世界に戻らないということですわ」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「世界からあぶれてしまった想いという欠片は、この≪運命の大広間≫に{rb}概念{/rb}{rt}ゆめ{/rt}となって収容される――ゆえに、皆サマは≪運命の奴隷≫」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「凛火サマ。貴女サマは、奴隷から解放され、ワタクシの器となった」"

    "崩壊していく世界の中、一切動じることはなく、白の女神は妖艶に微笑んでいた。"

    "一言話すたびに一歩ずつゆっくりと、光を集めながら私の方へと近づいてくる。"

    "私はわけの分からないまま、ただ立っていることしかできなかった。"

    "この円い床の上では、逃げ場所がない。"

    "女神が接近してくるのを、ただ息を呑んで見守ることしかできない。"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「11の夢は、ワタクシの力に変わります」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「その力を消費することで、ワタクシが現実世界に存在するという奇蹟を起こすのでございますわ」"

    show rnk uni arm vig ci at ci_r with ci_in

    voice get_voice_filename("rnk")
    rinka "「そのために私たちに束の間の希望を与えたっていうの？　だとしたらそれは、人を弄ぶのと同じ」"

    show rnk uni arm ang ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「この場所にいたみんなは、あなたの踏み台になったってことでしょ？」"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「何か……問題がございましたか？」"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「私は、あなたが憎い」"

    "私は、はっきりとそう口にすることができた。"

    "ごめん、おばあちゃん。"

    "私は目の前の存在を、心から憎いと思った。"

    show rnk uni nor nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「いいよ、来て。あなたが私の中にいてくれれば、私は一生あなたを恨み続けられる」"

    scene bg fatalhall02 normal with dissolve

    "パルカは私に向かって、手を伸ばしてくる。"

    "その手のひらは小さく、腕は折れてしまいそうな程細かった。"

    "私は彼女に応えるため、同じように真っ直ぐと手を伸ばした。"

    "パルカの腕は私と触れ合うことはなく、そのまま私の胸に触れた。"

    "パルカの白い手は、私の胸の中へと潜っていく。"

    "私の視界からは、彼女が自分の中へと貫通していくように見えた。"

    "パルカに集まっていた光はやがて、私に集束していく。"

    if flags_route_G:






        play music audio.firedeath
        scene ecg mindbattle normal with dissolve_long

        "≪運命の大広間≫を構成していた光がそうさせているのか、私が自分で思い出しているのかは分からない。"

        "けれども目を閉じた瞼の裏には、たくさんの夢が浮かんでいた。"

        "私の知らないところで脱落をした、チャンさんと魯さん。彼らにもこの一時的な希望の中で、抱いた想いがあっただろう。"

        "私に子供への想いを託してくれた、桂子さん。きっと旦那さんとは深いところでは通じていたから、手紙なんて必要なく、子供には桂子さんが決めたのと同じ名前が与えられていた。"

        "ごめんね、ソーニャ。私たちの幸せを願ってくれたのに、結局私一人しか生き残ることができなかった。"

        "でもパサジールにはちゃんと、もっと色々な世界を見せてあげるから。"

        "刹那の出会いでも、ユウくんを孫のように愛した茂継さん。最後まで好きになれはしなかったけれども、決して嫌いなんかじゃなかった。"

        "彼には彼の信念があり、ユウくんに授けたい願いがあったから。"

        "直未を殺害した、ユウくん。そのことを一生許すことはできない。"

        "けれど彼の悲しみだけは、忘れてはいけないと思った。きっとこの世界のあらゆる場所に存在する、悲劇。"

        "ただ普通の日常を願うなんていう、私と同じ未練。言葉は同じでも、それらがもつ意味は全く違った。"

        "知らないからこそ、願うこと。"

        "だから私は彼でさえも、恨むことができなかった。"

        "ずっと強かった、オデットさん。"

        "彼女はきっと、自分の運命を受け入れたのだ。≪死の運命≫とはすなわち、人生の結果。"

        "一秒一秒を後悔することのなかった彼女だからこそ、自ら潮時だと去っていった。"

        "スケールさんの生への執着は、私には一切否定ができない。"

        "だからこそ私には、私の意志でもって彼を脱落させるという答えしかなかった。"

        "彼のことを否定できなくても、分かり合うことはできないから。"

        "一度だけ現実世界で出会ったフェデリーコさんは、やっとつかんだ勝利の喜びに震えていた。"

        "彼に何があったのか詳しくは知らないけれど、彼にとっての人生は、充実したものになったに違いない。"

        "私の瞳が妹と似ていると言ったのはアランさん。"

        "彼の見せた生き方は、私ではなし得ないものだろう。"

        "だからこそ私は彼のことをすごいと思った。"

        "私を私だと教えてくれた海晴。"

        "恋することが何か分からないけれど、海晴が告白してくれたことがきっと、私にとっての一番の転機だった。"

        "生き方全部を変えるほど、鮮烈な色だった。"


        voice get_voice_filename("rnk")
        rinka "「海晴……海晴……」"

        "パルカの長い話を聞いていたから辛うじて抑えられていた悲しみが、どっと襲い掛かってきた。"

        "直未の時とは違う。"

        "海晴はもう、帰ってこないのだ。"

        "現実世界に戻ったとき、私はより大きな激しい感情の奔流に押しつぶされるだろう。"

        "それでも、生きなければならない。"

        "私は生きて、生きて、生きて、生き続けるのだ。"


        voice get_voice_filename("dia")
        parca "「残念、ながら。それは不可能なのでございます」"


        voice get_voice_filename("dia")
        parca "「ふふ、ふふふふふ！」"

        "どこからか、声が聞こえた。"

        "とても――鬱陶しい――声が――。"


        voice get_voice_filename("dia")
        parca "「言ったでしょう？　貴女サマを≪器≫にすることがワタクシの悲願でしたと」"


        voice get_voice_filename("dia")
        parca "「なぜなら」"

        "声が少しずつ――遠くなっていく。"

        "それは、きっと。"


        voice get_voice_filename("dia")
        parca "「貴女サマの体は、ワタクシがいただきますわ」"

        "――だから。"


        voice get_voice_filename("dia")
        parca "「貴女サマが前の≪器≫であるⅡ番サマと出会ってからずっと、ワタクシは貴女サマを求めていました」"


        voice get_voice_filename("dia")
        parca "「Ⅱ番サマが貴女サマと出会えたのが奇跡であるように、ワタクシが貴女サマに出会えたのもまた奇跡」"


        voice get_voice_filename("dia")
        parca "「Ⅱ番サマの≪因果≫に貴女サマを巻き込むことは、決して難しいことではありませんでしたわ」"


        voice get_voice_filename("dia")
        parca "「お二人はとても強い運命の環の中にいらっしゃいました。お二人の運命は螺旋の中心に向かっていくかのように、互いに引き合っていましたから」"


        voice get_voice_filename("rnk")
        rinka "「――ぷはっ！」"

        "ようやく、私は自分の意識を取り戻す。"

        "パルカの言葉は断片的だが、聞こえてきていた。"

        "きっと今彼女がしようとしているのは、海晴の時とは違う。"


        voice get_voice_filename("dia")
        parca "「貴女サマは元より、捻じれた運命の中で産み落とされた子供」"


        voice get_voice_filename("dia")
        parca "「貴女サマ自身が気付いていませんでしたけれど、貴女サマにも≪器≫の力の一部が流れ込んでいたようですわ」"


        voice get_voice_filename("dia")
        parca "「だから貴女サマの{rb}肉体{/rb}{rt}からだ{/rt}も{rb}精神{/rb}{rt}こころ{/rt}も、ワタクシと{rb}同質{/rb}{rt}おなじ{/rt}。他の皆サマでは不可能だった真の奇蹟をこれから見せてあげましょう」"


        voice get_voice_filename("dia")
        parca "「その頃には、もう貴女サマの意志は消滅しているでしょうけれど」"

        "内臓を直接かき回されることがあれば、きっとこんな感覚なのだろう。"

        "体の中に入ってきた異物に、嘔吐してしまいそうなほど息苦しくなる。"

        "パルカの言葉を解読するのであれば、彼女は――。"

        "私の意志を奪い取ろうとしている。"

        "そして、それは――。"


        voice get_voice_filename("dia")
        parca "「貴女サマをいただいて、ワタクシは現実世界の住人になりますわ」"

        "――正しかった。"

        "でも、私には特別な力なんて何もない。"

        "パルカの企みに抵抗する意志はあっても、手段がなかった。"

        "心が他人に奪い取られるなんて、あってたまるか。"

        "海晴にだって、奪われなかったのだ。"


        voice get_voice_filename("rnk")
        rinka "「ふざ……ふざけんなよ！」"

        "だから心が侵食されたって自覚があっても、私はそう叫ぶことができた。"

        "やがて私の薄弱な意識は、パルカの真っ白な淀みない心に塗り替えられていく。"

        $ add_seen_chapter("11_3-1")

        $ persistent.sentei11G_clear = True
        $ grant_achievement("divine_selection_11")



    if flags_route_H:





        play music audio.death
        scene ecg mindbattle normal with dissolve_long


        voice get_voice_filename("dia", 398)
        parca "「とても、か弱い心ですこと」"

        "女神の声が、私の中で直接響いた。"

        "それは優しく、温かく、身を委ねれば快感すらあった。"

        "私はもう、抵抗するという意志を失っていた。"

        "女神という私よりも上位な存在が、私を飲み込んでいく。"

        "そのことを、ただ受け入れるのみ。"


        voice get_voice_filename("dia")
        parca "「貴女サマは、ワタクシの≪器≫ではありません」"


        voice get_voice_filename("dia")
        parca "「貴女サマは心も体も特別。ワタクシと同じ性質を持っているのですわ」"


        voice get_voice_filename("dia")
        parca "「これからお見せするのは、真の奇蹟」"


        voice get_voice_filename("dia")
        parca "「もっとも貴女サマは、何も{rb}目撃す{/rb}{rt}み{/rt}ることはできませんけれど」"

        "おかしい、と思っていた。"

        "海晴は≪女神の器≫であったときも、自分の意志はあったと言っていた。"

        "自分の中に、別の存在が入っているだけ。"

        "決して女神そのものになるというわけではない。"

        "でも、今は――。"


        voice get_voice_filename("dia")
        parca "「ワタクシは貴女サマをいただいて、現実世界の住人になるのです」"

        "――ということらしい。"

        "それを――証明する――ように――。"

        "私の――ワタクシはすぐに――意識はもう――貴女サマの体を――頂戴いたしま――なくなって――す。"





        stop music fadeout 1
        scene black with dissolve_long
        pause 1

        "Ⅰ番サマは、こうしてワタクシになりました。"

        $ add_seen_chapter("11_4-1")

        $ persistent.sentei11H_clear = True
        $ grant_achievement("divine_selection_11")

    $ renpy.end_replay()

    jump f012_01GH
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

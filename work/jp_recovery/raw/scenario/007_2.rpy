


label f007_2:








    python:
        set_info_scene("97")
        set_info_date(6, 15, "fri")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "話の結論は出たが、落ち着けはしなかった。"

    "準備があるため、そのままオデットさんと彼女の拠点へ向かうとのことだった。"

    "ここから車で２時間程度の場所だそうだ。"

    "すでに簡単には足がつかないように車の用意はしてあるらしい。"

    show rnk sci nor nor at std_c with std_in

    voice get_voice_filename("rnk", 972)
    rinka "「疲れた……」"

    "色々なことがあり過ぎて、今日はどっと疲れてしまった。"

    "できることならそのままベッドへ飛び込みたいが、そうもいかない。"

    "今夜はその拠点という場所で一晩を明かさなければならない。"

    "準備が必要、ということらしい。"

    "本当に、現実感のない話だ。"

    "私は着替えやスマホのモバイルバッテリーを準備しながら、オデットさんとのやり取りを思い返していた。"

    if flags_route_A:



        "オデットさんが協力してくれる。"

        "正直に言って、それはとても心強かった。"

        "何より、ソーニャに対し両親を人質にとって交渉をしたということからいい印象はなかったが、実際に話してみた彼女はそこまで悪い人とは思えなかったのだ。"

        "あの人のことが、分からない。"

        "無条件とは言っていたけれど、結局、自分の≪氏名≫を私に伝えたという意味ではマイナスのはず。"

        "考えても無駄かと思い、私は考えるのをやめた。"

        "あの人に対しては、事前に予想をしたらしただけ、覆されて慌ててしまう。"

        "だったら、かえって何も考えない方がいいだろう。"

    if flags_route_B:



        "私の選択は、本当に正しかったのだろうか。"

        "自問をし始めると、それは留まるところを知らない。"

        "直未のため。"

        "――直未のためなんだ！"

        "私は心の中で、それだけを考えるようにした。"

        "自分が脱落すること。"

        "それは、その瞬間まで考えないことに決めた。"



    "結局、いつもの通り私は自分の思考に蓋をするという結論に至った。"

    "だが、違っているのは、この気持ちだった。"

    show rnk sci arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私は、必ず」"



    voice get_voice_filename("ode", 322)
    odette "「おーい、まだかー？」"

    "待つのに飽きたのだろう、店の方からオデットさんが私を呼ぶ声がした。"

    "私は今行きますと返事をして、階下へと向かった。"







    $ set_info_location("18")


    play music audio.gimon
    scene bg lion02 nightclose with fade

    show ode noj nor nor rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「さて、じゃあ行くとするか」"

    "ライオン館の前には、青色の車が停められていた。"

    "塗装には上品な光沢があり、街で見かける大衆車とは違うように思える。"

    "いわゆる、高級車だ。"

    "しかもハンドルが右についているから、どうやら外車のようだ。"

    "明らかに悪目立ちするような車だった。"

    show rnk sci nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あの、運転って……」"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「かかっ。車なんて船の操縦に比べれば簡単だ」"

    show ode noj nor inn rev with std_change

    voice get_voice_filename("ode")
    odette "「日本は……右側通行だったか？」"

    show rnk sci arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「左！」"

    "とぼけるオデットさんに向かって、私は思わず叫んでいた。"

    "この人の運転する車に、私は今から乗り込まないといけない。"

    "この後およそ２時間、予想よりもずっと荒い運転に乗り合わせることとなった。"






    python:
        set_info_scene("98")
        set_info_location("36")

    scene bg warehouse with fade_long
    pause 1

    $ show_hud()

    show rnk sci arm sad at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「……つかれた……」"

    show ode noj nor lau rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「かかっ、嬢ちゃんは貧弱だねぇ」"

    "豪快というにはあまりに雑な運転に、私はすっかり疲弊していた。"

    "ただでさえ精神的に疲れていて、時間的にも眠くなり始める時間なのに、肉体的にもどっと疲労が現れてしまった。"

    "オデットさんに対し、答える元気すらなくなっていた。"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「とまあ、どっかの配送会社が潰れて以来、そのままにされている廃墟みたいなもんだ」"




    play music audio.investigation
    scene bg warehouse large:
        subpixel True
        align (0.0, 0.5)
        linear 100 xalign 1.0
    with dissolve_long

    "着いた場所は、郊外の海沿いにある倉庫だった。"

    "来る途中の道路標識で横浜方面という表示があったので、その辺りだろう。"

    "窓ガラスは割れあちこちサビだらけで、オデットさんの言う通りいかにも廃墟という雰囲気だった。"

    scene bg warehouse with dissolve

    show rnk sci sur su1 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「寂れてるっていうか……寂しいっていうか」"

    show ode noj arm smi rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「ま、当時のものは何もねーからな。それに会社を潰しちまった経営者の怨念でもこもってたりしてな」"

    show rnk sci arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「そっ、そういう話はなし！」"

    show ode noj arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「怖がってんのかぁ？　幽霊なんかいやしねーよ」"

    "私も幽霊を信じているから怖いというわけではないけれど、ここは薄暗いし、ひんやりとしていて嫌な感じがした。"

    hide ode
    hide rnk
    with std_out




    voice get_voice_filename("aln")
    alan_unk3 "「誰だ？」"

    show rnk sci sur su2 at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「……っ！」"

    "私は暗闇の中から聞こえた声に、思わず肩に力を入れてしまった。"

    "まさか――などとありえないことを思うよりも前に、その声に聞き覚えがあることに気付く。"

    show aln sta nor nor rev at std_l with std_in

    voice get_voice_filename("aln")
    alan "「貴様は……」"

    "声の主はアラン・スコーピオンさんだ。"

    "目が慣れてきて、彼の姿も徐々にはっきり見えるようになる。"

    "オデットさんが拠点に使っている倉庫を、アランさんも使っているということだろうか。"

    "そんな確率、限りなく低い。"

    show ode noj nor gla at std_r with std_in

    voice get_voice_filename("ode")
    odette "「よー、アラン。連れて来たぜ？」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「……遅かったな」"

    python:
        add_character_cards("aln", ["11_name"])

    "私の疑問は、すぐに払拭されることとなった。"

    show rnk sci arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「まさか、二人とも……仲間？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「仲間ではない」"

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「嬢ちゃんと同じ、一時的な協力関係さ。ま、つまりこいつはリンカとも協力関係ってわけさ。文句はないね？」"

    "アランさんはいつも通りの無表情で、オデットさんは底の見えないにやりとした表情を浮かべている。"

    "私が恐怖を感じていたⅪとⅫの二人。"

    "まさかその２人が一時的とはいえ協力するなんて、そこに私も混ざるなんて、想像もしていなかった。"

    "緊張を通り越して、私は吐きそうな気分になっていた。"

    "だが、同時に安心もしている。"

    "これが動物的な直感というなら、まさにその通りだ。"

    "アランさんとオデットさん、この二人ほど心強い人は、そういまい。"

    show rnk sci nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「文句はないけど、状況を教えて」"

    show ode noj arm smi with std_change

    voice get_voice_filename("ode")
    odette "「どうってことはない。あたしもこいつも、人からの敵意には敏感ってだけだ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「Ⅸが率先して僕を脱落させたがっていることには、気付いていた。敵の敵は味方――と言っておこうか」"

    show ode noj arm irr with std_change

    voice get_voice_filename("ode")
    odette "「真っ先にフェデリーコのアホを狙ってもいいんだがよ、それじゃつまんねぇ」"

    show ode noj arm smi with std_change

    voice get_voice_filename("ode")
    odette "「だったら、まずは連中の狙ってるⅣのガキ――ユウを先取りしてやった方が面白いだろう」"

    "その話は、私にとって予想をなぞらえるのに等しかった。"

    "彼らが協力する理由など、それ以外にはあり得ないだろう。"

    "オデットさんの言う『連中』の中には、海晴も含まれているはずだ。"

    "それが気になったが、彼女の口振りからして、ユウの脱落までは海晴が狙われることはないだろう。"

    "ユウが脱落した後どうするか――それはまだ分からない。"

    if flags_route_A:


        "できれば早いうちに、海晴と話す必要がある。"

        "海晴と私とが仲間割れしているという前提があるから、スケールさんたちに知られないように十分注意しなければならないけれど。"

    if flags_route_B:


        "もっともその時、私は脱落することが決まっている。"

        "海晴にはお別れを言っておきたかったが――それも叶わないだろう。"

        "海晴なら、きっと全てを悟ってくれる。"



    show rnk sci nor nor with std_change_wait

    "私は、アランさんへと向き直った。"

    "彼はオデットさんが私に条件を出してきたことを知っているのだろうか。"

    show rnk sci arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「どうして、私を？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「君がⅣと何か因縁があるのは知っている。君なら彼の≪未練≫を聞き出せるはずだ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「そういう意味で、僕たちと利害は一致している」"

    "相変わらず、彼の真意は読めない。"

    "私の生き方がどこまで通用するのか――オデットさんとのやり取りを知った上で、見届けるということだろうか。"


    play music audio.badguys

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「さ、御託はいい。ちゃんと用意してるんだろうな？」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「問題ない」"

    hide ode
    hide rnk
    hide aln
    with std_out

    "アランさんはそう言うと、私たちの前にいくつかの頑丈そうなケースを持ってきた。"

    "オデットさんはにやりと笑い、それらを開ける。"

    "中にあったのは――拳銃。"

    "形が違うので種類は違うのだろう。"

    "全部で３丁用意されていた。"

    show ode noj gra smi at std_r with std_in

    voice get_voice_filename("ode")
    odette "「Ｍ500リボルバーにベレッタにトカレフか……。有名どころを揃えてきたもんだ」"

    show ode noj nor tro with std_change

    voice get_voice_filename("ode")
    odette "「おっと、このトカレフは偽物か？」"

    show aln sta nor irr rev at std_l with std_in

    voice get_voice_filename("aln")
    alan "「文句を言うな。３丁でもこの国で武器を仕入れるのは骨が折れた」"

    show rnk sci sur su1 rev at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「これ……全部本物？」"

    show ode noj nor lau with std_change

    voice get_voice_filename("ode")
    odette "「撃ってみるかい？　ここは今、治外法権だ」"

    show rnk sci arm ang rev with std_change

    voice get_voice_filename("rnk")
    rinka "「いやいやいやいや！　そうじゃなくって！」"

    "モデルガンは見たことがあるが、それとそう変わらない見た目だった。"

    "目の前にある拳銃が、人の命を奪うことのできる武器だという実感は湧かない。"

    "それでも無意識に、触ることを避けている自分がいた。"

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「テロ組織と戦うんだぜ？　丸腰でいけると思うか？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「……あくまで自衛用だ。悪いが予備の弾薬はほとんどない。銃撃戦を展開するには心許ない」"

    show ode noj nor gla with std_change

    voice get_voice_filename("ode")
    odette "「ただのボンボンじゃねぇことは分かってたが、てめーは中々面白い経歴を持ってそうだな、社長サマ」"

    show aln sta nor tre rev with std_change

    voice get_voice_filename("aln")
    alan "「……フン」"

    show ode noj arm ser with std_change

    voice get_voice_filename("ode")
    odette "「まあいい。≪ＮＵＬＬ日本支部≫の連中も大した武器は持っていないはずだ。爆弾を手作りするくらいだからな」"

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「あたしはＭ500リボルバーを頂く。ロマンがあるし、嬢ちゃんには扱えないシロモンだ」"

    show rnk sci arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「ち、ちょっと！　『あたし』はってどういうこと？」"

    "３丁ある時点でまさか、と思っていた。"

    "その中からオデットさんは一つを選ぶような発言をした。それって、つまり……。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「ベレッタ92の方が信頼性は高いか。撃ち方はこれから教えよう」"

    show rnk sci arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「いや、いやそうじゃなくって……こんなの持ったら私、犯罪者……」"

    "慌てる私を、オデットさんは目を丸くして見つめてきた。"

    show ode noj nor sur with std_change

    voice get_voice_filename("ode")
    odette "「喜ばねーの？」"

    show rnk sci ang an2 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ねーよ！」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「君に撃てと言っているわけではない。だが牽制用にしても、持っておいた方がいい。相手が丸腰だったら、それだけで優位に立てる」"

    show rnk sci nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「でも……！」"

    show ode noj nor gla with std_change

    voice get_voice_filename("ode")
    odette "「いい加減腹くくれ。あたしらが明日やろうとしてるのは、こういうことだ」"

    "オデットさんは一転して、鋭い眼光を向けてきた。"

    "運命の大広間で見た、今にも獲物を食いちぎろうとする獣の目だ。"

    "私はその目の奥に、ユウのことを思い出した。"

    "炎に包まれる教室。"

    "轟いた爆音。"

    "彼女の言う通り、≪そういうこと≫なのだ。"

    "私の知っている日常ではないところへ、すでに足を踏み入れているのだ。"

    show ode noj gra gla with std_change

    voice get_voice_filename("ode")
    odette "「こいつも言ってるが、別にてめーに人を撃てって言ってるわけじゃねぇ。怖かったら銃弾は抜いておいたっていい」"

    show rnk sci arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「――分かった。大丈夫。代わりに、暴発とかしたら恐いから、ちゃんと教えて」"

    show ode noj arm ser with std_change

    voice get_voice_filename("ode")
    odette "「よく言った。ま、持ってみな」"

    hide rnk
    hide ode
    hide aln
    with std_out

    "オデットさんたちの出身国では法律の下に許可されているかもしれないが、私にとって銃なんて全く無縁なのに。"

    "私は覚悟を見せるため、黒い光沢を見せる拳銃を手にした。"

    "これで立派な、銃刀法違反だ。"

    "想像以上に、重かった。"

    "１キロくらいはあるだろうか。"

    "フィクションの世界ではこれを片手で扱っているシーンをよく見るが、私では片手で銃を固定することはできない。"

    "両手で持ってようやく少しはマシ、といったところだ。"

    "しかしこれが命を奪える重さだと考えると、あまりに軽すぎる。"

    show aln sta nor nor rev at std_l with std_in

    voice get_voice_filename("aln")
    alan "「撃てば、さらに反動がある。君の筋力と体重では、照準どころではないだろうな」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「……フン。あくまで護身用だ。構え方を覚えておけば、牽制程度にはなる」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「使い方は後だ。オデット、先に話を進めてもらおう」"

    show rnk sci que nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「どうやってユウの、組織のテロを止めるかっていう具体的な話……ですね？」"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「ああ――その前に、リンカ、君は僕にも敬語を使わないでいい。あくまで僕たちは対等だ」"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん」"

    "変なところにこだわるな、と思っていた。"

    "だが、彼の提案を否定する理由もない。"


    play music audio.investigation

    show ode noj arm ser at std_r with std_in

    voice get_voice_filename("ode")
    odette "「これから話すのは、あくまでスケールを通じて聞いた話だ。もっとも、ユウの件に関してあたしらを騙す必要はねーだろうから、確実性は高いだろうがな」"

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「まず第一に。連中の目的だ」"

    "テロとは、何か政治的な意志を伝えるために行われるものだと聞いたことがある。"

    "≪ＮＵＬＬ日本支部≫というのはあくまで海外の組織に触発されて結成されたというが、その辺りはまだ知らなかった。"

    show ode noj arm ser with std_change

    voice get_voice_filename("ode")
    odette "「無関心への抵抗――だそうだ」"

    show rnk sci arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「どういう意味？」"

    "私の呟きに答えたのは、アランさんの方だった。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「この国は世界に無関心過ぎる、ということだろう。僕も時々思うことはある」"

    show aln sta nor noe rev with std_change

    voice get_voice_filename("aln")
    alan "「この世界は理不尽で満ちている。戦争、貧困、病気……数えればキリがない」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「日本という安全で裕福なこの国の住民は確かに、そんな世界の理不尽に対して鈍感かもしれない」"

    show ode noj nor tro with std_change

    voice get_voice_filename("ode")
    odette "「そいつは嫉妬、じゃあないのかね。テロを起こしたところで、何も変わりはしねぇよ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「そう思わない連中がいるから、テロが起こるんだろう。僕もテロリストの気持ちにはなれない」"

    show ode noj arm ser with std_change

    voice get_voice_filename("ode")
    odette "「ま、大切なのは――事件を起こせば、自分たちの声を聞いてもらえるって勘違いをしてるってことか」"

    "無関心への抵抗。"

    "私も≪女神の選定≫に関わらなければ、世界に{rb}蔓延{/rb}{rt}はびこ{/rt}る理不尽に対して意識を向けることはなかっただろう。"

    "私自身の死こそ、その理不尽のうちの一つであるのだから。"

    show rnk sci arm ang rev with std_change

    voice get_voice_filename("rnk")
    rinka "「そんなの、勝手だよ」"

    show ode noj arm smi with std_change

    voice get_voice_filename("ode")
    odette "「ああ。だからあたしらも、こっちの勝手な都合で連中の世界への抵抗を止めるわけだ。おあいこだ」"

    show ode noj arm ser with std_change

    voice get_voice_filename("ode")
    odette "「スケールの奴は正義だなんだって言うが、それもあくまであいつの都合に過ぎねぇ」"

    show rnk sci arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「勝手な都合じゃ……。だって、無関係の人たちが巻き込まれるのも防ぐんだから……」"

    show ode noj nor gla with std_change

    voice get_voice_filename("ode")
    odette "「何言ってんだ。さっきも言ったろ。あたしはこの国の人間が何人死のうと知ったこっちゃねぇんだよ」"

    show ode noj gra gla with std_change

    voice get_voice_filename("ode")
    odette "「てめーだって、地球の裏側でテロが起きて何人死のうが、後輩一人死ぬより悲しむことはねーだろ？」"

    show ode noj nor nor with std_change

    voice get_voice_filename("ode")
    odette "「いいんだよ。無関心で。人の器ってのはそこまででかくねぇんだ。手の届くところまでが、そいつの世界なんだからよ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「元より彼らの理想は成立するものではない、というわけだな」"

    show rnk sci arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「ユウも、本当にそのためにテロを起こしたのかな」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「全てに賛同したかどうか分からないが、共感するところはあったのだろうな」"

    show ode noj nor lau with std_change

    voice get_voice_filename("ode")
    odette "「かかっ、それこそリンカ、てめーが聞き出すことじゃねぇか」"

    "そしてオデットさんは、テロ計画の話を続けた。"

    "方法は恐らく、飴茶で使用されたのと同じ爆弾を使った爆破テロ。"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「実行犯の人数は何人だ？」"

    show ode noj arm ser with std_change

    voice get_voice_filename("ode")
    odette "「そこまでは分からねぇそうだが、一人じゃねぇだろうな。明日、何ヵ所かで爆発が起こるって計画だろうよ」"

    show rnk sci arm ang rev with std_change

    voice get_voice_filename("rnk")
    rinka "「嘘っ……」"

    "でっかい花火をあげようとしている――と、さっきオデットさんは言っていた。"

    "彼らの計画が成功すれば、間違いなく大事件だ。"

    "東京タワーのある港区周辺には、皇居や国会議事堂、他にも重要な施設がたくさんあるのだ。"

    "そんな場所でテロが起こるというだけで、日本中から注目が集まるだろう。"

    "スカイツリーができたといっても、まだまだ観光客が多い地域でもある。"

    "観光客が巻き込まれたら、世界から視線が向けられることだろう。そうなれば、彼らのメッセージは世界へ発信される。"

    "もしかしたら彼らはそこまで計算に入れているのかもしれない。"

    show ode noj nor tro with std_change

    voice get_voice_filename("ode")
    odette "「ま、東京タワー以外の爆弾は、日本の警察に任せるしかねーだろうよ」"

    show rnk sci arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ、でもさっき警察は……って……」"

    show ode noj arm irr with std_change

    voice get_voice_filename("ode")
    odette "「それはユウに対しての話だ。ジャーナリストにここまで漏れてるってことは、計画の概要くらいは警察も把握しているはずだ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「元々警備の厳しい地域だ。みすみすテロを起こさせることはしないだろう。普通の人間の対処は、普通の人間がするべきだ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「皮肉なものだが、僕たちは≪死の運命≫に守られている」"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「まさか、周りで起こそうとする爆発は……囮？」"

    show ode noj nor gla with std_change

    voice get_voice_filename("ode")
    odette "「違いねぇ。ユウのことを知ってるのはあたしらだけだ。奴なら変装でもしちまえば、警備を欺くこともできるだろうしな」"

    show rnk sci arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、もし計画がばれてるなら、東京タワーみたいに人の集まるところでは手荷物検査とかがあるはず」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「そこまで近付ければユウの目的は達成したも同然だ。警備を倒して押し通り、自爆すればいいのだからな」"

    "私はアランさんの言葉で、ようやく自分の想像が彼らの話に追いついた。"

    "警備員も格闘技の訓練を積んでいるわけではないだろうから、ユウと戦えば恐らく――負ける。"

    "茂継さんの話を信じるなら、相手が大人の男性数人でも、ユウは負けない。"

    "彼はきっと、後のことは考えてない。"

    "花火は、打ちあがってしまえばあとは消えるだけなのだ。"

    show rnk sci arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「私たちが止めるのは、ユウだけ」"

    show ode noj arm irr with std_change

    voice get_voice_filename("ode")
    odette "「その通り。あとは精々一緒に行動してるヤローくらい、か。東京タワーってとこにあたしは行ったことがないんだが、人が集まるところはどこだ？」"

    show rnk sci nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「一番人が集まるところだったら……展望台だと思う」"

    "東京タワーには、２つの展望台があったと思う。"

    "地上150メートルの大展望台と、地上250メートルの特別展望台だ。"

    "特別展望台の方は追加料金がかかるから、人が多いのは少し低い大展望台の方だろう。"

    "確か展望台へ向かう直前で、手荷物検査もあったはずだ。"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「展望台……フン、象徴的だな」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「高所から広い視野を見下ろしたところで、そこに現実感はない。自分の知っている景色以外に、非日常を感じる――どちらも地続きの現実にもかかわらず」"

    show ode noj nor lau with std_change

    voice get_voice_filename("ode")
    odette "「かかっ、てめーは意外と詩人だねぇ。向いてんじゃねえの、テロリスト」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「まさか」"

    "オデットさんの嫌味に対して、アランさんは気にもしない様子で短く答えた。"

    "東京タワーの展望台で、爆破テロ。"

    "こうして話していても、どうにも現実感がない。"

    "銃の重さを知っても、まだ実感が湧かないくらいなのだから、無理もない。"

    "しかし確実に言えるのは、そんなのはあっちゃいけないこと、ということだ。"

    "きっと、このままでは無関係の人が大勢死ぬ。"

    "子供も大人も日本人も外国人も関係なく、理不尽に死ぬ。"

    "世界への無関心が許せない――その考え方だけならば、理解できなくもない。"

    "だが他人を傷つけてまで理想を主張することに、一片の正しさもない。ありえない。"

    "きっと、理不尽ですらないのだ。"

    "ユウのやったこと――やろうとしたことは全て、ただの暴力だ。"

    "私は無意識に奥歯を強く噛んでいることに気が付いた。"

    "そんなただの暴力に、直未の命は奪われた。"

    "ならば、私の行動は正しさゆえか。"

    "あるいは使命感にかられてか。"

    "どちらでもない。"

    show rnk sci arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「これ以上、誰も傷付けない。そして直未を必ず取り戻す」"

    "私にあるのは、固く結んだ決意だけだった。"


    stop music fadeout 1

    if flags_route_A:


        show aln sta nor lee rev with std_change

        voice get_voice_filename("aln", 202)
        alan "「その覚悟の先、見届けさせてもらう」"

    if flags_route_B:


        show ode noj nor gla with std_change

        voice get_voice_filename("ode", 364)
        odette "「誰も……ねぇ」"




    hide rnk
    hide ode
    hide aln
    with std_out

    "その後、私たちは明日の行動について話しあった。"

    "私は実質オデットさんたちの話を聞いて頷いているだけだったが、具体的になればなるほど、緊張感が増していく。"

    "気になるのは、海晴とスケールさんたちの出方だった。"

    "オデットさんの予想だと、すでに彼女がスケールさんたちとの協力関係を裏切ったことは読んでいるが、大きな問題とは思っていないだろう、とのことだ。"

    "海晴はともかく、スケールさんたちの狙いはあくまでアランさんとオデットさんだ。"

    "結果的に仲間内でユウを指名することができなくても、自分たちのカードが取られるリスクは低いと読んでいるのだろう。"

    "オデットさんやアランさんも、私がユウを指名することを許容しているので、同じ考えのはずだ。"

    "現に私もこれまでのユウを見ているので、同感だ。"

    "最後は私に、かかっている。"

    "私がユウの未練を聞きださなければならないのだ。"

    "不安もあったが、私にしかできないという自負もあった。"

    "――ボクは、君に殺されたい。"

    "私にとっては、呪いの言葉と同じだ。"

    "だが同時にそれが、私が彼の未練を聞き出せるという裏付けでもあった。"






    python:
        set_info_scene("99")
        set_info_time("lnight")
        set_info_location("36")

    stop music fadeout 1
    scene bg warehouse with fade_long
    play music audio.relaxtime
    pause 1

    $ show_hud()

    "ここに来る前にオデットさんに言われた通り、私はこの倉庫で仮眠をとることになった。"

    "銃を持ち運んで見つかれば私は即逮捕だし、移動するにも深夜より早朝の方がリスクが低い、という判断だった。"

    show rnk sci nor apo at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「眠れないな……」"

    "寒くて暗くて、寂しかった。"

    "アランさんの気遣いで毛布は用意されていたが、それでも今まで野宿なんてしたことのない私にとっては過酷な環境だった。"

    "梅雨の時期だから湿気もあり、寝るにはあまりに不快だ。"

    "それでも、明日は早くから行動しないといけないし、眠って体力をつけなければいけない。"

    "目をつぶったまま、毛布を頭から被って唸っていた。"



    show ode noj nor tro rev at std_cl with std_in

    voice get_voice_filename("ode", 365)
    odette "「嬢ちゃん、ちょっとでも寝ておいた方がいいぜ？」"

    show rnk sci sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「心配してくれるんだね。オデットさんも、起きてるし」"

    show ode noj nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「不本意だが、てめーが鍵だからな。あたしは気にすんな。てめーの貧弱で貧相な体とは違ぇ」"

    show rnk sci arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……一言余計なんだけど」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「船の上じゃ、一晩眠れないなんて珍しくねぇ。その分、暇で暇で飽きてもまだ寝るしかねー時もあるんだけどよ」"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……船？」"

    "聞き返したところで、私は自分が彼女に興味を持っていることに気がついた。"

    "恐怖の対象でしかなかったのに、少し話しただけでこんなに変わっている。"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「おっ、あたしの情報を探ろうって算段かい？」"

    show rnk sci sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「い、いや違っ……」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「分かってるよ。てめーは馬鹿ではないが、そこまで賢{rt}さか{/rt}しくもねぇ。海晴ってのとはそこが違うわな」"

    "私が目を逸らすと、オデットさんは続けた。"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「こう見えて、あたしは船乗りだった」"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……むしろ納得なんだけど」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「いわゆる海運業者だ。ただし……手紙から違法の品物まで、気に入りゃ何でも依頼を受ける運び屋さ」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「武器とか密造酒とか、ま、たくさん運んださ。それこそ人も……な」"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「ただし麻薬だけは駄目だ。あれは流儀に反する。麻薬の運びの依頼をしてきた奴の大半は、かかっ、海に沈めたよ」"

    show rnk sci arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「海に沈めたってそれ、比喩だよね」"

    "オデットさんはまた、からからと笑った。"

    "彼女の仕事の話は、それこそ、私にとっては現実感のないものだった。"

    "日常という言葉でも、彼女と私だったら意味が全く違うのだろう。"

    "そういう意味では、私は広い意味で、自分以外の日常に対して無関心だった。"

    show ode noj nor gla rev with std_change

    voice get_voice_filename("ode")
    odette "「しっかし、あの坊ちゃんはよく寝るねぇ。宝石会社の社長様にしちゃ、荒事に慣れてるようだ」"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「奴の人生も中々、面白いだろうよ。かかっ、会ってみないと分からないもんだ」"

    show ode noj arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「さ、話は終わりだ。ちったぁ緊張もほぐれたろ。こんな場所じゃ、朝日が差したらすぐ目覚めちまうんだから、せめて目をつぶってろ」"

    show rnk sci arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「…………うん」"

    "私は、ますますこの人のことが分からなくなっていた。"

    "仕事でも違法なことをやっていたとはいうが、麻薬は運ばないという流儀がある。"

    "眠れない私に、気を遣ってくれる。"

    "今まで出会った誰とも違う、本当に読めない人だった。"

    "でも、ふと思う。"

    "同じ人なんていないんだから、きっと、それで当たり前なのだ。"

    "私たちはきっと、他人のことを全然知らないだけ。"

    "牛塚さんの孫として、好奇心旺盛だったユウ。"

    "オデットさんから聞いた、テロ組織の一員としてのユウ。"

    "そして直未を殺し、私に殺されたがっているユウ。"

    "そのどれが彼の本当の姿かも、私はまだ知らないのだ。"

    "真実の彼を知ったとき、きっと≪未練≫も知ることになる。"

    "そんなことを考えながら目をつぶっていると、徐々に体力の限界が近付いてきた。"

    "私は、まどろみの中に落ちていく。"

    if flags_route_A:
        $ add_seen_chapter("7_2-1")
    elif flags_route_B:
        $ add_seen_chapter("7_3-1")










    python:
        set_info_scene("100")
        set_info_date(6, 16, "sat")
        set_info_time("morning")
        set_info_location("02")


    stop music fadeout 2
    scene bg station01 with fade_longest
    play music audio.impatience
    pause 1

    $ show_hud()

    "小熊真央は、電車を待ちながらスマートフォンでＳＮＳを眺めていた。"

    "そこに流れてきたのは、心がざわつく緊急ニュースだった。"

    show mao sci nor ser at std_c with std_in

    voice get_voice_filename("mao")
    mao "「……まじ？」"

    "真央はすぐに、画面をニュースサイトに切り替えた。"

    "このニュースは、元の記事を確認しなければならないと、そう思ったからだ。"

    show mao sci nor ser with std_change

    voice get_voice_filename("mao")
    mao "「東京メトロ神谷町駅の周辺で、不審物の入ったリュックが複数発見された……これって、なおりんに関係して……」"

    show mao sci sel lau with std_change

    voice get_voice_filename("mao")
    mao "「不審物って、爆弾……じゃあ、犯人捕まった？」"

    "神谷町という駅に馴染みはなかったが、近くに東京タワーがあるということを、真央は知っていた。"

    "隣駅の霞が関は官公庁街であり、反対方面は六本木と、日本にとって重要な施設が集まっていることも、知識としては持っている。"

    show mao sci nor ser with std_change

    voice get_voice_filename("mao")
    mao "「これってぇ……テロが起こりそうだったってことぉ？」"

    "そんな場所で爆破テロが起きたら、場合によっては日本中が混乱するかもしれない。"

    "芸能ニュース以外にあまり興味のない真央だが、その危険性は分かっていた。"

    show mao sci nor ser with std_change

    voice get_voice_filename("mao")
    mao "「えっ……、犯人捕まってない……」"

    "記事をよく見ると、見つかったのはあくまでリュックだけ。"

    show mao sci nor ch1 with std_change

    voice get_voice_filename("mao")
    mao "「しかも、うちの学校のことも書いてあるし」"

    "飴茶高校での爆発は、この頃にはすっかり爆破テロとして認知されていた。"

    "あの規模の爆発を、死者まで出ているのに、事故と報道するのは元々無理があったのだ。"

    "あの事件からまだ１週間という短い期間で爆弾が見つかったのだから、≪飴茶女子高校爆破テロ事件≫との関連性が疑われない方がおかしい。"

    show mao sci nor sad with std_change

    voice get_voice_filename("mao")
    mao "「でも、犯人が捕まる日も遠くないってことだよねぇ……じゃないと、なおりんも……」"

    show mao sci nor ser with std_change

    voice get_voice_filename("mao")
    mao "「りーたんもみはるんもこのニュース見たかな？　教えてあげないと」"

    "真央はチャットアプリを起動して、３人のグループに送ってみた。元々は直未も入れた４人のグループだった、その場所に。"

    show mao sci sel irr with std_change

    voice get_voice_filename("mao")
    mao "「あーもう、こういう時に限って二人ともスマホ見てないしぃ！」"

    "真央の言葉通り、真央のメッセージはしばらく待っても既読にはならなかった。"

    "彼女はこの事件が他人事だとは思えなかったのだ。"

    "このニュースだけは、自分たちが誰よりも詳しく知っていなければならないと、真央はそう思っていた。"











    python:
        set_info_scene("101")
        set_info_location("37")

    stop music fadeout 2
    scene bg tokyotower01 with fade_longest
    pause 1

    $ show_hud()

    "東京タワー。"

    "日本で最も有名な建造物のうちの一つだ。"

    "高さでは634メートルのスカイツリーに負けているが、それでもビル街にそびえたつ333メートルの真っ赤な塔の姿は圧巻だ。"

    "有料の展望台は地上250メートルの位置にあり、東京の街を一望できる。"

    "あまりに高いところから見下ろす街並みは、地上から見るのとは全くの別物。"

    "現実感すらなく、本当に別の世界のように錯覚する。"

    "多くの人々は、そこに楽しさを覚えるのだ。"

    "だが、ここに一人、全く反対の感情を持っている者がいた。"

    "高所から街を見下ろして、別世界を感じるという行為はまさに、自分と世界との隔たりを大きくしていると。"

    "景色に心を躍らせている場合ではなく、危機感を覚えるべきだと。"

    "強く信じる者が、ここに。"


    play music audio.investigation

    show yuu awa nor no2 at std_c with std_in

    voice get_voice_filename("yuu")
    yuu "「……腹が立つよ」"

    "山手線での自爆テロで命を落とすはずだった少年――ユウだ。"

    "この世界に警鐘を鳴らさなくてはならないという使命感だけではなく、今の彼には苛立ちという感情もあった。"

    "自分でも制御し切れない、心。"

    "それがはっきりと芽生えた瞬間は、彼の胸に刻まれていた。"

    show yuu awa war sa2 with std_change

    voice get_voice_filename("yuu")
    yuu "「苦しいよ」"

    "だからこそ、彼の胸は痛むのだ。"

    "彼は組織から支給されたスマートフォンで、ニュースをチェックしていた。"

    "この周辺で、爆弾入りのリュックが複数見つかったという。"

    "現在、リュックを置いた人物について調査中。"

    "爆弾は≪飴茶女子高校爆破テロ事件≫で使用されたものと同型で、関連性が疑われている――と。"

    show yuu awa nor no2 with std_change

    voice get_voice_filename("yuu")
    yuu "「……順調だね」"

    "周辺の警備が強く、意識がそちらに向けば向くほど、ユウへの注意は薄れる。"

    "そもそも、この国では子供が爆破テロを起こすと思っている者などほとんどいないと、彼は知っていた。"

    "別世界のことだと、ニュースで見ていても、まさか自分の周辺で起こるはずがないと。"

    show yuu awa war sa2 with std_change

    voice get_voice_filename("yuu")
    yuu "「…………ボクは」"

    "ユウは、体の前で抱えたリュックを強く抱き締めた。"

    "かつて、山手線での爆破テロ計画で使用する予定だったものだ。"

    "鍵のチャームのついたそれは、ユウが自分で選んだものだった。"

    "ただし中には、あの時よりもさらに威力を増大させた爆弾が入っている。"

    "ユウの組織の一員――それを仲間と呼ぶか彼は判断しかねていた――が、組織の未来が絶望的でもはや手詰まりであるならばと、もてる技術と知識を尽くして改良した。"

    "この爆弾が爆発しても、ユウが死ぬことはない。"

    "東京タワーという象徴的な場所で、大勢の一般人を殺す。"

    "その中で、ユウだけが生き残る。"

    "死して英雄になれないのは残念だったが、この事実は世界に衝撃を与えるだろう。"

    "もっとも、それはユウの本当の目的ではなかった。"

    show yuu awa nor no2 with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクは止まれない。なら、止めてみせろ」"

    "そして、自分を殺せ。"

    "ユウの言葉は誰にも聞こえはしないけれど、たった一人に向けられている。"

    show yuu awa nor no2 with std_change

    voice get_voice_filename("yuu")
    yuu "「そろそろ行こう」"

    hide yuu with std_out

    "ユウは、展望台のチケットを買うために売り場に並び、つつがなく購入した。"

    "独りでいるのは珍しいけれど、かと言って不審に思われるほどではない。"

    "彼はあくまで、子供なのだ。"

    "受付の女性も、彼のリュックの中に爆弾が入っているなど想像だにしていなかった。"

    show yuu awa war wa2 at std_c with std_in

    voice get_voice_filename("yuu")
    yuu "「次は……」"

    "ユウは、荷物検査のスタッフに目を向けた。"

    "展望台へ向かう方法は２つ。"

    "一つは非常階段で、一つはエレベーターだ。"

    "非常階段は日中開放されていて、一般人でも利用することができる。"

    "展望台までは、15分程度で上りきることができるそうだ。"

    "ユウが爆破で多くの人を巻き込むためには、その両方を使用不可能にする必要があった。"

    "そのために、彼は独りであれはすれど、一人ではない。"

    "すでに作戦は進行している。"

    show yuu awa nor no2 with std_change

    voice get_voice_filename("yuu")
    yuu "「いよいよだ」"

    hide yuu with std_out

    "ユウの無表情は、少しの真剣さを帯びた。"

    "獣のように、瞳孔が開く。"

    "荷物検査の列に並ぶ。前にはユウよりもさらに小さい子供を連れた親子連れ。"

    "怪しまれるので振り返りはしなかったが、横目で見る限り後ろにいたのは自分と同い年くらいであろう少女だった。"

    "リンカも身長だけなら自分と同い年くらいに見えるから一概には言えないか、とユウは認識をあらためた。"

    "もっとも、前後にⅪの女性のような規格外の人間がいなければ、ユウにとっては誰であろうと同じだった。"

    "前の親子が荷物検査を問題なく通過する。"

    "次が、ユウの番だ。"





    "至近距離で荷物検査のスタッフを目にしたとき、ユウは反射的に動いていた。"


    play music audio.kinpaku

    show yuu awa eml wa2 at std_cr with std_in

    voice get_voice_filename("yuu")
    yuu "「……はっ」"


    play se "g17_close"
    show yuu awa bat con with std_change_wait

    "ユウは上着の内側に隠していた拳銃を取り出す。"

    "グロック19。"

    "取り回しのいいコンパクトサイズのハンドピストルだ。"

    "彼の右手に握られたそれは、モデルガンではない。"

    show aln hen nor nor rev at std_l with std_in


    voice get_voice_filename("aln", 203)
    alan_staff "「何っ……！」"


    voice get_voice_filename("yuu")
    yuu "「やっぱりね」"

    play se ["g17_shot", "g17_shot", "g17_shot"]
    with quake_long

    "ユウはそのまま拳銃に左手を添え、オートマチックの３連射をスタッフの腹部に撃ち込んだ。"

    "銃声は、フィクションの世界で聞くよりもずっと乾いていた。"

    "頭部を狙わなかったのは、荷物検査スタッフが選定の参加者だと気付いたからだ。"

    "彼を殺そうとすれば、運命が邪魔をするとユウは知っていたのだ。"


    show yuu awa bat non with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクを邪魔しに来たんだね」"

    show aln hen nor pai rev with std_change

    voice get_voice_filename("aln")
    alan "「ぐっ……」"

    "荷物検査スタッフに扮していたのは、Ⅻの位置に立っていた男性、アラン・スコーピオンであった。"

    "彼はユウの攻撃への反応が僅かに遅れたために、床にうずくまることとなった。"

    "真っ赤な液体が、床に広がった。"

    "どんなに強い肉体でも、銃弾より硬い皮膚はない。"

    "至近距離からの射撃ゆえ威力は低いが、動きを封じるには十分以上だった。"

    scene ecg hostage normal with dissolve_long

    "ユウはアランを見下ろすこともなく、自分の後ろにいた少女の腕をつかみ引き寄せると、頭に拳銃をつきつけた。"


    voice get_voice_filename("yuu")
    yuu "「これは、人質だ」"



    voice get_voice_filename("rnk")
    rinka_unk1 "「きゃっ……」"


    voice get_voice_filename("yuu")
    yuu "「エレベーターを止めたならば、こいつを殺すよ」"

    "選定の参加者でなければ、ユウは殺すことを躊躇わない。"

    "近くにいた他の客の中に、無謀な勇ましさを持つ者はいなかった。"

    "突然の銃声と、撃たれ怪我を負った男性の前では、足がすくまない者はいない。"

    "ただその場から動かず、怪我をしたアランに駆け寄る人もなく、悲鳴が上がるだけだった。"

    "騒ぎを聞きつけたスタッフと野次馬が集まる頃には、エントランスはパニック状態になっていた。"

    "こうなるともう、統制がとれない。"


    scene bg tokyotower01
    show aln hen nor pai rev at std_cl
    with dissolve_long


    voice get_voice_filename("aln")
    alan "「待……て……」"

    "常人ならば失神してしまうほどの痛みであろう。"

    "それでもアランは、ユウを見据えていた。"

    "結果的には、コンマ単位での判断が状況を分けたのだ。"

    "少女を人質に取ったまま、ユウはスマートフォンを取り出した。"

    "爆破テロを行うにあたり、彼というよりは彼らの、大きな目的を遂行するためだった。"


    stop music fadeout 1
    scene ecg hostage normal with dissolve_long


    voice get_voice_filename("yuu")
    yuu "「……これだね」"

    "ユウが起動したのは、リアルタイムで動画を配信できるアプリだった。"

    "無名の配信者であるユウだが、今から行う配信はＳＮＳなどで即、拡散されるという確信があった。"


    voice get_voice_filename("yuu")
    yuu "「……こうかな」"

    "一度練習してはいたが、すぐに慣れるものではない。"

    "カメラを自分の方に向け、自分がフレーム内に入る位置に調整をする。"

    "騒ぎを後目に、ユウはいくつかの入力を終え、配信を開始する。"

    "タイトルは組織の者と事前に決めた、『自爆テロ生中継』というストレートなものだった。"

    "つたない日本語だが、ユウはカードブックの力に頼らない自分の言葉で話し始めた。"


    play music audio.resistance
    scene ecg hostage broadcast with dissolve


    voice get_voice_filename("yuu")
    yuu "「ボクは今から、ここ、東京タワーで自爆テロを行う」"

    "突飛なタイトルのおかげで、視聴者はすぐに食いついたようだ。"

    "だが、コメントは荒らしのコメントで埋まる。"

    "『自演はやめろ』や『話題作り乙』などである。"

    "『これだから子供にネットを与えちゃだめなんだ』や『新手の炎上マーケティング？』などコメントは多種多様。"

    "視聴者数は一時的に増えたが、これらのコメントを目にした視聴者が去っていったのだろう。"

    "視聴者は爆発的には増えなかった。"

    "もっともユウは、それらのコメントは一切読んでいない。"


    voice get_voice_filename("yuu")
    yuu "「人質はとったよ。この銃も本物だ。そっちに、撃たれた人がいる」"



    voice get_voice_filename("rnk")
    rinka_unk1 "「きゃっ……」"

    "それでも、どういう反応になるか大体の予想はついていた。"

    "だてに、牛塚邸でテレビばかり見ていたわけではない。"

    "操作に慣れていないせいで、何度かフレームから外したが、彼は画面に負傷したアランを映した。"


    voice get_voice_filename("yuu")
    yuu "「嘘だと思っても、いいよ。だって、ボクはそういう人たちにこそ知らせたいんだ」"


    voice get_voice_filename("yuu")
    yuu "「これは、無関心への抵抗。残酷な世界からの警告だよ」"

    "ユウは間を開けながら話していた。"

    "銃や怪我人を映したことで、この放送が嘘ではないことが伝わると予想したからだ。"

    "まだ信じない人もいるだろうけれど、信じて拡散する人もいる。"

    "あるいは、この現場から見ている人もいるだろう。"

    "大衆がユウの配信を本物だと信じ始めた証拠に、視聴者数は伸び始めていた。"

    "配信が始まったばかりで運営は把握していないだろうし、もし運営がこの配信を見ても、迂闊に止めることはできないだろうと彼は思っていた。"


    voice get_voice_filename("yuu")
    yuu "「薄々気付いている人もいるかもしれないけれど、はっきり言うね」"


    voice get_voice_filename("yuu")
    yuu "「あの高校……私立飴茶女子高校で爆破テロを起こしたのは、ボクだ」"


    voice get_voice_filename("yuu")
    yuu "「ボクがあの事件の犯人だ。つまり――罪もないあの少女を殺したのはボクだよ」"


    voice get_voice_filename("yuu")
    yuu "「もっとも、罪がないっていうのは君たちの意見だ」"


    voice get_voice_filename("yuu")
    yuu "「ボクからすれば、世界に対して興味がなかった時点で罪なんだ。テレビやネットでニュースを見ている？　そんなものは、興味のうちには入らないよ」"


    voice get_voice_filename("yuu")
    yuu "「少し、ボクの話をしようか」"

    "ユウは声のトーンを少しだけ落とした。"













    python:
        set_info_scene("102")
        set_info_time("morning")
        set_info_location("02")


    stop music fadeout 2
    scene bg station01 with fade_longest
    play music audio.gimon
    pause 1

    $ show_hud()

    show mao sci nor que at std_c with std_in

    voice get_voice_filename("mao")
    mao "「何これ……ホントに日本……？」"

    "真央は、ネットの動画配信を見ながらそう呟いていた。"

    "さっき、爆弾の入ったリュックが発見されたというニュースを見た直後のことだから、余計に驚いた。"

    "少年が人質をとり、拳銃を持っている。"

    "すでに一人が撃たれ、負傷している。"

    "これからこの少年は展望台に上がり、爆破テロを行うという。"

    "真央の知っている日本での出来事とは信じられなかったのだ。"

    "そしてこの少年は、真央のようにこの事件が現実だとすぐには受け入れられない人々に対して抵抗しているのだと語っていた。"

    "だが真央は、自分を全くの無関係な他人とは思っていなかった。"

    show mao sci nor sad with std_change

    voice get_voice_filename("mao")
    mao "「この子が……犯人……？」"

    "彼は自らを≪飴茶女子高校爆破テロ事件≫の犯人だと名乗った。"

    "真央にとって、彼は直未を殺した当事者だった。"

    "自分の先輩と後輩という関係を超え、直未は真央の友達でもあった。"



    voice get_voice_filename("yuu")
    yuu "『少し、ボクの話をしようか』"

    "真央だけでなく、日本中で大勢の人が注目する中、少年は画面越しにそう切り出した。"

    "真央は、聞かないわけにはいかなかった。"








    scene ecg hostage broadcast with dissolve_long


    voice get_voice_filename("yuu")
    yuu "「ボクは、この国とは対照的な場所で生まれた。安全なんて保証されていない、国だよ。日本の人は、名前すら知らないだろうね」"


    voice get_voice_filename("yuu")
    yuu "「父親はボクが生まれる前に、母親は、ボクが生まれてすぐ死んだらしい。生まれてから、ボクは独りで生きてきた」"


    voice get_voice_filename("yuu")
    yuu "「そんなボクが生きることができたのは、とある施設に引き取られたからだった」"

    "それは、病院と併設された児童養護施設だと語る。"

    "ユウと同じように、大勢の身寄りのない子供たちがたくさんいたそうだ。"


    voice get_voice_filename("yuu")
    yuu "「大人たちの中に、ママと呼ばれる日本人の女の人がいた。ママは昼間は医者として働き、それ以外の時間はボクたちのいた施設で働いていた」"

    "その女性はさらに、医者を増やそうと教育も行っていたらしい。"

    "負傷者も多く、衛生環境も悪い紛争地域において、患者に対して医者の数は圧倒的に不足していた。"

    "さらに、時間の許す限り子供たちの面倒も見ていたという。"


    voice get_voice_filename("yuu")
    yuu "「ボクたち孤児は、ママがいるから生きることができた。たまには、料理も作ってくれたよ」"


    voice get_voice_filename("yuu")
    yuu "「その時期ボクは、母親がいるというのはこういうことなんだ、と思っていた」"


    voice get_voice_filename("yuu")
    yuu "「でも、ママ一人じゃ限界がある。体も心も――そして、お金も」"

    "医療には資金が必要だ。"

    "薬代や器具代、人件費や消耗品など数え上げればキリがない。"

    "施設の運営にもお金は必要だ。"

    "生きるために最低限必要な衣食住だけでも、莫大な金額が必要だ。"

    "増えていく患者と孤児。"

    "病院や施設を運営するためのお金は、常に不足していた。"


    voice get_voice_filename("yuu")
    yuu "「ママは自分の故郷――日本に助けを求めたよ。もちろん、国からはお金はもらえない」"

    "紛争地域を支援する非営利団体の補助金もあったが、それでも必要経費の足しにしかならない。"

    "彼らの施設だけに資金援助をしているわけではないのだ。"

    "無限の財源など、この世のどこにもない。"


    voice get_voice_filename("yuu")
    yuu "「だから、民間人……キミたちに支援を求めたんだ。インターネットを使って、寄付を募った」"


    voice get_voice_filename("yuu")
    yuu "「結果はもう、分かるよね？」"


    voice get_voice_filename("yuu")
    yuu "「集まったのは微々たる金額。ママはついに、過労で死んでしまった」"

    "彼らにとって、それは母親を亡くしたのと同じ重みがあった。"

    "施設にとって、それは柱を失ったのと同じ重みがあった。"


    voice get_voice_filename("yuu")
    yuu "「ママはこんな風に言ってたっけ。『きっと大丈夫。日本人はいい人たちばかりだから、きっと助けてくれる。離れていても、同じ故郷を持っているんだから』って」"

    "その言葉は、遠く離れた場所で頑張る同胞のことを想うことができるという意味だった。"

    "日本人のことを、信じていた。"


    voice get_voice_filename("yuu")
    yuu "「ママが言うんだからって、ボクも信じてたよ」"


    voice get_voice_filename("yuu")
    yuu "「でも、嘘だった」"


    voice get_voice_filename("yuu")
    yuu "「ボクたちの国だけじゃない。同じ日本人のママに対しても、君たちは無関心だった」"

    "ユウは淡々と、ここまでの話を語った。"











    play music audio.growapart
    scene bg station01
    show mao sci nor sad at std_c
    with dissolve_long


    voice get_voice_filename("mao")
    mao "「こんなの……」"

    "真央は、うまく言葉を出すことができなかった。"

    "少年の年齢から考えて、真央も生まれている時期のことだった。"

    "紛争地域で活動していた日本人女性がいたことも、医療従事者を増やそうとしていたことも、彼女は何も知らなかったのだ。"

    "同じ日本人が引き合いに出されたのが、決定的だった。"

    show mao sci nor sad with std_change

    voice get_voice_filename("mao")
    mao "「だって……」"

    "直未を殺したこの少年への恨みがあった。"

    "怒りがあった。"

    "だが、自分自身もまた、その怒りの矛先なのだとようやく分かった。"

    "年齢は関係ない。"

    "多くの無関心が、その女性を殺したのだ。"

    "だから直未を殺していいなんて理屈にはならない。"

    "けれども、真央はこの少年へ反論できる言葉を持ち合わせていなかった。"












    python:
        set_info_scene("103")
        set_info_location("37")


    stop music fadeout 2
    scene ecg hostage normal with fade_longest
    play music audio.resistance
    pause 1

    $ show_hud()

    "この場にいる誰もが、ユウの話に聞き入っていた。"


    voice get_voice_filename("yuu")
    yuu "「その後、ボクは傭兵となった。傭兵と言っても、使い捨ての少年兵だよ」"


    voice get_voice_filename("yuu")
    yuu "「≪敵≫なら誰でも倒したよ。ボクは戦う才能が――銃を扱う射手の才能があった」"


    voice get_voice_filename("yuu")
    yuu "「そうするしかなかった。そうできちゃったから」"

    "彼にとって、生き残り続けたことは幸せではなかったのかもしれない。"

    "戦場で生き残るということは、より多くの他人を殺すことでもある。"

    "母親の代わりだったママから、彼は人間らしさも教わっていたはずだったのに。"

    "人の命を奪うことに慣れるため、心を摩耗させていった。"

    "わずかに残った心は、蓋を閉じて隠してしまったのだ。"

    "壊れてしまわないように。"

    "代わりに、彼は別の生きる意味を見つける。"


    voice get_voice_filename("yuu")
    yuu "「英雄になれ――ボクはそう教えられてきた」"

    "人はその死に様で英雄になるのだと、ユウは教えられたことを話した。"

    "自らの主義や主張に対し、自らの死を捧げる。"

    "死をもって伝えれば、覆されることもない。"

    "人間にとって最も大切なものを守ったまま死ぬことこそが、英雄になることなのだと。"


    voice get_voice_filename("yuu")
    yuu "「ママは死んだからこそボクの中で英雄になったんだって、ボクは気付いた。ママは信念を守ったんだよ」"


    voice get_voice_filename("yuu")
    yuu "「だからボクも英雄になりたかった」"


    voice get_voice_filename("yuu")
    yuu "「やがてボクは、≪ＮＵＬＬ日本支部≫へと流れてきた。彼らの幹部が日本に来たとき、ボクは自分の過去を少しだけ話す機会があったからね」"


    voice get_voice_filename("yuu")
    yuu "「無関心への抵抗――ボクには難しかったけど、しっくりきたよ」"


    voice get_voice_filename("yuu")
    yuu "「世界への復讐を果たして、ボクは英雄になるよ」"

    "ユウはそう言うと、人質をエレベーターまで誘導した。"


    voice get_voice_filename("yuu")
    yuu "「今頃、ボクの仲間が展望台を占拠しているはずだ。非常階段から行こうとしても無駄だよ。そこにも、ボクの仲間がいるから」"

    "彼は冷たい声で言い残し、エレベーターへと向かう。"

    "スマホでは、エレベーターの内部を映していた。"

    "エレベーターの扉が閉まる直前に見せた、悲しげな表情が映らないように。"







    stop music fadeout 1
    scene black with dissolve_long



    voice get_voice_filename("rnk")
    rinka_unk1 "「……すっ……ぐすっ……」"

    "エレベーターに乗っている間、人質にされた少女はずっとすすり泣いていた。"

    "下を向き、震えたままで。"

    "ユウは彼女に、何の同情も覚えていなかった。"

    "どうせこの人質も、間もなく死ぬのだ。"

    "ひとつ感情が向いているとすれば、鬱陶しく騒ぐことがないから楽、という程度だった。"

    "エレベーターは、わずか１分程度で展望台まで到達する。"

    "上りきるまでの間、ユウは自らが語った過去を思い出していた。"

    "自分の生い立ちを聞き、感傷的になっている人がいるのかと思うと、苛立ちが止められなかった。"

    "この国のどこに、自分と同じ貧困を味わった者がいるのだろうか？"

    "わずかに関心を向けただけで自分は無関心ではない、人とは違うと勘違いをしている人間を、彼は嫌っていた。"

    "行動を起こさなければ、結果を残さなければ、意味がない。"

    "天に昇っていくエレベーターは、間もなく、その終着点へ到達する。"







    $ set_info_location("38")

    scene bg tokyotower02 with dissolve

    "エレベーターの回数表示が、展望台を示した。"

    "アナウンスの音声が流れた直後、ドアが開く。"

    show yuu awa war wa2 at std_r with std_in

    voice get_voice_filename("yuu")
    yuu "「どういうつもり？」"

    "エレベーターを出てユウが一番初めに見たものは、銃口だった。"

    "人間離れした体格の女性が、大口径のリボルバー式拳銃を向けていたのだ。"

    "ユウも拳を交えたことのある、Ⅺの女性。"


    play music audio.kinpaku

    show ode noj arm ser rev at std_l with std_in


    voice get_voice_filename("ode")
    odette_num "「ごっこ遊びはおしまいだ」"

    play se "44mag_shot"
    with quake_normal

    "彼女の手から、銃声が響く。"

    "仲間が待っているのだと、この時はさすがのユウも油断していた。"

    "緊急連絡も入っていなかったのだ。"

    "だから、一発目の銃声が響いたとき、ユウは棒立ちのままだった。"

    "だが、ユウは無傷のまま立っている。"

    "彼女が狙ったのはユウではなく、配信に使っていたスマートフォンだった。"

    "配線を飛び散らせながら、スマートフォンはエレベーターの中へ押し込まれた。"

    "ユウはすぐさま、さきほどアランを撃った自動拳銃を取り出す。"



    play se "g17_close"

    show yuu awa bat non with std_change

    voice get_voice_filename("yuu")
    yuu "「人質を……」"

    scene ecg claimerrinka henso with dissolve_long



    voice get_voice_filename("rnk")
    rinka_unk1 "「ああああああああっ！」"

    "聞いたことのある声が、自分の脇から響いていた。"

    "声の主は懐から自動拳銃を取り出すと、撃つのではなく、ユウが拳銃を取り出した手に向かって殴りかかってきた。"




    voice get_voice_filename("yuu")
    yuu "「……遅い」"

    "ユウはリュックをかばいながら、少女の攻撃を避ける。"

    "少女は振り下ろした両手で宙を切り、そのまま前傾姿勢をとった。"

    "頭から、黒い物体がずぞりと床へ落ちた。"

    "その下から、金髪混じりの黒髪が姿を見せる。"

    scene bg tokyotower02
    show rnk sci arm imp rev at std_c
    show yuu awa war cl2 at std_r
    with dissolve_long


    voice get_voice_filename("yuu")
    yuu "「お前は……」"

    hide rnk
    hide yuu
    with std_out

    "――獅子舞凛火。"

    "自分が人質にとったのは変装した凛火だと、ユウは気付いた。"

    "動きを鈍らせることもなく、ユウは反射的に凛火へ攻撃を加えようとした。"

    "だが、エレベーターの出口という閉鎖的な場所で２人を相手取るのは無謀だった。"

    "オデットはユウの服をつかみ、自分の方へ思い切り引き寄せた。"

    play se "g17_shot"
    with quake_fast

    "ユウが凛火へ向かって放った弾丸は、明後日の方向へ飛んでいき、エレベーターの天井へ突き刺さる。"

    play se ["44mag_shot", "44mag_shot"]
    with quake_normal

    "オデットは拳銃で、ユウの背中を狙った。"

    "正確には、背中とリュックの間。"

    "２発の弾丸が、リュックの肩ベルトに命中する。"

    show rnk sci arm ang at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「ちょっと！」"

    "一歩間違えば、爆弾に当たる距離だった。"

    "≪女神の選定≫の参加者なので運命に守られているとはいえ、この至近距離で爆風を浴びれば大怪我だ。"

    "だが、オデットはリュック本体に当てることはなく、見事ユウとリュックとを切り離した。"

    show yuu awa eml su2 at std_r with std_in

    voice get_voice_filename("yuu")
    yuu "「くっ……」"

    scene ecg odettobt fun with dissolve_long


    voice get_voice_filename("ode")
    odette "「かかっ！」"

    "爆弾の威力を知っているがゆえの行動だった。"

    "ユウは、今にも落下しそうなリュックへ意識を向けていた。"

    "自分が怪我をするのはまだいい。"

    "しかし今爆発したら、一般人を巻き込むことができないと思っていた。"

    "この判断が、オデットと違っていたのだ。"

    play se "punch01"
    with quake_fast

    "彼女は床を見たユウの背中を、思い切り蹴飛ばした。"

    "ユウの倍近く体重があるオデットの蹴りを受け、彼は文字通り体を浮かせた。"

    "オデットは満足そうににかっと笑う。"

    "爆弾の入ったリュックには、目を向けることもなく。"

    scene ecg claimerrinka normal with dissolve


    voice get_voice_filename("rnk")
    rinka "「あぶなぁあああいっ！」"

    "凛火は手に持っていた拳銃を投げ捨てて、リュックへ向かって飛んでいた。"

    "ヘッドスライディングの格好に近い。"

    "リュックが床と激突すれば、衝撃で爆発するだろう。"

    "凛火はその時無心で、リュックへと向かう。"

    play se "taoreru08"
    with quake_fast


    voice get_voice_filename("rnk")
    rinka "「ぐあっ」"


    scene bg tokyotower02 with dissolve_long

    "地面すれすれのところで、凛火は左右からはっしとつかみリュックを受け止めた。"

    "爆弾が作動しなかった代わりに、凛火は床で顔面をすりおろすような痛みを覚えていた。"

    show yuu awa eml cl2 at std_r with std_in

    voice get_voice_filename("yuu")
    yuu "「……どうしてっ！」"

    "目的達成の直前で、ユウは爆弾を奪取されてしまった。"

    "湧き上る感情に任せて、ユウはただその疑問を叫ぶことしかできなかった。"

    hide yuu with std_out









    python:
        set_info_scene("104")
        set_info_time("morning")
        set_info_location("38")

    "きっと、人生で一番ひやっとした瞬間だった。"

    "目の前で、爆弾入りのリュックが落下しようとしていたのだ。"

    "爆発すれば、私は爆風を顔面で受け止めることとなる。"

    "なかったことになっている記憶の中で、私は爆弾の威力を知っている。"

    "女神の運命に守られて死なないだけで、どんな大火傷をするか想像もつかない。"

    "顔なんて、原形を残すことはないだろう。"

    "そんな危機一髪の状況の第一段階目を、私はリュックを受け止めたことで切り抜けたと言っていいだろう。"

    show rnk sci ang an2 at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「爆弾、無視すんなよ！」"

    show ode noj nor lau rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「いやぁ、嬢ちゃんが分かってくれて助かった。仕方ねぇだろ。このガキを出し抜くには、虚をつくしかなかったんだ」"

    hide rnk with std_out

    "こんな状況なのに、いや、こんな状況だからこそ、彼女は笑っていた。"

    "概ね、彼女と申し合わせた通りだと言っていいだろう。"

    show yuu awa eml cl2 at std_r with std_in

    voice get_voice_filename("yuu")
    yuu "「どうして、誰もいないの？」"

    "展望台には一般客も、ユウの仲間も誰もいない。"

    "いるのはただオデットさんと私と、ユウだけだ。"

    show ode noj nor tro rev with std_change

    voice get_voice_filename("ode")
    odette "「んー、あー、のした。てめーみたいのを期待したが、残念ながら素人同然で歯ごたえがなかった」"

    show yuu awa war war with std_change

    voice get_voice_filename("yuu")
    yuu "「……10人はいたはずだよ」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「てめーが３人だったら詰んでたわな。だが、雑魚なら何人集めても大した問題にはならねぇ」"

    show yuu awa nor qu2 with std_change

    voice get_voice_filename("yuu")
    yuu "「君の特徴は、話していたはずなのに、どうして通したんだ。もし力ずくで押し通ったなら、騒ぎになっていたはずなのに」"

    show yuu awa nor no2 with std_change

    voice get_voice_filename("yuu")
    yuu "「それに、定期連絡にも異常はなかった」"


    voice get_voice_filename("ode")
    odette "「気付かなかったか？　その定期連絡をしてたのは、あたしだ」"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「わざと、躍らせたんだよ。てめーの仲間をぶっ倒して客を避難させただけじゃ、入り口で強硬手段に出る可能性もあった」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「この東京じゃ、どこで爆発を起こしても何人かは巻き込めるからな」"

    "だからこそ、確実に私たちが爆弾を奪取できる方法を考えたのだ。"

    "自分の命を勘定に入れていないということは、一筋縄ではいかないということ。"

    "敵の仲間をオデットさん一人で引き受けると言った時は心配もしたが、彼女は本当にやり遂げてしまった。"

    show ode noj gra gla rev with std_change

    voice get_voice_filename("ode")
    odette "「あとは分かるな。てめーをぶちのめして話を聞かせてもらう」"

    show yuu awa war wa2 with std_change

    voice get_voice_filename("yuu")
    yuu "「言っただろう？　簡単には殺されない」"

    "ユウのその言葉は、私に向けられたものだった。"


    play music audio.battle
    play se "g17_close"
    show yuu awa bat con with std_change

    "彼は手にした銃を私に向ける。"

    show rnk sci ang an1 rev behind yuu at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「くっ……」"

    "狙いは私ではない。"

    "恐らく、爆弾だ。"

    scene ecg odettobt fun with dissolve

    "だが、オデットさんは自分と向き合っている相手によそ見をさせるほど甘くはなかった。"

    play se "kick-middle"
    with quake_fast

    "身長差によるリーチを生かして、彼女はユウが引き金を引くよりも早く、彼のあごを蹴り飛ばした。"

    play se ["punch01", "dageki"]
    with quake_normal

    "すんでのところでかわしたユウに対し、オデットさんは手、足で攻撃を続ける。"


    scene bg tokyotower02 large at align(1.0, 0.3)
    show yuu awa war cl2 up at std_c
    with dissolve_long


    voice get_voice_filename("yuu")
    yuu "「こっちなら！」"

    scene bg tokyotower02 with dissolve

    "ユウは拳銃を持っていない左手で、今度はナイフを取り出した。"

    "ナイフの切っ先を見たオデットさんは、そのまま蹴ったら足を切られると思ったのだろう、一歩身を引く。"

    play se "swing"

    "その隙をついて、ユウはオデットさんの右足を左足で引っ掛ける。"

    "体勢を崩しながらも、オデットさんは飛び蹴りをユウの腹に食らわせた。"

    "ユウは片手のままで、オデットさんに銃を撃った。"

    "乾いた音で銃声が鳴る。"

    play se ["g17_shot", "g17_shot", "g17_shot", "g17_shot"]
    with quake_long

    "４発連続。"

    "エレベーターに乗る前、アランさんが撃たれたのと同じ音だ。"

    "転びながらの蹴りで体勢を崩していたので、オデットさんに銃弾は当たらない。"

    "床に反射した音が、きいんと響く。"

    "そのまま２人とも、床へ倒れ込んだ。"

    "体が小さいせいか、先に体を起こしたのはユウだった。"

    play se "byun"

    "彼は近づく前に、手にしたナイフをオデットさんへ向かって投げつける。"

    "ナイフが空を切るのと同時に、ユウは走り出す。"

    "体勢を整えるのが遅れたオデットさんも、半分寝転がったままで銃を構えた。"

    "私が構えたと思ったのと、彼女が引き金を引いたのはほとんど同じタイミングだ。"

    "だが、ユウもまた銃を撃っていた。"

    play se ["g17_shot", "g17_shot"]
    with quake_fast

    "２つの銃声が重なる。"

    "走りながらだからなのか、ユウはオデットさんとも私とも全く違う方向へ向かって撃っていた。"

    play se "metal1"
    scene bg tokyotower02 with wfade_fastest

    "オデットさんの放った銃弾は、偶然か必然か、ユウの投げたナイフに命中し、ナイフは天井側へ打ち上げられ、銃弾はまったく別方向へと飛んでいく。"

    "ユウの銃弾は、床の僅かな凹凸に反射し、オデットさんの手に命中した。"

    "いや、実際にはわずかに逸れ、手にした拳銃にのみ当たっていた。"

    "拳銃は衝撃で解体されながら、宙に浮いた。"

    scene ecg odettobt mad with dissolve_long

    voice get_voice_filename("ode")
    odette "「……面白ぇ……っ、さあ！」"


    voice get_voice_filename("yuu")
    yuu "「…………まずは一人」"

    "ユウはオデットさんに、再び銃口を向けた。"


    voice get_voice_filename("ode")
    odette "「返すぜ！」"

    play se "byun"

    scene bg tokyotower02 with dissolve_long

    "その時一瞬、私は何が起こったのか理解できなかった。"

    "ユウもまた、床に拳銃を落としていたのだ。"

    "時間差で、ユウの右手から血が滴るのを見た。"



    show rnk sci arm ten at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「きゃっ……」"

    show yuu awa war cl2 at std_r with std_in

    voice get_voice_filename("yuu")
    yuu "「ボクのナイフを……！」"

    "彼の言葉で、何が起きたのかを理解することができた。"

    "銃弾で弾いたナイフを、オデットさんはキャッチしたのだ。"

    "そしてそれを、ユウへ投げつけた。"

    show ode noj arm ser rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「さて、仕切り直しと……」"


    stop music fadeout 1

    show yuu awa war war with std_change

    voice get_voice_filename("yuu")
    yuu "「……この音」"

    hide rnk
    hide yuu
    hide ode
    with std_out

    $ renpy.music.set_volume(0.3, channel='ambient')
    play ambient "police_siren"

    "地上の方から、かすかにサイレンの音が聞こえた。"

    "事件発生からすれば、遅過ぎるくらいだろう。"

    "警察と消防隊と、機動隊も出動しているかもしれない。"

    "ユウは拳銃を拾い、非常階段へと向かった。"


    stop ambient fadeout 1
    $ renpy.music.set_volume(1.0, channel='ambient')

    play music audio.impatience

    show ode noj arm irr rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「逃げるのかっ……！」"

    "非常階段へと走ったユウは、まさにそこから出てきた人物に行く手を阻まれる。"

    show aln sta nor nor at std_r with std_in

    voice get_voice_filename("aln")
    alan "「ここは通さない」"

    show yuu awa eml su2 rev at std_c with std_in

    voice get_voice_filename("yuu")
    yuu "「君までフェイクか……！」"

    "ユウは一瞬で状況を理解したのだろう。"

    "アランさんは荷物検査のスタッフに扮していたが、撃たれることまで予想していた。"

    "そこで対策として防弾ベストを着込み、撃たれる可能性の高い腹部にはゴムのプレートも仕込んでいたのだ。"

    "ゴムにしたのは、音で無事だと気付かれないようにするためらしい。"

    "血は、血のりをあらかじめ用意していた。"

    "ここまで含めてが、私が人質になって展望台まで連れて行かれ、オデットさんがユウを無力化するための作戦だ。"

    "戦闘が始まれば、私の介入する余地は一切なかったが、それもまた予想通り。"

    "私は爆弾を守っていればよかった。"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「同行しろ。さもなくば力ずくだ」"

    "アランさんも銃で武装しているし、ユウは負傷している。"

    "そして何より、２対１で挟み撃ちをしている。"

    show yuu awa eml no2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「……嫌だね」"

    hide yuu
    hide aln
    hide ode
    with std_out

    play se ["g17_shot", "g17_shot", "g17_shot"]
    with quake_normal

    "ユウはアランさんとオデットさんが動くよりも先に、銃を数発撃った。"

    "その全てが、展望台に点在する消火器に命中した。"

    play se "air"

    show aln sta nor irr at std_r with std_in

    voice get_voice_filename("aln")
    alan "「……ちっ」"

    show ode noj gra smi rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「なるほど。煙幕代わりか」"

    show rnk sci arm ang at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「感心している場合じゃないっ！」"



    scene bg tokyotower02 large at align (1.0, 0.3)
    show white:
        alpha 0
        linear 5 alpha 0.9
    show smoke at smoke_lr(opacity = 0.5)
    with dissolve_long

    "瞬く間に、白い煙が室内を覆いつくした。"


    voice get_voice_filename("rnk")
    rinka "「きゃっ！」"


    voice get_voice_filename("yuu")
    yuu "「返してもらうよ」"

    "私が視界を失っている中、ユウの声が聞こえた。"

    "抱えていた重みが、消える。"


    voice get_voice_filename("rnk")
    rinka "「リュックが！」"


    voice get_voice_filename("yuu")
    yuu "「――明日の朝、今度こそ{rb}運命に{/rb}{rt}きみと{/rt}決着を」"

    "声に反応する余裕はなかった。"

    "私はただどうしたらいいのか、慌てているだけだった。"


    scene bg tokyotower02
    show white at alpha(0.8)
    show smoke at smoke_lr(opacity = 0.7)
    show smoke_front at smoke_lr(opacity = 0.4)
    with dissolve

    show aln sta nor ang behind smoke_front at std_cr with std_in

    voice get_voice_filename("aln")
    alan "「僕たちも限界だ。逃げるぞ」"


    show ode noj nor nor rev behind smoke_front at std_cl with std_in
    voice get_voice_filename("ode") 
    odette "「ちぃっ、面倒なルールがなけりゃよぉ」"

    "私はわけも分からないまま、アランさんに手を引かれていた。"






    python:
        set_info_scene("105")
        set_info_time("morning")
        set_info_location("02")

    stop music fadeout 2
    scene bg station01 with fade_longest
    pause 1

    $ show_hud()

    "真央は、突然終わった動画配信に驚きつつ、今度はニュースサイトに切り替えていた。"

    "状況はまだまだ不明だが、少なくとも東京タワーでテロは起きなかったらしい。"

    "しかし、人質になった少女は行方不明。"

    "拉致された可能性もあるとのこと。"

    "そんな中、真央は一つの懸念で血の気が引いていた。"

    show mao sci nor que at std_c with std_in

    voice get_voice_filename("mao")
    mao "「一瞬、りーたんの声がしなかった？」"

    "信じられないことだけど、真央は自分が親友の声を聞き間違えることはないと思っていた。"

    "だからこそ、依然として既読のつかないメッセージに気を揉んでいた。"








    python:
        set_info_scene("106")
        set_info_time("night")
        set_info_location("36")

    scene bg warehouse with fade_long
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "東京タワーには、警察や消防隊員などが押し寄せていて、大混乱といった状況だった。"

    "私たちはユウの仲間だったテロ組織の人たちが警察に身柄を拘束されている隙をついて、その場を何とか逃げ出した。"

    "一般客と野次馬で混乱していたおかげで、非常階段を抜けてからは比較的簡単にその場を離れることができたのだった。"

    "その後、私たちは拠点としていた横浜の倉庫に戻って来ていた。"



    show ode noj gra smi rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「ほれ」"

    show rnk sci nor smi at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「ありがと……いただきます」"

    "オデットさんは、私にファストフードの包みを手渡してきた。"

    "ハンバーガーとポテトが入っている。"

    "彼女の傍らには、それらとは別にコンビニで買ったお酒の瓶が置いてあった。"

    "私は、ボリュームのあるハンバーガーにかぶりつく。"

    "濃いケチャップとお肉の味が染みる。"

    "疲れているからか、強烈な味がとても美味しく感じた。"

    "そう言えば、今日初めての食事だった。"

    "今日の出来事はあまりに衝撃的で、まだ心臓がばくばくしている。"

    "食事をとるのもすっかり忘れていたのだ。"

    show aln sta nor nor at std_r with std_in

    voice get_voice_filename("aln")
    alan "「…………やはり、ユウも捕まっていないようだな」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「ま、あたしの前から逃げ出したんだ。そう簡単に捕まえられてたまるかっての」"

    "オデットさんは、豪快にハンバーガーとポテトを交互に食べていた。"

    "コーヒーに造詣が深いあたり食事にはこだわるのかと思っていたが、この人はどうやら食事そのものが好きらしい。"

    "見ていて気持ちよくなる食べっぷりだ。"

    "すでにハンバーガーは３つ目なのだから。"

    show ode noj gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「しっかし、てめーの演技は案外いけたな」"

    show aln sta nor tre with std_change

    voice get_voice_filename("aln")
    alan "「必要なら、するまでだ」"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「やせ我慢もか？」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「……分かっていたから、思ったより痛みはなかった。試してみるか？」"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「いいや、断る。あたしだったら反撃しちまうよ」"

    "結局、私はまだユウの≪未練≫のカードを手にしてはいない。"

    "私たちが思った以上に、ユウは手強い相手ということだろう。"

    "代わりに、私は彼の過去を知った。"

    "無関心への抵抗――その意味を理解していた。"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「リンカ、あのガキの演説の効果はどうだったんだ？」"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「ネットでは、ユウの昔話をきっかけに議論が起きてる。もちろん否の多い賛否両論だけど」"

    show rnk sci arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、ユウ本人に同情している声は多いみたい」"

    "ユウが動画の生配信を行った効果は出ている、と言っていいだろう。"

    "テレビでも、今日の事件は報道され続けている。"

    "犠牲者が出なかったことが不幸中の幸いだが、この世界に大きな影響を与えたことに変わりはない。"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「ユウが脱落したら、かなり大きな世界の改変が行われるだろうな」"

    show rnk sci nor que rev with std_change

    voice get_voice_filename("rnk")
    rinka "「……うん、そう思う」"

    "ユウがもし山手線の自爆テロで命を落としていたら、飴茶での爆弾テロも、今日のこの事件もなかったことになるのだろう。"

    "立て続けにテロ事件が起き、世の中は確実に緊張状態になっているのだ。"

    "今日のユウの配信をきっかけに、犯罪者側への同情も一部では高まっている。"

    "不特定多数の人に恐怖を与えているのだから、彼が世間に及ぼした影響は大きい。"

    "それら全てが、なかったことになるのだろうか。"

    "それは、その時になってみないと分からない。"

    show ode noj nor tro rev with std_change

    voice get_voice_filename("ode")
    odette "「しかし、どうしたもんかねぇ。見事に逃げられちまったもんだから、追いようもねぇ」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「僕の情報網でも、彼の動向はまだ分からない。≪ＮＵＬＬ日本支部≫は今日をきっかけに事実上壊滅状態になるだろうが、ユウは爆弾を持っている」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「爆弾ひとつでも、人の命を奪うことはできる。ユウは止まらないだろうな」"

    show rnk sci arm vig rev with std_change

    voice get_voice_filename("rnk")
    rinka "「彼はきっと、明日動きます」"

    show aln sta nor que with std_change

    voice get_voice_filename("aln")
    alan "「……心当たりでもあるのか？」"

    "私は頬張ったハンバーグを飲み込んで、続けた。"

    show rnk sci arm nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ユウは、私に言った――明日の朝、今度こそ運命に決着を――って」"

    show rnk sci nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「だから、明日も動くのは間違いない」"

    show aln sta nor clo with std_change

    voice get_voice_filename("aln")
    alan "「……そうか」"

    show rnk sci nor apo rev with std_change

    voice get_voice_filename("rnk")
    rinka "「でも、それしか分からない。一体、何をしようとしているのか……」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「順当なのは、東京タワーを狙う、だろうな。警備が厳重になっている中でやり遂げたら、さらに効果は上がるさ」"

    "私もその可能性は高い、と思っていた。"

    "彼の無関心への抵抗というのは紛れもない本心だろうけれど、それでは私に殺されたいと語ったことと繋がらない。"

    "それに、運命に決着という言葉も気になった。"

    "あれは一体、どういう意味だったのだろうか。"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「明日も早朝から、東京タワーへ向かおう。手掛かりがない今、そうするしかない」"

    "私たちは、アランさんの言葉に頷いた。"

    "この後、私たちは休むことにした。"

    "ユウが明日動くと分かっている以上、私はまだ家には帰れない。"

    "それにオデットさんが事前に対策をしていたとはいえ、東京タワーの監視カメラに私の姿が映っていたとしたら、警察に事情聴取されるに決まっている。"

    "拳銃も持っていたのだから、逮捕されちゃうかもしれない。"

    show rnk sci arm ama rev with std_change

    voice get_voice_filename("rnk")
    rinka "「はぁ……」"

    "ともかく、私は慣れていないことをしてとても疲れていた。"

    "思い返せば、無傷で戻って来られたのが奇跡に思える。"

    "それほどの状況だった。"


    scene bg warehouse with fade_long
    pause 1

    "20分ほど歩いたところに銭湯があったので、私たちはそこでお風呂に入った。"

    "帰り道で若干汗ばんでしまったけれど、極限の緊張状態で知らないうちにかなり汗をかいていたようだったから、お風呂に入れただけでもよかった。"

    "戻ってきた私たちは、すぐに眠ることにした。"

    "明日も今日と同じように早い。"

    "それに、相手の出方が分からない分、明日の方が体力を消耗するだろう。"

    "お酒を飲んでいたせいか、今日はオデットさんが先に眠ってしまったようだった。"

    "一見無防備だったが、近付けばすぐさま起きて反撃されてもおかしくない、と思っていた。"

    "昼間に見た彼らの戦いが、とても現実のものとは思えなかったからだ。"


    play music audio.growapart

    scene ecg alanspeak normal with dissolve_long


    voice get_voice_filename("aln")
    alan "「起きているのか？」"


    voice get_voice_filename("rnk")
    rinka "「う……うん」"


    voice get_voice_filename("aln")
    alan "「早く寝た方がいい」"

    "アランさんはそれだけ言うと、また顔を伏せた。"

    "銃弾を受けるという危険な役割を引き受けたことにお礼を言いたくなったが、ぐっと堪えた。"

    "これはあくまで、協力関係であり利害関係なのだ。"

    "アランさんは私を助けてくれたわけではない。"

    "余計なことを考えないように、私は彼が子供たちを人質にとったことを思い出していた。"

    "私も下を向いて眠ろうとすると、また彼の方から小声で声をかけてきた。"


    voice get_voice_filename("aln")
    alan "「人を殺すことは、罪だと思うか？」"

    "答えるまでもない質問だ。"

    "私は、首を縦に振った。"


    voice get_voice_filename("aln")
    alan "「なら、選定で人を脱落させるのは、罪か？」"


    voice get_voice_filename("rnk")
    rinka "「それは……そうだと、思う」"

    "直未と話したとき、私たちはその行為が罪だという前提で話していた。"

    "だが、その直未はいなくなってしまった。"

    "直未を取り戻すために、私は罪を犯さなくてはいけない。"

    show ecg alanspeak far with ecg_change


    voice get_voice_filename("aln")
    alan "「僕はそうは思わない。女神の選定で脱落させることは、本来の死の運命に戻すこと」"


    voice get_voice_filename("aln")
    alan "「あるいは最後の一人になり死の運命を乗り越えてしまうことの方が、罪かもしれないとも思う」"


    voice get_voice_filename("aln")
    alan "「そうなると結果的に、最後の一人になるために、女神の選定で他人を脱落させるという行為は罪になる」"

    "彼の話は、一周して矛盾した。"


    voice get_voice_filename("rnk")
    rinka "「何が言いたいの？」"

    show ecg alanspeak normal with ecg_change


    voice get_voice_filename("aln")
    alan "「最近は、そういうことをよく考える」"


    voice get_voice_filename("rnk")
    rinka "「は？」"

    "答えになっていない答えに、私は思わず聞き返してしまった。"

    "それ以上、アランさんは何も言わなかった。"

    "会話もなくなり、まどろみの中へ落ちていく間際、私はあることに気が付いた。"

    "アランさんの言葉はまるで弱音のようだったと。"

    "だとすれば、それを私の前でこぼした意味を――私は推し測ることができなかった。"

    if flags_route_A:
        $ add_seen_chapter("7_2-2")
    elif flags_route_B:
        $ add_seen_chapter("7_3-2")








    python:
        set_info_scene("107")
        set_info_date(6, 17, "sun")
        set_info_time("emorning")
        set_info_location("37")

    stop music fadeout 2
    scene bg tokyotower01 with fade_longest
    pause 1

    $ show_hud()

    "翌朝、私は再び東京タワーを訪れていた。"

    "昨日のこともあり、展望台は休業となっていた。"

    "水族館と一部の売店のみの営業のようだ。"

    "テロ騒ぎがあったのだから、無理もない。"

    "真相を知っている私たちからすれば、発砲や人質騒動、人質の少女は身元不明で行方不明という結果は、十分大事件。"

    "むしろ完全封鎖になっていない方が驚きだ。"

    "あるいはそれは、テロには屈しないという意志の表れかもしれない。"


    play music audio.gimon

    show ode noj nor tro rev at std_l with std_in

    voice get_voice_filename("ode")
    odette "「しかしまあ、これじゃあ奴も事を起こす意味がない」"


    show rnk sci nor nor at std_c with std_in
    voice get_voice_filename("rnk")
    rinka "「でも、必ず何かすると思う。じゃないと、『運命に決着を』なんて言わない」"

    show aln sta nor nor at std_r with std_in

    voice get_voice_filename("aln")
    alan "「心当たりがないのか、もう一度よく考えてみろ」"

    "アランさんは、静かな声でそう言った。"

    "その穏やかな力強さの中には、昨日見せたような弱さはどこにもない。"

    "心当たり――そんなもの、私には分からない。"

    "こういう時は、順番に考えてみるべきか。"

    "私とユウとの因縁。"

    "それは、直未を中心とするものだ。"

    "飴茶で、ユウは直未の命を奪った。"

    "――私に、ユウを脱落させるために。"

    "その真意は、まだ分からない。"

    "だが昨日ユウが語った世界への演説の中に、その手掛かりはあったと思う。"

    "死して、英雄になること。"

    "何かを成し遂げて死ぬことでこそ英雄になると言っていた。"

    "何故、私でなくてはならないのか。"

    "彼を脱落させるなら、他の誰でも――。"

    "私の脳裏に、炎がくゆった。"

    "炎の中で交わされた、運命の会話。"

    "――お前は英雄なんかにはなれない。"

    "――人間ですらない。"

    "――ただの人形だ。"

    "死の淵、ユウにそう言い放ったのは他でもない私だった。"

    show rnk sci arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「まさか……」"

    "思い至ると、すぐに結論と結びついた。"

    "その結論は恐らく、答えに最も近い。"

    "私は、オデットさんとアランさんに向き直る。"

    show rnk sci arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「私一人で、行かせて」"

    show ode noj arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「……ああん？」"

    show rnk sci nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「運命に決着をつけてくる」"

    show aln sta nor que with std_change

    voice get_voice_filename("aln")
    alan "「……心当たりがあったのか？」"

    show rnk sci nor nor rev with std_change_wait

    "アランさんの問いかけに、私は深く頷いた。"

    "反対されるのは目に見えていた。"

    "だが、詳しく説明すれば、私の情報も彼らに知られることになる。"

    "いや、概要を話すだけでも、彼らはきっとついて来るだろう。"

    "今はユウの手がかりが何もない状況なのだから、私の思いつきとはいえ乗るしかないだろう。"

    "だが、それではいけない。"

    "私一人で立ち向かわなければ、きっと答えには辿り着けない。"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「好きにしろよ。逃げる奴の目じゃねーだろ」"

    show aln sta nor lee with std_change

    voice get_voice_filename("aln")
    alan "「同感だ」"

    "アランさんは私の瞳を覗き込むようにして、ゆっくりとそう言った。"

    "少しして彼の方が目をつぶり、続けた。"

    show aln sta nor que with std_change

    voice get_voice_filename("aln")
    alan "「僕たちは、各自調べる……協力関係もここまでだ」"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「かかっ、まあ悪くはなかったよ。中々楽しめた」"

    show aln sta nor clo with std_change

    voice get_voice_filename("aln")
    alan "「……フン」"

    show rnk sci sur su2 rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ええっ……えっ？　いいの？　だって……」"

    show aln sta nor tre with std_change

    voice get_voice_filename("aln")
    alan "「仮に君が逃げようとしていたところで、僕たちから逃げられると思うか？」"

    show rnk sci arm lie rev with std_change

    voice get_voice_filename("rnk")
    rinka "「その方が、落ち着きます」"

    show ode noj gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「嬢ちゃんも中々嫌味な性格になったもんだ」"

    show rnk sci arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「誰のせいだと」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「次に会うときは、敵同士だ」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「今だって十分敵だよ。あたしらは。敵同士が一時的にお手てを繋いでただけなんだからな」"

    "不思議と、私の心臓の鼓動は速くなっていた。"

    "この人たちといると湧き上ってくる、奇妙な高揚感を味わっていた。"

    hide aln
    hide ode
    hide rnk
    with std_out

    "そして、私たち３人は別々の方向へ歩き出していった。"

    if flags_route_A:



        "オデットさんやアランさんと肩を並べられたことは、私にとって力になっていた。"

        "別の世界の住人かと思っていた彼女たち。"

        "身体能力や荒事に関しては私では至らないけれど、その精神性だけは対等だ。"

        scene bg tokyotower01 large at align(0.5, 0.3)
        show rnk sci arm vig up at std_c
        with wipe_lr

        voice get_voice_filename("rnk", 1044)
        rinka "「いくよ」"

        "私は強い決意の言葉を、胸の内で復唱した。"

    if flags_route_B:



        play music audio.death

        show ode noj arm ser rev at std_cl with std_in

        voice get_voice_filename("ode", 406)
        odette "「まあ待てよ」"

        "立ち去ろうとする私の背中に、冷たい声がかけられた。"

        "オデットさんのその声は、さっきまでとは異質なものに変わっていた。"

        "その意味を、私は理解している。"

        show rnk sci arm sad at std_cr with std_in

        voice get_voice_filename("rnk", 1045)
        rinka "「……分かってるよ」"

        "それ以上、余計な言葉を交わす必要はなかった。"

        "私はオデットさんに淡々と、自分のカードの内容を伝えた。"

        "これも一つの、運命の決着なのだから。"








    python:
        set_info_scene("108")
        set_info_time("morning")
        set_info_location("02")


    stop music fadeout 1
    scene bg station01 with fade_long
    play music audio.maintheme
    pause 1

    $ show_hud()

    "ある一つの結果に到達するまでの過程を、人は物語や人生と呼ぶ。"

    "様々な出会いがあり、別れがあり、事件があり、選択があり、そして未来の可能性の中を進み、一つの結果へ到達する。"

    "この世界というのは――運命というのは、そういう風にできている。"

    "運命は変わらないから運命なんだ。どんなに理不尽でも。"

    "そう、思っていた私に、私はお別れを告げた。"

    "運命は、人が自分自身で背負うものだ。"

    "だったら、私が決着をつけてやる。"

    "――変えてやる。"

    "東京タワーの最寄り駅から電車を乗り継ぎ、新宿駅へと到着した。"

    "ホームの階段を駆け上り、私はあの日と同じ場所へ戻ってきた。"

    "私の命が失われるきっかけとなった、あの日と同じ場所。"

    "女神の選定が始まったから、私は何度もこの駅を利用していた。"

    "けれども私の運命にとって同じなのは、今この瞬間であった。"

    show rnk sci arm ang at std_c with std_in

    voice get_voice_filename("rnk", 1046)
    rinka "「……っ、いる……！」"

    hide rnk with std_out

    "すでに電車は来ていて、ちょうど発車ベルが鳴り響く時。"

    "駅のホームの端に、彼の姿を見つけた。"

    show yuu sta sac non at std_c with std_in

    voice get_voice_filename("yuu")
    yuu "「…………」"

    "ユウは、どうやら今日も変装をしているようだ。"

    "遠目でほとんど輪郭しか見えないのに、私には彼の白い髪も、獣のような瞳も、背負った鍵のチャームがついたリュックも見えた気がした。"

    "彼もまた、私の存在に気付いたようだ。"

    "気温が下がるかのような視線を感じる。"

    "あるいは、そこでずっと私が来るのを待っていたのかもしれない。"

    "いや、きっとそうだ。"

    "ユウは正面に向き直ると、電車に足を踏み入れた。"

    "私も遅れないように、目の前の車両へと乗り込んだ。"







    $ set_info_location("03")


    stop music fadeout 1
    scene bg train normal with fade_long
    play music audio.impatience
    pause 1

    "日曜日の環状線だから、平日の通勤ラッシュほどではないにしろ、人は多かった。"

    "座席は全て埋まっていて、立っている乗客もそれぞれ一人分ずつくらいの隙間しかない。"

    show rnk sci arm imp at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「急がなくちゃ」"

    hide rnk with std_out

    "あの日、新宿を出てすぐに事は起きた。"

    "私は人にぶつかるのも気にせず、乗客をかき分けながらユウの乗りこんだ車両に向かって走っていた。"

    "進行方向と同じ、前方車両へ。"




    stop music fadeout 1

    "それは、一瞬の出来事だった。"

    "ユウがリュックを開いたのと、私がその車両に到達したのは同時だった。"


    play music audio.kinpaku

    show rnk sci ang an2 at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「逃げて！」"

    "私は、乗客に向かってそう叫んだ。"

    "どれだけの人が、私の言葉を聞いてくれたかも分からない。"

    "私が何を言ったのか聞き取れず、騒ぎにすらなっていない。"

    "だが、私には関係ない。"

    "私がすべきは、ただ一つ。"

    show yuu sta sac non rev at std_cl with std_in

    voice get_voice_filename("yuu")
    yuu "「……来たね」"

    show yuu awa nor no2 rev with std_change_wait

    "そこで、ユウは変装を解いた。"

    "彼の姿は、昨日の動画配信で日本中に知られている。"

    "ユウに気付いた人から、自分が今どんな状況にいるのかを理解したようだった。"

    "彼の姿は、私の声よりもよっぽど効果的であった。"


    voice get_voice_filename("rnk")
    rinka "「何をするつもり？」"

    show yuu awa eml wa2 rev with std_change

    voice get_voice_filename("yuu")
    yuu "「言ったはずだよ。運命に決着をつけるって」"


    voice get_voice_filename("rnk")
    rinka "「ここで爆弾を爆破させても、あなたはもう誰も殺せない」"

    "ユウが突然の強行に出なかったのが、幸いした。"

    "彼はいきなり爆弾を爆発させて乗客を巻き込むこともできたのだ。"


    play music audio.resistance
    scene ecg rinyuufaceto c with dissolve_long


    voice get_voice_filename("yuu")
    yuu "「いいよ。君がここに辿り着いてくれたから」"


    voice get_voice_filename("rnk")
    rinka "「あなたの希望は分かってるよ」"

    "私は毅然とした態度で、ユウに向き合った。"

    "乗客は徐々に、この車両から離れ始めている。"

    "私も知らない人に逃げるようにと腕を引っ張られたが、振り切った。"

    "私が逃げるそぶりを見せたら、それこそユウは爆弾を投げてくるかもしれない。"

    "もっとも、私は逃げる気なんて毛頭ない。"

    "この決着が、つくまでは。"

    show ecg rinyuufaceto b with ecg_change


    voice get_voice_filename("rnk")
    rinka "「英雄になりたいんだ。人形じゃなく、人間に」"


    voice get_voice_filename("yuu")
    yuu "「やっぱり、あれは幻聴じゃなかったんだ。あの時ボクたちは、カードブックを持っていなかったのに、会話が通じた」"


    voice get_voice_filename("yuu")
    yuu "「ボクはまだ日本語を、ほとんど使うことができなかったからね」"

    show ecg rinyuufaceto c with ecg_change


    voice get_voice_filename("rnk")
    rinka "「どうだっていい。あなたの言う決着は、これで終わりじゃないはず」"

    show ecg rinyuufaceto d with ecg_change


    voice get_voice_filename("yuu")
    yuu "「お前がボクを殺さなったからさ。今こうなっているのは！」"


    voice get_voice_filename("rnk")
    rinka "「だから言ってる。決着をつけたいのは、あなただけじゃない」"


    voice get_voice_filename("yuu")
    yuu "「記憶を失っていたけれど、おじいちゃんと生活しながら、ボクは徐々に思い出していたんだ」"


    voice get_voice_filename("yuu")
    yuu "「自分のことを。行き詰まった自分の過去を。ボクは自分の性質を分かっていた」"


    voice get_voice_filename("yuu")
    yuu "「だから５度目の選定のとき、お前に指名して欲しいとお願いをしたんだよ」"


    voice get_voice_filename("yuu")
    yuu "「ボクはもう、お前たちの言う普通へは帰れない！」"

    show ecg rinyuufaceto f with ecg_change


    voice get_voice_filename("rnk")
    rinka "「それでも！　牛塚さんとあなたは普通に暮らしていた。あなたはそうすることもできていた。まるで、家族のように！」"


    voice get_voice_filename("yuu")
    yuu "「できない方が幸せだったよ！　失うのは記憶じゃなくって、理性の方であるべきだった！」"


    voice get_voice_filename("yuu")
    yuu "「もしそうだったらボクは、人を殺すだけの機械になれた！」"


    voice get_voice_filename("yuu")
    yuu "「お前たちと同じ普通を知ってしまったからこそ、ボクは自分を否定しなくちゃいけなくなったんだ！」"

    show ecg rinyuufaceto g with ecg_change


    voice get_voice_filename("rnk")
    rinka "「あなたらしい生き方を探せばよかった！」"


    voice get_voice_filename("yuu")
    yuu "「無理だ！　おじいちゃんだって、そんなこと教えられない！」"


    voice get_voice_filename("rnk")
    rinka "「言葉にしなくても伝わると思ったから。あなたを信じていたから」"


    voice get_voice_filename("rnk")
    rinka "「牛塚さんはあなたに決めて欲しかった。生き方を選んで欲しかった。あなたが道を選べるように、お金だけを残したんでしょ」"

    show ecg rinyuufaceto i with ecg_change


    voice get_voice_filename("yuu")
    yuu "「そんなのっ、ボクにはっ！」"


    voice get_voice_filename("rnk")
    rinka "「無理じゃない。あなたは自分の意志で、自分が人形になるのを選んだんでしょ！」"


    voice get_voice_filename("yuu")
    yuu "「ボクは人形じゃない！」"

    show ecg rinyuufaceto f with ecg_change


    voice get_voice_filename("rnk")
    rinka "「だったら！」"


    voice get_voice_filename("yuu")
    yuu "「だからこうして、お前に殺されるようにしているんだ！　お前に殺されて英雄になるんだ！」"

    show ecg rinyuufaceto g with ecg_change


    voice get_voice_filename("rnk")
    rinka "「あなたの言う英雄って、何？　あなたにとっての英雄って、本当は空虚な幻想なんじゃないの？」"

    show ecg rinyuufaceto d with ecg_change


    voice get_voice_filename("yuu")
    yuu "「何かを成し遂げて、死ぬこと。死んで永遠になることだ」"


    voice get_voice_filename("yuu")
    yuu "「ボクはおじいちゃんがいなくなったから、自分の意志で元の仕事をこなすことを決めた。自分の意志で、世界へ抵抗することを決めた」"


    voice get_voice_filename("yuu")
    yuu "「自分の意志で、お前に殺されることを望んだ。だから自分の意志で、お前の大切なものを奪った……殺した」"


    voice get_voice_filename("yuu")
    yuu "「自分の意志で行動したんだ。ボクは自分の意志があることを証明できた……成し遂げたんだ！」"

    "直未の話題が出てきて、私は思わず叫びそうになった。"

    "だが、その怒りを奥歯でぐっと噛み殺す。"

    "ユウの語る言葉は全て、きっと彼の本心だ。"

    "だからこそ、彼に憐れみを覚えずにはいられなかった。"

    "そんなことしちゃ、駄目だと思っていた。"

    "直未を殺した相手に同情なんて、してはいけないと分かっている。"

    "東京タワーで私を人質にとった時に語った彼の過去を聞いても、私はそんなの関係ないと割り切った。"

    "でも……、でも……！"

    show ecg rinyuufaceto g with ecg_change


    voice get_voice_filename("rnk")
    rinka "「あなたの思う、英雄は誰なの？」"

    "その質問を、せずにはいられなかった。"


    voice get_voice_filename("yuu")
    yuu "「ボクの思う……一番の、英雄……」"


    voice get_voice_filename("yuu")
    yuu "「決まってる、それはママだ！」"


    voice get_voice_filename("rnk")
    rinka "「その人は、あなたに何を与えたの？　それはきっと、牛塚さんがあなたに与えたのと同じことじゃないの？」"

    show ecg rinyuufaceto h with ecg_change


    voice get_voice_filename("yuu")
    yuu "「えっ……あっ……マ、ママに……もらった……もの……？」"


    voice get_voice_filename("rnk")
    rinka "「牛塚さんは、あなたに誰かに何かを与えられる人になって欲しいと願っていた。その理想は、あなたの言うママと同じはず」"


    voice get_voice_filename("rnk")
    rinka "「でもその何かは、恐怖や絶望、怒りや悲しみなんかじゃない。そんなこと、誰も望んではいないはず。ユウ！　あなただって！」"


    voice get_voice_filename("yuu")
    yuu "「ボクは、自分の……っ」"


    voice get_voice_filename("rnk")
    rinka "「あなたが牛塚さんのつけてくれた名前を受け入れたのは、それが分かっていたからでしょ！　ユウっていうのはね、優しくて勇ましいってこと」"


    voice get_voice_filename("rnk")
    rinka "「あなただってそうなりたいから、今だって自分のことをユウって思ってるんでしょ！」"


    voice get_voice_filename("rnk")
    rinka "「だってあなたの≪氏名≫のカードは消えていない。あなたの本当の意志は、英雄になんてなりたがっていない！」"

    show ecg rinyuufaceto i with ecg_change


    voice get_voice_filename("rnk")
    rinka "「自分と向き合うことから、逃げるな！」"

    show ecg rinyuufaceto f with ecg_change


    voice get_voice_filename("yuu")
    yuu "「黙れっ！　もう、喋るなっ！」"

    "ユウは私の言葉を、絶叫で遮った。"

    "そして向けてきたのは、言葉だけではなかった。"

    "明確な、敵意。"

    "いや、彼の表情は自暴自棄になった子供そのものだった。"

    show ecg rinyuufaceto d with ecg_change


    voice get_voice_filename("yuu")
    yuu "「うわああっ！」"

    "絶叫と同時に、彼はリュックを開けた。"

    scene ecg bomb nor with dissolve

    "中にはあの日と同じ――爆弾が入っている。"

    scene ecg claimerrinka nor2 with dissolve


    voice get_voice_filename("rnk")
    rinka "「やめろっ！」"

    "彼は今、他人を殺そうとしているんじゃない。"

    "自分を――傷つけようとしているんだ。"

    "矛盾した自分自身から、逃げるために。"

    "私は、ユウに向かって走っていた。"

    "動いたのは、体が先だ。"

    "思考や理由は、後からついてくればいい。"


    voice get_voice_filename("rnk")
    rinka "「ヤケになんて……！」"


    voice get_voice_filename("yuu")
    yuu "「ボクはぁっ！」"



    scene bg train normal with dissolve_long

    "この距離なら、ユウが着火の動作をするのに間に合う。"

    "届く。"

    "だが、その時、電車が大きく揺れた。"

    "急ブレーキを告げるアナウンスが、スピーカーから発せられた。"

    "逃げ出した誰かが、車内の非常停止ボタンを押したのだろう。"

    "ユウに向かって走る体勢となっていた私は、転ばないように踏ん張るため、必要以上に後ろへ体重をかけてしまっていた。"

    "停車の反動でさらに足をもつれさせ、私は立ったまま車両を繋ぐドアに背中を叩きつけた。"

    "何が起こったのかを理解し、再びユウへと向き直ったとき――すでに手遅れだった。"




    stop music fadeout 1
    play se "bomb2"
    show layer master at quake
    scene white with dissolve_fast
    pause 3

    "轟音とともに、閃光が走った。"

    "私の深層心理が、その光景を覚えていた。"







    play ambient "fireloop" fadein 5
    scene bg train enjo with dissolve_long

    show rnk sci arm ang at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「くっ……」"

    "爆発の瞬間、私は目をつぶっていた。"

    "距離があったこと、そしてユウが爆弾を抱きかかえるようにして着火したことから、私は爆弾の破片で足に数センチの切り傷を作る程度で済んでいた。"

    "あるいは、≪女神の選定≫の参加者であるがゆえ、死から守られたのかもしれない。"

    "爆発による延焼は、以前のように車内へと広がっていた。"

    "視界をゆらめかせるように、炎がくゆる。"

    "ちりちりと、肌には熱を感じる。"

    "私の底に眠る記憶……夢の世界で目にした、なかったことになっていた記憶と、ほとんど同じ光景であった。"

    show rnk sci arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「ユウは……」"


    stop ambient fadeout 3
    play music audio.firedeath
    scene ecg yuuburn with dissolve_long


    voice get_voice_filename("yuu")
    yuu "「クク……やっぱりボクは、死ねないんだ……」"

    "私はユウの姿を見たとき、思わず目を逸らしてしまった。"

    "爆発により焼けただれた皮膚。"

    "破片を浴びて出血している、露出した筋肉。"

    "一瞬視線を向けただけでも、その無惨さが目に焼きついた。"

    "煙に乗って、焦げた生臭い臭いが漂ってくる。"

    "私はゆっくりと、再び彼の姿を直視することにした。"


    voice get_voice_filename("rnk")
    rinka "「こっちへ来て！　そんな怪我じゃ！　すぐ手当てすれば、まだ……！」"


    voice get_voice_filename("yuu")
    yuu "「ボクを手当てして、どうするつもりだい？」"


    voice get_voice_filename("rnk")
    rinka "「くっ……」"


    scene bg train enjo with dissolve_long

    "爆心地となったユウのいる側の方が、遥かに熱い。"

    "私はユウの元まで行こうとするが、体が動かなかった。"

    "ユウの足元には傷ひとつついていないカードブックが落ちていた。"

    "炎が燃え移ってもおかしくない位置にあるのに、まるで関係なしにそこにあった。"

    "その傍らに、ほとんど焼けただれたリュックの残骸があった。"

    "鍵のチャームだけが、かろうじて原形を留めていた。"

    "ユウはゆっくりとした動きで、そのチャームを拾う。"

    scene ecg yuuburn with dissolve_long


    voice get_voice_filename("yuu")
    yuu "「このキーホルダーがついたリュックは……ボクが日本に来て買ったものだ。別に、何となく買っただけだ」"


    voice get_voice_filename("yuu")
    yuu "「でも、東京タワーでこれをとられたとき、取り返さなくちゃって思った。ボクの大事なものになってたんだよ」"


    voice get_voice_filename("yuu")
    yuu "「おじいちゃんと暮らして……大事なものになっちゃったんだ」"


    voice get_voice_filename("rnk")
    rinka "「話なら後で聞くから、今は、こっちに！」"

    "自分でも、どうして彼の怪我を心配しているのか分からなかった。"

    "ユウからは、≪未練≫を聞き出せればそれでいいのに。"

    "大怪我をした彼の姿を見ていると、落ち着いてはいられなかった。"


    voice get_voice_filename("yuu")
    yuu "「おじいちゃんは誰かが家にいるときは鍵をかけなかったけど、出かけるときは鍵をかけた」"


    voice get_voice_filename("yuu")
    yuu "「鍵をかけて家を出る。鍵を開けて家に入る。そんなの……君たちからすれば当たり前だよね」"


    voice get_voice_filename("yuu")
    yuu "「その当たり前が……欲しくなっちゃってたんだ」"


    voice get_voice_filename("yuu")
    yuu "「おじちゃんがいなくなって、それが叶わなくなってから、気が付いた」"


    voice get_voice_filename("yuu")
    yuu "「……できることなら、ボクは君たちと同じ普通の中で暮らしたかったんだ」"

    "その時、私が持っていたカードブックが光を放つ。"

    python:
        add_character_cards("rnk", ["4_regret2"])
        add_character_cards("yuu", ["4_regret2"])

    "だが、その内容を確認できるような状況ではなかった。"

    "私は、体が許すぎりぎりのところまで彼に近づき、手を伸ばした。"

    "押し寄せてくる熱に、私は全身から発汗していた。"

    "汗は雫になる前に、蒸発していくような気さえする。"


    voice get_voice_filename("rnk")
    rinka "「こんな時に！　今は、そんなのいいから！」"


    voice get_voice_filename("yuu")
    yuu "「これで……ボクを殺せるね……」"


    voice get_voice_filename("rnk")
    rinka "「ユウくん！」"

    "彼の姿を私の視界から消し去るように、大量の煙が吹き荒んだ。"

    "窓が割れて急激に空気が流れ込んだせいだろう。"

    "炎は、より強くなる。"

    "私は目を開けていることすらできず、しゃがみこんでしまった。"

    "煙を吸い込まないように、体が勝手に動いたのだ。"

    "だが、それでも伸ばした右手は引っ込めない。"

    "右手だけは、心が体に勝っていた。"

    "何か、硬いものが手に触れる。"




    scene white with dissolve_long



    voice get_voice_filename("yuu")
    yuu "「お姉ちゃん……ありがとう……」"

    "その声は彼が私の手に触れたのか、あるいは幻聴か。"

    "私の精神を圧迫する熱量により、私の意識はぼんやりとしていく。"

    "そのまま、真っ暗になる意識に逆らうのをやめた。"

    if flags_route_A:
        $ add_seen_chapter("7_2-3")
    elif flags_route_B:
        $ add_seen_chapter("7_3-3")

label sentei7:

    call set_replay








    python:
        set_info_date(6, 17, "sun")
        set_info_scene("109")
        set_info_time("lnight")
        set_info_location("07")


    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall
    pause 2
    scene bg fatalhall01 up with dissolve
    pause 1

    $ show_hud()

    show dia sta fro smi ci at ci_c with ci_in

    voice get_voice_filename("dia", 141)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "次に意識を取り戻したのは、高らかに響くその声を聞いたときだった。"

    show dia sta fro no1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「おや、お顔がすぐれませんわね」"

    "電車の中、熱と煙にやられた私は意識を失ってしまった。"

    "運命の大広間にいるということはつまり、選定が始まったということ。"

    "電車に乗り込んだのがお昼前だったから、12時間くらい眠り続けていることになるのだろう。"

    "現実世界の私は、病院にいるのだろうか。"

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln", 234)
    alan "「……フン」"

    show ode sta nor lau ci at ci_r with ci_in

    voice get_voice_filename("ode", 407)
    odette "「かーっ」"

    "アランさんとオデットさんは、相変わらずの斜に構えた態度でいた。"

    "オデットさんに至っては、あくびをしている。"

    "この夢の世界の中では、眠くなることもないだろうに。"

    hide ode
    hide aln
    hide dia
    show sca sta nor bit rev ci at ci_l
    with ci_swap

    voice get_voice_filename("sca", 132)
    scale "「はぁ……」"

    "スケールさんは、呆れた顔でため息をついてる。"

    "その表情からは、どんなことを考えているのかよく分からない。"

    show fed sta nor irr ci at ci_r with ci_in

    voice get_voice_filename("fed", 192)
    federico "「…………ちっ」"

    "フェデリーコさんはというと、舌打ちをしてそわそわとした態度のまま、文字盤の床の上で貧乏ゆすりをしていた。"

    "彼らがどういう関係にあるのか、現在の情報では想像することしかできない。"

    "少なくとも、オデットさんは彼らと袂を分かったままであろう。"

    hide fed
    hide sca
    show mhr uni nor ser ci at ci_r
    with ci_swap

    voice get_voice_filename("mhr", 391)
    miharu "「…………」"

    "海晴はと言えば、私をちらりと見て、安堵したような表情を浮かべていた。"

    "電車で倒れた私のことを、何かの手段で知ったのかもしれない。"

    "話しかけてこないのは、海晴がまだスケールさんたちと協力関係にあり、私と仲違いしているように思わせないといけないからだろう。"

    hide mhr
    show yuu sta nor sad rev ci at ci_l
    with ci_swap

    voice get_voice_filename("yuu", 350)
    yuu "「…………お姉ちゃん」"

    "そして私は、Ⅳの床の方を向いた。"

    "ユウが、傷ひとつない状態でそこにいた。"

    "フェデリーコさんの時もそうだったけれど、現実世界での身体の状態は、夢の世界では反映されないのだろう。"

    "綺麗な顔の彼を見て、私は奇妙な安心感を覚えていた。"

    "これから、彼を指名しなければならないというのに。"

    show rnk uni arm ang ci at ci_r with ci_in

    voice get_voice_filename("rnk", 1079)
    rinka "「……私は」"

    "私は、カードブックを開いた。"

    "飛び出したカードの中から、生成されたはずのカードを確認する。"

    "――Ⅳ・未練。"

    "それは、ユウの≪未練≫のカードだ。"

    show dia sta nor smi rev ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「なんだか、とても険悪な雰囲気ですわねぇ」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシが、皆サマをなごませてあげられればいいのですけれど」"

    hide yuu
    hide rnk
    hide dia
    show ode sta arm smi ci at ci_r
    with ci_swap

    voice get_voice_filename("ode")
    odette "「それはいい。おうたでも歌ってもらおうかい。女神様よ」"

    show aln sta nor irr rev ci at ci_l with ci_in

    voice get_voice_filename("aln")
    alan "「……くだらん」"

    hide aln
    show fed sta nor pa1 rev ci at ci_l
    with ci_swap

    voice get_voice_filename("fed")
    federico "「そうだ！　もう始めてくれ。どうせオレは今日は――」"

    show ode sta nor gla ci with ci_change

    voice get_voice_filename("ode")
    odette "「誰も指名しない……かい？」"

    show fed sta nor ir2 rev ci with ci_change

    voice get_voice_filename("fed")
    federico "「ちっ、うるせぇ。どうせてめーも同じだろ」"

    show ode sta arm smi ci with ci_change

    voice get_voice_filename("ode")
    odette "「さぁて、どうかなぁ？」"

    "オデットさんがにやりと笑うと、フェデリーコさんは顔をしかめた。"

    hide fed
    hide ode
    show sca sta nor joy ci at ci_r
    with ci_swap

    voice get_voice_filename("sca")
    scale "「たった一人しか死の運命を乗り越えられないんだ。険悪にもなるだろう」"

    show sca sta nor lau ci with ci_change

    voice get_voice_filename("sca")
    scale "「女神の歌は聞いてみたくもあったけれどね、ＨＡＨＡＨＡ」"

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln")
    alan "「……いい加減、始めてくれ」"

    "アランさんは呆れた声で、女神にそう言った。"

    "選定初期と違い、すでにそれぞれが面識のある状態の今は、会話にも奇妙なリズムが生まれている。"

    "そのことがとても、恐ろしい。"

    show dia sta fro fee ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「もう、せっかく皆サマの知っているおうたも勉強しましたのに。残念ですわ」"

    hide aln
    hide sca
    show fed sta nor ama rev ci at ci_l
    with ci_swap

    voice get_voice_filename("fed")
    federico "「どこで勉強したっていうんだよ……」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「知りたいですか？」"

    show ode sta arm ser ci at ci_r with ci_in

    voice get_voice_filename("ode")
    odette "「あたしも……興味あるなぁ」"

    "オデットさんの声音が、真剣なものに変わった。"

    "彼女と直接話したことがあるから、分かる。"

    "何気ない言葉に聞こえるが、そこには威圧の意味がこめられている。"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「うふふっ。まだ、教えてあげませんわ」"

    show dia sta fro gl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「レディは秘密が多い方が、魅力的でございましょう？」"

    "女神は、悪戯っぽくそう言った。"

    "まるで、人間の子供のように。"

    hide fed
    hide ode
    show yuu sta eml non rev ci at ci_l
    with ci_swap

    voice get_voice_filename("yuu")
    yuu "「……いいから早くしてよ」"

    "ユウは冷たい声で、そう言った。"

    "パルカに対しての興味がないことが、よく分かる。"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら、せっかちさんですわねぇ。けれど、今日は少しお話しし過ぎてしまったかもしれませんわ」"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「それでは、今宵も女神の選定を始めますわ」"


    voice get_voice_filename("dia")
    parca "「廻りなさい。運命の大時計」"

    "パルカはその澄んだ声で、決まり文句を高らかに告げた。"

    "運命の大広間の中心にある時計の針が、回り出す。"

    "今夜の彼女の宣言は、今までとは全く違って聞こえた。"

    "なぜなら、今日は私にとって――初めて人を指名する夜なのだから。"




    play music audio.electing

    if flags_route_A:


        scene bg fatalhall01 up
        show rnk uni arm sad ci at ci_r
        with dissolve_long

        voice get_voice_filename("rnk", 1080)
        rinka "「でも――」"

        "この期に及んで、私は葛藤していた。"

        "人を指名するということは、人から生きるというはしごを外すことに等しい。"

        "人を殺すことにも、等しい。"

        "ユウの苦しみの声が、思い出される。"

        "世界への叫びが、思い出される。"

        "矛盾との戦いが、思い出される。"

        "私はあらためて、彼の顔を見た。"

        "こうしてみれば、テロなんて起こしそうにない少年だ。"

        "瞳の中には獣の鋭さはなく、穏やかですらあった。"

        "自分はもう指名されるのだと、諦観しているのか。"

        "ようやく苦悩から解放されるのだと、安堵しているのか。"

        "ここからでは、私には到底分からない。"

        show yuu sta eml non rev ci at ci_l with ci_in

        voice get_voice_filename("yuu", 352)
        yuu "「…………」"

        "ユウはもう、私には何も言おうとはしなかった。"

        show dia sta nor ama rev ci at ci_c with ci_in

        voice get_voice_filename("dia", 152)
        parca "「Ⅰ番サマ、いかがなさいますか？」"

        "女神の声は、私の心を見透かしているかのようだった。"

        "私がユウを指名しようとしていることを、知っているかのような。"

        "現実世界の様子を見ているとしたら、そう思うのも当然だ。"

        "何らかの方法で、私たちを見ているとしたら――けれども今、そんなことはどうでもよかった。"

        show rnk uni arm ang ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「私はっ……」"

        "言いかけて、その先が出てこなかった。"

        "人の命を踏み台にする業を背負う覚悟は、したはずなのに。"

        "呼吸の仕方を忘れてしまったかのように、続く言葉は出てこない。"

        hide yuu
        show mhr uni nor ser rev ci at ci_l
        with ci_swap

        voice get_voice_filename("mhr", 392)
        miharu "「……君は……」"

        show dia sta fro smi ci with ci_change

        voice get_voice_filename("dia")
        parca "「あら、どうされました？　指名は、いかがなさいますか？」"

        show rnk uni arm ten ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「私は……！」"

        "何のために、ユウの未練を手に入れたのか。"

        "このままでは、分からなくなってしまう。"

        "だけど、だけど……。"

        show dia sta nor ama rev ci with ci_change

        voice get_voice_filename("dia")
        parca "「指名はなし、でよろしいでしょうか？」"

        show rnk uni arm imp ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「待って……！」"

        "――直未の顔が脳裏に浮かぶ。"

        "ユウを脱落させて、その間の行動をなかったことにする。"

        "飴茶女子高校での爆破テロを、なかったことにする。"

        "そうすれば、直未は――。"

        "しっかしろ、獅子舞凛火。"

        "私は自分の名前を、自分へ呼びかけた。"

        "そんなの、駄目だ。"

        "こんな考え方は、一緒に罪を背負うってことじゃない。"

        "ただ、自分の弱さを直未のせいにしているだけだ。"

        "私は自分の意志で、決断したのだ。"

        "自分の意志で、彼を指名することを決めたのだ。"

        "私自身の未練を思い出した。"

        "生きると、決めたんだ。"

    if flags_route_B:


        scene bg fatalhall01 up with dissolve_long

        "迷うことなど、何もなかった。"

        "私の運命はすでに、決している。"

        "今日は、私の人生最期の日だ。"

        "やるべきことをやり遂げて、私は散るのだ。"

        "なんて、皮肉。"

        "そんな考え方は、ユウの望む英雄の姿じゃないか。"



    if flags_route_A:
        show rnk uni arm vig ci with ci_change

    if flags_route_B:
        show rnk uni arm vig ci at ci_r with ci_in

    voice get_voice_filename("rnk", 1084)
    rinka "「指名……するよ」"

    show dia sta nor smi rev ci with ci_in

    voice get_voice_filename("dia", 155)
    parca "「…………ふふっ。あら」"

    "私は背筋を伸ばして、姿勢を整えた。"

    "そして、ユウの姿をしっかりと見据えた。"

    hide mhr
    show yuu sta nor nor rev ci at ci_l
    with ci_swap

    "ユウの優しい目と、私の目が合った。"

    "今のユウは、私の料理を食べてくれたときと、同じ表情を浮かべていた。"

    "でも、それでも。"

    show rnk uni arm nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「私はⅣを――指名する」"

    "私はこの言葉を、口にしなくてはならなかった。"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「承りましたわ」"

    "そしてパルカは、他の参加者にも指名をするかどうかを問い掛けた。"

    if flags_route_A:


        "オデットさんの番を通り過ぎたとき、思わずひやりとした。"

        "金曜日の夜、私が勇気を出さなければ、今頃私は指名されていたのだ。"

        "結局、時計の針は私以降止まることなく一周した。"

        "今夜指名を行うのは、私だけだ。"

        scene bg fatalhall01 up large
        show dia sta fro gl2 big at std_c
        with dissolve

        voice get_voice_filename("dia", 157)
        parca "「それではこれより、Ⅰ番サマによるⅣ番サマのご指名を開始いたしますわ」"

        "女神の声と同時に、私の立つ床が動き始めた。"

        "それは、ユウの乗っている床も同じだ。"

        "互いの床だけが天井のないこの空間の上層へ向かって浮遊し始めた。"

    if flags_route_B:


        hide rnk
        hide yuu
        show ode sta arm ser ci at ci_r
        with std_swap

        voice get_voice_filename("ode", 412)
        odette "「あたしの番だ」"

        "オデットさんの番になった時、彼女は自分からそう言い出した。"

        show mhr uni sco vig rev ci at ci_l with ci_in

        voice get_voice_filename("mhr", 393)
        miharu "「……何だって？」"

        show dia sta fro glo ci with ci_change

        voice get_voice_filename("dia", 158)
        parca "「Ⅺ番サマ。指名をどうぞ」"

        show ode sta gra gla ci with ci_change

        voice get_voice_filename("ode")
        odette "「Ⅰ番だ。そいつを指名させてもらう」"

        "私は、黙って頷いた。"

        "怖かった。"

        "私はユウの指名を終えたあともう何分もすれば、自分が指名される。"

        "その覚悟はしてきたつもりだったけれど、やっぱり怖かった。"

        "私の奥底に眠る炎の記憶に、戻らなくてはならないのだから。"

        show mhr uni pai ten rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「凛火……凛火。ちょっと待ってくれ。どういうことだい？　なぜ君が……指名されているんだ？」"

        hide ode
        show rnk uni nor apo ci at ci_r
        with ci_swap

        voice get_voice_filename("rnk", 1086)
        rinka "「黙っててごめんね、海晴」"


        play music audio.growapart

        "私は、海晴の名前を呼んだ。"

        "海晴のカードはみんなが知っているから、名前を呼んだって大丈夫だろう。"

        show mhr uni pai irr rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「謝らなくていい……そんなのいらないよ」"

        show rnk uni arm nor ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「……後は、お願いね」"

        show mhr uni pai cry rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「ちょっと待ってくれ！　取り消してくれ！　どうして凛火が！」"

        hide rnk
        show ode sta arm smi ci at ci_r
        with ci_swap

        voice get_voice_filename("ode")
        odette "「女神サマよぉ、取り消しってのはできるのかい？」"

        show dia sta fro nor ci with ci_change

        voice get_voice_filename("dia")
        parca "「いえ。ワタクシはもう、貴女サマからⅠ番サマへのご指名を承ってしまいましたわ」"

        show ode sta arm ser ci with ci_change

        voice get_voice_filename("ode")
        odette "「……だ、そうだ。ま、取り消すつもりもないがな。嬢ちゃん自身が受け入れたことだ」"

        hide ode
        show rnk uni arm lie ci at ci_r
        with ci_swap

        voice get_voice_filename("rnk")
        rinka "「そういうことなんだ。海晴なら……分かるよね」"

        "私は、溢れ出る感情を必死に抑えていた。"

        "私が取り乱したら、きっと海晴はもっと辛い。"

        show rnk uni arm sad ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「私自身が決めたこと。直未を取り戻すためには、こうするしかなかったんだ」"

        show mhr uni pai cry rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「嫌だ……そんなの嫌に決まっている！」"

        show rnk uni arm lie ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「……直未のこと、お願いね。７週間前に遡ったら、直未との関係がどうなっているか分からない。でも……きっとまた、友達になってあげてね」"

        show rnk uni arm sad ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「真央のことは……大丈夫か。なんだかんだ言っても、私よりもずっと、海晴の方が真央のことを分かってるもん」"

        show mhr uni pai cry rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「嘘だ……凛火！　どうして！　ぼくは、ぼくは……！　女神！　どうにかしてくれ！」"

        "海晴の声に応えることもなく、パルカはアランさんへも指名の意志確認を行った。"

        show rnk uni nor smi ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「３人で仲良く……するんだよ？」"

        "海晴もまた、私の質問には答えなかった。"

        show dia sta fro cl2 ci with ci_change

        voice get_voice_filename("dia")
        parca "「それではこれより、Ⅰ番サマによるⅣ番サマのご指名および、Ⅺ番サマによるⅠ番サマのご指名を開始いたしますわ」"

        "女神の声と同時に、私の立つ床が動き始めた。"

        "それは、ユウの乗っている床も同じだ。"

        show mhr uni pai ten rev ci with ci_change

        voice get_voice_filename("mhr")
        miharu "「凛火、凛火、凛火、凛火、凛火……」"

        "海晴の声は、徐々に遠くなっていった。"











    python:
        set_info_scene("110")
        set_info_location("16")

    stop music fadeout 1
    scene bg fatalhall02 normal with fade_long
    play music audio.fatalhall
    pause 1

    "不思議な感覚だった。"

    "私の乗った床は、まるでエレベーターのように上昇をする。"

    "私の周りに壁はなく体がさらされているのに、不思議と落ちてしまいそうという恐怖はなかった。"

    "落ちることが想像できないくらい、床の上昇は安定していたのだ。"
    "床が停止したとき、そこは今までとは違った空間だった。"

    "まるで、雲の上にいるようだ。"

    "下を見ても、遥か闇。"

    "下層にいる海晴たちの姿は一切見えなかった。"

    "私の向かいには、ユウがいた。"

    scene bg fatalhall02 up with dissolve

    if flags_route_A:


        show yuu sta nor nor rev ci at ci_l with ci_in

        voice get_voice_filename("yuu", 353)
        yuu "「ボクを殺してくれるんだね、お姉ちゃん」"

        show rnk uni nor apo ci at ci_r with ci_in

        voice get_voice_filename("rnk", 1093)
        rinka "「……うん」"

        show yuu sta lau lau rev ci with ci_change

        voice get_voice_filename("yuu")
        yuu "「ボクを苦しみから、やっと解き放ってくれる！」"

        show rnk uni nor apo ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「そうじゃない。あなたを救えるのは、あなたしかいない」"

        show dia sta fro nor ci at ci_c with ci_in

        voice get_voice_filename("dia", 161)
        parca "「お待たせいたしましたわ。それでは、指名を始めましょう」"

        show yuu sta war cla rev ci with ci_change

        voice get_voice_filename("yuu")
        yuu "「待って！　ねえ、お姉ちゃん！　それはどういう意味……？　ボクは！　お姉ちゃんに殺されて！　それで……！」"

        scene bg fatalhall02 normal with dissolve

        "私は女神がうながすのに従って、カードブックを開いた。"

        "私の持っているすべてのカードが、空中へと現れた。"

        "必要なのは、そのカードを順番に選び取ること。"


        play music audio.electing
        scene ecg senteirinka gentle with dissolve_long


        voice get_voice_filename("rnk")
        rinka "「氏名、ユウ。牛塚さんがあなたに与えた、大切な名前。すごく……素敵な名前」"


        voice get_voice_filename("rnk")
        rinka "「死因、焼死。私の運命と奇妙に絡み合っていた、あなたの死因。正直言って、恨んでる。でも今となってはもう、悲しいだけだね」"

        "私は続けて、≪氏名≫と≪死因≫を選んだ。"


        voice get_voice_filename("rnk")
        rinka "「いい加減、自分で自分を許してあげて」"


        voice get_voice_filename("yuu")
        yuu "「えっ……？」"


        voice get_voice_filename("rnk")
        rinka "「直未の命を奪ったあなたを、私は許してあげることはできない。でもね、あなたが否定をしたら、あなたを許す人は誰もいないよ」"


        voice get_voice_filename("rnk")
        rinka "「あなたは……人形なんかじゃない。英雄にも、なれっこないよ」"


        voice get_voice_filename("rnk")
        rinka "「でもね、それでもあなたは人間だ」"

        "それは、今私が言える精一杯の言葉だった。"

        "あの日。"

        "電車で爆破テロが起こったときに聞いた私の言葉を、彼はずっと覚えていた。"

        "ゆえに、彼自身の過去と一緒に、彼は自分を否定し続けるほかなかったのだ。"


        voice get_voice_filename("rnk")
        rinka "「私も、生まれてすぐ両親を亡くしたんだ。だからもしかしたら、あなたのことをもっと理解してあげなきゃいけなかったのかもしれないけど」"


        voice get_voice_filename("rnk")
        rinka "「……無理だった。あなたと私は違い過ぎたから。私が色んな人に色んなものを与え続けられて育った反面、あなたは色んな人に色んなものを奪われながら育った」"


        voice get_voice_filename("rnk")
        rinka "「にもかかわらず――牛塚さんと出会って、与えられる幸せを知ってしまった。可能性を見せられてしまった」"


        voice get_voice_filename("rnk")
        rinka "「あなたの未練、普通の日常という可能性を。その普通はあなたにとってではなくて、牛塚さんや私の思う普通だった」"

        "私は、３枚目のカードを手にした。"


        voice get_voice_filename("rnk")
        rinka "「だから辛かったんだよね。結果だけ与えられちゃっても、どうやったら普通になれるか分からない。だから、普通を否定することしかできなかった」"

        scene ecg senteirinka gentle large at align(0.45, 0.15) with dissolve


        voice get_voice_filename("rnk")
        rinka "「ユウ。あなたのことは、忘れないよ」"


        scene bg fatalhall02 up
        show yuu sta nor nor rev ci at ci_l
        with dissolve_long

        voice get_voice_filename("yuu")
        yuu "「ボクたちは、絶対に理解し合うことはできない。その理由が今、分かったよ。ボクたちの始まりは、同じだったんだね」"

        show yuu sta nor sad rev ci with ci_change

        voice get_voice_filename("yuu")
        yuu "「残酷だね。あんまりに」"

        show yuu sta nor que rev ci with ci_change

        voice get_voice_filename("yuu")
        yuu "「でも、最後に人間として死ねる。これって普通のことだよね？」"

        show rnk uni arm nor ci at ci_r with ci_in

        voice get_voice_filename("rnk")
        rinka "「……うん」"

        scene ecg trianglecard small with dissolve_long

        "私の選び取った３枚のカードは、ひとりでに動き始めた。"

        "大広間の中心で三角に並び、そこで動きを止める。"

        show ecg trianglecard cover with ecg_change_wait

        "やがてカードのまとった光が、一気にこの空間を埋め尽くすほどに増幅した。"


        voice get_voice_filename("yuu")
        yuu "「ああ、よかった。ボクを殺してもらう相手に、お姉ちゃんを選んで」"

        "奇しくも、私たちの未練の言葉は同じだった。"

        "普通の日常。"

        "けれども言葉は同じでも、意味するものは全く違っていた。"

        "知っているものと、知ってしまったもの。"


        voice get_voice_filename("yuu")
        yuu "「お姉ちゃんが相手なら、恨みながら死ねるから」"


        voice get_voice_filename("rnk")
        rinka "「……お互い様だよ」"




        scene white with Dissolve(3)
        pause 1

        "私たちは、カードから放たれた光に包まれた。"

        "思わず目をつぶると、私の意識だけが浮遊し始めた。"


        voice get_voice_filename("yuu")
        yuu "「……たくない！」"

        "浮遊感の中で、声を聞いた。"


        voice get_voice_filename("yuu")
        yuu "「死にたくない！　ボクは死にたくないよ！」"


        voice get_voice_filename("yuu")
        yuu "「暮らせたかもしれないのに！　普通になれたかもしれないのに！」"


        voice get_voice_filename("yuu")
        yuu "「死にたくないっ……死にたくないっ……」"


        voice get_voice_filename("yuu")
        yuu "「嫌だっ、嫌だっ、嫌だっ……」"


        voice get_voice_filename("yuu")
        yuu "「お姉ちゃんっ、おじいちゃんっ……、ママっ……」"


        voice get_voice_filename("yuu")
        yuu "「死にたくないよぉ……」"


        voice get_voice_filename("yuu")
        yuu "「もっと、もっと、ボクの未来は……っ」"


        voice get_voice_filename("yuu")
        yuu "「うわああああっ」"

        "声は、少しずつ遠ざかっていく。"

        "私は彼の叫びを、ただ無心で受け止めていた。"

        "最後の最後で、私は彼の本音を聞いた。"

    if flags_route_B:



        play music audio.electing

        show yuu sta nor nor rev ci at ci_l with ci_in

        voice get_voice_filename("yuu", 371)
        yuu "「お姉ちゃんも……指名されちゃったんだね」"

        show rnk uni arm sad ci at ci_r with ci_in

        voice get_voice_filename("rnk", 1109)
        rinka "「大切な人を……取り戻すためには必要だったんだ」"

        show yuu sta war war rev ci with ci_change

        voice get_voice_filename("yuu")
        yuu "「……謝らないよ。だって元はと言えば、５回目の選定でボクを指名してくれればよかったんだから」"

        show rnk uni arm vig ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「謝罪なんていらない。謝られたら、怒ってるよ。私は迷ったけど」"

        show dia sta fro smi ci at ci_c with ci_in

        voice get_voice_filename("dia", 162)
        parca "「あらためまして、ごきげんよう」"

        "時間差で、女神の声がした。"

        "女神は音もなく、この不思議な空間に現れていた。"

        "女神は、不敵な笑みを浮かべる。"

        show dia sta nor ama rev ci with ci_change

        voice get_voice_filename("dia")
        parca "「皮肉なものですわね」"

        show rnk uni nor nor ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「――何が？」"

        show dia sta fro gl2 ci with ci_change

        voice get_voice_filename("dia")
        parca "「いいえ。それでは始めてくださいませ。方法は簡単ですわ」"

        scene ecg trianglecard small with dissolve_long
        pause 2
        show ecg trianglecard cover with dissolve
        pause 1

        "そして私は、女神の言う通りに３枚のカードを宣言した。"

        "あまり感情は湧かなかった。"

        "だって同じやり方で、これから私が死ぬのだから。"










    stop music fadeout 2

    if flags_route_B:
        scene white with Dissolve(3)
        play music audio.death
        pause 2

    if flags_route_A:
        play music audio.death

    scene ecg yuuburn non with dissolve_longest

    "炎の中にいた。"

    "見覚えのある光景だ。"

    "だってこれは、私の死の風景とほとんど同じなのだから。"

    "私よりも僅かに視線が低い。"

    "直感で分かった。"

    "これは、ユウの視点だ。"

    "私の喉を潰した後、少年は座り込んだ。"


    voice get_voice_filename("yuu", 373)
    yuu "「……ボクは、人間だ」"

    "すでに、彼の肺は焼かれていた。"

    "皮膚も焼けただれ、彼の細胞のほとんどは死滅していた。"


    voice get_voice_filename("yuu")
    yuu "「……そしてボクは、英雄になった」"

    "ユウの言葉は、虚しく響くだけ。"


    voice get_voice_filename("yuu")
    yuu "「これで……よかった」"

    "呼吸をしても、彼の酸素は血液で運ばれない。"

    "そもそも息を吸い込んでも、空気が肺に届かない。"


    voice get_voice_filename("yuu")
    yuu "「よかったんだよね……ママ……」"

    "彼の言葉は、言葉になっているのかも怪しかった。"

    "彼は人生最期の呟きを、ただ精神力だけで行っていた。"

    "確かめるように。"

    "安心するために。"


    voice get_voice_filename("yuu")
    yuu "「…………れで、本当の……」"

    "しかし、それもすぐに限界がくる。"


    voice get_voice_filename("yuu")
    yuu "「……んなの、嫌…………」"

    "機能を停止させてしまった肺では、もう喋れない。"


    voice get_voice_filename("yuu")
    yuu "「……嫌だ……嫌だ……嫌だ嫌だ……だ…………嫌……」"

    "だから、この言葉が彼の最期の言葉。"

    "後悔と懺悔の入り混じった、焼けただれた叫びだった。"

    "そしてそのまま、視界は真っ赤に染まっていく。"

    "その炎は、彼の抱えた矛盾も業も、全て無慈悲に焼き払った。"









    stop music fadeout 2
    scene bg fatalhall02 up with fade_longest
    play music audio.electing
    pause 1

    show rnk uni arm sad ci at ci_r with ci_in

    voice get_voice_filename("rnk", 1112)
    rinka "「今のは……ユウの死の映像……」"

    "私の向かいには、すでにユウの姿はなかった。"

    if flags_route_A:


        "ユウが私へ最期に遺したのは、恨み節だった。"

        "でも、それくらいの方が清々しい。"

        "だって私は、彼の持っていないものを、欲しかったものをたくさん持っていたのだ。"

        "清々しいはずなのに、私は拳を強く握っていた。"

        "せめて願うのは、もし死後の世界なんてものがあるとしたら、そこでは、女神の選定期間中のことが≪なかったこと≫になっていないように――ということだった。"

        "彼にとっては、その方が辛いかもしれない。"

        "私たちにとっての≪普通の日常≫を知っている方が、悩んでしまうかもしれない。"

        "だけど、せめてその場所が自由な場所であれば、きっと大丈夫だろう。"

        show rnk uni nor apo ci with ci_change

        voice get_voice_filename("rnk", 1113)
        rinka "「天国なんて、神様なんて信じていないのにな……」"

        show dia sta nor ama rev ci at ci_c with ci_in

        voice get_voice_filename("dia", 165)
        parca "「あら？　ここに女神はいますわよ？」"

        show rnk uni arm vig ci with ci_change

        voice get_voice_filename("rnk")
        rinka "「……黙っててよ」"

        show dia sta nor smi rev ci with ci_change

        voice get_voice_filename("dia")
        parca "「恐ろしいですわねぇ。それでは、Ⅳ番サマの持っていたカードをあなたにお見せします。どれを自分のものとするか、下層へ戻るまでに考えてくださいませ」"

        "感傷に浸る間もなく、私の乗った床が動き出した。"

        "これで、直未を取り戻すことができる。"

        "そう思っても、心に浮かぶのはやるせなさだけだった。"

    if flags_route_B:


        show dia sta nor no2 rev ci at ci_c with ci_in

        voice get_voice_filename("dia", 167)
        parca "「さて、貴女サマはそのままでいてくださいませ」"

        hide dia with ci_out

        "間髪入れずに、パルカの声が聞こえた。"

        "しばらく待つと、私の正面にオデットさんが現れた。"


        show ode sta nor nor rev ci at ci_l with ci_in
        voice get_voice_filename("ode", 416)
        odette "「よぅ。嬢ちゃんの友達に散々罵倒されちまったよ。てめーがいなくなっちまって、あいつは大丈夫なのか？」"

        show rnk uni arm nor ci with ci_change

        voice get_voice_filename("rnk", 1115)
        rinka "「意外と優しい。でも心配無用だよ。だって……海晴は強いから。あなたには、負けないよ」"


        voice get_voice_filename("ode")
        odette "「気に食わねぇぜ。女神サマよ、指名を始めてもいいかい？」"

        show dia sta nor nor ci at ci_c with ci_in

        voice get_voice_filename("dia")
        parca "「かしこまりましたわ」"

        "そう言うと、オデットさんはカードブックを広げた。"

        "そこから、３枚のカードを選び取る。"


        play music audio.electing
        scene ecg senteiodetto nor with dissolve_long


        voice get_voice_filename("ode")
        odette "「氏名、獅子舞凛火。死因、窒息死……万が一あたしのカードを揃えている可能性もあると思ったが、なさそうだな」"

        "オデットさんは、指名の防御のことを言っているのだろう。"

        "私の心中は、むしろ下層にいた時よりも穏やかだった。"

        "なかったことになっている記憶の底から、私自身の死の映像が脳裏に浮かんでいた。"

        "私は本当は、すでに死んでいるのだ。"

        "だからこそ、こんな気持ちでいられるのだろう。"

        "束の間の希望だったけれど、最後に直未のために死ぬことができる。"

        scene ecg senteirinka receive with dissolve


        voice get_voice_filename("rnk")
        rinka "「海晴は、こんな気持ちだったのかな」"

        "だったら、駄目だ。"

        "穏やかなのに、涙は止まらなかったから。"


        voice get_voice_filename("ode")
        odette "「ったく、やりにくい。未練、普通の日常。当たり前のものがてめーの未練、か。ある意味てめーらしいんだろうな」"

        "オデットさんは舌打ちをしてから、私の≪未練≫を告げた。"


        voice get_voice_filename("rnk")
        rinka "「……ごめんね、直未。ごめんね……真央。ごめんね……海晴」"

        "私は、もう死ぬ。"

        "これが、終わりだ。"


        voice get_voice_filename("rnk")
        rinka "「ごめんね……おばあちゃん」"

        "こんな不孝を、許して欲しい。"

        "結局私はこの瞬間まで、逃げていた。"

        "私は、自分の死なんて受け入れることはできないのだ。"

        "だから考えないようにして、逃げてきた。"

        "感情の堤防はもう、決壊していた。"

        "でも、それでいい。"

        "だってこれで本当に。"

        scene ecg senteiodetto dow with dissolve


        voice get_voice_filename("ode")
        odette "「……じゃあな。つまらなくはなかったぜ、嬢ちゃん」"

        "終わり。"

        $ renpy.end_replay()
        $ add_seen_chapter("7_3-4")

        $ persistent.sentei7B_clear = True
        $ grant_achievement("divine_selection_07")

        jump fBAD_01





    show rnk uni arm sad ci with ci_change

    voice get_voice_filename("rnk", 1119)
    rinka "「カード、全部持ってる……」"

    "パルカはカードを選ぶようにと言ったけれど、ユウの所持カードは全て脱落者のものか、私の持っているものだった。"

    "Ⅱ・氏名とⅨ・氏名だ。"

    "それこそ海晴のカードと、スケール・ジョーンズさんのカード。"

    "ユウがいかに選定に興味がなかったかというのが分かる。"

    "こうして、私の初めての指名は終わった。"

    "案外あっけないもので、結果としては背中に抱える重みが増えただけだった。"

    $ set_info_location("07")

    scene bg fatalhall01 up large with fade_long
    pause 1

    show dia sta fro nor big at std_c with std_in

    voice get_voice_filename("dia", 169)
    parca "「それでは、今宵の脱落者は１名。これをもって、選定を終了といたしましょう」"

    "私は、誰もいなくなったⅣの場所を見つめていた。"

    "そこだけではない。"

    "牛塚さんのいたⅤ。"

    "桂子さんのいたⅧ。"

    "ソーニャのいたⅩ。"

    "名前も知らない誰かがいたⅥ、Ⅶも。"

    "その全てに、想いを馳せていた。"

    $ renpy.end_replay()
    $ add_seen_chapter("7_2-4")

    $ persistent.sentei7A_clear = True
    $ grant_achievement("divine_selection_07")

    jump f008
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

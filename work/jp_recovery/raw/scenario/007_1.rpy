

label f007_1:








    python:
        set_info_scene("85")
        set_info_date(6, 11, "mon")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom rain with fade_longest
    play music audio.rain
    pause 1

    $ show_hud()

    "月曜日になったらしい。"

    "今日も天気は雨だった。"

    "学校は――行かなくていいか。"

    "そもそも、今日は臨時休校だったか。"

    "もう、何でもいいか。"

    "脳裏に、直未の微笑んだ顔が浮かぶ。"

    "ライオン館で一緒にコーヒーを淹れた香りを思い出す。"

    "クッキーのほのかな甘さが蘇る。"

    "全て私が、壊した。"

    "私は布団を被ることで、その全部から逃げた。"

    "インターホンが鳴ったのを、私は無視をした。"

    "スマホに着信があるのも、無視をした。"

    "動く気力はもう、一切湧かなかった。"

    "これからの人生なんてもう、どうでもいい。"

    "女神の選定なんてもう、私にとっては終わったも同然だ。"

    "今週でも来週でも、私を脱落させればいい。"

    "海晴に頼んでも、無駄だ。"

    "アランさんなら、私を脱落させてくれるかな……。"

    scene bg myroom rain large at align(0.0, 0.3) with dissolve



    voice get_voice_filename("mao")
    mao "「りーーたぁーーーーーん！」"

    "雨音に混ざって、聞き慣れた声が窓の外から聞こえた。"

    "外から２階に聞こえるのだから、かなり大きな声を出しているのだろう。"

    "だから、何だって言うんだ。"

    "私は再び、心を閉ざした。"



    voice get_voice_filename("mao")
    mao "「ちゃんとお別れしなきゃ……駄目だよぅ……」"

    "だが、人として最低になるぎりぎりのところで、私は窓を開けることができた。"






    python:
        set_info_time("noon")
        set_info_location("33")


    stop music fadeout 1
    scene ecg funeral with fade_long
    play music audio.despair
    pause 1

    $ show_hud()

    "私は無理矢理に体を動かして、都内のセレモニーホールへと足を運んでいた。"

    "直未の両親や親族にどんな声をかけていいかは分からなかったが、お悔やみの言葉をかけたと思う。"

    "来てみれば、無気力ではない方の私が、自然と最低限の行動をしてくれた。"


    voice get_voice_filename("mao")
    mao "「ぐすっ………」"

    "真央が来てくれなかったら、私は日辻直未の葬式に参列してはいなかっただろう。"

    "ここは、お別れの場なのだ。"

    "いくつもの涙の粒が、溢れていた。"

    "私も例外ではない。"

    "不思議な気持ちだった。"

    "心が二つに分裂した気分だ。"

    "悲しむ私と、虚ろ過ぎて冷静になっている私。"

    "この瞬間は、雨音よりもすすり泣く音の方がよっぽど大きかった。"

    "飴茶の制服を着た生徒がたくさんいた。きっと、直未の同級生だろう。"

    "学校が始まってから２ヵ月とちょっとでこんなに来てくれるのは、文化祭の準備を誰よりも頑張っていたからだろう。"

    "直未の素直さが、みんなを変えたのだ。"

    "だけどよりにもよってその文化祭で、直未は命を落とした。"

    "私に涙する権利はあるのだろうか。"

    "私が女神の選定に巻き込まなければ、直未は死ななかった。"

    "私が文化祭の相談を受けるために、ライオン館へ呼ばなければ、直未は死ななかった。"

    "あの日図書室で声をかけなければ、直未は死ななかった。"

    "――直未は死ななかった。"

    "――直未は死ななかった。"

    "――直未は死ななかった。"

    "私が、死ねばよかったのに。"

    "後悔はきっと永遠に終わることはないだろう。"

    "たくさんの悲しみが、行き場をなくしていた。"

    "若過ぎる死は、早過ぎる死は、悲しみという言葉では安過ぎる。"

    "今この光景が夢であればいいと、誰もが思っていることであろう。"

    "現実から直未という存在が引き剥がされてしまったことに、誰もが実感を持ててはいないだろう。"

    "眼前で直未の死の瞬間を見せつけられた私ですら、現実だと受け入れることができないんだから。"

    show ecg funeral tear

    "どうしてこれが、現実なんだ。"

    "この現実が運命だと言うのなら、私は運命なんて嫌いだ。"


    voice get_voice_filename("rnk")
    rinka "「直未、直未ぃ……」"

    "気付けば２人の私は一人になっていた。"

    "感情を抑えることができず、人目をはばからず嗚咽していた。"


    voice get_voice_filename("mao")
    mao "「なおりん、なおりん……うちだって悲しいよ……ううん、悲しくない人なんていない…………」"


    voice get_voice_filename("mao")
    mao "「うっ……うっ……ううっ…………」"


    voice get_voice_filename("rnk")
    rinka "「直未ぃっ……うわああっ、うわぁぁっ……」"


    voice get_voice_filename("mhr")
    miharu "「凛火……ぼくは……」"



    scene black with dissolve

    "程なくして、日辻直未の告別式は終わった。"

    "私は帰宅するやいなや、何も食べることができずにベッドへ倒れ込んでいた。"

    $ add_seen_chapter("7_1-1")








    python:
        set_info_scene("86")
        set_info_date(6, 12, "tue")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom rain with fade_longest
    play music audio.rain
    pause 1

    $ show_hud()

    "私は何時に寝たかも分からないし、何時に起きたのかも分からなかった。"

    "一抹の空虚さを覚えていた。"

    "夢では、直未との想い出をたくさん見た。"

    "目覚めてしまえば何のことはない、全てただの過去。"

    "過去に向く未練を、私はたった今、真の意味で理解することができた。"

    "学校のこと。"

    "ようやく、爆弾テロの疑いで本格的に捜査が入るらしい。"

    "臨時休校は一週間に延長された。"

    "立ち上がるのにすら一日分の気力を使うような状態の私にとって、それはありがたかった。"

    "こんな時こそおばあちゃんに頼ろうとしたが、何の因果か、おばあちゃんの介護中の親戚が土曜日の夜に倒れてつきっきりの状態らしい。"

    show rnk mos nor hol at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「独りで」"

    "私は今日も、ただ無気力に転がるだけだった。"








    python:
        set_info_scene("87")
        set_info_time("noon")
        set_info_location("30")


    stop music fadeout 2
    scene bg schoollibrary with fade_longest
    play music audio.miharu
    pause 1

    $ show_hud()

    "未島海晴の行動は、獅子舞凛火とは対照的であった。"

    "失意の凛火の表情を見て、海晴はすでに決意を固めていたのだ。"

    "疎ましく思っていた直未ではあるけれど、死んで欲しいと思ったことは一度もなかった。"

    show mhr uni pai ten at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「ぼくに、できることをするさ」"

    "飴茶の高等部は休校だったが、中等部と大学は通常授業のため、図書室は空いていた。"

    "海晴は、現状を整理していた。"

    "まず考えなければならないのは、Ⅳ番の少年についてだった。"

    "彼の名前が『ユウ』だということを海晴は知っていた。"

    "凛火が妄言のように繰り返していたのを聞いていたからだ。"

    "そしてそのユウが教室に爆弾を仕掛け、直未を殺害したことも。"

    "理由や目的は分からないが、そのユウは凛火に殺されたがっているらしい。"

    show mhr uni sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「この状況がどうなっているのか、よく分からないよ。日辻さんの死からこっち、さすがのぼくも頭が働いていなかったからね」"

    "ようやく選定のことを考えられるようになったのが今日であった。"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「残念ながら、ぼくだけでは凛火の笑顔を取り戻せない」"

    "ユウの素性も何もかも、海晴はまだ分かってはいなかった。"

    "だが調べなくてはならないと、海晴はすでに決意していた。"

    "凛火のために命を捧げる――その言葉に偽りはない。"

    "偽りにしてはいけないのだと、海晴は固く決めていた。"

    "それは、決して軽いものではない。"

    "凛火の笑顔を守れなかったら、意味がないのだ。"

    show mhr uni sco far with std_change

    voice get_voice_filename("mhr")
    miharu "「大事なことを見落としていたよ……くすっ。それに気付かせてくれたのだから、必ず君にもお礼を言わないといけないね――日辻さん」"

    "凛火以外の参加者で海晴が持っているカードは決して多くはなかったし、まばらでもあった。"

    "海晴自身は頭脳明晰であるけれど、あくまで一介の女子高生である。"

    "信頼できる情報網など持っていないから、新聞や本、インターネットで情報を集めるほかないのだ。"

    "Ⅳ――ユウの氏名。"

    "Ⅸ――６度目の選定で初めて口を開いた男性の未練。"

    "Ⅻ――アランの氏名。"

    "そしてⅫの、死因。"

    "凛火と自分、脱落した参加者のカード以外で所持しているのはこれらの情報だった。"

    "他にも、Ⅺの未練にもおおよその見当がついていたが、まだカード化するには至っていなかった。"

    "有用そうなのは、すでに３名を脱落させているアランのカードだ。"

    "しかし、その未練はまだ手掛かりもない。海晴はアランと直接会ったこともないのだ。"

    "とはいえ有名人であるアランは、テレビに出演したり雑誌のインタビューを受けたりしているから、まだ調べようがある。"

    "インド人とはいえ南インドで主要言語が英語の地域の出身らしい。"

    "英語なら分からない単語を調べながら自分で翻訳することができる。"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「ユウのことは気になるけど、まだ情報がなさすぎる」"

    "海晴は優先順位をつけ、調べ物を始めることにした。"

    "決意は固いが、大局を見誤ってはいけないという考えだ。"

    "海晴は独りで黙々と、調べ物を続けるのであった。"







    python:
        set_info_time("evening")
        set_info_location("14")


    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    play music audio.gimon
    pause 1

    $ show_hud()

    "海晴が校門から出ようとした時、門の横に見知らぬ男性のシルエットを見つけた。"

    "一度足を止め、その男性から距離を取るために大回りをした。"

    show sca sta nor gre rev at std_cl with std_in


    voice get_voice_filename("sca")
    scale_unk1 "「やあやあ、元気かい？」"

    "だが海晴に気付いた男性の方から声をかけてきた。"

    "海晴は警戒心を強めて何も応えず、彼が近付いてくるのを待った。"

    "彼の顔には見覚えがあったからだ。"

    "運命の大広間で見かけ、直近の選定まで一言も発しなかったⅨの男。"

    show sca sta nor gre rev with std_change


    voice get_voice_filename("sca")
    scale_num "「怖がっているわけじゃ……なさそうだ。そうだなぁ。動揺していないアピールでもしてるって感じかな？」"

    show mhr uni nor ser at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「どちらでも構わないよ。ぼくの名前から場所を特定――はできないはずだ」"

    "蛇鉈海晴という人間は、いまや存在しない。"

    "詳しく調べれば飴茶女子高校の未島海晴と同一人物だということに辿り着くかもしれないが、容易ではない。"

    "とすれば、彼が待っていたのは凛火かもしれない。凛火の≪氏名のカード≫が初期に配られていたのだろうか。"

    "いや、それは違う――海晴は気付く。"

    "≪Ⅰ・氏名≫を持っていたのはすでに脱落したⅧの女性のはずだ。"

    "彼女を脱落させたのはⅫのアランであり、この男性が凛火のカードを持っているのはおかしいということから、海晴は別の予想を立てた。"

    show mhr uni sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「もしかして君は、ぼくの≪未練≫を持っているのではないかい？」"

    show sca sta nor lau rev with std_change


    voice get_voice_filename("sca")
    scale_num "「ＨＡＨＡＨＡ、そこまで察しがいいと損の方が多いんじゃないかな？」"

    show sca sta nor smi rev with std_change


    voice get_voice_filename("sca")
    scale_num "「君の未練には驚かされたけれど、そのおかげでこの高校を特定することができたのさ」"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「とはいえ、今はそのリンカ・シシマイとは仲違いしているようだけど」"

    $ add_character_cards("sca", ["1_name"])

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「選定初期に君たちが知り合いだということは分かっていたからね。この飴茶女子高校に在籍している生徒を調べさせてもらった」"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「ミハル・ヘビナタという生徒はいなかったけれど、ミハルという生徒がいた。顔を見れば一発で分かるさ」"

    show mhr uni sco wic with std_change

    voice get_voice_filename("mhr")
    miharu "「一体何をご所望しているのかな？　凛火とはすでに決別しているけど、他の参加者に情報を教えるつもりはないよ」"

    show sca sta nor joy rev with std_change


    voice get_voice_filename("sca")
    scale_num "「分かってるよ。おれがリンカを脱落させたら、君の情報を知られるリスクがあることくらい」"

    show mhr uni nor vig with std_change_wait

    "海晴は反射的に、彼を睨んでいた。"

    "凛火の脱落というのは、聞き過ごせることではなかったのだ。"

    "だが、彼はそれを別の意味でとったらしい。"

    show sca sta nor smi rev with std_change


    voice get_voice_filename("sca")
    scale_num "「おっと。勘違いはしないでくれよ。おれは今のところ君を脱落させる気はないんだ」"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「おれは君と交渉をしに来たのさ。君は一度Ⅺの女性を出し抜いたことがあったよね？」"

    show sca sta nor lau rev with std_change


    voice get_voice_filename("sca")
    scale_num "「それを見込んだんだ。ＨＡＨＡＨＡ、意味が分かるね？」"

    show mhr uni sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「まさかとは思うけれど、協力を持ちかけているのかな？　でも、どうして今なんだい？」"

    show sca sta nor joy rev with std_change


    voice get_voice_filename("sca")
    scale_num "「おれは状況を静観していたんだ。放っておけば、ある程度までは人数が減るだろうからね」"

    "海晴も、概ね同じ考えをしていた。"

    "この男性は飄々と話しているが、案外抜け目ないのかもしれない。"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「誰も脱落しない回を待とうと決めていたんだ。膠着状態になったら動き出すとね」"

    show sca sta nor lau rev with std_change


    voice get_voice_filename("sca")
    scale_num "「３回目くらいでそういう機会は来ると思っていたけど、ＨＡＨＡＨＡＨＡ、思ったよりもずっと、女神の選定というのは激しかったようだ」"

    show mhr uni sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「なるほど。君の話は納得できないものではなさそうだ。だけど、まだ君に協力するとは言えないよ」"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「おれの情報を知りたい、とかかな？」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「そうだね。ぼくは君のことを全く知らない。対して、ぼくは君に氏名も未練も握られている」"

    show mhr uni nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「この状態で協力関係というのは、難しいんじゃないかな？」"

    "海晴は、嘘をついていた。"

    "彼の死因だけを、海晴は知っているのだ。"

    "だが、今は彼のことを何も知らないと言う方が、話はうまく運ぶと予想していた。"

    show sca sta nor joy rev with std_change


    voice get_voice_filename("sca")
    scale_num "「おれが正直にミハルの情報を持っていることを明かしたことじゃ不足かい？」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「『≪死因≫さえ調べれば君を脱落させられるぞ』とも聞こえるよ」"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「おや、失礼。そんな意図は全くなかったんだ。とはいえ……おれもさすがに≪自身のカード≫を明かすわけにはいかない」"


    stop music fadeout 1

    show sca sta nor smi rev with std_change


    voice get_voice_filename("sca")
    scale_num "「ここらで、おれの本音を話すということで納得してもらえないかな？」"

    show mhr uni sco vig with std_change

    voice get_voice_filename("mhr")
    miharu "「確約はできないけれど、聞こう」"

    "男性は海晴が半身ながらも一歩近づいたのを見てから、続ける。"


    play music audio.disclose

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「おれは、この選定が間違っていると思っているんだ」"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「君も分かっているだろう？　この選定は、他人を犠牲にすることを厭わない人間が多く混ざっている」"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「相手を脱落させれば選定期間中の行動がなかったことになるのをいいことに、選定の参加者ではない人間に暴力を振るったり、人質にとって脅迫したりというのが横行している」"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「この行為は、悪だ」"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「極めつけは、土曜日の事件だ」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「……知っているんだね」"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「女神の選定との関与を疑わない方がどうかしているだろう？」"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「Ⅳの少年は、無国籍テロ集団――通称≪ＮＵＬＬ≫と関係があるという仮説が出ている」"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「この学校を狙った意味はまだ分かっていないが……人が集まるライブ会場なんかも無差別に狙う連中だ。人さえいればいいのかもしれない」"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「もっともおれは、君たちが飴茶に通っているからこそ、選定参加者への宣戦布告をしたのだと思っているよ」"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「降伏しなければ、こうなると――もっと被害を拡大させるとでも言いたいのかな。夢の世界でⅣの少年はだんまりだから、不気味だ」"

    "海晴は、Ⅸの男性を見る目を大きくした。"

    "ユウという名前以外に、彼の情報に繋がる手掛かりを見つけたからだ。"

    "≪ＮＵＬＬ≫とは、世界の至るところに拠点をもつ国際テロ集団だ。"

    "その実態は明らかになっておらず、ただ名前を騙っているだけの偽物も多いらしい。"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「不幸中の幸い、死者は一人で済んだらしいけど……人数なんて関係ない」"

    show sca sta nor smi rev with std_change


    voice get_voice_filename("sca")
    scale_num "「話が逸れてしまったね。おれが言いたいことはもう分かったかな？」"

    "真剣な表情のまま、彼は続けた。"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「おれは、正義の人がこの選定で生き残らなければいけないと思っている」"

    show sca sta nor ser rev with std_change


    voice get_voice_filename("sca")
    scale_num "「それが君なのか、おれなのか、君の友人のリンカなのかは分からない。だが今までの行動から考えて、その３人以外は考えられないだろう」"

    show sca sta nor gre rev with std_change


    voice get_voice_filename("sca")
    scale_num "「それに君の方がおれよりも生きるべき人間だと判断したら、勝ちは譲るつもりでもいるさ」"

    "話が通じるし、まともな意見だと海晴は頷いた。"

    "もっとも、この男の言い分を全て本音ととるつもりもない。"

    "Ⅲの男性、Ⅳの少年、Ⅺの女性、Ⅻの男性――強敵と見込まれる彼ら４人を脱落させるための方便かもしれない。"

    "だが海晴はもう、彼の理想についてはどうでもいいと思っていた。"

    "彼のあげた３人の中には凛火も入っているのだから、なおさらだ。"

    "何より気にしているのは、一つ――Ⅳの少年の情報を得られるかもしれないということだった。"

    show sca sta nor nor rev with std_change


    voice get_voice_filename("sca")
    scale_num "「どうだい？　おれと、協力関係を結ばないかい？」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「君を全て信用したわけではないけれど、ぼくにとって悪くはないかもしれないね」"

    "海晴は一息ついてから、芝居を続けた。"

    "本当は、今すぐにでもⅣの情報を集めたいと思っているのに。"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「いいよ。君と協力する。ただし――ぼくが関係を破棄した方がいいと判断したら、いつでもそうさせてもらうよ」"

    show sca sta nor joy rev with std_change


    voice get_voice_filename("sca")
    scale_num "「分かった。もちろん、最後まで信用してもらえるよう努力はするけどね。それが落とし所なら、文句は言わない」"


    stop music fadeout 1

    show sca sta nor smi rev with std_change


    voice get_voice_filename("sca")
    scale_num "「早速だが、実は他にも協力者がいてね。ついて来て欲しい」"

    "協力者――選定の参加者以外にもいるということだろう。"

    "彼の素性が分からないので危険ではあるが、ここで断るのは信用を失うリスクもある。"

    "侮れない男ではあるが、いきなり裏切ることはしないだろう。"

    "海晴はそう判断し、念の為スマホの充電が十分にあることを確認してから、男性の後についていった。"






    python:
        set_info_scene("88")
        set_info_time("night")
        set_info_location("34")


    stop music fadeout 1
    scene bg bar with fade_long
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "海晴はスケールに連れられて、新宿歌舞伎町にあるバー≪MILK CROWN≫を訪れていた。"

    "制服で入るのが憚られる場所だが、メイド喫茶でアルバイトをしているからか元々度胸があるのか、海晴は大して臆してはいなかった。"

    "いきなり裏切られはしないだろうと、海晴は思っていた。"

    "しかし、予想を裏切られるのはあまりに早過ぎた。"

    scene ecg barodefed c with dissolve_long



    voice get_voice_filename("ode")
    odette_num "「てめー、他の仲間を連れて来るとは言っていたが……中々ふざけてるじゃねぇか」"



    voice get_voice_filename("fed")
    federico_num "「お、おい！　こいつ……違いねぇよな……」"


    voice get_voice_filename("mhr")
    miharu "「君は……君たちは……」"



    play music audio.badguys
    show ecg barodefed d with ecg_change_wait

    "狭い店内には、客は彼らしかいなかった。"

    "先にいた二人は片方がオーク色、片方が透明なピンク色の液体が入ったグラスを傾けていた。"

    "アルバイト先でもアルコールは提供しているので、片方がウイスキー、海晴は片方が何かのカクテルだと分かる。"

    "もっとも、彼らが何を飲んでいるかなどということは些末な問題でしかなかった。"

    "海晴も先客の二人も、選定とは関係のない人物が来ると思っていたからだ。"


    scene bg bar
    show sca sta nor joy rev at std_c
    with dissolve_long



    voice get_voice_filename("sca")
    scale_num "「後で説明するよ」"

    "スケールは海晴にこう耳打ちをしたが、この時点で海晴は状況をある程度察していた。"

    scene ecg barodefed a with dissolve_long



    voice get_voice_filename("fed")
    federico_num "「おい、スチール！　こりゃどういうことだ！　こいつはミハル・ヘビナタ……オレたちの敵じゃねーのかよ！」"



    voice get_voice_filename("ode")
    odette_num "「うっさいフェデリーコ。ちったあ落ち着けよ」"

    show ecg barodefed c with ecg_change


    voice get_voice_filename("fed")
    federico "「おいいい！　スチールと違ってオレのは本名なんだぞ！　気軽に名前を呼んでんじゃねえぞオデット！」"


    voice get_voice_filename("ode")
    odette "「そいつは失礼したぜ。ムッシュ・カルミナーティ」"


    voice get_voice_filename("fed")
    federico "「オデット、てめえ……」"

    show ecg barodefed e with ecg_change


    voice get_voice_filename("ode")
    odette "「賑やかで悪いな嬢ちゃん。あたしはオデット・マランソンだ」"

    python:
        add_character_cards("mhr", ["3_name", "11_name"])
        add_character_cards("sca", ["3_name", "11_name"])


    voice get_voice_filename("ode")
    odette "「まさかこんなところで会うとは思わなかったが、あたしらはこのスチールって胡散臭い奴から協力関係を持ちかけられたんだ」"


    voice get_voice_filename("sca")
    scale "「あんたたち……一体どういう了見だ？」"


    voice get_voice_filename("fed")
    federico "「オレが聞きてえよ！」"


    voice get_voice_filename("ode")
    odette "「ミハルって言ったな。あの時、あたしはずいぶん驚かされたもんだ」"


    voice get_voice_filename("mhr")
    miharu "「どう答えればいいのか分からないよ。マダム・マランソン？」"


    voice get_voice_filename("ode")
    odette "「その顔じゃ、ずいぶん動揺してるみたいじゃねーか。かかっ、満足だ」"

    show ecg barodefed c with ecg_change


    voice get_voice_filename("ode")
    odette "「これで４度目の時の借りを返せたってところかな。オデットでいい。そこに座りな。ま、まずは話してみないと何も分からないだろ。せっかく来たんだ、一杯くらいおごるぜ？」"


    voice get_voice_filename("mhr")
    miharu "「アルコールは遠慮するよ。ぼくは未成年だからね。そうだな……ならミルクでもいただけるかい？」"


    voice get_voice_filename("ode")
    odette "「日本の高校生ってのは真面目だね。ま、いいだろう」"


    scene bg bar
    show mhr uni sco vig at std_c
    with dissolve_long

    "海晴は心臓の鼓動を速くさせながら、店の中へと移動した。"

    "冷静でいることの多い海晴も、この状況ではさすがに落ち着くことはできなかった。"

    "どう立ち回るのが正解なのかぐるぐると考えて、結論を出せずにいた。"

    "ある程度プロファイリングしていたにもかかわらず、実際に会ってみたオデットいう女性は、全く感情を読むことができなかったのだ。"

    "会話の主導権はスチールという男ではなく、オデットが握っていた。"

    scene ecg barodefed d with dissolve_long


    voice get_voice_filename("ode")
    odette "「ま、これでミハルによく似た女じゃないってことは証明されたか。若干だが、カードブックの光が漏れてたぜ。あたしらの≪氏名のカード≫がちゃんと増えてるはずだ」"


    voice get_voice_filename("mhr")
    miharu "「そのために、あんなことを？」"


    voice get_voice_filename("ode")
    odette "「だけじゃないさ。な、スチールさんよぉ？」"


    voice get_voice_filename("sca")
    scale "「ＨＡＨＡ、ここでおれに話題を振るのかい？」"


    voice get_voice_filename("ode")
    odette "「たった一人しか生きられないこの≪女神の選定≫で協力しようって話をしてんだ。信頼が大事なのは分かるだろう」"

    show ecg barodefed b with ecg_change


    voice get_voice_filename("ode")
    odette "「あたしらは大切な名前をさらしたんだ。勝利条件の一つである名前をな……後は分かるな？　おっと嬢ちゃん、ミルクだ」"




    play music audio.investigation
    scene bg bar with dissolve_long

    "オデットはスチールを問い詰めるような態度は見せなかった。"

    "ただオーク色の液体の入ったロックグラスを傾けながら、平然とした態度で訊ねていたのだ。"

    "海晴は、そんな彼女を測っていた。"

    "ソーニャの話を聞いたときもただ残虐なだけではないと思っていたが、ここまでおしゃべりで豪快だとは思っていなかったのだ。"

    "ミルクを受け取った海晴は、ガムシロップを入れてストローに口をつけた。"

    show sca sta nor joy rev at std_l with std_in

    voice get_voice_filename("sca")
    scale "「オーケーだ。おれの名前も教えよう」"

    show ode sta nor nor at std_c with std_in

    voice get_voice_filename("ode")
    odette "「物分かりが良くて助かるぜ。ここで渋ったら、てめーを次の標的にしなくちゃいけなかったからな」"

    show fed sta nor pa4 at std_r with std_in

    voice get_voice_filename("fed")
    federico "「……ったく、勝手に自分で決めやがって。こいつかミハルがオレたちの情報を持ってたらどうするつもりだったんだ」"

    show ode sta arm ser with std_change

    voice get_voice_filename("ode")
    odette "「そん時はま、次の選定までに嬢ちゃんたちの≪カード≫を集めればいいだけだ。さあ兄ちゃん、てめーの名前を教えな」"

    "男性は小さく息を吸ってから、勿体をつけるような調子でゆっくりと口を開いた。"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「おれはスケール・ジョーンズ。職業やらは内緒だが、血液型はＯ型だ。これでいいか？」"

    python:
        add_character_cards("mhr", ["9_name"])
        add_character_cards("fed", ["9_name"])
        add_character_cards("sca", ["9_name"])
        add_character_cards("ode", ["9_name"])

    show ode sta nor lau with std_change

    voice get_voice_filename("ode")
    odette "「……かかっ、上等だ」"

    scene ecg cardbook bli with dissolve_long

    "海晴の傍らで、カードブックが光を放った。"

    "カードはきちんと生成されているからⅨの男性の本名はスケールだと、海晴もまた確認していた。"


    scene bg bar with dissolve_long

    "オデットはグラスのウイスキーを飲み干すと、おかわりを頼む。"

    "お酒を飲んだことのない海晴も、ウイスキーは40度以上ということを知っていた。"

    "その度数のお酒は臭いからして人間の飲むものと思えない年頃ではあるが、オデットがさらにそれをごくごく飲んでいることには驚愕していた。"



    play music audio.relaxtime
    scene ecg barodefed d with dissolve_long


    voice get_voice_filename("ode")
    odette "「おいフェデリーコ。日本製のウイスキーってのもいけるぜ。お前もどうだ？」"


    voice get_voice_filename("fed")
    federico "「いいんだよ。たまには甘いカクテルも飲みたいんだ。もっとも、この店にはロクなワインがなかったからなんだけどよ」"


    voice get_voice_filename("sca")
    scale "「……おれも何か頂こうかな。強いのを」"

    "スケールは震えた声でそう言うと、海晴の知らない銘柄のお酒を注文した。"

    "しかし安心した顔でお酒を飲むスケールを見て、海晴は飲まなきゃやっていけないという気持ちを少し理解していた。"

    "常人では、オデットのペースについていけない。"

    "彼女の陰に隠れているが、オデットの前で平然としているフェデリーコもまた、異常であると思っていた。"

    "海晴はそう思いながらも、どうにかして自分を保っていた。"

    show ecg barodefed f with ecg_change


    voice get_voice_filename("ode")
    odette "「さ、嬢ちゃん。兄ちゃんにどう言われてここまで来たのかは知らないが、面子を見たらどういうことか察しはつくよな？"


    voice get_voice_filename("fed")
    federico "「性格が悪い奴だ。こいつこうやって、組む価値があるかを値踏みしてるんだぜ」"


    scene bg bar
    show mhr uni sco wic rev at std_c
    with dissolve_long

    voice get_voice_filename("mhr")
    miharu "「忠告ありがとうと言っておこうかな、フェデリーコさん。でも心配いらないよ。ぼくもそれくらいはわきまえているさ」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「スケールさん。この連合は、Ⅳの少年を脱落させるためのものではない」"

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくたちは、目下アラン・スコーピオンの脱落を目的とする――間違いないかい？」"

    python:
        add_character_cards("mhr", ["12_name"])
        add_character_cards("sca", ["12_name"])

    show sca sta nor lau rev behind mhr at std_l with std_in

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡＨＡ、素晴らしい」"

    "スケールは先ほどよりも楽しげな様子でそう答えた。"

    "酔いが回っているのだろうかと、海晴は訝しげな目で彼を見た。"













    $ set_info_scene("89")

    stop music fadeout 2
    scene black with dissolve_longest
    pause 2
    scene bg hotel japan with wfade_longest
    play music audio.investigation
    pause 1





    "６度目の選定のとき、オレとオデットは日本のホテルに滞在していた。"

    show fed sta nor nor at std_cr with std_in

    voice get_voice_filename("fed")
    federico "「初の脱落者なし、だったな」"

    show ode sta nor lau rev at std_cl with std_in

    voice get_voice_filename("ode")
    odette "「珍しいこともあるもんだ。かかっ、あたしらも手詰まりじゃあ仕方ねぇ」"

    "少年に負わされた怪我は、ほとんど治っていた。"

    "もちろん、完治には程遠い。"

    "オレにとっての治ったは、動けるかどうかが判断基準だ。"

    show fed nor nor int with std_change

    voice get_voice_filename("fed")
    federico "「それで、だがよ、Ⅳの少年のカードはどうだったんだ？」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「ああ、あれか。言った通りだよ。あたしの初期カードとして≪Ⅳ・氏名≫は配られたが……なくなっちまった」"

    show ode sta arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「確か、５度目の選定――ジジイが脱落した夜の直前だ。あの時は、アランの奴にも似たようなことが起きてたな。あれは、選定が終わる時だったが」"

    "アラン・スコーピオン。"

    python:
        add_character_cards("fed", ["12_name"])
        add_character_cards("ode", ["12_name"])

    "世界的に有名な宝石商である奴の名前を、オレたちはすでにつかんでいた。"

    "しかしどうにも、氏名以上の情報は分からずじまい。"

    "それぞれの初期カードにも、含まれてはいない。"

    "オデットが言っているのは、カードの消滅の話だ。"

    "運命の大広間でアランはシゲツグを脱落させたあと、≪Ⅴ・未練≫を取得した。"

    "だがそのカードは奴が手に取ろうとした瞬間、ガラスが割れるみたいに砕け散り、光の粒になっちまった。"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「あたしのカードも、アランのカードと同じ消え方をしたんだ。他に何人がⅣのガキのカードを持ってたかは知らないが……≪死因≫以外は消えちまってるんだろうな」"

    show ode sta arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「考えられるのは――その内容が変わったってところだろうな」"

    show ode sta gra gla rev with std_change

    voice get_voice_filename("ode")
    odette "「≪未練≫が変わるってのは理解しかねるけどよ、≪氏名≫が変わるのなんて珍しい話じゃねぇ」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「特にこの≪女神の選定≫っていうのは曖昧な認知の上にルールが成り立ってるからな」"

    show fed nor nor nor with std_change

    voice get_voice_filename("fed")
    federico "「しかし、元々のblankってのは気になるな。名前がないってどういうことだ？」"

    show ode sta arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「それこそ簡単だろ。両親に名前をつけてもらえない状況――たとえば戦争孤児や、過去を捨て名前を捨てたってとこだろうな」"

    show fed nor nor int with std_change

    voice get_voice_filename("fed")
    federico "「過去を捨て――か。確かにオレの世界にもそういう連中は決まってその時々の呼び名をつけられるもんだがな」"

    show fed nor nor pa1 with std_change

    voice get_voice_filename("fed")
    federico "「待てよ！　そういうことか」"

    "自分で答えの一つを口にしていた。"

    "Ⅳのガキは、選定中に呼び名を与えられて、それが自分の≪氏名≫だと認知したわけか。"

    "話しながら考えをまとめる癖がオデットに似てきているようで癪だったが、オデットのしたり顔を見るに、同じ予想をしていたということだろう。"

    show ode sta nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「日本の高校でテロがあったらしい。テロリストってのははぐれ者も少なくない」"

    show ode sta arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「加えてガキってのは警戒されにくい。特にこの日本ではな」"

    show fed nor nor int with std_change

    voice get_voice_filename("fed")
    federico "「無関係とは思えない――ってわけか」"

    "膠着状態ではあったが、着実に事態は動いている。"

    "オレたちが派手に動いていないとき、その裏では別の誰かが活動しているのだ。"

    "そのことを証明するかのように、胡散臭いアメリカ人――スチールと名乗るⅨの男がこのホテルを訪ねて来たのは、この日の午後であった。"












    $ set_info_scene("90")


    scene black with wfade_longest
    pause 2
    scene bg bar with dissolve_longest
    pause 1

    $ show_hud()

    "――アラン・スコーピオンの脱落。"

    "海晴はスケールに対して、はっきりとそう言ってみせた。"




    scene ecg barodefed c with dissolve_long


    voice get_voice_filename("fed")
    federico "「流れとしちゃ、Ⅳのガキを最初の標的にする方が自然だと思うが？」"


    voice get_voice_filename("mhr")
    miharu "「かもしれないね。Ⅳの少年が起こしたテロに挑発の意味があるとすれば、普通だったらそちらに注目するだろう」"


    voice get_voice_filename("mhr")
    miharu "「しかし君たちを見て確信したよ。誰も彼の挑発に乗る気はないと」"

    show ecg barodefed c with ecg_change


    voice get_voice_filename("fed")
    federico "「嫌に鋭い嬢ちゃんだな。付き合うには頭が良過ぎるか……一夜くらいが丁度いい」"

    show ecg barodefed a with ecg_change


    voice get_voice_filename("ode")
    odette "「下らねーこと言ってねーでてめーが見習えってんだ」"


    scene bg bar with dissolve_long

    show mhr uni nor nor at std_cr with std_in

    voice get_voice_filename("mhr")
    miharu "「……続けるよ。今、一番指名回数が多いのはアランだ。取得しているカードも一番多いはずだ。だからこそ、彼を目の上のたんこぶだと思っているぼくたちが結託をする」"

    show mhr uni nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「そういうことだろう、スケールさん？」"

    show sca sta nor nor rev behind mhr at std_l with std_in

    voice get_voice_filename("sca")
    scale "「アラン・スコーピオン。彼が一代で成り上がったインドの宝石商であることは周知の事実だ」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「選定初期に無茶をし過ぎたせいで、彼は日本の警察に目をつけられている。不法侵入に業務妨害……立派な犯罪者だ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「でも彼は、会社を通じてインド政府、そして日本政府とコネクションがあるらしいんだ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「完全にではないけれど、それでも日本警察に圧力をかけてかなりの動きを抑えているらしい」"


    play music audio.badguys

    hide mhr
    show ode sta arm ser at std_cr
    with std_swap

    voice get_voice_filename("ode")
    odette "「それだけじゃねぇ。あいつが最も厄介なのは情報網……だろ？」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「そうだ。つまり彼に名前を知られるということは、自分の素性を知られることに等しい」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「相手がおれだからよかったものの……君たちはもう少し慎重になった方がいいぞ」"

    show ode sta arm irr with std_change

    voice get_voice_filename("ode")
    odette "「嘘つけ。てめーだって立派な情報網を持ってるんだろ？」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「一大企業の社長と比べないでくれよな」"

    show ode sta nor nor with std_change

    voice get_voice_filename("ode")
    odette "「否定はしないんだな。そういうところは嫌いじゃない。まあいい。お互いの≪氏名≫を共有するのはあたしとしちゃ協力関係の最低条件だ」"

    show ode sta gra gla with std_change

    voice get_voice_filename("ode")
    odette "「下手な動きをしようもんなら、{rb}自分{/rb}{rt}てめー{/rt}の首も噛み付かれるってことは分かってるだろ」"

    "スケールは自分に矢が向いていることを嫌がるように顔をしかめ、飲み物に口をつけた。"

    "そして、強引に話を戻す。"


    play music audio.investigation

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「とにかく、だ。放っておけばアランが選定の勝者になる可能性が高いと、おれは思っている」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「正義のためにも、それは許せない。さっきも言ったが、アランはいまや犯罪者だ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「そもそも今の地位を手に入れるために、どんな悪事を働いたかも想像がつくくらいに彼は――悪だ！」"

    hide ode
    show mhr uni sco wic at std_cr
    with std_swap

    voice get_voice_filename("mhr")
    miharu "「くすっ、中々に愉快な演説だ」"

    "海晴はスケールには聞こえないようにそう呟いた。"

    "選定には生き残るべき人とそうでない人がいる――自分に話したことは嘘ではないらしいが、方便もいいところだ。"

    "そのために、結局オデットやフェデリーコに協力を仰いでいるのだから。"

    "最終的にどうするつもりなのか――海晴が今できるのは、スケールの行動を注視することだった。"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「強敵であるアランを、野放しにするわけにはいかない。Ⅳの少年が派手な動きを見せた以上、隙もできる」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「アランはその隙を狙い、Ⅳの少年を指名しようとするはずだ。そうなれば彼はまたカードを１枚取得してしまう」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「しかし、これ以上彼を有利にするわけにはいかない。だからこそ、おれたちが手を組んで彼を脱落させようじゃないか！」"

    hide mhr
    show fed sta nor ama at std_c
    with std_swap

    voice get_voice_filename("fed")
    federico "「とか言って、あんた自身もアランの情報を探すのが手詰まりだっただけじゃねぇか？」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「正直に言おう。それも事実の一つではある。彼が≪因果の刻≫にどんな行動をしていたか知る者は少ないし、関係者には箝口令をしいている」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「おれだけでは力不足だから、こうして君たちに声をかけたんだ」"

    show ode sta nor lau at std_r with std_in

    voice get_voice_filename("ode")
    odette "「かかっ、こいつに突っ込まれるとはねぇ。だが正義か悪かってんならあたしもこいつも悪だぜ？　そいつはいいのかい？」"

    show ode sta arm ser with std_change

    voice get_voice_filename("ode")
    odette "「あたしらが名乗ったとき、てめーのカードブックは反応しなかった。ホテルの宿泊情報か何かから、調べたんだろうけどよ」"

    show ode sta gra smi with std_change

    voice get_voice_filename("ode")
    odette "「当然、あたしらの素性もすでに調べてるんだろ？」"

    show fed sta nor pan with std_change

    voice get_voice_filename("fed")
    federico "「げぇっ、そうだったのかよ！」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「初めに伝えているはずだ。協力関係はアラン・スコーピオン、そしてもう一人、Ⅳの少年を脱落させるまでだ」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「現状では君たちと協力することはおれにとって必要悪だと割り切っている」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「悪いが関係が切れたら、君たちもおれの標的だ。もっとも君たちも同じことを思っているはずさ。あくまで目的達成のための協力関係だ」"

    show ode sta nor lau with std_change

    voice get_voice_filename("ode")
    odette "「かかっ、どっちかってぇと悪役の台詞じゃねえのか、それは。そこの嬢ちゃんに対しても、同じなのかねぇ……」"

    "海晴は、３人の会話を呆れながら聞いていた。"

    "第三者の海晴からすると、今話すべきことではない内容を酔った勢いに任せて話しているようにしか聞こえなかった。"

    hide sca
    show mhr uni sco dis rev at std_l
    with std_swap

    voice get_voice_filename("mhr")
    miharu "「協力関係を結ぶかどうかで揉めるなら、それはぼくのいないところでやっていただきたいな」"

    "出会ってすぐこそオデットという女性に驚かされ威圧されていたが、海晴はすでに落ち着きを取り戻していた。"

    "賑やかに口論をする彼らを見て、拍子抜けだったこともあるだろう。"

    "運命の大広間では恐怖の対象でしかなかったが、話してみれば、ただの人間。"

    show mhr uni sco con rev with std_change

    voice get_voice_filename("mhr")
    miharu "「オデットさん。あまりスケールさんをからかっては可哀想だ」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「ほう、こいつ……。嬢ちゃん分かってるねぇ。同じ女だからかァ？」"

    show fed sta nor ela with std_change

    voice get_voice_filename("fed")
    federico "「夢の世界で見るよりもちょっと若いが、十分発育はいい……どうだい、こいつら放っておいてオレと抜け出さないか？」"

    "フェデリーコが海晴にそう訊ねると、海晴は一歩下がって距離を取った。"

    "言葉は発しなかったが、歪ませた顔が拒絶の応え。"

    show ode sta nor tro with std_change

    voice get_voice_filename("ode")
    odette "「バカヤロー。ま、この嬢ちゃんが{rb}美味{/rb}{rt}うま{/rt}そうだってのには同感だが……まあいい」"

    show ode sta arm smi with std_change

    voice get_voice_filename("ode")
    odette "「てめーの思想があまりに矛盾してたんで突っ込んじまったが、協力関係には反対しねぇよ。ちっと不本意だが、あたしらも頭打ちだったんでねぇ」"

    hide mhr
    hide ode
    hide fed
    show sca sta nor lau rev at std_l
    with std_swap

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡＨＡ、実際に会ってみれば、夢の世界で思っていたよりもずっと厄介なマダムのようだ」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「ひとまず、おれたちはこれからアラン脱落まで、協力関係だ。方針はこれから決めるとして、まずは杯を交わし直そう」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「ミハル、君も何か飲み物のお代わりを頼むかい？」"

    stop music fadeout 1

    show mhr uni sco wic at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「おかわりの前に、飲んでもらいたいものがあるんだ」"

    "空のグラスを差し出して、海晴は不敵に笑う。"

    "オデットはすまし顔だったが、フェデリーコとスケールは眉をひくつかせていた。"

    "この期に及んで何を、と思っているに違いない。"

    play music audio.badguys

    show mhr uni nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくはアランの≪死因≫を知っている。初期カードに含まれていてね」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「……なんだって？」"

    show fed sta nor pa1 at std_r with std_in

    voice get_voice_filename("fed")
    federico "「マジかよ！」"

    show mhr uni sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「君たちがいくらぼくにない情報網と調査力を持っていたとしても、≪死因≫のカードそのものをもつアドバンテージには敵わないだろう」"

    hide fed
    show ode sta nor lau at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「言えよ。かかっ。てめーは酒よりも条件を飲ませたいみたいだからな」"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、その通りさ。この協力関係の上で優先するのはまず、Ⅳの少年にして欲しいんだ」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「スケールさんはすでに知っているだろうけれど、彼がテロの標的にしたのはぼくの通う私立飴茶女子大学附属高校だ」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「その事件での死者は１名。そしてその犠牲者は、ぼくの見知った後輩だ」"

    hide ode
    show fed sta nor nor at std_r
    with std_in

    voice get_voice_filename("fed")
    federico "「じゃあ何だ、オレらでそいつを脱落させたら、アランの野郎の≪死因≫を教えるってことでいいんだな？」"

    show mhr uni nor vig rev with std_change_wait

    "フェデリーコの質問に、海晴は黙って頷いた。"

    show fed sta nor ela with std_change

    voice get_voice_filename("fed")
    federico "「可愛い面して復讐とは、怖ろしいもんだぜ」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「フェデリーコくん。ミハルが言っているのは復讐の手伝いをしろとか、そういうことじゃないと思う」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「選定の参加者が脱落した場合、選定開始から脱落までに起こした行動はなかったことになる――女神の選定には、こんなルールがあったね」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「Ⅳの少年を脱落させ、亡くなった知人を取り戻したいんだね？」"

    show mhr uni pai irr with std_change

    voice get_voice_filename("mhr")
    miharu "「どう解釈してもらっても構わない。だから、否定はしないよ」"

    show sca sta nor lau rev with std_change

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡＨＡ、おれは大賛成だ！　後輩を助けたいだなんて、まさしく正義じゃないか！」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「どちらにせよ、無関係の人間を巻き込んだⅣの少年は、悪に違いない。順番が逆になるだけだ」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「≪未練≫のカードが消滅するなんて奇妙なことがあったが、このメンバーならそんな苦難も乗り越えられるとは思わないかい？」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「どうするよ、オデット？　遠回りではあるが、確実にアランの≪死因≫が手に入るし、何より敵を１人は減らせるんだ」"

    hide fed
    show ode sta arm ser at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「嬢ちゃんよぉ、あたしらが断ることは想定済みかい？」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「その可能性は低いと思っているよ。スケールさんがⅣの少年を後回しにしたのは、初期カードに消滅したⅣのカードが含まれていたからではないかと思っていたんだ」"

    show mhr uni sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「さっきわざわざそのことに触れたのも、裏付けの一つだね。話題に出さないということは、あるいはオデットさんたちも……」"

    "海晴にとっては、勝算の高い賭けであった。カマをかけたと言ってもいい。"

    "そして、その予想が外れてもただ考え過ぎと思われるだけということも読んでいた。"


    play music audio.badguys

    show ode sta arm smi with std_change

    voice get_voice_filename("ode")
    odette "「ふぅん」"

    "オデットはにやり、と笑ってみせた。"

    "海晴はその顔を見て、賭けに勝ったことを確信する。"

    "彼女はユウの≪氏名≫か≪未練≫のカードを持っていて、内容の変化によって消滅した経験がある。"

    "スケールも真剣な表情を浮かべているのを見た。"

    "海晴は自分の予想が当たっていたことに頷いた。"

    show ode sta nor nor with std_change

    voice get_voice_filename("ode")
    odette "「確かにあたしが持ってたあのガキの≪氏名≫のカードは、消滅しちまった」"

    show ode sta arm ser with std_change

    voice get_voice_filename("ode")
    odette "「消去法で言えば、スケールのやつは≪未練≫だな。ま、イレギュラーがあったからこそ後回しにしているってのは嬢ちゃんも重々承知してるだろ？」"

    show ode sta arm ser with std_change

    voice get_voice_filename("ode")
    odette "「勝算がないとあたしらが動けないことも、分かってるはずだ」"

    show ode sta gra smi with std_change

    voice get_voice_filename("ode")
    odette "「例えばてめーがすでに≪Ⅳ・死因≫を取得している……でもない限り、あのガキを優先することはできないな。そうだろ？」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡ、そうだね。でもおれは、ミハルもそのことを分かっていると思ったからこそ、賛成したのさ」"

    show mhr uni sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、当然さ。けれども、ぼくが持っているのは≪Ⅳ・死因≫ではない。≪Ⅳ・氏名≫のカードだよ」"

    show ode sta arm smi with std_change

    voice get_voice_filename("ode")
    odette "「ほぅ……そいつは中々面白い」"

    hide ode
    show fed sta nor int at std_r
    with std_swap

    voice get_voice_filename("fed")
    federico "「ミハルの≪Ⅳ・氏名≫は消えてないってわけか？」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    odette "「なるほど……そう来たか。君は何らかの方法で、消滅した後の情報を手に入れたんだね」"

    hide fed
    show ode sta nor gla at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「嬢ちゃん……てめーはそいつをどこで手に入れた？」"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「そこまで教える義理はない。けれど、まずⅣの少年を狙うということであれば当然――君たちにも彼の≪氏名≫を教えよう」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「派手な活動をしている分、行動もつかみやすい。スタート地点は≪氏名≫一つだけれど、アランよりは残りの情報を集めやすい、とぼくは思っているよ」"

    "海晴はわざとらしく、スケールに目配せをした。"

    "スケールも、その意味には気付いていた。"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「任せてくれ。おれはてっきり≪死因≫から追うのかと思っていたが、いくらかやりやすくなったくらいだ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「例の事件を独自に調べてるジャーナリストは多いから、いい交渉材料になるかもしれない。使わせてもらうけれど、情報を得るためだ。いいね？」"

    show mhr uni nor ser with std_change_wait

    "海晴はスケールにそう訊ねられたので、無言で頷いた。"

    "スケールをどれほど信用していいものかはっきりは分からないが、オデットやフェデリーコの名前を調べたくらいだから情報収集力については信用できるはずだ、と思っていた。"

    hide ode
    show fed sta nor smi at std_r
    with std_swap

    voice get_voice_filename("fed")
    federico "「あのムカつく野郎の鼻っ柱を折るのが先延ばしになるのは不本意だが……かと言って情報もないしな。ま、嬢ちゃんの言う通りでいいだろ」"

    hide fed
    show ode sta nor lau at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「あたしも乗ったぜ。嬢ちゃん、大立ち回りの甲斐があったな」"

    show mhr uni sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「……くすっ。どうも」"

    hide mhr
    hide ode
    hide sca
    with std_out

    "そして、海晴は≪Ⅳ・氏名≫のカードを３人に共有した。"

    python:
        add_character_cards("mhr", ["4_name"])
        add_character_cards("fed", ["4_name"])
        add_character_cards("sca", ["4_name"])
        add_character_cards("ode", ["4_name"])

    "海晴は再度この３人の評価をし直すことにした。"

    "スケールは間違いなく、まだ何か隠している。"

    "彼の真意が読めないというのがその理由だ。"

    "胡散臭い男ではあるが、校門で海晴に話した内容が嘘とも思えないにもかかわらず、オデットやフェデリーコと手を組んでいる。"

    "フェデリーコもオデットの陰に隠れているが、十分頭が切れる。"

    "彼についてはさらに、何をしでかすか分からない得体の知れなさがあった。"

    "言わば、キレたら何をするか分からないタイプといったところだろう。"

    "オデットに関しては言うまでもない。"

    "この交渉をする時、海晴が緊張していたことを見透かされている。"

    "動揺した表情を見せず、汗も流さないように努めていたが、それでもこの女性はあえて大立ち回りという言葉を使ったと、理解していた。"

    "迂闊なことは言ってはいけないとあらかじめ気をつけてはいたが、オデットの前ではその警戒さえも危ういと、海晴自分に言い聞かせる。"


    play music audio.relaxforadult

    show ode sta gra smi at std_cr with std_in

    voice get_voice_filename("ode")
    odette "「さて、酒だ酒だ！　てめーら飲むぞ」"

    show sca sta nor bit rev at std_l with std_in

    voice get_voice_filename("sca")
    scale "「君たちは……。まあ、仕方ない。おれも付き合うよ」"

    hide sca
    hide ode
    with std_out

    "海晴はその後、スケールに連絡先を教えた。"

    "躊躇いはしたが、いざとなれば解約すればいいと思い至り、スケールの連絡先と交換することにした。"

    "彼らが酒宴を始める前に、海晴はバーを立ち去る。"

    "海晴は自分自身、彼らと対等に話せたことに驚いていた。"

    "同時に、彼らと協力してでも成し遂げなければならないと、決意を固くしていた。"

    "一刻も早く、凛火の笑顔を取り戻す――と。"

    $ add_seen_chapter("7_1-2")










    python:
        set_info_scene("91")
        set_info_date(6, 13, "wed")
        set_info_time("noon")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom rain with fade_longest
    play music audio.rain
    pause 1

    $ show_hud()

    show rnk mos nor hol at std_c with std_in


    "昨日は、ずっと部屋にいた。"

    hide rnk with std_out

    "今日はご飯がないから、コンビニまでは行かなくてはならない。"

    "外は雨だ。"

    "梅雨は始まったばかりだから、雨の日はまだまだ続く。"








    python:
        set_info_scene("92")
        set_info_time("evening")
        set_info_location("34")

    stop music fadeout 2
    scene bg bar with fade_longest
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    "直未の葬式以来、海晴は凛火と連絡をとっていなかった。"

    "自分では凛火の悲しみを埋めることができないと分かっていたからだ。"

    "願わくば、一秒でも長く凛火と寄り添っていたい、と思っている。"

    "しかし海晴にとってもっとも大切なのは、凛火の本当の幸せだった。"

    "凛火が落ち込み悲しんでいるならば、海晴が行動することこそが凛火を守ることに繋がると信じている。"

    "だからスケールが協力関係に誘って来たのは朗報であった。"

    "集まった全員がきっと腹に何か抱えているけれど、海晴もまた、彼ら全員が指名の対象であるのだから問題はない。"





    "スケールたちと手を組むと決めてから一日が経ち、海晴は彼に呼び出されていた。"

    "しばらくはスケールがユウの情報を集めるということだったが、進展があったのだろう。"

    "もう一日二日はかかると思っていたが、予想よりもずっと早い。"

    "夢の世界では否定していたが、彼の職業は本当に探偵だったのだろうか。"

    "もっとも、進展が見込めなかったからこそ呼ばれた可能性もある。対策を打つなら早い方がいいからだ。"

    show sca sta nor gre rev at std_l with std_in

    voice get_voice_filename("sca")
    scale "「こんばんは」"

    show ode sta arm smi at std_c with std_in

    voice get_voice_filename("ode")
    odette "「丁度いい。嬢ちゃんを待ってたところだ」"

    show fed sta nor smi behind ode at std_r with std_in

    voice get_voice_filename("fed")
    federico "「今日はおごるぜ」"

    "店に入ると、すでにスケールたちは酒を嗜んでいた。"

    "昨日も飲んだばかりだろうに、大人の考えはよく分からない、と呆れていた。"

    "海晴は半ば呆れながらも、前日のやり取りである程度酒が入っても会話が成り立つ人たちというのは分かっていたので、「ご馳走してもらえるなら」と今日もミルクを注文した。"

    "この店にはエスプレッソもあるが、なるべくならば次に飲むコーヒーは凛火の淹れたものがいい、とそう思っているから頼まなかった。"

    hide ode
    hide fed
    show mhr civ sco dis at std_c
    with std_swap

    voice get_voice_filename("mhr")
    miharu "「要件は手短にしてもらえるかな？　君たちが飲んでいると、話が長くなって嫌だからね」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「辛辣だねぇ。ま、呼んだからにはそれなりの成果はあるさ」"

    show mhr civ sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「成果……かい？」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「Ⅳの少年――ユウのことについてさ。おれの見立て通り、すでに多くのジャーナリストがこの件を調べていた」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「おれたちが彼を脱落させたら、彼らの努力はどうなってしまうんだろうね。『別の事件を調べていたこと』にでも変わるのだろうかねぇ」"

    show fed sta nor ama at std_r with std_in

    voice get_voice_filename("fed")
    federico "「勿体ぶってないでとっとと話せよ。結局、どこまでの情報が分かったんだ？」"


    play music audio.investigation

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「飴茶高校爆破事件と関係が囁かれてる無国籍テロ集団、通称≪ＮＵＬＬ≫だが、どうやら直接の関係はないらしい」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「が、全くの無関係でもなさそうだ。どうやら思想やスタンスに共感して≪ＮＵＬＬ日本支部≫を名乗っている組織があるらしく、そいつと関係があるようだ」"

    show mhr civ sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「昨日の段階では、君は彼が≪ＮＵＬＬ≫と関係していると言っていたね。どうしてたった一日でそこまで分かったんだい？」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「ユウというのは彼のコードネームみたいなものだろう？　おれたちくらいしかその情報はつかんでいないからね、有力な情報交換の材料になったよ」"

    "組織だとか支部だとか、海晴は急に現実感を失っていた。"

    "こうして改めて話されると、余計にフィクションの世界のような違和感が増す。"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「ま、連中の思想や目的なんて今はどうでもいい。ユウにも直接の関係はないからな」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「大事なのは、ユウ個人の情報さ」"

    hide fed
    show ode sta arm ser at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「ここまでが前提条件ってわけか。続けな」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「あの少年のことかは分からないが、≪ＮＵＬＬ日本支部≫に今年の春、少年のメンバーが入ったという話を聞いた」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「紛争地域の出身らしく、元傭兵だそうだ。向こうの方には身寄りのない子供を集めて少年兵にしている組織もあるらしくてな、そこから買われたらしい」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「銃器の扱いに長け、まるで心がないかのように戦っていたらしい。ついたあだ名は、≪神速の射手――サジタリウス≫」"

    show ode sta nor tro with std_change

    voice get_voice_filename("ode")
    odette "「胡散臭ぇ」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「この辺りは、少年を商品としている組織が囃し立てただけだろうな……話を戻そうか」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「どうやら日本に個人的な恨みを持っているという噂もあるから、自分から志願したという説もある」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「もっとも、≪ＮＵＬＬ日本支部≫としては、兵士を求めていたわけではないらしい」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「ただ命を捨てることを厭わない人形を買った、そんな認識だそうだ」"

    hide ode
    show fed sta nor no2 at std_r
    with std_swap

    voice get_voice_filename("fed")
    federico "「どの筋の情報だぁ、そりゃ？」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「そいつは教えられないね。教えたら、あんたらが襲いに行くかもしれないだろ？」"

    hide fed
    show ode sta nor lau at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「かかっ、分かってらっしゃる。まあこの場合はいいさ。どうせあたしらはカチコミ担当だろ？」"

    show mhr civ sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「そうなると、この中でぼくは場違いだね」"

    show sca sta nor lau rev with std_change

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡ、そうでもないさ。現に君は、おれたちを動かしている――メリットも、きちんと提供してくれているしね」"

    "スケールはわざとらしくウインクをしてみせた。"

    "海晴は苛立ちながら、彼から視線を逸らした。"

    hide ode
    show fed sta nor int at std_r
    with std_swap

    voice get_voice_filename("fed")
    federico "「アメチャ高校だっけか？　あんなところを爆破したのはどうしてなんだ？」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「おれも、丁度その話をしようと思っていたところだ。どうやら、組織の指示ではないそうだ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「持ち込まれた爆弾の量や、彼の潜入の手段などからして、ユウの他に協力者はいたらしいが、どうやらユウ個人がメンバーを扇動したそうだ」"

    "潜入の手段――それは、飴茶の制服を着ていたということであろう。"

    "中性的な顔立ちの彼はその容姿から目立ってはいたが、女子かどうかを疑う生徒はいなかった。"

    "大胆さが、かえって自然だったというわけだろう。"

    hide fed
    show ode sta nor lau at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「かかっ、そんなもん、もう組織として崩壊してんじゃねぇか」"

    show mhr civ sco thi with std_change

    voice get_voice_filename("mhr")
    miharu "「組織として崩壊――そういえば、先月の終わり頃に渋谷付近の山手線内で不審物が見つかった事件があったね。何か、関係があるのかな？」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「そうだ、どうして≪ＮＵＬＬ日本支部≫の情報がこうも筒抜けになってきているかそろそろ想像できるはずだ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「何事もなく済んだのは、組織に裏切り者がいたからだそうだ。自らテロに志願したが、実行しなかった裏切り者がね」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「これをきっかけに、水面下で捜査が入った」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「混乱や報復を招くため大々的には報道されてはいないが、すでに≪ＮＵＬＬ日本支部≫の中枢メンバーは逮捕され、組織は半壊状態だそうだ」"

    hide ode
    show fed sta nor ama at std_r
    with std_swap

    voice get_voice_filename("fed")
    federico "「ある意味じゃ、≪ＮＵＬＬ≫ってのも風評被害を食らってんだな。そんな間抜けに足元すくわれてんだから」"

    hide fed
    show ode sta arm ser at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「裏切り者が出るってことは、事を起こす前に組織としちゃ限界を迎えてたんだろうな。金か人かは知らねえが……さて、そろそろ核心だろ？」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「ああ、情報はまだある。連中にはいま話した事件の前に、山手線で自爆テロを起こす計画があったらしい」"

    show sca sta nor smi rev with std_change

    voice get_voice_filename("sca")
    scale "「しかし、その実行犯が突然失踪したことにより、計画は延期」"

    "海晴はここまで聞けば、概ねの状況を理解していた。"

    "別の世界の話のようではあるが、流れが分からないわけではない。"

    "スケールはグラスに口をつけてから、静かな声で告げる。"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「失踪した実行犯こそ恐らく――ユウだ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「そして当初の計画実行の時期は、５月の初週。この国のゴールデンウィークの直後だ。選定開始と被っているのは偶然とは思えないさ」"

    show ode sta nor lau with std_change

    voice get_voice_filename("ode")
    odette "「かかっ、こいつは思った以上の成果だ。てめー、ユウの死因まで挙げてきたってわけか！」"

    hide ode
    show fed sta nor nor at std_r
    with std_swap

    voice get_voice_filename("fed")
    federico "「自爆テロとは、ずいぶん予想外な答えが飛び込んできたもんだ……」"

    "会話が成立していないとも思えるやり取りだが、海晴は彼らの会話の間を自分で補完することができていた。"

    "いや、ここまで情報が揃えば誰でも分かるだろう。"

    show fed sta nor nor with std_change

    voice get_voice_filename("fed")
    federico "「自爆テロで死んだから、その事件自体がなかったことになってるってわけだな……」"

    show fed sta nor pa2 with std_change

    voice get_voice_filename("fed")
    federico "「となると奴の死因は爆死か――焼死か……うおっ、出たぜ」"


    play music audio.impatience

    scene ecg cardbook bli with dissolve_long

    "フェデリーコの持つカードブックから、光が放たれた。オデットや海晴のカードブックにも同様に、カードが生成される。"

    python:
        add_character_cards("mhr", ["4_death"])
        add_character_cards("fed", ["4_death"])
        add_character_cards("sca", ["4_death"])
        add_character_cards("ode", ["4_death"])


    "協力関係を結んでからたった一日でユウの≪死因≫まであきらかになったことに、彼らは感心するよりも驚いていた。"

    "海晴も彼らと同じように、驚きの表情を浮かべていた。"

    "もっとも、海晴の驚きにはもう一つの意味があった。"

    "５月２日水曜日。"

    "海晴や凛火を含めた選定の参加者が命を落とした日であり、運命が改変された日でもある。"

    "この日に何をしていたかの大まかな内容を、海晴は凛火から聞いている。"

    "直接的な死因を聞いていなかったけれど、海晴はその時一緒にいたという直未に、後日、当時の状況をある程度聞いていた。"

    "直未は質問してくる海晴の剣幕に怯えていたが、自分が凛火とともに列車の火事に巻き込まれる夢を見ることを語った。"

    "この時に冷たく接し過ぎたことを、海晴は直未がいなくなってしまった今こそひどく後悔しているが、後の祭りだ。"

    "ともかく、凛火の≪死因≫のカードは窒息死。海晴はソーニャを指名したとき、このカードを手に入れていた。"

    "凛火の死に際など想像したくはなかったが、直未の話と合わせて、火事に巻き込まれ、煙が肺に入り込んだことにより窒息、とそう予想していた。"

    "だが、海晴の中でその予想は覆され、一本の線に繋がった。"

    "電車の火事は事故なんかじゃない。"

    "――凛火は、ユウが引き起こしたテロに巻き込まれて死んだ。"


    play music audio.investigation
    scene bg bar
    show sca sta nor ser rev at std_l
    with dissolve_long


    voice get_voice_filename("sca")
    scale "「どうしたミハル？　顔色が悪いようだけれど？」"

    show mhr civ sco dis at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「失礼。山手線というのはぼくも利用しているからね。そこで人が死ぬところをつい想像してしまっただけさ」"

    "海晴は動揺を隠していたが、表情の端々には怒りが滲み出ていた。"

    "直未だけでなく凛火も、ユウに奪われた――海晴がその事実を許せるはずもない。"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「気持ちは分かるよ。どんな思想があるのかは知らないが……こいつは間違いなくとんでもない悪だな。野放しにしてはいけない」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「ミハルの方からⅣを優先すると提案してもらって、感謝してるくらいだ」"

    show sca sta nor bit rev with std_change

    voice get_voice_filename("sca")
    scale "「ちっ。カードの消滅なんてことが起こらなければ、おれには３つのカードが揃ってたのにな……」"

    show fed sta nor nor at std_r with std_in

    voice get_voice_filename("fed")
    federico "「ま、問題はその≪未練≫だな。あんたの早さには敵わないだろうが時間さえかければオレたちも≪死因≫までは辿り着けた」"

    show mhr civ sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「残念ながら、彼の未練についての手がかりをぼくは持っていないよ」"

    hide fed
    show ode sta gra smi at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「ま、手段は二つだろ。一つはガキを知る奴を探し出して話を聞く。もう一つは……」"

    hide ode
    show fed sta nor ama behind mhr at std_r
    with std_swap

    voice get_voice_filename("fed")
    federico "「はぁ……」"

    hide fed
    show ode sta gra gla at std_r
    with std_swap

    voice get_voice_filename("ode")
    odette "「直接聞く、だ」"

    "オデットは不敵に笑うと、手に持ったグラスを飲み干した。"








    python:
        set_info_time("night")
        set_info_location("18")



    stop music fadeout 1
    scene bg lion02 nightclose with fade_long
    play music audio.growapart
    pause 1

    $ show_hud()

    "海晴は遠回りをして、ライオン館の前に立ち寄っていた。"

    show mhr civ sco sh1 at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「凛火は何をしているだろうか……？」"

    "ライオン館の中へ立ち入る勇気は持ち合わせていない。"

    "自分では足りないと、自覚するのが嫌だったから。"

    "見慣れた喫茶店を外から眺めながら、海晴はバーでのことを思い返していた。"

    "海晴は、スケールの手腕に驚かされていた。"

    "自分が≪ユウ≫という情報を教えただけで、彼の≪死因≫まで特定したのだ。"

    "どう≪未練≫を取得しようかと立ち止まりそうになれば、今度はオデットが方法を提示した。"

    "荒事は一手に引き受けると、楽しそうな顔で言ったのだ。"

    "海晴は自分自身を優秀だと自覚していたが、それだけでは越えられない人脈と経験、そして強靭な肉体と精神の高く分厚い壁がはっきり見えた瞬間でもあった。"

    "彼女は、自分が脱落することは恐くなかった。"

    "だが凛火が脱落すること、そして自分の脱落により凛火が悲しむことが恐かったのだ。"

    show mhr civ nor ser with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくだけ――いや、ぼくでは、凛火を繋ぎとめることはできないから」"

    "この諦めこそ、自身への信用のなさこそ、海晴が誰にも見せない弱さだった。"

    "けれども、海晴はとっくの昔に決意していたのだ。"

    "吊り橋の上を片足立ちで進むような自分でも、凛火が強いと言ってくれるなら、信頼に応えようと。"

    "幸いにも、スケールもオデットも海晴を過大評価していることを、海晴自身が分かっていた。"

    "それは海晴が精一杯の虚勢を張った姿であったけれど、いっそ真実になるまで偽り続ければいいのだと、海晴は微笑んだ。"

    "嘘つきな自分は嫌いだけれど、一つの目的のために嘘をつく自分のことを、海晴は嫌ってはいない。"

    "そう、全ては。"

    "凛火の、ためなのだから。"

    $ add_seen_chapter("7_1-3")










    python:
        set_info_scene("93")
        set_info_date(6, 14, "thu")
        set_info_time("morning")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom rain with fade_longest
    play music audio.rain
    pause 1

    $ show_hud()

    "梅雨の日は続いていた。"

    "私は無気力状態で、何もできずにいた。"

    "食事も最低限しかとっていない。"

    "量っていないけれど、体重は何キロか減っていることだろう。"

    show rnk mos nor hol at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「直未……ごめんね……」"

    "最近は毎日、夢を見ていた。"

    "直未と出会ってからあの日に至るまでの思い出と、直未の死の瞬間が交互に繰り返される悪夢だ。"

    "何度も何度も、直未の死を見せつけられる。"

    "でも、それは罰なのだと思っていた。"

    "私のせいで直未はいなくなってしまったから。"

    "罰を受けることが、私の償い。"

    "ベッドの上で私がすることと言ったら、ひたすらに後悔することだけだった。"

    show rnk mos nor hol with std_change

    voice get_voice_filename("rnk")
    rinka "「こんなことなら、出会わなければよかったのかな……」"

    hide rnk with std_out

    "そんな風に思わずにはいられない。"

    "何度も何度も、思考はループしていた。"

    scene bg myroom rain large at align(0.5, 1.0) with dissolve

    "スマホが鳴ったのを聞いて、手に取ってみた。"

    "日付が表示されている。"

    "そうか、今日は木曜日か。"

    "直未が命を落としてから、すでに５日目だ。"

    "着信もメッセージも、すごいことになっている。"

    "ほとんど全てが真央からだ。"

    "学校が休みなんだから、放っておいてくれてもいいのに。"

    "私はずっと、見ることも着信をとることもできなかった。"

    "だって、私が直未を殺したも同然なんだ。"

    "私が巻き込まなかったら、直未は死ななかったのだ。"

    "なのに、どうして私が真央と話せるんだ。"

    "日に日に、私は責任の重大さに押しつぶされそうになっていた。"

    scene bg myroom rain with dissolve

    show rnk mos nor hol at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「おばあちゃんだ……」"

    "一件だけ、おばあちゃんからの着信があった。"

    "留守番電話が録音されている。"

    "――辛かったら、こっちへおいで。"

    "簡単なメッセージだった。"

    "でも、とても心強かった。"

    "全てを投げ出して、脱落するまでの期間をおばあちゃんと過ごすのも、悪くはないかもしれない。"








    python:
        set_info_scene("94")
        set_info_time("noon")
        set_info_location("09")

    stop music fadeout 2
    scene bg maidcafe with fade_longest
    pause 1

    $ show_hud()

    "スケールたちと協力関係を結びこそしたが、海晴は海晴で日常生活を送っていた。"

    "学校が休みな分、海晴はアルバイトを増やしていた。"

    "学校からはなるべく外出は控えるように指示されているが、海晴の知ったことではない。"

    "お客の来店を知らせるベルが鳴り、海晴は入り口に視線を向けた。"


    play music audio.maidcafe

    show mhr mai sco vig rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「お帰りなさいませご主人さ……」"

    "海晴はお決まりの挨拶を言いかけたところで、絶句した。"

    "無理もないことだ。"

    "客として迎えようとしたのは、とてもご主人様とは言い難い人物たちだったのだ。"

    show mhr mai sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「本日は雨のため、足元にご注意してお帰り下さいませ」"

    show fed sta nor int at std_c with std_in

    voice get_voice_filename("fed")
    federico "「おい待てよ、オレたちは客だぜ！」"

    show sca sta nor joy at std_r with std_in

    voice get_voice_filename("sca")
    scale "「まあまあ、フェデリーコくん。ここはメイド喫茶というものだ。おれたちも、きちんと挨拶を返さないから言われてしまうんだ」"

    "スケールは咳払いをしてから、言い直す。"

    show sca sta nor smi with std_change

    voice get_voice_filename("sca")
    scale "「ただいま」"

    show mhr mai sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「お気をつけていってらしゃいませ」"

    show fed sta nor pa4 with std_change

    voice get_voice_filename("fed")
    federico "「帰れってことじゃねーか！」"

    show sca sta nor lau with std_change

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡ、日本のツンデレというやつは面白いな」"

    show fed sta nor irr rev with std_change

    voice get_voice_filename("fed")
    federico "「適当なこと言ってんじゃねーぞ。大体なんだこの店は……」"

    show mhr mai sco dis rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ちっ……。入り口で騒がれても迷惑だ、席まで案内するよ」"

    hide fed
    hide mhr
    hide sca
    with std_out

    "秋葉原のメイド喫茶は外国人観光客も多いから、彼らがそこまで悪目立ちすることはない。"

    "海晴は彼らに聞こえるように舌打ちをしてから、テーブルまで案内した。"

    show mhr mai sco vig rev at std_l with std_in

    voice get_voice_filename("mhr")
    miharu "「はぁ……どうしてぼくが……」"

    "言葉の問題もあり、二人の接客は全て海晴に丸投げされてしまった。"

    show mhr mai sco dis rev with std_change

    voice get_voice_filename("mhr")
    miharu "「何を勘違いしているのか知らないけれど、ここは君たちの来る店ではないよ」"

    show mhr mai sco dis rev with std_change

    voice get_voice_filename("mhr")
    miharu "「もっと、現実に不満を持っていて、さらに女子と接点がないがために過度の幻想を抱いてしまった残念なご主人様たちが訪れる場所さ」"

    show sca sta nor joy rev at std_c with std_in

    voice get_voice_filename("sca")
    scale "「フェデリーコくん、おれはこのと・く・せ・いパンケーキを頼もうと思っているのだが」"

    show fed sta nor no2 at std_r with std_in

    voice get_voice_filename("fed")
    federico "「あんた持ちだろ？　注文は任せるよ。しかし落ち着かない店だなぁ」"

    show mhr mai sco vig rev with std_change

    voice get_voice_filename("mhr")
    miharu "「とりあえずスケールさん。そのメニューを頼んだらぼくは君を一生許さない」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「あ、フェデリーコくん。アルコールメニューもあるみたいだよ。ビールでいいかな？」"

    show mhr mai sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くっ……何故だ……どうして……」"





    scene bg maidcafe with fade_long
    pause 1

    "１時間後、海晴は顔を真っ赤にして彼らを見送っていた。"

    "結局、スケールは容赦なく海晴に呪文をかけさせた。"

    "ソフィアが注文して以来の呪文に、海晴は生涯最大級の屈辱を覚えていた。"

    "メイド喫茶がどんなものか知っていたスケールはともかく、単純にポーズを決める海晴を見て喜んでいたフェデリーコには、明確な殺意を感じていた。"

    "だが、彼らがふざけているのは会計までだった。"

    "今日も例の店に来いと、スケールは小声で告げた。"

    "スマートフォンで連絡をすればいいものをわざわざメイド喫茶に立ち寄ってきた、それも二人で。"

    "海晴は、そこに彼らの抱える隠し事を感じ取っていた。"







    python:
        set_info_time("night")
        set_info_location("34")


    stop music fadeout 1
    scene bg bar with fade_long
    play music audio.relaxforadult
    pause 1

    $ show_hud()

    show mhr uni sco cau at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「三日連続でこんなところに出入りしていたら、ぼくはそのうち補導されてしまうよ」"

    "海晴がバー≪MILK CROWN≫についた時、フェデリーコとスケールはすでにいた。"

    "そして海晴の予想通り、そこにオデットの姿はなかった。"

    show mhr uni sco wic with std_change

    voice get_voice_filename("mhr")
    miharu "「いくら情報網に自信があるとはいえ、あれはないんじゃないかな、スケールさん？」"

    "海晴は顔こそ笑っていたが、心の中ではスケールに対する敵意が剥き出しだった。"

    show sca sta nor lau rev behind mhr at std_l with std_in

    voice get_voice_filename("sca")
    scale "「ＨＡＨＡＨＡ、おれもせっかく日本に来たんだから、日本の文化に触れておきたくてね」"

    show fed sta nor nor at std_r with std_in

    voice get_voice_filename("fed")
    federico "「他の店員も見たが、あんたが一番の上玉だ。自身を持っていいぜ？」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「もう帰っていいかい？　そもそも、今日はあまり穏やかな話ができそうにないからね」"

    "海晴はふざけた空気を切り裂くように、本題へと切り込んだ。"

    "今日は飲み物を注文することはせず、まくし立てるように続ける。"

    show mhr uni nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「メイド喫茶にスケールさんと行ってくる――そうでもないと、オデットさんから逃れらないんだね、フェデリーコさん？　すっかり尻に敷かれていると言っていいね」"

    show fed sta nor ang with std_change

    voice get_voice_filename("fed")
    federico "「てめぇっ、オレに喧嘩売ってんのか？」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「落ち着け。ミハルもだ。その様子だと、今日呼ばれた理由はもう分かっているんだね？」"


    stop music fadeout 1

    "海晴はスケールから尋ねられ、一瞬立ち止まった。"

    "数秒間、思考を巡らせる。"

    "それは、自身の予想のさらに一歩先まで考えていたから。"

    "薄暗い店内で、海晴はかすかに瞳孔を広げた。"


    play music audio.badguys

    show mhr uni sco con with std_change

    voice get_voice_filename("mhr")
    miharu "「オデット・マランソンの脱落――ぼくを引き入れたのは、それが目的だね？」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「おれは君を仲間にして、良かったと思っているよ。話が早くて本当に助かる」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「彼女もまた、危険な存在であることは分かっているはずだ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「以前話した通り、人は行動するとき隙ができる。前を見ればその分、後ろで起きている出来事に気付かなくなるからね」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「あんたが唯一、あいつの懐に潜れる可能性を持っている。オレやこいつに対して、オデットは隙なんて見せやしないからな」"

    show mhr uni sco cau with std_change

    voice get_voice_filename("mhr")
    miharu "「一昨日の――今日だ。種明かしをするには少し早過ぎやしないかい？」"

    show sca sta nor gre rev with std_change

    voice get_voice_filename("sca")
    scale "「だからだよ。ミハル、君はオデットに敵わないと思ってしまってはいないか？」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「彼女が強く聡明であることは、誰の目に見ても明らかだ。だからこそ、負けを認めるのは危険だ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「オデットの性質は紛れもなく、悪だ。だが、それを感じさせない不思議な性質も持ち合わせている」"

    show fed sta nor int with std_change

    voice get_voice_filename("fed")
    federico "「あんたが取り込まれる前に、伝えておこうと思ってな。アランの野郎もオデットもいなくなる――どうだ？　随分と戦いやすくなるとは思えないか？」"

    show mhr uni sco vig rev with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくが彼女の情報を集められると？　それは過大評価じゃないのかい？」"

    show fed sta nor no2 with std_change

    voice get_voice_filename("fed")
    federico "「情報っていっても、≪死因≫はすでにオレとこいつで見当をつけてるんだ。オデットから隠れながらになっちまうが、もう数日もあればカード化できるまで情報が集まるはずだ」"

    show fed sta nor smi with std_change

    voice get_voice_filename("fed")
    federico "「あんたはオデットの≪未練≫だけ探してくれればいいんだ」"

    show sca sta nor nor rev with std_change

    voice get_voice_filename("sca")
    scale "「卑怯なことをしていると良心が痛むなら、心配することはない」"

    show sca sta nor joy rev with std_change

    voice get_voice_filename("sca")
    scale "「悪を倒すなら――おれたちは正義だろ？」"

    "悪びれることなく、スケールは海晴に問いかけた。"

    "海晴は下を向き、考え込む仕草を見せた。"

    "徐々に口を開くと、それは笑い声に変わった。"


    play music audio.shadowmiharu

    show mhr uni sco wic with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、くくく、ふふふふふふ……」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「面白いことを言うね、君は。ぼくたちは正義？　くすっ、それは違うよ。ぼくたちは……みんなまとめて悪だよ」"

    show mhr uni nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「でも、それでいいさ。悪だって構わない。あはははは！　ぼくの目的はいつだって一つだからね」"

    "海晴が笑っているのは、緊張という堤防が崩壊したからでもあった。"

    "高く分厚い壁の一つと思っていたオデットという壁は、あまりに呆気なく綻びを見せたのだ。"

    "彼らがオデットの≪死因≫に目星がついているように、海晴もまた彼女の≪未練≫に繋がるヒントを得ていたのだから。"

    "スケールの協力があれば、ヒントからカードへと変化するのもそう難しくはないだろう。"

    "そして協力関係を結んだオデットをあっさり裏切る算段を立てているスケール自身の≪死因≫のカードを目の前の海晴が持っていることを、彼は知らないのだ。"

    "これほどおかしいことは、滅多にないだろう。海晴は珍しく、腹筋がつりそうになるまで笑っていた。"

    "海晴の変貌に度肝を抜かれたのか、フェデリーコは引きつった表情を浮かべていた。"

    show fed sta nor ama behind mhr with std_change

    voice get_voice_filename("fed")
    federico "「こいつ……壊れたか？」"

    show mhr uni sco wic rev with std_change

    voice get_voice_filename("mhr")
    miharu "「心外だね。ぼくもおかしい時には笑ってしまうよ」"

    show mhr uni sco wic with std_change

    voice get_voice_filename("mhr")
    miharu "「協力関係を結んだんだ。精一杯全うさせてもらうよ。ただし、ぼくが動くのはどちらにせよユウを脱落させた後だ。この条件については――守ってもらうよ」"

    show sca sta nor ser rev with std_change

    voice get_voice_filename("sca")
    scale "「そう言うと思ったよ。もちろんだ。正義のために……ね」"

    "スケールは海晴に右手を差し出し握手を求めた。"

    "海晴は応じることなく振り向き、長い髪を揺らす。"

    "海晴の長く滑らかな髪は、薄暗いバーの照明を浴び怪しく光る。"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくが言うまでもないけれど、ボロは出さないようにした方がいいよ。噛みつこうとして、噛みつかれたら情けないからね」"

    show fed sta nor irr with std_change

    voice get_voice_filename("fed")
    federico "「はっ、今更だぜ。オレはあいつと組んでからずっとこの機会をうかがってたんだ」"

    show fed sta nor ela with std_change

    voice get_voice_filename("fed")
    federico "「気付かれていようが気付かれていまいが、やるしかねーだろ」"

    hide mhr with std_out

    "フェデリーコの言葉を最後まで聞くことなく、海晴はバーを後にした。"







    $ set_info_location("18")


    stop music fadeout 1
    scene bg lion02 night with fade_long
    play music audio.growapart
    pause 1

    $ show_hud()

    "この日も、海晴はライオン館を外から眺めていた。"

    "ねっとりとした初夏の夜の風を、海晴は浴びる。"

    show mhr uni sco wic at std_c with std_in

    voice get_voice_filename("mhr")
    miharu "「君のために、やり遂げるよ。くすっ、正義か悪かなんて、ぼくたちには関係ないからね」"

    "海晴はそれだけ告げると、再び帰路へとつくのであった。"

    $ add_seen_chapter("7_1-4")











    python:
        set_info_scene("95")
        set_info_date(6, 15, "fri")
        set_info_time("noon")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom rain with fade_longest
    play music audio.rain
    pause 1

    $ show_hud()

    show rnk mos nor hol at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「もう、金曜日か……」"

    "私は一人で、そう呟いていた。"

    "おばあちゃんのところには、行かなかった。"

    "それは、私が一人で大丈夫だからと思ったからではない。"

    "ただ、数日間泊まる準備をする気力も、遠出する元気もなかったからというだけだ。"

    "誰かが準備をしてくれて、おばあちゃんが迎えに来てくれたら、行っただろう。"

    "私はもう、駄目になってしまったのかもしれない。"

    play se "doorbell01"

    "来客を告げるインターホンの音が鳴った。"

    "私は無視をした。"

    play se "doorbell01"

    "またインターホンの音がした。"

    "私はまた無視をした。"

    play se "doorbell01"

    "音は、鳴りやまなかった。"

    "徐々に苛立ってきて、私はインターホンに出ることにした。"

    show rnk mos nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「いい加減にし……」"

    hide rnk with std_out



    voice get_voice_filename("mao")
    mao "「りーーーたーーん！」"

    "スピーカーからいきなり大きい声が出てきたので、私はつい一歩引いた。"

    "通話停止のボタンを押し損ねた私の隙をつくようにして、声の主は畳みかけた。"



    voice get_voice_filename("mao")
    mao "「りーたん、りーたん！　あーけーてー！」"

    "何の用事か知らないけれど、いま真央に会う気はしない。"

    "だが無視をしようと思っても、どうしてもできなかった。"

    "迎えに来てくれたと、期待していたのかもしれない。"







    $ set_info_location("04")


    stop music fadeout 1
    scene bg lion01 rain with fade_long
    play music audio.nichijo01
    pause 1

    show mao civ nor que rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「りーたん、久しぶり～って、すごい格好だね」"

    "真央は私を見るなり、そう言った。"

    "部屋着だし寝癖だらけだしで、言われても仕方ないと思っている。"

    "お風呂や歯磨きなど人間として最低限の清潔さは保っているから、ひどいのは主に見た目だと思うけれど。"

    show mao civ nor nor rev with std_change

    voice get_voice_filename("mao")
    mao "「何だか――随分久し振りだね。たった４日なのにさ、うちらこんなに会わなかったことってないかも」"

    show mao civ sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「そういえば、ライオン館に来たのもめっちゃ久し振りだよぉ。確かゴールデン・ウィーク前に……なおりんと……」"

    show mao civ sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「あ！　き、昨日のドラマ見たぁ？　まさかあの二人がキスしちゃうとは思わなかったよ～」"

    show rnk mos nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「変な気、遣わなくていいよ。真央だって辛いんだし、無理したくないでしょ。それよりさ、今日はどうしたの？」"

    show mao civ nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「にっはっはー。りーたんにはばれちゃうよね」"

    show mao civ nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「決まってるじゃん。りーたんに会いにきたんだよ」"

    show mao civ nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「連絡しても全然返してくれないから、心配だったよ。何だか、りーたんまでいなくなっちゃうような気がしちゃって……」"

    show rnk mos nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「真央……。コーヒー淹れるね。真央はカフェオレでいい？」"

    show mao civ nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「今日はうちもコーヒーをもらおっかな。ただ、お砂糖とミルクはたっぷり持って来てねん」"


    hide rnk
    hide mao
    with std_out

    "私は髪を結んで厨房に行き、コーヒーを淹れる準備をした。"

    "真央の表情を見ればどんな気持ちでここに来てくれたか、分からないはずがない。"

    "厨房に立ったなら、どんなに元気がなくてもちゃんとしないといけない。"

    "それは、おばあちゃんの口癖だから。"

    "思えば数日ぶりにコーヒーを淹れている。"

    "たった数日だけど、確かにこんなに日が空いたことはなかった。"

    "それでも、腕は鈍っていないと思う。"

    "ここに立っている時だけは気が引き締まるように、体が覚えているからだろう。"

    scene ecg raintalkB2 smi with dissolve_long


    voice get_voice_filename("rnk")
    rinka "「お待たせ」"


    voice get_voice_filename("mao")
    mao "「あー、いい香り」"


    voice get_voice_filename("mao")
    mao "「ってあれ、髪ほどいた瞬間、またさっきのだらしなーいりーたんに戻っちゃったねぇ」"

    "真央はいつもの調子で話していたけれど、それでもやはり元気は半減という感じだった。"

    show ecg raintalkB2 tro with ecg_change


    voice get_voice_filename("mao")
    mao "「苦っ」"

    "コーヒーを一口舌で舐めて顔を歪ませた真央は、すぐに角砂糖４つとミルクを入れた。"

    "真央は遠慮も躊躇いも一切ない。"

    "私としては、ブラックで飲んで欲しいというこだわりはないので、別によかった。"

    "ここは第二のおうちであればいい。"

    "家の中なんだから、好きに楽しめばいいのだ。"


    play music audio.rain

    show ecg raintalkB2 ser with ecg_change


    voice get_voice_filename("mao")
    mao "「雨だねぇ」"

    "窓の外に降り注ぐ雨粒を数えながら、私たちはコーヒーを飲んでいた。"

    "雨の刻むリズムよりもずっとゆっくりと、時間は過ぎて行く。"

    "濡れた木々の葉は、水をたっぷり含んだ鮮やかな緑色をしている。"


    voice get_voice_filename("mao")
    mao "「この数日間、毎日泣いたよ。不思議だよねぇ。雨だって止むのに、涙は枯れないんだから」"

    "雨音に消えてしまいそうなほど静かな声で、真央は呟いた。"

    "確かに不思議だ。"

    "私も毎日泣いていた。"

    "それでも、涙は枯れないんだから。"


    voice get_voice_filename("mao")
    mao "「りーたんはさ、どうして自分を責めてるの？」"

    scene ecg raintalkA2 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「自分を……どうして？」"

    "どうして分かったのか、と聞きたかった。"

    "ユウのことは、海晴に概要を話したくらいだ。"

    "それも、ただ事実を淡々と話しただけ。"

    "直未が≪女神の選定≫に巻き込まれたことなど、真央は知らないはずだ。"

    scene ecg raintalkB2 ser with dissolve


    voice get_voice_filename("mao")
    mao "「りーたんがうちのことを分かるなら、うちだってりーたんのことは分かるよ」"


    voice get_voice_filename("mao")
    mao "「あの時りーたんは事件現場に居合わせちゃっただけ。助けられなかったなんて思わなくていいんだよぅ」"

    show ecg raintalkB2 tro with ecg_change


    voice get_voice_filename("mao")
    mao "「悪いのは犯人――だよ。りーたんは自分を責めるんじゃなくて、なおりんのことを悲しんでればいいんだってぇ」"

    scene ecg raintalkA2 sad with dissolve


    voice get_voice_filename("rnk")
    rinka "「ううん、私が直未にコーヒーを教えなかったら、模擬店をやろうって思わなければ、こんなことにはならなかったんだ」"

    show ecg raintalkA2 ser with ecg_change


    voice get_voice_filename("rnk")
    rinka "「あの日、図書室で声をかけなければ――私と出会わなければ、直未は死ななかったかもしれないんだ」"

    "何度も何度も、繰り返した思考。"

    "そう思い悩むことはもはや、私にとって日常的なことになっていた。"


    play music audio.memories

    scene ecg raintalkB2 tro with dissolve


    voice get_voice_filename("mao")
    mao "「そんな風に言うなよぉ、りーたん。うちは、楽しかった」"


    voice get_voice_filename("mao")
    mao "「りーたんとみはるんと……なおりんで過ごして、楽しかったよ。ここでおしゃべりしたり、遊園地に行ったりもした」"


    voice get_voice_filename("mao")
    mao "「りーたんがそんな風に言ったら、せっかくの想い出がつまんなくなっちゃよぅ」"

    show ecg raintalkB2 ser with ecg_change


    voice get_voice_filename("mao")
    mao "「なおりんとの想い出は、うちの――うちらの宝物だよ」"


    voice get_voice_filename("mao")
    mao "「文化祭が終わったら遊ぼうって、約束もしてたのになぁ……もっと色々一緒にいたかったけど」"

    show ecg raintalkB2 smi with ecg_change


    voice get_voice_filename("mao")
    mao "「だからさ、りーたんは自分を責めるんじゃなくて、悲しんだ方がいいと思うよぅ。もっと一緒にいたかったって――なくなっちゃった未来を悲しもうよ」"

    scene ecg raintalkA2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「直未との――想い出」"

    "それは、私だけのものではない。"

    "真央の言う通り、私たちの宝物だ。"

    scene ecg raintalkB2 ser with dissolve


    voice get_voice_filename("mao")
    mao "「言ったじゃん。りーたんがいなくなっちゃうような気がしたって。そんなの嫌だ」"


    voice get_voice_filename("mao")
    mao "「りーたんがこのままずーっと駄目になっちゃうのも、嫌だ」"


    voice get_voice_filename("mao")
    mao "「割り切れないよ。うちだって全然……割り切れないけどさぁ！」"


    voice get_voice_filename("mao")
    mao "「これから{rb}未来{/rb}{rt}さき{/rt}を生きるのは、うちらなんだよ？」"

    "これから先、生きること。"

    "私の――私たちの未来。"

    "まだ何も分からない、私の可能性。"

    "誰も見たことのない、この先の運命。"


    voice get_voice_filename("mao")
    mao "「元気出して、なんて言わないよ。でもね、りーたん。ずっと下を見てなくてもいい……前を見たら、一緒に泣いてるうちらがいるよ？」"

    scene ecg raintalkA2 smi with dissolve


    voice get_voice_filename("rnk")
    rinka "「真央……」"

    show ecg raintalkA2 sad with ecg_change


    voice get_voice_filename("rnk")
    rinka "「駄目だ、もう我慢できないや」"


    scene bg lion01 rain with dissolve_long

    "そして私たちは、泣いた。"

    "――たくさん泣いた。"

    "目の前にはずっと、ぐずぐずに崩れた真央の泣き顔があった。"

    "一緒にいるから悲しみが半減するなんてことはない。"

    "悲しみを分かち合うことなんてできない。"

    "みんながみんな、同じくらい悲しい。"

    "でも、それでも。"

    "せめて、消えてしまった未来を嘆こう。"







    python:
        set_info_time("night")
        set_info_location("18")


    stop music fadeout 1
    scene bg lion02 night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "ようやく落ち着いたのは、夜になってからだった。"

    "梅雨真っ只中なのに珍しく、今夜は雨が止んでいた。"

    show mao civ sel irr at std_cr with std_in

    voice get_voice_filename("mao")
    mao "「今週で休校はおしまいだってさ、りーたん聞いてた？」"


    show rnk mos nor nor rev at std_cl with std_in
    voice get_voice_filename("rnk")
    rinka "「え、そうなの？」"

    show mao civ sel glo with std_change

    voice get_voice_filename("mao")
    mao "「着信を遡ってみたら、学校から連絡あったと思うよぅ。とりあえず、来週いきなりさぼっちゃだめだからねぇ？」"

    show rnk mos nor smi rev with std_change

    voice get_voice_filename("rnk")
    rinka "「分かってる。来週、また会おうね」"

    show mao civ sel lau with std_change

    voice get_voice_filename("mao")
    mao "「うむ。まったねぇ～」"

    "真央を見送った後、私は自分の部屋に戻ることにした。"







    $ set_info_location("04")

    stop music fadeout 1
    scene bg lion01 night with fade_long
    pause 1

    "試したいことがあり、私はカードブックに触れてみた。"

    show rnk mos nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「やっぱり、そうだよね。こんな簡単なことに気付かなかったなんて、私……馬鹿だな」"

    "カードブックは光を放ち、一枚のカードを生成した。"

    "それは、私自身の≪未練≫のカードだった。"


    play music audio.rinka
    scene ecg rinkaresurrection a with dissolve_long

    "――普通の日常。"

    python:
        add_character_cards("rnk", ["1_regret"])
        add_character_cards("mhr", ["1_regret"])

    "ありふれた言葉だけれど、つまり、未来の可能性だ。"

    "私はまだ、何の未練もないと思っていた。"

    "それでも生きたいと思っていた。"

    "その矛盾の答えに、ようやくたどり着くことができた。"

    "答えがないことそれ自体が、私の答えだったのだ。"

    "みんなともっと一緒にいたい。"

    "おばあちゃんみたいに、慕われる大人になりたい。"

    "少女漫画のような恋をしてみたい。"

    "面白い映画で感動してみたい。"

    "コーヒーをもっと美味しくいれたい。"

    "お店で出せるような料理を作れるようになりたい。"

    "大学にも行ってみたい。"

    "お酒も飲めるようになりたい。"

    "――たい。"

    "――――たい。"

    "――――――たい。"

    "私自身が把握しきれないほど、無限の小さな願望がある。"

    "何者になるのか分からないからこそ、私の可能性全てが、私の未来そのものが、今の私の未練だったのだ。"

    "悩みながら、迷いながら生きること自体が私にとっての普通であり、日常。"

    "どうしても捨てられない、強い想い。"

    "作られたカードを、私は胸に抱き留めた。"


    voice get_voice_filename("rnk")
    rinka "「まさか、真央に気付かされるなんてね」"

    "私は思わず、笑っていた。"

    "すごく久し振りに、笑うことができた。"

    "私のこれからの行動全てが、未来なのだ。"

    "私の未来に無限に広がる可能性を、希望を、つかめるのは私しかいない。"

    "だってそれは私のものだ。"

    "一つだけ。"

    "たった一つだけ、今すぐにつかまなければいけない可能性があった。"


    voice get_voice_filename("rnk")
    rinka "「直未を、取り戻す」"

    "私は拳を天井に向け、握った。"

    "真央は悲しんでいていいといったけれど、悲しんでいる場合じゃない。"

    "もちろん自分を責めてる場合でもない。"

    "私は今、運命の分水嶺に立っている。"

    "前を向いて、自分にできることをするべき時だ。"

    "ユウを、脱落させる。"

    "彼が何を言ったかなんて関係ない。"

    "私は私の意志で、未来を手に入れてやるんだ。"

    "普通を、取り戻してやるんだ。"


    voice get_voice_filename("rnk")
    rinka "「待っててね、直未――」"

    "私が人の命を踏み台にして生きるべきかなんて、分からないけど。"

    "私の未来は、私が決める。"









    python:
        set_info_scene("96")
        set_info_time("night")
        set_info_location("05")

    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "ユウを指名すること、それが私の今為すべきことだった。"

    "彼を脱落させれば、直未を殺害したことがなかったことになるはずだ。"

    "彼の起こした爆弾テロ自体が、なかったことになるのだろう。"

    "思えば――できることなら思い出したくない光景だけど――わざわざユウくんが直未にとどめを刺したのは、その可能性を残すためかもしれない。"

    "爆弾や火事が直未の死因になれば、直未の死自体はそのままで、事故に巻き込まれたという形で運命が変わるに留まってしまうかもしれないからだ。"

    "彼は私に殺されるため、用意周到に準備していたのだ。"

    "だが≪未練≫のカードが消滅してしまった今、私はまだ彼の≪氏名≫と≪死因≫しか持っていない。"

    "しかも、彼をこのまま脱落させればいいというものではない。"

    "彼が取り戻した記憶に何が隠されていたのか。"

    "彼はどうして私に指名されたがっているのか。"

    "私はユウくんのことを正しく知った上で、脱落させるつもりだ。"

    "今までのように同情するつもりはない。"

    "彼が直未の命を奪った――その事実だけは、何があっても揺るがないのだから。"

    stop music fadeout 1
    play se "doorbell01"

    "その時、またインターホンが鳴った。"

    "この時間に来客はないだろうから、真央が忘れ物でもしたのだろうか。"

    "インターホンの通話のボタンを押したとき、私は思わず尻餅をついてしまった。"







    voice get_voice_filename("ode")
    odette_num "「よう嬢ちゃん、景気はいいかい？」"

    "訊ねてきたのが真央だったら、どんなによかったことか。"

    "そこにいたのは、Ⅺの女性であったのだ。"









    python:
        set_info_time("lnight")
        set_info_location("04")

    scene bg lion01 night with fade_long
    play music audio.impatience
    pause 1

    $ show_hud()

    "無視をする方が恐かったので、私は彼女をライオン館に上げていた。"

    "放っておいたら、彼女は平気で扉くらい壊しそうだ。"

    show ode noj nor nor rev at std_cl with std_in


    voice get_voice_filename("ode")
    odette_num "「喫茶店か。中々雰囲気がいいねぇ」"

    "近くで見る彼女は、牛塚さんの家で見るよりも大きく感じた。"

    "見慣れたライオン館の中で見る分、彼女の迫力がよりはっきりと分かるのだ。"

    "いきなり襲っては来ないところから見ると、私を取って食おうというわけではないらしい。"

    "この距離だったら、私なんて３秒もかからず無力化されてしまう。"

    "彼女が話そうとしていることが、不幸中の幸いだった。"

    show ode noj arm smi rev with std_change


    voice get_voice_filename("ode")
    odette_num "「悪いな。もう寝る時間だったかい？」"


    show rnk mos nor nor at std_cr with std_in
    voice get_voice_filename("rnk")
    rinka "「…………いえ」"

    show ode noj nor lau rev with std_change


    voice get_voice_filename("ode")
    odette_num "「かかっ。現実世界で会うのは２週間ぶりくらいか。元気してたァ？」"

    show rnk mos nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「目的は何ですか？」"

    show ode noj nor gla rev with std_change


    voice get_voice_filename("ode")
    odette_num "「あーあ、どこ行っても警戒されるねぇ、あたしはさ。ミハルって嬢ちゃんの方がもう少しフレンドリーだったけどな」"

    show rnk mos nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴？　海晴に……何かしたんですか？」"

    "海晴が人質にとられた――その考えがまず頭に浮かんだ。"

    "しかしおかしい。"

    "運命の大広間でのやり取りで、私たちは仲間割れしたように見せていたのに。"

    show ode noj gra smi rev with std_change


    voice get_voice_filename("ode")
    odette_num "「あー、やっぱてめーらは仲間割れなんてしてなかったわけだ。だがその反応を見ると、あの嬢ちゃんが今どうしてるかは知らなそうだな」"

    show ode noj arm smi rev with std_change


    voice get_voice_filename("ode")
    odette_num "「無理もないか。後輩が殺されて、悲しまない方がおかしいか」"

    show ode noj arm irr rev with std_change


    voice get_voice_filename("ode")
    odette_num "「てめーの目が死んでないところを見ると、ここ数日でようやく立ち上がったってとこか」"

    "話しながら考えをまとめるタイプと、アランさんはこの人のことを評価していた。"

    "まさにその通りだ。"

    "私と話し、私の反応を見ながら、自分の推理を正しい方向に持っていっている。"

    "私は、ただでさえ萎縮して思考が鈍っている。"

    "せめて、背筋だけでも伸ばしていよう。そうすれば、自然と勇気も湧いてくる。おばあちゃんの口癖だ。"


    stop music fadeout 1

    show rnk mos nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「もう一度聞きます。海晴に何かしたんですか？」"

    show ode noj arm smi rev with std_change


    voice get_voice_filename("ode")
    odette_num "「ああ、その調子だ嬢ちゃん。それくらいの気概がなくちゃ、あたしと話す資格はねぇ」"

    show ode noj arm ser rev with std_change


    voice get_voice_filename("ode")
    odette_num "「ミハルってのは、そんなに弱く見えるかい？」"

    show rnk mos nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「いいえ。少なくとも私よりはずっと――強い」"

    show ode noj arm smi rev with std_change


    voice get_voice_filename("ode")
    odette_num "「ほう、いい答えだ」"


    play music audio.odette

    show ode noj gra smi rev with std_change

    voice get_voice_filename("ode")
    odette "「あたしはオデット・マランソン。ま、とりあえずこれで警戒レベルは下げてくれ」"

    "彼女が言うと、持って来ていたカードブックが光を放った。"

    $ add_character_cards("rnk", ["11_name"])

    "作られたのは、彼女の≪氏名≫のカード。"

    show rnk mos nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「どうして……？」"

    show ode noj nor nor rev with std_change

    voice get_voice_filename("ode")
    odette "「あたしはてめーと話をしに来たんだ。てめーにあたしの名前を知られたところで、負ける気はしない」"

    show ode noj gra gla rev with std_change

    voice get_voice_filename("ode")
    odette "「何より初めのビビりようからして、あたしのカードを持ってないことは分かってたしな」"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「だったら名前くらい明かして、信頼関係の第一歩にでもしようじゃねーか」"

    show rnk mos nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私は――教えませんよ」"

    show ode noj arm ser rev with std_change

    voice get_voice_filename("ode")
    odette "「ああ、その心配はいらねぇ。リンカ・シシマイ。この場所が割れてる時点で、≪氏名≫がばれてるって分かってただろうけどよ」"

    $ add_character_cards("rnk", ["1_name"])

    "彼女の言う通りだ。"

    "ライオン館を突き止めているのに私の名前を知らない方が不自然だ。"

    show rnk mos nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたが牛塚さんのときみたいにこの家を襲いに来たわけじゃないってことは分かりました」"

    show ode noj nor tro rev with std_change

    voice get_voice_filename("ode")
    odette "「最初からそう言ってるだろ。そうだな、うーん。あえてこう言ってみるか」"

    show ode noj nor lau rev with std_change

    voice get_voice_filename("ode")
    odette "「あたしは、てめーを助けに来てやったんだ」"

    show rnk mos nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私を、助ける？　冗談はやめてください」"

    show ode noj arm smi rev with std_change

    voice get_voice_filename("ode")
    odette "「まあまあ遠慮しなさんな。ユウを脱落させたくても、一歩先に進む手段がないってのがてめーの状況だろう？」"

    show ode noj arm irr rev with std_change

    voice get_voice_filename("ode")
    odette "「さあて一から話すか。おい、コーヒーくらい出してくれ」"

    "オデットさんは慌てる私に視線も向けず、テーブルに座ってしまった。"

    "仕方がないので、私は自分の分も一緒にコーヒーを淹れることにした。"





    stop music fadeout 1
    scene ecg nighttalkO2 glo with fade_long
    play music audio.nichijo01
    pause 1


    voice get_voice_filename("ode")
    odette "「ふむ。中々いい味だ。てめー、年の割には努力してるじゃねえか。上出来だ」"

    "オデットさんはコーヒーを飲んだ後、再び席から立って伸びをしていた。"

    "肉なら何でもいい、酒なら何でもいい、とそんな豪快な人かと思っていたが、豆の種類や焙煎の仕方など言い当てられ、繊細な舌を持っていることに驚かされてしまった。"

    "コーヒーを飲みながら、私たちは話をしていた。"

    "まず聞いたのは、ユウの状況についてだ。"

    "彼は日本のテロ組織と関わりがあり、元々電車で自爆テロを起こす計画の実行犯を務めるつもりだったそうだ。"

    "私と直未が巻き込まれたのは、まさにその事件だ。"

    "もっともこのこと――つまり私の≪死因≫は、さすがにオデットさんたちには知られていないようだ。"

    "次に、海晴のこと。"

    "海晴とオデットさんは会っていたどころか、海晴・オデットさん・フェデリーコさん・Ⅸの男性――スケールさんとで協力関係を結んでいるという。"

    $ add_character_cards("rnk", ["9_name"])

    "その協力関係の目的は、アランさんの脱落。"

    "私は彼と直接話したことがあるからこそ、一概に悪い人なのかどうか判断しかねてはいるが、強敵であることに間違いはない。"

    "だが驚くべきことに、海晴の提案によりユウを脱落させることを最優先にしているらしい。"

    "海晴の目的は私と同じ。"

    "直未を――救うためだそうだ。"

    "動機不明の爆破テロが飴茶で起きている以上、選定と無関係と思う方が難しいだろう。"

    "ユウが犯人であり、飴茶には海晴と私が通っているのだ。"

    "ユウの真の目的が「私に自分を指名させること」であるのを知っているのは私だけで、オデットさんたちは「選定参加者への挑発」という推測をしているらしい。"


    play music audio.investigation
    scene ecg nighttalkN2 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「海晴が、あなたたちと……」"

    scene ecg nighttalkO2 glo with dissolve


    voice get_voice_filename("ode")
    odette "「てめーらが内輪揉めしているって情報があるからこそ、スケールはミハルを誘ったんだろうよ」"


    voice get_voice_filename("ode")
    odette "「あたしを騙すには甘すぎるが、てめーらの考えは悪くねぇ。フェデリーコの馬鹿もスケールも、リンカとミハルは仲違いしたままだと思ってるみてぇだからな」"

    "だが、そのことはオデットさんが私のところに来る理由にはならない。"

    "むしろ彼らは協力関係なのだから、反対だ。"

    show ecg nighttalkO2 ser with ecg_change


    voice get_voice_filename("ode")
    odette "「ユウを脱落させた後、連中はアランだけじゃねぇ。３人で組んであたしのことも脱落させるつもりさ」"

    scene ecg nighttalkN2 que with dissolve


    voice get_voice_filename("rnk")
    rinka "「でも海晴がそんな、嘘をつくようなこと……」"

    "しない、とは言い切れなかった。"

    "海晴の強さは、ぶれない強さだ。"

    "でも、海晴はただ自分の利益のために人を裏切ることはしない。"

    "直未のためか、あるいは私のためか。"

    "それは、簡単に予想がつくことだった。"

    scene ecg nighttalkO2 glo with dissolve


    voice get_voice_filename("ode")
    odette "「ま、あの嬢ちゃんはあたしがスケールの腹に気付いていることも、想定しているだろうよ」"


    voice get_voice_filename("ode")
    odette "「もっとも言った通り、ユウを脱落させ、アランのカードを揃える見通しが立つまではあたしに白羽の矢は立たねえだろう」"


    voice get_voice_filename("ode")
    odette "「あたしの力を、連中は過小評価してるはずはねぇからな」"

    "彼女の自己評価の高さには、私は納得することしかできない。"

    "個人で比べるものではないけれど、もしこの≪女神の選定≫に強さというものがあるとすれば、アランさんに匹敵するのはオデットさんしかいないと思う。"

    "しかしここまで聞いてもなお、オデットさんが私に会いに来る理由にはならない。"

    show ecg nighttalkO2 puc with ecg_change


    voice get_voice_filename("ode")
    odette "「しかしあたしとしては、ユウを脱落させた後に連中と敵対するのも予定調和でつまらない」"


    voice get_voice_filename("rnk")
    rinka "「つまらないとか……面白いとか。関係あるんですか？」"

    show ecg nighttalkO2 glo with ecg_change


    voice get_voice_filename("ode")
    odette "「当たり前だ。人生楽しめねーなら死んだ方がマシさ」"


    voice get_voice_filename("rnk")
    rinka "「……分かりません」"


    voice get_voice_filename("ode")
    odette "「かかっ、理解なんざ求めてねーよ」"


    voice get_voice_filename("ode")
    odette "「――ま、ってわけで、あたしの方から裏切ってやるってわけだ」"

    "オデットさんはにやりと笑い、そう言い切ってみせた。"

    scene ecg nighttalkN2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「そろそろ、ちゃんと話してください。私を助けに来たっていうのはどういう意味なんですか？」"

    scene ecg nighttalkO2 ser with dissolve


    voice get_voice_filename("ode")
    odette "「言葉通りの意味だよ。てめーは後輩の死を≪なかったことにする≫ために、ユウを脱落させたいが、手段がねえ」"

    show ecg nighttalkO2 puc with ecg_change


    voice get_voice_filename("ode")
    odette "「たかが一人死んだくらいで女々しい嬢ちゃんだが……」"


    stop music fadeout 1

    scene ecg nighttalkN2 cla with dissolve


    voice get_voice_filename("rnk")
    rinka "「たかがじゃないだろ！　直未の命を、たかがなんて言うな」"

    "やってしまった、と思った。"

    "しかし、後悔はしていなかった。"

    "直未の命をたかがなんて言われて、黙っているわけにはいかない。"

    show ecg nighttalkN2 ser with ecg_change

    "私は大声を出したフォローを入れることもせず、オデットさんを睨みつけた。"


    play music audio.investigation

    scene ecg nighttalkO2 glo with dissolve


    voice get_voice_filename("ode")
    odette "「かかっ、上出来だ。てめーが今の発言を聞き逃してたら、あたしはこのまま帰るつもりだった」"

    show ecg nighttalkO2 ser with ecg_change


    voice get_voice_filename("ode")
    odette "「それに、その調子で喋れよ。敬語なんてのはあたしは知らねー」"


    voice get_voice_filename("rnk")
    rinka "「私を、試した？」"


    voice get_voice_filename("ode")
    odette "「ああそうさ。悪いかい？」"


    voice get_voice_filename("ode")
    odette "「あたしはてめーを助けに来たって言ったが、無条件じゃねぇ。その選択を迫る意味があるかどうかを、試したんだ」"


    voice get_voice_filename("ode")
    odette "「あのガキ、そしてあのガキの所属する≪ＮＵＬＬ日本支部≫の残党は今週末の土曜日――つまり明日、再びテロを起こすつもりだそうだ」"


    voice get_voice_filename("ode")
    odette "「最後にでっかい花火をあげようって魂胆だろうな。連中の標的は、東京タワーだ」"

    scene ecg nighttalkN2 sur with dissolve


    voice get_voice_filename("rnk")
    rinka "「嘘っ……！」"


    voice get_voice_filename("ode")
    odette "「すでに計画は動き出している。爆弾作成に必要な硝酸アンモニウムや軽油のイレギュラーな動きがあったって情報は出てるみたいだ」"

    "硝酸アンモニウムというのは肥料にも使われるらしいけれど、素人が使うものではないそうで、彼らが口裏を合わせて入手しても完全には隠しきれないそうだ。"

    "仕組みはよく分からないが、爆弾として威力があるだけでなく、同梱された酸化鉄とアルミニウムの粉末によるテルミット反応で、延焼効果もあるそうだ。"

    "つまり、燃やす爆弾。"

    "ユウが電車の中で使用したのはまさしく、その爆弾だろう。きっと、直未のいた空き教室を爆破したのも同じものに違いない。"

    scene ecg nighttalkO2 ser with dissolve


    voice get_voice_filename("ode")
    odette "「後先なんて考える余裕はないだろうから、派手にやるだろうな。休日の東京タワーで爆発なんて、何人死ぬか分からねぇ」"


    voice get_voice_filename("ode")
    odette "「それに、ユウは選定の参加者だから、死なねぇ。普通なら犯人も死亡して終わりの自爆テロが、終わらねぇってわけだ」"

    scene ecg nighttalkN2 ser with dissolve


    voice get_voice_filename("rnk")
    rinka "「そんな……分かってるんだったら、止めないと！」"


    voice get_voice_filename("ode")
    odette "「かかっ、優しいねぇ。だが、あたしは別にこの国の人間が何人死のうが知ったことじゃない」"

    "彼女の言い方に嫌気がさし、私はまたオデットさんを睨んだ。"

    "オデットさんは指を一本立てて突き出し、私の言葉を止めて続ける。"

    scene ecg nighttalkO2 glo with dissolve


    voice get_voice_filename("ode")
    odette "「だが、あたしが動けば、チンケなテロごとき止めるのは容易い」"

    "大げさな発言だったが、反面、真実にも聞こえるのが彼女の凄み。"


    voice get_voice_filename("rnk")
    rinka "「でも、テロなら警察が出動した方が……」"

    show ecg nighttalkO2 ser with ecg_change


    voice get_voice_filename("ode")
    odette "「連中の計画を知ってるのは、あたしらみたいな裏の人間だ。たとえ僅かでも警察と関わりたがる奴はいねぇ」"


    voice get_voice_filename("ode")
    odette "「しかも、テロが起きた方が利益が得られる連中ばかりだぜ？　記事は金に変わるからよ」"


    voice get_voice_filename("ode")
    odette "「何より、わけのわからねぇ偶然に守られて、自爆しても死なねぇ人間が混ざってるんだぞ？　警察の被害も相当なモンになるだろうなぁ」"

    "確かに彼女の言う通りかもしれない。"

    "≪女神の選定≫の参加者だから死なないといって、信じる人はいないだろう。"

    "テロ組織というなら彼らの武器は爆弾だけとも思えないし、被害は未知数だ。"

    show ecg nighttalkO2 puc with ecg_change


    voice get_voice_filename("ode")
    odette "「あたしとしては、スケールやフェデリーコ、一応ミハルからも狙われている以上とっとと勝負をつけたいんだ」"


    voice get_voice_filename("ode")
    odette "「ここまで来たら言いたいことは分かるな？」"


    voice get_voice_filename("rnk")
    rinka "「……言って」"

    show ecg nighttalkO2 ser with ecg_change


    voice get_voice_filename("ode")
    odette "「あたしが、テロを止め、てめーとユウが接触する機会を作ってやる」"


    voice get_voice_filename("ode")
    odette "「てめーなら、奴から≪未練≫を引き出せるはずだ。ジジイの家に出入りしてたのも、ジジイの脱落後にガキと話してたのも、裏は取れてるんだ」"


    voice get_voice_filename("ode")
    odette "「ユウを脱落させて、後輩を救える。見知らぬ何人もの国民も救える」"


    play music audio.impatience

    show ecg nighttalkO2 glo with ecg_change


    voice get_voice_filename("ode")
    odette "「ただし、これは取引だ」"


    voice get_voice_filename("ode")
    odette "「代償は、リンカ、てめー自身のカードだ。≪死因≫と≪未練≫、ってわけだ」"

    show ecg nighttalkO2 ser with ecg_change


    voice get_voice_filename("ode")
    odette "「てめーがユウの情報を得た時点で、教えてもらう。つまり、ユウと同じ選定でてめーは終わりだ」"


    voice get_voice_filename("ode")
    odette "「ただし確信を持って言えるぜ。運命は元通りになり、後輩が無事助かるってな」"

    scene ecg nighttalkN2 sur with dissolve

    "ユウくんと私が脱落して、運命が元通りになること。"

    "その説得力はあった。"

    "私が死んでいるということは、直未は私の死を看取っているということだ。"

    "それが、本来の死の運命なのだから。"

    "オデットさんはそのことを知らないだろうけれど、彼女の言葉は私の胸の奥に響いていた。"

    scene ecg nighttalkO2 glo with dissolve


    voice get_voice_filename("ode")
    odette "「さあ、選べ。確実な方法で後輩を助けるか、不確実だが自分で頑張るか。どうする？」"





    if flags_mhr_koukando < 6:
        jump f007_1.s1_end_B


label f007_1.s1_start:
    menu:
        "私は――。"
        "条件を飲む。":


            $ persistent.s12_1_seen = True
            $ grant_hear_all()
            jump f007_1.s1_end_B
        "条件を飲まない":


            $ persistent.s12_2_seen = True
            $ grant_hear_all()
            jump f007_1.s1_end_A


label f007_1.s1_1:


    if flags_007_1_s1_counter_A == 1 and flags_007_1_s1_counter_B == 0:

        voice get_voice_filename("ode", 313)
        odette "「こいつはまさしくてめーの命運を左右する選択だ。よーく考えた結果かい？」"

        jump f007_1.s1_start



    if flags_007_1_s1_counter_A == 2:
        jump f007_1.s1_end_B
    else:
        jump f007_1.s1_end_A


label f007_1.s1_2:



    if flags_007_1_s1_counter_B == 1 and flags_007_1_s1_counter_A == 0:

        voice get_voice_filename("ode", 314)
        odette "「こいつはまさしくてめーの命運を左右する選択だ。よーく考えた結果かい？」"

        jump f007_1.s1_start



    if flags_007_1_s1_counter_B == 2:
        jump f007_1.s1_end_A
    else:
        jump f007_1.s1_end_B

label f007_1.s1_end_A:



    $ flags_route_A = True

    scene ecg rinkaresurrection b with dissolve


    voice get_voice_filename("rnk", 962)
    rinka "「っざっけんなよ！」"

    scene ecg nighttalkO2 puc with dissolve


    voice get_voice_filename("ode", 315)
    odette "「……ひゅーぅ」"



    play music audio.rinka

    scene ecg rinkaresurrection b with dissolve


    voice get_voice_filename("rnk")
    rinka "「さっきからずっと、上から目線で！」"


    voice get_voice_filename("rnk")
    rinka "「あなたは重要なところを隠してる。あなただけじゃ……ユウを脱落させられないってことを」"


    voice get_voice_filename("rnk")
    rinka "「そしてきっと、あなたは海晴たちが彼の≪未練≫を手に入れられないことも読んでいるはず」"


    voice get_voice_filename("rnk")
    rinka "「助けるだなんて言ってるけど、そんなの嘘だ」"


    voice get_voice_filename("rnk")
    rinka "「私たちは、対等だ。私も、あなたに力を貸すんだ」"

    scene ecg nighttalkO2 ser with dissolve


    voice get_voice_filename("ode")
    odette "「後輩ちゃんのことはいいのかい？」"

    scene ecg rinkaresurrection b with dissolve


    voice get_voice_filename("rnk")
    rinka "「だから言ってるんだ。私も……って」"


    voice get_voice_filename("rnk")
    rinka "「私はユウを脱落させて、後輩を救う。ついでに、無関係な人がテロに巻き込まれるのも防ぐ」"


    voice get_voice_filename("rnk")
    rinka "「その手伝いを、させてやる！」"

    "私は精一杯の力を込めて言い放った。"

    "その全てが、本心であった。"

    "分かっていたのだ。"

    "いや、ヒントを出していた。"

    "自分が楽しいかどうかで判断をすると。"

    "人生を楽しめないなら死んだ方がマシだと"

    "だったら楽しませてあげればいい。"

    "私が条件を飲むなんて、それこそ彼女の予定調和だろう。"

    scene ecg nighttalkO2 glo with dissolve


    voice get_voice_filename("ode")
    odette "「かかっ、上等。そういうのを待ってたんだ」"


    voice get_voice_filename("ode")
    odette "「コーヒー代にしては高くつくが、やってやろうじゃねーか」"

    "この人は、理屈で動く人じゃないんだから。"

    jump f007_2

label f007_1.s1_end_B:



    $ flags_route_B = True


    play music audio.thebonds

    "オデットさんの言う通りにすれば、直未は助かる。"

    "確実に、直未は助かる。"

    "直未。"

    "――直未。"

    "直未の顔が、脳裏に浮かぶ。"

    "私は脱落しても、直未が助かるならそれでいい。"

    "元々、直未を助けて失った命なのだ。"

    "迷うことなんて、何もないのだ。"

    scene ecg nighttalkN2 ser with dissolve


    voice get_voice_filename("rnk", 971)
    rinka "「約束は守ります。代わりに――あなたも、守ってください」"

    scene ecg nighttalkO2 glo with dissolve


    voice get_voice_filename("ode", 319)
    odette "「かかっ、そうかいそうかい」"


    voice get_voice_filename("ode")
    odette "「てめーにとって最善かしらねーが、あたしにはどっちでもいいことだしな」"

    show ecg nighttalkO2 ser with ecg_change


    voice get_voice_filename("ode")
    odette "「任せな。丁度、あたしも派手に暴れたかったところなんだ」"




    jump f007_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

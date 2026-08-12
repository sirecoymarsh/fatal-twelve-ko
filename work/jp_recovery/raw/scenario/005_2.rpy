

label f005_2:









    python:
        set_info_scene("64")
        set_info_date(5, 31, "thu")
        set_info_time("morning")
        set_info_location("14")



    stop music fadeout 2
    scene bg schoolgate noon with fade_longest
    play music audio.nichijo02
    pause 1

    $ show_hud()

    "眠ればすぐに朝が来る。"

    "選定のない日は、少なくともそれが当たり前だった。"

    "いつものように準備を終えて、登校していた。"

    "今日は夕方に牛塚さんの家で手料理を作るという予定が入っているので、お店は開けられない。"

    "最近はお店を閉めがちで、おばあちゃんへの言い訳もネタが尽きそうだ。"

    "もっとも私がお店を開けたところで売り上げは微々たるものどころか時にはマイナスなこともあるくらいだし、そもそも強制されていることでもないため、おばあちゃんは強く追及はしてこない。"

    "私が何か特殊な状況にあることは、気付いているだろうから。"

    "もちろんそれは女神の選定なんて本当の意味で特殊なものではなく、テストや人間関係などでだろうけれど。"

    "私は成績が悪い方なので、やはりその辺りを疑われているだろう。"

    show nom uni nor nor at std_cl with std_in

    "校門に入ったあたりで、前の方に直未を見つけた。"





    menu:
        "友達と一緒にいるが……。"
        "声をかける":

            $ persistent.s10_1_seen = True
            $ grant_hear_all()
            jump f005_2.s1_1
        "声をかけない":

            $ flags_mhr_koukando += 1

            $ persistent.s10_2_seen = True
            $ grant_hear_all()
            jump f005_2.s1_2


label f005_2.s1_1:

    "友達と一緒にいるので少し迷ったが、挨拶だけと思い、声をかけた。"

    show rnk uni nor smi at std_cr with std_in

    voice get_voice_filename("rnk", 728)
    rinka "「直未、おはよ」"

    show nom uni nor lau rev with std_change

    voice get_voice_filename("nom", 263)
    naomi "「凛火先輩！　おはようございます」"

    "後ろから声をかけた私に振り向いて、直未は笑顔で答えてくれた。"

    "その後は、友達に「文化祭のためにコーヒーを教えてくれた人」というような紹介をされた。"

    "避けられている、という方の私の噂も知っていたようだが、同一人物だとは思われていなかったらしい。"

    "それでも露骨に怖がられることはなく、むしろお礼を言われてしまった。"

    "文化祭の準備は順調らしい。"

    "校舎まで三人で話しながら歩き、玄関でそれぞれの教室へと向かった。"

    jump f005_2.s1_end

label f005_2.s1_2:


    "声はかけない方が、いいだろう。"

    "私以外に一緒に過ごす人がいるなら、その方がいいのだ。"

    "私と多く関わるということは、その分、選定に巻き込まれてしまう危険が生まれるから。"

    show nom uni fal sur with std_change

    voice get_voice_filename("nom", 264)
    naomi "「ふぎゃっ」"

    "後ろから見ていたら、直未は何もないところでバランスを崩していた。"

    show nom uni nor smi with std_change

    "隣にいた友達に支えられて、「えへへ」と笑っていた。"

    "私に気付くこともなく、そのまま校舎へ向かって行った。"

    hide nom with std_out

    "私は歩く速度を少し落として、玄関で鉢合わせないようにした。"

    jump f005_2.s1_end



label f005_2.s1_end:







    python:
        set_info_time("evening")
        set_info_location("04")


    stop music fadeout 1
    scene bg lion01 evening with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "学校から一度家に帰った私は、いくつか調味料などを持って行くことにした。"

    "いただいたお金で調味料を買い揃えるのは難しいし、一度しか行かないのだから余ってしまう。"

    show rnk uni nor nor at std_c with std_in

    voice get_voice_filename("rnk", 729)
    rinka "「カレーでいいかな。うーん、カレーならおばあちゃんのレシピがあったはず……」"

    "以前、ライオン館ではカレーも提供していた。"

    "私も何度か手伝いをしたことはあるが、最初から一人で作ったことはなかった。"

    "レシピがあればそうそう失敗することもないだろうし、カレーなら日持ちもするので、丁度いいだろう。"

    "調味料とスパイス、そして鍋と余っているタッパーを持ち、私は牛塚さんの家へと向かうことにした。"







    $ set_info_location("27")



    stop music fadeout 1
    scene bg shigetsugu03 with fade_long
    play music audio.comicaldays
    pause 1

    $ show_hud()

    "牛肉、じゃがいも、玉ねぎ、にんじん、りんご、ヨーグルトなど必要なものを準備して、牛塚さんの家に上がった。"

    "途中警戒しながら歩いて来たが、カルミナーティさんやⅪの女性の姿はなかった。"

    "夕方で人通りが多いから、というのもあるのだろう。"

    "元々噂が立ちやすい家なので、私が行けばそれはそれで別の噂が立つような気もしたが、一度きりなら大丈夫だろう。"

    show sig sta inn lau rev at std_c with std_in

    voice get_voice_filename("sgt")
    ushizuka "「おお、待っとったよ」"

    show yuu sta nor nor rev at std_l with std_in


    voice get_voice_filename("yuu")
    yuu_unk5 "「あ、お姉ちゃん！　聞いたよ。ご飯作ってくれるんだよね？」"

    show yuu sta lau lau rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ボク、何でも手伝うから！　料理って、一回してみたかったんだぁ」"

    show rnk uni arm nor at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「お姉ちゃん……」"

    "そう言っている時点で、私が母親代わりに手料理を作るという案自体が破綻しているけれど。"

    "買い物袋ごと台所に持ち込んで、牛塚さんにはレシートとお釣りを渡した。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「そっか、じゃあ……じゃがいもとにんじんの皮を剥いてもらおうかな」"

    show yuu sta nor kir rev with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「うん、分かった！」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「その前に、まず手洗いね」"

    hide yuu
    hide rnk
    hide sig
    with std_out

    "エプロンをつけて、まずは手を洗う。"

    "少年も同じように手を洗ったので、私はじゃがいもとにんじんを手渡した。"

    "牛塚さんはと言うと、居間でテレビをつけて寝転がっていた。"

    "私の方はお肉の下処理からしよう。"

    "牛肉を一口大に切り分けて塩コショウで下味をつける。"

    "筋のところには噛みやすいように切れ目を入れておく。"

    "すりおろしたリンゴとヨーグルト、はちみつ、そしておばあちゃんのレシピ通りに混ぜたスパイスと一緒にお肉を小さなビニール袋に入れ、揉み込む。"




    voice get_voice_filename("yuu")
    yuu_unk5 "「…………あの」"

    scene ecg rinyuucooking a with dissolve_long

    "少年に話しかけられて見ると、じゃがいもを持ったまま上目遣いで私を見ていた。"



    voice get_voice_filename("yuu")
    yuu_unk5 yuu_unk5 "「どうすればいいの？」"


    voice get_voice_filename("rnk")
    rinka "「あーそっか。そこからか……。ピーラーは……なさそう。よし、じゃあ見ててね」"

    "私は包丁でじゃがいもの芽をとって、皮の剥き方を教えてあげた。"

    show ecg rinyuucooking b with ecg_change



    voice get_voice_filename("yuu")
    yuu_unk5 "「すごい！」"


    voice get_voice_filename("rnk")
    rinka "「なんにもすごくないよ。じゃあ、やってみて。ああ、包丁は危ないから気をつけてね」"

    "料理をあまりしないからなのだろうか、妙に切れ味のいい包丁だった。"



    voice get_voice_filename("yuu")
    yuu_unk5 "「ボクが砥いだ包丁で、ちゃんと料理できるなんて……」"

    "料理以外の用途で何故包丁を研ぐ必要があるのか、怖くて詳しくは聞けなかった。"

    "ともかく彼は手が器用なのか、私よりも綺麗にじゃがいもを剥いていた。"

    "にんじんの方も問題なく、野菜を切るのもお願いすることにした。"

    show ecg rinyuucooking c with ecg_change



    voice get_voice_filename("yuu")
    yuu_unk5 "「目が……うう、痛い……」"

    show ecg rinyuucooking d with ecg_change


    voice get_voice_filename("rnk")
    rinka "「ははは、玉ねぎを切るとそうなっちゃうよね。あ、目を擦ったらもっと駄目だよ！」"

    show ecg rinyuucooking e with ecg_change



    voice get_voice_filename("yuu")
    yuu_unk5 "「お姉ちゃん、やっと笑ったね！」"

    show ecg rinyuucooking a with ecg_change


    voice get_voice_filename("rnk")
    rinka "「えっ……」"

    show ecg rinyuucooking b with ecg_change



    voice get_voice_filename("yuu")
    yuu_unk5 "「ずっと怖い顔だったけど、今は何かちょっと楽しそう。敵じゃなくって、本当によかった」"

    "言われてみれば、料理を始めてからの私は完全に気を抜いていた。"

    "いや、牛塚さんが私の荷物を漁ったりしないかちらちら見てはいたけれど、それでも、緊張感がなかったのは事実だ。"



    voice get_voice_filename("yuu")
    yuu_unk5 "「ボクね、楽しみなんだ。カレーはあっためるやつで食べたことあるけど、どうやって作るか知らないもん」"



    voice get_voice_filename("yuu")
    yuu_unk5 "「ただ野菜切っただけなのに、どうなるのかなーって」"

    show ecg rinyuucooking e with ecg_change


    voice get_voice_filename("rnk")
    rinka "「……そっか。じゃあ、頑張ろうね」"

    "私はまた、表情を綻ばせていた。"

    "好奇心できらきらしている目を見ていると、自然とそうなってしまう。"

    "同時に、どうして私たちは選定の参加者なのだろう――そうも、思っていた。"






    scene bg shigetsugu03
    show yuu sta lau lau at std_c
    with fade_long
    pause 1


    voice get_voice_filename("yuu")
    yuu_unk5 "「わーい、できたー！」"

    "煮込む時間も含めて、結局２時間弱かかってしまったが、無事完成した。"

    "鍋からふわっと立ち込める濃厚な香りは、おばあちゃんの作ってくれたカレーにそっくりだ。"

    "味見もしているので大丈夫かとは思うが、人に食べてもらうとなると多少緊張する。"

    show sig sta nor nor rev at std_l with std_in

    voice get_voice_filename("sgt")
    ushizuka "「おおっ、ご馳走じゃのう」"

    show rnk uni nor que at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「お待たせしました……これで、いいんですよね？」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子もとっても喜んでおるしの。おぬしは食べていかんのか？」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「まさか。ここまで来たんですから、私もいただきます」"

    show yuu sta nor pun with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「はーやーくー！　食べよーよ！」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おお、すまんすまん」"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「いっただきまーす！」"

    hide sig
    hide yuu
    hide rnk
    with std_out

    "彼らが食べ始めたのを見て、私も一口食べてみる。"

    "おばあちゃんの味にはまだ遠いけれど、うん、我ながら美味しい。"

    "こうやって食卓を囲むのは、あまり久し振りではなかった。"

    "ソーニャがいた時も、海晴とソーニャと三人で食事をした。"

    "選定が始まってからの方がこういう機会に恵まれるなんて、皮肉だ。"

    "恵まれる――いい加減認めざるを得ない。私はみんなで食べる食事を楽しんでいた。"

    show sig sta nor squ rev at std_l with std_in

    voice get_voice_filename("sgt")
    ushizuka "「ちょっと味が濃くないかのう」"

    show rnk uni arm nor at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「……文句言わないでください」"

    show yuu sta lau lau rev at std_c with std_in


    voice get_voice_filename("yuu")
    yuu_unk5 "「とっても美味しい！　お姉ちゃんの作ってくれたカレーとっても美味しいよ！」"

    "うんうん、いい子だ、と内心で彼のことを褒めてあげた。"

    show yuu sta lau que with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「おじいちゃん見た？　これ、ボクが切ったんだよ」"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「このニンジンか？　いもか？　とってもうまいのう」"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「わーい！」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「親バカならぬ、ジジバカ……？」"

    "まあ、喜んでもらえているならそれでいい。"

    "私はあまり会話に混ざることなく、黙々とカレーを食べていた。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「昔を、思い出すのう……」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「息子が初めて料理したのも、カレーじゃったかのう……。野菜を切って……喜んで……」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「どうして、今になって思い出すんじゃろうなぁ……」"

    "牛塚さんは、カレーの中に浮かぶ具材を見つめながらぼそりと呟いていた。"

    "湯気がまばらなまつ毛にあたって、細かい水滴を作っていた。"

    "カレーというのはいつの間にか、日本の家庭料理の代表になっている。"

    "私も作りながら、おばあちゃんのことを思い出していた。"

    "だから、牛塚さんが昔を思い出すのも無理はないと、思う。"

    "その時、チンと音が立ち、私は音のした方に意識を向けた。"

    "少年が、皿の端っこにスプーンを置いた音だった。"

    show yuu sta nor sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「昔って、そんなに大事なものなのかな？」"

    "彼の疑問に、私たちは答えなかった。"

    "少年は回想する牛塚さんに、見開いた目を向けていた。"

    "彼の大好きなおじいさんが思い出しているのは、決して彼自身のことではないのだ。"

    "そして彼は今、同じように回想する過去を失っている。"

    show yuu sta nor nor with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ボクは色々なことを忘れてる。でも、おじいちゃんを見てて思ったことがあるよ」"

    show yuu sta nor sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ボクの記憶の中に、こんな幸せで……ゆっくりした風景はなかった」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬし……」"


    play music audio.impatience

    show yuu sta hea pai with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「あ……うう……」"

    "彼は突然、頭を押さえて唸り始めた。"

    show rnk uni arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「ち、ちょっと！」"

    show yuu sta hea cla with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ううううう！」"

    "それは、彼と初めて現実世界で鉢合わせたときの様子に似ていた。"

    "あの時は私も痛みを感じたけれど、今は彼だけだ。"

    "すごい形相の牛塚さんが少年を寝かせた。"

    show sig sta nor pan rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「大丈夫かっ」"

    show yuu sta hea cla with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「うう……ああああっ」"

    show sig sta nor pan rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「落ち着くんじゃ……のう」"

    "牛塚さんの言葉が届いたのかは分からないが、少年はそのまま目を閉じ、意識を失ったかのように眠ってしまった。"

    "私は少年を寝室まで運ぶのを手伝うことにした。"







    python:
        set_info_time("night")
        set_info_location("25")



    stop music fadeout 1
    scene bg shigetsugu02 night with fade_long
    play music audio.investigation
    pause 1

    $ show_hud()

    "少年を布団に寝かせてから、私は残っていた自分のカレーを食べ終え、洗い物もしてしまった。"

    "余ったカレーはタッパーに移して冷蔵庫にしまった。"

    "明日以降、鍋で温め直してもらえば食べられる。"

    show sig sta nor tro rev at std_cl with std_in

    voice get_voice_filename("sgt")
    ushizuka "「時々、あるんじゃよ」"

    show rnk uni nor que at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「あの子があんな風になってしまうことが、ですか？」"

    "牛塚さんは無言で頷いてから、続ける。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子が何かのきっかけに記憶を取り戻そうとするとき……それが意識的か無意識なのかは分からんがともかく、頭痛に襲われているようなんじゃ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「その後は決まって寝てしまう。心配はいらんよ。数時間は目を覚まさんが、起きたら何事もなかったようにぴんぴんしとる」"

    "心配……自分と争うべき相手のはずなのに、奇妙なものだ。"

    "私もまた、彼のことを心配していたのだし。"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「すまんのう。予想できたはずだったんじゃが……あの子が嬉しそうで忘れておった」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「いえ……」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃが、あの子が料理も食事も喜んでおったのは本当なんじゃ」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「分かってます。おじいちゃん想いの優しい子……ですよね。選定がなければ、弟みたいに感じていたかもしれません」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「選定がなければ、わしらは出会いもせんかったがのう」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ。そうじゃのう。わしも改めて礼を言わせてもらおう」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ありがとう。幸せそうなあの子を見ることができて……わしもまた幸せじゃった」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……はい」"

    "思わず、目の奥に力が入ってしまった。"

    "こんなこと、言われている場合じゃないのに。"

    "どうしても、私の頭からそんな想いが離れなかった。"

    "私の感じたささやかな幸せと、向き合うべき現実がせめぎ合っている。"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「さて、ここからはおぬしが昨日言った通りにしよう」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「はい――お願いします」"

    "もう、関わらない。"

    "それが、一番なのだ。"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「タッパーは返さなくていいです。正直……私もちょっと楽しかったです。だから、あんまり負い目は感じないでください」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、元々気にしとらんから大丈夫じゃよ」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「さて、別れる前に約束じゃ。わしの≪死因≫を教えよう」"

    "牛塚さんは座りもせず、そう切り出した。"

    "彼がその約束を忘れていたならば、それはそれでいいと思っていた。"

    "彼の≪死因≫を聞いたところで、私は自分が指名に踏み切れるか分からなかったからだ。"

    "ここまで感情移入してしまえば、できない可能性の方が高い。その後悔と自己嫌悪に比べれば、知らない方がマシとすら思っていた。"

    "しかし彼が話すというのであれば、拒否する理由はない。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「孤独死、というのは分かるじゃろう？」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「はい。たまに、ニュースでは見ますから」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしも、その一例じゃよ」"

    "高齢者の独り暮らしは社会問題になるほど多い。そして身寄りもなく近所づきあいもなければ、孤独死のリスクは高まる。"

    "餓死したのではと噂になるくらいなのだから、彼が孤独死によって選定の参加者になっただろうことは想定していた。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしは腰痛があってのう。ふとした拍子で痛みがきて、動けなくなることも多い」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃからなるべく、缶詰や即席料理なんかを買い溜めておったんじゃ。まともな料理をしておると、急に動けなくなってガスも止められず火事、なんてことになりかねんしのう」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「それは言い訳かもしれんが……それはいい」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「雨の日じゃったかのう。これまでで一番ひどい腰痛がきた。わしは動けなくなってしまった。這って動くことすらできんほどじゃ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あとは分かるじゃろう？　水も飯もなければ人は生きていけん。数日のうちに、わしは餓死した」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「一日経ったあたりから記憶が曖昧でのう、正確な日時は思い出せん」"

    show sig sta nor app rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「自宅で餓死なんて、情けないとは思うがのう。家族に捨てられたわしの末路としては、相応しいかもしれん」"

    $ add_character_cards("rnk", ["5_death"])

    show rnk uni nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「そんなことは……」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「よいよい。おぬしも感じているとは思うが、わしはひねくれもんじゃ」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子に会って、少し変わったくらいじゃ。いや、少し戻ったという方がいいかのう。家族と仲が良かった頃のわしにのう」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「確かにあったんじゃよ……そんな頃も。せめてもう一度会いたかったの」"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ。いかんのう。年寄りになると辛気臭くなるうえに、話が長くなる」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしのことを脱落させにくくしているわけじゃないんじゃよ。これは本音じゃ」"

    "牛塚さんは切実に、後悔の言葉を、口にした。"

    "彼の想いなんて聞かなくても、簡単に分かってしまう。"

    "聞こうが聞くまいが……私は彼を躊躇せずに指名することなんてもう、できない。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「では、私はもう行きますね」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「夜も遅いから、気を付けるんじゃよ」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「ありがとうございます」"

    hide rnk
    hide sig
    with std_out

    "彼から聞いた≪死因≫の話に対して、私は特に何も言うことはなかった。"

    "それでも私の表情だけで十分会話になっていたに違いない。"

    play se "doorknock01"

    "玄関の扉の前まで移動したとき、ごんごんと太い音が響いた。"

    "扉が外からノックされた音だ。"

    show sig sta inn smi rev at std_c with std_in

    voice get_voice_filename("sgt")
    ushizuka "「ちょっと待っておれ。こんな時間に……借金取りじゃないといいがのう」"

    hide sig with std_out

    "牛塚さんが覗き穴を通して外を見た直後、彼は尻餅をついていた。"

    "突然の出来事に驚いていると、ノックはごんごんごんごんとさらに大きな音に変わった。"

    play music audio.kinpaku

    show sig sta nor squ at std_c with std_in

    voice get_voice_filename("sgt")
    ushizuka "「おぬしは……！」"



    "牛塚さんは扉に鍵がかかっていないことを思い出し、すぐに立ち上がり扉に手をかけた。"

    "急に動くとぎっくり腰にならないか心配だが、昨日言っていた通り選定期間中は症状はかなり和らいでいるのだろう、ソーニャの病気と同様だ。"

    "来訪者の見当はついていた。選定の参加者。この家を昨日襲ったという、あの――。"

    "近づこうとする私を、牛塚さんは手をかざして制した。"

    "来訪者がこの家に鍵がかかっていないことに気が付いたのは、恐らく牛塚さんが動き出したのより少し前。"

    "すでに扉は、開いていた。"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「なんじゃ、藪から棒に！」"

    show aln sta nor irr rev at std_l with std_in

    voice get_voice_filename("aln")
    alan "「……黙れ」"

    "突然の来訪者は、夢の世界でⅫに位置している男性――アラン・スコーピオンだった。"

    "牛塚さんの胸ぐらをつかみ呼吸を制限してから、あくまで静かに扉を閉めた。"

    "大柄な彼が胸ぐらをつかんでいたことで、小柄な牛塚さんは文字通り地に足がついていなかった。"

    "Ⅳの子がいてくれれば、と思った。"

    "しかし彼を呼ぶ隙はないし、これだけ物音を立てても起きてこないということは、相当眠りが深いのだろう。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「何故、君が……」"

    show rnk uni arm vig at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「Ⅺの人じゃ……ない」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「…………まあいい」"

    "男性は一瞬だけ私の方に視線を向けたが、すぐに牛塚さんへと向き直った。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「まずは貴様からだ」"

    show sig sta nor pai with std_change

    voice get_voice_filename("sgt")
    ushizuka "「がっ……ぐっ……」"

    show rnk uni ang an2 with std_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと待ってください！　いきなりやって来て、そんな……。彼を離してください」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「……君はまた、他人に肩入れしているのだな」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたには関係ない！」"

    "彼の冷徹な瞳を見て、内心では怖かった。"

    "相変わらず太い腕だし、部屋に入るなり無感情に牛塚さんの胸ぐらを掴みあげた容赦のなさは不気味なほどだ。"

    "だが、だからといって牛塚さんを見捨てて逃げるわけにもいかない。"

    "そう思う感情に、理由はつけられないけれど。"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「それに私が人を呼んだら、不利なのはあなたの方だ」"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「……僕ならそれより早く君の動きを止められる」"

    show sig sta nor pai with std_change

    voice get_voice_filename("sgt")
    ushizuka "「待……て……。話を……」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「声を出すのは、僕が質問をした時だけにするんだ」"

    show sig sta nor pai with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わし……は、貴様の未練を……知って……おる……」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「……何？」"

    show sig sta nor pai with std_change

    voice get_voice_filename("sgt")
    ushizuka "「だから……話を……」"

    "スコーピオンさんは逡巡した末、牛塚さんから手を離した。"

    "牛塚さんは尻餅をついて、床に落下する形になった。いててと腰をさすっていたが、動けないほどではないようだ。"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬし、焦っておるな？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「……余計なことはいらない。貴様の情報だけ話せ」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ⅢとⅪの参加者が、うちに来たのを見ておったのだろう？」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「だから何だ？」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「安心せい。うちには優秀なぼでーがーどがおっての。あやつらにわしの未練は知られてはおらん」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「≪氏名≫と≪死因≫は知られたかもしれんがのう」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「なら無用な説明はいらないな。僕はお前の≪氏名≫しか知らない。それ以外の情報を、教えろ」"

    "彼は一歩、牛塚さんへと近付いた。"

    "子供一人分くらいは身長差があるようにも見える。"

    "あの距離で見下ろされたならば、どれほどの威圧感があるのだろう。"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「待ってください。私はすでに――牛塚さんの情報を知っています」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「…………」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「その意味が分かりますか？　あなたはすでに同時指名のリスクを負っている」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「僕の≪氏名≫を、君も知っているだろう？　そしてⅢやⅪの連中も知っているだろう」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「氏名を軽んじるのは不本意だが――今となっては指名の優先権を得るために≪僕自身のカード≫を晒すことは躊躇わない」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「私だって、あなたに知られています。だったら――もう、躊躇う必要はないです」"


    stop music fadeout 1

    show aln sta nor lee rev with std_change

    voice get_voice_filename("aln")
    alan "「君のその瞳が、僕をざわつかせるんだ」"

    show rnk uni arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「……は？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「僕も≪自身のカード≫を２枚晒すリスクは負えないな。だが君に≪未練≫を知られるのも、今となっては危険かもしれない」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「なるほど。この状況は力では解決できそうにない」"


    play music audio.investigation
    "私は心の中で、自分が彼を言いくるめられたことに驚いていた。"

    "いや、桂子さんの時に見せた彼の強引さのせいで、警察に目をつけられているのかもしれない。"

    "だとすれば、彼が以前に比べて多少なりとも慎重なのも納得できる。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「欲を出してはいけないな。僕の目的は君が言った通り、ⅢとⅪの情報だ。昨日の朝以降、動きを見せていない。何があった？」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「やっぱり、あの人たちの動向が知りたかったんですね」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「言ったろう。わしの家にはぼでーがーどがおるとな」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「フン。だが、この家に貴様の≪未練≫への手がかりがあることはこれではっきりしたな」"

    "牛塚さんの発言のどの部分から、そのことに気が付いたのだろうか。"

    "自分の発言一つ一つにも気を配らなくてはならない。"

    "一度彼を納得させられたからといって、まだ油断は許されないのだ。"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「貴様が言う、ボディーガードとは誰のことだ？　この家には子供が居候していたが、まさかな」"

    show aln sta nor que rev with std_change

    voice get_voice_filename("aln")
    alan "「プロを雇う金もないだろう。まだ姿を見せないⅨの男も結託しているのか？」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……どうじゃかな」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「その線はなさそうだな。貴様は一瞬、僕を見上げるよりも上を見た。Ⅸの男の顔を思い出していたというところだろう。つまり、まだ現実世界で接触はしていなさそうだ」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おぬし、何者じゃ」"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「余計なことはいい」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「侮れないな。あんな少女が連中を撃退するとは……」"

    "彼と目を合わせたら隠し事もできないのか、と不安を覚えていた。"

    "だが同時に、今の発言は彼が万能でないことを指名している。当然ではあるけれど、私と同じ勘違いをしたということが私をちょっとだけ安心させた。"

    show sig sta inn smi with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ。あの子はのう、Ⅲの男にはしばらくは行動できないくらいの怪我を負わせたと言っておった」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「連中は協力しているみたいじゃから、Ⅺの女も数日は動けないじゃろうよ」"

    stop music fadeout 1



    voice get_voice_filename("ode")
    odette_unk1 "「悪いな。あんたの予想を裏切っちまってよぉ……」"



    show rnk uni arm imp with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……」"

    hide sig
    hide aln
    hide rnk
    with std_out

    play music audio.odette

    play se "dageki"
    with quake_fast

    "自分の体が玄関の壁に激突したのは、その直後だった。"

    "玄関にかかっていた牛塚さんのコートがクッションになって衝撃を吸収してくれたおかげで、痛みはほとんど感じなかった。"

    "その女性――Ⅺの女性は玄関からこの家に入るのと同時に、私を軽く振り払ったのだ。"

    scene ecg odettobt fun with dissolve_long



    voice get_voice_filename("ode")
    odette_num "「ほらよっ！」"

    play se "kick-middle"
    with quake_fast


    voice get_voice_filename("aln")
    alan "「貴様、いつからっ……！」"



    voice get_voice_filename("ode")
    odette_num "「たった今だ！」"

    "彼女の狙いは、スコーピオンさんに絞られていた。"

    "肉体的にもっとも優れているのは間違いなく彼だ。"

    "狭い廊下だからだろう。彼女はスコーピオンさんに向かって直接的な蹴りで攻撃していた。"

    "人を呼べばいいのかもしれない。"

    "けれど、足がすくんで動けなかった。"

    "アランさんとは違う。"

    show ecg odettobt mad with ecg_change

    "笑いながら他人に暴力を振るう彼女に――夢の世界で感じたよりもずっと恐怖を覚えていたのだ。"

    "一歩でも動いて、ちょっとでも声を出して、彼女の狙いが自分に向くのを恐れていた。"

    "交渉をしてみよう――そんな気持ちが湧くことさえなかった。"



    play se "swing"


    play music audio.battle

    scene ecg alanbt tre with dissolve


    voice get_voice_filename("aln")
    alan "「フン」"



    voice get_voice_filename("ode")
    odette_num "「ほう。その体は伊達じゃねぇか」"

    "しかし、スコーピオンさんも言葉では説明し難い身のこなしだった。"

    "Ⅺの女性の攻撃を受けたり避けたりしながら、隙あらば反撃を試みている。"

    play se "kick-middle"

    scene ecg odettobt mad with wipe_rl

    pause 1

    play se "tackle"

    show ecg alanbt gla with wipe_lr

    "彼女の攻撃は一撃一撃が重く、スコーピオンさんがガードする度にばちぃんと大きな音がした。"

    "お互いに、いわゆるクリーンヒットはなかった。"

    "細長い廊下では左右に動けないという理由もあるだろうが、一歩も譲らない攻防は言葉通り、彼らをその場からほとんど動かしてはいなかった。"


    scene bg shigetsugu02 night
    show ode sta nor nor at std_cr
    with dissolve_long


    voice get_voice_filename("ode")
    odette_num "「あたしは、このジジイの≪未練≫を探しに来たんだ」"

    show aln sta nor nor rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「…………僕もだ」"

    show ode sta gra smi with std_change


    voice get_voice_filename("ode")
    odette_num "「なら、協力するのも悪くないんじゃねーか？」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「断る」"

    show ode sta nor nor with std_change


    voice get_voice_filename("ode")
    odette_num "「ほう……。このジジイ、てめーの情報をどれか持ってるな」"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「何っ？」"

    play se "tackle"
    with quake_fast

    "一瞬の動揺が命取りになるのは、私も想像がつく。"

    "スコーピオンさんは、彼女に隙を見せたのだろう。お腹に蹴りを食らって、一歩下がっていた。"

    "おかしな話だが、私はスコーピオンさんの方を応援していた。"

    "自分が傷付かないために、彼に頼っていた。"

    "どちらも味方ではないけれど、会話ができた分スコーピオンさんの方がまだ、安全だと思ったのだ。"

    "そして悔しいけれど、私はⅣの少年が助けに来てくれることを祈るほかなかった。"

    "――私は、あまりにも無力だった。"

    "アランさんはさらに一歩下がって距離をとったが、それは廊下の端まで追いつめられるのと同義だった。"

    scene ecg odettobt ser with dissolve_long



    voice get_voice_filename("ode")
    odette_num "「そうでもなきゃ、てめーは会話に応じる奴じゃねぇ……気がするんだ」"



    voice get_voice_filename("ode")
    odette_num "「会話の内容はそうだな、そっちのガキがジジイを脱落させる情報を揃えそう――あるいはすでに揃っているってのはどうだ？」"



    voice get_voice_filename("ode")
    odette_num "「Ⅰ番がジジイを指名する可能性がある以上、てめーがジジイの情報を知ったところで、二重指名のリスクが残る」"



    voice get_voice_filename("ode")
    odette_num "「それでどうしようか考えていた……ま、そんなところだな」"

    scene ecg alanbt tre with dissolve


    voice get_voice_filename("aln")
    alan "「…………フン。貴様は話しながら考えをまとめるタイプなのだな」"

    show ecg alanbt gla with ecg_change


    voice get_voice_filename("aln")
    alan "「そのおかげで、貴様の仲間があの少女に為す術なく撃退されて以降、貴様は何の情報も得られていないことが分かった」"


    voice get_voice_filename("aln")
    alan "「……どうやら、過大評価していたようだよ」"

    play se "punch01"
    with quake_fast

    "会話の一瞬の隙をつき、スコーピオンさんは女性に反撃をくわえた。"


    scene bg shigetsugu02 night with dissolve_long

    "肩にパンチをくらった女性は数歩後ずさりし、再び元の位置へ戻った。"

    show ode sta nor lau at std_cr with std_in


    voice get_voice_filename("ode")
    odette_num "「なあ。あたしとてめーでこの家を仲良く探すって選択肢はないのか？」"

    show aln sta nor irr rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「ない。貴様と同時指名になり、優先権の争いになるリスクは変わらない」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「この家の住人たちを守るようで不本意ではあるが……貴様を追い返さないといけないようだ」"

    show ode sta gra smi with std_change_wait

    "スコーピオンさんの言葉を聞き、Ⅺの女性が牙のような歯をむき出しにして笑ったのを見てから、私は牛塚さんの姿がないことに気がついた。"

    "一体どこへという疑問は、階段から聞こえて来た足音が解消してくれた。"


    play music audio.impatience

    hide ode
    hide aln
    show sig sta nor pan rev at std_c
    with std_swap

    voice get_voice_filename("sgt")
    ushizuka "「ま、待ていっ。隠れておればいい」"

    show yuu sta war war at std_r with std_in


    voice get_voice_filename("yuu")
    yuu_unk5 "「嫌だよ。おじいちゃんが危ないんでしょ？」"

    "階段を駆け下りて来たのは、Ⅳの少年だ。"

    "起き抜けだろうけれど、眠そうな表情はしていない。"

    show yuu sta war sur with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「……人が、ふ、増えてる」"

    show aln sta nor nor rev at std_l with std_in

    voice get_voice_filename("aln")
    alan "「貴様……強いのだったな。手伝ってくれ」"

    show yuu sta war war with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「あっちが敵で、こっちは敵じゃない。いいの、おじいちゃん？」"

    show sig sta nor nor rev with std_change_wait

    "遅れて階段の上から顔を見せた牛塚さんは、少年に向かってこくりと頷いた。"

    scene ecg odettobt mad with dissolve_long



    voice get_voice_filename("ode")
    odette_num "「二対一か。楽しめそうだ」"

    "だが、Ⅺの女性は全く怯むどころか、発言の通り、より楽しそうに口の端を吊り上げた。"



    stop music
    scene bg shigetsugu02 night with dissolve_long

    "その時、近くからパトカーのサイレンが鳴り響く。"

    "徐々に音が大きくなっていく。近づいて来ているのだ。"


    play music audio.odette

    show ode sta arm irr at std_cr with std_in


    voice get_voice_filename("ode")
    odette_num "「ちっ……。残念だが潮時か……。また戦おうぜ、≪アラン・スコーピオン≫社長サマ！」"

    hide ode with std_out

    show aln sta nor nor rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「やはり……知られていたか」"

    "女性はスコーピオンさんの返事も聞かず、躊躇うことなく家を飛び出していった。"

    "パトカーのサイレンが移動し続けているのから察するに、Ⅺの女性は警察に見つからなかったようだ。"

    "何事も判断が早い女性だと感心するとともに、危険が一つ去っていったことに安心していた。"




    play music audio.gimon

    hide aln
    show sig sta nor pan rev at std_l
    with std_swap

    voice get_voice_filename("sgt")
    ushizuka "「近所の誰かが通報したのかのう」"

    show rnk uni arm ten at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「いえ……私が友達に頼んで通報してもらいました」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「なんじゃと？」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「言い訳は、お願いします」"

    "動かなくても、声を出さなくても、できること。"

    "彼女は私から注意を外しはしていなかったけれど、視覚はスコーピオンさんに向いていた。"

    "だから海晴にチャットで連絡して、この住所に警察を呼んでもらったのだ。"

    "海晴がスマホを見ているかどうかの賭けだったけれど、勝つことができた。"

    show yuu sta nor pun at std_r with std_in


    voice get_voice_filename("yuu")
    yuu_unk5 "「警察？　おじいちゃん何も悪い事してないよ！」"

    show rnk uni nor nor rev with std_change

    voice get_voice_filename("rnk")
    rinka "「大丈夫。そうじゃなくても来るときがあるの。ややこしくなるから、ちょっと隠れていよう」"

    hide yuu
    hide rnk
    hide sig
    show aln sta nor clo rev at std_c
    with std_swap

    voice get_voice_filename("aln")
    alan "「仕方ない」"

    "パトカーのサイレンがこの家の前で止まったのとほとんど同じタイミングで、私たち３人は居間へと移動した。"






    python:
        set_info_scene("65")
        set_info_location("27")

    stop music fadeout 1
    scene bg shigetsugu03 with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "私たちは無言で、牛塚さんの部屋にいた。"

    "私、Ⅳの少年、スコーピオンさんの３人という本来であれば一触即発の布陣だ。"

    "スコーピオンさんが大人しく隠れることに従ったことからして、警察を警戒しているという予想は当たっているようだ。"

    "さっきの殴り合いが人間離れしているということは、分かる。男子だからだとか体が大きいからだとか、そういう次元のものではなかった。"

    "拳銃を持っている警察官と戦っても勝てる気がするのが彼のすごいところだが、さすがに組織を相手取りたくはないのだろう。"

    show sig sta inn lau at std_cl, xoffset(180) with std_in

    voice get_voice_filename("sgt")
    ushizuka "「ふいー、どうにかなったわい」"



    "いい加減無言なのも辛くなってきたあたりで、牛塚さんが戻って来た。"

    show aln sta nor clo at std_l, xoffset(-80) with std_in

    voice get_voice_filename("aln")
    alan "「なら、もういいな」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「おや。これからこの子にカレーを温めてあげようと思ったところじゃが……、いらんかね？」"

    show yuu sta lau lau at std_cr, xoffset(-50) with std_in


    voice get_voice_filename("yuu")
    yuu_unk5 "「わーい！　起きたらお腹が空いてたから、食べたかったんだぁ」"

    show rnk uni nor que at std_r, xoffset(50) with std_in

    voice get_voice_filename("rnk")
    rinka "「ち、ちょっと！？」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あんなことをされはしたが、わしらを助けてくれたんじゃ。ま、作ったのはおぬしじゃが、構わんじゃろ」"

    show yuu sta eml war with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「あんなこと？」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「よいよい。ほれ、待っておれ」"

    hide sig with std_out

    "スコーピオンさんの返事を待たずに、牛塚さんは冷蔵庫からタッパーを取り出し、鍋に移して温めはじめた。"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「クミン、カルダモン、ターメリック……悪くはない、か」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「…………いただこう」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「ええっ！？」"

    "スコーピオンさんは無表情で座り込んだ。"

    "一刻も早く立ち去りたいが、こうなると牛塚さんたちが心配で、帰るに帰れない。"

    show yuu sta lau que with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ってことは、Ⅻのお兄さんは敵じゃ……ない？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「今はな」"

    show yuu sta nor que with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「あれ？　でもお兄さんも選定の参加者なんだよね？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「…………ああ」"

    show yuu sta nor que with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「でも、どうしておじいちゃんを守ったの？」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「守ったわけではない。偶然、利害関係が一致しただけだ」"

    show yuu sta nor nor with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「りがい？」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「…………ああ」"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「そっかー、よく分かんないけど、敵じゃないならまあ、いっか。それより、お姉ちゃんのカレー、とっても美味しいんだよ！」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「…………そうか」"

    show yuu sta nor kir with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「でねっ、でねっ」"

    "二人の会話を、私はびくびくしながら聞いていた。"

    "無表情ではあるが、馴れ馴れしいともとれる少年の態度にスコーピオンさんがいつ怒り出さないか不安だったのだ。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「貴様は、どうしてあの老人と一緒にいる？」"

    show yuu sta nor que with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「きさま？」"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「…………君のことだ」"

    show yuu sta nor nor with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「おじいちゃんがね、ボクを拾ってくれたんだよ。ボク、記憶ソウシツってやつみたいだったから」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「そうか。Ⅲの男を退かせたのも、体に技術が身についていたというわけか……」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「それ、話しちゃっていいんだ……」"

    "自分の秘密をあっさりと話す少年に、半ば呆れていた。"

    "敵じゃないと言われたからといって、そう簡単に心を開いていいものなのだろうか。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「あの、スコ……あなたは……」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「アレンでいい」"

    "苗字を言いかけたスコーピオンさんは、さらりと偽名を名乗った。私が彼の氏名を知っていることは予想がついているのだろう。"

    "私も偽名を名乗ろうか考えたが、求められたらでいいだろう。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「アレンさんは、この後どうするつもりなんですか？」"

    show sig sta nor squ at std_cl, xoffset(180) with std_change

    voice get_voice_filename("sgt")
    ushizuka "「物騒な話は、食事を終えてからでもよかろう」"


    play music audio.comicaldays
    hide sig with std_out

    "私たちの話を遮って、牛塚さんはカレーを運んで来た。"

    "私と牛塚さんは食べないので、２皿だ。"

    "アランさんは牛塚さんの提案に、こくりと頷いていた。"

    "彼はインドの宝石商だというから、カレーの本場出身。"

    "そんな人に自分の作ったカレーを食べられることに、場違いの緊張を覚えていた。"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「美味しい！」"

    show aln sta nor irr with std_change

    voice get_voice_filename("aln")
    alan "「…………これは」"

    "アランさんが一口飲み込んだのを見て、私はつい萎縮してしまっていた。"

    "ばくばくとカレーを口に運ぶ少年と対照的ではあるが、アランさんも二口三口と淡々と食事を続けていた。"

    "――なんなのだ、この緊張は。"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「こんなところまで、似ているとはな」"

    "彼が何か言ったのを聞いて、私は視線を合わせていた。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「家族がかつて、戯れに日本のカレールゥを買ってきたことがあるだけだ」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「奥さん……とかですか？」"

    "聞き返すと、アランさんは私をきっと睨んだ。"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「僕のことを探っているのか？」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「否定はしませんけど、深い意味はありませんでした」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「そうか。もっともこれは一般に知られている情報だが、僕は未婚だ。家族というのは配偶者の意味ではない」"

    show yuu sta lau lau with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ごちそうさま！」"

    "ざわりと走った緊張感を、少年が打ち破ってくれた。空気の読めなさに助けられてしまった。"

    "家族という言葉が彼から出てきたのは意外だった。"

    "人間だから別に家族の話をしてもおかしくはないが、アランさんには無縁な言葉だと思い込んでいたのだ。"

    "美味しいともまずいとも言わないのは、少なくとも悪くはなかったということだろうか。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「……スプーンを使うのがそんなに珍しいか？」"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ！　いやそんなことも思ってもなかったですけど……」"

    "言われてみれば、インドの人は手でカレーを食べるというイメージはあったかもしれない。"

    "もっとも、それはナンで食べる時で、日本のカレーライスを食べているのだから言われなければ疑問にも思わなかった。"

    "神妙な顔でそう言った彼を見て、私はつい堪えられず、吹き出してしまう。"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「僕の国は、日本では偏見を強く持たれているらしいな」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「……っ、いや、そうじゃなくって……」"


    "声の雰囲気からして、どうやら少し怒っているらしい。"

    "感情の全く読めない人だと思うと、緊張のせいもあったのだろう、余計に笑いを堪えるのが難しくなってしまった。"

    "アランさんはまあいいと短く言って、少年に食器を流しまで運ばせた。"





    stop music fadeout 1
    scene bg shigetsugu03
    show sig sta nor nor rev at std_cl, xoffset(180)
    show rnk uni nor nor at std_cr, xoffset(-70)
    with fade_long
    play music audio.nichijo03
    pause 1

    "少し経って、牛塚さんは４人分のお茶を淹れて来た。"

    show aln sta nor irr behind sig at std_l, xoffset(-80) with std_in

    "アランさんは匂いを嗅いだあと、牛塚さんの湯飲みと入れ替えてから、一口すすり、渋い顔をした。"

    "日本茶が苦かったのかこのお茶が薄かったのかは分からないが、よく見るとちゃんと表情の変化がある人なのだと、思った。"

    show yuu sta nor nor behind rnk at std_r, xoffset(50) with std_in

    "少年は退屈そうにちゃぶ台の上で頭を転がしていたが、そんな沈黙を破ったのはやはりアランさんだった。"


    play music audio.investigation

    show aln sta nor gen with std_change

    voice get_voice_filename("aln")
    alan "「さて、シゲツグ。僕には少し発音がし辛い名前だが――それはいい」"

    show aln sta nor nor with std_change

    voice get_voice_filename("aln")
    alan "「僕の目的はすでに分かっているな？」"

    show sig sta nor gla with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしらの情報……かぁどじゃろう？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「ああ。最終的にはここにいる全員を脱落させるが――そう欲張りはしない」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「意外じゃの。わしらを脅迫してでも、情報を集めると思ったがのう」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「その少年は記憶喪失と言っていた。であれば、脅したところでカードは出てこないだろう」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「そして君も同じだ。未だ手掛かりがない。これは僕の勘ではあるが、まさか君も、自分のカードを忘れているのではと思っている」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「不確定にもかかわらず強引な手段に出れば、長期的に見て不利になる」"

    "桂子さんの時にあれほど大胆な行動に出た人が何を言う、と思う。"

    "この少年を少女だと間違えたことが、アランさんが万能ではないことを証明した。"

    "茂継さんがアランさんに言った『焦っている』という言葉は、選定初期の桂子さんの時にもっとも当てはまったのかもしれない。"

    "しかし――自分のカードを覚えていないことが、有利に働くこともあるのは意外だった。"

    "アランさんの言葉に、初めに返事をしたのはⅣの少年だった。"

    show yuu sta nor sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「勝手なこと言わないでよ！　それは……おじいちゃんが脱落するってことじゃないか」"

    show yuu sta war war with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「そんなことさせないよ。この人は今から敵――」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「…………フン」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「落ち着くんじゃ。わしが嫌じゃと言ったらどうするつもりじゃ？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「予想はついているだろう？　ここまで来た以上、ただ引き返すことはできない」"

    show yuu sta war war with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「やっぱり、僕がこの人を……！」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしはおぬしらが傷付くのを見たくはない。それに、アレンと言ったか。おぬしはまずそこの娘を狙うじゃろう？」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「…………でしょうね」"

    "いつでも逃げられるように準備はしているけれど、それでもアランさんが本気を出せば恐らく、廊下に出る前に捕まってしまう。"

    "もっとも私は牛塚さんの情報を持っているから交渉の余地はあるかもしれないが、とにかく、この状況の推移を見守ることにした。"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしの情報を教えよう。ただし、条件がある」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「聞かせろ」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしが脱落するまでの間、この家を守って欲しいということじゃ。Ⅺの女性はわしの家を狙うじゃろうからの」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしやこの子が傷付かんよう、守って欲しいんじゃ」"

    show aln sta nor que rev with std_change

    voice get_voice_filename("aln")
    alan "「……僕があの女から貴様らを守ったとして、もう一つ懸念があるのは分かるな？」"

    "アランさんはそう言うと、私と視線を合わせた。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……分かりました。アレンさんが牛塚さんの条件を飲むなら、私は牛塚さんの指名を行いません」"


    play music audio.impatience

    show yuu sta war cla with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ちょっと待ってよ！　いらないよ！　あの人が来ても、僕が……僕がおじいちゃんを守るよ！」"

    "再び、少年は興奮してそう言った。"

    "だが、答えたのは牛塚さんではなくアランさんであった。"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「まだ分からないのか？」"

    show yuu sta war sur with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「何がっ！」"

    show aln sta nor ang rev with std_change

    voice get_voice_filename("aln")
    alan "「シゲツグは君を傷付けたくないと言っているんだ」"

    show yuu sta war sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ボクを……？」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたにも分かるんですね。家族が……いるからですか？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「その質問には、答えない」"

    show yuu sta nor que with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「そうなの……おじいちゃん？」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「当然じゃ」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「お前は強いかもしれん。じゃが、わしはお前が怪我をするところは見たくない」"

    show yuu sta eml war with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「でも……ボクが勝てれば……！」"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「思いあがらない方がいい。僕が君と本気で戦うとなれば、手加減はしない」"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「無傷で済むとは、わしには思えん！」"

    "家族としての想い。"

    "牛塚さんの語った想いはまさに、桂子さんがアランさんに息子を人質に取られたときに言ったのと同じものであった。"

    "アランさんが意図してそういう状況に持ち込んでいるのか、あるいはただの偶然なのか、相変わらずの無表情に戻ってしまった今では分からなかった。"

    show yuu sta nor sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「おじい……ちゃん……」"

    show yuu sta nor sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「ボクがおじいちゃんの敵をやっつけるから、喜んでくれると思ったのに」"

    show yuu sta war cla with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「おじいちゃんがこの人たちのカードを集めれば、守れるんじゃないの！」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「同じことじゃ。彼らから情報を引き出すのは……容易ではない」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「悪いが、家族ごっこは後でやってくれ。一つ目の条件は飲もう。ただし、選定の日までどこかの部屋を提供してもらう」"

    "彼の言葉に驚いた顔を見せると、彼は補足の説明をした。"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「僕としても、この国で自由に動けない。数日でも滞在先ができるのは悪い条件ではない」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「いいじゃろう。ただし、二つ目の条件も飲んでこそじゃぞ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「分かっている」"


    stop music fadeout 1

    show yuu sta nor sad with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「――いい」"

    "話を進めていく牛塚さんとアランさんを遮るように、少年は立ち上がった。"

    show yuu sta eml cla with std_change


    voice get_voice_filename("yuu")
    yuu_unk5 "「もういいよっ！」"

    show rnk uni cat ten rev with std_change

    voice get_voice_filename("rnk")
    rinka "「ち、ちょっと！」"

    hide yuu with std_out

    "少年はそのまま、部屋を出て行ってしまった。"

    "アランさんは全く動揺を見せていなかったが、さすがに牛塚さんは違う。"

    show sig sta nor app with std_change

    voice get_voice_filename("sgt")
    ushizuka "「すまんが、少し待っていてくれ」"

    hide sig with std_out

    "あの子なら夜に出歩いて絡まれたとして心配はないだろうが、補導されてトラブルを起こす可能性もある。"

    "だがアランさんがいる以上、この家を彼だけにするわけにもいかない。"

    "二人でいるのは恐いけれど、結果的に残ることになってしまった。"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「……やれやれだ」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたのこと、勘違いしていました。もっと、常識がない人だと」"

    show aln sta nor lee rev with std_change

    voice get_voice_filename("aln")
    alan "「……そうか」"

    "会話をして時間を稼ごうと思ったが、そもそも私にそんな技術はないし、彼は元々無口な方だから、無理な案だった。"


    scene bg shigetsugu03 with fade_long
    pause 1

    "10分ほど経過したが、その間ずっと、沈黙の時間が流れていた。"

    "アランさんは何も言わず何もせず、ただそこに座っていた。変化といえば、ただまばたきをするくらいだ。"

    "私も彼にならってじっとしていたが、そろそろ辛くなってきた。"

    show aln sta nor nor rev at std_cl with std_in

    voice get_voice_filename("aln")
    alan "「リンカ、君は……」"

    show rnk uni arm nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「は、はい」"

    "何の前触れもなく声をかけられて、つい声が裏返ってしまった。"


    play music audio.alan

    show aln sta nor lee rev with std_change

    voice get_voice_filename("aln")
    alan "「生きたいのか？　君の行動は、生きたい人間の行動には見えない」"

    "彼の言い分はもっともだ。"

    "私は選定に参加しながら、学校には引き続き通っている。"

    "もっとも彼はそのことを知らないだろうから、こうして他の参加者と関わっていることを指しているのだろうけれど。"

    "私自身、どうして今の状況になっているのか迷うことも多い。"

    "けれども、自分の意志でこうなっていることに変わりはない。"

    "そして今日まで、生きるべきか悩んだことはあっても、脱落してもいいと思ったことは一度もなかった。"

    "だから、彼への答えは決まっていた。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「私は、生きたいです」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「あなたには非効率的に見えるかもしれないですけれど……これが、私の生き方なんです、きっと」"

    "平凡じゃない状況に陥っても、平凡にしか生きられない。"

    "流されやすくて、お節介で、余計なことに首を突っ込んでしまう。"

    "それが、私。獅子舞凛火。"

    show aln sta nor tre rev with std_change

    voice get_voice_filename("aln")
    alan "「……フン。愚問だったようだ」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「病院で君の瞳を見たとき、僕はとっくにそのことに気付いていた」"

    "アランさんの口元は、少し綻んだように見えた。"

    show aln sta nor gen rev with std_change

    voice get_voice_filename("aln")
    alan "「リンカの生き方がどこまで通用するのか、見させてもらおう」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「どちらにせよ、君自身が忘れているなら、問い詰めても君の情報は引き出せなさそうだ」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「ど、どこでそれを……？」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「君は選定のルールを忘れていたな。≪自身のカード≫を忘れていても不思議ではない。≪死因≫や≪未練≫を自覚していないからこそ、身を晒して行動できるのだろう」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「もっとも、それはあの少年も同じ……ではあるな。ああいった手合いは、他の参加者を脱落させてカードを得るほかないだろう」"

    "一度目の選定、私が初めて運命の大広間へ行ったときのことだ。"

    "私は海晴と話しながら、女神の説明を一から聞き直していた。"

    "彼はその時から、私が≪私自身のカード≫が何かを忘れてしまっていたことを予想していたのだろうか。"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「アランさんは……あの子の情報も得るために牛塚さんの条件を飲んだんですか？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「その意図はなかったな。だが、なるほど。ここにいれば何か手掛かりが得られるのだな」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「あの無防備な少年だ。何かの拍子に話してもおかしくはない――か。記憶喪失というが、例えば――夢というのは深層心理が呼び起こされる場合もあるから、寝言などか」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「……フン。さすがにそれは都合が良過ぎるか。しかし、なるほど、君の言う通りだな」"

    "これ以上この人と喋るのはやめておこう、と思った。"

    "ペースを握られたら、海晴のことも引き出されてしまうかもしれない。"

    "海晴の機転で私たちは仲間割れしたように見せているが、この調子ではいつボロを出してしまうか分からないし、何がボロになるのかも予想できない。"

    "とにかく、彼が牛塚さんの条件を承諾したのは意外だった。"

    "彼の言葉を信じるならば、利害関係だけで首を縦に振ったのか分かりかねるから。"

    "はっきり言えば、私は感情的な何かが彼を動かした以外に考えられなかった。"

    "もっとも、そんなこと口にするわけもない。"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「……ようやく戻るか」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「えーっと、え？」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「足音が聞こえた。玄関まで行ってやればいい。心配するな。僕はここでじっとしている。約束を反故にされても適わん」"

    "言われてみれば、確かに玄関の方から物音が聞こえる。"

    "私は出迎えるため、玄関へと向かった。"








    python:
        set_info_scene("66")
        set_info_time("night")
        set_info_location("24")

    stop music fadeout 1
    scene bg shigetsugu01 night with fade

    $ show_hud()

    "牛塚茂継は、逃げ出した少年のことを５分ほど探したところで、自分の家へ戻っていく少年の姿を見つけた。"


    play music audio.growapart

    show sig sta nor nor at std_cr with std_in

    voice get_voice_filename("sgt")
    ushizuka "「ここにおったか、ユウ」"

    show yuu sta nor sad rev at std_cl with std_in

    voice get_voice_filename("yuu")
    yuu "「どこかへ行こうとしたけど、ボクは記憶がないから、他に行く場所なんてなかった」"

    "Ⅳの少年は、茂継にユウと呼ばれていた。"

    "元々の名前ではない。"

    "それは、二人が出会ってから茂継が彼に与えた名前だった。"

    show yuu sta nor que rev with std_change

    voice get_voice_filename("yuu")
    yuu "「おじいちゃんは、ボクのこと嫌いになったの？」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「そんなわけなかろう」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「なら、どうしておじいちゃんが脱落――死んじゃうようなことを言うの？」"

    show yuu sta nor tro rev with std_change

    voice get_voice_filename("yuu")
    yuu "「おじいちゃんが死んだら、ボクは一人になっちゃう」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「本当の……家族じゃないから？」"

    show sig sta nor tro with std_change

    voice get_voice_filename("sgt")
    ushizuka "「本当の家族が、無条件に一緒にいるとも限らんよ」"


    scene ecg citysky with dissolve_long

    "茂継は寂しそうな声で、夜空に向かってそう言った。"

    "早くに妻を亡くした茂継は、ずっと寂しさに怯えていた。"

    "優秀な彼の息子は大学も卒業し、金融業界に就職し、すぐに結婚をした。"

    "孫が生まれるまでの数年間、息子の嫁とも良好な関係を築いていたが、幸せな家族は息子の嫁が妊娠した時に変わってしまった。"

    "いや、変わってしまったのは、茂継だけだったのかもしれない。"

    "孫が生まれることが決まり、息子たちは引っ越すことを決意した。社内でも順調に地位を上げていた茂継の息子にとっては、いいタイミング。"

    "茂継が抱えていた孤独への恐怖は、その時に最高潮になってしまったのだ。"

    "ストレスは、攻撃性へと変質した。"

    "家庭内で傍若無人な振舞いをするようになり、どうでもいいことに頑固になった。"

    "息子の嫁が作る食事にも、文句を言うようになった。"

    "おかげで、息子の家族は躊躇することなく家を出て行った。"

    "寂しさと自己嫌悪によって、茂継はもう普通の状態ではなかったのかもしれない。"

    "別居して数年こそ交流はあったが、それまで。"

    "色の無くなってしまった有り余る時間を紛らわせるために、茂継はギャンブルにはまった。"

    "借金は膨れ上がり、茂継の息子の家族に問題が波及しそうになった頃、縁は切れた。"

    "その数年後、息子一家と会っていなかった茂継が家を訪ねたとき、そこに彼らの姿はなかった。"

    "完全に、消息は不明になってしまった。"

    "もっとも息子夫婦からすれば、不明なのは茂継の行方だったのかもしれないけれど。"


    scene bg shigetsugu01 night
    show yuu sta nor nor rev at std_cl
    with dissolve_long

    voice get_voice_filename("yuu")
    yuu "「そうだったね。おじいちゃんが話してくれた」"

    show sig sta nor app at std_cr with std_in

    voice get_voice_filename("sgt")
    ushizuka "「悪いのは、わしじゃ。じゃが、おぬしはそれを知ってもわしと一緒にいてくれた」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「他に行く場所がないから――などという利害関係だけでないことは、よく分かっておる」"

    show yuu sta nor que rev with std_change

    voice get_voice_filename("yuu")
    yuu "「リガイ？　よく分からないけど、うん、ボクはおじいちゃんが好きだから一緒にいたんだ」"

    show yuu sta nor nor rev with std_change

    voice get_voice_filename("yuu")
    yuu "「お馬さんを見たり、ボートも見たりした」"

    show sig sta inn smi with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……こほん」"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「何より……独りぼっちのボクを助けてくれた。記憶がない不安よりも、この家にいられる安心の方が大きいよ」"

    "女神の選定が始まってから、一ヵ月以上が経過している。"

    "その時間のほとんどを、彼らは一緒に過ごしてきたのだ。"

    "歪な形かもしれない。"

    "だがそれは茂継にとっても、紛れもない家族の形。"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ユウ……わしはお前を家族だと思っておる」"

    show yuu sta nor nor rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクも、そうだよ！　おじいちゃんはボクの唯一の家族だ！」"

    "今は、とか、日本での、とか、そういった枕詞をユウはつけなかった。"

    "自分の本来の記憶なんて、どうでもよかったのだ。"

    "そのことが、ユウの言葉が本心からのものであることを強く証明していた。"

    show sig sta nor tro with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃが、わしは死ぬ」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「お前たち若い連中は、運命の悪戯のようなもので、本来の寿命よりも随分早くに命を落としてしまったんじゃろうが、わしは違う」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの日、腰を痛めなかったとしても、もう老い先は長くなかったんじゃ」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしの願いは、できるだけ長くお前と過ごすことじゃった……」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ささやかな願いじゃった。だからこそ、必死に生きようとする者たちに拒まれたんじゃ」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「分からないよ、難しくって……ボクにはおじいちゃんが言っていることが分からない！」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……ユウ。これからの生き方は、お前が決めるんじゃ」"

    show yuu sta nor que rev with std_change

    voice get_voice_filename("yuu")
    yuu "「……ボク、が？」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ああ。生きたいと思うんじゃったら、選定を勝ち残るんじゃ」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「思わない――そう思えないんじゃったら、わしは止めはせん」"

    show yuu sta nor tro rev with std_change

    voice get_voice_filename("yuu")
    yuu "「決められないよ。ボクは、そんなもの！」"

    show sig sta nor gla with std_change

    voice get_voice_filename("sgt")
    ushizuka "「決めねばならんのじゃ。わしは数日後にはもう、死んだことになっているんじゃからな」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「嫌だ……嫌だよ……。おじいちゃん……！」"

    "ユウの声は、徐々に切迫さを増していった。"

    "反比例するように、茂継はただ淡々と話す。"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「お前にユウという名前を与えたのは、わしの過ちじゃったかもしれん」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「記憶喪失じゃからか知らんが……まさか、その名前でかぁどが作られるとは思わんかった」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「お前は≪自身のかぁど≫を忘れていることが強みじゃったが、それを一つ奪ってしまったからのう」"

    show yuu sta nor tro rev with std_change

    voice get_voice_filename("yuu")
    yuu "「そんなことない！　おじいちゃんが名前をつけてくれて、ボクは嬉しかった。だって……自分の名前も分からなかったんだもん！」"

    show sig sta inn smi with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、それは嬉しいわい。ならば、わしの願いは一つじゃ」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「無理に生きろなどとは言わん。ただ、誰かに何かを与える喜びだけは知って欲しいんじゃ」"

    "彼がユウに名前を与えたように。"

    "彼がユウに居場所を与えたように。"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「わしも、ユウに大切なものをもらって死ねる」"

    show yuu sta nor que rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクがおじいちゃんに何かを……あげた？」"

    show sig sta nor nor with std_change

    voice get_voice_filename("sgt")
    ushizuka "「……そうじゃ」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「駄目だ！　やっぱりボクには分からないよ。何も……分からない」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃったら、徐々に分かるようになればいいんじゃ。その時には、その喜びもちゃんと理解できるじゃろう」"

    "朗らかな声で言うと、茂継はユウの頭をしわくちゃな手で撫でた。"

    "何も答えは出ていない。"

    "ユウ自身は、一つも納得していない。"

    "ともすれば、茂継の詭弁に丸め込まれたような状態だ。"

    "だけれども、ユウはようやく理解することができた。"

    "牛塚茂継――おじいちゃんは本当に、間もなく死んでしまうのだと。"

    "それだけは、何があっても止められないのだと。"








    python:
        set_info_scene("67")
        set_info_time("night")
        set_info_location("25")

    scene bg shigetsugu02 night with fade

    $ show_hud()

    "一連のやり取りを、私は聞いてしまっていた。"

    "盗み聞きする気がなかったという言い訳は使えない。"

    "彼らの会話の全てをしっかり聞いたわけではないが、どうしても、聞き逃せないことがあったのだ。"

    "――ユウ。"

    python:
        add_character_cards("rnk", ["4_name"])
        add_character_cards("yuu", ["4_name", "5_name"])
        add_character_cards("sig", ["4_name"])

    "牛塚さんがⅣの少年の名前を呼んだとき、私の本は光を放った。"

    "生成されたカードに書かれていたのは、苗字もないたった二文字だけ。"

    "アランさんが近くにいなくてよかったと安心していた。"

    "私が彼の情報を得たとすれば、もっと話がややこしくなっていたに違いない。"

    show rnk uni arm sad at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「ユウくん……」"

    "心の中で、私はそう呟いた。"

    "牛塚さんが何かしらの呼び名を決めていたとは思っていたが、それが彼のカードになっているのは予想外だった。"

    "海晴と≪名前の認知≫について話していなければ、信じられなかっただろう。"

    "牛塚さんは、その名前に一体どんな意味を込めたのだろうか。"

    "かくして、私は人知れずユウくんのカードを３枚集めたことになる。"

    "けれども、すでに私は、彼らを指名する勇気を持ち合わせてはいない。"

    "アランさんが牛塚さんを指名するのであれば、私もユウくんを指名するくらでないと駄目なのだと自分に言い聞かせ、私は奥歯を噛み締めた。"







    $ set_info_location("27")

    scene bg shigetsugu03 with fade_long
    pause 1

    "玄関で牛塚さんとユウくんを出迎えた私は、再び居間へと戻って来ていた。"

    "再び、四人での会話が始まるが、今度は簡潔に終わったのだった。"


    play music audio.nichijo03

    show sig sta nor nor at std_cl, xoffset(200) with std_in

    voice get_voice_filename("sgt")
    ushizuka "「すまんのう。待たせてしまった」"

    show aln sta nor nor rev at std_l, xoffset(-80) with std_in

    voice get_voice_filename("aln")
    alan "「……構わない。僕からは特に話すことはない。僕のために部屋を用意すれば、それでいい」"

    show sig sta nor squ with std_change

    voice get_voice_filename("sgt")
    ushizuka "「うむ、分かっておる」"

    show yuu sta nor tro at std_cr, xoffset(-50) with std_in

    voice get_voice_filename("yuu")
    yuu "「…………」"

    "それでも納得していないユウくんをよそに、話はそれでまとまった。"

    "結局流れで遅い時間までいてしまったが、私ももう帰ることにした。"

    show aln sta nor irr rev with std_change

    voice get_voice_filename("aln")
    alan "「君も、Ⅺの女に狙われるかもしれない」"

    show rnk uni nor nor at std_r with std_in

    voice get_voice_filename("rnk")
    rinka "「は、はい……」"

    show aln sta nor clo rev with std_change

    voice get_voice_filename("aln")
    alan "「もっとも、あの女は僕の方を狙って来るだろうな。ああいうタイプは、決着をつける方を優先する」"

    show aln sta nor nor rev with std_change

    voice get_voice_filename("aln")
    alan "「それはこっちの少年が狙われる可能性もあるということではあるが、僕がいる限り心配はしなくていい。約束は守る」"

    "はっきりしない返事は、彼の口から私を心配する言葉が出てきたのが意外だったからだ。"

    "この人のことが、分からなくなった。"

    "赤ん坊を平気で殺すと言ったと思えば、牛塚さんと利害関係だけでは納得できないような約束をし、私の心配までしてくれる。"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「……ばいばい、お姉ちゃん。ご飯、とっても美味しかった。忘れないよ」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、ありがとう。まだちょっと残ってるから、お腹が空いたら食べてね」"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ふむ。さて、わしが見送ろう」"

    "牛塚さんと一緒に、私は廊下へと向かった。"







    $ set_info_location("24")

    scene bg shigetsugu01 night with fade

    show rnk uni arm nor at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「そんな、玄関まででよかったのに」"

    "牛塚さんは、私と一緒に家の前まで出て来てくれた。"

    "珍しく二人きりになったので、私は彼に疑問をぶつけることにした。"


    play music audio.gimon

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「牛塚さんが脱落したら――、ユウくんはどこで暮らすつもりだったんですか？」"

    show sig sta nor nor rev at std_cl with std_in

    voice get_voice_filename("sgt")
    ushizuka "「盗み聞きとは趣味が良くないのう」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「わざとです。あなたが、つけた名前なんですよね？」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「そうじゃ。あの子は優しいけれど、勇気もある子じゃ」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「ユウ、という響きは日本人らしくもあり、外国人らしくもあるじゃろう？」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「優、勇、悠――ユウ。まさか本当の名前として≪かぁど≫が作られるとは思わなかったがのう」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「私の推測ではありますが……カードの情報は、本人の認知が大きく関わっているみたいです」"

    show sig sta nor squ rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「なるほどの。で、ユウのその後、じゃったのう」"

    "私が小さく頷くと、牛塚さんはそのままの調子で話を続けた。"

    show sig sta nor gla rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「現金で100万ほど、用意してある」"

    "私はついびっくりして、きょろきょろと周りを見てしまった。"

    "泥棒でもいたら、標的にされてしまうかもしれない。今のこの家の状況から考えると、盗みに入る人の方が心配だけど。"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「選定が終わるまでの約２ヵ月であれば、その金で何とかなるじゃろう」"

    show sig sta nor tro rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「あの子が選定の後どうするかは、わしが関われることではないじゃろう。じゃが贅沢をしなければ記憶が戻ったとき、帰国するくらいの金は残っているはずじゃ」"

    show rnk uni sur su1 with std_change

    voice get_voice_filename("rnk")
    rinka "「そんなに……お金を……」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「選定が始まってから、わしが家にある現金をかき集めて、売れるものは全て売り……まあ色々して集めた金じゃ」"

    "彼の収入源は現在、国からの年金と補助金が主なものだと言っていた。"

    "そういった制度について詳しくは知らないが、彼は一時期借金をしていたくらいだと言っていたし、100万円を集めるのはあまり大きな声では言えない手段をとった可能性もある。"

    "だが、それがユウくんのためだと思うと、批判する気は失せてしまう。"

    show sig sta inn smi rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「貯金なんぞ全部使い切ったし、口座も凍結しておったからのう、苦労したわい」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「後のことを構わず家探しをしたんじゃが片付ける気にもならんでの、家は散らかっていたじゃろう」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「どうりで……あ」"

    "言いかけて、私は口元を手で隠した。"

    "事実ではあるが、言ってしまっては失礼だろう。"

    show sig sta nor app rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「構わん構わん」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「というわけじゃ。おぬしが心配することなど何もありゃせんよ」"

    "快活にそう言うと、牛塚さんは笑った。"

    "私は一緒に笑うことはできず、ただこくりと頷いていた。"

    show sig sta inn lau rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「じゃあの。また夢の世界とやらで会ったらよろしく頼むぞ」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「……はい。色々と、お世話になりました」"

    show sig sta nor nor rev with std_change

    voice get_voice_filename("sgt")
    ushizuka "「世話になったのはこちらじゃよ」"

    "牛塚さんは、そう言い残して家の中へと戻って行った。"

    "そう、これでいい。"

    "状況は私にとって悪くないままだ。"

    "それでもどこか胸にはわだかまりを残したまま、私は帰路につくのであった。"









    $ set_info_location("05")



    stop music fadeout 1
    scene bg myroom night with fade_long
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "家族……か。"

    "自室に帰った私は一人、牛塚さんとユウくんのことを思い返していた。"

    "誰かに何かを、与えることのできる人。"

    "私は桂子さんに、何かを与えることができたのだろうか。"

    "私はソーニャに、何かを与えることができたのだろうか。"

    "次の選定で間違いなく、牛塚さんは脱落する。"

    "そんな彼に対して、私が何か与えることはできたのだろうか。"

    "彼のお願いを聞いて、ユウくんのために手料理を作った。"

    "選定の参加者にこれ以上深入りする必要などないというのに、私の心には月曜日の朝、後悔なく目覚めることができるのかという疑問がぶつかっていた。"

    show rnk paj arm ang up at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「あー、もうっ」"

    "もやもやするくらいなら動こうと思って、私は机に置いてあるパソコンに向かうことにした。"

    $ add_seen_chapter("5-4")







    python:
        set_info_scene("68")
        set_info_date(6, 1, "fri")
        set_info_time("morning")
        set_info_location("05")

    stop music fadeout 2
    scene bg myroom morning with fade_longest
    pause 1

    $ show_hud()

    "一晩開け、私は今日も学校だ。"

    "昨日は調べ物で夜更かしをしてしまったから、まだ少し眠い。"

    "気付けばもう、今日から６月。"

    "みんなで遊園地に行った日が懐かしい。"

    "カレンダーを見て少しだけ驚いてから、私は学校へ行く準備を始めた。"







    python:
        set_info_time("noon")
        set_info_location("08")



    stop music fadeout 1
    scene bg schoolroom noon with fade_long
    play music audio.nichijo02
    pause 1

    $ show_hud()

    "私たちは教室で話していた。"

    show mao uni sel lau rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「おはよ～。りーたんたちは、文化祭の日どうするか決めた？」"

    show rnk uni nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「どうするかって……土日でそれぞれ１時間の手伝い、でしょ？」"

    show mhr uni sco cau behind rnk at std_r with std_in

    voice get_voice_filename("mhr")
    miharu "「ぼくも、やらなくてはいけないみたいだ」"

    "こうして話していると、ちゃんと日常に戻ってきたような気がした。"

    "来週の土日に控えた文化祭で、私たちのクラスは占いの館をやることに決まっている。"

    "１ヵ月を切ってから決まった企画なのでぐだぐだにならないかが心配だが、まあ、大掛かりな準備はいらないしそれなりに形にはなるだろう。"

    "私たちは主要メンバーではないが、一応クラスでの参加になるため、手伝いをしなくてはならない。"

    "土日それぞれ１時間ずつのシフト制、らしかった。"

    show mao uni sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「ちーがーうーよー。うちは、それ以外の時間をどうしよっかって聞いてるの」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「ああ、そうだったんだ。だったら、直未の喫茶店には行ってみたいかな」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「日辻さんの……ね」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「別にみはるんは無理に行かなくてもいいんじゃないのぉ？」"

    show mhr uni sco smi with std_change

    voice get_voice_filename("mhr")
    miharu "「いや、凛火が行くならぼくも行くよ」"

    "学校の中くらい、直未と一緒にいても大丈夫だろう。"

    "直未はその日のために着々と準備を進めて頑張っているのだし、私もちゃんと見届けたい。"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「真央は、何か案があるの？」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「ない！」"

    show rnk uni nor apo with std_change

    voice get_voice_filename("rnk")
    rinka "「……ないんだね」"

    show mhr uni nor rea with std_change

    voice get_voice_filename("mhr")
    miharu "「ぼくは文化部の活動にもあまり興味がないから、シフトを午前中に入れてもらう予定だよ」"

    show mhr uni nor nor with std_change

    voice get_voice_filename("mhr")
    miharu "「生徒は午前中まで校内にいれば、あとは帰宅してもいいことになっているからね」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「なら、私もそうしようかな。他に興味あるものもないし」"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「冷っめてる～」"

    "私たちをからかう真央をよそに、私たちは食堂へ向かうのであった。"







    $ set_info_time("evening")



    scene bg schoolroom noon with fade_long
    pause 1

    $ show_hud()

    show mao uni nor lau at std_c with std_in

    voice get_voice_filename("mao")
    mao "「んじゃ、お先～」"

    hide mao with std_out

    "そう言うと、真央は教室を出て行った。"

    "どうやら今日は早く帰宅する日らしい。"

    "真央はあまり教えてはくれないが、用事が入っていることも多い。"

    "部活はやっていないが、バイトでもしているのだろうか。"

    "海晴も丁度帰ろうとしているところだった。"





    menu:
        "海晴も今日はバイトが入っているらしいが……。"
        "「一人で帰る」":


            $ flags_mhr_koukando = 0

            $ persistent.s11_1_seen = True
            $ grant_hear_all()
            jump f005_2.s2_1
        "「一緒に帰る」":

            $ flags_mhr_koukando += 1

            $ persistent.s11_2_seen = True
            $ grant_hear_all()
            jump f005_2.s2_2

label f005_2.s2_1:


    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk", 802)
    rinka "「また明日っ」"

    show mhr uni sco con rev at std_cl with std_in

    voice get_voice_filename("mhr", 270)
    miharu "「……ああ。また明日だね、凛火」"

    "他の選定の参加者たちに対し、私たちは仲間割れをしたように見せている。"

    "万が一見られてしまったら、嘘だと見破られてしまうかもしれない。"

    "私は海晴に声をかけて、教室を後にした。"

    jump f005_2.s2_end

label f005_2.s2_2:


    show rnk uni nor que at std_cr with std_in

    voice get_voice_filename("rnk", 803)
    rinka "「一緒に駅まで行く？」"

    show mhr uni sco cau rev at std_cl with std_in

    voice get_voice_filename("mhr", 271)
    miharu "「……本当かい？」"

    "そう訊き返した海晴は、荷物をまとめる手を早めた。"

    "教科書の下には、学校支給のものではない参考書も含まれていた。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「そんなに焦らなくてもいいよ」"

    show mhr uni sco dis rev with std_change

    voice get_voice_filename("mhr")
    miharu "「遅くなったら、君はぼくを見捨てて先に行ってしまうかもしれないからね」"

    "海晴の言葉に、私は苦笑いを浮かべた。"







    $ set_info_location("14")


    stop music fadeout 1
    scene bg schoolgate noon with fade_long
    play music audio.miharu
    pause 1

    show rnk uni nor smi at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「昨日はありがとね」"

    show mhr uni nor nor rev at std_cl with std_in

    voice get_voice_filename("mhr")
    miharu "「大したことはしていないよ。ぼくも丁度そのことについて聞こうと思っていたところなんだ。一体何があったんだい？」"

    show rnk uni arm ama with std_change

    voice get_voice_filename("rnk")
    rinka "「えっと……話すと長くなるんだけどさ」"

    "海晴と二人きりになる以上、この話題を避けられないのは分かっていた。"

    "私は、牛塚さんの家に行っていたことと、Ⅺの女性が襲撃してきたことを海晴に話した。"

    "海晴は私の話の冒頭あたりから顔を歪ませ、最後には呆れてため息をついていた。"

    show mhr uni sco cau rev with std_change

    voice get_voice_filename("mhr")
    miharu "「呆れを通り越して、ぼくはもはや君のことが恐いよ」"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「でも……何とかなってる。Ⅻの人とも、ちゃんと話せることが分かったし」"

    show mhr uni nor ser rev with std_change

    voice get_voice_filename("mhr")
    miharu "「話してどうするんだい？　最後には、彼のことも脱落させないといけないんだ」"

    "自分でも楽観的だとは思っていたが、海晴は間髪入れずにそう差し込んできた。"

    "私は言い返すことができず、目を逸らしてしまった。"

    show mhr uni nor nor rev with std_change

    voice get_voice_filename("mhr")
    miharu "「まあ、君がどんな行動をしようが否定しないし、どんなことがあってもぼくは君を守る」"

    show mhr uni sco thi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「もっとも、君にあった出来事を話してくれないよりはいい、か」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「海晴は、何かないの？」"

    show mhr uni sco smi rev with std_change

    voice get_voice_filename("mhr")
    miharu "「くすっ、気になるかい？」"

    "海晴は微笑んで、そう問い掛けて来た。"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「……教えてくれないやつでしょ」"

    show mhr uni nor rea rev with std_change

    voice get_voice_filename("mhr")
    miharu "「さすが凛火だ。ご名答」"

    "その後は、他愛のない話をしながら駅へと向かった。"

    hide rnk
    hide mhr
    with std_out

    "駅までついたら、お互いに「また明日」と言い、別れた。"



    jump f005_2.s2_end

label f005_2.s2_end:

    $ add_seen_chapter("5-5")







    python:
        set_info_scene("69")
        set_info_date(6, 2, "sat")
        set_info_time("evening")
        set_info_location("08")


    stop music fadeout 2
    scene bg schoolroom noon with fade_longest
    play music audio.nichijo02
    pause 1

    $ show_hud()

    "昨日は、久しぶりにちゃんとお店を開けていた。"

    "お休みが連日続くと当然客足も遠のくが、たまたま前を通りかかった常連さんが寄ってくれた。"

    "お客さんのほとんどはおばあちゃんがいないという事情をある程度理解してくれているので、責めるどころかむしろ応援してくれるので、助かっている。"

    show mao uni nor no1 rev at std_cl with std_in

    voice get_voice_filename("mao")
    mao "「りーたん、文化祭の次の週、どっか行かない？」"

    "帰りがけ、話しかけてきたのは真央だった。"

    show rnk uni nor nor at std_cr with std_in

    voice get_voice_filename("rnk", 810)
    rinka "「いいけど、どこに？」"

    show mao uni nor ch1 rev with std_change

    voice get_voice_filename("mao")
    mao "「んー、まだ決めてないけど、映画とかカラオケとか？」"

    "私が返事を躊躇っていると、真央はにやにやと笑ってみせた。"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたんが恥ずかしがりながら歌うとこ、また見たいのだよ……」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「……だから嫌なんだよ」"

    show mao uni nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「でもさ、なおりんとはまだカラオケ行ったことなかったよね？　文化祭が終わって丁度いいタイミングだと思うし、いいんじゃないかなぁ～？」"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「ってかさ、なおりんって歌上手いと思うんだよねー、うち。何歌うのか知らないけど、大人しい子が意外と上手かったりするしねぇ」"

    show mao uni sel lau rev with std_change

    voice get_voice_filename("mao")
    mao "「問題はみはるんのバイトだけど……、ま、何とかなる気がするなぁ」"

    "真央は続けざまに喋る。"

    "これは、私が反対する隙を与えない作戦だと分かっている。"

    "確かに直未がどんな歌を歌うのか興味もあるので、「いいよ」と返事をした。"

    show mao uni sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「いえーい。んじゃ、ちゃんと再来週の土曜は開けといてねぇ」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「うん、分かった」"

    "再来週の土曜日というと、日程的には16日だ。"

    "間に、二度の選定を挟むことになる。"

    "このまま行けば今週指名されることはなさそうだが、来週は分からない。"

    "もっとも、そんな気持ちでは駄目なことくらい分かっている。"

    "来週も再来週もずっと、私は指名されてはいけないのだ。"

    show mao uni nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「りーたん？」"

    "考え込んでしまった真央に「ごめんね」と伝えて、私たちは教室を後にした。"






    python:
        set_info_scene("70")
        set_info_location("02")


    stop music fadeout 1
    scene bg station01 with fade_long
    play music audio.nichijo03
    pause 1

    $ show_hud()

    "新宿で少し寄り道をしたあと、私はホームで電車を待っていた。"

    "そういえば最近あまり本屋さんに行けていなかったと思いつき、寄ってみたのだ。"

    "少女漫画の新刊が出ていたのを、何冊か買ってみた。"

    show nom uni nor lau rev at std_cl with std_in

    voice get_voice_filename("nom", 265)
    naomi "「あ、凛火先輩っ！」"

    "偶然、直未が声をかけてきた。"

    "直未も本屋さんのビニール袋を持っていたので、同じ場所にいたことになるだろう。"

    "何を買ったかという話を少ししてから、直未は目を細めて訪ねてきた。"


    play music audio.gimon

    show nom uni hes tr1 rev at std_cl with std_in

    voice get_voice_filename("nom")
    naomi "「そういえば……あの子、どうなったんですか？」"

    "あの子、というのはユウくんのことだろう。"

    "直未と駅で姿を見かけたときには名前を知らないどころか、私は彼のことを女の子だと思っていたことが懐かしい。"

    "海晴には概ね話したけれど、直未にはどこまで話せばいいのか考える。"

    "そして、海晴の忠告を思い出した。"

    show rnk uni arm ama at std_cr with std_in

    voice get_voice_filename("rnk")
    rinka "「うーん、大丈夫だったよ」"

    show nom uni nor ser rev with std_change

    voice get_voice_filename("nom")
    naomi "「……そうですか」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「……ごめんね」"

    "短いやり取りだけど、直未もきっと思うところは多かっただろう。"

    "中途半端に話すくらいならと、話さないことに決めたのだ。"

    "直未は辛そうな表情を浮かべている。"

    "私は心が痛くなるが、露骨に避けられている直未の方がずっと辛いことが分かるので、「でね……」と無理矢理話題を変えることで取り繕おうとした。"

    show nom uni que que rev with std_change

    voice get_voice_filename("nom")
    naomi "「先輩、どうしたんですか？」"

    "何ともなしに人混みに目をやった時、私は見覚えのあるシルエットに気がついた。"

    "直未に悟られないように向き直るが、横目でちらちらとその姿を確認していた。"

    "視線の先にはⅣの少年――ユウくんがいたのだ。"

    "彼はさも待ち合わせしているかのように、人混みの中に紛れていた。"

    "しかし、彼にこの駅で待ち合わせをするような相手がいないことを知っている。"

    "何食わぬ顔をしているけれど、ちらちらとこちらを見ている。"

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「お店の買い物を思い出しちゃった。ごめん、今日は先帰ってて」"

    show nom uni nor sur rev with std_change

    voice get_voice_filename("nom")
    naomi "「あ、だったら私も……」"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「ううん、大丈夫。文化祭の準備で疲れてるだろうし、ちゃんと休んだ方がいいから」"

    show nom uni nor ser rev with std_change_wait

    "直未は含みのある顔で頷いた。"

    hide nom with std_out

    "私はそのまま、直未が電車に乗るまでを見送った。"


    stop music fadeout 1

    "一人になったのを確認してから、彼は私の方へと近付いて来た。"

    show yuu sta nor nor rev at std_cl with std_in

    voice get_voice_filename("yuu")
    yuu "「……お姉ちゃん」"

    "私がユウくんを認識していたことは、彼も分かっていたのだろう。"


    play music audio.growapart

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「お姉ちゃんにね、お願いがあるんだ」"

    "挨拶などを抜きにして、ユウくんはいきなり本題へと入った。"

    "私も彼がここにいたことに戸惑うことはなく、無言で話を聞くことにした。"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「おじいちゃんを家族と、会わせてあげたい」"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「だから、一緒に場所を調べて欲しいんだ」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「おじいちゃんは大丈夫って言って、もう諦めてるけど、ホントはずっと会いたがってたんだ」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクは……気付いてたよ。気付いてたけど、悔しくって。会いに行こうっていってあげられるのはボクだけなのに、言えなくって」"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「今日までずっと、迷ってたんだ。ボクはどうすればいいのか、分からなかったから」"

    show yuu sta nor tro rev with std_change

    voice get_voice_filename("yuu")
    yuu "「でも……、でも！」"

    show yuu sta war cla rev with std_change

    voice get_voice_filename("yuu")
    yuu "「このままじゃボクも――おじいちゃんも、後悔しちゃうから！」"

    "ユウくんは人目もはばからず、感情的に叫んでいた。"

    "彼のその感情の発露を、私は止めることはしない。"

    "彼はひとしきり言い終えて、不安げな顔で私を見つめた。"

    "無理もない。普通なら彼のお願いを聞くことはしないだろうから。それでもユウくんは私ならと、そう思ったに違いない。"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「どこにいるのか知らないし、たぶんおじいちゃんに聞いても教えてくれない」"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「アレンさんはもっと無理だし……ボクにはもう頼れる人はお姉ちゃんしかいないんだ！」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「だから……」"

    "無言の私を見て、彼は断ることを想定したのだろうか。"

    "私は少し、おかしくなっていた。"

    "必死な彼を見て、微笑ましい気持ちになっていた。"

    "だって――。"


    play music audio.commit

    show rnk uni nor nor with std_change

    voice get_voice_filename("rnk")
    rinka "「同じ会社で異動になって地方に引っ越しただけだから、地域を特定するのはそう難しくなかったよ」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「あとは……部署をいくつか変えながら電話してみたら意外と何とかなったんだ。選定が始まってから、嘘の演技にちょっとは慣れたからかな。大体の町までは絞れたよ」"

    show yuu sta war sur rev with std_change

    voice get_voice_filename("yuu", 163)
    yuu "「えっ……？」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk")
    rinka "「あとは、君の頑張り次第かな。近所の人とかに聞き込みをして、家を見つければいいよ」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk", 90001)
    rinka "「新幹線代と今日の宿泊代は……まあ、貸してあげる。おばあちゃんには内緒だけど、後で返してくれれば大丈夫かな」"

    show yuu sta nor que rev with std_change

    voice get_voice_filename("yuu", 165)
    yuu "「……お姉ちゃん？」"

    show rnk uni arm nor with std_change

    voice get_voice_filename("rnk", 820)
    rinka "「牛塚さんを連れて行けはしないんだったら、君が説得して牛塚さんのご家族に来てもらうようにしないと」"

    show rnk uni arm lie with std_change

    voice get_voice_filename("rnk")
    rinka "「私はそこまでは協力できない――けど、自分を信じてね」"

    show yuu sta nor que rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ちょっとお姉ちゃん、どういうこと？」"

    "だって、牛塚さんがその名を授けた通り、ユウくんは優しくて勇気がある子だったのだから。"

    "戸惑うユウくんに、私は封筒を手渡した。"

    "中には私が調べた牛塚さんの家族についての情報と、こっそり持って来たお金が入っている。"

    show yuu sta war sur rev with std_change

    voice get_voice_filename("yuu")
    yuu "「分かって……たの？」"

    show rnk uni nor smi with std_change

    voice get_voice_filename("rnk")
    rinka "「何となくだけど、私も同じことを考えてたから」"

    "ここからは、ユウくんと牛塚さんの物語だ。"

    "その結末を、私は見届けようとは思わなかった。"

    "ユウくんに可能性を託せたから、牛塚さんがたとえ脱落してしまっても、もう後悔はしないだろう。"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「おじいちゃんが、最期に笑っていられるように。ボク、頑張るよ」"

    show yuu sta lau lau rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ありがとう、お姉ちゃん！　お金は絶対返すから！」"

    "ユウくんは笑顔でそう言ったあと、少しの間動かなかった。"


    stop music fadeout 1

    "私が「そろそろ行くね」と声をかけようとしたとき、真剣な表情で「待って」と話し始めた。"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「もう一つお願いがあるんだ」"

    "神妙な表情は、明るい話題ではないことを示していた。"

    "ここからは、私が完全に予想外のことだった。"


    play music audio.disclose

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクを、脱落させて欲しい」"

    show rnk uni sur su2 with std_change

    voice get_voice_filename("rnk")
    rinka "「えっ……」"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「お姉ちゃんがボクの≪カード≫を３枚持っていることは、察しがついてた」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ただね、お姉ちゃんは優しいから、ボクを指名できないんじゃないかって思ってたんだ」"

    show rnk uni nor que with std_change

    voice get_voice_filename("rnk")
    rinka "「……どうして？」"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「お姉ちゃんに、生きて欲しいって思ったからなんだ」"

    show rnk uni arm ang with std_change

    voice get_voice_filename("rnk")
    rinka "「そんなの！　……ごめん、大きな声出しちゃったね」"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクは本気だよ。お姉ちゃんがボクを脱落させるなら、納得できるから」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「それだけじゃない――ボクはきっと、生きてちゃいけないんだ」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「生きてちゃ……いけない？」"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクがなくした記憶は、全然戻る気はしないよ。でもね、時々自分が怖くなる」"

    show yuu sta nor tro rev with std_change

    voice get_voice_filename("yuu")
    yuu "「ボクの中にいるもう一人のボクが、何か怖ろしいことをしようとしている気がして……」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「もし記憶が戻ったら、ボクは何するか分からない。ボクがボクじゃなくなっちゃうかもしれない」"

    show yuu sta war sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「だから！　その前にボクを殺して！」"

    "ユウくんは追い詰められたような声でそう告げた。"

    "心の中にいる自分の知らない自分が、ユウくんを追い詰めているのだろう。"

    "彼の言う通り、私は今週の選定ではユウくんを指名するつもりはなかった。"

    "まだその覚悟はできていなかったのだ。"

    show rnk uni arm sad with std_change

    voice get_voice_filename("rnk")
    rinka "「……ごめん、即答はできない」"

    show yuu sta nor sad rev with std_change

    voice get_voice_filename("yuu")
    yuu "「どうして？　お姉ちゃんが生きたいんだったら、いずれはボクのことも脱落させるはずでしょ？」"

    show rnk uni arm ten with std_change

    voice get_voice_filename("rnk")
    rinka "「そうだよ。でも、もしユウくんを脱落させるとしたら、それはユウくんの記憶が戻ってから。真実が、分かってから。ユウくんは記憶喪失で、不安になっているだけなんじゃないかな？」"

    show rnk uni arm vig with std_change

    voice get_voice_filename("rnk")
    rinka "「何も分からないままユウくんが脱落したら、私は後悔するかもしれない」"

    show yuu sta war cla rev with std_change

    voice get_voice_filename("yuu")
    yuu "「駄目だよ！」"

    "それでも、ユウくんは食い下がる。"

    "私の性格を知っているだろうに、彼はまるで気にせず続けた。"

    show yuu sta nor tro rev with std_change

    voice get_voice_filename("yuu")
    yuu "「お願いだから――優しいお姉ちゃんなら、聞いてくれるよね？」"

    "その質問に、私は答えることはできなかった。"

    "ユウくんは大きな瞳でずっと、私を見つめている。"

    "彼が怖ろしいことをする――そんなことを言われても、信じられない。"

    "戦い方を知らざるをえないような過去を持っているのかもしれないけれど、だからと言って彼の抱える不安とは繋がらない。"

    show yuu sta nor ser rev with std_change

    voice get_voice_filename("yuu")
    yuu "「絶対だよ」"

    hide yuu with std_out

    "返事のできない私に痺れを切らしたのか、ユウくんは短くそう言い残し、乗換ホームへと去っていった。"

    "彼にはっきりとした返事ができなかったのは、私の中で答えは決まっていたからだ。"

    "――今はまだ、できないと。"

    $ add_seen_chapter("5-6")







    python:
        set_info_scene("71")
        set_info_date(6, 3, "sun")
        set_info_time("night")
        set_info_location("05")



    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "日曜日は久々に、終日お店を開けていた。"

    "ここ最近は休みがちだったため、ちょっとなまってしまったのだろう、足が疲れてしまった。"

    "それでも、労働の汗を流すのは気持ちいい。"

    "ライオン館でくつろいでいるお客さんの顔を見ていると、充実感もある。"

    show rnk civ nor nor at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「よし、シャワーを浴びて早く寝よう」"

    "今日は、女神の選定。"

    "何時に寝たって関係はないのだけれど、睡眠時間は多い方が、明日の寝起きはマシなはずだ。"



    scene bg myroom night with fade_long
    pause 1

    "シャワーを浴びて部屋へ戻ると、丸くって黒い塊が部屋にあった。"

    "黒猫のレテが、ふてぶてしい態度でベッドの上にいた。"

    show rnk paj nor smi at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「もう……」"

    "口ではそう言いつつも、一人じゃないことが心強かった。"

    $ add_seen_chapter("5-7")

label sentei5:

    call set_replay












    python:
        set_info_date(6, 3, "sun")
        set_info_scene("72")
        set_info_time("lnight")
        set_info_location("07")

    stop music fadeout 2
    scene bg fatalhall01 up large with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    show dia sta fro nor big at std_c with std_in

    voice get_voice_filename("dia", 114)
    parca "「ごきげんよう。運命の奴隷の皆サマ」"

    "女神の声が、運命の大広間に響く。"

    "私は今夜も、女神の選定の場へと来ていた。"


    voice get_voice_filename("sgt", 260)
    ushizuka "「ほっほ。録画をせんでも毎週忘れることがないから楽じゃのう」"

    show dia sta fro fee big with std_change

    voice get_voice_filename("dia")
    parca "「あらおじいサマ？　テレビ番組のようにおっしゃらないでくださいます？」"


    voice get_voice_filename("sgt")
    ushizuka "「女神様もテレビのことは知っておったんじゃのう」"

    show dia sta fro smi big with std_change

    voice get_voice_filename("dia")
    parca "「ワタクシはこれでも、浮世の流行には敏感なのでございますわ」"

    show dia sta fro nor big with std_change

    voice get_voice_filename("dia")
    parca "「時の移ろいから外れた存在のワタクシですけれど、無為に過ごすには退屈過ぎますもの」"

    "女神は牛塚さんに対し、微笑みながらそう答えていた。"

    "ファンタジー世界の登場人物のような彼女からテレビという言葉が出るのは、とても違和感があった。"

    "上位の存在である彼女は、夢の世界から私たちの世界を全て監視でもしているのだろうか。"

    show dia sta fro no2 big with std_change

    voice get_voice_filename("dia")
    parca "「皆サマ、そろそろお疲れのご様子ですね。選定も中盤……無理もありませんね」"


    voice get_voice_filename("fed", 140)
    federico "「おいおい、とっとと始めてくれないか？　あんたの言う通り確かに疲れてるから、睡眠時間は確保したいんだよ」"

    "海晴の隣から、Ⅲのカルミナーティさんがおどけた口調でそう言った。"

    "彼を見ると、特に怪我などはしていないようだ。"

    "ユウくんは彼にしばらく動けない怪我を負わせたと言っていたが、勘違いだったのか。"

    "あるいは、夢の世界では現実世界の体調は影響しない……か。"

    "とすれば、彼が健康に振舞うことは怪我をしていることのカムフラージュにもなる。"

    show dia sta fro fee big with std_change

    voice get_voice_filename("dia")
    parca "「全くもうっ。皆サマはせっかちさんで嫌になりますわ。ワタクシの退屈をもっと紛らわせてくださってもよろしいのに」"

    show dia sta fro smi big with std_change

    voice get_voice_filename("dia")
    parca "「まあ、仕方がないと致しましょう。今宵を含め、≪女神の選定≫はまだ８回も残っているのですから」"

    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「それでは、今宵も女神の選定を始めますわ」"


    voice get_voice_filename("dia")
    parca "「廻りなさい。運命の大時計」"


    scene bg fatalhall01 normal with dissolve_long

    "その後は、いつもと同じ流れだ。"

    "時計が回り、順番に指名の意志確認を行っていく。"

    "Ⅰ番の私は、当然最初に聞かれる。"

    "今夜も、私は指名を行わない宣言をした。"

    "さらに順番に時計は回り、今夜氏名を行うのは結局Ⅻのアランさん一人だ。"

    scene bg fatalhall01 up with dissolve

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln", 158)
    alan "「僕は、“Ⅴ”を指名させてもらおう」"

    "あらかじめ分かっていた通り、Ⅴの牛塚さんを指名した。"

    show sig sta nor nor ci at ci_r with ci_in

    "牛塚さんは満足そうな表情を浮かべていた。"

    "その裏にどんな想いがあるのか推し測ることしかできなかったけれど、きっと彼らの物語は悪い結末ではなかったのだろう。"

    "それよりも。"

    hide aln
    hide sig
    show yuu sta eml sad rev ci at ci_l
    with ci_swap

    voice get_voice_filename("yuu", 185)
    yuu "「――どうして。お姉ちゃんの、嘘つき」"

    "夢の世界に虚しく漂う彼の呟きへ、私は罪悪感を抱いていた。"







    python:
        set_info_scene("73")
        set_info_location("16")

    scene bg fatalhall02 normal with fade

    "運命の大広間の上層で、青年と老人が向かい合っていた。"

    "アランと茂継だ。"

    "すでに３回目の指名となる彼は、この空間に来ても前２回と同じように表情を変えることはなかった。"

    scene bg fatalhall02 up with dissolve

    show sig sta nor nor ci at ci_r with ci_in

    voice get_voice_filename("sgt")
    ushizuka "「ほう、すごいのう。夢の世界とやらはこんな風になっておったのか」"

    show aln sta nor nor rev ci at ci_l with ci_in

    "茂継に対し、アランは何も言わなかった。"

    "感情の読めない瞳で、老人のしわくちゃの笑顔をとらえている。"

    show dia sta fro gl1 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「貴方サマはすっかり常連ですわね」"

    "いきなり姿を見せた女神に対して、アランは何も答えない。"

    show dia sta fro cl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシも、貴方サマがつれないお方だというのは分かっていますわ」"

    show dia sta fro sm2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「それでは、３枚のカードをお選びくださいませ」"



    play music audio.electing
    scene ecg senteialan nor with dissolve_long

    "アランは開かれたカードブックから、３枚のカードに触れ、選び取る。"

    "そして、その内容を淡々と読み上げた。"


    voice get_voice_filename("aln")
    alan "「氏名、牛塚茂継。死因、餓死。未練……仲の良かった家族」"


    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、とはいえ、わしはもう思い残すことはないがのう」"


    scene bg fatalhall02 up
    show sig sta nor nor ci at ci_r
    with dissolve_long

    voice get_voice_filename("sgt")
    ushizuka "「どんなからくりを使ったかは知れんが、わしの息子たち一家と会わせてくれおった」"

    show aln sta nor clo rev ci at ci_l with ci_in

    voice get_voice_filename("aln")
    alan "「何を言う」"

    show aln sta nor nor rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「からくりではないだろう。彼――貴様の家族からの冥途の土産だろう？　そう言ってやらなければ、報われない」"

    show sig sta inn smi ci with ci_change

    voice get_voice_filename("sgt")
    ushizuka "「ほっほ、分かっておるよ。老人の照れ隠しじゃ」"

    show aln sta nor gen rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「……そうか」"

    show sig sta nor nor ci with ci_change

    voice get_voice_filename("sgt")
    ushizuka "「意外じゃのう。いや、意外でもないか。短い付き合いじゃったが分かる。おぬしは――誰よりも家族想いじゃとな」"

    show aln sta nor que rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「……フン。余計な話をし過ぎた。女神、もういいだろう？」"

    show dia sta fro nor ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「あら、もうよろしいのですか？」"

    scene ecg trianglecard small with dissolve_long

    "パルカの問いかけにアランが答える前に、アランの取り出したカードを中心として白い光が広がり始める。"

    show ecg trianglecard cover with ecg_change_wait

    "光は一瞬で、この空間を覆いつくした。"






    stop music fadeout 2
    scene white with Dissolve(3)
    play music audio.death
    pause 3







    scene bg shigetsugu01 night with dissolve_longest

    "孤独であった。"

    "自宅の床。"

    "布団ですらない剥き出しの畳の上で、空腹に爛れた思考で過去を見る。"

    "あの頃をもう一度。"

    "叶わぬ夢が彼の脳裏に焼き付いたまま、命の灯は消えていく。"






    stop music fadeout 2
    scene bg fatalhall02 up with fade_longest
    pause 1

    $ add_character_cards("aln", ["5_name", "5_death", "5_regret"])

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln")
    alan "「同情もしない。もっとも、貴様の場合は最期に夢を見たのだ――十分だろう」"

    show dia sta nor ama ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「やはり珍しいですわね。貴方サマが少しでも感傷をお見せになるなんて」"

    show aln sta nor irr rev ci with ci_change

    voice get_voice_filename("aln")
    alan "「余計な話はいいと言っているはずだ。貴様は貴様の仕事をしてくれ」"

    show dia sta nor smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「まこと、面白味のない方ですわね。もっとも――もう幾度かすれば、貴方サマの興味深いところが見られるかもしれませんけれど」"

    "アランの乗った床が動き出し、茂継の持っていたカードが彼の前に展開される。"

    "下層に戻る前に、彼はどのカードを取得するのか決める必要があるのだ。"

    "アランは相変わらずの無表情で、カードを選び始めた。"











    python:
        set_info_scene("74")
        set_info_location("07")

    scene bg fatalhall01 normal with fade_long
    pause 1

    "しばらくして、アランさん一人だけが戻って来た。"

    scene bg fatalhall01 up with dissolve

    show dia sta fro no2 ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「それでは、どのカードを選びますか？」"

    show aln sta nor nor rev ci at ci_l with ci_in

    voice get_voice_filename("aln")
    alan "「≪Ⅳ・未練≫のカードをもらおう」"

    $ add_character_cards("aln", ["4_regret"])

    show yuu sta eml non ci at ci_r with ci_in

    voice get_voice_filename("yuu")
    yuu "「…………」"


    play music audio.restlessness

    "様子がおかしい、と思っていた。"

    "ユウくんは、アランさんが自分のカードを宣言しても表情一つ変えはしなかった。"

    "いや、それよりも。"

    "彼の顔つきは明らかに、たった数分前と異なっていた。"

    "その表情に、ぞくりと悪寒が走る。"

    "彼はアランさんよりも、私の方を見ていたのだ。"

    hide dia
    hide aln
    hide yuu
    show mhr uni pai irr rev ci at ci_l
    with ci_swap

    voice get_voice_filename("mhr", 280)
    miharu "「あの子は……」"

    "私が彼を指名しなかったことに対して怒っている――それだけにはとても思えなかった。"

    "もっと異質な、たとえるなら底無し沼を覗くような錯覚をするような、そんな目をしていた。"

    show rnk uni arm pai ci at ci_r with ci_in

    voice get_voice_filename("rnk", 832)
    rinka "「たっ……！」"

    "夢の世界にもかかわらず、頭の奥に痛みを感じる。"

    "立っていられない程ではないので、精一杯堪えていた。"

    scene white with dissolve_fast

    scene ecg cardbreak with dissolve_long
    play se "glass_break"
    pause 1


    voice get_voice_filename("aln")
    alan "「何っ……？」"

    "アランさんがカードを手にしたとき、私は彼が心から動揺している姿を見た。"

    "白く光っていたカードが、まるでガラスが割れるように破壊されたのだ。"

    "飛び散った破片は、光の粒になって霧散する。"


    scene bg fatalhall01 up large
    show dia sta fro smi big at std_c
    with dissolve_long

    voice get_voice_filename("dia")
    parca "「あら、あらあらあら」"

    "私の本も光を帯びたが、そのことに気付いたときには女神が次の言葉を口にしていた。"

    show dia sta fro gl2 big with std_change

    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者は１名。これをもって、選定を終了といたしましょう」"

    "不協和音はすでに、響き始めている。"

    "私はまだ、その発端に触れたに過ぎなかった――。"

    $ renpy.end_replay()
    $ add_seen_chapter("5-8")

    $ persistent.sentei5_clear = True
    $ grant_achievement("divine_selection_05")

    jump f006
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

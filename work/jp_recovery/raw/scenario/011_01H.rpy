

label f011_01H:






    python:
        set_info_scene("180")
        set_info_time("evening")
        set_info_location("04")


    scene bg lion01 evening with fade_long
    play music audio.nichijo01
    pause 1

    $ show_hud()

    "最後のお客さんを見送ったあと、私は深いため息をついて座っていた。"

    "無気力なまま、一日が終わろうとしていた。"

    "お店の仕事に集中していれば考えなくてよかったことも、つい考えてしまうからだ。"

    show mao sci nor no1 rev at std_cl with std_in

    voice get_voice_filename("mao", 291)
    mao "「いやはや、店長さんがそんなため息はよくないねぇ」"

    "いつの間にか入ってきていた真央が、おどけた口調でそう言った。"

    "私は真央の顔を見て、またため息をついた。"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「ま、仕方がないよ」"

    show rnk apr arm sad at std_cr with std_in

    voice get_voice_filename("rnk", 1653)
    rinka "「聞いたんだ」"

    show mao sci sel glo rev with std_change

    voice get_voice_filename("mao")
    mao "「仕組んだ側としては聞いておかないとさ～」"

    "真央は飄々と言うと、テーブルに座った。"

    "見れば、随分と大荷物だ。"


    play music audio.relaxtime
    scene ecg maocomic normal with dissolve_long


    voice get_voice_filename("mao")
    mao "「今日は、真央様おすすめのマンガを大量に借りてきました。一晩じゃ読み切れないくらい。ふぃー、重かった」"

    "言うと、真央は見慣れないボストンバックから大量のマンガをテーブルに並べた。"


    voice get_voice_filename("mao")
    mao "「うち、今日りーたんの家に泊まるから。よろしく」"


    voice get_voice_filename("rnk")
    rinka "「ええっ。私よりも、海晴の方が……きっと」"


    voice get_voice_filename("mao")
    mao "「みはるんは今日はバイトだよ。きっとフられると思ったから、土日はバイトを詰めこんでたみたい」"


    voice get_voice_filename("mao")
    mao "「それに、今はうちがいったって泣いてるみはるんの横でマンガ読んでるだけだしぃ」"

    "うちでもマンガを読むだけな気もするが、黙っていることにした。"

    "フったとはっきり言われると、より自覚してしまう。"

    "私は間違いなく自分の意志で、海晴との恋愛関係を拒否したのだ。"

    "それは、罪ではない。"

    "だからこそ、罰で許されることはできない。"

    "辛いのは海晴の方だとは分かっているけれど――割り切れないから、さっきため息をついたのだ。"


    voice get_voice_filename("mao")
    mao "「りーたんといた方がいいよ。りーたん、告られるなんて初めてだからダメージ大きいだろうし。相手みはるんだしさ」"


    voice get_voice_filename("mao")
    mao "「この土日が終わったら、切り替える。これ、真央様からの命令」"


    voice get_voice_filename("mao")
    mao "「みはるんがうちに頼んだのは、ここまで含めてだからさ～って、言っちゃった。今のはみはるんには内緒ね」"

    "ああ、わざとだなとすぐに分かった。"

    "そっか、海晴は私に告白を断られると予想して、真央にその後のフォローまで頼んでいたのか。"

    "しかも自分じゃなくて、私のこと。"

    "私は、言葉を失っていた。"

    "海晴の覚悟と決意の重さを、改めて知ったからだ。"

    "当たって砕けろなんて軽い気持ちじゃない。"

    "ビル解体作業のように、とても繊細な行動だったのだ。"


    voice get_voice_filename("mao")
    mao "「でもさ、りーたん……ありがとね。みはるんにはっきり返事してくれて」"


    voice get_voice_filename("mao")
    mao "「中途半端な返事なんて、みはるんは望んでないわけだったしぃ」"


    voice get_voice_filename("mao")
    mao "「これで、みはるんも新しい恋に進めるわけなのだよ！」"

    "さすがの真央も、今回のことは結構堪えたのだろう。"

    "人間関係を見るとなるほど、今回はややこしい。"

    "ぎこちない優しさが切なく、だけど嬉しかった。"


    voice get_voice_filename("rnk")
    rinka "「……さ！　どれから読めばいい？」"


    voice get_voice_filename("mao")
    mao "「実は１巻が借りられてるのが多くてさ～、最初から読めるのってこれかこれくらいなんだよねぇ」"


    voice get_voice_filename("rnk")
    rinka "「……おい」"

    "真央がすすめてきたのは珍しく少女マンガではなくて少年マンガだった。"

    "それも、私が生まれる前から続いているおそろしく長いシリーズ。"

    "私は観念して、マンガを読んだり話したりしながら、真央と一緒にこの土日を過ごすことに決めた。"

    $ add_seen_chapter("11_4-2")










    python:
        set_info_scene("181")
        set_info_date(7, 15, "sun")
        set_info_time("night")
        set_info_location("05")


    stop music fadeout 2
    scene bg myroom night with fade_longest
    play music audio.myroom_night
    pause 1

    $ show_hud()

    "日曜日の夜、間もなく11回目の選定を迎えるというとき、私は自室でまったりと過ごしていた。"

    "結局、土日のほとんどを真央と過ごした私は、我ながら堕落した生活を送っていたと思う。"

    "日記帳も読まなかったし、選定について考えることもしなかった。"

    "あと一度あるからと、完全に気を抜いていた。"

    "もっとも海晴とのことが私にとって重くのしかかっていたことも事実であり、真央と過ごすことで大分気が楽になったことも事実なのだけど。"

    "22時頃、海晴からチャットが届いていた。"

    "今日の選定で、自分を指名してくれというものだった。"

    "もちろんそれには続きがあり、海晴がそれを防御する、ということである。"

    "確かに、その方法を試すならば今回しかない。"

    "海晴と私であれば裏切られる心配もないし、やはり僅かでも可能性があるなら試すべきだろう。"

    "私は納得して、海晴に了承の返事を送っていた。"

    "来週からは切り替える。真央の言った通りにしよう。"

    "すぐに元通りとはいかないけれど、私にとって海晴が大切な友人であることだけは絶対に変わりない。"

    show rnk paj arm lie at std_c with std_in

    voice get_voice_filename("rnk")
    rinka "「おやすみ」"

    "誰に言うでもなく、私はそう呟いていた。"


    scene black with dissolve


    voice get_voice_filename("cat", 16)
    lete "「にゃーお……」"

    "電気を消してから、レテが部屋にやってきた。"

    "どこか寂しそうに鳴いた声が、私の耳に残っていた。"

    $ add_seen_chapter("11_4-3")

    jump f011_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

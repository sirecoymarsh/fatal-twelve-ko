

label fBAD_02:

    if not _in_replay:
        call staffroll ("ED_BAD.mkv")

    call set_replay






    python:
        set_info_date(7, 23, "mon")
        set_info_time("noon")
        set_info_location("18")


    stop music fadeout 2
    scene bg lion02 noon with fade_longest
    play music audio.memories
    pause 1

    "２ヵ月前の話。"

    "連休が始まる直前の５月３日は、真央が親友を二人同時に失った日であった。"

    "それぞれ別のところで、それぞれの死の運命を辿った。"

    "獅子舞凛火は列車での爆破テロに巻き込まれ、後輩の日辻直未を守って死亡。"

    "未島海晴は、自室で自殺。リストカットした直後に睡眠薬を服用し、死亡したものと見られる。"

    show mao sci nor sad rev at std_cl with std_in

    voice get_voice_filename("mao", 341)
    mao "「うちはさ、独りになっちゃったよ」"

    "小熊真央は、親友の自宅の前でぽつりと呟いた。"

    "喫茶ライオン館は、長期休業している。凛火のお葬式が終わったあとも、彼女の祖母は親戚の介護で田舎に帰ってしまった。"

    "しかし家族との想い出が詰まったこの家も手放すことはできなかったらしい。"

    "真央もその気持ちは、痛いほどよく分かっていた。"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「ライオン館はみんなの第二のおうちって、りーたんは言ってたな」"

    show mao sci nor sad rev with std_change

    voice get_voice_filename("mao")
    mao "「でもさ、人がいなくっちゃ、おうちはおうちじゃないよねぇ」"

    "寂しい声は、誰にも届かない。"

    show mao sci nor che rev with std_change

    voice get_voice_filename("mao")
    mao "「遊園地行こうって約束してたのにさ」"

    "それはもう決して叶わない夢。"

    "真央は凛火のお葬式以降、直未とも何となく気まずくなってしまい、話してはいなかった。"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「うちもいつまでもこんなんじゃ、駄目だって思うんだけどさぁ」"

    "ライオン館を見る度に、思い出が駆け巡る。"

    show mao sci nor sad rev with std_change

    voice get_voice_filename("mao")
    mao "「どうして、してないことまで夢に見るのかねぇ」"

    "遊園地でみんなで写真を撮ったこと。"

    "文化祭で直未のクラスの模擬店で、凛火仕込みのコーヒーを飲んだこと。"

    "ただし、真央はミルクと砂糖を大量に入れたこと。"

    "何度も、凛火と海晴と屋上でご飯を食べたこと。"

    "どれもあり得ない日々なのに、真央は夢を見る度、まるで思い出であるかのようにそんな光景を見せられていた。"

    show mao sci nor sad rev with std_change

    voice get_voice_filename("mao")
    mao "「だってそれくらい、悲しくって」"

    "その後、真央は30分ほどライオン館の前にいた。"

    "そろそろ行こうかと意を決して歩こうとしたとき、ちょうど反対側から歩いてきた男性にぶつかってしまった。"

    "背の高い男性だから、急に動いた真央が視界に入っていなかったのだと思った。"

    show mao sci sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「あ、すみま……」"


    play music audio.badguys
    show fed sta nor smi at std_cr with std_in


    voice get_voice_filename("fed", 395)
    federico_unk2 "「おっと失礼、お嬢ちゃん。可愛い顔は汚れてないかい？」"

    show mao sci nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「……え？　いや、大丈夫っすけど」"

    "ナンパかと思い、真央は露骨に嫌な表情を浮かべていた。"

    "カタコトだが日本語を喋っているので、日本に住んでいるのか慣れた観光客かどちらかだろうと思っていた。"

    show fed sta dar phi with std_change


    voice get_voice_filename("fed")
    federico_unk2 "「おっと、そういえばここ、か。≪運命の終着点≫からこんなに近くに住んでたんだなぁ」"

    show mao sci sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「おにーさん、りーたんを知ってるのぉ？」"

    show fed sta dar ser with std_change


    voice get_voice_filename("fed")
    federico_unk2 "「りーたん……ああ、リンカ・シシマイのことか。知ってるよ。オレの……仲間だった奴が随分と肩入れしてたからな」"

    show mao sci nor que rev with std_change

    voice get_voice_filename("mao")
    mao "「……どういう関係？」"

    show fed sta dar smi with std_change


    voice get_voice_filename("fed")
    federico_unk2 "「……ああ、お嬢ちゃんはミハルとも同じ学校か」"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「みはるんのことも？」"

    show fed sta dar phi with std_change


    voice get_voice_filename("fed")
    federico_unk2 "「まあ、な」"

    show mao sci nor lau rev with std_change

    voice get_voice_filename("mao")
    mao "「もしよかったら、二人のこと聞かせてよ。うちの知らない二人がいるんだったら、知っておきたいから」"

    show fed sta dar smi with std_change


    voice get_voice_filename("fed")
    federico_unk2 "「そうか……あんたはあの二人と仲が良かったんだな」"

    "真央は、珍しく必死になっていた。"

    "大好きだった二人の痕跡は、少しでも多く自分の中に刻みたい。それが自分の知らない二人の姿なら、なおさらだ。"

    "思い出して、泣いてしまうかもしれないけれど。"

    show mao sci nor ser rev with std_change

    voice get_voice_filename("mao")
    mao "「仲がいいとかじゃないよ。うちら、親友だから」"

    show fed sta nor int with std_change


    voice get_voice_filename("fed")
    federico_unk2 "「どこまで話していいもんなのか――まあいいか、終わっちまったことだしな」"

    show fed sta nor nor with std_change


    voice get_voice_filename("fed")
    federico_unk2 "「ただ、ちょっとナントカ御苑ってとこに行かなくちゃいけなくてな。話はそこでしてもいいか？　公園なんだろ？」"

    show mao sci sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「……このタイミングでもナンパするわけ？」"

    show fed sta nor pa1 with std_change


    voice get_voice_filename("fed")
    federico_unk2 "「ち、違ぇんだって。大体あんたはオレのタイプじゃねぇから、その心配はいらないぜ」"

    show mao sci sel irr rev with std_change

    voice get_voice_filename("mao")
    mao "「うわ、サイテー」"

    scene ecg maoandfed normal with dissolve_long


    voice get_voice_filename("mao")
    mao "「ま、いいよ。案内するから、教えてねぇ。おにーさんみたいな男の人とどうして知り合いなのか、やっぱ気になるし」"



    voice get_voice_filename("fed")
    federico_unk2 "「ちっ、なんかオレの評価はイマイチ変わらないんだよなぁ」"

    "そして二人は、曇り空の下、歩き出した。"

    "この後、真央は今まで生きてきた自分の知識では理解しきれないような話を聞かされることになるが、それはあくまでこれからの物語。"

    "出会いと別れは無数に絡み合いながら、未来へと進んでいく。"

    "時間は一方向にしか進まないからこそ、尊いのだと。"

    "誰もがいつか、知ることになる。"

    $ renpy.end_replay()









    scene black with wfade_long
    pause 1

    "この日の夜。"

    "未島海晴――蛇鉈海晴は、一人の男から電話を受けた。"

    "スケール・ジョーンズ。"

    "彼は自分の持てる最大限の話術を使い、海晴を説得した。"

    "――どんなに凛火が好きでも、その恋は叶わないと。"

    "――思いを伝えたところで、関係にヒビが入るだけだと。"

    "――獅子舞凛火の未練は、君ではないのだと。"

    "――君は一生、獅子舞凛火と結ばれることはないと。"

    "――ただ一つ、獅子舞凛火の魂を手に入れることができると。"

    "――自らの手で凛火を脱落させれば、彼女の運命を手中にすれば、それは凛火を手に入れることと同義だと。"

    "普段の海晴ならば、スケールからの言葉など戯言と切り捨てただろう。"

    "しかし、この夜が悪かった。"

    "自分の秘密を打ち明けた海晴は、それを秘密にしてきたこと自体に負い目を抱えていた。"

    "それだけではない。"

    "海晴はまだ隠していることがあった。"

    "そのことも、話せない勇気のなさと自己嫌悪も、海晴の心を蝕んでいたのだ。"



    voice get_voice_filename("sca", 299)
    scale "「自分の心に、正直になればいい」"

    "スケールのその言葉は海晴にとって、麻薬になってしまった。"

    "あの時、凛火からの着信を取れなかったというだけで。"

    "運命は、分岐したのだ。"



    voice get_voice_filename("mhr", 941)
    miharu "「ああ、そうか。ぼくは、凛火を――奪いたかったのか」"

    "殺したかったのか。"

    stop music fadeout 3
    scene black with Dissolve(3)
    pause 2

    $ renpy.end_replay()

    $ add_seen_chapter("9_3-5")

    call show_ending_image ("gui/BADEND_02.png")

    $ persistent.BAD02_clear = True
    $ grant_achievement("bad_end_02")
    $ grant_end_comp()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

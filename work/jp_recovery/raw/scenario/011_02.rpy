

label f011_02:

label sentei11:

    call set_replay








    python:
        set_info_date(7, 15, "sun")
        set_info_scene("182")
        set_info_time("lnight")
        set_info_location("07")


    stop music fadeout 2
    scene bg fatalhall01 normal with fade_longest
    play music audio.fatalhall
    pause 1

    $ show_hud()

    "運命の大広間を一周するように浮かぶ12個の円い床の上に立つのは、もはや私と海晴だけになっていた。"

    "どこまでも続くように見えるこの空間。広い視界には、ただ寂しさだけが漂っている。"

    "その寂しさを切り払う一筋の光条は、いつも女神の一声だった。"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro nor big at std_c with std_in

    voice get_voice_filename("dia", 276)
    parca "「ごきんげんよう。運命の奴隷の皆サマ」"

    scene bg fatalhall01 up with dissolve

    show dia sta nor ama rev ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「あら。皆サマといえども、もうお二人サマしかいらっしゃいませんね」"

    "軽薄な皮肉に答えないでいると、女神はそのまま一人語りを続ける。"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「今宵は11度目の選定。いくつもの嘆きの果てに、あなた方のどちらかがワタクシの器になることでしょう」"

    show dia sta fro gl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「おやおや。貴女サマ方だけでは、急かされることもありませんねぇ」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「それはそれで、少し寂しくもありますね」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「此度の選定の参加者は、特に賑やかでございましたから」"

    show rnk uni nor que ci at ci_r with ci_in

    voice get_voice_filename("rnk", 1658)
    rinka "「≪女神の選定≫は、今までに何回行われてきたの？」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「そういえば、気にしたこともありませんでしたわ。確か……」"

    show dia sta nor rev smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「12度目。あら、運命的ですわね」"

    show mhr uni sco cau rev ci at ci_l with ci_in

    voice get_voice_filename("mhr", 817)
    miharu "「きちんと覚えているんじゃないか……」"

    "海晴はため息をつきながら。そう続けた。"

    "12回。それは確かに運命的な数字だった。"

    "選定の期間は12週間であり、参加者は12人。それ自体は、よくあるキリのいい数字であると思っていた。"

    "１年を12に分けた暦から始まり、時計の文字盤や十二支、十二星座など、日本だけでなく世界でも一つのまとまりとして認められている数だ。"

    "けれど今回の選定が12回目となると、意味が違ってくる。"

    "１から順番に数を重ねた12回目。偶然にしては、確かによくできている。"

    "どれくらいの間隔で行われているのかは知らないので、その数が多いか少ないかは分からないのだけど。"

    show dia sta fro cle ci with ci_change

    voice get_voice_filename("dia")
    parca "「おやおや。あまり長話をしてもいけませんわね」"

    "私は女神の言葉を聞き、引っかかることがあった。"

    "そういえば、女神はよく時間を気にする。"

    "選定の参加者同士が話していると、いつまでも放置せず、どこかで無理矢理この≪女神の選定≫を進行するのだ。"

    "この空間は、時間から切り離されているはずなのに――。"

    play music audio.restlessness
    scene ecg parcadeclaration at top with dissolve_long


    voice get_voice_filename("dia")
    parca "「それでは、今宵も選定を始めましょう」"

    "パルカに直接訊ねようと思った矢先、彼女は美しい声で宣言をした。"

    "直後、大広間の中心にある大時計が回り始める。"


    voice get_voice_filename("dia")
    parca "「さて、Ⅰ番サマ。今宵の指名は……いかがなさいますか？」"







    if flags_route_G or flags_route_H:
        jump f011_02GH







    $ set_info_scene("183")


    scene bg fatalhall01 up
    show rnk uni nor nor ci at ci_r
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「私は、指名をしない」"

    show dia sta fro cle ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「……かしこまりましたわ」"

    "女神は私から海晴に、視線を移す。"

    show dia sta fro no2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「Ⅱ番サマはいかがなさいますか？」"

    show dia sta fro sm2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシの……元、器のⅡ番サマ」"

    show mhr uni nor ser rev ci at ci_l with ci_in

    voice get_voice_filename("mhr")
    miharu "「挑発したところで何もないよ。ぼくも指名をしない」"

    show dia sta fro fee ci with ci_change

    voice get_voice_filename("dia")
    parca "「分かりました。もう、面白くありませんわねぇ」"

    hide dia with std_out

    "パルカは頬を膨らませて言うと、踵を返して大広間の中央へと戻っていく。"

    "彼女のそういう態度は、日記帳に書かれていたダイアナさんと被るところがあった。"

    "無邪気で気まぐれな、リンダさんの妹。猫のようだからか、猫に懐かれる少女。"

    show dia sta fro nor ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「お二人サマが指名をなさらないのであれば、今宵の≪女神の選定≫はこれでおしまいでございます」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「次回の選定が、此度の≪女神の選定≫最後の刻{rt}とき{/rt}」"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「もう一度Ⅱ番サマがワタクシの器になるのか、Ⅰ番サマが器になるのか。今から楽しみでございますわ」"

    scene ecg parcawalk nor with dissolve_long


    voice get_voice_filename("dia")
    parca "「どちらが器になっても、くすっ、きっと素敵な生活が待っているでしょうから」"

    "パルカは微笑むと、スカートの裾をつまみ上げてお辞儀をした。"

    "この場所で彼女と出会ったとき、最初に見せた仕草だ。"


    scene bg fatalhall01 up
    show rnk uni nor que ci at ci_r
    with dissolve_long

    voice get_voice_filename("rnk")
    rinka "「一つ、聞かせて。次の≪女神の選定≫で私たちがどちらも指名を行わなかったらどうなるの？」"

    show dia sta fro nor ci at ci_c with ci_in

    voice get_voice_filename("dia")
    parca "「なるほど。確かにもう、その可能性を考慮しないといけない時期になりましたわね」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「運命の奴隷の皆サマに割り当てられた番号が何を意味するのか、想像していただければよろしいかと」"

    show mhr uni sco cau rev ci at ci_l with ci_in

    voice get_voice_filename("mhr")
    miharu "「仮にぼくらがどちらも指名を行わなかった場合……若い方が優先して生き残るということかい？」"

    show rnk uni arm ama ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「……そんな」"

    "だが、パルカの言っているのはそういうことだろう。"

    "この状況になれば、私でもそう予想することは容易い。"

    "私たちに割り当てられた番号のことを、指名の順番程度にしか考えていなかった。"

    "だが、それが運命に関わるものとなれば、話は別だ。"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「もう勿体ぶることもないよね。この番号の意味、教えて」"

    show mhr uni sco thi rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「割り当てられた、と言ったね。つまり、君がつけた番号ではないということだ」"

    show mhr uni sco cau rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「おかしいとは思っていた。ぼくの死をもって≪女神の選定≫という儀式が始動するのであれば、ぼくがⅠ番ではないかと」"

    show mhr uni nor ser rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「もしそうであれば、≪因果の刻≫に発生した僅かな誤差と推測できる。けれど、ぼくがⅡ番の時点でそれは否定される」"

    show dia sta nor smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「ええ、よろしいでしょう。実を言うと、ワタクシもいつ聞かれるかそわそわしていましたの」"

    show dia sta nor nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「皆サマの番号は、ワタクシが好きな数字をつけたものではございません」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「ⅠからⅫの番号は、世界の本流に近い順番。すなわち、Ⅰ番がもっとも世界の本流に近く、Ⅻ番が最も遠いということですわ」"

    "海晴も私も、その説明だけでは理解ができなかった。"

    "世界の本流などという言葉を、私は聞いたことがない。"

    show dia sta fro no2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「世界というのは、無限に支流を作り出す大河のようなもの」"

    show dia sta fro no1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「人間の皆サマは認識することができませんが、ある原因に対して少しずつ違った結果になった世界が、いくつも存在するのです」"

    show dia sta fro sm2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「そしてこの≪運命の大広間≫は、世界を俯瞰する場所」"

    show mhr uni nor ser rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「一度目の選定で、君はそう言っていたね」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「ええ」"

    show rnk uni arm ang ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「ちょっと待って。本流とか支流とか、どういうこと？」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「例えば、貴女サマが朝食にパンを食べようと思ったとき、貴女サマが朝食にパンを食べた世界と、食べなかった世界が生まれます」"

    show rnk uni nor que ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「……え？」"

    "パルカの言い出した具体例がよく分からず、私は聞き返していた。"

    "パルカは話を止められたことに頬を膨らませてから、「仕方がありませんわね」と話を続ける。"

    show dia sta fro gl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「どうして、二つの世界が生まれるのでしょうか？」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「貴女サマがパンを食べようと思った時点で、貴女サマはパンを食べようとした自分とパンを食べない自分を想像します」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「世界とは人間の皆サマが思っているほど確かなものではありません。あくまで、認知の上に成り立つもの」"

    show dia sta fro cle ci with ci_change

    voice get_voice_filename("dia")
    parca "「結果として貴女サマがパンを食べても、貴女サマの想像の中にパンを食べなかった結果はすでに生まれている」"

    show dia sta fro cl2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「実は、その瞬間、認知上にパンを食べなかったという結果は生まれているのです」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「これが、世界の本流と支流という考え方だとご理解ください」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「つまりこの場合、世界の本流はパンを食べた世界になります。食べなかった世界は支流として進み、本流から少しずつ離れていきます」"

    show rnk uni arm nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「どういうこと？」"

    "私はパルカではなく、海晴の方を見ていた。"

    "海晴は軽く頷いてから、口を開いた。"

    show mhr uni sco cau rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「観測者とでも言えばいいのかな。そうだな。より可能性の高い方が世界の本流になる、と理解すればいいかい？」"

    show dia sta nor nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「さすがⅡ番サマ。実はこのお話、貴女サマと夢の中でお話ししたことがありましたのですけれど、覚えていらっしゃったのですか？」"

    "パルカの問いに、海晴は首を振った。"

    "海晴が言い換えてくれた言葉なら、私でも理解できる。より可能性が高い方……。"

    "パンの話で言えば、私がパンを食べたいと思っているのだから、パンを食べた世界の可能性が高いのは当たり前だろう。"

    show dia sta fro no1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「話が逸れてしまいましたわね」"

    "パルカはわざとらしく咳払いをしてから、続けた。"

    show dia sta fro smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「≪因果の刻≫で皆サマが命を落としてしまったとき、どこかに命を落とさなかった世界も存在する」"

    show dia sta nor ama ci with ci_change

    voice get_voice_filename("dia")
    parca "「ワタクシは運命の女神の力をもって、≪因果の刻≫で結ばれた12人の≪命を落とさなかった世界≫を本流に束ねているのですわ」"

    show mhr uni nor ser rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「今、本流の世界にはぼくたちが≪命を落とした世界≫と≪命を落としていない世界≫が同時に存在するということかい？」"

    show dia sta nor nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「少しだけ、異なっています。矛盾した世界が存在できるのは、あくまで皆サマの集合無意識である夢の世界の中でのみ」"

    show dia sta nor smi ci with ci_change

    voice get_voice_filename("dia")
    parca "「≪運命の大広間≫は本来、世界にとって異物同然。しかしこの場所における認知が、本流世界に影響していると思ってくださっても結構です」"

    "段々、訳が分からなくなってきた。"

    "パルカの語る世界の構造について海晴は興味深く聞いているようだが、私としてはただ混乱するだけだ。"

    "私はパルカが息をついたのを見計らって、床を指差しながら訊ねた。"

    show rnk uni nor que ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「それで結局、この番号は何なの？」"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「察しが悪い、というべきなのでしょうか」"

    show dia sta fro nor ci with ci_change

    voice get_voice_filename("dia")
    parca "「皆サマが生きている世界は、本来であれば世界の支流。その支流をワタクシの力で紡ぎ直すことで、一本の世界にしている」"

    show dia sta fro no2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「簡単に言えば、運命を変えるのが容易い順番と思っていただければよいでしょう」"

    "パルカは半ば投げ遣りにそう告げた。"

    "だが、言いたいことは概ね分かった。"

    show rnk uni nor nor ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「二人残った場合に番号が後ろの人が脱落するのは、運命を変えるのが大変だから切り落とされる――そう思えばいい？」"

    show dia sta fro glo ci with ci_change

    voice get_voice_filename("dia")
    parca "「あら、その通りですわ。貴女サマは変なところで察しがいいのでしたね」"

    "横目で見ると、海晴がパルカの言葉に頷いていた。"

    "海晴に納得されると、私は否定できなくなってしまう。"

    show mhr uni sco thi rev ci with ci_change

    voice get_voice_filename("mhr")
    miharu "「もっと言えば12週間という期間は、君が矛盾した世界を成立させられる限界……と考えてもいいのかい？」"

    show dia sta fro sm2 ci with ci_change

    voice get_voice_filename("dia")
    parca "「さあ。限界は試したことがありませんわ。けれど、それ以上は疲れてしまうから実行しないと思っていただいてよろしいです」"

    "パルカは唇を尖らせてそう言った。"

    "これは、誇張も混ざっていると思った。女神としてのプライドというか、限界と言いたくないというのが傍から聞いていてよく分かる。"

    "つまり、女神の言う本流世界に支流世界をくっつけていられるのは、12週間が限界なのだ。"

    show rnk uni nor que ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「選定の参加者が脱落するってことは、≪死がなかったことになっている世界≫はどうなるの？」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「いい質問ですわね」"

    show dia sta nor ama rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「世界には元に戻ろうとする力があります。ワタクシのような女神が世界の糸を紡いだ時、支流は再び支流に、本来の流れに戻ろうとするのです」"

    show dia sta nor smi rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「脱落した皆サマが≪生きている≫世界は、それぞれ支流となって、この世界――本流の世界から遠ざかっていきます」"

    show rnk uni arm vig ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「なら、どこかにみんなが生きている世界は存在するってこと？　なら……！」"

    show dia sta nor nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「ええ、存在はしているでしょう。けれども一度離れてしまった世界はもう、ワタクシの力をもってしても観測することはできません」"

    show dia sta fro nor rev ci with ci_change

    voice get_voice_filename("dia")
    parca "「≪因果の刻≫で結ばれているからこそ、ワタクシは12もの世界を紡ぎ直すことができたのですから」"

    show dia sta fro cl1 ci with ci_change

    voice get_voice_filename("dia")
    parca "「さて、指名を行わないのであれば、今宵はもうおしまいにしましょう。必要以上に長いお話をしてしまいましたわ」"

    show rnk uni cat ten ci with ci_change

    voice get_voice_filename("rnk")
    rinka "「待って……」"

    scene bg fatalhall01 up large with dissolve

    show dia sta fro no2 big at std_c with std_in

    voice get_voice_filename("dia")
    parca "「それでは、今宵の脱落者はなし。これをもって、選定を終了といたしましょう"

    "パルカは会話を打ち切ると、そのままいつもの通りに選定を終える宣言をした。"

    "海晴と目が合うと、海晴は落ち着いた表情で静かに首を振った。"

    "ここで焦っても仕方ながい。私も冷静さを取り戻し、頷いた。"

    "今回分かったことによって、私たちの逃げ道が断たれたのに等しい。"

    "選定で残った二人は、番号が後ろの方が脱落するということ。"

    "指名を行わなかった場合だけでなく、私が海晴を指名して海晴が防御した場合も、おそらく同じ脱落者の決め方になるだろう。"

    "希望は、私のカードブックに眠る１枚のカードに託されることとなった。"

    $ renpy.end_replay()
    $ add_seen_chapter("11_2-4")

    $ persistent.sentei11F_clear = True
    $ grant_achievement("divine_selection_11")

    python:
        add_character_cards("fed", ["6_regret", "8_death"])
        add_character_cards("yuu", ["5_death", "7_name", "9_name"])
        add_character_cards("sig", ["7_death", "10_regret", "12_regret"])
        add_character_cards("cha", ["5_regret", "6_name", "6_death", "6_regret", "8_name", "12_name"])
        add_character_cards("cnh", ["5_name", "11_name", "11_death"])
        add_character_cards("kik", ["3_regret", "10_regret"])
        add_character_cards("sca", ["6_name", "2_regret"])
        add_character_cards("son", ["1_name", "1_death", "2_name", "2_regret"])
        add_character_cards("ode", ["2_death", "3_death", "3_regret", "8_regret"])
        add_character_cards("aln", ["4_name", "7_regret", "9_death", "11_regret"])

    jump f012_01F
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

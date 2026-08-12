

label fBAD_03:

    if not _in_replay:
        call staffroll ("ED_BAD.mkv")

    call set_replay






    python:
        set_info_date(7, 1, "sun")
        set_info_time("night")
        set_info_location("07")


    stop music fadeout 2
    scene bg fatalhall01 up large with fade_longest
    play music audio.restlessness
    pause 1

    $ show_hud()

    "誰もいなくなったその場所で、女神パルカは微笑んでいた。"

    show dia sta fro cle big at std_c with std_in

    voice get_voice_filename("dia", 516)
    parca "「意外な結末――というべきなのでしょうか」"

    show dia sta fro gl1 big with std_change

    voice get_voice_filename("dia")
    parca "「Ⅰ番サマはもう少し長く、生きてくださると思っていましたのに。だって――」"

    show dia sta fro smi big with std_change

    voice get_voice_filename("dia")
    parca "「おや、誰が聞いているか分かりませんものね。これ以上はこの場所でも、お話ししない方がよろしいでしょうかしら」"

    "スケール・ジョーンズは獅子舞凛火を指名した。"

    "同時に、アラン・スコーピオンはスケール・ジョーンズを指名した。"

    "その時点で、獅子舞凛火は人質にとられていた祖母が助からないのだと直感した。"

    show dia sta fro nor big with std_change

    voice get_voice_filename("dia")
    parca "「けれどⅠ番サマのあのお顔は、とても印象的でございました」"

    "祖母の死と自分の死を確信した瞬間の、絶望という言葉では表現しきれない表情。"

    "パルカはその顔を見て、一体どんな気持ちを湧き立たせていたのか。"

    "きっとパルカですら、その気持ちの正体を知ることはない。"

    show dia sta fro cle big with std_change

    voice get_voice_filename("dia")
    parca "「さて、残る参加者はⅡ番サマ、Ⅲ番サマ、Ⅻ番サマ」"

    "彼女は微笑みながら、淡々と残った参加者を挙げる。"

    show dia sta fro glo big with std_change

    voice get_voice_filename("dia")
    parca "「一体どなたが脱落し、どなたが生き残るのでしょうか」"

    show dia sta fro gl1 big with std_change

    voice get_voice_filename("dia")
    parca "「どなたがワタクシの器になるのか、未だ予想がつきません」"

    show dia sta fro cl2 big with std_change

    voice get_voice_filename("dia")
    parca "「こうなってしまえば、もはやどなたサマでも同じですけれども」"

    show dia sta fro nor big with std_change

    voice get_voice_filename("dia")
    parca "「……あら？」"

    "パルカは首を傾げて、口にする。"

    show dia sta fro cl1 big with std_change

    voice get_voice_filename("dia")
    parca "「それは、どうしてでしたっけ？」"

    "こぼれた疑問に、返事は決して返ってこない。"

    "パルカは再び、≪女神の選定≫の管理者へと戻るのであった。"

    stop music fadeout 3
    scene black with Dissolve(3)
    pause 2

    $ renpy.end_replay()

    $ add_seen_chapter("9_4-2")

    call show_ending_image ("gui/BADEND_03.png")

    $ persistent.BAD03_clear = True
    $ grant_achievement("bad_end_03")
    $ grant_end_comp()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

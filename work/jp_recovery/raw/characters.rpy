

define d_kind = Character(name = None, show_two_window=True)


define narrator = Character(name = None, kind = d_kind, what_rest_indent = 0)


define rinka = Character(name = _("凛火"), kind = d_kind, image="rnk", voice_tag="rnk")
define rinka_num = Character(name = _("Ⅰの少女"),kind = rinka)
define rinka_unk1 = Character(name = _("黒髪の少女"),kind = rinka)


define miharu = Character(name = _("海晴"), kind = d_kind, image="mhr", voice_tag="mhr")
define miharu_num = Character(name = _("Ⅱの少女"),kind = miharu)
define miharu_unk1 = Character(name = _("聞き慣れた声"),kind = miharu)


define naomi = Character(name = _("直未"), kind = d_kind, image="nom", voice_tag="nom")
define naomi_unk1 = Character(name = _("？？？"), kind = naomi)
define naomi_unk2 = Character(name = _("聞き慣れた声Ｂ"), kind = naomi)


define mao = Character(name = _("真央"), kind = d_kind, image="mao", voice_tag="mao")
define mao_unk1 = Character(name = _("聞き慣れた声Ａ"), kind = mao)


define diana = Character(name = _("ダイアナ"), kind = d_kind, image="har", voice_tag="har")
define diana_unk1 = Character(name = _("？？？"), kind = diana)


define parca = Character(name = _("パルカ"), kind = d_kind, image="dia", voice_tag="dia")



define alan = Character(name = _("アラン"), kind = d_kind, image="aln", voice_tag="aln")
define alan_num = Character(name = _("Ⅻの男性"), kind = alan)
define alan_unk1 = Character(name = _("見知らぬ男性の声"), kind = alan)
define alan_unk2 = Character(name = _("謎の男性"), kind = alan)
define alan_unk3 = Character(name = _("？？？"), kind = alan)
define alan_unk4 = Character(name = _("聞き覚えのある男性の声"), kind = alan)
define alan_unk5 = Character(name = _("屈強な男性"), kind = alan)
define alan_staff = Character(name = _("スタッフ"), kind = alan)
define alan_scale = Character(name = _("スケール？"), kind = alan)


define odette = Character(name = _("オデット"), kind = d_kind, image="ode", voice_tag="ode")
define odette_num = Character(name = _("Ⅺの女性"), kind = odette)
define odette_unk1 = Character(name = _("？？？"), kind = odette)
define odette_unk2 = Character(name = _("聞き慣れた声"), kind = odette)
define odette_unk3 = Character(name = _("長身の女性"), kind = odette)


define federico = Character(name = _("フェデリーコ"), kind = d_kind, image="fed", voice_tag="fed")
define federico_num = Character(name = _("Ⅲの男性"), kind = federico)
define federico_unk1 = Character(name = _("聞き覚えのある声"), kind = federico)
define federico_unk2 = Character(name = _("外国人のお兄さん"), kind = federico)
define federico_unk3 = Character(name = _("長身の男性"), kind = federico)


define yuu = Character(name = _("ユウ"), kind = d_kind, image="yuu", voice_tag="yuu")
define yuu_unk1 = Character(name = _("少女？"), kind = yuu)
define yuu_unk2 = Character(name = _("少女"), kind = yuu)
define yuu_unk3 = Character(name = _("？？？"), kind = yuu)
define yuu_unk4 = Character(name = _("Ⅳの少女？"), kind = yuu)
define yuu_unk5 = Character(name = _("Ⅳの少年"), kind = yuu)
define yuu_unk6 = Character(name = _("少年"), kind = yuu)
define yuu_unk7 = Character(name = _("影のある少女"), kind = yuu)


define sonya = Character(name = _("ソーニャ"), kind = d_kind, image="son", voice_tag="son")
define sonya_unk1 = Character(name = _("謎の少女"), kind = sonya)
define sonya_unk2 = Character(name = _("明るい少女"), kind = sonya)


define keiko = Character(name = _("桂子"), kind = d_kind, image="kik", voice_tag="kik")
define keiko_num = Character(name = _("Ⅷの女性"), kind = keiko)
define keiko_unk1 = Character(name = _("謎の女性"), kind = keiko)
define keiko_unk2 = Character(name = _("聞き覚えのある声"), kind = keiko)
define keiko_unk3 = Character(name = _("子供を抱いた女性"), kind = keiko)


define scale = Character(name = _("スケール"), kind = d_kind, image="sca", voice_tag="sca")
define scale_num = Character(name = _("Ⅸの男性"), kind = scale)
define scale_unk1 = Character(name = _("見知らぬ男性"), kind = scale)
define scale_unk2 = Character(name = _("カメラを提げた男性"), kind = scale)
define scale_unk3 = Character(name = _("聞き覚えのある男性の声"), kind = scale)


define ushizuka = Character(name = _("茂継"), kind = d_kind, image="sgt", voice_tag="sgt")
define ushizuka_unk1 = Character(name = _("？？？"), kind = ushizuka)
define ushizuka_unk2 = Character(name = _("おじいさん"), kind = ushizuka)


define chan = Character(name = _("チャン"), kind = d_kind, image="cha", voice_tag="cha")
define chan_num = Character(name = _("Ⅵの女性"), kind = chan)
define chan_unk1 = Character(name = _("観光客の女性"), kind = chan)


define chanho = Character(name = _("昌鎬"), kind = d_kind, image="cnh", voice_tag="cnh")
define chanho_unk1 = Character(name = _("家族連れの男性"), kind = chanho)


define lete = Character(name = _("レテ"), kind = d_kind, image="let", voice_tag="let")
define lete_unk1 = Character(name = _("見知らぬ男性"), kind = lete)
define lete_cat = Character(name = _("レテ（猫）"), kind = lete)


define other_kind = Character(kind = d_kind, voice_tag="other")

define other_female_1 = Character(name = _("近所の主婦"), kind = other_kind)

define linda = Character(name = _("リンダ"), kind = other_kind)
define linda_unk1 = Character(name = _("？？？"), kind = linda)

define rinka_miharu = Character(name = _("凛火＆海晴"), kind = d_kind, voice_tag="other", what_rest_indent = 0)
define rinka_naomi = Character(name = _("凛火＆直未"), kind = d_kind, voice_tag="other", what_rest_indent = 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

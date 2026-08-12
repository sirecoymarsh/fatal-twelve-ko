




init -3 python:
    DELAY_FASTEST = 0.1
    DELAY_FAST = 0.2
    DELAY_NORMAL = 0.5
    DELAY_LONG = 1.0
    DELAY_LONGEST = 2.0

    renpy.const(DELAY_FASTEST)
    renpy.const(DELAY_FAST)
    renpy.const(DELAY_NORMAL)
    renpy.const(DELAY_LONG)
    renpy.const(DELAY_LONGEST)


define WIPE_EYESHUTTER = "images/rule/wipe_eyeshutter.png"
define WIPE_HORIZONTAL = "images/rule/wipe_horizontal.png"
define WIPE_VERTICAL = "images/rule/wipe_vertical.png"


define STD_YANCHOR = 0.95


define STD_CL_XALIGN = 0.2
define STD_CR_XALIGN = 0.8


define CI_L_XALIGN = 0.046
define CI_R_XALIGN = 0.946


define CAT_L_XALIGN = 0.25
define CAT_R_XALIGN = 0.85
define CAT_YALIGN = 0.4


define STD_SLIDE_OFFSET = 100


define BACK_S = 1.70158

define SCREEN_SIZE = (config.screen_width, config.screen_height)

define GIRLSTALK_DIR = "images/ecg/girlstalk/"
define FAMILYRES_DIR = "images/ecg/familyrestaurant/"
define NIGHTALK_DIR = "images/ecg/nighttalk/"
define RAINTALK_DIR = "images/ecg/raintalk/"

define CTC_ICON_ANIME_PAUSE = 0.8






define gameinfo_time = ""

define gameinfo_date = ""

define gameinfo_location = ""

define gameinfo_seen_chapters = ""

define gameinfo_owned_cards_rnk = ""
define gameinfo_owned_cards_mhr = ""
define gameinfo_owned_cards_nom = ""
define gameinfo_owned_cards_aln = ""
define gameinfo_owned_cards_ode = ""
define gameinfo_owned_cards_fed = ""
define gameinfo_owned_cards_yuu = ""
define gameinfo_owned_cards_son = ""
define gameinfo_owned_cards_kik = ""
define gameinfo_owned_cards_sca = ""
define gameinfo_owned_cards_sig = ""
define gameinfo_owned_cards_cha = ""
define gameinfo_owned_cards_cnh = ""



define gameflags_completed_once = False


define gameinfo_cardbook_rnk_unlocked = False
define gameinfo_cardbook_mhr_unlocked = False
define gameinfo_cardbook_nom_unlocked = False
define gameinfo_cardbook_aln_unlocked = False
define gameinfo_cardbook_ode_unlocked = False
define gameinfo_cardbook_fed_unlocked = False
define gameinfo_cardbook_yuu_unlocked = False
define gameinfo_cardbook_son_unlocked = False
define gameinfo_cardbook_kik_unlocked = False
define gameinfo_cardbook_sca_unlocked = False
define gameinfo_cardbook_sig_unlocked = False
define gameinfo_cardbook_cha_unlocked = False
define gameinfo_cardbook_cnh_unlocked = False


define voicecount_rnk = 0
define voicecount_mhr = 0
define voicecount_nom = 0
define voicecount_mao = 0
define voicecount_dia = 0
define voicecount_aln = 0
define voicecount_ode = 0
define voicecount_fed = 0
define voicecount_yuu = 0
define voicecount_son = 0
define voicecount_kik = 0
define voicecount_sca = 0
define voicecount_sgt = 0
define voicecount_cha = 0
define voicecount_cnh = 0
define voicecount_cat = 0
define voicecount_let = 0
define voicecount_har = 0
define voicecount_rnk_mhr = 0
define voicecount_rnk_nom = 0
define voicecount_other = 0

define flags_007_1_s1_counter_A = 0
define flags_007_1_s1_counter_B = 0

define flags_route_A = False
define flags_route_B = False
define flags_route_C = False
define flags_route_D = False
define flags_route_E = False
define flags_route_F = False
define flags_route_G = False
define flags_route_H = False

define flags_mhr_koukando = 0

init -3:

    define audio.title = "<loop 000.000 to 143.704>bgm_00"
    define audio.kinpaku = "<loop 000.577 to 067.038>bgm_01"
    define audio.nichijo01 = "<loop 008.478 to 091.957>bgm_02"
    define audio.myroom_night = "<loop 000.109 to 083.587>bgm_03"
    define audio.firedeath = "<loop 000.000 to 097.818>bgm_04"
    define audio.miharu = "<loop 000.167 to 181.500>bgm_05"
    define audio.amusementpark_noon = "<loop 014.130 to 104.565>bgm_06"
    define audio.gimon = "<loop 000.153 to 205.867>bgm_07"
    define audio.amusementpark_night = "<loop 000.000 to 132.706>bgm_08"
    define audio.maintheme = "<loop 000.000	 to 103.000>bgm_09"
    define audio.parca = "<loop 000.000 to 153.810>bgm_10"
    define audio.restlessness = "<loop 000.000 to 141.176>bgm_11"
    define audio.fatalhall = "<loop 000.000 to 102.857>bgm_12"
    define audio.myroom_melancholic_morning = "<loop 000.000 to 076.154>bgm_13"
    define audio.nichijo02 = "<loop 000.222 to 156.667>bgm_14"
    define audio.maidcafe = "<loop 000.802 to 118.053>bgm_15"
    define audio.growapart = "<loop 000.000 to 172.251>bgm_16"
    define audio.badguys = "<loop 000.323 to 082.903>bgm_17"
    define audio.investigation = "<loop 000.064 to 196.987>bgm_18"
    define audio.odette = "<loop 004.248 to 159.292>bgm_19"
    define audio.relaxforadult = "<loop 021.717 to 165.000>bgm_20"
    define audio.electing = "<loop 000.000 to 168.728>bgm_21"
    define audio.death = "<loop 000.000 to 087.904>bgm_22"
    define audio.thebonds = "<loop 016.538 to 115.000>bgm_23"
    define audio.impatience = "<loop 000.119 to 076.310>bgm_24"
    define audio.commit = "<loop 000.000 to 114.753>bgm_25"
    define audio.comicaldays = "<loop 000.000 to 112.500>bgm_26"
    define audio.disclose = "<loop 000.203 to 100.743>bgm_27"
    define audio.battle = "<loop 003.693 to 144.000>bgm_28"
    define audio.relaxtime = "<loop 000.000 to 189.311>bgm_29"
    define audio.memories = "<loop 000.000 to 145.634>bgm_30"
    define audio.nichijo04 = "<loop 007.276 to 121.903>bgm_31"
    define audio.despair = "<loop 000.000 to 132.777>bgm_32"
    define audio.rain = "<loop 000.000 to 133.305>bgm_33"
    define audio.rinka = "<loop 003.270 to 224.808>bgm_34"
    define audio.resistance = "<loop 000.000 to 168.164>bgm_35"
    define audio.shadowmiharu = "<loop 004.068 to 158.644>bgm_36"
    define audio.nichijo03 = "<loop 016.923 to 131.795>bgm_37"
    define audio.myroom_refreshing_morning = "<loop 000.123 to 126.025>bgm_38"
    define audio.naomi = "<loop 009.385 to 120.154>bgm_39"
    define audio.climaxtheme = "<loop 000.000 to 337.719>bgm_40"
    define audio.teaserforgame = "<loop 000.000 to 100.792>bgm_41"
    define audio.myroom_lastmorning = "<loop 000.000 to 170.596>bgm_42"
    define audio.alan = "<loop 015.230 to 199.846>bgm_43"


define game_menu_tips = {
    "save" : _("データをセーブ"),
    "load" : _("データをロード"),
    "settings" : _("環境設定を変更"),
    "story" : _("あらすじを読む"),
    "cardbook" : _("カードブックを調べる"),
    "title" : _("タイトルメニューへ戻る"),
    "close" : _("ゲームへ戻る"),
    "quit" : _("ゲームを終了"),
    }


init python:





    class NoRollbackObj(NoRollback):
        def __init__(self):
            self.rollback_color_set = False
            self.just_loaded = False
            self.voice_count_done = True
            self.last_loaded_slot = None

    no_rollback = NoRollbackObj()


init -2 python:

    if persistent.first_boot is None:        
        persistent.first_boot = True

    if persistent.message_alpha is None:
        persistent.message_alpha = config.message_alpha_default

    if persistent.text_cps_seen is None:
        persistent.text_cps_seen = config.text_cps_seen_default

    if persistent.text_cps_unseen is None:
        persistent.text_cps_unseen = config.text_cps_unseen_default


    if persistent.TRUE_clear is None:
        persistent.TRUE_clear = False

    if persistent.UNHAPPY_clear is None:
        persistent.UNHAPPY_clear = False

    if persistent.MIHARU_clear is None:
        persistent.MIHARU_clear = False

    if persistent.BAD01_clear is None:
        persistent.BAD01_clear = False

    if persistent.BAD02_clear is None:
        persistent.BAD02_clear = False

    if persistent.BAD03_clear is None:
        persistent.BAD03_clear = False

    if persistent.BAD04_clear is None:
        persistent.BAD04_clear = False



    if persistent.sentei1_clear is None:
        persistent.sentei1_clear = False

    if persistent.sentei2_clear is None:
        persistent.sentei2_clear = False

    if persistent.sentei3_clear is None:
        persistent.sentei3_clear = False

    if persistent.sentei4_clear is None:
        persistent.sentei4_clear = False

    if persistent.sentei5_clear is None:
        persistent.sentei5_clear = False

    if persistent.sentei6_clear is None:
        persistent.sentei6_clear = False

    if persistent.sentei7A_clear is None:
        persistent.sentei7A_clear = False

    if persistent.sentei7B_clear is None:
        persistent.sentei7B_clear = False

    if persistent.sentei8_clear is None:
        persistent.sentei8_clear = False

    if persistent.sentei9C_clear is None:
        persistent.sentei9C_clear = False

    if persistent.sentei9D_clear is None:
        persistent.sentei9D_clear = False

    if persistent.sentei10_clear is None:
        persistent.sentei10_clear = False

    if persistent.sentei11F_clear is None:
        persistent.sentei11F_clear = False

    if persistent.sentei11G_clear is None:
        persistent.sentei11G_clear = False

    if persistent.sentei11H_clear is None:
        persistent.sentei11H_clear = False

    if persistent.sentei12_clear is None:
        persistent.sentei12_clear = False    

    if persistent.seen_chapters is None:
        persistent.seen_chapters = {}


    if persistent.fed_botou_seen is None:
        persistent.fed_botou_seen = False


    if persistent.last_lang is None:
        persistent.last_lang = None

    if persistent.boot_times is None:
        persistent.boot_times = 0

    if persistent.s1_1_seen is None:
        persistent.s1_1_seen = False

    if persistent.s1_2_seen is None:
        persistent.s1_2_seen = False

    if persistent.s2_1_seen is None:
        persistent.s2_1_seen = False

    if persistent.s2_2_seen is None:
        persistent.s2_2_seen = False

    if persistent.s3_1_seen is None:
        persistent.s3_1_seen = False

    if persistent.s3_2_seen is None:
        persistent.s3_2_seen = False

    if persistent.s4_1_seen is None:
        persistent.s4_1_seen = False

    if persistent.s4_2_seen is None:
        persistent.s4_2_seen = False

    if persistent.s5_1_seen is None:
        persistent.s5_1_seen = False

    if persistent.s5_2_seen is None:
        persistent.s5_2_seen = False







    if persistent.s7_1_seen is None:
        persistent.s7_1_seen = False

    if persistent.s7_2_seen is None:
        persistent.s7_2_seen = False

    if persistent.s8_1_seen is None:
        persistent.s8_1_seen = False

    if persistent.s8_2_seen is None:
        persistent.s8_2_seen = False

    if persistent.s9_1_seen is None:
        persistent.s9_1_seen = False

    if persistent.s9_2_seen is None:
        persistent.s9_2_seen = False

    if persistent.s10_1_seen is None:
        persistent.s10_1_seen = False

    if persistent.s10_2_seen is None:
        persistent.s10_2_seen = False

    if persistent.s11_1_seen is None:
        persistent.s11_1_seen = False

    if persistent.s11_2_seen is None:
        persistent.s11_2_seen = False

    if persistent.s12_1_seen is None:
        persistent.s12_1_seen = False

    if persistent.s12_2_seen is None:
        persistent.s12_2_seen = False

    if persistent.s13_1_seen is None:
        persistent.s13_1_seen = False

    if persistent.s13_2_seen is None:
        persistent.s13_2_seen = False

    if persistent.s13_3_seen is None:
        persistent.s13_3_seen = False

    if persistent.s14_1_seen is None:
        persistent.s14_1_seen = False

    if persistent.s14_2_seen is None:
        persistent.s14_2_seen = False

    if persistent.s15_1_seen is None:
        persistent.s15_1_seen = False

    if persistent.s15_2_seen is None:
        persistent.s15_2_seen = False

    if persistent.s16_1_seen is None:
        persistent.s16_1_seen = False

    if persistent.s16_2_seen is None:
        persistent.s16_2_seen = False

    if persistent.s17_1_seen is None:
        persistent.s17_1_seen = False

    if persistent.s17_2_seen is None:
        persistent.s17_2_seen = False

    if persistent.s18_1_seen is None:
        persistent.s18_1_seen = False

    if persistent.s18_2_seen is None:
        persistent.s18_2_seen = False

    if persistent.s19_1_seen is None:
        persistent.s19_1_seen = False

    if persistent.s19_2_seen is None:
        persistent.s19_2_seen = False

    if persistent.s20_1_seen is None:
        persistent.s20_1_seen = False

    if persistent.s20_2_seen is None:
        persistent.s20_2_seen = False




init -2 python:


    def grant_achievement(s):
        
        if not config.is_steam:
            return
        
        if not achievement.has(s):
            achievement.grant(s)
            if config.developer:
                print("Granted achievement: " + s)

    def grant_end_comp():
        
        if not config.is_steam:
            return
        
        if (persistent.BAD01_clear and
            persistent.BAD02_clear and
            persistent.BAD03_clear and
            persistent.BAD04_clear and
            persistent.TRUE_clear and
            persistent.MIHARU_clear and
            persistent.UNHAPPY_clear):
            
            grant_achievement("end_comp")

    def grant_cg():
        
        if not config.is_steam:
            return
        
        seen = 0
        total = 0
        
        for k in gallery.buttons.keys():
            seen = seen + float(gallery.get_fraction(k, "{seen}"))
            total = total + float(gallery.get_fraction(k, "{total}"))
        
        gallery_ratio = int((seen/total) * 100)
        
        
        
        
        
        
        
        
        if gallery_ratio >= 100:
            grant_achievement("cg_comp")

    def grant_hear_all():
        
        if not config.is_steam:
            return
        
        if (persistent.s1_1_seen and
            persistent.s1_2_seen and
            persistent.s2_1_seen and
            persistent.s2_2_seen and
            persistent.s3_1_seen and
            persistent.s3_2_seen and
            persistent.s4_1_seen and
            persistent.s4_2_seen and
            persistent.s5_1_seen and
            persistent.s5_2_seen and
            
            
            persistent.s7_1_seen and
            persistent.s7_2_seen and
            persistent.s8_1_seen and
            persistent.s8_2_seen and
            persistent.s9_1_seen and
            persistent.s9_2_seen and
            persistent.s10_1_seen and
            persistent.s10_2_seen and
            persistent.s11_1_seen and
            persistent.s11_2_seen and
            persistent.s12_1_seen and
            persistent.s12_2_seen and
            persistent.s13_1_seen and
            persistent.s13_2_seen and
            persistent.s13_3_seen and
            persistent.s14_1_seen and
            persistent.s14_2_seen and
            persistent.s15_1_seen and
            persistent.s15_2_seen and
            persistent.s16_1_seen and
            persistent.s16_2_seen and
            persistent.s17_1_seen and
            persistent.s17_2_seen and
            persistent.s18_1_seen and
            persistent.s18_2_seen and
            persistent.s19_1_seen and
            persistent.s19_2_seen and
            persistent.s20_1_seen and
            persistent.s20_2_seen):
            
            grant_achievement("hear_all")



    def sort_story_buttons(key):
        
        split_key = key.split("_")
        
        split_key_len = len(split_key) 
        
        if split_key_len > 2 or split_key_len == 0:
            raise Exception("'" + key + "' is not a valid format for the chapter key.")
        
        elif split_key_len == 2:
            return int(split_key[0]) * 10 + int(split_key[1])
        
        else:
            return int(split_key[0]) * 10


    def on_exit_replay():
        renpy.suspend_rollback(False)

    game_menu_keymap = None
    hide_windows_keymap = None
    rollback_keymap = None
    skip_keymap = None
    toggle_skip_keymap = None



    def disable_keys():
        global game_menu_keymap
        global hide_windows_keymap
        global rollback_keymap
        global skip_keymap
        global toggle_skip_keymap
        
        game_menu_keymap = config.keymap['game_menu']
        hide_windows_keymap = config.keymap['hide_windows']
        rollback_keymap = config.keymap['rollback']
        skip_keymap = config.keymap['skip']
        toggle_skip_keymap = config.keymap['toggle_skip']
        
        config.keymap['game_menu'] = []
        config.keymap['hide_windows'] = []
        config.keymap['rollback'] = []
        config.keymap['skip'] = []
        config.keymap['toggle_skip'] = []
        
        renpy.clear_keymap_cache()



    def enable_keys():
        global game_menu_keymap
        global hide_windows_keymap
        global rollback_keymap
        global skip_keymap
        global toggle_skip_keymap
        
        config.keymap['game_menu'] = game_menu_keymap
        config.keymap['hide_windows'] = hide_windows_keymap
        config.keymap['rollback'] = rollback_keymap
        config.keymap['skip'] = skip_keymap
        config.keymap['toggle_skip'] = toggle_skip_keymap
        
        game_menu_keymap = None
        hide_windows_keymap = None
        rollback_keymap = None
        skip_keymap = None
        toggle_skip_keymap = None
        
        renpy.clear_keymap_cache()

    def after_loads():
        no_rollback.just_loaded = True
        no_rollback.voice_count_done = False
        renpy.run(Preference("auto-forward", "disable"))
        config.skipping = None

    def set_just_loaded():
        no_rollback.just_loaded = False





    def get_voice_filename(tag, startcount = None):
        
        
        
        
        str_var = "store.voicecount_" + tag
        
        if startcount:
            exec (str_var + "=" + str(startcount))
        
        else:
            if no_rollback.just_loaded and no_rollback.voice_count_done:
                pass
            
            else:
                exec (str_var + "+= 1")
                no_rollback.voice_count_done = True
        
        c_str = tag + "_" + str(eval(str_var)).zfill(5)
        
        return c_str








    def set_info_scene(scene_id):
        global save_name
        
        if scene_id in scenes:
            save_name = scenes[scene_id]
        else:
            raise ValueError("The scene id '{0}' is unknown.".format(scene_id))





    def set_info_time(time_id):
        global gameinfo_time
        
        if time_id in times:
            gameinfo_time = time_id
        else:
            raise ValueError("The time id '{0}' is unknown.".format(time_id))





    def set_info_location(location_id):
        global gameinfo_location
        
        if location_id in locations:
            gameinfo_location = location_id
        else:
            raise ValueError("The location id '{0}' is unknown.".format(location_id))







    def set_info_date(month, day, weekday):
        global gameinfo_date
        
        if (weekday != "mon" and 
            weekday != "tue" and 
            weekday != "wed" and 
            weekday != "thu" and 
            weekday != "fri" and
            weekday != "sat" and
            weekday != "sun" and
            weekday != "???"):
            raise ValueError("No such a weekday: {0}.".format(weekday))
        
        gameinfo_date = "{0}/{1} ({2})".format(str(month).zfill(2), str(day).zfill(2), weekday.upper())




    def show_hud():
        global gameinfo_date
        
        if config.skipping:
            if renpy.get_screen("hud"):
                renpy.hide_screen("hud")
            else:
                return
        
        if not renpy.get_screen("hud") and not renpy.in_rollback():
            renpy.show_screen("hud")






    def add_character_cards(character_tag, card_tags):
        
        
        
        str_var = "store.gameinfo_owned_cards_" + character_tag
        
        
        val_var = eval(str_var).split(",")
        
        for obj in card_tags:
            
            if obj not in cards:
                raise Exception("'" + obj + "' is not a valid card.")
            
            if obj in val_var:
                card_tags.remove(obj)
        
        
        if len(card_tags) != 0:
            
            exec (str_var + "+='" + ",".join(card_tags) + ",'")







    def remove_character_cards(character_tag, card_tags):
        str_var = "store.gameinfo_owned_cards_" + character_tag
        
        val_var = eval(str_var).split(",")
        
        for obj in card_tags:
            if obj in val_var:
                val_var.remove(obj)
        
        exec (str_var + "='" + ",".join(val_var) + "'")






    def add_seen_chapter(chapter_name):
        global gameinfo_seen_chapters
        
        if chapter_name not in plots:
            raise Exception("'" + chapter_name + "' is not a valid chapter.")
        
        if chapter_name not in gameinfo_seen_chapters.split(","):
            gameinfo_seen_chapters += chapter_name + ","
        
        
        
        chapter_name_split = chapter_name.split("-")
        key = chapter_name_split[0]
        value = chapter_name_split[1]
        
        if key not in persistent.seen_chapters:
            persistent.seen_chapters[key] = []
        
        if value not in persistent.seen_chapters[key]:
            persistent.seen_chapters[key].append(value)




    def get_time_icon():
        if gameinfo_time in times:
            return times[gameinfo_time]["icon"]
        else:
            return None

    def get_location_name():       
        if gameinfo_location in locations:  
            return locations[gameinfo_location]["name"]
        else:
            return ""

    def get_location_tip():       
        if gameinfo_location in locations:  
            return locations[gameinfo_location]["tip"]
        else:
            return ""


    def get_seen_chapters():
        global gameinfo_seen_chapters
        
        chapters_dic = {}
        chapters = gameinfo_seen_chapters.split(",")[:-1]
        
        for chapter in chapters:
            split_chapter = chapter.split("-")
            
            if split_chapter[0] not in chapters_dic:
                chapters_dic[split_chapter[0]] = []
            
            chapters_dic[split_chapter[0]].append(split_chapter[1])
        
        return chapters_dic        


    def get_character_cards(character_tag):
        return eval("store.gameinfo_owned_cards_" + character_tag).split(",")[:-1]



    def get_character_cards_count(character_tag):
        if character_tag:
            return len(get_character_cards(character_tag))
        else:
            return 0



    def get_current_bgm_title():
        
        now_playing = renpy.music.get_playing()
        
        if now_playing:
            now_playing = now_playing[-6:]
            if now_playing in bgm_titles:
                return bgm_titles[now_playing]
        
        return ""    


    def get_slotname(name, page=None):
        
        if page is None:
            page = persistent._file_page
        
        if config.linear_saves_page_size is not None:
            try:
                page = int(page)
                name = int(name)
                return str((page - 1) * config.linear_saves_page_size + name)
            except ValueError:
                pass
        
        return str(page) + "-" + str(name)



    def json_store(dic):
        
        dic["current_language"] = _preferences.language



    def set_message_color(color):
        style.say_dialogue.color = color
        style.say_thought.color = color
        style.ruby_text.color = color
        
        
        style.rebuild()



    def rollback_text_color_setter():
        
        if main_menu:
            return
        
        is_rollback = renpy.in_rollback()
        
        if (is_rollback and not no_rollback.rollback_color_set):
            no_rollback.rollback_color_set = True
            set_message_color(config.rollback_text_color)
        
        elif (not is_rollback and no_rollback.rollback_color_set):
            no_rollback.rollback_color_set = False
            set_message_color(config.default_text_color)



    def text_speed_setter():
        
        if main_menu:
            return
        
        is_seen = renpy.is_seen(True)
        
        if is_seen and _preferences.text_cps != persistent.text_cps_seen:
            renpy.run(Preference("text speed", persistent.text_cps_seen))
        
        elif not is_seen and _preferences.text_cps != persistent.text_cps_unseen:
            renpy.run(Preference("text speed", persistent.text_cps_unseen))

init -4:

    python:

        import math

        class Shaker(object):
            
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                
                self.start = [ self.anchors.get(i, i) for i in start ]  
                self.dist = dist    
                self.child = child
            
            def __call__(self, t, sizes):
                
                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                
                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, loop=False, **properties):
            
            move = Shaker(start, child, dist=dist)
            
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          repeat=loop,
                          **properties)

        Shake = renpy.curry(_Shake)




init -2 python:





    @renpy.pure
    class FileManipulation(Action):
        
        
        selected_filename = None
        
        def __init__(self, filenumber, mode, confirm=True):
            self.filename = get_slotname(filenumber)
            self.mode = mode
            self.confirm = confirm
        
        def __call__(self):
            if not FileManipulation.selected_filename:
                FileManipulation.selected_filename = self.filename
                
                renpy.restart_interaction()
            
            else:
                
                if FileManipulation.selected_filename == self.filename:
                    FileManipulation.selected_filename = None
                    
                    renpy.restart_interaction()
                
                elif self.mode == "copy":
                    
                    if self.confirm:
                        msg = renpy.can_load(self.filename) and _("セーブデータを上書きコピーしますか？") or _("セーブデータをコピーしますか？")
                        renpy.run(Confirm(msg, yes=self.copy, no=None))
                    else:
                        self.copy()
                
                elif self.mode == "move":
                    
                    if self.confirm:
                        renpy.run(Confirm(_("セーブデータを移しますか？"), yes=self.move, no=None))
                    else:
                        self.move()
        
        def copy(self):
            try:
                renpy.copy_save(FileManipulation.selected_filename, self.filename)
            except:
                pass
            
            finally:
                FileManipulation.selected_filename = None
        
        def move(self):
            try:
                
                if renpy.can_load(self.filename):
                    renpy.copy_save(FileManipulation.selected_filename, "temp_" + FileManipulation.selected_filename)
                    renpy.rename_save(self.filename, FileManipulation.selected_filename)
                    renpy.rename_save("temp_" + FileManipulation.selected_filename, self.filename)
                
                else:
                    renpy.copy_save(FileManipulation.selected_filename, "temp_" + FileManipulation.selected_filename)
                    renpy.unlink_save(FileManipulation.selected_filename)
                    renpy.rename_save("temp_" + FileManipulation.selected_filename, self.filename)
            
            except:
                pass
            
            finally:
                FileManipulation.selected_filename = None
        
        def get_sensitive(self):
            if FileManipulation.selected_filename:
                return True
            else:
                return renpy.can_load(self.filename)
        
        def get_selected(self):
            return FileManipulation.selected_filename == self.filename
        
        @staticmethod
        def is_selected():
            return bool(FileManipulation.selected_filename)
        
        @staticmethod
        def reset_selected():
            FileManipulation.selected_filename = None            



    @renpy.pure
    class SetPreferencesDefault(Action):        
        
        def __init__(self, page=None, confirm=True):
            self.page = page
            self.confirm = confirm
        
        def __call__(self):
            
            func = None
            msg = ""
            
            if self.page:
                
                if self.page == "system":
                    func = SetPreferencesDefault.set_system
                
                elif self.page == "sound":
                    func = SetPreferencesDefault.set_sound
                
                else:
                    raise Exception("'" + self.page + "' is not a valid value.")
                
                msg = _("このページの環境設定を初期化しますか？")
            
            else:
                func = SetPreferencesDefault.set_all
                msg = _("全ての環境設定を初期化しますか？")
            
            
            if self.confirm:
                renpy.run(Confirm(msg, yes=func, no=None))
            else:
                func()
        
        @staticmethod
        def set_system():
            
            if config.default_fullscreen:
                renpy.run(Preference("display", "fullscreen"))
            else:
                renpy.run(Preference("display", "window"))
            
            persistent.message_alpha = config.message_alpha_default
            
            persistent.text_cps_unseen = config.text_cps_unseen_default
            
            persistent.text_cps_seen = config.text_cps_seen_default
            
            renpy.run(Preference("auto-forward time", config.default_afm_time))
            
            renpy.run(Preference("skip", "seen"))
            
            if config.has_voice:
                renpy.run(Preference("wait for voice", "enable"))
        
        @staticmethod
        def set_sound():
            
            renpy.run(Preference("music volume", config.default_music_volume))
            
            renpy.run(Preference("mixer game_sfx volume", config.default_game_sfx_volume))
            
            renpy.run(Preference("sound volume", config.default_sfx_volume))
            
            if config.has_voice:
                renpy.run(Preference("voice mute", "disable"))
                
                renpy.run(Preference("voice volume", config.default_voice_volume))
                
                renpy.run(Preference("voice sustain", "disable"))
        
        @staticmethod
        def set_all():
            SetPreferencesDefault.set_system()
            SetPreferencesDefault.set_sound()




init -2 python:


    def do_with_override(self, trans, paired, clear=False):
        
        if renpy.config.with_callback:
            trans = renpy.config.with_callback(trans, paired)
        
        
        if config.is_steam:
            if "ecg" in renpy.get_showing_tags():
                grant_cg()
        
        
        
        
        
        for obj in config.no_wait_transitions:
            if trans and trans is obj:
                renpy.transition(trans, layer="master")
                return False
        
        
        if (not trans) or self.suppress_transition:
            self.with_none()
            return False
        else:
            self.set_transition(trans)
            return self.interact(trans_pause=True,
                                 suppress_overlay=not renpy.config.overlay_during_with,
                                 mouse='with',
                                 clear=clear)

    renpy.display.core.Interface.do_with = do_with_override



label _hide_windows_override:

    if renpy.context()._menu:
        return

    if _windows_hidden:
        return

    python:
        _windows_hidden = True

        config.skipping = None
        renpy.run(Preference("auto-forward", "disable"))
        renpy.context_dynamic("_last_voice_play")
        renpy.transition(Dissolve(0.2))

        ui.saybehavior(dismiss=['dismiss', 'hide_windows', 'game_menu', 'rollback', 'rollforward', 'toggle_skip', 'skip'])
        ui.interact(suppress_overlay=True, suppress_window=True)


        renpy.transition(Dissolve(0.2))

        _windows_hidden = False

    return




init -3 python:




    def linear(t):
        return t    

    def ease(t):
        import math
        return 0.5 - math.cos(math.pi * t) / 2.0

    def easein(t):
        import math
        return math.cos((1.0 - t) * math.pi / 2.0)

    def easeout(t):
        import math
        return 1.0 - math.cos(t * math.pi / 2.0)

    def easeinback(t):
        return t * t *((BACK_S + 1) * t - BACK_S)

    def easeoutback(t):
        t -= 1
        return t * t * ((BACK_S + 1) * t + BACK_S) + 1





    def DissolveMoveIn(time, transform=None, time_warp=None):
        return ComposeTransition(
            Dissolve(time, time_warp=time_warp),
            after=MoveTransition(time, enter=transform, enter_time_warp=time_warp))




    def DissolveMoveOut(time, transform=None, time_warp=None):
        return ComposeTransition(
            Dissolve(time, time_warp=time_warp),
            before=MoveTransition(time, leave=transform, leave_time_warp=time_warp))


    def WipeTransition(image, time, ramplen=5, reverse=False, alpha=True, time_warp=None):
        return ImageDissolve(image, time, ramplen=2**ramplen, reverse=reverse, alpha=alpha, time_warp=time_warp)






    def ComposedTransition(transition1, transition2=None, inbetween_color="#000", inbetween_time=DELAY_NORMAL):
        inbetween_image = Solid(color=inbetween_color)
        return MultipleTransition([False,
            transition1, inbetween_image,
            Pause(inbetween_time),
            inbetween_image, transition2 and transition2 or transition1,
            True])





translate english python:

    style.window.left_padding = 150
    style.window.right_padding = 150

    style.say_who_window.xminimum = 300

    style.choice_text.size = 26

    style.say_label.size = 22

    style.say_dialogue.rest_indent = 11
    style.say_dialogue.kerning = 1
    style.say_dialogue.line_spacing = 2

    style.info_panel_text.size = 14
    style.info_panel_text.line_spacing = 0

    style.cardbook_button_text.size = 13

    style.home_link.pos = (981, 590)

    style.chapter_name_label_text.size = 40

    style.game_menu_chaptername_vbox.align = (0.2, 0.09)

    style.game_menu_chaptername_text.size = 44


translate None strings:

    old "Quick save complete."
    new "クイックセーブ完了"

    old "Are you sure you want to delete this save?"
    new "セーブデータ削除しますか?"

    old "Are you sure you want to overwrite your save?"
    new "セーブデータを上書きしますか？"

    old "Loading will lose unsaved progress.\nAre you sure you want to do this?"
    new "セーブデータロードしますか？"

    old "Are you sure you want to quit?"
    new "ゲームを終了しますか？"

    old "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
    new "タイトル画面に戻りますか？"

    old "Image [index] of [count] locked."
    new "画像 [index] / [count] はロックされています。"

    old "Saved screenshot as %s."
    new "スクリーンショットを %s に保存しました"

translate english strings:




    old "Are you sure you want to delete this save?"
    new "Delete this save?"

    old "Are you sure you want to overwrite your save?"
    new "Overwrite this save?"

    old "Loading will lose unsaved progress.\nAre you sure you want to do this?"
    new "Load this save?"

    old "Are you sure you want to quit?"
    new "Quit the game?"

    old "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
    new "Go back to title?"










init python:

    gallery = Gallery()
    gallery.transition = Dissolve(0.3)



    gallery.button("01")
    gallery.unlock_image("ecg coffee sip")
    gallery.unlock_image("ecg coffee ole")  

    gallery.button("02")
    gallery.unlock_image("ecg miharu nor")

    gallery.button("03")
    gallery.unlock_image("ecg amusement01 smi")
    gallery.unlock_image("ecg amusement01 sad")
    gallery.unlock_image("ecg amusement01 se1")
    gallery.unlock_image("ecg amusement01 se2")

    gallery.button("04")
    gallery.unlock_image("ecg amusement02 sur")
    gallery.unlock_image("ecg amusement02 smi")

    gallery.button("05")
    gallery.unlock_image("ecg parcawalk nor")

    gallery.button("06")
    gallery.unlock_image("ecg cardapp nor")



    gallery.button("07")
    gallery.unlock_image("ecg maidcafe nor")

    gallery.button("08")
    gallery.unlock_image("ecg miharumaid nor")
    gallery.unlock_image("ecg miharumaid shy")
    gallery.unlock_image("ecg miharumaid mag")
    gallery.unlock_image("ecg miharumaid dis")
    gallery.unlock_image("ecg miharumaid bit")

    gallery.button("09")
    gallery.unlock_image("ecg chinarest odetto nor")
    gallery.unlock_image("ecg chinarest odetto ama")
    gallery.unlock_image("ecg chinarest odetto kno")    
    gallery.unlock_image("ecg chinarest odetto lau")
    gallery.unlock_image("ecg chinarest odetto ser")    
    gallery.unlock_image("ecg chinarest odetto smi")

    gallery.button("10")
    gallery.unlock_image("ecg chinarest federico nor")
    gallery.image("ecg chinarest federico boutou")
    gallery.condition("persistent.fed_botou_seen")
    gallery.unlock_image("ecg chinarest federico ama")
    gallery.unlock_image("ecg chinarest federico ave")
    gallery.unlock_image("ecg chinarest federico ser")

    gallery.button("11")
    gallery.unlock_image("ecg odettobt fun")
    gallery.unlock_image("ecg odettobt ser")
    gallery.unlock_image("ecg odettobt mad") 

    gallery.button("12")
    gallery.unlock_image("ecg parcadeclaration")



    gallery.button("13")
    gallery.unlock_image("ecg senteiodetto nor")
    gallery.unlock_image("ecg senteiodetto bor") 
    gallery.unlock_image("ecg senteiodetto dow") 
    gallery.unlock_image("ecg senteiodetto reb")
    gallery.unlock_image("ecg senteiodetto smi")

    gallery.button("14")
    gallery.unlock_image("ecg naomidetermination ser")
    gallery.unlock_image("ecg naomidetermination cry")

    gallery.button("15")
    gallery.unlock_image("ecg keikospeak")

    gallery.button("16")
    gallery.unlock_image("ecg senteialan nor")

    gallery.button("17")
    gallery.unlock_image("ecg pasajiru nor")
    gallery.unlock_image("ecg pasajiru pai")

    gallery.button("18")
    gallery.unlock_image("ecg sophiatear lau")
    gallery.unlock_image("ecg sophiatear pai")
    gallery.unlock_image("ecg sophiatear cry")
    gallery.unlock_image("ecg sophiatear cla")

    gallery.button("19")
    gallery.unlock_image("ecg senteimiharu gen")
    gallery.unlock_image("ecg senteimiharu bea")
    gallery.unlock_image("ecg senteimiharu ser")



    gallery.button("20")
    gallery.unlock_image("ecg rinkasento smi")
    gallery.unlock_image("ecg rinkasento lon")
    gallery.unlock_image("ecg rinkasento rel")

    gallery.button("21")
    gallery.unlock_image("ecg rinyuucooking a")
    gallery.unlock_image("ecg rinyuucooking b")
    gallery.unlock_image("ecg rinyuucooking c")
    gallery.unlock_image("ecg rinyuucooking d")
    gallery.unlock_image("ecg rinyuucooking e")

    gallery.button("22")
    gallery.unlock_image("ecg alanbt gla")
    gallery.unlock_image("ecg alanbt tre")

    gallery.button("23")
    gallery.unlock_image("ecg nomdeath")

    gallery.button("24")
    gallery.unlock_image("ecg yuufire obscurity")
    gallery.unlock_image("ecg yuufire sad")



    gallery.button("25")
    gallery.unlock_image("ecg funeral")
    gallery.unlock_image("ecg funeral tear")

    gallery.button("26")
    gallery.unlock_image("ecg barodefed a")
    gallery.unlock_image("ecg barodefed b")
    gallery.unlock_image("ecg barodefed c")
    gallery.unlock_image("ecg barodefed d")
    gallery.unlock_image("ecg barodefed e")
    gallery.unlock_image("ecg barodefed f")

    gallery.button("27")
    gallery.unlock_image("ecg rinkaresurrection a")
    gallery.unlock_image("ecg rinkaresurrection b")

    gallery.button("28")
    gallery.unlock_image("ecg hostage normal")
    gallery.unlock_image("ecg hostage broadcast")

    gallery.button("29")
    gallery.unlock_image("ecg claimerrinka henso")
    gallery.unlock_image("ecg claimerrinka normal")
    gallery.unlock_image("ecg claimerrinka nor2")

    gallery.button("30")
    gallery.unlock_image("ecg alanspeak normal")
    gallery.unlock_image("ecg alanspeak far")



    gallery.button("31")
    gallery.unlock_image("ecg rinyuufaceto b")
    gallery.unlock_image("ecg rinyuufaceto c")
    gallery.unlock_image("ecg rinyuufaceto d")
    gallery.unlock_image("ecg rinyuufaceto f")
    gallery.unlock_image("ecg rinyuufaceto g")
    gallery.unlock_image("ecg rinyuufaceto h")
    gallery.unlock_image("ecg rinyuufaceto i")

    gallery.button("32")
    gallery.unlock_image("ecg yuuburn")
    gallery.unlock_image("ecg yuuburn non")

    gallery.button("33")
    gallery.unlock_image("ecg senteirinka gentle")
    gallery.unlock_image("ecg senteirinka serious")
    gallery.unlock_image("ecg senteirinka receive")

    gallery.button("34")
    gallery.unlock_image("ecg rinkahug")

    gallery.button("35")
    gallery.unlock_image("ecg odettopast")

    gallery.button("36")
    gallery.unlock_image("ecg odettomiharupark a")
    gallery.unlock_image("ecg odettomiharupark b")
    gallery.unlock_image("ecg odettomiharupark c")
    gallery.unlock_image("ecg odettomiharupark d")
    gallery.unlock_image("ecg odettomiharupark e")



    gallery.button("37")
    gallery.unlock_image("ecg amrita hid")
    gallery.unlock_image("ecg amrita normal")

    gallery.button("38")
    gallery.unlock_image("ecg miharukokuhaku panic")
    gallery.unlock_image("ecg miharukokuhaku serious")
    gallery.unlock_image("ecg miharukokuhaku shy")

    gallery.button("39")
    gallery.unlock_image("ecg rinkaawate normal")
    gallery.unlock_image("ecg rinkaawate panic")

    gallery.button("40")
    gallery.unlock_image("ecg alantalk normal")
    gallery.unlock_image("ecg alantalk smile")
    gallery.unlock_image("ecg alantalk close")

    gallery.button("41")
    gallery.unlock_image("ecg miharupasttalk lie")
    gallery.unlock_image("ecg miharupasttalk sad")
    gallery.unlock_image("ecg miharupasttalk serious")
    gallery.unlock_image("ecg miharupasttalk shy")

    gallery.button("42")
    gallery.unlock_image("ecg dianapicture normal") 



    gallery.button("43")
    gallery.unlock_image("ecg maocomic normal")

    gallery.button("44")
    gallery.unlock_image("ecg miharubye normal")
    gallery.unlock_image("ecg miharubye serious")
    gallery.unlock_image("ecg miharubye light")

    gallery.button("45")
    gallery.unlock_image("ecg mindbattle normal")
    gallery.unlock_image("ecg mindbattle light")
    gallery.unlock_image("ecg mindbattle hand")
    gallery.unlock_image("ecg mindbattle climax")

    gallery.button("46")
    gallery.unlock_image("ecg falllete fall")
    gallery.unlock_image("ecg falllete die")

    gallery.button("47")
    gallery.unlock_image("ecg dianafire normal")
    gallery.unlock_image("ecg dianafire lete")

    gallery.button("48")
    gallery.unlock_image("ecg parcaindiana general")
    gallery.unlock_image("ecg parcaindiana close")



    gallery.button("49")
    gallery.unlock_image("ecg parcafire alone")
    gallery.unlock_image("ecg parcafire rinka")

    gallery.button("50")
    gallery.unlock_image("ecg komorebi normal")

    gallery.button("51")
    gallery.unlock_image("ecg maoandfed normal")

    gallery.button("52")
    gallery.unlock_image("ecg miharuend normal")

    gallery.button("53")
    gallery.unlock_image("ecg unhappyend01 normal")

    gallery.button("54")
    gallery.unlock_image("ecg trueend01 dark")
    gallery.unlock_image("ecg trueend01 light")

    gallery.button("55")
    gallery.unlock_image("ecg trueend02 normal")



    gallery.button("56")
    gallery.unlock_image("ecg trueend03 normal")







init python hide:


    if persistent.first_boot:        
        persistent.first_boot = False 
        
        renpy.run(SetPreferencesDefault)
        
        persistent.last_lang = _preferences.language




    grant_achievement("game_start")


    if persistent.last_lang != _preferences.language:
        grant_achievement("change_language")
    persistent.last_lang = _preferences.language


    if persistent.boot_times < 11:
        persistent.boot_times += 1
    else:
        grant_achievement("twelve_times_start")













label set_replay():

    $ renpy.suspend_rollback(_in_replay)
    window auto

    return

label show_ending_image(dis, stop_music=False):


    $ config.skipping = None


    $ disable_keys()

    scene expression dis
    $ renpy.transition(Dissolve(3))
    $ renpy.pause(5, hard = True)

    if stop_music:
        stop music fadeout 3

    scene black
    $ renpy.transition(Dissolve(3))
    $ renpy.pause(5, hard = True)


    $ enable_keys()

    return


label staffroll(movie):

    stop music fadeout 2
    scene black with Dissolve(3)
    pause 3


    $ config.skipping = None


    $ disable_keys()

    $ renpy.movie_cutscene("movies/" + movie)
    pause 2


    $ enable_keys()

    return


label trial_end:


    $ config.skipping = None


    $ disable_keys()

    scene black
    show expression Text("to be continued...", size=50, font="gui/fonts/CharisSILR.ttf") at align(0.95, 0.95)
    $ renpy.transition(Dissolve(3))
    $ renpy.pause(5, hard = True)

    show screen demo_last
    $ renpy.transition(fade)
    $ renpy.pause(6, hard = True)

    scene black
    hide screen demo_last
    $ renpy.transition(Dissolve(3))
    $ renpy.pause(8, hard = True)


    $ enable_keys()

    return

label splashscreen:

    if not config.developer:
        $ disable_keys()
        $ renpy.pause(1, hard = True)
        scene sp_logo_movie
        $ renpy.pause(5, hard = True)
        hide sp_logo_movie
        $ renpy.pause(3, hard = True)
        scene splash_circle_logo
        $ renpy.transition(Dissolve(2))
        $ renpy.pause(5, hard = True)
        scene black
        $ renpy.transition(Dissolve(2))
        $ renpy.pause(5, hard = True)

        $ enable_keys()
    return


label before_start:

    stop music fadeout 2.0
    scene black
    hide screen main_menu
    $ renpy.transition(Dissolve(2))
    $ renpy.pause(5, hard = True)


    $ renpy.run(Start())



label start:

    if config.developer:
        jump test

label start.initialization:

    window auto    

    if persistent.TRUE_clear or persistent.UNHAPPY_clear or persistent.MIHARU_clear:
        jump fNG_plus
    else:
        jump f001

label test:

    jump start.initialization
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

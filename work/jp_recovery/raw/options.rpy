








init -1 python hide:



    config.screen_width = 1280
    config.screen_height = 720




    config.window_title = u"FATAL TWELVE"



    config.name = "FATAL TWELVE"
    config.version = "180420"

    config.developer = False










    theme.diamond(
        
        

        
        widget = "#BF7C51",

        
        widget_hover = "#dda570",

        
        widget_text = "#E5DFDF",

        
        
        widget_selected = "#ffffff",

        
        disabled = "#ab6038",

        
        disabled_text = "#BF7C51",

        
        label = "#ffffff",

        
        frame = "#49271b",

        
        
        
        mm_root = "#2a201f",

        
        
        
        gm_root = "#2a201f",

        
        
        rounded_window = False,

        
        
        
        )








    config.has_sound = True



    config.has_music = True



    config.has_voice = True








    config.enter_sound = "blip-pop"
    config.exit_sound = "blip-pop"







    config.main_menu_music = audio.title












    config.help = None






    config.enter_transition = Dissolve(.3)


    config.exit_transition = Dissolve(.3)


    config.intra_transition = Dissolve(.2)


    config.main_game_transition = None


    config.game_main_transition = ComposedTransition(Dissolve(2.0))


    config.end_splash_transition = Dissolve(2)


    config.end_game_transition = ComposedTransition(Dissolve(2.0))


    config.after_load_transition = ComposedTransition(Dissolve(2.0))


    config.window_show_transition = Dissolve(.2)


    config.window_hide_transition = config.window_show_transition


    config.adv_nvl_transition = dissolve


    config.nvl_adv_transition = dissolve


    config.enter_yesno_transition = None


    config.exit_yesno_transition = None


    config.enter_replay_transition = ComposedTransition(Dissolve(2.0))


    config.exit_replay_transition = ComposedTransition(Dissolve(2.0))


    config.say_attribute_transition = None





python early:
    config.save_directory = "FATAL TWELVE"


init -1 python hide:









    config.default_fullscreen = False



    config.default_afm_time = 10





    config.has_autosave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False

    config.joystick = False


    config.quicksave_slots = 10

    config.quit_action = None



    config.keymap['dismiss'].append('mousedown_5')
    config.keymap['self_voicing'] = []
    config.keymap['help'] = []

    if not config.developer:
        config.keymap['screenshot'] = []

    config.gl_resize = False

    config.thumbnail_width = 257
    config.thumbnail_height = 144

    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    config.start_interact_callbacks.append(rollback_text_color_setter)
    config.start_interact_callbacks.append(text_speed_setter)

    config.after_load_callbacks.append(after_loads)
    config.interact_callbacks.append(set_just_loaded)

    config.after_replay_callback = on_exit_replay

    config.save_json_callbacks.append(json_store)

    config.label_overrides = {"_hide_windows" : "_hide_windows_override"}

    config.history_length = 0

    config.rollback_length = 20

    config.skip_indicator = False





    config.window_icon = "gui/icon_lin-osx.png"

    config.windows_icon = "gui/icon_win.png"

init -2 python:


    config.locked = False


    config.is_trial = False

    config.is_steam = True

    config.lock_extra = False

    config.lock_cardbook = False

    config.lock_story = False

    config.message_alpha_default = 1.0

    config.rollback_text_color = Color("#de792e")
    config.default_text_color = Color("#FFF")

    config.text_cps_unseen_default = 40

    config.text_cps_seen_default = 180


    config.default_game_sfx_volume = 0.5












    config.no_wait_transitions = [std_change, ecg_change, ci_change]


    config.ctc_align = (0.97, 0.96)

    config.auto_icon_align = (0.98, 0.02)

    config.skip_icon_align = config.auto_icon_align

    config.menu_navigation_align = (0.9715, 0.98)


    config.locked = True



    config.fade_music = 1.0



    config.default_music_volume = 0.50

    config.default_sfx_volume = 0.50    

    config.default_voice_volume = 1.0



    renpy.music.register_channel("music", mixer="music", loop = True, file_prefix="sounds/bgm/", file_suffix=".ogg")

    renpy.music.register_channel("audio", mixer="sfx", loop = False, file_prefix="sounds/sfx/", file_suffix=".ogg")
    renpy.music.register_channel("sound", mixer="sfx", loop = False, file_prefix="sounds/sfx/", file_suffix=".ogg")

    renpy.music.register_channel("se", mixer="game_sfx", loop = False, file_prefix="sounds/sfx/", file_suffix=".ogg")
    renpy.music.register_channel("ambient", mixer="game_sfx", loop=True, file_prefix="sounds/sfx/", file_suffix=".ogg", tight=True)

    renpy.music.register_channel("voice", mixer="voice", loop = False, file_prefix="sounds/voice/", file_suffix=".ogg")

    config.sample_sound = "sounds/test/se_button01"



init python:


    _game_menu_screen = "game_menu"

    config.replay_scope = { "_game_menu_screen" : "game_menu" }


    _history = False




init python:




    build.directory_name = "FATAL_TWELVE"




    build.executable_name = "fatal"



    build.include_update = False


    build.archive("system", "all")
    build.archive("scenario", "all")
    build.archive("images", "all")
    build.archive("sounds", "all")
    build.archive("movies", "all")
    build.archive("tl", 'all')





























    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify("game/**.rpy", None)


    build.classify("game/localize.rpyc", None)

    build.classify("game/_private/**", None)


    if config.is_trial:
        
        
        
        build.classify("game/scenario/003.rpyc", None)
        build.classify("game/scenario/004.rpyc", None)
        build.classify("game/scenario/005_1.rpyc", None)
        build.classify("game/scenario/005_2.rpyc", None)
        build.classify("game/scenario/006.rpyc", None)
        build.classify("game/scenario/007_1.rpyc", None)
        build.classify("game/scenario/007_2.rpyc", None)
        build.classify("game/scenario/009.rpyc", None)
        build.classify("game/scenario/010.rpyc", None)
        build.classify("game/scenario/011_01.rpyc", None)
        build.classify("game/scenario/011_01F.rpyc", None)
        build.classify("game/scenario/011_01G.rpyc", None)
        build.classify("game/scenario/011_01_H.rpyc", None)
        build.classify("game/scenario/011_02.rpyc", None)
        build.classify("game/scenario/012_01F.rpyc", None)
        build.classify("game/scenario/0012_01GH.rpyc", None)
        build.classify("game/scenario/012_02.rpyc", None)
        build.classify("game/scenario/BAD_END_01.rpyc", None)
        build.classify("game/scenario/BAD_END_02.rpyc", None)
        build.classify("game/scenario/BAD_END_03.rpyc", None)
        build.classify("game/scenario/NG_plus.rpyc", None)
        build.classify("game/scenario/TRUE_END.rpyc", None)
        build.classify("game/scenario/UNHAPPY_END.rpyc", None)
        
        build.classify("game/tl/english/scenario/003.rpyc", None)
        build.classify("game/tl/english/scenario/004.rpyc", None)
        build.classify("game/tl/english/scenario/005_1.rpyc", None)
        build.classify("game/tl/english/scenario/005_2.rpyc", None)
        build.classify("game/tl/english/scenario/006.rpyc", None)
        build.classify("game/tl/english/scenario/007_1.rpyc", None)
        build.classify("game/tl/english/scenario/007_2.rpyc", None)
        build.classify("game/tl/english/scenario/009.rpyc", None)
        build.classify("game/tl/english/scenario/010.rpyc", None)
        build.classify("game/tl/english/scenario/011_01.rpyc", None)
        build.classify("game/tl/english/scenario/011_01F.rpyc", None)
        build.classify("game/tl/english/scenario/011_01G.rpyc", None)
        build.classify("game/tl/english/scenario/011_01_H.rpyc", None)
        build.classify("game/tl/english/scenario/011_02.rpyc", None)
        build.classify("game/tl/english/scenario/012_01F.rpyc", None)
        build.classify("game/tl/english/scenario/0012_01GH.rpyc", None)
        build.classify("game/tl/english/scenario/012_02.rpyc", None)
        build.classify("game/tl/english/scenario/BAD_END_01.rpyc", None)
        build.classify("game/tl/english/scenario/BAD_END_02.rpyc", None)
        build.classify("game/tl/english/scenario/BAD_END_03.rpyc", None)
        build.classify("game/tl/english/scenario/NG_plus.rpyc", None)
        build.classify("game/tl/english/scenario/TRUE_END.rpyc", None)
        build.classify("game/tl/english/scenario/UNHAPPY_END.rpyc", None)
        
        build.classify("game/movies/ED_BAD.mkv", None)
        build.classify("game/movies/ED_MHR_UNH.mkv", None)
        build.classify("game/movies/ED_TRUE.mkv", None)






    build.classify("game/*.rpyc", 'system')
    build.classify("game/gui/**", 'system')
    build.classify("game/scenario/**", 'scenario')
    build.classify("game/images/**", 'images')
    build.classify("game/sounds/**", 'sounds')
    build.classify("game/movies/**", 'movies')
    build.classify("game/tl/**", 'tl')  





    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

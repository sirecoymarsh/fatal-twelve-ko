











screen say(who, what, side_image=None, two_window=False):


    if not two_window:


        window:
            id "window"

            has vbox
            style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        window:
            style_prefix "say"
            id "window"

            has vbox

            fixed:
                ysize 34

                if who:
                    window:
                        style "say_who_window"

                        text who:
                            id "who"

            text what id "what"


    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


    use quick_menu

    if renpy.in_rollback():

        key "mousedown_5" action RollForward()







screen choice(items):

    $ transform_delay = 0.0
    $ in_rollback = renpy.in_rollback()

    vbox:
        style_prefix "choice"
        spacing 15
        xalign 0.5
        yalign 0.4

        for caption, action, chosen in items:
            if action:
                button at not in_rollback and choice_show(transform_delay) or None:
                    action action
                    text caption style "choice_text"


                $ transform_delay += 0.1

            else:
                text caption style "choice_caption"



init -2:
    $ config.narrator_menu = True

    style choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)

        idle_background Frame("gui/button01_idle.png", 30, 30)
        hover_background Frame("gui/button01_hover.png", 30, 30)
        selected_background Frame("gui/button01_selected.png", 30, 30)
        insensitive_background Frame("gui/button01_insensitive.png", 30, 30)

        activate_sound None

    style choice_text is button_text clear:

        size 28









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox
                spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu







screen main_menu():
    tag menu


    style_prefix "main_menu"

    python:

        newest_slot = renpy.newest_slot()
        if newest_slot:
            newest_slot = newest_slot.split("-")


    add "title_art"

    frame:
        pos (865, 460)

        has vbox
        spacing 14

        textbutton _("START") action Jump("before_start")
        textbutton _("CONTINUE"):
            if newest_slot:
                action [SetField(no_rollback, "last_loaded_slot", newest_slot),
                        FileLoad(newest_slot[1], confirm=False, page=newest_slot[0], newest=False)]
            else:
                action SensitiveIf(False)
        textbutton _("LOAD") action ShowMenu("file_manager")
        textbutton _("SETTINGS") action ShowMenu("preferences")
        textbutton _("EXTRA") action [ShowMenu("extra"),
                                        SensitiveIf(not config.is_trial and
                                            not config.lock_extra and
                                            persistent.TRUE_clear or persistent.UNHAPPY_clear or persistent.MIHARU_clear)]
        textbutton _("QUIT") action Quit(confirm=False)

init -2:

    style main_menu_frame:
        background None

    style main_menu_button is menu_button:
        xysize (196, 24)
        background None
        hover_background "gui/title_button_bg_hover.png"
        hover_sound "basic-click-wooden"

    style main_menu_button_text is menu_button_text:
        font "gui/fonts/NotoSansCJKjp-Thin.otf"
        size 20




screen menu_navigation(alignment):

    style_prefix "menu_navigation"

    frame:
        align alignment
        background None

        if not main_menu:
            hbox:
                spacing 10


                textbutton _("close") action Return()
        else:
            textbutton _("back") action Return()


    key "game_menu" action Return()

init -2:

    style menu_navigation_button is menu_button:
        xsize 130
        ysize 30
        selected_background Frame("gui/button01_idle.png", 4, 4)

    style menu_navigation_button_text is menu_button_text:
        size 16




screen reset_default_navigation(page, alignment):

    style_prefix "menu_navigation"

    frame:
        align alignment
        background None

        has hbox
        spacing 10

        textbutton _("reset page") action SetPreferencesDefault(page)

        textbutton _("reset all") action SetPreferencesDefault()




screen menu_page_title(title, alignment):

    style_prefix "menu_page_title"

    frame:
        align alignment
        background "gui/headline_bg.png"
        xysize (312, 122)
        right_padding 20

        label title:
            align (0.6, 0.5)

init -2:

    style menu_page_title_label_text is text:
        font "gui/fonts/ipaexm.ttf"
        size 34




screen file_manager(mode="load"):
    tag menu


    default current_mode = mode

    $ current_page = str(FileCurrentPage())
    $ page_number = 10


    if main_menu:
        add "title_art"

    add "gui/right_click_bg.png"


    use menu_page_title(_("データ管理"), (1.0, 0.00))


    frame:
        style_prefix "file_manager_mode"

        has hbox

        textbutton _("セーブ"):
            action [SetScreenVariable("current_mode", "save"),
                    Function(FileManipulation.reset_selected),
                    SensitiveIf(current_mode != "save" and not main_menu)]


        textbutton _("ロード"):
            action [SetScreenVariable("current_mode", "load"),
                    Function(FileManipulation.reset_selected),
                    SensitiveIf(current_mode != "load")]

        textbutton _("移動"):
            action [SetScreenVariable("current_mode", "move"),
                    Function(FileManipulation.reset_selected),
                    SensitiveIf(current_mode != "move")]


        textbutton _("コピー"):
            action [SetScreenVariable("current_mode", "copy"),
                    Function(FileManipulation.reset_selected),
                    SensitiveIf(current_mode != "copy")]


        textbutton _("削除"):
            action [SetScreenVariable("current_mode", "delete"),
                    Function(FileManipulation.reset_selected),
                    SensitiveIf(current_mode != "delete")]


    frame:
        background "gui/layout_saves.png"
        xysize (1200, 560)
        align (0.5, 0.615)
        xpadding 20
        ypadding 11

        has vbox
        spacing 12

        hbox:
            style_prefix "file_manager_nav"
            xalign 0.5

            textbutton _("クイックセーブ"):
                action [FilePage("quick"),
                            SensitiveIf(current_page != "quick")] style "file_manager_nav_quicksave_button"

            for i in range (1, (page_number + 1)):

                $ current_index = str(i)

                textbutton current_index:
                    action [FilePage(i),
                            SensitiveIf(current_page != current_index)]


        $ columns = 4
        $ rows = 2

        grid columns rows:
            style_prefix "file_manager_slots"

            spacing 10
            transpose False
            xfill True

            for i in range(1, columns * rows + 1):


                button:
                    if current_mode == "save":
                        action [FileSave(i), SelectedIf(False)]

                    elif current_mode == "load":
                        action [SetField(no_rollback, "last_loaded_slot", [current_page, str(i)]),
                                FileLoad(i),
                                SelectedIf(False)]

                    elif current_mode == "move":
                        action FileManipulation(i, current_mode)

                    elif current_mode == "copy":
                        action FileManipulation(i, current_mode)

                    elif current_mode == "delete":
                        action [FileDelete(i), SelectedIf(False)]

                    fixed:


                        if (current_page == "quick"):
                            hbox:
                                text _("クイックセーブ № ") style_suffix "number_text"
                                text FileSlotName(i, columns * rows)[1:].zfill(2) style_suffix "number_text"
                        else:
                            hbox:
                                xalign 0.0
                                yalign 0.01

                                text _("セーブ № ") style_suffix "number_text"
                                text FileSlotName(i, columns * rows).zfill(2) style_suffix "number_text"



                        add FileScreenshot(i, empty = "gui/thumbnail_save_nodata.png") xalign 0.5 yalign 0.25


                        vbox:
                            yalign 0.923
                            spacing 8

                            $ file_save_name = FileSaveName(i)

                            text file_save_name style_suffix "slot_infotext"

                            if file_save_name:
                                hbox:
                                    text _("日付： ") style_suffix "slot_infotext"
                                    text FileTime(i, format=_("%Y/%m/%d - %H:%M"), empty=u'') style_suffix "slot_infotext"








                    if FileNewest(str(i), FileCurrentPage()):
                        add "gui/icon_new.png" align (1.0, 0.0195) xoffset 13


    use menu_navigation(config.menu_navigation_align)

    on "show":
        action Function(FileManipulation.reset_selected)

init -2:

    style file_manager_mode_frame:
        background None
        pos (33, 60)

    style file_manager_mode_button is menu_button:
        idle_background "gui/tab_idle.png"
        hover_background "gui/tab_hover.png"
        selected_background "gui/tab_selected.png"
        insensitive_background "gui/tab_insensitive.png"
        xysize (128, 30)
        activate_sound "button_click01"

    style file_manager_mode_button_text is menu_button_text:
        font "gui/fonts/NotoSansCJKjp-Regular.otf"
        size 14
        outlines []

    style file_manager_nav_button is menu_button:
        font "gui/fonts/NotoSansCJKjp-Medium.otf"
        background None
        hover_background "gui/num_hover.png"
        xysize (32, 32)
        activate_sound "page_turn"

    style file_manager_nav_button_text is menu_button_text:
        font "gui/fonts/NotoSansCJKjp-Regular.otf"
        size 14
        kerning 0
        outlines []

    style file_manager_nav_quicksave_button is file_manager_nav_button:
        hover_background "gui/quicksave_hover.png"
        xysize (160, 32)

    style file_manager_nav_quicksave_button_text is file_manager_nav_button_text

    style file_manager_slots_button:
        xysize (280, 240)
        background "gui/saveslot_idle.png"
        hover_background "gui/saveslot_hover.png"
        selected_background "gui/saveslot_selected.png"

    style file_manager_slots_number_text:
        font "gui/fonts/NotoSansCJKjp-Medium.otf"
        outlines []
        size 12

    style file_manager_slots_slot_infotext is text:
        size 12







screen preferences():
    tag menu


    default current_tab = "system"


    if main_menu:
        add "title_art"

    add "gui/right_click_bg.png"


    use menu_page_title(_("環境設定"), (1.0, 0.0))


    frame:
        style_prefix "preferences_page"

        background None
        pos (33, 60)

        has hbox

        textbutton _("システム"):
            action SetScreenVariable("current_tab", "system")

        textbutton _("サウンド"):
            action SetScreenVariable("current_tab", "sound")

    frame:
        style_prefix "preferences_options"

        background "gui/layout_settings.png"
        xysize (1200, 560)
        align (0.5, 0.615)
        xpadding 1
        ypadding 10


        has vbox
        spacing 10




        if current_tab == "system":

            frame:

                label _("画面モード")

                hbox:
                    textbutton _("ウインドウ") action Preference("display", "window")
                    textbutton _("フルスクリーン") action Preference("display", "fullscreen")

            frame:
                label _("メッセージ枠の透明度")

                bar value FieldValue(persistent, "message_alpha", 1.0, max_is_zero=False)


            frame:
                label _("未読メッセージの表示速度")
                bar value FieldValue(persistent, "text_cps_unseen", range=200, max_is_zero=True)

            frame:
                label _("既読メッセージの表示速度")
                bar value FieldValue(persistent, "text_cps_seen", range=200, max_is_zero=True)

            frame:
                label _("オートモード時のウエイト速度")
                bar value Preference("auto-forward time") style "preferences_options_bar"

            frame:
                label _("スキップモード")

                hbox:
                    textbutton _("既読のみ") action Preference("skip", "seen")
                    textbutton _("全て") action Preference("skip", "all")

            if config.has_voice:
                frame:
                    label _("オートモードは音声を待つ")

                    button style "checkbutton":
                        action Preference("wait for voice", "toggle")

            if config.developer:
                frame:
                    label _("言語")

                    hbox:
                        textbutton "日本語" action Language(None)
                        textbutton "English" action Language("english")





        elif current_tab == "sound":

            frame:
                label _("BGM")

                bar value Preference("music volume") style "preferences_options_bar"

            frame:
                label _("効果音")

                bar value Preference("mixer game_sfx volume") style "preferences_options_bar"

            frame:
                label _("システム効果音")

                bar value Preference("sound volume") style "preferences_options_bar"

            if config.has_voice:

                frame:
                    label _("ボイス")

                    bar value Preference("voice volume") style "preferences_options_bar"

            if config.has_voice:
                frame:
                    label _("ボイス再生を次のメッセージまで継続する")

                    button style "checkbutton":
                        action Preference("voice sustain", "toggle")


    use menu_navigation(config.menu_navigation_align)


    use reset_default_navigation(current_tab, (0.034, 0.98))

init -2:

    style preferences_page_button is file_manager_mode_button

    style preferences_page_button_text is file_manager_mode_button_text

    style preferences_options_frame:
        background Frame("gui/each_bg.png", 10, 10)
        ysize 45
        xfill True

    style preferences_options_label:
        align (0.01, 0.5)

    style preferences_options_label_text:
        size 15

    style preferences_options_hbox:
        spacing 10
        align (0.98, 0.5)

    style preferences_options_button is menu_button:
        xsize 145
        ysize 30
        align (0.98, 0.5)
        activate_sound "button_click03"

    style preferences_options_button_text is menu_button_text:
        size 13

    style preferences_options_bar:
        left_bar "gui/slider_left.png"
        right_bar "gui/slider_right.png"
        thumb "gui/slider_thumb.png"
        thumb_offset 14
        xsize 560
        ysize 28
        align (0.97, 0.5)

    style checkbutton:
        idle_background "gui/checkbox_idle.png"
        hover_background "gui/checkbox_hover.png"
        selected_idle_background "gui/checkbox_selected.png"
        selected_hover_background "gui/checkbox_selected_hover.png"
        xysize (28, 28)
        align (0.985, 0.5)
        activate_sound "button_click02"








screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add Solid("#000") alpha 0.8

    window:
        background None
        xysize (560, 200)
        align (0.5, 0.3)
        padding (20, 5)

        text _(message)

    hbox:
        align (0.5, 0.5)
        spacing 0

        textbutton _("はい") action yes_action style_suffix "button_yes"
        textbutton _("いいえ") action no_action style_suffix "button_no"


    key "game_menu" action no_action

init -2:

    style confirm_button:
        xysize (200, 107)

    style confirm_button_yes is confirm_button:
        background "gui/btn_yes_idle.png"
        hover_background "gui/btn_yesno_hover.png"

    style confirm_button_no is confirm_button:
        background "gui/btn_no_idle.png"
        hover_background "gui/btn_yesno_hover.png"

    style confirm_button_text is menu_button_text:
        size 20
        xalign 0.5
        yalign 0.9
        insensitive_color "#eee"

    style confirm_button_yes_text is confirm_button_text

    style confirm_button_no_text is confirm_button_text

    style confirm_text:
        font "gui/fonts/NotoSansCJKjp-Light.otf"
        size 24
        spacing 5
        xalign 0.5
        yalign 0.5
        layout "subtitle"
        text_align 0.5
        outlines [(absolute(1), Color("#bbbbbb55"), absolute(0), absolute(0))]









screen quick_menu(trans=None):

    style_prefix "quick"

    zorder 100


    frame at trans:

        background None
        xpadding 0
        top_padding 20
        bottom_padding 10
        xalign 0.5
        yalign 1.0

        has hbox
        spacing 0

        textbutton _("AUTO") action Preference("auto-forward", "toggle")
        textbutton _("SKIP") action Skip()
        if not _in_replay:
            textbutton _("QUICK SAVE") action QuickSave()
        if config.has_voice:
            textbutton _("VOICE") action VoiceReplay()
        textbutton _("HIDE") action HideInterface()
        textbutton _("MENU"):
            selected_background None
            action ShowMenu('game_menu')
        if _in_replay:
            textbutton _("END REPLAY") action EndReplay(False)

init -2:

    style quick_button is menu_button:
        xysize (138, 24)
        background None
        hover_background "gui/quick_button_bg_hover.png"
        selected_background "gui/quick_button_bg_hover.png"

    style quick_button_text is menu_button_text:
        font "gui/fonts/NotoSansCJKjp-Thin.otf"
        size 13
        outlines [(absolute(1), Color("#bbbbbb88"), absolute(0), absolute(0))]





screen info_panel(label_text, message_text, icon_d, alignment, trans=None):





    style_prefix "info_panel"

    frame at trans:
        background Frame("gui/right_click_info_line.png", 38, 0, 12, 0, ysize = 24, yoffset=28)
        align alignment

        has vbox
        spacing 5

        hbox:
            spacing 10
            xalign 0.09


            add icon_d


            label label_text


        window:
            background None
            margin (0, 0)
            top_padding 5
            bottom_padding 0
            left_padding 40
            right_padding 0
            xsize 500
            yminimum 50
            ymaximum 150

            text message_text

        transclude

init -2:

    style info_panel_label_text is text:
        font "gui/fonts/NotoSansCJKjp-Medium.otf"
        size 20
        spacing 0
        kerning 0
        layout "nobreak"

        outlines [(1, "#00000099", 0, 0)]

    style info_panel_text is text:
        font "gui/fonts/NotoSansCJKjp-Light.otf"
        size 13
        spacing 0
        kerning 0
        outlines [(1, "#00000088", 0, 0)]


screen game_menu():
    tag menu


    style_prefix "game_menu"

    default tp = Tooltip("")
    $ bgm_title = get_current_bgm_title()


    add "gui/right_click_bg.png"


    frame at game_menu_buttons_appear:
        background "rclick_buttons_frame"
        align (0.95, 0.5)
        xysize (567, 564)

        imagebutton:
            auto "gui/right_click_icon_save_%s.png"
            align (0.36, 0.13)
            hovered tp.Action(game_menu_tips["save"])
            action [ShowMenu("file_manager", "save"), SensitiveIf(not _in_replay)]

        imagebutton:
            auto "gui/right_click_icon_load_%s.png"
            align (0.64, 0.13)
            hovered tp.Action(game_menu_tips["load"])
            action [ShowMenu("file_manager", "load"), SensitiveIf(not _in_replay)]



        imagebutton:
            auto "gui/right_click_icon_story_%s.png"
            align (0.132, 0.36)
            hovered tp.Action(game_menu_tips["story"])
            action [ShowMenu("story_info"), SensitiveIf(not config.is_trial and not config.lock_story and not _in_replay)]

        imagebutton:
            auto "gui/right_click_icon_cardbook_%s.png"
            align (0.132, 0.64)
            hovered tp.Action(game_menu_tips["cardbook"])
            action [ShowMenu("cardbook"), SensitiveIf(not config.is_trial and not config.lock_cardbook and not _in_replay)]




        imagebutton:
            auto "gui/right_click_icon_config_%s.png"
            align (0.868, 0.36)
            hovered tp.Action(game_menu_tips["settings"])
            action ShowMenu("preferences")

        imagebutton:
            auto "gui/right_click_icon_backtotitle_%s.png"
            align (0.868, 0.64)
            hovered tp.Action(game_menu_tips["title"])
            action [MainMenu(), SensitiveIf(True)]



        imagebutton:
            auto "gui/right_click_icon_endgame_%s.png"
            align (0.36, 0.871)
            hovered tp.Action(game_menu_tips["quit"])
            action Quit(confirm=True)

        imagebutton:
            auto "gui/right_click_icon_backtogame_%s.png"
            align (0.64, 0.871)
            hovered tp.Action(game_menu_tips["close"])
            action Return()



        window:
            background None
            align (0.5, 0.5)
            xmaximum 250
            ymaximum 300
            padding (0, 0, 0 , 0)

            showif tp.value != "":
                text tp.value at game_menu_tooltip_appear:
                    style_suffix "tooltip_text"



    vbox at game_menu_chapter_info_appear style_suffix "chaptername_vbox":

        text save_name style_suffix "chaptername_text"

        hbox:
            spacing 15
            xalign 0.5

            add get_time_icon()

            text "[gameinfo_date]" style_suffix "date_text"

    on "show" action [Preference("auto-forward", "disable"), SetField(config, "skipping", None)]


    use info_panel(_("BGM"), get_current_bgm_title(), "gui/right_click_content_music.png", (0.05, 0.35), game_menu_info_appear)







    use info_panel(_("Location"), get_location_name(), "gui/right_click_content_location.png", (0.1, 0.50), game_menu_info_appear(0.1))







    use info_panel(_("Tip"), get_location_tip(), "gui/right_click_content_tips.png", (0.2, 0.65), game_menu_info_appear(0.2))






init -2:

    style game_menu_chaptername_vbox:
        spacing 15
        align (0.25, 0.15)

    style game_menu_chaptername_text:
        font "gui/fonts/NotoSerifCJKjp-Medium.otf"
        size 48
        xalign 0.5

    style game_menu_date_text:
        font "gui/fonts/CharisSILR.ttf"
        size 30
        line_spacing 0
        line_leading 0
        yoffset -7

    style game_menu_tooltip_text:
        font "gui/fonts/NotoSansCJKjp-Medium.otf"
        align (0.5, 0.5)
        size 18
        color "#fff"
        outlines [(1, "#00000099", 0, 0)]
        kerning 0
        line_spacing 0
        line_leading 0
        layout "subtitle"
        text_align 0.5




screen cardbook():
    tag menu


    default current_character = None
    default current_card = None

    $ cards_count = get_character_cards_count(current_character)


    add "gui/cardbook_bg.png"


    use menu_page_title(_("カードブック"), (1.0, 0.03))


    if current_character:
        label "Numeral " + character_info[current_character]["numeral"] style "cardbook_character_name_label":
            align (0.05, 0.06)


    grid 2 6:
        style_prefix "cardbook_characters"
        xalign 0.04
        yalign 0.55
        spacing 10


        button:
            idle_background "gui/thumb_rnk_idle.png"
            selected_background "gui/thumb_rnk_selected.png"
            hover_background "gui/thumb_rnk_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "rnk"),
                    SelectedIf(current_character == "rnk"),
                    SensitiveIf(current_character != "rnk" and gameinfo_cardbook_rnk_unlocked)]


        button:
            idle_background "gui/thumb_cnh_idle.png"
            selected_background "gui/thumb_cnh_selected.png"
            hover_background "gui/thumb_cnh_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "cnh"),
                    SelectedIf(current_character == "cnh"),
                    SensitiveIf(current_character != "cnh" and gameinfo_cardbook_cnh_unlocked)]


        button:
            idle_background "gui/thumb_mhr_idle.png"
            selected_background "gui/thumb_mhr_selected.png"
            hover_background "gui/thumb_mhr_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "mhr"),
                    SelectedIf(current_character == "mhr"),
                    SensitiveIf(current_character != "mhr" and gameinfo_cardbook_mhr_unlocked)]


        button:
            idle_background "gui/thumb_kik_idle.png"
            selected_background "gui/thumb_kik_selected.png"
            hover_background "gui/thumb_kik_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "kik"),
                    SelectedIf(current_character == "kik"),
                    SensitiveIf(current_character != "kik" and gameinfo_cardbook_kik_unlocked)]


        button:
            idle_background "gui/thumb_fed_idle.png"
            selected_background "gui/thumb_fed_selected.png"
            hover_background "gui/thumb_fed_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "fed"),
                    SelectedIf(current_character == "fed"),
                    SensitiveIf(current_character != "fed" and gameinfo_cardbook_fed_unlocked)]


        button:
            idle_background "gui/thumb_sca_idle.png"
            selected_background "gui/thumb_sca_selected.png"
            hover_background "gui/thumb_sca_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "sca"),
                    SelectedIf(current_character == "sca"),
                    SensitiveIf(current_character != "sca" and gameinfo_cardbook_sca_unlocked)]


        button:
            idle_background "gui/thumb_yuu_idle.png"
            selected_background "gui/thumb_yuu_selected.png"
            hover_background "gui/thumb_yuu_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "yuu"),
                    SelectedIf(current_character == "yuu"),
                    SensitiveIf(current_character != "yuu" and gameinfo_cardbook_yuu_unlocked)]


        button:
            idle_background "gui/thumb_son_idle.png"
            selected_background "gui/thumb_son_selected.png"
            hover_background "gui/thumb_son_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "son"),
                    SelectedIf(current_character == "son"),
                    SensitiveIf(current_character != "son" and gameinfo_cardbook_son_unlocked)]


        button:
            idle_background "gui/thumb_sig_idle.png"
            selected_background "gui/thumb_sig_selected.png"
            hover_background "gui/thumb_sig_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "sig"),
                    SelectedIf(current_character == "sig"),
                    SensitiveIf(current_character != "sig" and gameinfo_cardbook_sig_unlocked)]


        button:
            idle_background "gui/thumb_ode_idle.png"
            selected_background "gui/thumb_ode_selected.png"
            hover_background "gui/thumb_ode_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "ode"),
                    SelectedIf(current_character == "ode"),
                    SensitiveIf(current_character != "ode" and gameinfo_cardbook_ode_unlocked)]


        button:
            idle_background "gui/thumb_cha_idle.png"
            selected_background "gui/thumb_cha_selected.png"
            hover_background "gui/thumb_cha_hover.png"


            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "cha"),
                    SelectedIf(current_character == "cha"),
                    SensitiveIf(current_character != "cha" and gameinfo_cardbook_cha_unlocked)]


        button:
            idle_background "gui/thumb_aln_idle.png"
            selected_background "gui/thumb_aln_selected.png"
            hover_background "gui/thumb_aln_hover.png"

            action [SetScreenVariable("current_card", None),
                    SetScreenVariable("current_character", "aln"),
                    SelectedIf(current_character == "aln"),
                    SensitiveIf(current_character != "aln" and gameinfo_cardbook_aln_unlocked)]

    frame:
        background Frame("gui/frame.png", 4, 4)
        xsize 180
        ysize 506

        xalign 0.23
        yalign 0.55

        right_padding 1
        left_padding 1
        ypadding 1

        has vpgrid
        cols 1
        xfill True
        spacing 0

        if current_character:

            if cards_count > 0:


                if cards_count > 12:
                    scrollbars "vertical"
                    mousewheel True
                    draggable False

                for obj in sorted(get_character_cards(current_character), key = lambda x: cards[x]["order"]):
                    button:
                        style "cardbook_button"
                        hbox:
                            spacing 0
                            align (0.0, 0.5)
                            text cards[obj]["title"]["chara"] style "cardbook_button_text"
                            text " - " style "cardbook_button_text"
                            text cards[obj]["title"]["type"] style "cardbook_button_text"

                        action [SetScreenVariable("current_card", cards[obj]), SensitiveIf(current_card != cards[obj])]






    if current_character:

        window:
            style_prefix "cardbook_card"
            background current_card and "gui/card_front.png" or "gui/card_back.png"
            xysize (213, 400)
            align (0.7, 0.55)
            margin (0, 0)
            padding (10, 10)

            if current_card:

                label current_card["title"]["chara"]:
                    align (0.5, 0.01)

                text current_card["desc"]:
                    align (0.5, 0.5)

                label current_card["title"]["type"]:
                    align (0.5, 0.99)


    use menu_navigation(config.menu_navigation_align)

    on "replace" action Function(grant_achievement, "open_cardbook")

init -2:


    style cardbook_character_name_label_text:
        font "gui/fonts/NotoSerifCJKjp-Medium.otf"

        text_align 0.0
        size 46

    style cardbook_characters_button:
        xysize (76, 76)
        insensitive_background "gui/thumb_unk.png"

    style cardbook_button:
        ysize 40
        xfill True
        background None
        hover_background "#74040488"
        selected_background "#4b4b4b88"

    style cardbook_button_text:
        font "gui/fonts/NotoSerifCJKjp-Light.otf"
        size 16
        selected_color "#fff"





    style cardbook_card_text:
        font "gui/fonts/NotoSerifCJKjp-Light.otf"
        color "#000"
        size 18
        text_align 0.5

    style cardbook_card_label_text is cardbook_text:
        font "gui/fonts/NotoSerifCJKjp-SemiBold.otf"
        color "#000"
        size 22
        text_align 0.5




screen story_info():
    tag menu


    default current_chapter = None

    $ seen_chapters = get_seen_chapters()


    add "gui/right_click_bg.png"


    use menu_page_title(_("あらすじ"), (1.0, 0.03))

    if current_chapter:
        label plot_titles[current_chapter] style "chapter_name_label" align (0.05, 0.06)

    hbox:
        spacing 15
        xalign 0.5
        yalign 0.65


        frame:
            style_prefix "chapter_buttons"

            has vpgrid
            cols 1
            xfill True
            spacing 0

            if seen_chapters:


                if len(seen_chapters.keys()) >= 14:
                    scrollbars "vertical"
                    mousewheel True
                    draggable False

                for k in sorted(seen_chapters.keys(), key=sort_story_buttons):
                    button:
                        text plot_labels[k]

                        action [SetScreenVariable("current_chapter", k), SensitiveIf(current_chapter != k)]






        frame:
            style_prefix "chapter_contents"

            has side "l r"
            xfill True
            yfill True

            window:
                has viewport
                id "chapter_contents_window_vp"
                mousewheel True

                if current_chapter:

                    $ separator_height = 24

                    vbox:
                        spacing 0

                        null height separator_height

                        for obj in seen_chapters[current_chapter]:
                            text plots[current_chapter + "-" + obj]
                            null height separator_height

            vbar:
                value YScrollValue("chapter_contents_window_vp")
                bar_invert True
                unscrollable "hide"


    use menu_navigation(config.menu_navigation_align)

    on "replace" action Function(grant_achievement, "open_story")

init -2:

    style chapter_name_label_text is cardbook_character_name_label_text

    style chapter_buttons_frame:
        background Frame("gui/frame.png", 4, 4)
        xsize 160
        ysize 535

        right_padding 1
        left_padding 1
        ypadding 1

    style chapter_buttons_button is cardbook_button

    style chapter_buttons_text is cardbook_button_text:
        text_align 0.5

    style chapter_contents_frame is chapter_buttons_frame:
        xsize 1025
        ysize 535

    style chapter_contents_window:
        background None
        margin (0, 0)
        padding (20, 0)

    style chapter_contents_text:
        font "gui/fonts/NotoSansCJKjp-Light.otf"
        color "#FFF"
        size 16
        spacing 24
        outlines []




screen ctc():

    zorder 100

    if renpy.get_screen("say") and not renpy.in_rollback():
        add "ctc_icon" at ctc_anime:
            align config.ctc_align




screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        background Frame("gui/main_notify_bg.png", 0,0, right=40)
        align (0.0, 0.05)
        right_padding 60
        left_padding 10

        has hbox
        spacing 10

        add "gui/main_notify_icon.png" yalign 0.5
        text message

    timer 3.25 action Hide('notify')

init -2:

    style notify_text is text:
        size 18
        yalign 0.5




screen hud():

    zorder 100
    style_prefix "hud"

    frame at hud_appear:
        background Frame("gui/main_hud_bg.png", 40)
        align (1.0, 0.05)
        left_padding 40
        right_padding 30

        has hbox
        spacing 10

        add get_time_icon() yalign 0.5
        text "[gameinfo_date]"

    timer 5 action Hide('hud')

init -2:

    style hud_text is notify_text




screen demo_last():

    default link = "http://fatal12.com/"

    add "gui/demo_last_bg.png"

    if _preferences.language is "english":
        $ link = "http://fatal12.com/en.html/"

    imagebutton style "home_link":
        idle "gui/demo_last_link.png"
        hover "gui/demo_last_link_hover.png"
        action OpenURL(link)

init -2:

    style home_link:
        pos (988, 582)




screen extra(mode="gallery"):
    tag menu


    default current_mode = mode
    default current_replay_mode = "endings"
    default gallery_current_page = 1
    default replay_current_page = 1
    default page_number = 10


    if main_menu:
        add "title_art"

    add "gui/right_click_bg.png"


    use menu_page_title(_("エクストラ"), (1.0, 0.00))


    frame:
        style_prefix "extra_manager_mode"

        has hbox


        textbutton _("ギャラリー"):
            action [SetScreenVariable("current_mode", "gallery"),
                    SensitiveIf(current_mode != "gallery"),
                    SetScreenVariable("page_number", 10)]


        textbutton _("リプレイ"):
            action [SetScreenVariable("current_mode", "replay"),
                    SensitiveIf(current_mode != "replay"),
                    SetScreenVariable("page_number", 3),
                    Function(grant_achievement, "open_scenereplay")]

    frame:
        background "gui/layout_extra.png"
        xysize (1200, 560)
        align (0.5, 0.615)
        xpadding (current_mode == "gallery") and 16 or 24
        ypadding (current_mode == "gallery") and 35 or 10

        has vbox
        spacing (current_mode == "gallery") and 35 or 10

        hbox:
            style_prefix "extra_manager_nav"
            xalign (current_mode == "gallery") and 0.5 or 0.565

            if current_mode == "gallery":
                for i in range (1, (page_number + 1)):

                    $ current_index = str(i)

                    textbutton current_index:
                        action [SetScreenVariable("gallery_current_page", i), SensitiveIf(gallery_current_page != i)]

            elif current_mode == "replay":

                xminimum 500

                textbutton _("エンディング"):
                    action [SetScreenVariable("current_replay_mode", "endings"),
                        SensitiveIf(current_replay_mode != "endings")] style "extra_manager_nav_endings_button"

                hbox:
                    xalign 1.0
                    spacing 0

                    textbutton _("女神の選定"):
                        action [SetScreenVariable("current_replay_mode", "sentei"),
                            SensitiveIf(current_replay_mode != "sentei")] style "extra_manager_nav_sentei_button"

                    for i in range (1, (page_number + 1)):

                        $ current_index = str(i)

                        textbutton current_index:
                            action [SetScreenVariable("replay_current_page", i),
                                SensitiveIf(current_replay_mode == "sentei" and replay_current_page != i)]




        if current_mode == "gallery":

            python:
                rows = 2
                columns = 3
                items_per_page = rows * columns
                first_slot = (gallery_current_page - 1)  * items_per_page + 1
                last_slot = first_slot + items_per_page



                nulls_number = 4
                existing_slot_last_page = gallery_current_page * items_per_page - nulls_number

            grid columns rows:
                style_prefix "gallery_items"

                for i in range(first_slot, last_slot):

                    $ num = str(i).zfill(2)

                    if gallery_current_page == page_number and i > existing_slot_last_page:
                        null width 378 height 212

                    else:
                        add gallery.make_button(
                            num, "gui/thumb_ecg_" + num + ".png",
                            locked="gui/thumb_ecg_nodata.png", style="gallery_item", hover_border="gui/thumb_ecg_hover.png")


        elif current_mode == "replay" and current_replay_mode == "endings":

            vbox:
                style_prefix "replay_ed_items"

                hbox:

                    button:
                        style "replay_ed_good_items"
                        idle_background "gui/good01_idle.png"
                        hover_background "gui/good01_hover.png"

                        action [Replay("fTRUE"), SensitiveIf(persistent.TRUE_clear)]

                    button:
                        style "replay_ed_good_items"
                        idle_background "gui/good02_idle.png"
                        hover_background "gui/good02_hover.png"
                        action [Replay("fMIHARU"), SensitiveIf(persistent.MIHARU_clear)]

                    button:
                        style "replay_ed_good_items"
                        idle_background "gui/good03_idle.png"
                        hover_background "gui/good03_hover.png"

                        action [Replay("fUNHAPPY"), SensitiveIf(persistent.UNHAPPY_clear)]

                hbox:

                    button:
                        style "replay_ed_bad_items"
                        idle_background "gui/bad01_idle.png"
                        hover_background "gui/bad01_hover.png"

                        action [Replay("fBAD_01"), SensitiveIf(persistent.BAD01_clear)]

                    button:
                        style "replay_ed_bad_items"
                        idle_background "gui/bad02_idle.png"
                        hover_background "gui/bad02_hover.png"

                        action [Replay("fBAD_02"), SensitiveIf(persistent.BAD02_clear)]

                    button:
                        style "replay_ed_bad_items"
                        idle_background "gui/bad03_idle.png"
                        hover_background "gui/bad03_hover.png"

                        action [Replay("fBAD_03"), SensitiveIf(persistent.BAD03_clear)]

                    button:
                        style "replay_ed_bad_items"
                        idle_background "gui/bad04_idle.png"
                        hover_background "gui/bad04_hover.png"

                        action [Replay("fBAD_04"), SensitiveIf(persistent.BAD04_clear)]

        elif current_replay_mode == "sentei":

            $ nulls_number = 2

            grid 3 2:
                style_prefix "replay_sentei_items"

                if replay_current_page == 1:

                    button:
                        idle_background "gui/thumb_scene_replay_DS_01_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_01_hover.png"
                        action [Replay("sentei1"), SensitiveIf(persistent.sentei1_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_02_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_02_hover.png"
                        action [Replay("sentei2"), SensitiveIf(persistent.sentei2_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_03_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_03_hover.png"
                        action [Replay("sentei3"), SensitiveIf(persistent.sentei3_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_04_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_04_hover.png"
                        action [Replay("sentei4"), SensitiveIf(persistent.sentei4_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_05_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_05_hover.png"
                        action [Replay("sentei5"), SensitiveIf(persistent.sentei5_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_06_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_06_hover.png"
                        action [Replay("sentei6"), SensitiveIf(persistent.sentei6_clear)]

                elif replay_current_page == 2:

                    button:
                        idle_background "gui/thumb_scene_replay_DS_07-1_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_07-1_hover.png"
                        action [Replay("sentei7", { "flags_route_A" : True }), SensitiveIf(persistent.sentei7A_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_07-2_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_07-2_hover.png"
                        action [Replay("sentei7", { "flags_route_B" : True }), SensitiveIf(persistent.sentei7B_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_08_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_08_hover.png"
                        action [Replay("sentei8"), SensitiveIf(persistent.sentei8_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_09-1_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_09-1_hover.png"
                        action [Replay("sentei9", { "flags_route_C" : True }), SensitiveIf(persistent.sentei9C_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_09-2_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_09-2_hover.png"
                        action [Replay("sentei9", { "flags_route_D" : True }), SensitiveIf(persistent.sentei9D_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_10_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_10_hover.png"
                        action [Replay("sentei10"), SensitiveIf(persistent.sentei10_clear)]

                elif replay_current_page == 3:

                    button:
                        idle_background "gui/thumb_scene_replay_DS_11-1_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_11-1_hover.png"
                        action [Replay("sentei11", { "flags_route_F" : True }), SensitiveIf(persistent.sentei11F_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_11-2_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_11-2_hover.png"
                        action [Replay("sentei11", { "flags_route_G" : True }), SensitiveIf(persistent.sentei11G_clear)]

                    button:
                        idle_background "gui/thumb_scene_replay_DS_11-3_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_11-3_hover.png"
                        action [Replay("sentei11", { "flags_route_H" : True }), SensitiveIf(persistent.sentei11H_clear)]


                    button:
                        idle_background "gui/thumb_scene_replay_DS_12_idle.png"
                        hover_background "gui/thumb_scene_replay_DS_12_hover.png"
                        action [Replay("sentei12"), SensitiveIf(persistent.sentei12_clear)]

                    for i in range (0, nulls_number):
                        null width 368 height 232



    use menu_navigation(config.menu_navigation_align)

    on "replace" action Function(grant_achievement, "open_gallery")




init -2:

    style extra_manager_mode_frame is file_manager_mode_frame

    style extra_manager_mode_button is file_manager_mode_button

    style extra_manager_mode_button_text is file_manager_mode_button_text

    style extra_manager_nav_button is file_manager_nav_button

    style extra_manager_nav_button_text is file_manager_nav_button_text

    style extra_manager_nav_endings_button is file_manager_nav_quicksave_button

    style extra_manager_nav_sentei_button is extra_manager_nav_endings_button

    style extra_manager_nav_endings_button_text is file_manager_nav_quicksave_button_text

    style extra_manager_nav_sentei_button_text is extra_manager_nav_endings_button_text

    style gallery_items_grid:
        xalign 0.5
        spacing 17

    style gallery_item:
        xysize (378, 212)
        insensitive_background "gui/thumbnail_ecg_nodata.png"

    style replay_ed_items_vbox:
        xalign 0.5
        spacing 22

    style replay_ed_items_hbox:
        xalign 0.5
        spacing 24

    style replay_ed_good_items:
        xysize (368, 266)
        background None
        insensitive_background "gui/thumbnail_no_arrival_good.png"

    style replay_ed_bad_items:
        xysize (270, 200)
        background None
        insensitive_background "gui/thumbnail_no_arrival_bad.png"

    style replay_sentei_items_grid:
        xalign 0.5
        xspacing 23
        yspacing 20
        yoffset -1

    style replay_sentei_items_button:
        xysize (368, 232)
        background None
        insensitive_background "gui/thumbnail_no_data_sentei.png"





screen _gallery:

    if locked:
        add "#000"
        text _("Image [index] of [count] locked.") align (0.5, 0.5)
    else:
        frame:
            background "#000"
            xpadding 0
            ypadding 0

            has viewport
            scrollbars None
            mousewheel True
            arrowkeys True

            for d in displayables:
                add d

    if gallery.slideshow:
        timer gallery.slideshow_delay action Return("next") repeat True

    key "game_menu" action gallery.Return()


    key "mouseup_1" action gallery.Next(unlocked=gallery.unlocked_advance)
    key "K_SPACE" action gallery.Next(unlocked=gallery.unlocked_advance)


    if gallery.navigation:
        use gallery_navigation

screen gallery_navigation:
    hbox:
        spacing 20

        style_group "gallery"
        align (.98, .98)

        textbutton _("prev") action gallery.Previous(unlocked=gallery.unlocked_advance)
        textbutton _("next") action gallery.Next(unlocked=gallery.unlocked_advance)
        textbutton _("slideshow") action gallery.ToggleSlideshow()
        textbutton _("return") action gallery.Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

# FATAL TWELVE bonus access. A single patch preference controls preview availability.
init 8 python:
    import copy as _f12_bonus_copy
    import renpy.persistent as _f12_persistence

    def f12_bonus_enabled():
        return bool(getattr(renpy.game.persistent, "f12_bonus_open", False))

    class F12BonusSetting(Action, DictEquality):
        def __init__(self, enabled):
            self.enabled = bool(enabled)

        def __call__(self):
            renpy.game.persistent.f12_bonus_open = self.enabled
            f12_fc_set_revealed(self.enabled)
            renpy.restart_interaction()

        def get_selected(self):
            return f12_bonus_enabled() == self.enabled

    def f12_bonus_label(ko, en, ja):
        return {"korean": ko, "english": en}.get(_preferences.language, ja)

    def f12_bonus_gallery_for_view():
        return _f12_preview_gallery if f12_bonus_enabled() else gallery

    def _f12_build_preview_gallery(source):
        duplicate = Gallery()
        for key in ("transition", "unlocked_advance", "navigation", "span_buttons", "slideshow_delay"):
            setattr(duplicate, key, getattr(source, key))
        for name, group in sorted(source.buttons.items(), key=lambda pair: pair[1].index):
            duplicate.button(name)
            for image in group.images:
                duplicate.image(*image.displayables)
                duplicate.transform(*image.transforms)
        return duplicate

    _f12_preview_gallery = _f12_build_preview_gallery(gallery)

    def _f12_bonus_progress_key(key):
        return (key.startswith("_seen") or key.startswith("_chosen") or
                key.endswith("_clear") or key.endswith("_seen"))

    def f12_bonus_run_preview(action):
        if not f12_bonus_enabled() or store._in_replay:
            return action()
        # Replay executes actual script statements. Retain reading, images, and
        # routes from ordinary play, including play while bonus access is on.
        renpy.save_persistent()
        owner = renpy.game.persistent
        snap = {k: _f12_bonus_copy.deepcopy(v) for k, v in vars(owner).items() if _f12_bonus_progress_key(k)}
        seen = renpy.game.seen_session.copy()
        count = renpy.game.seen_translates_count
        saving = _f12_persistence.should_save_persistent
        _f12_persistence.should_save_persistent = False
        try:
            return action()
        finally:
            values = vars(owner)
            for key in list(values):
                if _f12_bonus_progress_key(key) and key not in snap:
                    del values[key]
            values.update(snap)
            renpy.game.seen_session.clear()
            renpy.game.seen_session.update(seen)
            renpy.game.seen_translates_count = count
            _f12_persistence.should_save_persistent = saving
            renpy.save_persistent()

    class F12BonusReplay(Replay):
        def __call__(self):
            return f12_bonus_run_preview(super(F12BonusReplay, self).__call__)

    def f12_bonus_replay(label, earned, scope=None):
        if f12_bonus_enabled():
            return F12BonusReplay(label, scope or {}, locked=False)
        return [Replay(label, scope or {}), SensitiveIf(earned)]

    def f12_bonus_gallery_achievement(key):
        if not f12_bonus_enabled():
            grant_achievement(key)

    if _f12_sync_language_selector in config.interact_callbacks:
        config.interact_callbacks.remove(_f12_sync_language_selector)


init 10:

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

        if current_tab == "system":
            use f12_patch_language_selector
            frame:
                style "preferences_options_frame"
                xpos 40
                ypos 548
                xsize 1200

                label f12_bonus_label(u"특전", u"Extras", u"特典"):
                    style "preferences_options_label"

                hbox:
                    style "preferences_options_hbox"

                    textbutton f12_bonus_label(u"특전 개방", u"Unlock extras", u"特典を開放"):
                        style "preferences_options_button"
                        id "f12_bonus_open_button"
                        action F12BonusSetting(True)

                    textbutton f12_bonus_label(u"개방 취소", u"Cancel unlock", u"開放を取り消す"):
                        style "preferences_options_button"
                        id "f12_bonus_cancel_button"
                        action F12BonusSetting(False)

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
                                            SensitiveIf((f12_bonus_enabled() and not config.is_trial and not config.lock_extra) or (not config.is_trial and
                                                not config.lock_extra and
                                                persistent.TRUE_clear or persistent.UNHAPPY_clear or persistent.MIHARU_clear))]
            textbutton _("QUIT") action Quit(confirm=False)

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
                        Function(f12_bonus_gallery_achievement, "open_scenereplay")]

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
                            add f12_bonus_gallery_for_view().make_button(
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

                            action f12_bonus_replay("fTRUE", persistent.TRUE_clear)

                        button:
                            style "replay_ed_good_items"
                            idle_background "gui/good02_idle.png"
                            hover_background "gui/good02_hover.png"
                            action f12_bonus_replay("fMIHARU", persistent.MIHARU_clear)

                        button:
                            style "replay_ed_good_items"
                            idle_background "gui/good03_idle.png"
                            hover_background "gui/good03_hover.png"

                            action f12_bonus_replay("fUNHAPPY", persistent.UNHAPPY_clear)

                    hbox:

                        button:
                            style "replay_ed_bad_items"
                            idle_background "gui/bad01_idle.png"
                            hover_background "gui/bad01_hover.png"

                            action f12_bonus_replay("fBAD_01", persistent.BAD01_clear)

                        button:
                            style "replay_ed_bad_items"
                            idle_background "gui/bad02_idle.png"
                            hover_background "gui/bad02_hover.png"

                            action f12_bonus_replay("fBAD_02", persistent.BAD02_clear)

                        button:
                            style "replay_ed_bad_items"
                            idle_background "gui/bad03_idle.png"
                            hover_background "gui/bad03_hover.png"

                            action f12_bonus_replay("fBAD_03", persistent.BAD03_clear)

                        button:
                            style "replay_ed_bad_items"
                            idle_background "gui/bad04_idle.png"
                            hover_background "gui/bad04_hover.png"

                            action f12_bonus_replay("fBAD_04", persistent.BAD04_clear)

            elif current_replay_mode == "sentei":

                $ nulls_number = 2

                grid 3 2:
                    style_prefix "replay_sentei_items"

                    if replay_current_page == 1:

                        button:
                            idle_background "gui/thumb_scene_replay_DS_01_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_01_hover.png"
                            action f12_bonus_replay("sentei1", persistent.sentei1_clear)

                        button:
                            idle_background "gui/thumb_scene_replay_DS_02_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_02_hover.png"
                            action f12_bonus_replay("sentei2", persistent.sentei2_clear)

                        button:
                            idle_background "gui/thumb_scene_replay_DS_03_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_03_hover.png"
                            action f12_bonus_replay("sentei3", persistent.sentei3_clear)

                        button:
                            idle_background "gui/thumb_scene_replay_DS_04_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_04_hover.png"
                            action f12_bonus_replay("sentei4", persistent.sentei4_clear)

                        button:
                            idle_background "gui/thumb_scene_replay_DS_05_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_05_hover.png"
                            action f12_bonus_replay("sentei5", persistent.sentei5_clear)

                        button:
                            idle_background "gui/thumb_scene_replay_DS_06_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_06_hover.png"
                            action f12_bonus_replay("sentei6", persistent.sentei6_clear)

                    elif replay_current_page == 2:

                        button:
                            idle_background "gui/thumb_scene_replay_DS_07-1_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_07-1_hover.png"
                            action f12_bonus_replay("sentei7", persistent.sentei7A_clear, { "flags_route_A" : True })

                        button:
                            idle_background "gui/thumb_scene_replay_DS_07-2_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_07-2_hover.png"
                            action f12_bonus_replay("sentei7", persistent.sentei7B_clear, { "flags_route_B" : True })

                        button:
                            idle_background "gui/thumb_scene_replay_DS_08_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_08_hover.png"
                            action f12_bonus_replay("sentei8", persistent.sentei8_clear)

                        button:
                            idle_background "gui/thumb_scene_replay_DS_09-1_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_09-1_hover.png"
                            action f12_bonus_replay("sentei9", persistent.sentei9C_clear, { "flags_route_C" : True })

                        button:
                            idle_background "gui/thumb_scene_replay_DS_09-2_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_09-2_hover.png"
                            action f12_bonus_replay("sentei9", persistent.sentei9D_clear, { "flags_route_D" : True })

                        button:
                            idle_background "gui/thumb_scene_replay_DS_10_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_10_hover.png"
                            action f12_bonus_replay("sentei10", persistent.sentei10_clear)

                    elif replay_current_page == 3:

                        button:
                            idle_background "gui/thumb_scene_replay_DS_11-1_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_11-1_hover.png"
                            action f12_bonus_replay("sentei11", persistent.sentei11F_clear, { "flags_route_F" : True })

                        button:
                            idle_background "gui/thumb_scene_replay_DS_11-2_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_11-2_hover.png"
                            action f12_bonus_replay("sentei11", persistent.sentei11G_clear, { "flags_route_G" : True })

                        button:
                            idle_background "gui/thumb_scene_replay_DS_11-3_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_11-3_hover.png"
                            action f12_bonus_replay("sentei11", persistent.sentei11H_clear, { "flags_route_H" : True })


                        button:
                            idle_background "gui/thumb_scene_replay_DS_12_idle.png"
                            hover_background "gui/thumb_scene_replay_DS_12_hover.png"
                            action f12_bonus_replay("sentei12", persistent.sentei12_clear)

                        for i in range (0, nulls_number):
                            null width 368 height 232



        use menu_navigation(config.menu_navigation_align)

        on "replace" action Function(f12_bonus_gallery_achievement, "open_gallery")

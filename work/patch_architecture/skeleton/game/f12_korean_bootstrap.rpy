# Fatal Twelve Korean patch bootstrap (source skeleton only).
#
# This file is intentionally additive. It does not replace localize.rpyc,
# system.rpa, scenario.rpa, or tl.rpa.

init -999 python:

    # The shipped loose localize.rpyc runs at init priority -1000 and assigns
    # _preferences.language = "english" on every boot. Keep a patch-owned
    # preference so Japanese/English/Korean choices survive that assignment.
    _f12_language_marker = getattr(persistent, "fatal12_ko_language_v1", None)

    if _f12_language_marker not in ("japanese", "english", "korean"):
        _f12_language_marker = "korean"
        persistent.fatal12_ko_language_v1 = _f12_language_marker

    if _f12_language_marker == "japanese":
        _preferences.language = None
    else:
        _preferences.language = _f12_language_marker


    class F12PatchLanguage(Action, DictEquality):

        def __init__(self, marker, language):
            self.marker = marker
            self.language = language

        def __call__(self):
            persistent.fatal12_ko_language_v1 = self.marker
            renpy.change_language(self.language)

        def get_selected(self):
            return _preferences.language == self.language

        def get_sensitive(self):
            if self.language is None:
                return True

            return self.language in renpy.known_languages()


    def _f12_sync_language_selector():
        """Shows the additive selector only on Preferences > System."""

        preferences_screen = renpy.get_screen("preferences")
        selector_screen = renpy.get_screen("f12_patch_language_selector")

        should_show = (
            preferences_screen is not None and
            preferences_screen.scope.get("current_tab", None) == "system"
        )

        if should_show and selector_screen is None:
            renpy.show_screen("f12_patch_language_selector")
        elif not should_show and selector_screen is not None:
            renpy.hide_screen("f12_patch_language_selector")


    if _f12_sync_language_selector not in config.interact_callbacks:
        config.interact_callbacks.append(_f12_sync_language_selector)


# The original developer-only language row would occupy this exact eighth row:
# options frame x=40, top~=98, ypadding=10, row height=45, vbox spacing=10.
screen f12_patch_language_selector:

    zorder 250

    frame:
        style "preferences_options_frame"
        xpos 40
        ypos 493
        xsize 1200

        label "언어":
            style "preferences_options_label"

        hbox:
            style "preferences_options_hbox"

            textbutton "日本語":
                style "preferences_options_button"
                action F12PatchLanguage("japanese", None)

            textbutton "English":
                style "preferences_options_button"
                action F12PatchLanguage("english", "english")

            textbutton "한국어":
                style "preferences_options_button"
                action F12PatchLanguage("korean", "korean")


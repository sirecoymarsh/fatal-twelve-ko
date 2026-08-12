# Fatal Twelve Korean language-slot registration and font overrides.
# No scenario or UI translation text is included in this architecture skeleton.

translate korean python:

    # The shipped dialogue font (mgenplus-2pp-regular.ttf) has no Hangul
    # syllable glyphs. The shipped Noto CJK fonts cover all 11,172 modern
    # Hangul syllables and preserve Japanese/Latin coverage.
    style._default.font = "gui/fonts/NotoSansCJKjp-Regular.otf"
    style.default.font = "gui/fonts/NotoSansCJKjp-Regular.otf"
    style.say_dialogue.font = "gui/fonts/NotoSansCJKjp-Regular.otf"

    # These two shipped styles use IPAex Mincho and Charis SIL respectively;
    # neither font contains Hangul. Override them only while Korean is active.
    style.menu_page_title_label_text.font = "gui/fonts/NotoSansCJKjp-Medium.otf"
    style.game_menu_date_text.font = "gui/fonts/NotoSansCJKjp-Regular.otf"

    # Ren'Py 6.99.14.3 explicitly supports this line-breaking mode.
    style._default.language = "korean-with-spaces"
    style.default.language = "korean-with-spaces"


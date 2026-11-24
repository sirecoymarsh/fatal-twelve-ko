# Fatal Twelve: Korean date display only. Original date validation is retained.
# Authored by Codex internal; no scenario text or user preference changes.
init 100 python:
    import re as _f12_ui_date_re

    _f12_ui_weekdays = (
        (u"MON", u"월"), (u"TUE", u"화"), (u"WED", u"수"),
        (u"THU", u"목"), (u"FRI", u"금"), (u"SAT", u"토"),
        (u"SUN", u"일"),
    )

    def _f12_ui_date_for_language(value, language):
        # Only this game's exact date format is eligible. Unknown dates survive.
        if not isinstance(value, basestring):
            return value
        match = _f12_ui_date_re.match(
            ur"\A([0-9]{2}/[0-9]{2} \()(MON|TUE|WED|THU|FRI|SAT|SUN|월|화|수|목|금|토|일)(\))\Z",
            value)
        if match is None:
            return value
        token = match.group(2)
        for english, korean in _f12_ui_weekdays:
            if token in (english, korean):
                result = korean if language == "korean" else english
                return match.group(1) + result + match.group(3)
        return value

    def _f12_ui_sync_date():
        value = getattr(store, "gameinfo_date", None)
        translated = _f12_ui_date_for_language(value, _preferences.language)
        if translated != value:
            store.gameinfo_date = translated

    _f12_ui_original_set_info_date = set_info_date

    def _f12_ui_set_info_date(month, day, weekday):
        result = _f12_ui_original_set_info_date(month, day, weekday)
        _f12_ui_sync_date()
        return result

    set_info_date = _f12_ui_set_info_date

    # Restore original English date labels in preserved languages, and repair
    # saved/rolled-back dates at the next interaction before screens render.
    if _f12_ui_sync_date not in config.change_language_callbacks:
        config.change_language_callbacks.append(_f12_ui_sync_date)
    if _f12_ui_sync_date not in config.interact_callbacks:
        config.interact_callbacks.append(_f12_ui_sync_date)

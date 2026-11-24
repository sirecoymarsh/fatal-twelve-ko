# Fatal Twelve review-build audio restoration.
# Runs once per Ren'Py persistent profile, then leaves user settings alone.

init 999 python:
    if not getattr(persistent, "fatal12_audio_restored_v1", False):
        for _f12_audio_mixer in ("music", "sfx", "voice"):
            _preferences.set_mute(_f12_audio_mixer, False)
            _preferences.set_volume(_f12_audio_mixer, 1.0)

        persistent.fatal12_audio_restored_v1 = True

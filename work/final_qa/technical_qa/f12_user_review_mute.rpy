# Fatal Twelve isolated user-review mute overlay.
# Review-only: never include this file in the distributable patch payload.

init -1200 python:
    config.sound = False
    config.audio_periodic_thread = False

    for _f12_review_mixer in ("music", "sfx", "voice"):
        _preferences.set_volume(_f12_review_mixer, 0.0)
        _preferences.set_mute(_f12_review_mixer, True)


init 999 python:
    # Reassert after all shipped init blocks. SDL_AUDIODRIVER=dummy remains the
    # independent process-level safety layer used by the visible launcher.
    config.sound = False

    for _f12_review_mixer in ("music", "sfx", "voice"):
        _preferences.set_volume(_f12_review_mixer, 0.0)
        _preferences.set_mute(_f12_review_mixer, True)


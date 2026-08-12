


init -3:
    define std_change = Dissolve(DELAY_FAST)
    define ecg_change = Dissolve(DELAY_NORMAL)
    define ci_change = Dissolve(DELAY_FAST)


define std_change_wait = Dissolve(DELAY_FAST)
define std_in = Dissolve(DELAY_NORMAL)
define std_out = std_in
define std_swap = Dissolve(DELAY_NORMAL)

define std_slide_in_lr = DissolveMoveIn(DELAY_NORMAL, xoffset(-STD_SLIDE_OFFSET), easein)
define std_slide_out_lr = DissolveMoveOut(DELAY_NORMAL, xoffset(STD_SLIDE_OFFSET), easein)
define std_slide_in_rl = DissolveMoveIn(DELAY_NORMAL, xoffset(STD_SLIDE_OFFSET), easein)
define std_slide_out_rl = DissolveMoveOut(DELAY_NORMAL, xoffset(-STD_SLIDE_OFFSET), easein)

define std_slide_in_lr_long = DissolveMoveIn(DELAY_LONG, xoffset(-STD_SLIDE_OFFSET), linear)
define std_slide_out_lr_long = DissolveMoveOut(DELAY_LONG, xoffset(STD_SLIDE_OFFSET), linear)
define std_slide_in_rl_long = DissolveMoveIn(DELAY_LONG, xoffset(STD_SLIDE_OFFSET), linear)
define std_slide_out_rl_long = DissolveMoveOut(DELAY_LONG, xoffset(-STD_SLIDE_OFFSET), linear)


define ecg_change_wait = Dissolve(DELAY_NORMAL)


define ci_change_wait = Dissolve(DELAY_FAST)
define ci_swap = Dissolve(DELAY_NORMAL)
define ci_in = Dissolve(DELAY_NORMAL)
define ci_out = std_in




define dissolve_fastest = Dissolve(DELAY_FASTEST)
define dissolve_fast = Dissolve(DELAY_FAST)
define dissolve_long = Dissolve(DELAY_LONG)
define dissolve_longest = Dissolve(DELAY_LONGEST)


define wipe_lr_fast = WipeTransition(WIPE_HORIZONTAL, DELAY_FAST, reverse=True)
define wipe_lr = WipeTransition(WIPE_HORIZONTAL, DELAY_NORMAL, reverse=True)
define wipe_lr_long = WipeTransition(WIPE_HORIZONTAL, DELAY_LONG, reverse=True)

define wipe_rl_fast = WipeTransition(WIPE_HORIZONTAL, DELAY_FAST)
define wipe_rl = WipeTransition(WIPE_HORIZONTAL, DELAY_NORMAL)
define wipe_rl_long = WipeTransition(WIPE_HORIZONTAL, DELAY_LONG)

define wipe_bu_fast = WipeTransition(WIPE_VERTICAL, DELAY_FAST)
define wipe_bu = WipeTransition(WIPE_VERTICAL, DELAY_NORMAL)
define wipe_bu_long = WipeTransition(WIPE_VERTICAL, DELAY_LONG)

define wipe_td_fast = WipeTransition(WIPE_VERTICAL, DELAY_FAST, reverse=True)
define wipe_td = WipeTransition(WIPE_VERTICAL, DELAY_NORMAL, reverse=True)
define wipe_td_long = WipeTransition(WIPE_VERTICAL, DELAY_LONG, reverse=True)


define fade_normal = ComposedTransition(dissolve)
define fade_long = ComposedTransition(dissolve_long, inbetween_time=DELAY_LONG)
define fade_longest = ComposedTransition(dissolve_longest, inbetween_time=DELAY_LONGEST)

define wfade_fastest = ComposedTransition(dissolve_fastest, inbetween_time=0.2, inbetween_color="#FFF")
define wfade_normal = ComposedTransition(dissolve, inbetween_color="#FFF")
define wfade_long = ComposedTransition(dissolve_long, inbetween_time=DELAY_LONG, inbetween_color="#FFF")
define wfade_longest = ComposedTransition(dissolve_longest, inbetween_time=DELAY_LONGEST, inbetween_color="#FFF")


define comp_lr = ComposedTransition(WipeTransition(WIPE_HORIZONTAL, DELAY_NORMAL))
define comp_lr_long = ComposedTransition(WipeTransition(WIPE_HORIZONTAL, DELAY_LONG), inbetween_time=DELAY_LONG)

define comp_rl = ComposedTransition(WipeTransition(WIPE_HORIZONTAL, DELAY_NORMAL, reverse=True))
define comp_rl_long = ComposedTransition(WipeTransition(WIPE_HORIZONTAL, DELAY_LONG, reverse=True), inbetween_time=DELAY_LONG)

define comp_bu = ComposedTransition(WipeTransition(WIPE_VERTICAL, DELAY_NORMAL))
define comp_bu_long = ComposedTransition(WipeTransition(WIPE_VERTICAL, DELAY_LONG), inbetween_time=DELAY_LONG)

define comp_td = ComposedTransition(WipeTransition(WIPE_VERTICAL, DELAY_NORMAL, reverse=True))
define comp_td_long = ComposedTransition(WipeTransition(WIPE_VERTICAL, DELAY_LONG, reverse=True), inbetween_time=DELAY_LONG)


define quake_light = Shake((0.5, 1.0, 0.5, 1.0), 0.1, dist=2, loop=True)
define quake = Shake((0.5, 1.0, 0.5, 1.0), 0.1, dist=5, loop=True)
define quake_fast = Shake((0.5, 1.0, 0.5, 1.0), DELAY_FAST, dist=10, loop=False)
define quake_normal = Shake((0.5, 1.0, 0.5, 1.0), DELAY_NORMAL, dist=10, loop=False)
define quake_long = Shake((0.5, 1.0, 0.5, 1.0), DELAY_LONG, dist=10, loop=False)
define quake_longest = Shake((0.5, 1.0, 0.5, 1.0), DELAY_LONGEST, dist=10, loop=False)


define eyeshutter_close_fastest = WipeTransition(WIPE_EYESHUTTER, DELAY_FASTEST, reverse=False, ramplen=4)
define eyeshutter_close_fast = WipeTransition(WIPE_EYESHUTTER, DELAY_FAST, reverse=False, ramplen=4)
define eyeshutter_close = WipeTransition(WIPE_EYESHUTTER, DELAY_NORMAL, reverse=False, ramplen=4)
define eyeshutter_close_long = WipeTransition(WIPE_EYESHUTTER, DELAY_LONG, reverse=False, ramplen=4)
define eyeshutter_close_longest = WipeTransition(WIPE_EYESHUTTER, DELAY_LONGEST, reverse=False, ramplen=4)

define eyeshutter_open_fastest = WipeTransition(WIPE_EYESHUTTER, DELAY_FASTEST, reverse=True, ramplen=4)
define eyeshutter_open_fast = WipeTransition(WIPE_EYESHUTTER, DELAY_FAST, reverse=True, ramplen=4)
define eyeshutter_open = WipeTransition(WIPE_EYESHUTTER, DELAY_NORMAL, reverse=True, ramplen=4)
define eyeshutter_open_long = WipeTransition(WIPE_EYESHUTTER, DELAY_LONG, reverse=True, ramplen=4)
define eyeshutter_open_longest = WipeTransition(WIPE_EYESHUTTER, DELAY_LONGEST, reverse=True, ramplen=4)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

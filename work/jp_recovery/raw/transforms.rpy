




init -3:

    transform cat_c:
        center
        yalign CAT_YALIGN

    transform cat_l:
        xalign CAT_L_XALIGN
        yalign CAT_YALIGN

    transform cat_r:
        xalign CAT_R_XALIGN
        yalign CAT_YALIGN

    transform ci_c:
        center

    transform ci_l:
        left
        xalign CI_L_XALIGN

    transform ci_r:
        right
        xalign CI_R_XALIGN

    transform std_c:
        center
        yanchor STD_YANCHOR

    transform std_l:
        left
        yanchor STD_YANCHOR

    transform std_cl:
        std_l
        xalign STD_CL_XALIGN

    transform std_r:
        right
        yanchor STD_YANCHOR

    transform std_cr:
        std_r
        xalign STD_CR_XALIGN

    transform std_offscreenleft:
        offscreenleft
        yanchor STD_YANCHOR

    transform std_offscreenright:
        offscreenright
        yanchor STD_YANCHOR

    transform offscreentop:
        top
        yanchor 1.0

    transform offscreenbottom:
        center
        yanchor 0.0

    transform xoffset(n):
        xoffset n

    transform yoffset(n):
        yoffset n

    transform additive(n):
        additive n

    transform pos(x, y):
        pos (x, y)

    transform alpha(n):
        alpha n

    transform align(x, y):
        align (x, y)

    transform xalign(n):
        xalign n

    transform yalign(n):
        yalign n

    transform zoom(n):
        zoom n

    transform xzoom(n):
        xzoom n

    transform yzoom(n):
        yzoom n

    transform smoke_slide(start_transform, speed, opacity, final_offset):
        start_transform
        alpha opacity
        subpixel True
        block:
            xoffset 0
            linear speed xoffset final_offset
            repeat

    transform smoke_lr(speed=50.0, opacity=1.0):
        smoke_slide(left, speed, opacity, -2730)

    transform smoke_rl(speed=50.0, opacity=1.0):
        smoke_slide(right, speed, opacity, 2730)




    transform rotable:
        xcenter 0.5
        ycenter 0.5
        subpixel True
        rotate_pad True

    transform rotate_loop_clockwise(speed):
        rotable

        block:
            linear speed rotate 360
            rotate 0
            repeat

    transform rotate_loop_counter_clockwise(speed):
        rotable

        block:
            linear speed rotate -360
            rotate 0
            repeat

    transform rollback_arrow:
        yalign (0.5)
        xoffset 0

    transform rollback_arrow_next:
        rollback_arrow

        block:
            easein 0.7 xoffset 10
            xoffset 0
            repeat

    transform rollback_arrow_prev:
        rollback_arrow

        block:
            easein 0.7 xoffset -10
            xoffset 0
            repeat

    transform game_menu_buttons_appear:
        alpha 0.0
        xoffset 200


        ease_back .5 alpha 1.0 xoffset 0





    transform game_menu_chapter_info_appear:
        alpha 0.0
        yoffset -200


        ease_back 1.0 alpha 1.0 yoffset 0





    transform game_menu_info_appear(delay=0):
        yanchor 0.0
        alpha 0.0
        xoffset -200


        pause delay
        ease_back .5 alpha 1.0 xoffset 0





    transform game_menu_tooltip_appear:
        alpha 0.0
        xoffset -30

        on show:
            easein .2 alpha 1.0 xoffset 0

        on hide:
            alpha 0.0
            xoffset -30

        on replaced:
            event show

    transform notify_appear:
        alpha 0
        xoffset -200

        on show:
            easein .3 alpha 1.0 xoffset 0
        on hide:
            easein .3 alpha 0.0 xoffset -200

    transform hud_appear:
        alpha 0
        xoffset 200

        on show:
            easein .3 alpha 1.0 xoffset 0
        on hide:
            easein .3 alpha 0.0 xoffset 200

    transform ctc_anime:
        yoffset 0

        block:
            easein CTC_ICON_ANIME_PAUSE * 0.5 yoffset 10
            linear CTC_ICON_ANIME_PAUSE * 0.5 yoffset 0
            repeat

    transform choice_show(delay_time=0.0):
        alpha 0.0
        xoffset 200

        pause delay_time
        easein 0.3 alpha 1.0 xoffset 0

    transform title_chara(x, y, start_delay=0.0, fade_time=1.0, y_offset=200):
        subpixel True
        xpos x
        ypos y
        yoffset y_offset
        alpha 0.0

        pause start_delay

        ease fade_time alpha 1.0 yoffset 0

    transform title_logo:
        xpos 720
        ypos 155
        alpha 0.0

        pause 2.0

        easein 1 alpha 1.0

    transform title_card(x, y, start_delay=0.0, slide_time=30, slide_offset=10):
        subpixel True
        xpos x
        ypos y
        alpha 0.0

        pause start_delay

        parallel:
            ease slide_time yoffset 0 knot slide_offset
            repeat

        parallel:
            easein 2 alpha 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

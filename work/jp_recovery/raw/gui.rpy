

init -2:

    style menu_button is button:
        idle_background Frame("gui/button01_idle.png", 4, 4)
        hover_background Frame("gui/button01_hover.png", 4, 4)
        selected_background Frame("gui/button01_selected.png", 4, 4)
        insensitive_background Frame("gui/button01_insensitive.png", 4, 4)


    style menu_button_text is button_text:
        font "gui/fonts/NotoSansCJKjp-Light.otf"
        align (0.5, 0.5)
        line_leading 0
        spacing 0
        kerning 1
        color "#eee"
        insensitive_color "#3d3d3d"
        outlines [(absolute(1), Color("#bbbbbb55"), absolute(0), absolute(0))]


init python:


    def message_background_displayable(st, at):
        return At(Frame("gui/main_message_bg.png", 0, 60, 0, 0, tile=True), alpha(persistent.message_alpha)), None
    style.window.background = DynamicDisplayable(message_background_displayable)

    style.window.yminimum = 260


    style.say_window.margin = (0, 0)




    style.window.left_padding = 200
    style.window.right_padding = 200
    style.window.top_padding = 30
    style.window.bottom_padding = 45






    style.say_vbox.spacing = 20
    style.say_vbox.xfill = True

    style.say_who_window.background = Frame("gui/main_message_line.png", 36, 0, yoffset = 28, ymaximum = 24)
    style.say_who_window.margin = (0, 0)
    style.say_who_window.xalign = 0.5
    style.say_who_window.xminimum = 280
    style.say_who_window.ysize = 45

    style.say_who_window.left_padding = 0
    style.say_who_window.right_padding = 0
    style.say_who_window.top_padding = 10
    style.say_who_window.bottom_padding = 0







    style._default.font = "gui/fonts/MTLc3m.ttf"


    style.default.font = "gui/fonts/NotoSansCJKjp-Regular.otf"



    style.default.size = 20

    style.default.language = "japanese-strict"


    style.say_label.bold = False
    style.say_label.size = 20
    style.say_label.font = "gui/fonts/NotoSansCJKjp-Bold.otf"
    style.say_label.outlines = [(2, "#00000066", 0, 0)]
    style.say_label.kerning = 1
    style.say_label.line_spacing = 0
    style.say_label.first_indent = 0
    style.say_label.line_leading = 0
    style.say_label.layout = "nobreak"  
    style.say_label.xalign = 0.5


    style.say_dialogue.size = 24
    style.say_dialogue.color = config.default_text_color
    style.say_dialogue.font = "gui/fonts/mgenplus-2pp-regular.ttf"
    style.say_dialogue.outlines = [(1, "#00000099", 1, 1)]
    style.say_dialogue.kerning = 1
    style.say_dialogue.line_spacing = 5
    style.say_dialogue.first_indent = 0
    style.say_dialogue.rest_indent = 15
    style.say_dialogue.line_leading = 0
    style.say_dialogue.layout = "tex"


    style.ruby_text.size = 12
    style.ruby_text.yoffset = -28
    style.ruby_text.color = style.say_dialogue.color


    style.vscrollbar.top_bar = None
    style.vscrollbar.bottom_bar = None
    style.vscrollbar.thumb = "gui/scrollbar_idle.png"
    style.vscrollbar.xsize = 5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

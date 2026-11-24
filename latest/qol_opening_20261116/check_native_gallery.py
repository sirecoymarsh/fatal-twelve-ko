from pathlib import Path
p=Path(__file__).resolve().parent/'fixture_probe.rpy'
s=p.read_text('utf8')
a=s.index('                b = visible.buttons["01"]');b=s.index('                _b_check(not renpy.seen_image',a)
s=s[:a]+'''                renpy.show_screen("f12_qa_gallery_timer")
                visible.show(visible.buttons["01"].index, 1)
                renpy.hide_screen("f12_qa_gallery_timer")
                renpy.hide_screen("_gallery")
                result["milk_gallery"] = _b_os.path.join(root, "milk_gallery.png")
                _b_check(_b_os.path.isfile(result["milk_gallery"]), "gallery did not render")
'''+s[b:]
s=s.replace('                renpy.hide_screen("preferences")\\n                F12BonusSetting(True)()', '                renpy.get_widget("preferences", "f12_bonus_open_button").action()\\n                renpy.hide_screen("preferences")').replace('\\\\n','\\n')
a=s.index('label f12_bonus_verify_replay:')
s=s[:a]+'''    def _b_still_gallery():
        _b_check(renpy.screenshot(_b_os.path.join(_b_os.environ["F12_QA_ROOT"], "milk_gallery.png")), "screenshot")

screen f12_qa_gallery_timer():
    zorder 500
    timer .65 action [Function(_b_still_gallery), Return("return")]

'''+s[a:]
p.write_text(s,'utf8')
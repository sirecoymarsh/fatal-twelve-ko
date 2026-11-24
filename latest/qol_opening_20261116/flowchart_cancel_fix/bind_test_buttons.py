from pathlib import Path
p=Path(__file__).resolve().parent/'probe.rpy'
s=p.read_text('utf8')
old='''        b = renpy.get_widget("preferences", key)
        _fq_expect(b is not None, key)
        renpy.display.behavior.run(b.action)'''
new='''        _fq_expect(renpy.get_widget("preferences", key) is not None, key)
        matches = []
        def bind(d):
            ac = getattr(d, "action", None)
            if isinstance(ac, F12BonusSetting) and ac.enabled == enabled:
                matches.append(ac)
        renpy.get_screen("preferences").visit_all(bind)
        _fq_expect(len(matches)==1, ("bound system button", key, len(matches)))
        renpy.display.behavior.run(matches[0])'''
assert s.count(old)==1;s=s.replace(old,new)
old='''        renpy.display.behavior.run(button.action)
        _fq_pause()'''
new='''        letters=[]
        def read_label(d):
            if isinstance(d, renpy.text.text.Text):
                letters.extend(x for x in d.text if isinstance(x,basestring))
        button.visit_all(read_label)
        _fq_expect((u"전체 개방 취소" if s.scope["fc_reveal"] else u"플로우 차트 전체 개방") in letters,("chart button caption",letters))
        renpy.display.behavior.run(button.action)
        _fq_pause()'''
assert s.count(old)==1
p.write_text(s.replace(old,new),'utf8')

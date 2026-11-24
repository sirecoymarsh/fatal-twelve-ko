"""Maintain the build sources and produce the overlay used by this fix."""
from pathlib import Path
from types import ModuleType
import hashlib, os, shutil, json, sys, textwrap
HERE=Path(__file__).resolve().parent
HISTORY=HERE.parent
BASE=HISTORY.parent
GAME=BASE/'runtime_review/game'
BUILD=HERE/'build'
PAYLOAD=HERE/'payload'
GENERATED=HISTORY/'delivery'
def sha(p):
    with open(p,'rb') as file:return hashlib.file_digest(file,'sha256').hexdigest()
def one(s,a,b):
    assert s.count(a)==1,repr(a)
    return s.replace(a,b)
def generate():
    BUILD.mkdir(parents=True,exist_ok=True);PAYLOAD.mkdir(exist_ok=True)
    # Keep the builder valid for both an original chart and a previously enhanced one.
    g=(HISTORY/'build_bonus.py').read_text('utf8')
    a=g.index("    if 'f12_bonus_run_preview' in chart:");b=g.index("    (OUT/'f12_flowchart.rpy')",a)
    transformations=g[g.index("    chart=replace_once(chart,'fc_reveal",a):b]
    shared=(HERE/'chart_helpers.txt').read_text('utf8').strip('\n')+'\n\n'
    edits=[
        ('    def f12_fc_end_open(e):',shared+'    def f12_fc_end_open(e):',1),
        ('    def f12_fc_end_open(e):\n        if f12_bonus_enabled():','    def f12_fc_end_open(e):\n        if f12_fc_bonus_preview():',1),
        ('return f12_bonus_enabled() or f12_fc_done(', 'return f12_fc_bonus_preview() or f12_fc_done(',1),
        ('and (f12_bonus_enabled() or f12_fc_done(', 'and (f12_fc_bonus_preview() or f12_fc_done(',1),
        ('fc_reveal = f12_bonus_enabled() or bool(persistent.f12_fc_reveal)', 'fc_reveal = f12_fc_revealed()',3),
        ('                selected fc_reveal\n                action ToggleField(persistent, "f12_fc_reveal")',
         '                id "f12_fc_reveal_toggle"\n                selected fc_reveal\n                action Function(f12_fc_set_revealed, not fc_reveal)',3),
        ('        fc_selcol = fc_cols[sel]',
         '        if not fc_opened[fc_cols[sel]["key"]]:\n            fc_fallback = f12_fc_default_sel(fc_mode)\n            if fc_fallback != sel:\n                sel = fc_fallback\n                f12_fc_scroll(fc_adj, sel)\n        fc_selcol = fc_cols[sel]',3),
        ('text fc_selcol["short"] pos (20, 290)','text (fc_selcol["short"] if fc_opened[fc_selcol["key"]] else u"？？？") pos (20, 290)',3),
        ('text fc_selcol["sub"] pos (20 +','text (fc_selcol["sub"] if fc_opened[fc_selcol["key"]] else u"") pos (20 +',3),
    ]
    # The generator's helpers are written as source for an ordinary developer rebuild.
    # Keep the multiline passages readable rather than embedding backslash-escaped code.
    code="    if 'f12_bonus_run_preview' not in chart:\n"+textwrap.indent(transformations,'    ')
    code+="    if '    def f12_fc_revealed():' not in chart:\n"
    def literal(value):
        return "'''"+value+"'''" if '\n' in value else repr(value)
    for old,new,n in edits:
        code+="        chart=replace_once(chart, "+literal(old)+", "+literal(new)+", "+str(n)+")\n"
    g=g[:a]+code+g[b:]
    (BUILD/'build_bonus.py').write_text(g,'utf8')
    source=(HISTORY/'bonus_functions.txt').read_text('utf8')
    source=one(source,'            renpy.game.persistent.f12_bonus_open = self.enabled\n            renpy.save_persistent()',
        '            renpy.game.persistent.f12_bonus_open = self.enabled\n            f12_fc_set_revealed(self.enabled)')
    (BUILD/'bonus_functions.txt').write_text(source,'utf8')
    shutil.copyfile(HISTORY/'settings_row.txt',BUILD/'settings_row.txt')
    builder=ModuleType('build_chart');builder.__file__=str(BUILD/'build_bonus.py')
    exec(compile(g,builder.__file__,'exec'),builder.__dict__)
    builder.BASE=BASE;builder.GAME=GAME;builder.OUT=PAYLOAD;builder.HERE=BUILD
    before={}
    for n in ['f12_bonus_access.rpy','f12_bonus_access.rpyc','f12_flowchart.rpy','f12_flowchart.rpyc']:
        before[n]=sha(GAME/n)
    # Verify the current installed source matches the just-completed binary release.
    old_report=json.loads((HISTORY/'install/INSTALL.json').read_text('utf8'))
    old={f['path']:f['after'] for f in old_report['files'] if f['path'] in before}
    assert old==before
    builder.build()
    (HERE/'baseline.json').write_text(json.dumps(before,indent=2),'utf8')
    # The same generator can regenerate from the original chart, the old enhancement,
    # or its current output. This prevents restoring the stuck condition on rebuild.
    archive=HISTORY/'install/before'
    builder.GAME=BUILD/'original';builder.GAME.mkdir(exist_ok=True)
    for src in (archive/'f12_flowchart.rpy', GAME/'f12_korean_bootstrap.rpy'):
        shutil.copy2(src,builder.GAME/src.name)
    builder.OUT=BUILD/'origin_build';builder.build()
    for n in ('f12_flowchart.rpy','f12_bonus_access.rpy'):
        assert sha(builder.OUT/n)==sha(PAYLOAD/n),n
    shutil.copy2(PAYLOAD/'f12_flowchart.rpy',builder.GAME/'f12_flowchart.rpy')
    builder.OUT=BUILD/'rebuild';builder.build()
    assert sha(builder.OUT/'f12_flowchart.rpy')==sha(PAYLOAD/'f12_flowchart.rpy')
    print('Generated identical scripts from original, installed and corrected source.',flush=True)
if __name__=='__main__':generate()
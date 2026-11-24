"""Generate the two shipping sources against the local game's original screen definitions."""
from pathlib import Path
import textwrap,re,hashlib,json
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
GAME=BASE/'runtime_review/game'
OUT=HERE/'delivery'
def replace_once(s,old,new,count=1):
    assert s.count(old)==count,(old,s.count(old),count)
    return s.replace(old,new)
def block(s,name):
    a=s.index('screen '+name);b=re.search(r'^(?:init |screen |\Z)',s[a+1:],re.M)
    return s[a:a+1+b.start()].strip('\n')
def build():
    OUT.mkdir(exist_ok=True)
    system=(BASE/'work/extracted/system/screens.rpy').read_text('utf-8-sig')
    main=block(system,'main_menu(')
    main=replace_once(main,'SensitiveIf(not config.is_trial and','SensitiveIf((f12_bonus_enabled() and not config.is_trial and not config.lock_extra) or (not config.is_trial and')
    main=replace_once(main,'persistent.MIHARU_clear)]','persistent.MIHARU_clear))]')
    extra=block(system,'extra(')
    extra=replace_once(extra,'add gallery.make_button(', 'add f12_bonus_gallery_for_view().make_button(')
    extra=replace_once(extra,'Function(grant_achievement,','Function(f12_bonus_gallery_achievement,',2)
    pat=r'action \[Replay\("([^"]+)"(?:, (\{.*?\}))?\), SensitiveIf\(persistent\.(\w+)\)\]'
    repl=lambda m: 'action f12_bonus_replay("'+m[1]+'", persistent.'+m[3]+(', '+m[2] if m[2] else '')+')'
    extra,n=re.subn(pat,repl,extra)
    assert n==23,n
    preferences=block(system,'preferences(')
    start=preferences.index('            if config.developer:')
    end=preferences.index('        elif current_tab == "sound":',start)
    preferences=preferences[:start]+preferences[end:]
    rows=(HERE/'settings_row.txt').read_text('utf8').rstrip()
    rows=rows.replace('                action F12BonusSetting(True)','                id "f12_bonus_open_button"\n                action F12BonusSetting(True)')
    rows=rows.replace('                action F12BonusSetting(False)','                id "f12_bonus_cancel_button"\n                action F12BonusSetting(False)')
    preferences+='\n\n    if current_tab == "system":\n        use f12_patch_language_selector\n'+textwrap.indent(rows,'    ')
    header=(HERE/'bonus_functions.txt').read_text('utf8')
    header+='\n    if _f12_sync_language_selector in config.interact_callbacks:\n        config.interact_callbacks.remove(_f12_sync_language_selector)\n'
    output=header+'\n\ninit 10:\n\n'+textwrap.indent('\n\n'.join([preferences,main,extra]),'    ')+'\n'
    (OUT/'f12_bonus_access.rpy').write_text(output,'utf8')
    path=GAME/'f12_flowchart.rpy'
    chart=path.read_text('utf-8-sig')
    if 'f12_bonus_run_preview' not in chart:
        chart=replace_once(chart,'fc_reveal = bool(persistent.f12_fc_reveal)','fc_reveal = f12_bonus_enabled() or bool(persistent.f12_fc_reveal)',3)
        chart=replace_once(chart,'def f12_fc_end_open(e):\n','def f12_fc_end_open(e):\n        if f12_bonus_enabled():\n            return True\n')
        chart=replace_once(chart,'return f12_fc_done(F12_FC_CHIPMAP.get((self.colk, self.file, self.sid)))','return f12_bonus_enabled() or f12_fc_done(F12_FC_CHIPMAP.get((self.colk, self.file, self.sid)))')
        chart=replace_once(chart,'and _F12FCState.target is not None and f12_fc_done(F12_FC_CHIPMAP.get((self.colk, self.file, self.sid)))','and _F12FCState.target is not None and (f12_bonus_enabled() or f12_fc_done(F12_FC_CHIPMAP.get((self.colk, self.file, self.sid))))')
        chart=replace_once(chart,'            snap = f12_fc_persist_snapshot()','            return f12_bonus_run_preview(self.play_scene)\n\n        def play_scene(self):\n            snap = f12_fc_persist_snapshot()')
        # Allow changing the user's access preference from within a chart replay.
        chart=replace_once(chart,'k in ("_preferences", "_changed", "_version")','k in ("_preferences", "_changed", "_version", "f12_bonus_open")')
    if '    def f12_fc_revealed():' not in chart:
        chart=replace_once(chart, '    def f12_fc_end_open(e):', '''    def f12_fc_revealed():
        # Existing saves may have an explicit chart choice, including False.
        choice = renpy.game.persistent.f12_fc_reveal
        if choice is None:
            return f12_bonus_enabled()
        return bool(choice)

    def f12_fc_set_revealed(reveal):
        renpy.game.persistent.f12_fc_reveal = bool(reveal)
        renpy.save_persistent()

    def f12_fc_bonus_preview():
        return f12_bonus_enabled() and f12_fc_revealed()

    def f12_fc_end_open(e):''', 1)
        chart=replace_once(chart, '''    def f12_fc_end_open(e):
        if f12_bonus_enabled():''', '''    def f12_fc_end_open(e):
        if f12_fc_bonus_preview():''', 1)
        chart=replace_once(chart, 'return f12_bonus_enabled() or f12_fc_done(', 'return f12_fc_bonus_preview() or f12_fc_done(', 1)
        chart=replace_once(chart, 'and (f12_bonus_enabled() or f12_fc_done(', 'and (f12_fc_bonus_preview() or f12_fc_done(', 1)
        chart=replace_once(chart, 'fc_reveal = f12_bonus_enabled() or bool(persistent.f12_fc_reveal)', 'fc_reveal = f12_fc_revealed()', 3)
        chart=replace_once(chart, '''                selected fc_reveal
                action ToggleField(persistent, "f12_fc_reveal")''', '''                id "f12_fc_reveal_toggle"
                selected fc_reveal
                action Function(f12_fc_set_revealed, not fc_reveal)''', 3)
        chart=replace_once(chart, '        fc_selcol = fc_cols[sel]', '''        if not fc_opened[fc_cols[sel]["key"]]:
            fc_fallback = f12_fc_default_sel(fc_mode)
            if fc_fallback != sel:
                sel = fc_fallback
                f12_fc_scroll(fc_adj, sel)
        fc_selcol = fc_cols[sel]''', 3)
        chart=replace_once(chart, 'text fc_selcol["short"] pos (20, 290)', 'text (fc_selcol["short"] if fc_opened[fc_selcol["key"]] else u"？？？") pos (20, 290)', 3)
        chart=replace_once(chart, 'text fc_selcol["sub"] pos (20 +', 'text (fc_selcol["sub"] if fc_opened[fc_selcol["key"]] else u"") pos (20 +', 3)
    (OUT/'f12_flowchart.rpy').write_text(chart,'utf-8-sig' if path.read_bytes().startswith(b'\xef\xbb\xbf') else 'utf8')
    (HERE/'feature_source.json').write_text(json.dumps({'screen_source':str(BASE/'work/extracted/system/screens.rpy'),'before_chart':hashlib.sha256(path.read_bytes()).hexdigest(),'native_replay_variants':n},indent=2))
if __name__=='__main__':build()
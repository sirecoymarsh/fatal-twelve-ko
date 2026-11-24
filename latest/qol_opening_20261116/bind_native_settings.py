from pathlib import Path
p=Path(__file__).resolve().parent
q=p/'build_bonus.py';s=q.read_text('utf8')
a=s.index('    selector=block(');b=s.index("    (OUT/'f12_bonus_access",a)
s=s[:a]+'''    preferences=block(system,'preferences(')
    start=preferences.index('            if config.developer:')
    end=preferences.index('        elif current_tab == "sound":',start)
    preferences=preferences[:start]+preferences[end:]
    rows=(HERE/'settings_row.txt').read_text('utf8').rstrip()
    rows=rows.replace('                action F12BonusSetting(True)','                id "f12_bonus_open_button"\\\\n                action F12BonusSetting(True)')
    rows=rows.replace('                action F12BonusSetting(False)','                id "f12_bonus_cancel_button"\\\\n                action F12BonusSetting(False)')
    preferences+='\\\\n\\\\n    if current_tab == "system":\\\\n        use f12_patch_language_selector\\\\n'+textwrap.indent(rows,'    ')
    header=(HERE/'bonus_functions.txt').read_text('utf8')
    header+='\\\\n    if _f12_sync_language_selector in config.interact_callbacks:\\\\n        config.interact_callbacks.remove(_f12_sync_language_selector)\\\\n'
    output=header+'\\\\n\\\\ninit 10:\\\\n\\\\n'+textwrap.indent('\\\\n\\\\n'.join([preferences,main,extra]),'    ')+'\\\\n'
'''+s[b:]
# Generated source uses Python newline escapes, not literal backslashes.
s=s.replace('\\\\n','\\n')
q.write_text(s,'utf8')
q=p/'fixture_probe.rpy';s=q.read_text('utf8').replace('renpy.get_screen("f12_patch_language_selector") is not None','renpy.get_widget("preferences","f12_bonus_open_button") is not None');q.write_text(s,'utf8')

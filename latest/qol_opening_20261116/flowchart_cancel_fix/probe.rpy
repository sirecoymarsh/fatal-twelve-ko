# Checks the game's actual screens and the actions bound to their buttons.
init 990 python:
    import os as _fq_os, json as _fq_json, traceback as _fq_tb
    config.label_overrides["start"] = "f12_chart_check_start"
    config.window_title = "Fatal Twelve isolated flowchart test"
    config.autosave_on_quit = False
    config.autosave_on_choice = False
    _preferences.fullscreen = False

    def _fq_expect(test, detail):
        if not test:
            raise AssertionError(detail)

    def _fq_pause():
        renpy.pause(.09, hard=True)

    def _fq_open(name):
        renpy.show_screen(name)
        _fq_pause()
        return renpy.get_screen(name)

    def _fq_state(name):
        sc = renpy.get_screen(name).scope
        return {"view":bool(sc["fc_reveal"]), "selected":sc["sel"],
                "open_weeks":sum(bool(row[1]) for row in sc["fc_weeks"]),
                "open_columns":sum(bool(v) for v in sc["fc_opened"].values()),
                "selected_key":sc["fc_selcol"]["key"]}

    def _fq_toggle(name):
        s = renpy.get_screen(name)
        button = renpy.get_widget(name,"f12_fc_reveal_toggle")
        if button is None:
            found = []
            def inspect(d):
                ac = getattr(d,"action",None)
                if isinstance(ac, ToggleField) and ac.field == "f12_fc_reveal":
                    found.append(d)
            s.visit_all(inspect)
            _fq_expect(len(found)==1, ("old bound chart toggle",len(found)))
            button=found[0]
        letters=[]
        def read_label(d):
            if isinstance(d, renpy.text.text.Text):
                letters.extend(x for x in d.text if isinstance(x,basestring))
        button.visit_all(read_label)
        _fq_expect((u"전체 개방 취소" if s.scope["fc_reveal"] else u"플로우 차트 전체 개방") in letters,("chart button caption",letters))
        renpy.display.behavior.run(button.action)
        _fq_pause()

    def _fq_system(enabled):
        _fq_open("preferences")
        key = "f12_bonus_open_button" if enabled else "f12_bonus_cancel_button"
        _fq_expect(renpy.get_widget("preferences", key) is not None, key)
        matches = []
        def bind(d):
            ac = getattr(d, "action", None)
            if isinstance(ac, F12BonusSetting) and ac.enabled == enabled:
                matches.append(ac)
        renpy.get_screen("preferences").visit_all(bind)
        _fq_expect(len(matches)==1, ("bound system button", key, len(matches)))
        renpy.display.behavior.run(matches[0])
        _fq_pause()
        renpy.hide_screen("preferences")

    def _fq_access():
        c=F12_FC_COLS[0]; earned=c["chips"][0]
        futurecol=F12_FC_COLS[-1]; future=futurecol["chips"][-1]
        return [bool(F12FCReplay(earned["file"],earned["sid"],c["colk"]).get_sensitive()),
                bool(F12FCReplay(future["file"],future["sid"],futurecol["colk"]).get_sensitive()),
                bool(f12_fc_end_open([None,None,"TRUE_clear"]))]

    def _fq_select_last(name):
        s=renpy.get_screen(name)
        s.scope["sel"]=len(F12_FC_COLS)-1
        renpy.restart_interaction()
        _fq_pause()
        _fq_expect(_fq_state(name)["selected"]==len(F12_FC_COLS)-1,"could not select future column")

    def _fq_check_closed(name):
        rd=_fq_state(name)
        _fq_expect(not rd["view"] and rd["open_weeks"]==1 and rd["selected"]==0,("closed chart",rd))
        _fq_expect(_fq_access()==[True,False,False],("chart playback",_fq_access()))
        _fq_expect(renpy.seen_image("ecg coffee sip") and not gallery.Action("02"),"earned CG changed")
        _fq_expect(not renpy.game.persistent.TRUE_clear,"ending history changed")
        return rd

    def _fq_cycle(name):
        _fq_open(name)
        opened=_fq_state(name)
        _fq_expect(opened["view"] and opened["open_weeks"]==13 and _fq_access()==[True,True,True],("open chart",opened,_fq_access()))
        _fq_select_last(name)
        _fq_toggle(name)
        shut=_fq_check_closed(name)
        _fq_expect(f12_bonus_enabled() and f12_bonus_gallery_for_view().Action("02"),"chart-only cancel changed gallery")
        _fq_expect(renpy.get_widget(name,"f12_fc_reveal_toggle") is not None,"toggle missing")
        return {"before":opened, "after_cancel":shut}

    def _fq_replay_ui():
        name="f12_flowchart_replay"
        previous=_fq_cycle(name)
        c=F12_FC_COLS[-1];ch=c["chips"][-1]
        _fq_expect(not F12FCChain(ch["file"],ch["sid"],c["colk"]).get_sensitive(),"unread replay chain escaped the chart lock")
        _F12FCState.fq_replay_result=previous
        renpy.hide_screen(name)

    def _fq_probe():
        phase=_fq_os.environ["F12_CHART_PHASE"]; proof={"phase":phase,"engine":renpy.version_only}
        p=renpy.game.persistent
        try:
            renpy.change_language("korean")
            if phase=="old_setup":
                _fq_system(True)
                p.f12_fc_reveal=False
                p.TRUE_clear=False
                c=F12_FC_COLS[0];p._seen_translates.add(c["chips"][0]["ends"][0])
                renpy.show("ecg coffee sip")
                renpy.hide("ecg")
                renpy.save_persistent()
                proof["saved_pair"]=[f12_bonus_enabled(),p.f12_fc_reveal]
                _fq_expect(proof["saved_pair"]==[True,False],"legacy fixture")
            elif phase=="old_reopen":
                name="f12_flowchart";_fq_open(name)
                _fq_expect([f12_bonus_enabled(),p.f12_fc_reveal]==[True,False],"loaded legacy pair")
                proof["before"]=_fq_state(name)
                _fq_toggle(name)
                proof["first_cancel"]=[_fq_state(name),p.f12_fc_reveal]
                _fq_toggle(name)
                proof["second_click"]=[_fq_state(name),p.f12_fc_reveal]
                _fq_expect(proof["before"]["view"] and proof["first_cancel"][0]["view"] and proof["second_click"][0]["view"] and p.f12_fc_reveal is False,"reported failure did not reproduce")
                renpy.save_persistent()
            elif phase=="old_save_fixed":
                name="f12_flowchart";_fq_open(name)
                proof["old_cancel_applied_on_first_start"]=_fq_check_closed(name)
                _fq_expect(f12_bonus_enabled() and f12_bonus_gallery_for_view().Action("02"),"independent gallery access")
                # A profile that has never chosen a chart setting still inherits Extras.
                p.f12_fc_reveal=None
                _fq_expect(f12_fc_revealed(),"missing legacy field lost bonus default")
                _fq_system(True)
                _fq_expect(p.f12_fc_reveal is True and f12_bonus_enabled(),"global action did not set chart default")
            elif phase=="cancel_after_reopen":
                _fq_expect(f12_bonus_enabled() and p.f12_fc_reveal is True,"restarted in wrong state")
                proof["extra"]=_fq_cycle("f12_flowchart")
                _fq_toggle("f12_flowchart")
                renpy.hide_screen("f12_flowchart")
                proof["ingame"]=_fq_cycle("f12_flowchart_ingame")
                _fq_toggle("f12_flowchart_ingame")
                renpy.hide_screen("f12_flowchart_ingame")
                c=F12_FC_COLS[0];start=c["chips"][0]
                _F12FCState.target=(start["file"],start["sid"])
                _F12FCState.target_colk=c["colk"]
                try:
                    f12_bonus_run_preview(lambda: renpy.call_replay("f12_chart_check_replay",{}))
                    proof["replay"]=_F12FCState.fq_replay_result
                finally:
                    _F12FCState.target=None
                    _F12FCState.target_colk=None
                _fq_expect(p.f12_fc_reveal is False and f12_bonus_enabled(),"replay restored the old chart choice")
            elif phase=="verify_reclosed":
                name="f12_flowchart";_fq_open(name)
                proof["after_second_restart"]=_fq_check_closed(name)
                _fq_expect(f12_bonus_enabled() and p.f12_fc_reveal is False,"cancellation lost on restart")
                _fq_toggle(name)
                _fq_system(False)
                _fq_open(name)
                proof["system_cancel_after_local_open"]=_fq_check_closed(name)
                _fq_expect(not f12_bonus_enabled() and f12_bonus_gallery_for_view() is gallery,"system cancel failed")
                _fq_toggle(name)
                _fq_expect(_fq_state(name)["view"] and _fq_access()==[True,False,False],"standalone spoiler view changed playback access")
                _fq_toggle(name)
                _fq_check_closed(name)
            else:
                raise ValueError(phase)
            proof["status"]="PASS"
        except Exception:
            proof["status"]="FAIL";proof["error"]=_fq_tb.format_exc()
        with open(_fq_os.path.join(_fq_os.environ["F12_CHART_QA"],phase+".json"),"wb") as f:
            f.write(_fq_json.dumps(proof,ensure_ascii=False,indent=2).encode("utf8"))

label f12_chart_check_start:
    $ _fq_probe()
    $ renpy.quit()

label f12_chart_check_replay:
    $ _fq_replay_ui()
    $ renpy.end_replay()
    return
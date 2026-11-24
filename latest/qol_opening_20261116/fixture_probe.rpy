init 950 python:
    import os as _b_os, json as _b_json, hashlib as _b_hash, traceback as _b_traceback
    config.window_title = "Fatal Twelve isolated bonus verification"
    config.label_overrides["start"] = "f12_bonus_verify_start"
    config.autosave_on_quit = False
    config.autosave_on_choice = False
    _preferences.fullscreen = False

    def _b_check(ok, reason):
        if not ok:
            raise AssertionError(reason)

    def _b_capture(name):
        import os
        renpy.pause(.34, hard=True)
        path = os.path.join(os.environ["F12_QA_ROOT"], name + ".png")
        _b_check(renpy.screenshot(path), name)
        return path

    def _b_verify():
        root = _b_os.environ["F12_QA_ROOT"]
        phase = _b_os.environ.get("F12_QA_PHASE", "functional")
        result = {"phase":phase, "engine": renpy.version_only}
        try:
            if phase == "reopen":
                _b_check(f12_bonus_enabled(), "reopened setting")
                F12BonusSetting(False)()
                _b_check(gallery.Action("01") and not gallery.Action("02"), "genuine gains after restart")
                result["stored_switch_and_genuine_gains"] = True
            else:
                renpy.change_language("korean")
                p = renpy.game.persistent
                F12BonusSetting(False)()
                for image in ("ecg coffee sip", "ecg coffee ole", "ecg miharu nor"):
                    p._seen_images.pop(tuple(image.split()), None)
                _b_check(not bool(gallery.Action("01")), "fresh native gallery")
                renpy.show_screen("preferences")
                renpy.pause(.35, hard=True)
                _b_check(renpy.get_widget("preferences","f12_bonus_open_button") is not None, "settings/system overlay")
                result["settings"] = _b_capture("settings")
                renpy.hide_screen("preferences")
                F12BonusSetting(True)()
                visible = f12_bonus_gallery_for_view()
                result["cg_groups"] = len(visible.buttons)
                result["cg_variants"] = sum(len(b.images) for b in visible.button_list)
                _b_check(all(visible.Action(k) for k in gallery.buttons), "locked gallery group")
                _b_check(all(i.check_unlock(False) for b in visible.button_list for i in b.images), "locked gallery variant")
                _b_check(not gallery.Action("01"), "gallery wrote original flags")
                renpy.show_screen("extra")
                result["gallery"] = _b_capture("gallery_open")
                renpy.hide_screen("extra")
                fp = renpy.loader.load("images/ecg/ecg coffee ole.png")
                result["milk_sha256"] = _b_hash.sha256(fp.read()).hexdigest()
                fp.close()
                _b_check(result["milk_sha256"] == "8da22536064f8945ffeb65825baf2ecc649ecf281652c918709344afb7128476", "wrong language raster")
                # Capture the actual gallery viewer and its native registered second variant.
                renpy.show_screen("f12_qa_gallery_timer")
                visible.show(visible.buttons["01"].index, 1)
                renpy.hide_screen("f12_qa_gallery_timer")
                renpy.hide_screen("_gallery")
                result["milk_gallery"] = _b_os.path.join(root, "milk_gallery.png")
                _b_check(_b_os.path.isfile(result["milk_gallery"]), "gallery did not render")
                _b_check(not renpy.seen_image("ecg coffee ole"), "preview counted as earned")
                # Normal story-driven acquisition while bonus access is enabled.
                renpy.show("ecg coffee sip")
                renpy.hide("ecg")
                _b_check(gallery.Action("01") and not gallery.Action("02"), "ordinary acquisition")
                act = f12_bonus_replay("sentei7", False, {"flags_route_B": True})
                _b_check(act.get_sensitive() and act.scope["flags_route_B"], "variant replay scope")
                F12BonusReplay("f12_bonus_verify_replay", {}, locked=False)()
                _b_check(not renpy.seen_image("ecg miharu nor") and not p.f12_qa_preview_clear, "replay polluted progress")
                _b_check(f12_fc_end_open([None,None,"TRUE_clear"]), "ending movie locked")
                num_chips = sum(len(c["chips"]) for c in F12_FC_COLS)
                result["chart_nodes"] = num_chips
                _b_check(all(F12FCReplay(ch["file"],ch["sid"],c["colk"]).get_sensitive() for c in F12_FC_COLS for ch in c["chips"]), "chart access")
                F12BonusSetting(False)()
                _b_check(gallery.Action("01") and not gallery.Action("02") and f12_bonus_gallery_for_view() is gallery, "cancel restore")
                _b_check(not f12_fc_end_open([None,None,"TRUE_clear"]), "movie still forced")
                F12BonusSetting(True)()
            result["status"] = "PASS"
        except Exception:
            result["status"]="FAIL"
            result["traceback"]=_b_traceback.format_exc()
        with open(_b_os.path.join(root,phase+".json"),"wb") as f:
            f.write(_b_json.dumps(result,ensure_ascii=False,indent=2).encode("utf8"))

    def _b_still_gallery():
        _b_check(renpy.screenshot(_b_os.path.join(_b_os.environ["F12_QA_ROOT"], "milk_gallery.png")), "screenshot")

screen f12_qa_gallery_timer():
    zorder 500
    timer .65 action [Function(_b_still_gallery), Return("return")]

label f12_bonus_verify_replay:
    scene ecg miharu nor
    $ persistent.f12_qa_preview_clear = True
    $ renpy.end_replay()
    return

label f12_bonus_verify_start:
    $ _b_verify()
    $ renpy.quit()

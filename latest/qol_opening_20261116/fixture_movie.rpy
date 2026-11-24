init 980 python:
    import os as _q_os, time as _q_time, json as _q_json, hashlib as _q_hash, traceback as _q_trace
    if _q_os.environ.get("F12_QA_PHASE") == "movie":
        config.label_overrides["start"] = "f12_movie_run"
        _f12_movie_result = {"seconds":[], "captures":[]}
        def _q_poll_movie():
            t = renpy.music.get_pos(channel="movie")
            if t is None:
                return
            t = float(t)
            times = _f12_movie_result["seconds"]
            if not times or t - times[-1] > .95:
                times.append(round(t,3))
            for when in [2.65, 48.0, 99.0]:
                existing = _f12_movie_result["captures"]
                if t >= when and not any(item["when"] == when for item in existing):
                    path = _q_os.path.join(_q_os.environ["F12_QA_ROOT"], "game_op_%03d.png" % int(when))
                    existing.append({"when":when, "position":t, "file":path, "saved":bool(renpy.screenshot(path))})
        config.periodic_callbacks.append(_q_poll_movie)

    def _q_play_op():
        res = _f12_movie_result
        root = _q_os.environ["F12_QA_ROOT"]
        try:
            renpy.change_language("korean")
            stream = renpy.loader.load("movies/OP.mkv")
            dig = _q_hash.sha256()
            while True:
                buf = stream.read(1<<20)
                if not buf:break
                dig.update(buf)
            stream.close()
            res["selected_file_sha256"] = dig.hexdigest()
            start = _q_time.time()
            f12_fc_play_movie("movies/OP.mkv")
            res["elapsed"] = _q_time.time()-start
            res["returned_from_movie"] = not bool(renpy.music.get_playing(channel="movie"))
            res["status"] = "PASS" if (res["elapsed"]>99 and res["seconds"] and max(res["seconds"])>100 and res["returned_from_movie"] and len(res["captures"])==3) else "CHECK"
        except Exception:
            res["status"]="FAIL"
            res["exception"]=_q_trace.format_exc()
        with open(_q_os.path.join(root,"movie.json"),"wb") as f:
            f.write(_q_json.dumps(res,indent=2).encode("utf8"))
label f12_movie_run:
    $ _q_play_op()
    $ renpy.quit()

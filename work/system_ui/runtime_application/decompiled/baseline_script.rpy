label audit_show_expression:

    show expression Text("to be continued...", size=50)
    return

label start:

    python:
        import json
        import os
        import traceback

        renpy.game.preferences.language = "korean"

        def audit_text(value, substitute):
            d = renpy.text.text.Text(value, substitute=substitute)
            return unicode(d.text[0])

        direct_actual = {
            "textbutton_japanese": audit_text('日本語', True),
            "textbutton_english": audit_text('English', True),
            "text_separator": audit_text(' - ', None),
            "python_text_continued": audit_text('to be continued...', None),
            "label_numeral_composed": audit_text('Numeral I', True),
        }

        direct_expected = {'textbutton_japanese': '일본어', 'textbutton_english': '영어', 'text_separator': ' - ', 'python_text_continued': '계속됩니다...'}
        base_expected = {'Quick save complete.': '빠른 저장 완료', 'Are you sure you want to delete this save?': '저장 데이터를 삭제하시겠습니까?', 'Are you sure you want to overwrite your save?': '저장 데이터를 덮어쓰시겠습니까?', 'Loading will lose unsaved progress.\nAre you sure you want to do this?': '저장 데이터를 불러오시겠습니까?', 'Are you sure you want to quit?': '게임을 종료하시겠습니까?', 'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.': '타이틀 화면으로 돌아가시겠습니까?', 'Image [index] of [count] locked.': '[count]개 중 [index]번 이미지는 잠겨 있습니다.', 'Saved screenshot as %s.': '스크린샷을 %s에 저장했습니다.'}
        base_actual = { }
        for k in base_expected:
            base_actual[k] = unicode(renpy.translation.translate_string(k))

        result = {
            "engine_version": unicode(renpy.version),
            "language": unicode(renpy.game.preferences.language),
            "direct_actual": direct_actual,
            "direct_expected": direct_expected,
            "base_actual": base_actual,
            "base_expected": base_expected,
            "direct_exact_four_pass": all(direct_actual[k] == direct_expected[k] for k in direct_expected),
            "numeral_composed_pass": direct_actual["label_numeral_composed"] == 'Numeral I',
            "base_eight_pass": all(base_actual[k] == base_expected[k] for k in base_expected),
        }
        result["all_pass"] = result["direct_exact_four_pass"] and result["numeral_composed_pass"] and result["base_eight_pass"]

        fn = os.path.join(config.basedir, "runtime_probe.json")
        f = open(fn, "wb")
        try:
            payload = json.dumps(result, ensure_ascii=True, indent=2)
        except Exception:
            payload = json.dumps({ "probe_exception": traceback.format_exc() })
        f.write(payload)
        f.write("\n")
        f.close()

    $ renpy.quit()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

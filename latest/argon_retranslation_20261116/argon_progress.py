"""Publish a local, automatically refreshing view of the translation ledger."""
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path
from story_context import put, save

KST=timezone(timedelta(hours=9))
NAMES={"queued":"전송 대기","request_in_flight":"아르곤 응답 대기","translating":"번역 중",
       "capacity_wait":"Google 처리 용량 대기","source_check":"출력 확인","pilot_returned":"첫 장면 확인",
       "completed":"전체 번역 저장 완료","paused":"중단됨","needs_review":"확인이 필요한 행이 남았습니다",
       "provider_error":"API 응답 확인 필요","worker_error":"실행 상태 확인 필요","preparing":"대기열 확인 중"}

def publish(path, status):
    save(path,status)
    total=status.get("total_rows",0);done=status.get("verified_rows",0)
    pct=100*done/total if total else 0
    def n(k):return f"{int(status.get(k,0) or 0):,}"
    stamp=datetime.now(KST).strftime("%m월 %d일 %H:%M:%S")
    current=escape(str(status.get("active_chunk") or status.get("last_chunk") or "대기"))
    sent=n("unique_rows_sent")
    msg=escape(str(status.get("message") or ""))
    next_at=status.get("next_attempt")
    if next_at:
        when=datetime.fromisoformat(next_at).astimezone(KST).strftime("%H:%M:%S")
        msg+=f"　다음 시도 {when}"
    stage=escape(NAMES.get(status.get("stage"),str(status.get("stage",""))))
    doc=f"""<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="6"><title>Fatal Twelve 번역 진행</title>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#f5f4f1;color:#222923;font:17px/1.6 "Malgun Gothic",system-ui,sans-serif}}main{{max-width:680px;margin:9vh auto;padding:32px}}h1{{font-size:25px;line-height:1.3;margin:0 0 25px}}.big{{font-size:clamp(38px,8vw,64px);font-weight:700;line-height:1.15;font-variant-numeric:tabular-nums}}progress{{width:100%;height:13px;accent-color:#346f52;margin:15px 0}}dl{{margin:20px 0}}dl div{{display:flex;justify-content:space-between;gap:16px;padding:9px 0;border-bottom:1px solid #cfd4ce}}dt,footer{{color:#555f59}}dd{{margin:0;font-variant-numeric:tabular-nums}}p{{margin:12px 0}}footer{{font-size:14px;margin-top:20px}}</style>
<main><h1>Fatal Twelve 번역 진행</h1><div class="big">{pct:.2f}%</div><progress max="{total}" value="{done}">{pct:.2f}%</progress>
<p><strong>{done:,} / {total:,}행 검증 완료</strong></p><dl>
<div><dt>기존 카본 번역</dt><dd>{n("carbon_rows")}행</dd></div><div><dt>아르곤에 전송한 고유 행</dt><dd>{sent} / {n("queued_for_argon")}행</dd></div>
<div><dt>아르곤 번역 검증 완료</dt><dd>{n("argon_rows")}행</dd></div><div><dt>남은 번역</dt><dd>{n("remaining_rows")}행</dd></div>
<div><dt>현재 상태</dt><dd>{stage} · {current}</dd></div></dl><p>{msg}</p><footer>한국시간 {stamp} 갱신</footer></main></html>"""
    put(path.with_name("진행.html"),doc)

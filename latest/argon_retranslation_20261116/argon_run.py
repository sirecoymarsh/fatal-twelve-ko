"""Resumable one-worker Argon translation from real AItranslator receipts."""
from collections import Counter, defaultdict, deque
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from html import escape
import json
import math
import msvcrt
import os
from pathlib import Path
import random
import re
import sys
import time
import zipfile
from argon_queue import (ROOT,STORY,MODEL,RECEIPTS,OUTPUT,MARKER,PROGRESS,
                         Translator,stopped,prepare,validated,validation_module,load,put,save,compact,digest,utc)
from argon_progress import publish
from story_context import PACK

def as_time(s):
    return datetime.fromisoformat(s.replace("Z","+00:00")).timestamp()

def as_iso(t):
    return datetime.fromtimestamp(t,timezone.utc).isoformat()


@contextmanager
def single_worker():
    with (ROOT/"runtime"/"worker.lock").open("a+b") as handle:
        handle.seek(0)
        try:msvcrt.locking(handle.fileno(),msvcrt.LK_NBLCK,1)
        except OSError:raise SystemExit("기존 아르곤 작업이 실행 중입니다.") from None
        try:yield
        finally:
            handle.seek(0)
            msvcrt.locking(handle.fileno(),msvcrt.LK_UNLCK,1)


class Run:
    def __init__(self):
        self.records,self.jobs,self.baseline,self.queue=prepare()
        self.source={r["id"]:r for r in self.records}
        self.valid=validation_module()
        self.service=Translator()
        self.allowed={c:set(ids) for c,ids in self.queue["jobs"].items()}
        self.old_ids={r["id"] for r in self.records if r["stable_id"] in self.baseline}
        self.done={};self.by_chunk=defaultdict(dict);self.problems={}
        self.held={};self.seen=set();self.uncertain=set();self.attempt_counts=Counter()
        self.fails=Counter();self.response_counts=Counter();self.tok=Counter()
        self.limits={};self.retry_seq=0;self.deadline=0.0;self.job_pause={}
        self.last={};self.fatal="";self.last_ok=None
        # One pending marker can survive power loss after the reply was saved.
        if MARKER.is_file():
            m=load(MARKER); dest=RECEIPTS/(m["ref"]+".json")
            if not dest.exists():
                save(dest, dict(m,finished=utc(),http_status=None,provider_status="delivery_unconfirmed",
                                  delivery="unconfirmed",model_version=None,finish_reason=None,usage={},visible_text=""))
            elif load(dest).get("request_sha256")!=m["request_sha256"]:
                raise ValueError("전송 기록과 기존 응답의 해시 불일치")
            MARKER.unlink()
        for path in sorted(RECEIPTS.glob("*.json")):
            self.apply(load(path),persist=False)
        for name,items in self.by_chunk.items():
            save(OUTPUT/(name+".json"),items)
        self.order=deque(self.queue["jobs"])
        self.default_limit=max(1,min(100,int(self.service.settings.get("chunk_size") or 100)))

    def apply(self, rec, persist=True):
        chunk=rec["chunk"]; ids=rec["ids"]; status=rec.get("http_status"); end=as_time(rec["finished"])
        if (rec.get("model_requested")!=MODEL or rec.get("guide_sha256")!=self.queue["guide_sha256"]
                or len(set(ids))!=len(ids) or not set(ids)<=self.allowed.get(chunk,set()) or set(ids)&self.old_ids):
            raise ValueError("아르곤 응답이 지정된 미번역 범위를 벗어났습니다.")
        self.last=rec;self.seen.update(ids);self.response_counts[str(status)]+=1
        usage=rec.get("usage") or {}
        for k in ("promptTokenCount","candidatesTokenCount","thoughtsTokenCount","cachedContentTokenCount"):
            self.tok[k]+=int(usage.get(k,0) or 0)
        key=rec["request_sha256"]
        if status in (408,429,500,502,503,504):
            self.retry_seq+=1;self.attempt_counts[key]+=1
            base=min(600,60*(2**min(self.retry_seq-1,4)))
            # Deterministic jitter lets a restart recover the original cooldown.
            sample=random.Random(rec["ref"]).uniform(0.9,1.0)
            self.deadline=end+max(base*sample,float(rec.get("retry_after") or 0))
            if self.attempt_counts[key]%3==0:
                self.job_pause[chunk]=max(self.deadline,end+900)
            return
        if status is None:
            self.uncertain.update(ids)
            for sid in ids:self.held[sid]="전송 후 수신 여부 미확인"
            return
        if status==401:
            self.service.auth.access="";self.attempt_counts["401"]+=1
            if self.attempt_counts["401"]>=2:self.fatal="선택된 프로젝트의 인증이 두 번 거절되었습니다."
            return
        if status!=200:
            self.fatal=f"HTTP {status} {rec.get('provider_status') or ''} · {rec.get('error_message') or ''}"
            return
        self.retry_seq=0;self.deadline=0;self.last_ok=rec["finished"]
        if rec.get("finish_reason") not in ("STOP","MAX_TOKENS"):
            for sid in ids:self.held[sid]="API 종료 사유 "+str(rec.get("finish_reason"))
            return
        ok,bad=validated(rec,self.source,self.valid)
        for sid,row in ok.items():
            if sid in self.done:
                if self.done[sid]["request_sha256"]!=row["request_sha256"]:
                    raise ValueError("완료한 ID에 별도 응답이 생겼습니다: "+sid)
                continue
            self.by_chunk[chunk][sid]=self.done[sid]=row;self.problems.pop(sid,None);self.held.pop(sid,None)
        for sid,issues in bad.items():
            if sid in self.done: continue
            self.problems[sid]=issues
            # A cut-off tail wasn't individually mistranslated; retry the remaining text in smaller groups.
            if issues!=["완전한 출력 행이 없음"] or len(ids)==1:
                self.fails[sid]+=1
            if self.fails[sid]>=3:self.held[sid]=" · ".join(issues)
        if rec.get("finish_reason")=="MAX_TOKENS" or (not ok and bad):
            self.limits[chunk]=max(1,len(ids)//2)
        if persist and ok:save(OUTPUT/(chunk+".json"),self.by_chunk[chunk])

    def state(self,stage,**extra):
        total=self.queue["total"];n=len(self.baseline)+len(self.done);last=self.last
        s={"stage":stage,"updated":utc(),"model":MODEL,"total_rows":total,"queued_for_argon":self.queue["rows_to_send"],
           "carbon_rows":len(self.baseline),"argon_rows":len(self.done),"verified_rows":n,"remaining_rows":total-n,
           "unique_rows_sent":len(self.seen),"not_yet_sent":self.queue["rows_to_send"]-len(self.seen),
           "http_responses":sum(v for k,v in self.response_counts.items() if k!="None"),
           "http_status_counts":dict(self.response_counts),"provider_tokens":dict(self.tok),
           "last_chunk":last.get("chunk"),"last_http":last.get("http_status"),"last_finish":last.get("finish_reason"),
           "last_returned_model":last.get("model_version"),"last_success":self.last_ok,"rows_needing_review":len(self.held),
           "source_guide_model":"gemini-4-carbon","guide_sha256":self.queue["guide_sha256"],
           "native_implementation":"AItranslator v1.11","worker_pid":os.getpid()}
        s.update(extra)
        publish(PROGRESS,s)
        return s

    def sleep_until(self,until,stage):
        self.state(stage,next_attempt=as_iso(until),message="다음 전송까지 한 작업만 대기합니다.")
        while time.time()<until and not stopped():
            time.sleep(min(5,max(0,until-time.time())))

    def choose(self):
        now=time.time(); deadlines=[]
        for _ in range(len(self.order)):
            name=self.order.popleft()
            missing=[sid for sid in self.queue["jobs"][name] if sid not in self.done and sid not in self.held]
            if not missing:continue
            if self.job_pause.get(name,0)>now:
                deadlines.append(self.job_pause[name]);self.order.append(name);continue
            # Finish a partly translated scene before moving to the next scene.
            self.order.appendleft(name)
            return name,missing[:self.limits.get(name,self.default_limit)],None
        return None,[],min(deadlines) if deadlines else None

    def finish(self):
        if self.held or len(self.done)!=self.queue["rows_to_send"]:
            save(ROOT/"확인_필요.json",{"ids":self.held,"issues":self.problems})
            self.state("needs_review",message="모든 나머지 행을 시도했습니다. 미확인 ID는 확인_필요.json에 기록했습니다.")
            return
        all_rows=[]; by_stable={}
        for r in self.records:
            row=self.baseline.get(r["stable_id"]) or self.done.get(r["id"])
            if not row or row["source_text_sha256"]!=r["source_text_sha256"] or row["source_jp"]!=r["source_jp"]:
                raise ValueError("최종 원문 행 불일치 "+r["id"])
            all_rows.append(row);by_stable[r["stable_id"]]=row
        if len(all_rows)!=len(by_stable) or len(all_rows)!=self.queue["total"]:raise ValueError("최종 고유 행 수")
        merged=ROOT/"Fatal_Twelve_한국어.jsonl";put(merged,"".join(compact(row)+"\n" for row in all_rows))
        packet=ROOT/"Fatal_Twelve_한국어_29패킷.zip";part=packet.with_suffix(".partial");files=[];order=[]
        with zipfile.ZipFile(part,"w",zipfile.ZIP_DEFLATED) as archive:
            for item in load(PACK/"MANIFEST.json")["packets"]:
                name=item["packet"];raw=(PACK/name).read_bytes()
                if digest(raw)!=item["packet_initial_sha256"]:raise ValueError("원문 파일 변경 "+name)
                lines=[]
                for line in raw.splitlines():
                    if not line.strip():continue
                    src=json.loads(line);row=by_stable[src["stable_id"]]
                    if row["source_jp"]!=src["source_jp"] or row["source_text_sha256"]!=src["source_text_sha256"]:raise ValueError(name)
                    for key in ("target_ko","notes","status","translator_model"):src[key]=row[key]
                    lines.append(compact(src)+"\n");order.append(src["stable_id"])
                blob="".join(lines).encode();archive.writestr(name,blob)
                files.append({"file":name,"rows":len(lines),"sha256":digest(blob)})
            if order!=[r["stable_id"] for r in all_rows]:raise ValueError("29개 패킷 순서")
            meta={"files":files,"rows":len(order),"rows_by_model":dict(Counter(r["translator_model"] for r in all_rows)),
                  "source_guide_model":"gemini-4-carbon","guide_sha256":self.queue["guide_sha256"]}
            archive.writestr("translation_manifest.json",compact(meta).encode())
        with zipfile.ZipFile(part) as archive:
            if archive.testzip() or any(digest(archive.read(f["file"]))!=f["sha256"] for f in files):raise ValueError("출력 ZIP 확인 실패")
        os.replace(part,packet)
        save(ROOT/"완료.json",{**meta,"merged_sha256":digest(merged.read_bytes()),"zip_sha256":digest(packet.read_bytes())})
        self.state("completed",merged=str(merged),packet_zip=str(packet),message="모든 행의 원문 연결과 패킷 순서를 확인했습니다.")

    def run(self):
        while not stopped():
            if self.fatal:
                self.state("provider_error",message=self.fatal);return
            if self.deadline>time.time():
                self.sleep_until(self.deadline,"capacity_wait");continue
            name,ids,pause=self.choose()
            if pause:
                self.sleep_until(pause,"capacity_wait");continue
            if not ids:
                self.finish();return
            self.state("translating",active_chunk=name,active_ids=ids,new_rows_this_request=len(set(ids)-self.seen),message=f"미번역 {len(ids)}행을 준비했습니다.")
            try:
                rec=self.service.submit(self.records,self.jobs[name],ids,self.problems)
            except Exception as exc:
                self.state("worker_error",message=str(exc)[:320]);raise
            self.apply(rec)
            self.state("translating",message=f"{name} · HTTP {rec.get('http_status')} · {rec.get('finish_reason') or rec.get('provider_status') or '수신 여부 미확인'}")
            if rec.get("http_status")==200:
                time.sleep(1)
        self.state("paused",message="중단 신호를 확인해 새 전송을 멈췄습니다.")


if __name__=="__main__":
    with single_worker():
        Run().run()

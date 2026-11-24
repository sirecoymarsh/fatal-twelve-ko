"""Prepare the complete remaining queue and preserve original stable IDs and model attribution."""
import collections
import json
import os
from pathlib import Path
import re
from argon_native import ROOT, STORY, MODEL, RECEIPTS, PROGRESS, MARKER, Translator, stopped
from story_context import compact, digest, load, put, save, source_data
from carbon_api import utc
from translate_chunks import RESULTS, input_text, check_terms, validation_module, export_row
from import_gui import rows as parse_lines

MANIFEST=ROOT/"대기열.json"
OUTPUT=ROOT/"검증_청크"
BASELINE=ROOT/"기존_카본_검증본.jsonl"

def prepare():
    records,_,_=source_data()
    jobs=load(STORY/"청크_목록.json")["jobs"]
    for d in (ROOT/"runtime",RECEIPTS,OUTPUT):
        d.mkdir(parents=True,exist_ok=True)
    if not MANIFEST.exists():
        initial=(STORY/"카본_시나리오_진행본.jsonl").read_bytes()
        if BASELINE.exists() and BASELINE.read_bytes()!=initial:
            raise ValueError("카본 체크포인트가 준비 중 변경됐습니다.")
        put(BASELINE,initial)
    data=BASELINE.read_bytes()
    old=[json.loads(line) for line in data.splitlines() if line.strip()]
    baseline={row["stable_id"]:row for row in old}
    mapping={r["stable_id"]:r for r in records}
    if len(baseline)!=len(old) or len(mapping)!=len(records):
        raise ValueError("원문/완료 ID 중복")
    for sid,row in baseline.items():
        if row["source_text_sha256"]!=mapping[sid]["source_text_sha256"] or row["source_jp"]!=mapping[sid]["source_jp"] or row.get("translator_model")!="gemini-4-carbon":
            raise ValueError("이전 번역의 원문/모델 연결 오류 "+sid)
    tasks={}; short_ids=[]
    for job in jobs:
        ids=[r["id"] for r in records[job["start"]:job["end"]] if r["stable_id"] not in baseline]
        if ids: tasks[job["chunk"]]=ids;short_ids.extend(ids)
    if len(set(short_ids))!=len(short_ids) or len(short_ids)+len(old)!=len(records):
        raise ValueError("대기열 범위 오류")
    structure={"model":MODEL,"total":len(records),"baseline":len(old),"baseline_sha256":digest(data),
               "rows_to_send":len(short_ids),"jobs":tasks,"guide_sha256":load(STORY/"공통참조_등록.json")["guide_sha256"]}
    if MANIFEST.exists() and load(MANIFEST)!=structure:raise ValueError("원문/기존 번역/대기열이 달라졌습니다.")
    save(MANIFEST,structure)
    return records,{j["chunk"]:j for j in jobs},baseline,structure

def initial_progress(queue):
    if not PROGRESS.exists():
        save(PROGRESS,{"stage":"queued","updated":utc(),"model":MODEL,"total_rows":queue["total"],
             "queued_for_argon":queue["rows_to_send"],"carbon_rows":queue["baseline"],"argon_rows":0,
             "verified_rows":queue["baseline"],"remaining_rows":queue["rows_to_send"],"http_responses":0})

def validated(rec,source,validator):
    ver=rec.get("model_version") or ""
    if rec.get("http_status")!=200 or rec.get("finish_reason") not in ("STOP","MAX_TOKENS"):
        return {},{}
    if not (ver==MODEL or ver.startswith(MODEL+"-") and "cyber" not in ver):
        raise ValueError("실제 반환 모델을 확인할 수 없습니다: "+ver)
    parsed=parse_lines(rec["visible_text"]);keep={};problems={}
    for sid in rec["ids"]:
        if sid not in parsed:
            problems[sid]=["완전한 출력 행이 없음"];continue
        r=source[sid];obj=parsed[sid];text=obj["ko"];notes=obj.get("notes",[])
        if not text.strip() or not isinstance(notes,list) or not all(isinstance(x,str) for x in notes):
            problems[sid]=["빈 번역 또는 메모 형식"];continue
        errors=check_terms(r["source_jp"],text);warnings=[]
        validator.check_protected_tokens(r,text,errors.append,warnings.append)
        validator.check_language(r,text,errors.append,warnings.append)
        for mark in ("≪","≫"):
            if text.count(mark)!=r["source_jp"].count(mark):errors.append("작품 괄호 "+mark)
        if any(t.get("ruby_kind")=="ateji" for t in r["protected_tokens"]):
            tags=lambda value:re.findall(r"\{/?(?:rb|rt)\}",value)
            if tags(text)!=tags(r["source_jp"]):errors.append("아테지 루비 순서")
        if errors:problems[sid]=errors;continue
        entry=export_row(r,text,notes)
        entry.update(translator_model=MODEL,model_version=ver,provider_response_id=rec.get("response_id"),request_sha256=rec["request_sha256"])
        keep[sid]=entry
    return keep,problems

def pilot():
    records,jobs,old,queue=prepare();initial_progress(queue)
    if stopped():raise SystemExit("작업 중단 신호")
    if list(RECEIPTS.glob("*.json")) or MARKER.exists():raise SystemExit("기존 전송이 있어 첫 요청을 반복하지 않습니다.")
    name=min(queue["jobs"],key=lambda c:(len(queue["jobs"][c]),c))
    ids=queue["jobs"][name]
    print("queue",len(jobs),queue["rows_to_send"],"first",name,len(ids),flush=True)
    service=Translator(); rec=service.submit(records,jobs[name],ids,{})
    keep,problems=validated(rec,{r["id"]:r for r in records},validation_module())
    if keep:save(OUTPUT/(name+".json"),keep)
    status=load(PROGRESS);status.update(stage="pilot_returned",updated=utc(),active_chunk=None,active_ids=[],
            argon_rows=len(keep),verified_rows=len(old)+len(keep),remaining_rows=queue["rows_to_send"]-len(keep),
            http_responses=1,last_chunk=name,last_http=rec["http_status"],last_finish=rec["finish_reason"],last_model=rec["model_version"])
    save(PROGRESS,status)
    print("response",rec["http_status"],rec.get("provider_status"),rec["model_version"],rec["finish_reason"],len(keep),len(problems),flush=True)

if __name__=="__main__":
    import sys
    if sys.argv[1:]==["--first"]:pilot()

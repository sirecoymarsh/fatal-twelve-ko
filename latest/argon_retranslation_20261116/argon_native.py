"""Run the verified AItranslator v1.11 request builder with the selected local Vertex profile."""
import collections
import concurrent.futures
import csv
import hashlib
import io
import json
import logging
import marshal
import os
from pathlib import Path
import re
import sys
import threading
import time
import traceback
import types
from urllib.parse import unquote, urlsplit
import xml.sax.saxutils

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent
STORY = PROJECT / "handoff/carbon_20261116/story_context"
APP = PROJECT / "carbon_gui_20261116/app"
sys.path.insert(0, str(STORY))
sys.path.insert(0, str(APP / "carbon_runtime"))
sys.path.insert(0, str(APP))
import truststore
truststore.inject_into_ssl()
import requests
from carbon_api import transport, utc
from carbon_bridge import canonical_settings, NUMBER
from fatal_capacity import retry_hint
from argon_progress import publish
from story_context import compact, digest, load, put, save
from translate_chunks import input_text

MODEL = "gemini-4-argon"
VERIFY_MAIN = "1cebd4b191b4b77613d3307032cb2746642828046c139b5cf19956a9415767e0"
ORIGINAL = Path(r"P:\AI\Codex\projects\tsr25-carbon-api-20261112\appclone\internals\main.marshal")
RECEIPTS = ROOT / "receipts"
MARKER = ROOT / "전송중.json"
PROGRESS = ROOT / "진행.json"


def stopped():
    return transport.STOP.exists() or (ROOT / "중단.flag").exists()


class ActiveProfile(transport.Vertex):
    def __init__(self, profile):
        config = profile["vertex_ai_common"]["vertex_credentials_json"]
        account = json.loads(config) if isinstance(config, str) else config
        if account.get("profile_reference"):
            source = Path(load(APP.parent/"controller/jobs.json")["source_config"])
            data = load(source)["vertex_ai_common"]["vertex_credentials_json"]
            source_account = json.loads(data) if isinstance(data, str) else data
            if any(account.get(k) != source_account.get(k) for k in ("project_id","client_email")):
                raise ValueError("선택한 번역기 계정과 원본 프로필의 식별 정보가 다릅니다.")
            account = source_account
        if not all(account.get(k) for k in ("project_id", "client_email", "private_key")):
            raise ValueError("활성 번역기 프로필에서 Vertex 인증을 읽을 수 없습니다.")
        self.account = account
        self.access = ""
        self.expiry = 0

    def native_token(self, project, _credentials, _location):
        if project != self.account["project_id"] or stopped():
            raise RuntimeError("활성 프로젝트 또는 작업 중단 상태를 확인하세요.")
        return self.token(), None


class Translator:
    def __init__(self):
        profile = load(APP/"config.json")
        self.settings = profile["providers"]["vertex_ai_gemini"]
        self.auth = ActiveProfile(profile)
        self.project = self.auth.account["project_id"]
        self.guide = (STORY/"카본_공통참조.txt").read_text("utf-8").rstrip()
        self.guide_sha = load(STORY/"공통참조_등록.json")["guide_sha256"]
        if digest((STORY/"카본_공통참조.txt").read_bytes()) != self.guide_sha:
            raise ValueError("전편 인물 해석의 해시가 달라졌습니다.")
        src = Path(profile["prompt_settings"]["translation"]["selected"]).read_text("utf-8-sig")
        if self.guide not in src or src.count("{{slot::content}}") != 1:
            raise ValueError("선택한 프롬프트의 공통 해석 또는 입력 슬롯을 확인하세요.")
        guide_end = src.index(self.guide) + len(self.guide)
        tail = src[guide_end:].replace("인물의 어투는 카본이 정한다.", "인물의 어투는 아르곤이 현재 장면과 카본의 전편 해석을 참고해 정한다.")
        self.prompt = src[:guide_end] + "\n\n이 청크의 번역자는 아르곤이다. 위의 전편 인물·관계 해석은 카본이 일본어 전편을 읽고 작성한 참고 자료이다. 장면의 일본어와 인물 관계에 맞춰 자연스러운 한국어 대화를 먼저 쓰고 용어표와 보호 토큰을 확인한다." + tail
        self.prompt_file = ROOT/"아르곤_번역_프롬프트.txt"
        put(self.prompt_file, self.prompt)
        self.session = requests.Session()
        self.receipt = None
        self.pending = None
        raw = ORIGINAL.read_bytes()
        if digest(raw) != VERIFY_MAIN:
            raise ValueError("검증된 AItranslator 원본과 다릅니다.")
        logger = logging.getLogger("fatal.argon.native")
        logger.addHandler(logging.NullHandler())
        logger.propagate = False
        g = dict(globals())
        g.update(logger=logger, UI_TEXTS={}, PROMPT_FOLDER=str(self.prompt_file.parent),
                 _last_thought_signature=None, _vertex_token_cache={})
        for f in marshal.loads(raw).co_consts:
            if isinstance(f, types.CodeType) and not f.co_freevars:
                g[f.co_name] = types.FunctionType(f, g)
        g["process_prompt_variables"].__defaults__ = (None,None)
        g["get_vertex_access_token"] = self.auth.native_token
        g["log_thinking_feedback"] = g["log_safety_feedback_requests"] = lambda *a, **k: None
        g["requests"] = types.SimpleNamespace(post=self.post, exceptions=requests.exceptions)
        self.translate_text = g["translate_text"]

    def post(self, url, *, headers, json, timeout):
        if stopped():
            raise RuntimeError("중단 신호")
        parts = urlsplit(url)
        expected = "/projects/"+self.project+"/locations/global/publishers/google/models/"+MODEL+":generateContent"
        if parts.scheme != "https" or parts.hostname != "aiplatform.googleapis.com" or not unquote(parts.path).endswith(expected):
            raise ValueError("아르곤 전송 대상이 선택한 Vertex global 프로젝트와 다릅니다.")
        canonical_settings(json)
        sys_instruction = json.get("systemInstruction", json.get("system_instruction")) or {}
        system = "\n".join(x.get("text","") for x in sys_instruction.get("parts",[]))
        inp = "\n".join(x.get("text","") for msg in json.get("contents",[]) if msg.get("role")=="user" for x in msg.get("parts",[]))
        selected = [m[2] for m in NUMBER.finditer(inp)]
        safety = {x["category"]:x["threshold"] for x in json.get("safetySettings",[])}
        settings = json.get("generationConfig", {})
        if selected != self.pending["ids"] or self.guide not in system or "이 청크의 번역자는 아르곤이다." not in system:
            raise ValueError("실제 요청의 대상 ID 또는 인물 해석/번역자 지시가 다릅니다.")
        if safety != self.settings["safety_settings"] or settings.get("thinkingConfig",{}).get("thinkingLevel") != "MEDIUM":
            raise ValueError("실제 요청의 안전 설정 또는 추론 수준이 다릅니다.")
        if "X-Vertex-AI-LLM-Shared-Request-Type" in headers:
            raise ValueError("기본 과금 방식이 아닙니다.")
        ticket = dict(self.pending, started=utc(), model_requested=MODEL,
                      project_fingerprint=digest(self.project.encode())[:16], request_sha256=digest(compact(json).encode()),
                      guide_sha256=self.guide_sha, system_sha256=digest(system.encode()), thinking="MEDIUM",
                      safety_settings=safety, max_output_tokens=settings.get("maxOutputTokens"),
                      transport="AItranslator v1.11 / Vertex generateContent / Standard")
        ticket["ref"] = ticket["started"].replace(":","").replace("-","").replace(".","")+"_"+ticket["chunk"]
        if MARKER.exists():
            raise RuntimeError("복구되지 않은 전송 기록이 있습니다.")
        save(MARKER, ticket)
        status = load(PROGRESS) if PROGRESS.is_file() else {}
        status.update(stage="request_in_flight",active_chunk=ticket["chunk"],active_ids=selected,
                      active_since=ticket["started"],updated=utc())
        status["unique_rows_sent"] = status.get("unique_rows_sent", 0) + status.pop("new_rows_this_request", 0)
        status["not_yet_sent"] = max(0,status.get("queued_for_argon",0)-status["unique_rows_sent"])
        publish(PROGRESS,status)
        try:
            answer = self.session.post(url,headers=headers,json=json,timeout=(25,600))
        except requests.RequestException as exc:
            record=dict(ticket,finished=utc(),http_status=None,provider_status=type(exc).__name__,
                        finish_reason=None,model_version=None,usage={},visible_text="",delivery="unconfirmed")
            self.save_reply(record)
            raise
        try: data=answer.json()
        except ValueError: data={}
        if not isinstance(data,dict): data={}
        error=data.get("error") or {}
        candidates=data.get("candidates") or []
        candidate=candidates[0] if candidates else {}
        content=(candidate.get("content") or {}).get("parts") or []
        visible="".join(x.get("text","") for x in content if not x.get("thought"))
        record=dict(ticket,finished=utc(),http_status=answer.status_code,model_version=data.get("modelVersion"),
                    response_id=data.get("responseId"),finish_reason=candidate.get("finishReason") or
                    (data.get("promptFeedback") or {}).get("blockReason"),provider_status=error.get("status"),
                    retry_after=retry_hint(answer,data) if answer.status_code==429 else 0,
                    usage=data.get("usageMetadata") or {},visible_text=visible,response_sha256=digest(visible.encode()),
                    error_message=(str(error.get("message","")).replace(self.project,"[프로젝트]")[:350] if error else ""))
        self.save_reply(record)
        return answer

    def save_reply(self, record):
        save(RECEIPTS/(record["ref"]+".json"),record)
        self.receipt=record
        MARKER.unlink(missing_ok=True)

    def submit(self, records, base, wanted, errors, cap=None):
        index={r["id"]:j for j,r in enumerate(records[base["start"]:base["end"]],base["start"])}
        job=dict(base,start=min(index[i] for i in wanted),end=max(index[i] for i in wanted)+1)
        scene=json.loads(input_text(records,job,set(wanted),{i:errors[i] for i in wanted if i in errors}))
        lines=[]
        for pos,item in enumerate(scene["target"]):
            row={k:v for k,v in item.items() if k!="id"}
            row["file"]=scene["file"]
            if pos==0:
                for key in ("context_before","additional_context"):
                    if scene.get(key):row["before" if key=="context_before" else "nearby"]=scene[key]
            if pos==len(wanted)-1 and scene["context_after"]:row["after"]=scene["context_after"]
            if item["id"] in errors:row["check"]=errors[item["id"]]
            lines.append(item["id"]+"\t"+compact(row))
        self.pending={"chunk":base["chunk"],"ids":wanted}
        self.receipt=None
        s=self.settings
        _out,err=self.translate_text(text_content="\n".join(lines),provider="vertex_ai_gemini",api_key="",
            vertex_project_id=self.project,vertex_credentials_json="{}",vertex_location="global",model_name=MODEL,
            prompt=self.prompt,promptB="",prefill="",prefillB="",glossary={},character={},
            temperature=s.get("temperature",1),top_p=s.get("top_p"),max_output_tokens=cap or s.get("max_output_tokens",11264),
            log_enabled=False,safety_settings=s["safety_settings"],use_thinking_budget=False,thinking_budget=None,
            use_thinking_level=True,thinking_level="medium",include_thoughts=False,thought_signature_mode="none",
            structured_response_mode="none",enable_dynamic_character_profiles=False,enable_glossary_dynamic_filtering=False,
            selected_prompt_type=str(self.prompt_file),use_search_grounding=False,is_running_check_cb=lambda:not stopped())
        if self.receipt is None:
            message=re.sub(r"https?://\S+","[주소]",str(err or "응답 없음")).replace(self.project,"[프로젝트]")
            raise RuntimeError("번역기 전송 준비 실패: "+message[:280])
        return self.receipt

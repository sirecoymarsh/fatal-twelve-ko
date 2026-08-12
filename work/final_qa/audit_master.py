#!/usr/bin/env python3
"""Static linguistic/runtime audit for Fatal Twelve Korean master drafts.

Consumes only Japanese-source/Korean-target master JSON and never rewrites text.
The original CLI and legacy report columns are preserved.
"""
from __future__ import annotations

import argparse
import ast
import collections
import dataclasses
import decimal
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

HIRAGANA_RE = re.compile(r"[ぁ-ゖゝ-ゟ]")
KATAKANA_CORE_RE = re.compile(r"[ァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")
KANA_RE = re.compile(r"[ぁ-ゖゝ-ゟァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")
LONG_MARK_RE = re.compile(r"[ーｰ]")
KANJI_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff々〆ヶ]")
HANGUL_RE = re.compile(r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7a3]")
FULLWIDTH_DIGIT_RE = re.compile(r"[０-９]")
ROMAN_UNICODE_RE = re.compile(r"[\u2160-\u2188]+")
ROMAN_ASCII_RE = re.compile(r"(?<![A-Za-z0-9])(?:[IVXLCDM]+)(?![A-Za-z0-9])")
ASCII_WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]{1,}")
EXPLICIT_NUMBER_RE = re.compile(r"\d+(?:,\d{3})*(?:\.\d+)?")
PERCENT_FORMAT_RE = re.compile(r"%(?:\([^)]+\))?[#0\- +]?\d*(?:\.\d+)?[diouxXeEfFgGcrsa]")
KATAKANA_BOUNDARY_CLASS = r"ァ-ヺヽヾーㇰ-ㇿｦ-ﾟ"
CHAN_TOKEN_RE = re.compile(rf"(?<![{KATAKANA_BOUNDARY_CLASS}])チャン(?![{KATAKANA_BOUNDARY_CLASS}])")
ENGLISH_SFX = {"badump", "ba-dump", "thump", "thud", "whoosh", "swoosh", "wham", "bam", "bang", "clunk", "clank", "click", "slam", "smack", "crash", "rustle", "shuffle", "gulp", "gasp", "pant", "sniff", "sob", "tch", "heh", "hah", "haha", "hahaha", "hmph", "ugh", "urk", "eep"}
FORBIDDEN_VARIANTS = {"알란": "아란", "알랜": "아란", "파르카": "파르카", "파사질": "파사지르", "운명의 대광장": "운명의 대회랑"}
FIXED_TERMS = {"凛火": "린카", "海晴": "미하루", "直未": "나오미", "真央": "마오", "ダイアナ": "다이아나", "パルカ": "파르카", "アラン": "아란", "オデット": "오데트", "フェデリーコ": "페데리코", "ユウ": "유우", "ソーニャ": "소냐", "桂子": "게이코", "スケール": "스케일", "茂継": "시게쓰구", "チャン": "장", "昌鎬": "창호", "レテ": "레테", "リンダ": "린다", "蛇鉈": "헤비나타", "瓶淵桂子": "카메부치 게이코", "瓶淵春樹": "카메부치 하루키", "女神の選定": "여신의 선정", "運命の終着点": "운명의 종착점", "運命の大広間": "운명의 대회랑", "夢の世界": "꿈의 세계", "パサジール": "파사지르"}
POLICY_TO_LEGACY = {"HARD": "error", "REVIEW": "warning", "INFO": "info"}

@dataclasses.dataclass(frozen=True)
class LexToken:
    kind: str
    value: str
    start: int
    end: int

@dataclasses.dataclass
class LexResult:
    tokens: list[LexToken]
    errors: list[str]

RubyKey = tuple[str, str]
RubyValue = tuple[str, str]
RubyMap = Mapping[RubyKey, RubyValue]

def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", "surrogatepass")).hexdigest()

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def load_entries(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, list): return data
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        raise ValueError(f"{path}: expected object with entries[]")
    return data["entries"]

def protected_values(entry: Mapping[str, Any]) -> list[str]:
    values = []
    for token in entry.get("protected_tokens") or []:
        if isinstance(token, str):
            # Legacy system-UI masters store protected tokens as strings. A
            # full-width source number and its NFKC-equivalent ASCII Korean
            # spelling are semantically identical and are checked below by
            # explicit_number_values(), not by brittle code-point equality.
            normalized = unicodedata.normalize("NFKC", token)
            if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", normalized):
                continue
            values.append(token)
        elif isinstance(token, dict) and token.get("value") is not None:
            # Explicit numbers are validated semantically after width
            # normalization (and Roman numerals by exact code point), not by
            # brittle source spelling equality such as １７ versus 17.
            if str(token.get("kind") or "").lower() == "number":
                continue
            values.append(str(token["value"]))
    return values

def render_renpy_literal(text: str) -> str: return json.dumps(text, ensure_ascii=False)
def decode_renpy_literal(raw: str) -> str:
    value = ast.literal_eval(raw)
    if not isinstance(value, str): raise ValueError("literal did not decode to str")
    return value

def literal_roundtrip(text: str) -> bool:
    try: return decode_renpy_literal(render_renpy_literal(text)) == text
    except (SyntaxError, ValueError, UnicodeError): return False

def _scan_interpolation(text: str, start: int) -> int | None:
    depth, index = 1, start + 1; quote = None; escaped = False
    while index < len(text):
        char = text[index]
        if quote is not None:
            if escaped: escaped = False
            elif char == "\\": escaped = True
            elif char == quote: quote = None
        elif char in "'\"": quote = char
        elif char == "[": depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0: return index + 1
        index += 1
    return None

def lex_renpy_text(text: str) -> LexResult:
    tokens, errors = [], []; index = 0
    while index < len(text):
        if text.startswith("[[", index) or text.startswith("{{", index):
            tokens.append(LexToken("literal_escape", text[index:index + 2], index, index + 2)); index += 2; continue
        char = text[index]
        if char == "[":
            end = _scan_interpolation(text, index)
            if end is None: errors.append(f"unclosed interpolation at {index}"); index += 1
            else: tokens.append(LexToken("interpolation", text[index:end], index, end)); index = end
            continue
        if char == "{":
            close = text.find("}", index + 1)
            if close < 0: errors.append(f"unclosed text tag at {index}"); index += 1
            else:
                end = close + 1; value = text[index:end]; body = value[1:-1].strip()
                if not body: errors.append(f"empty text tag at {index}")
                kind = "ruby_tag" if body in {"rb", "/rb", "rt", "/rt"} else "text_tag"
                tokens.append(LexToken(kind, value, index, end)); index = end
            continue
        if text.startswith("%%", index): tokens.append(LexToken("percent_escape", "%%", index, index + 2)); index += 2; continue
        if char == "%":
            match = PERCENT_FORMAT_RE.match(text, index)
            if match:
                value = match.group(0); kind = "percent_named" if value.startswith("%(") else "percent_positional"
                tokens.append(LexToken(kind, value, index, match.end())); index = match.end(); continue
        if char == "\\" and index + 1 < len(text) and text[index + 1] in "nrt\\":
            tokens.append(LexToken("literal_escape", text[index:index + 2], index, index + 2)); index += 2; continue
        if char == "\n": tokens.append(LexToken("control_newline", "\n", index, index + 1))
        index += 1
    return LexResult(tokens, errors)
def _tokens(result: LexResult, *kinds: str) -> list[LexToken]:
    allowed = set(kinds); return [token for token in result.tokens if token.kind in allowed]
def _values(result: LexResult, *kinds: str) -> list[str]: return [token.value for token in _tokens(result, *kinds)]
def mask_token_spans(text: str, result: LexResult, kinds: Iterable[str] | None = None) -> str:
    selected = set(kinds) if kinds is not None else {"interpolation", "text_tag", "ruby_tag", "percent_named", "percent_positional", "percent_escape", "literal_escape"}
    chars = list(text)
    for token in result.tokens:
        if token.kind in selected: chars[token.start:token.end] = " " * (token.end - token.start)
    return "".join(chars)
def _tag_body(value: str) -> str: return value[1:-1].strip()
def validate_text_tag_closures(result: LexResult) -> list[str]:
    stack=[]; paired={"a","alpha","b","color","font","i","k","outlinecolor","plain","s","size","u"}; errors=[]
    for token in _tokens(result,"text_tag"):
        body=_tag_body(token.value)
        if body.startswith("#"): continue
        if body=="/":
            if not stack: errors.append(f"closing tag without open at {token.start}: {token.value}")
            else: stack.pop()
            continue
        closing=body.startswith("/"); name=(body[1:] if closing else body.split("=",1)[0]).strip().lower()
        if closing:
            if not stack or stack[-1]!=name: errors.append(f"crossed or unmatched closing tag at {token.start}: {token.value}")
            else: stack.pop()
        elif name in paired: stack.append(name)
    return errors

def _ruby_base_class(char: str) -> str | None:
    if KANJI_RE.fullmatch(char): return "han"
    if HIRAGANA_RE.fullmatch(char): return "hiragana"
    if KATAKANA_CORE_RE.fullmatch(char) or LONG_MARK_RE.fullmatch(char): return "katakana"
    if HANGUL_RE.fullmatch(char): return "hangul"
    if char.isascii() and char.isalnum(): return "ascii_alnum"
    return None

def _standalone_ruby_base(text: str, end: int) -> str:
    """Infer the base immediately before a Ren'Py 6.99 {rt} tag.

    Fatal Twelve also uses the legacy compact form 刻{rt}とき{/rt}
    without explicit {rb} tags. A same-script run selects 刻 from 最後の刻
    and 순간 from 마지막 순간.
    """
    if end <= 0:
        return ""
    char_class = _ruby_base_class(text[end - 1])
    if char_class is None:
        return ""
    start = end - 1
    while start > 0 and _ruby_base_class(text[start - 1]) == char_class:
        start -= 1
    return text[start:end]

def parse_ruby_pairs(text: str, result: LexResult | None = None):
    result=result or lex_renpy_text(text); pairs=[]; skeleton=[]; errors=[]; state="idle"; rb_start=0; rb_text=""
    for token in _tokens(result,"ruby_tag"):
        body=_tag_body(token.value); skeleton.append(body)
        if body=="rb" and state=="idle":
            state,rb_start="in_rb",token.end
        elif body=="/rb" and state=="in_rb":
            rb_text,state=text[rb_start:token.start],"after_rb"
        elif body=="rt" and state=="after_rb":
            state,rt_start="in_rt",token.end
        elif body=="rt" and state=="idle":
            rb_text=_standalone_ruby_base(text,token.start)
            if not rb_text:
                errors.append(f"standalone ruby rt has no visible base at {token.start}")
            state,rt_start="in_rt",token.end
        elif body=="/rt" and state=="in_rt":
            pairs.append((rb_text,text[rt_start:token.start])); state="idle"
        else:
            errors.append(f"unexpected ruby tag {token.value!r} at {token.start} while {state}")
    if state!="idle": errors.append(f"incomplete ruby sequence ending in state {state}")
    return pairs,errors,skeleton

def load_ruby_map(path: Path | None) -> dict[RubyKey,RubyValue]:
    if path is None: return {}
    data=json.loads(path.read_text(encoding="utf-8-sig")); rows=data.get("entries") if isinstance(data,dict) and "entries" in data else data; result={}
    if isinstance(rows,list):
        for row in rows: result[(str(row["source_rb"]),str(row["source_rt"]))]=(str(row["target_rb"]),str(row["target_rt"]))
        return result
    if isinstance(rows,dict):
        for packed_key,row in rows.items():
            source_rb,source_rt=packed_key.split("\u0000",1)
            value=((str(row["target_rb"]),str(row["target_rt"])) if isinstance(row,dict) else (str(row[0]),str(row[1])))
            result[(source_rb,source_rt)]=value
        return result
    raise ValueError(f"{path}: unsupported ruby map schema")

def _ascii_roman_is_contextual(text: str,start:int,end:int,token:str)->bool:
    if len(token)>=2:return True
    left,right=text[max(0,start-12):start],text[end:min(len(text),end+12)]; markers=r"(?:第|章|部|編|型|号|ルート|route|part|chapter)"
    return bool(re.search(markers+r"\s*$",left,re.I) or re.match(r"^\s*"+markers,right,re.I))
def extract_roman_tokens(text:str,lexed:LexResult|None=None)->list[str]:
    lexed=lexed or lex_renpy_text(text); visible=mask_token_spans(text,lexed); found=[]; occupied=[]
    for match in ROMAN_UNICODE_RE.finditer(visible): found.append((match.start(),match.group(0))); occupied.append(match.span())
    for match in ROMAN_ASCII_RE.finditer(visible):
        if any(match.start()<end and match.end()>start for start,end in occupied): continue
        if _ascii_roman_is_contextual(visible,match.start(),match.end(),match.group(0)): found.append((match.start(),match.group(0)))
    return [token for _,token in sorted(found)]
def quote_skeleton(text:str,lexed:LexResult|None=None)->list[str]:
    visible=mask_token_spans(text,lexed or lex_renpy_text(text)); return [char for char in visible if char in "「」『』"]
def quote_balance_errors(skeleton:Sequence[str])->list[str]:
    stack=[];errors=[];pairs={"」":"「","』":"『"}
    for index,token in enumerate(skeleton):
        if token in "「『":stack.append(token)
        elif not stack or stack[-1]!=pairs[token]:errors.append(f"unmatched {token} at quote token {index}")
        else:stack.pop()
    if stack:errors.append("unclosed quote(s): "+"".join(stack))
    return errors
def _mask_exact_allowlist(text:str,allowlist:Iterable[str])->str:
    for value in sorted({v for v in allowlist if v},key=len,reverse=True):text=text.replace(value," "*len(value))
    return text
def source_contains_term(source:str,term:str)->bool:return CHAN_TOKEN_RE.search(source) is not None if term=="チャン" else term in source
def _fullwidth_numeric_copy(text:str)->str:return text.translate(str.maketrans("０１２３４５６７８９＋－．，％：／～","0123456789+-.,%:/~"))
def explicit_number_values(text:str,lexed:LexResult|None=None)->list[str]:
    lexed=lexed or lex_renpy_text(text);visible=mask_token_spans(text,lexed);roman_spans=[]
    for match in ROMAN_UNICODE_RE.finditer(visible):roman_spans.append(match.span())
    chars=list(visible)
    for start,end in roman_spans:chars[start:end]=" "*(end-start)
    visible=_fullwidth_numeric_copy("".join(chars));values=[]
    for match in EXPLICIT_NUMBER_RE.finditer(visible):
        try:value=decimal.Decimal(match.group(0).replace(",",""))
        except decimal.InvalidOperation:continue
        values.append(format(value.normalize(),"f"))
    return values

def _finding_id(payload:Mapping[str,Any])->str:
    identity={key:payload.get(key) for key in ("rule_id","script","stable_id","sequence","source_sha256","target_sha256","message")};encoded=json.dumps(identity,ensure_ascii=False,sort_keys=True,separators=(",",":"));return hashlib.sha256(encoded.encode("utf-8")).hexdigest()
def add_issue(issues,entry,script,policy_severity,rule_id,message,evidence=None,*,category=None):
    source,target=str(entry.get("source_jp") or ""),str(entry.get("draft_ko") or "");issue={"script":script,"sequence":entry.get("sequence") or entry.get("command_index"),"stable_id":entry.get("stable_id"),"source_line":entry.get("source_line"),"speaker":entry.get("speaker"),"severity":POLICY_TO_LEGACY[policy_severity],"policy_severity":policy_severity,"rule_id":rule_id,"category":category or rule_id.lower(),"status":"open","message":message,"evidence":evidence,"normalized_evidence":evidence,"source_sha256":text_sha256(source),"target_sha256":text_sha256(target),"source_jp":source,"draft_ko":target};issue["finding_id"]=_finding_id(issue);issues.append(issue)
def _compare_counter(issues,entry,script,source_values,target_values,rule_id,message):
    source_counter,target_counter=collections.Counter(source_values),collections.Counter(target_values)
    if source_counter==target_counter:return True
    add_issue(issues,entry,script,"HARD",rule_id,message,{"source":dict(source_counter),"target":dict(target_counter)},category="runtime_tokens");return False
def audit_entry(entry,script,issues,*,ruby_map=None,cjk_allowlist=()):
    source=str(entry.get("source_jp") or "");target=str(entry.get("draft_ko") or "");ruby_map=ruby_map or {}
    if not target.strip():add_issue(issues,entry,script,"HARD","COVERAGE_PENDING_OR_NULL","빈 한국어 번역",category="empty");return
    if "\ufffd" in target or any(0x80<=ord(char)<=0x9F for char in target):add_issue(issues,entry,script,"HARD","RENPY_LITERAL_PARSE_FAIL","깨진 문자 또는 C1 제어 문자",category="encoding")
    for side,text,raw_keys in (("source",source,("source_literal_raw","source_raw_literal")),("target",target,("target_literal_raw","draft_literal_raw","target_raw_literal"))):
        if not literal_roundtrip(text):add_issue(issues,entry,script,"HARD","RENPY_LITERAL_ROUNDTRIP_FAIL",f"{side} decoded 문자열 literal round-trip 실패")
        for key in raw_keys:
            if key in entry and entry.get(key) is not None:
                try:decoded=decode_renpy_literal(str(entry[key]))
                except (SyntaxError,ValueError,UnicodeError) as exc:add_issue(issues,entry,script,"HARD","RENPY_LITERAL_PARSE_FAIL",f"{side} raw literal parse 실패",{"field":key,"error":str(exc)})
                else:
                    if decoded!=text:add_issue(issues,entry,script,"HARD","RENPY_LITERAL_ROUNDTRIP_FAIL",f"{side} raw literal decoded 값 불일치",{"field":key,"decoded":decoded})
    source_lex,target_lex=lex_renpy_text(source),lex_renpy_text(target)
    if source_lex.errors:add_issue(issues,entry,script,"HARD","RENPY_LITERAL_PARSE_FAIL","원문 Ren'Py control parse 실패",source_lex.errors)
    if target_lex.errors:add_issue(issues,entry,script,"HARD","RENPY_LITERAL_PARSE_FAIL","번역 Ren'Py control parse 실패",target_lex.errors)
    source_tag_errors=validate_text_tag_closures(source_lex);target_tag_errors=validate_text_tag_closures(target_lex)
    if source_tag_errors or target_tag_errors:add_issue(issues,entry,script,"HARD","TEXT_TAG_MALFORMED","Ren'Py text tag 닫힘 구조 오류",{"source":source_tag_errors,"target":target_tag_errors})
    source_interpolations=_values(source_lex,"interpolation");target_interpolations=_values(target_lex,"interpolation")
    if _compare_counter(issues,entry,script,source_interpolations,target_interpolations,"INTERPOLATION_MISMATCH","Ren'Py interpolation 멀티셋 불일치"):
        if source_interpolations!=target_interpolations:add_issue(issues,entry,script,"REVIEW","INTERPOLATION_REORDER","named interpolation 순서 변경 검토",{"source":source_interpolations,"target":target_interpolations})
    source_tags,target_tags=_values(source_lex,"text_tag"),_values(target_lex,"text_tag")
    if source_tags!=target_tags:add_issue(issues,entry,script,"HARD","TEXT_TAG_MISMATCH","Ren'Py text/control tag sequence 불일치",{"source":source_tags,"target":target_tags},category="runtime_tokens")
    source_positional=_values(source_lex,"percent_positional");target_positional=_values(target_lex,"percent_positional")
    if source_positional!=target_positional:add_issue(issues,entry,script,"HARD","PERCENT_POSITIONAL_MISMATCH","positional percent formatter sequence 불일치",{"source":source_positional,"target":target_positional},category="runtime_tokens")
    source_named,target_named=_values(source_lex,"percent_named"),_values(target_lex,"percent_named")
    if _compare_counter(issues,entry,script,source_named,target_named,"PERCENT_NAMED_MISMATCH","named percent formatter 멀티셋 불일치"):
        if source_named!=target_named:add_issue(issues,entry,script,"REVIEW","PERCENT_NAMED_REORDER","named percent formatter 순서 변경 검토",{"source":source_named,"target":target_named})
    _compare_counter(issues,entry,script,_values(source_lex,"percent_escape"),_values(target_lex,"percent_escape"),"PERCENT_LITERAL_ESCAPE_MISMATCH","literal percent escape 개수 불일치")
    _compare_counter(issues,entry,script,_values(source_lex,"literal_escape"),_values(target_lex,"literal_escape"),"LITERAL_ESCAPE_MISMATCH","Ren'Py literal escape 멀티셋 불일치")
    if len(_tokens(source_lex,"control_newline"))!=len(_tokens(target_lex,"control_newline")):add_issue(issues,entry,script,"HARD","CONTROL_NEWLINE_MISMATCH","내장 개행 수 불일치",{"source":source.count("\n"),"target":target.count("\n")},category="linebreak")
    for value in dict.fromkeys(protected_values(entry)):
        if source.count(value)!=target.count(value):add_issue(issues,entry,script,"HARD","PROTECTED_TOKEN_MISMATCH",f"보호 토큰 개수 불일치: {value!r}",{"source_count":source.count(value),"target_count":target.count(value)},category="protected_token")
    source_ruby,source_ruby_errors,source_ruby_skeleton=parse_ruby_pairs(source,source_lex);target_ruby,target_ruby_errors,target_ruby_skeleton=parse_ruby_pairs(target,target_lex)
    if source_ruby_errors or target_ruby_errors:add_issue(issues,entry,script,"HARD","RUBY_MALFORMED","ruby rb/rt stack 오류",{"source":source_ruby_errors,"target":target_ruby_errors})
    if source_ruby_skeleton!=target_ruby_skeleton or len(source_ruby)!=len(target_ruby):add_issue(issues,entry,script,"HARD","RUBY_STRUCTURE_MISMATCH","ruby rb/rt pair 수·순서 불일치",{"source":source_ruby_skeleton,"target":target_ruby_skeleton})
    elif not source_ruby_errors and not target_ruby_errors:
        for index,(source_pair,target_pair) in enumerate(zip(source_ruby,target_ruby)):
            expected=ruby_map.get(source_pair)
            if expected is None:add_issue(issues,entry,script,"REVIEW","RUBY_UNMAPPED","승인 ruby map에 없는 표기",{"pair_index":index,"source":source_pair,"target":target_pair})
            elif tuple(target_pair)!=tuple(expected):add_issue(issues,entry,script,"HARD","RUBY_MAPPING_MISMATCH","승인 ruby target 표기와 불일치",{"pair_index":index,"source":source_pair,"expected":expected,"target":target_pair})
    source_roman=extract_roman_tokens(source,source_lex);target_roman=extract_roman_tokens(target,target_lex)
    if source_roman!=target_roman:add_issue(issues,entry,script,"HARD","ROMAN_NUMERAL_CHANGED","Roman numeral code point/개수/순서 변경",{"source":source_roman,"target":target_roman})
    source_quotes,target_quotes=quote_skeleton(source,source_lex),quote_skeleton(target,target_lex);target_quote_errors=quote_balance_errors(target_quotes)
    if target_quote_errors:add_issue(issues,entry,script,"HARD","TARGET_QUOTE_UNBALANCED","한국어 target 낫표 불균형",target_quote_errors)
    if source_quotes:
        if source_quotes!=target_quotes:add_issue(issues,entry,script,"HARD","JP_QUOTE_STYLE","원문 「」/『』 종류·개수·중첩 skeleton 불일치",{"source":source_quotes,"target":target_quotes},category="dialogue_quotes")
    elif target_quotes:add_issue(issues,entry,script,"REVIEW","QUOTE_ADDED","원문에 없는 낫표 추가 검토",target_quotes,category="dialogue_quotes")
    source_visible=mask_token_spans(source,source_lex);target_visible=mask_token_spans(target,target_lex)
    if source==target and (KANA_RE.search(source_visible) or KANJI_RE.search(source_visible)):add_issue(issues,entry,script,"HARD","UNTRANSLATED_JAPANESE","일본어 원문과 번역이 동일",category="untranslated")
    kana_hits=[(match.start(),match.group(0)) for match in KANA_RE.finditer(target_visible)];adjacent_long_hits=[];standalone_long_hits=[]
    for match in LONG_MARK_RE.finditer(target_visible):
        left=target_visible[match.start()-1:match.start()];right=target_visible[match.end():match.end()+1]
        if KANA_RE.search(left) or KANA_RE.search(right):adjacent_long_hits.append(match.group(0))
        else:standalone_long_hits.append(match.group(0))
    if kana_hits or adjacent_long_hits:add_issue(issues,entry,script,"HARD","RESIDUAL_KANA","한국어 visible text에 가나가 남음",sorted({char for _,char in kana_hits}|set(adjacent_long_hits)),category="residual_japanese")
    if standalone_long_hits:add_issue(issues,entry,script,"REVIEW","RESIDUAL_LONG_MARK","kana 비인접 장음부호 검토",sorted(set(standalone_long_hits)),category="residual_japanese")
    cjk_scan=_mask_exact_allowlist(target_visible,cjk_allowlist);kanji_hits=sorted(set(KANJI_RE.findall(cjk_scan)))
    if kanji_hits:add_issue(issues,entry,script,"HARD","RESIDUAL_HANJA","한국어 visible text에 비승인 CJK ideograph가 남음",kanji_hits,category="residual_kanji")
    width_hits=sorted(set(FULLWIDTH_DIGIT_RE.findall(target_visible)))
    if "\u3000" in target_visible:width_hits.append("U+3000")
    if width_hits:add_issue(issues,entry,script,"HARD","KO_WIDTH_STYLE","한국어 target의 전각 숫자 또는 U+3000",width_hits,category="fullwidth_space")
    source_numbers=explicit_number_values(source,source_lex);target_numbers=explicit_number_values(target,target_lex)
    if source_numbers and len(source_numbers)==len(target_numbers) and source_numbers!=target_numbers:add_issue(issues,entry,script,"HARD","NUM_SEMANTIC_MISMATCH","명시 숫자 값/순서 불일치",{"source":source_numbers,"target":target_numbers})
    source_words={word.lower() for word in ASCII_WORD_RE.findall(source_visible)};target_words={word.lower() for word in ASCII_WORD_RE.findall(target_visible)};imported_sfx=sorted((target_words-source_words)&ENGLISH_SFX)
    if imported_sfx:add_issue(issues,entry,script,"REVIEW","ENGLISH_PROSE_OR_SFX","일본어 원문에 없는 영어식 의성어/감탄사",imported_sfx,category="english_sfx")
    for jp,ko in FIXED_TERMS.items():
        if source_contains_term(source_visible,jp) and ko not in target_visible:
            rule_id="CHAN_GLOSSARY_MISMATCH" if jp=="チャン" else "GLOSSARY_MISMATCH";add_issue(issues,entry,script,"HARD",rule_id,f"고정 표기 누락: {jp} -> {ko}",category="term_candidate")
    for bad,good in FORBIDDEN_VARIANTS.items():
        if bad!=good and bad in target_visible:add_issue(issues,entry,script,"HARD","GLOSSARY_MISMATCH",f"금지 표기 {bad!r}; 권장 {good!r}",category="term_variant")
    semantic_source=KANA_RE.search(source_visible) or KANJI_RE.search(source_visible)
    if semantic_source and not HANGUL_RE.search(target_visible) and target_visible.strip():add_issue(issues,entry,script,"REVIEW","NO_HANGUL","일본어 의미 문장인데 한글이 없음",category="no_hangul")
    source_length,target_length=max(1,len(source_visible.strip())),len(target_visible.strip());ratio=target_length/source_length
    if source_length>=12 and (ratio<0.25 or ratio>2.7):add_issue(issues,entry,script,"REVIEW","LENGTH_RATIO","번역 길이 비율 극단값",{"ratio":round(ratio,3),"source_len":source_length,"target_len":target_length},category="length_ratio")

def audit_ui_old_key_conflicts(records,issues):
    groups=collections.defaultdict(list)
    for script,entry in records:
        if script!="system_ui":continue
        old,target=str(entry.get("source_jp") or ""),str(entry.get("draft_ko") or "");groups[old].append((script,entry,target))
    for old,rows in groups.items():
        targets=sorted({target for _,_,target in rows})
        if len(targets)>1:
            script,entry,_=rows[0];add_issue(issues,entry,script,"HARD","UI_GLOBAL_OLD_CONFLICT","동일한 decoded UI old key에 서로 다른 한국어 target",{"old":old,"targets":targets,"contexts":len(rows)})
def build_open_gate(issues):
    open_issues=[item for item in issues if item.get("status","open")=="open"];totals=collections.Counter(item.get("policy_severity") for item in issues);opened=collections.Counter(item.get("policy_severity") for item in open_issues);hard_open,review_open=opened.get("HARD",0),opened.get("REVIEW",0)
    return {"hard_total":totals.get("HARD",0),"review_total":totals.get("REVIEW",0),"info_total":totals.get("INFO",0),"hard_open":hard_open,"review_open":review_open,"info_open":opened.get("INFO",0),"pass":hard_open==0 and review_open==0}

def audit_master_directory(master_dir:Path,out:Path,*,ruby_map=None,cjk_allowlist=()):
    files=sorted(master_dir.glob("*.master.json"))
    if not files:raise ValueError(f"no JSON masters in {master_dir}")
    issues=[];seen_ids={};files_report=[];all_records=[];total=0
    for path in files:
        document=json.loads(path.read_text(encoding="utf-8-sig"));entries=load_entries(path)
        script=(document.get("script_key") if isinstance(document,dict) else None) or path.name.removesuffix(".master.json")
        total+=len(entries);sequences=[]
        for entry in entries:
            sequence=entry.get("sequence") or entry.get("command_index");sequences.append(sequence);stable_id=entry.get("stable_id")
            if stable_id:
                if stable_id in seen_ids:add_issue(issues,entry,script,"HARD","DUPLICATE_ASSIGNMENT","master 전체 stable_id 중복",{"first":seen_ids[stable_id]},category="duplicate_stable_id")
                else:seen_ids[stable_id]=(script,sequence)
            if entry.get("english_reference_used") not in (False,None):add_issue(issues,entry,script,"HARD","ENGLISH_NEW_PROVENANCE_VIOLATION","english_reference_used가 false가 아님",category="source_contract")
            if entry.get("external_translation_api_used") not in (False,None):add_issue(issues,entry,script,"HARD","SOURCE_CONTRACT_VIOLATION","external_translation_api_used가 false가 아님",category="source_contract")
            audit_entry(entry,script,issues,ruby_map=ruby_map,cjk_allowlist=cjk_allowlist);all_records.append((script,entry))
        files_report.append({"path":str(path.resolve()),"sha256":sha256(path),"entries":len(entries),"sequence_min":min((v for v in sequences if isinstance(v,int)),default=None),"sequence_max":max((v for v in sequences if isinstance(v,int)),default=None)})
    audit_ui_old_key_conflicts(all_records,issues);category_counts=collections.Counter(item["category"] for item in issues);severity_counts=collections.Counter(item["severity"] for item in issues);policy_counts=collections.Counter(item["policy_severity"] for item in issues);rule_counts=collections.Counter(item["rule_id"] for item in issues)
    report={"schema_version":"fatal-twelve-consolidated-static-qa-v1","policy_schema_version":"fatal-twelve-validator-policy-v1","master_dir":str(master_dir.resolve()),"files":files_report,"entry_count":total,"issue_count":len(issues),"severity_counts":dict(sorted(severity_counts.items())),"policy_severity_counts":dict(sorted(policy_counts.items())),"category_counts":dict(sorted(category_counts.items())),"rule_id_counts":dict(sorted(rule_counts.items())),"gate":build_open_gate(issues),"issues":issues}
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");tsv=out.with_suffix(".tsv")
    with tsv.open("w",encoding="utf-8",newline="\n") as fh:
        fh.write("severity\tcategory\tscript\tsequence\tstable_id\tsource_line\tmessage\tsource_jp\tdraft_ko\trule_id\tpolicy_severity\tstatus\tfinding_id\n")
        for item in issues:
            keys=("severity","category","script","sequence","stable_id","source_line","message","source_jp","draft_ko","rule_id","policy_severity","status","finding_id");values=[item.get(key,"") for key in keys]
            fh.write("\t".join(str(value).replace("\t","\\t").replace("\r","").replace("\n","\\n") for value in values)+"\n")
    return report

def main(argv:Sequence[str]|None=None)->int:
    parser=argparse.ArgumentParser();parser.add_argument("master_dir",type=Path);parser.add_argument("--out",type=Path,required=True);parser.add_argument("--ruby-map",type=Path);parser.add_argument("--cjk-allow",action="append",default=[]);args=parser.parse_args(argv)
    try:report=audit_master_directory(args.master_dir,args.out,ruby_map=load_ruby_map(args.ruby_map),cjk_allowlist=args.cjk_allow)
    except ValueError as exc:raise SystemExit(str(exc)) from exc
    print(json.dumps({"entries":report["entry_count"],"issues":report["issue_count"],"severities":report["severity_counts"],"policy_severities":report["policy_severity_counts"],"gate":report["gate"],"json":str(args.out),"tsv":str(args.out.with_suffix(".tsv"))},ensure_ascii=False));return 0
if __name__=="__main__":raise SystemExit(main())
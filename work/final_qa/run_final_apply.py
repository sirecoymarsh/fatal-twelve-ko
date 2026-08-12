#!/usr/bin/env python3
"""Hash-bound complete correction/apply/audit/render wrapper for Fatal Twelve."""
from __future__ import annotations

import argparse, collections, copy, json, re, sys
from argparse import Namespace
from pathlib import Path
from typing import Any

import apply_corrections, audit_master, render_final_scenario
from final_qa_common import file_sha256, read_json, text_sha256, token_validation_findings, write_json

HERE=Path(__file__).resolve().parent
REPO_ROOT=HERE.parents[1]
MANIFEST_SCHEMA="fatal-twelve-global-correction-manifest-v1"
OVERLAY_SCHEMA="fatal-twelve-structural-overlay-spec-v1"
APPROVAL_SCHEMA="fatal-twelve-record-bound-qa-approvals-v1"
HEX64_RE=re.compile(r"[0-9a-fA-F]{64}\Z")
REVIEWERS=("A","B","C","ROOT")
SCHEMA_INDEX="fatal-twelve-master-index-v1"
SCHEMA_GROUPS="fatal-twelve-review-group-manifest-v1"
SCHEMA_UI="fatal-twelve-system-ui-master-v1"
N_SCENARIO_MASTERS=29
N_SCENARIO=18184
N_UI=732
N_UI_CONTEXTS=739
N_ALL=18916
N_SCENARIO_MENU=58
N_SCENARIO_OLD=53
N_MASTER_MENU=790
N_MASTER_OLD=785
N_SUPPLEMENT=12
N_FINAL_OLD=797
N_TRANSLATE=18126

class FinalApplyError(ValueError): pass

def require_sha(path:Path,expected:Any,label:str)->str:
    if not isinstance(expected,str) or not HEX64_RE.fullmatch(expected):
        raise FinalApplyError(f"{label}: sha256 must be 64 hex characters")
    actual=file_sha256(path)
    if actual.lower()!=expected.lower():
        raise FinalApplyError(f"{label}: SHA-256 mismatch: expected {expected}, got {actual}")
    return actual

def resolve_input(value:Any,manifest_path:Path,label:str)->Path:
    if not isinstance(value,str) or not value: raise FinalApplyError(f"{label}: invalid path")
    raw=Path(value)
    if raw.is_absolute(): result=raw.resolve()
    else:
        candidates=[(REPO_ROOT/raw).resolve(),(manifest_path.parent/raw).resolve()]
        existing=[]
        for p in candidates:
            if p.exists() and p not in existing: existing.append(p)
        if len(existing)>1: raise FinalApplyError(f"{label}: ambiguous relative path {value!r}")
        result=existing[0] if existing else candidates[0]
    if not result.is_file(): raise FinalApplyError(f"{label}: missing file {result}")
    return result

def read_jsonl(path:Path,label:str)->list[dict[str,Any]]:
    rows=[]
    with path.open("r",encoding="utf-8-sig") as fh:
        for line_no,line in enumerate(fh,1):
            if not line.strip(): continue
            try: row=json.loads(line)
            except json.JSONDecodeError as exc: raise FinalApplyError(f"{label}:{line_no}: {exc}") from exc
            if not isinstance(row,dict): raise FinalApplyError(f"{label}:{line_no}: record must be object")
            row=copy.deepcopy(row);row["_line"]=line_no;rows.append(row)
    return rows

def validate_bootstrap(path:Path)->dict[str,Any]:
    try: text=path.read_bytes().decode("utf-8","strict")
    except UnicodeDecodeError as exc: raise FinalApplyError(f"bootstrap not strict UTF-8: {exc}") from exc
    required=['label "\uc5b8\uc5b4":','textbutton "\u65e5\u672c\u8a9e":','textbutton "\ud55c\uad6d\uc5b4":']
    if any(x not in text for x in required): raise FinalApplyError("bootstrap language literals missing")
    return {"path":str(path.resolve()),"sha256":file_sha256(path),"strict_utf8":True,
            "language_label":"\uc5b8\uc5b4","japanese_button":"\u65e5\u672c\u8a9e","korean_button":"\ud55c\uad6d\uc5b4"}

def load_bases(index_path:Path,groups_path:Path,ui_path:Path):
    idx=read_json(index_path)
    refs=idx.get("masters") if isinstance(idx,dict) and idx.get("schema_version")==SCHEMA_INDEX else None
    if not isinstance(refs,list) or len(refs)!=N_SCENARIO_MASTERS: raise FinalApplyError("scenario index must contain 29 masters")
    docs={};stable={};base_target={};order={};scenario_count=0;menu_count=0;old_targets=collections.defaultdict(set)
    combined_refs=[]
    for rank,ref in enumerate(refs):
        key=ref.get("script_key");raw=Path(ref.get("path",""));p=(raw if raw.is_absolute() else REPO_ROOT/raw).resolve()
        if not isinstance(key,str) or not p.is_file(): raise FinalApplyError("invalid scenario master reference")
        require_sha(p,ref.get("sha256"),f"master {key}");doc=read_json(p);entries=doc.get("entries")
        if doc.get("script_key")!=key or not isinstance(entries,list): raise FinalApplyError(f"{key}: invalid master")
        docs[key]=doc;order[key]=rank;scenario_count+=len(entries)
        for seq,e in enumerate(entries,1):
            sid=e.get("stable_id")
            if e.get("sequence")!=seq or not isinstance(sid,str) or sid in stable: raise FinalApplyError(f"{key}:{seq}: identity failure")
            stable[sid]=(key,seq);base_target[sid]=e.get("draft_ko")
            if e.get("menu_key") is not None:
                menu_count+=1;old_targets[str(e.get("source_jp"))].add(str(e.get("draft_ko")))
        combined_refs.append(copy.deepcopy(ref))
    if (scenario_count,menu_count,len(old_targets))!=(N_SCENARIO,N_SCENARIO_MENU,N_SCENARIO_OLD):
        raise FinalApplyError(f"scenario counts mismatch: {(scenario_count,menu_count,len(old_targets))}")
    if any(len(v)!=1 for v in old_targets.values()): raise FinalApplyError("base scenario old-key target conflict")

    ui=read_json(ui_path);entries=ui.get("entries") if isinstance(ui,dict) else None
    if (ui.get("schema_version")!=SCHEMA_UI or not isinstance(entries,list) or len(entries)!=N_UI
        or ui.get("unique_runtime_string_keys")!=N_UI or ui.get("input_catalog_records")!=N_UI_CONTEXTS):
        raise FinalApplyError("UI master is not 732-key/739-context reviewed input")
    ui_old=set();docs["system_ui"]=ui;order["system_ui"]=len(order)
    for seq,e in enumerate(entries,1):
        sid=e.get("stable_id")
        if e.get("sequence")!=seq or not isinstance(sid,str) or sid in stable: raise FinalApplyError(f"system_ui:{seq}: identity failure")
        if token_validation_findings(e,e.get("draft_ko")): raise FinalApplyError(f"system_ui:{seq}: legacy token failure")
        stable[sid]=("system_ui",seq);base_target[sid]=e.get("draft_ko");ui_old.add(e.get("source_jp"))
    if len(ui_old)!=N_UI or set(old_targets)&ui_old: raise FinalApplyError("UI old-key uniqueness/overlap failure")
    combined_refs.append({"script_key":"system_ui","kind":"system_ui_strings","path":str(ui_path.resolve()),
                          "sha256":file_sha256(ui_path),"catalog_records":N_UI_CONTEXTS,
                          "selected_unique_records":N_UI,"coverage_complete":True,"complete":True})
    combined_index=copy.deepcopy(idx);combined_index["masters"]=combined_refs
    combined_index["combined_summary"]={"scenario_masters":29,"scenario_records":N_SCENARIO,
        "system_ui_masters":1,"system_ui_records":N_UI,"system_ui_contexts":N_UI_CONTEXTS,
        "combined_masters":30,"combined_records":N_ALL}

    groups=read_json(groups_path)
    if not isinstance(groups,dict) or groups.get("schema_version")!=SCHEMA_GROUPS: raise FinalApplyError("invalid review groups")
    combined_groups=copy.deepcopy(groups);assignment={};ag=None
    for group in combined_groups.get("groups",[]):
        reviewer=group.get("group_id")
        if reviewer not in REVIEWERS or not isinstance(group.get("scripts"),list): raise FinalApplyError("invalid review group")
        if reviewer=="A": ag=group
        for item in group["scripts"]:
            key=item.get("script_key")
            if key in assignment: raise FinalApplyError(f"duplicate assignment {key}")
            assignment[key]=reviewer
    if set(assignment)!=set(docs)-{"system_ui"} or ag is None: raise FinalApplyError("scenario review coverage mismatch")
    ag["scripts"].append({"script_key":"system_ui","expected_records":N_UI});ag["expected_records"]=int(ag.get("expected_records",0))+N_UI
    assignment["system_ui"]="A"
    return combined_index,combined_groups,docs,stable,base_target,assignment,order

def load_bound_item(item,manifest_path,label,schema):
    if not isinstance(item,dict): raise FinalApplyError(f"{label}: missing manifest item")
    p=resolve_input(item.get("path"),manifest_path,label);sha=require_sha(p,item.get("sha256"),label);doc=read_json(p)
    rows=doc.get("entries") if isinstance(doc,dict) and doc.get("schema_version")==schema else None
    if not isinstance(rows,list) or not all(isinstance(x,dict) for x in rows): raise FinalApplyError(f"{label}: schema/entries failure")
    if item.get("records") is not None and item["records"]!=len(rows): raise FinalApplyError(f"{label}: record guard failure")
    return p,doc,rows,{"path":str(p),"sha256":sha,"records":len(rows),"schema_version":schema}
def load_canonical(manifest,manifest_path,docs,stable,base_target,assignment):
    items=manifest.get("correction_files")
    if not isinstance(items,list) or not items: raise FinalApplyError("correction_files must be nonempty array")
    canonical={};inputs=[];duplicates=0
    for idx,item in enumerate(items,1):
        if not isinstance(item,dict): raise FinalApplyError(f"correction_files[{idx}] invalid")
        reviewer=item.get("reviewer") or item.get("group")
        if item.get("reviewer") and item.get("group") and item["reviewer"]!=item["group"]: raise FinalApplyError("reviewer/group mismatch")
        if reviewer not in REVIEWERS: raise FinalApplyError(f"unknown reviewer {reviewer!r}")
        p=resolve_input(item.get("path"),manifest_path,f"correction {idx}");sha=require_sha(p,item.get("sha256"),f"correction {idx}")
        rows=read_jsonl(p,f"correction {idx}")
        if item.get("records") is not None and item["records"]!=len(rows): raise FinalApplyError(f"correction {idx}: record count")
        inputs.append({"reviewer":reviewer,"path":str(p),"sha256":sha,"records":len(rows)})
        for row in rows:
            sid,old,new=row.get("stable_id"),row.get("old_ko"),row.get("new_ko")
            if not isinstance(sid,str) or not isinstance(old,str) or not isinstance(new,str) or not new or old==new:
                raise FinalApplyError(f"{p}:{row['_line']}: invalid correction")
            if sid not in stable: raise FinalApplyError(f"{p}: unknown stable_id {sid}")
            script,seq=stable[sid]
            apply_reviewer=assignment[script]
            # Manifest reviewer is review provenance. apply_corrections.py uses
            # the fixed ownership group, which differs for the C-reviewed 011_01*
            # files (owned by group B).
            if row.get("reviewer",reviewer)!=reviewer: raise FinalApplyError(f"{p}: embedded reviewer mismatch")
            if row.get("script_key",row.get("script",script))!=script or row.get("sequence",seq)!=seq:
                raise FinalApplyError(f"{p}: script/sequence guard failure {sid}")
            if old!=base_target[sid]: raise FinalApplyError(f"{p}: old_ko guard failure {sid}")
            entry=docs[script]["entries"][seq-1]
            findings=token_validation_findings(entry,new)
            if findings: raise FinalApplyError(f"{p}: protected token failure {sid}: {json.dumps(findings,ensure_ascii=False)}")
            out={"reviewer":apply_reviewer,"script_key":script,"sequence":seq,"stable_id":sid,"old_ko":old,"new_ko":new,
                 "_sources":[{"path":str(p),"sha256":sha,"line":row["_line"],"provenance_reviewer":reviewer}]}
            note=row.get("note") or row.get("reason")
            if isinstance(note,str) and note: out["note"]=note
            prior=canonical.get(sid)
            if prior is None: canonical[sid]=out
            elif all(prior[k]==out[k] for k in ("reviewer","script_key","sequence","old_ko","new_ko")):
                prior["_sources"].extend(out["_sources"]);duplicates+=1
            else: raise FinalApplyError(f"conflicting duplicate correction {sid}")
    return canonical,inputs,duplicates

def apply_overlay(item,manifest_path,canonical,docs,stable,base_target,assignment):
    p,doc,rows,ref=load_bound_item(item,manifest_path,"structural overlay",OVERLAY_SCHEMA)
    embedded_mode=item.get("status")=="fully_merged_into_canonical_correction_rows"
    seen=set();created=rebased=embedded=0
    for pos,o in enumerate(rows,1):
        sid=o.get("stable_id")
        if not isinstance(sid,str) or sid in seen or sid not in stable: raise FinalApplyError(f"overlay {pos}: stable_id failure")
        seen.add(sid);script,seq=stable[sid];entry=docs[script]["entries"][seq-1]
        if o.get("script")!=script or o.get("sequence")!=seq or o.get("source_jp_sha256")!=text_sha256(entry["source_jp"]):
            raise FinalApplyError(f"overlay {pos}: source/script guard failure")
        expected,final=o.get("expected_after_semantic"),o.get("final_ko")
        if (not isinstance(expected,str) or not isinstance(final,str)
            or o.get("expected_after_semantic_sha256")!=text_sha256(expected)
            or o.get("final_ko_sha256")!=text_sha256(final)):
            raise FinalApplyError(f"overlay {pos}: target hash guard failure")
        current=canonical.get(sid);current_target=current["new_ko"] if current else base_target[sid]
        if token_validation_findings(entry,final): raise FinalApplyError(f"overlay {pos}: protected token failure")
        if embedded_mode:
            if current is None or current_target!=final:
                raise FinalApplyError(f"overlay {pos}: manifest claims merged but canonical final target differs {sid}")
            embedded+=1
        elif current_target!=expected:
            raise FinalApplyError(f"overlay {pos}: expected-after-semantic guard failure {sid}")
        elif current is None:
            if final==base_target[sid]: raise FinalApplyError(f"overlay {pos}: no-op")
            current={"reviewer":assignment[script],"script_key":script,"sequence":seq,"stable_id":sid,
                     "old_ko":base_target[sid],"new_ko":final,"note":o.get("reason","guarded structural overlay"),"_sources":[]}
            canonical[sid]=current;created+=1
        elif not embedded_mode:
            current["new_ko"]=final;rebased+=1
        current["_overlay"]={"path":str(p),"sha256":ref["sha256"],"entry":pos,"transforms":o.get("transforms"),
                             "reviewer":o.get("reviewer"),"reason":o.get("reason")}
    ref["manifest_status"]=item.get("status")
    return ref,rows,created,rebased,embedded

def load_approvals(item,manifest_path,docs,stable,final_target):
    p,doc,rows,ref=load_bound_item(item,manifest_path,"approval ledger",APPROVAL_SCHEMA)
    if doc.get("blanket_approvals") is not False: raise FinalApplyError("blanket approvals must be false")
    keys=set()
    for pos,a in enumerate(rows,1):
        sid,rule=a.get("stable_id"),a.get("rule_id")
        if not isinstance(sid,str) or sid not in stable or not isinstance(rule,str): raise FinalApplyError(f"approval {pos}: identity")
        script,seq=stable[sid];entry=docs[script]["entries"][seq-1]
        expected_scope="system_ui" if script=="system_ui" else "scenario"
        if (a.get("scope") not in (None,expected_scope) or a.get("script")!=script
            or a.get("sequence")!=seq or a.get("source_sha256")!=text_sha256(entry["source_jp"])
            or a.get("target_sha256")!=text_sha256(final_target[sid])):
            raise FinalApplyError(f"approval {pos}: exact guard failure")
        if (sid,rule) in keys: raise FinalApplyError(f"approval {pos}: duplicate key")
        keys.add((sid,rule))
    return p,rows,ref

def load_supplement(manifest,manifest_path):
    items=manifest.get("supplemental_strings")
    if not isinstance(items,list) or len(items)!=1: raise FinalApplyError("exactly one supplemental_strings item required")
    item=items[0]
    if not isinstance(item,dict): raise FinalApplyError("invalid supplemental item")
    p=resolve_input(item.get("path"),manifest_path,"supplemental strings")
    sha=require_sha(p,item.get("sha256"),"supplemental strings")
    pairs,parsed=render_final_scenario.parse_supplemental_strings(p)
    romans=("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")
    expected=[(f"Numeral {r}",f"\ubc88\ud638 {r}") for r in romans]
    if [(x["old"],x["target"]) for x in pairs]!=expected or len(pairs)!=N_SUPPLEMENT:
        raise FinalApplyError("Numeral supplement must be exact I-XII mapping")
    if item.get("pairs") is not None and item["pairs"]!=len(pairs): raise FinalApplyError("supplement pair guard")
    return [p],[{**parsed,"sha256":sha,"expected_numeral_pairs_exact":True}]

def validate_ui_report(path,ui_path,canonical,supplements):
    r=read_json(path);scope=r.get("scope",{});contract=r.get("source_contract",{});struct=r.get("structural_validation",{})
    if not isinstance(r,dict) or r.get("schema_version")!="fatal-twelve-system-ui-manual-review-v1" or r.get("verdict")!="PASS":
        raise FinalApplyError("invalid UI review report")
    if (scope.get("entries_reviewed"),scope.get("contexts_reviewed"),scope.get("unique_runtime_old_keys"))!=(N_UI,N_UI_CONTEXTS,N_UI):
        raise FinalApplyError("UI report coverage")
    for k in ("official_english_new_prose_used","external_translation_api_used","game_executed","master_modified"):
        if contract.get(k) is not False: raise FinalApplyError(f"UI source/runtime contract {k}")
    if r.get("input",{}).get("sha256")!=file_sha256(ui_path): raise FinalApplyError("UI report master hash")
    expected_struct={
        "sequence_contiguous_1_732":True,
        "fullwidth_digits_remaining":0,
        "u3000_remaining":0,
        "embedded_newline_counts_exact":True,
        "tab_counts_exact":True,
        "interpolation_multisets_exact":True,
        "printf_percent_multisets_exact":True,
        "renpy_tag_multisets_exact":True,
        "roman_numeral_multisets_exact":True,
        "nfkc_arabic_number_multisets_exact":True,
        "same_old_key_target_conflicts":0,
    }
    if struct!=expected_struct: raise FinalApplyError("UI structural report mismatch")
    cref=r.get("corrections",{});cp=Path(cref.get("path",""))
    if not cp.is_file(): raise FinalApplyError("UI reviewed correction file missing")
    require_sha(cp,cref.get("sha256"),"UI reviewed corrections");rows=read_jsonl(cp,"UI reviewed corrections")
    if len(rows)!=167 or cref.get("records")!=167: raise FinalApplyError("UI correction count")
    expected=set()
    for row in rows:
        sid=row.get("stable_id");expected.add(sid);actual=canonical.get(sid)
        if actual is None or (actual["old_ko"],actual["new_ko"])!=(row.get("old_ko"),row.get("new_ko")):
            raise FinalApplyError(f"missing reviewed UI correction {sid}")
    actual={sid for sid,row in canonical.items() if row["script_key"]=="system_ui"}
    if actual!=expected: raise FinalApplyError("unreviewed extra/missing UI corrections")
    sup=r.get("numeral_composed_supplement",{})
    if (sup.get("supplemental_pairs"),sup.get("expected_pairs_exact"),sup.get("old_key_conflicts_with_master"))!=(12,True,0):
        raise FinalApplyError("UI supplement report")
    if len(supplements)!=1 or supplements[0]["sha256"]!=sup.get("sha256"): raise FinalApplyError("UI supplement hash")
    return {"path":str(path.resolve()),"sha256":file_sha256(path),"verdict":"PASS","entries_reviewed":N_UI,
            "contexts_reviewed":N_UI_CONTEXTS,"corrections":167}
def apply_approvals(report,rows,ref):
    issues=copy.deepcopy(report.get("issues",[]));used=set();applied=[];keys=set()
    for pos,a in enumerate(rows,1):
        sid,rule=a.get("stable_id"),a.get("rule_id");source=a.get("source_sha256");target=a.get("target_sha256")
        scope=a.get("scope")
        if (scope not in (None,"scenario","system_ui") or not all(isinstance(x,str) and x for x in (sid,rule,source,target,a.get("reviewer"),a.get("reason")))
            or a.get("status","approved")!="approved"):
            raise FinalApplyError(f"approval {pos}: invalid fields")
        if (sid,rule) in keys: raise FinalApplyError(f"approval {pos}: duplicate key")
        keys.add((sid,rule))
        matches=[i for i in issues if i.get("stable_id")==sid and i.get("rule_id")==rule
                 and text_sha256(str(i.get("source_jp") or ""))==source and text_sha256(str(i.get("draft_ko") or ""))==target
                 and (a.get("finding_id") is None or i.get("finding_id")==a.get("finding_id"))]
        if len(matches)!=1: raise FinalApplyError(f"approval {pos} matched {len(matches)} findings, expected 1")
        issue=matches[0];fid=issue.get("finding_id")
        if fid in used: raise FinalApplyError(f"finding approved twice {fid}")
        used.add(fid);issue["status"]="approved";issue["approval"]={"ledger_path":ref["path"],"ledger_sha256":ref["sha256"],
            "ledger_entry":pos,"reviewer":a["reviewer"],"reason":a["reason"],"source_sha256":source,"target_sha256":target}
        applied.append({"ledger_entry":pos,"stable_id":sid,"rule_id":rule,"finding_id":fid,"reviewer":a["reviewer"]})
    out=copy.deepcopy(report);out["issues"]=issues;out["gate"]=audit_master.build_open_gate(issues)
    out["scenario_gate"]=audit_master.build_open_gate([i for i in issues if i.get("script")!="system_ui"])
    out["system_ui_gate"]=audit_master.build_open_gate([i for i in issues if i.get("script")=="system_ui"])
    out["approval_ledger"]=ref;out["record_bound_approvals_applied"]=applied;out["record_bound_approval_count"]=len(applied)
    return out

def write_tsv(path,issues):
    keys=("severity","category","script","sequence","stable_id","source_line","message","source_jp","draft_ko",
          "rule_id","policy_severity","status","finding_id")
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="\n") as fh:
        fh.write("\t".join(keys)+"\n")
        for i in issues:
            vals=[str(i.get(k,"")).replace("\t","\\t").replace("\r","").replace("\n","\\n") for k in keys]
            fh.write("\t".join(vals)+"\n")

def run(args):
    manifest_path=args.manifest.resolve()
    if not manifest_path.is_file(): raise FinalApplyError(f"missing global manifest {manifest_path}")
    manifest=read_json(manifest_path)
    if not isinstance(manifest,dict) or manifest.get("schema_version")!=MANIFEST_SCHEMA:
        raise FinalApplyError(f"manifest schema must be {MANIFEST_SCHEMA}")
    output=args.output_root.resolve()
    if output.exists() and any(output.iterdir()): raise FinalApplyError(f"output root must be absent or empty: {output}")
    paths={k:getattr(args,k).resolve() for k in ("master_index","review_groups","system_ui_master","system_ui_report","ruby_map","bootstrap")}
    for k,p in paths.items():
        if not p.is_file(): raise FinalApplyError(f"{k} missing: {p}")
    combined_index,combined_groups,docs,stable,base_target,assignment,order=load_bases(
        paths["master_index"],paths["review_groups"],paths["system_ui_master"])
    policy_items=manifest.get("policy_artifacts")
    if not isinstance(policy_items,list): policy_items=[]
    policy={item.get("kind"):item for item in policy_items if isinstance(item,dict)}
    overlay_item=manifest.get("structural_overlay") or policy.get("structural_overlay_spec")
    approval_item=(manifest.get("approval_ledger") or manifest.get("audit_approval_ledger")
                   or policy.get("record_bound_qa_approvals"))
    ruby_item=policy.get("ruby_map")
    if not isinstance(ruby_item,dict):
        raise FinalApplyError("manifest must bind ruby_map policy artifact")
    ruby_bound=resolve_input(ruby_item.get("path"),manifest_path,"ruby map policy artifact")
    if ruby_bound.resolve()!=paths["ruby_map"].resolve():
        raise FinalApplyError("manifest ruby map path differs from CLI ruby map")
    require_sha(ruby_bound,ruby_item.get("sha256"),"ruby map policy artifact")
    if ruby_item.get("entries")!=52: raise FinalApplyError("ruby map manifest count must be 52")

    canonical,correction_inputs,duplicates=load_canonical(manifest,manifest_path,docs,stable,base_target,assignment)
    overlay_ref,overlay_rows,overlay_created,overlay_rebased,overlay_embedded=apply_overlay(
        overlay_item,manifest_path,canonical,docs,stable,base_target,assignment)
    final_target=base_target.copy()
    for sid,row in canonical.items(): final_target[sid]=row["new_ko"]
    _,approval_rows,approval_ref=load_approvals(approval_item,manifest_path,docs,stable,final_target)
    supplement_paths,supplement_reports=load_supplement(manifest,manifest_path)
    ui_summary=validate_ui_report(paths["system_ui_report"],paths["system_ui_master"],canonical,supplement_reports)
    bootstrap_summary=validate_bootstrap(paths["bootstrap"])
    ruby=read_json(paths["ruby_map"])
    if not isinstance(ruby,dict) or len(ruby.get("entries",[]))!=52:
        raise FinalApplyError("approved ruby map must contain 52 entries")

    prepared=output/"prepared";merged_dir=prepared/"corrections";merged_dir.mkdir(parents=True,exist_ok=True)
    index_out=prepared/"master_index.with_system_ui.json";groups_out=prepared/"review_group_manifest.with_system_ui.json"
    write_json(index_out,combined_index);write_json(groups_out,combined_groups)
    by_reviewer={r:[] for r in REVIEWERS}
    for sid,row in canonical.items():
        outrow={k:row[k] for k in ("reviewer","script_key","sequence","stable_id","old_ko","new_ko")}
        if isinstance(row.get("note"),str) and row["note"]: outrow["note"]=row["note"]
        by_reviewer[row["reviewer"]].append(outrow)
    merged=[];specs=[]
    for reviewer in REVIEWERS:
        rows=sorted(by_reviewer[reviewer],key=lambda x:(order[x["script_key"]],x["sequence"],x["stable_id"]))
        if not rows: continue
        p=merged_dir/f"{reviewer}.final.corrections.jsonl"
        with p.open("w",encoding="utf-8",newline="\n") as fh:
            for row in rows: fh.write(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n")
        merged.append({"reviewer":reviewer,"path":str(p.resolve()),"sha256":file_sha256(p),"records":len(rows)})
        specs.append(f"{reviewer}={p.resolve()}")

    preflight={"schema_version":"fatal-twelve-final-apply-preflight-v1",
      "global_manifest":{"path":str(manifest_path),"sha256":file_sha256(manifest_path),"schema_version":MANIFEST_SCHEMA},
      "source_contract":{"semantic_authority":"Japanese only","official_english_new_prose_used":False,
        "external_translation_api_used":False,"game_executed":False,"source_masters_modified":False},
      "inputs":{"scenario_master_index":{"path":str(paths["master_index"]),"sha256":file_sha256(paths["master_index"]),
          "masters":29,"records":N_SCENARIO},
        "system_ui_master":{"path":str(paths["system_ui_master"]),"sha256":file_sha256(paths["system_ui_master"]),
          "records":N_UI,"contexts":N_UI_CONTEXTS},
        "review_groups":{"path":str(paths["review_groups"]),"sha256":file_sha256(paths["review_groups"])},
        "ruby_map":{"path":str(paths["ruby_map"]),"sha256":file_sha256(paths["ruby_map"]),"entries":52},
        "correction_files":correction_inputs,"structural_overlay":overlay_ref,"approval_ledger":approval_ref,
        "supplemental_strings":supplement_reports,"system_ui_review":ui_summary,"bootstrap":bootstrap_summary},
      "canonical_corrections":{"records":len(canonical),"semantic_duplicates_collapsed":duplicates,
        "overlay_records":len(overlay_rows),"overlay_created_new_rows":overlay_created,
        "overlay_rebased_existing_rows":overlay_rebased,"overlay_already_embedded_rows":overlay_embedded,
        "system_ui_records":sum(row["script_key"]=="system_ui" for row in canonical.values()),"merged_files":merged},
      "expected_final_render":{"input_masters":30,"scenario_scripts":29,"system_ui_string_masters":1,"records":N_ALL,
        "translate_blocks":N_TRANSLATE,"menu_occurrences":N_MASTER_MENU,"unique_master_old_keys":N_MASTER_OLD,
        "supplemental_pairs":N_SUPPLEMENT,"total_unique_global_old_keys":N_FINAL_OLD,"menu_target_conflicts":0},
      "preflight_pass":True}
    preflight_path=prepared/"preflight_report.json";write_json(preflight_path,preflight)
    if args.preflight_only:
        return {"status":"preflight_only_pass","preflight_report":str(preflight_path),
                "preflight_report_sha256":file_sha256(preflight_path),"prepared_master_index":str(index_out),
                "prepared_review_groups":str(groups_out),"merged_corrections":merged}
    corrected=output/"corrected"
    applied,code=apply_corrections.apply(Namespace(master_index=index_out,review_groups=groups_out,correction=specs,output_root=corrected))
    summary=applied["summary"]
    if (code or summary.get("scripts")!=30 or summary.get("records")!=N_ALL or summary.get("ready_for_final_render") is not True
        or summary.get("remaining_runtime_or_protected_token_failed_records")!=0 or summary.get("source_masters_modified") is not False):
        raise FinalApplyError("corrected masters not render-ready: "+json.dumps(summary,ensure_ascii=False))

    audit_dir=output/"audit";raw_path=audit_dir/"final_static_qa.raw.json"
    raw=audit_master.audit_master_directory(corrected/"masters",raw_path,
        ruby_map=audit_master.load_ruby_map(paths["ruby_map"]))
    approved=apply_approvals(raw,approval_rows,approval_ref)
    approved_path=audit_dir/"final_static_qa.approved.json";write_json(approved_path,approved)
    write_tsv(approved_path.with_suffix(".tsv"),approved["issues"])
    gate={"schema_version":"fatal-twelve-final-scenario-gate-v1","approval_ledger":approval_ref,
          "approvals_applied":approved["record_bound_approval_count"],"all_master_gate":approved["gate"],
          "scenario_gate":approved["scenario_gate"],"system_ui_static_gate":approved["system_ui_gate"],
          "system_ui_review":ui_summary,
          "pass":approved["gate"]["pass"] and approved["scenario_gate"]["pass"]
                 and approved["system_ui_gate"]["pass"] and ui_summary["verdict"]=="PASS"}
    gate_path=audit_dir/"scenario_gate.json";write_json(gate_path,gate)
    if gate["pass"] is not True:
        raise FinalApplyError("final scenario semantic gate open: "+json.dumps(approved["scenario_gate"],ensure_ascii=False))

    rendered=output/"final_rpy"
    render_result,render_code=render_final_scenario.render(Namespace(
        master_index=corrected/"corrected_master_index.json",supplemental_strings=supplement_paths,output_root=rendered))
    if render_code: raise FinalApplyError("renderer nonzero")
    rs=render_result["summary"]
    expected={"input_masters":30,"scripts":29,"system_ui_string_masters":1,"records":N_ALL,
      "translate_blocks":N_TRANSLATE,"menu_occurrences":N_MASTER_MENU,"unique_global_menu_old_keys":N_MASTER_OLD,
      "deduplicated_same_target_menu_occurrences":5,"supplemental_string_inputs":1,
      "supplemental_string_pairs":N_SUPPLEMENT,"supplemental_old_key_conflicts":0,
      "total_unique_global_old_keys":N_FINAL_OLD,"menu_target_conflicts":0}
    mismatch={k:{"expected":v,"actual":rs.get(k)} for k,v in expected.items() if rs.get(k)!=v}
    if mismatch: raise FinalApplyError("final render exact-count gate: "+json.dumps(mismatch,ensure_ascii=False))
    result={"schema_version":"fatal-twelve-final-text-pipeline-result-v1","status":"PASS","game_executed":False,
      "source_masters_modified":False,
      "preflight_report":{"path":str(preflight_path),"sha256":file_sha256(preflight_path)},
      "corrected_master_index":{"path":applied["corrected_master_index"],"sha256":applied["corrected_master_index_sha256"]},
      "correction_audit":{"path":applied["correction_audit"],"sha256":applied["correction_audit_sha256"]},
      "approved_static_audit":{"path":str(approved_path),"sha256":file_sha256(approved_path),
        "all_master_gate":approved["gate"],"scenario_gate":approved["scenario_gate"],
        "system_ui_gate":approved["system_ui_gate"],"record_bound_approvals":approved["record_bound_approval_count"]},
      "system_ui_review":ui_summary,
      "render_manifest":{"path":render_result["render_manifest"],"sha256":render_result["render_manifest_sha256"],"summary":rs},
      "global_strings":{"path":render_result["global_strings"],"sha256":render_result["global_strings_sha256"],
        "unique_old_keys":N_FINAL_OLD}}
    result_path=output/"final_text_pipeline_result.json";write_json(result_path,result)
    result["result_path"]=str(result_path);result["result_sha256"]=file_sha256(result_path)
    return result

def parse_args(argv):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest",type=Path,default=HERE/"reviews"/"global_correction_manifest.json")
    p.add_argument("--output-root",type=Path,required=True)
    p.add_argument("--master-index",type=Path,default=HERE/"output"/"master_index.json")
    p.add_argument("--review-groups",type=Path,default=HERE/"review_group_manifest.json")
    p.add_argument("--system-ui-master",type=Path,default=HERE/"output"/"masters"/"system_ui.master.json")
    p.add_argument("--system-ui-report",type=Path,default=HERE/"reviews"/"A.manual.system_ui.report.json")
    p.add_argument("--ruby-map",type=Path,default=HERE/"ruby_map.approved.json")
    p.add_argument("--bootstrap",type=Path,default=REPO_ROOT/"work"/"patch_architecture"/"skeleton"/"game"/"f12_korean_bootstrap.rpy")
    p.add_argument("--preflight-only",action="store_true")
    return p.parse_args(argv)

def main(argv=None):
    try: result=run(parse_args(sys.argv[1:] if argv is None else argv))
    except Exception as exc:
        print(json.dumps({"fatal_error":str(exc)},ensure_ascii=False,indent=2),file=sys.stderr);return 1
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0

if __name__=="__main__": raise SystemExit(main())
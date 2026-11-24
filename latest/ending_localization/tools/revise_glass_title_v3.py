"""User-directed three-string revision, rendered from original and installed narrowly."""
from pathlib import Path
import copy, hashlib, json, os, shutil, subprocess, sys
from install_fatal_endings_v2 import E,LIVE,GAME,DEST,FF,FP,now,sha,dump,read,run,packets,safe,stopped,inventory
sys.path.insert(0,str(E.parent/'raster_localization_20260927/deps'))
from PIL import Image,ImageFont
sys.stdout.reconfigure(encoding='utf8')
S=E/'subtitles_v3';C=E/'candidate_v3';Q=E/'review_v3';D=E/'delivery_v3'
OLD='181ff23bb5c1b102368ea37cada4fe2c92c374eebd6f57cce0752f67527c31c4'
CHANGES=[('ending_theme_title','「유리실」','「유리의 실」'),
         ('G07','유리실로 자아낸','유리의 실로 자아낸'),
         ('G20','유리실은 어긋나고','유리의 실은 어긋나고')]

def prepare():
    for p in [S,C,Q,D]:safe(p,E);p.mkdir(exist_ok=True)
    assert not (C/'ED_TRUE_KO_REVIEW.webm').exists(),'v3 already rendered; inspect it instead of overwriting'
    srcass=E/'subtitles_v2/ED_TRUE.ass';oldtext=srcass.read_text('utf8');text=oldtext
    for ident,before,after in CHANGES:
        assert text.count(before)==1,(ident,'Unexpected number of exact occurrences')
        text=text.replace(before,after)
    restored=text
    for ident,before,after in CHANGES:restored=restored.replace(after,before)
    assert restored==oldtext and '유리실' not in text
    ass=S/'ED_TRUE.ass';ass.write_text(text,'utf8')
    lyrics=read(E/'subtitles_v2/ED_TRUE_LYRICS.json');credits=read(E/'subtitles_v2/ED_TRUE_CREDITS.json')
    before_lyrics=copy.deepcopy(lyrics);before_credits=copy.deepcopy(credits)
    for ident,before,after in CHANGES:
        if ident.startswith('G'):
            row=next(r for r in lyrics if r['id']==ident);assert row['target_ko']==before
            row['target_ko']=after
            assert ImageFont.truetype('C:/Windows/Fonts/NotoSerifKR-VF.ttf',48).getlength(after)<1192
        else:
            rows=[r for r in credits['rows'] if r['ko']==before];assert len(rows)==1
            rows[0]['ko']=after
            assert ImageFont.truetype('C:/Windows/Fonts/NotoSerifKR-VF.ttf',rows[0]['font_size']).getlength(after)<rows[0]['max_width']
    for a,b in zip(before_lyrics,lyrics):
        assert {k:v for k,v in a.items() if k!='target_ko'}=={k:v for k,v in b.items() if k!='target_ko'}
    for a,b in zip(before_credits['rows'],credits['rows']):
        assert {k:v for k,v in a.items() if k!='ko'}=={k:v for k,v in b.items() if k!='ko'}
    dump(S/'ED_TRUE_LYRICS.json',lyrics);dump(S/'ED_TRUE_CREDITS.json',credits)
    oldqa=next(r for r in read(E/'review_v2/MEDIA_VALIDATION.json')['movies'] if r['asset']=='ED_TRUE')
    original=E/'source/movies/ED_TRUE.mkv';assert sha(original)==oldqa['source_sha256']
    out=C/'ED_TRUE_KO_REVIEW.webm'
    filterpath=str(ass).replace('\\','/').replace(':','\\:')
    print('Rendering ED_TRUE v3: title + G07 + G20; no other semantic/timing edits.',flush=True)
    run([FF,'-n','-v','error','-i',original,'-vf',"drawbox=x=0:y=0:w=iw:h=ih:color=black:t=fill,ass='"+filterpath+"'",
      '-map','0:v:0','-map','0:a:0','-c:v','libvpx','-b:v','12M','-crf','6','-qmin','0','-qmax','8',
      '-threads','6','-deadline','good','-cpu-used','3','-auto-alt-ref','0','-lag-in-frames','0',
      '-c:a','copy','-fps_mode','passthrough',out])
    movie=D/'ED_TRUE.mkv'
    run([FF,'-n','-v','error','-copyts','-i',out,'-map','0:v:0','-map','0:a:0','-c','copy',
      '-map_metadata','-1','-avoid_negative_ts','disabled',movie])
    original_audio=packets(original,'a');new_audio=packets(movie,'a')
    assert original_audio==new_audio
    for stream in ['v','a']:assert packets(out,stream)==packets(movie,stream)
    v0=packets(original,'v');v1=packets(movie,'v')
    assert [r['pts_time'] for r in v0]==[r['pts_time'] for r in v1]
    checked=subprocess.run([str(FF),'-v','error','-i',str(movie),'-f','null','-'],capture_output=True,creationflags=subprocess.CREATE_NO_WINDOW)
    assert checked.returncode==0 and not checked.stderr.strip(),checked.stderr
    times={r['id']:(r['start']+r['end'])/2 for r in lyrics if r['id'] in ['G07','G20']}
    cr=next(r for r in credits['rows'] if r['ko']=='「유리의 실」')
    times['ending_theme_title']=(cr['enter']+cr['exit'])/2
    frames=[]
    for ident,t in times.items():
        p=Q/f'{ident}.png';run([FF,'n' if False else '-y','-v','error','-ss',t,'-i',out,'-frames:v','1',p])
        assert Image.open(p).size==(1280,720)
        frames.append({'id':ident,'time':t,'path':str(p),'sha256':sha(p)})
    validation={'asset':'ED_TRUE','candidate':str(out),'sha256':sha(out),'bytes':out.stat().st_size,
      'source_sha256':oldqa['source_sha256'],'frame_count':len(v1),'video_pts_exact':True,'audio_packets_exact':True,
      'audio_packet_count':len(new_audio),'full_decode_errors':0,'size':[1280,720],'sample_frames':3,
      'lyric_cues':len(lyrics),'credit_cells':len(credits['rows']),'ass_sha256':sha(ass),
      'installed_container_candidate':str(movie),'installed_container_sha256':sha(movie),
      'source_fields_and_timings_unchanged':True,'only_three_ass_strings_changed':True,
      'remux_packet_data_and_timing_equal':True,'frames':frames,'runtime_playback_verified':False}
    dump(Q/'MEDIA_VALIDATION.json',validation)
    dump(E/'TITLE_DECISION_v3.json',{'created_at':now().isoformat(),'user_instruction':'유리실이라 하니까 유리방같은데 유리의 실이라고 해라',
      'source_title':'硝子の糸','canonical_korean_title':'유리의 실','translator_model':'Codex internal',
      'changes':[{'id':a,'before':b,'after':c} for a,b,c in CHANGES],
      'baseline_ass_sha256':sha(srcass),'revised_ass_sha256':sha(ass),'source_uncertainty_not_changed':True,
      'old_v2_media_and_provenance_preserved':True})
    shutil.copy2(__file__,E/'tools/revise_glass_title_v3.py')
    print(json.dumps(validation,ensure_ascii=False),flush=True)

def install():
    qa=read(Q/'MEDIA_VALIDATION.json');target=DEST/'ED_TRUE.mkv';safe(target,GAME)
    latest=read(E/'LATEST_INSTALL.json');assets=copy.deepcopy(latest['assets'])
    previous=next(r for r in assets if r['asset']=='ED_TRUE')
    assert previous['sha256']==OLD and sha(target)==OLD
    new=Path(qa['installed_container_candidate']);expected=qa['installed_container_sha256']
    assert sha(new)==expected and sha(Path(qa['candidate']))==qa['sha256']
    assert sha(S/'ED_TRUE.ass')==qa['ass_sha256']
    assert qa['only_three_ass_strings_changed'] and qa['full_decode_errors']==0
    for r in assets:assert sha(Path(r['target']))==r['sha256']
    op=read(E.parent/'opening_localization_20261002/LATEST_INSTALL.json')
    assert sha(Path(op['target']))==op['sha256']
    archive_hashes=read(Path(latest['record']))['archive_hashes']
    assert all(sha(GAME/p)==h for p,h in archive_hashes.items())
    I=E/'installation_v3'/now().strftime('%Y%m%d_%H%M%S');safe(I,E);I.mkdir(parents=True)
    B=I/'recovery';B.mkdir();old=B/'ED_TRUE.previous_v2.mkv';patched=B/'ED_TRUE.patched_v3.mkv'
    shutil.copy2(target,old);assert sha(old)==OLD
    shutil.copy2(new,patched);assert sha(patched)==expected
    incoming=I/'ED_TRUE.incoming';shutil.copy2(new,incoming);assert sha(incoming)==expected
    shutil.copy2(E/'LATEST_INSTALL.json',I/'PREVIOUS_INSTALL.json')
    shutil.copy2(E/'TITLE_DECISION_v3.json',I/'TITLE_DECISION.json')
    shutil.copy2(Q/'MEDIA_VALIDATION.json',I/'MEDIA_VALIDATION.json')
    before=inventory();rel=str(target.relative_to(GAME))
    rec={'status':'IN_PROGRESS','created_at':now().isoformat(),'target':str(target),'previous_sha256':OLD,
      'sha256':expected,'archive_hashes':archive_hashes,'backup':str(B),'process_check':stopped(),
      'previous_installation_record':latest['record'],'translator_model':'Codex internal',
      'changes':read(E/'TITLE_DECISION_v3.json')['changes'],'runtime_playback_verified':False}
    dump(I/'INSTALL_RECORD.json',rec);committed=False
    try:
        assert sha(target)==OLD
        os.replace(incoming,target);committed=True
        assert sha(target)==expected
        after=inventory();assert set(before)==set(after)
        assert [p for p in before if before[p]!=after[p]]==[rel]
        assert all(sha(Path(r['target']))==r['sha256'] for r in assets if r['asset']!='ED_TRUE')
        assert sha(Path(op['target']))==op['sha256']
        assert all(sha(GAME/p)==h for p,h in archive_hashes.items())
        rec.update(status='INSTALLED_VERIFIED_NOT_RUNTIME_PLAYED',finished_at=now().isoformat(),
          changed_files=[rel],unrelated_game_files_changed=0,other_endings_and_op_unchanged=True,archives_unchanged=True)
        dump(I/'INSTALL_RECORD.json',rec)
    except BaseException as exc:
        rec['error']=repr(exc)
        if committed and sha(target)==expected and sha(old)==OLD:
            recovery=I/'ED_TRUE.rollback';shutil.copy2(old,recovery);assert sha(recovery)==OLD
            os.replace(recovery,target);assert sha(target)==OLD;rec['status']='ROLLED_BACK_TO_V2'
        else:rec['status']='FAILED_RECOVERY_PRESERVED'
        dump(I/'INSTALL_RECORD.json',rec);raise
    previous.update(stage=str(new),sha256=expected,bytes=new.stat().st_size,preview_sha256=qa['sha256'],
      baseline='verified installed v2 ending',patched_backup=str(patched),previous_version_backup=str(old))
    dump(E/'LATEST_INSTALL.json',{'version':'v3','record':str(I/'INSTALL_RECORD.json'),'status':rec['status'],
        'assets':assets,'backup':str(B),'runtime_playback_verified':False})
    page=['<!doctype html><html lang="ko"><meta charset="utf-8"><title>Fatal Twelve 엔딩 v3</title><style>body{background:#141416;color:#eee;font:18px system-ui;margin:28px}main{max-width:1280px;margin:auto}video,img{width:100%}section{margin:38px 0}a{color:#9cd2ff}small{color:#ccc}</style><main><h1>엔딩 한국어화 — 설치본 v3</h1><p>제목과 반복 가사 표기를 「유리의 실」로 통일했습니다. 자막 크기·위치·타이밍과 원음은 이전과 같습니다.</p><p><small>유리의 실의 유튜브 자막 본문 대조와 후반 라라라 자막은 별도 후속 작업입니다. 실제 게임 재생 검증은 아직 하지 않았습니다.</small></p>']
    for n,label in [('ED_TRUE','진엔딩 — 유리의 실'),('ED_MHR_UNH','미하루·언해피 엔딩 — Unveil'),('ED_BAD','배드 엔딩')]:
        v='v3' if n=='ED_TRUE' else 'v2'
        page.append(f'<section><h2>{label}</h2><video controls preload="metadata" src="../candidate_{v}/{n}_KO_REVIEW.webm"></video></section>')
    page.append('<h2>이번에 바뀐 세 곳</h2>')
    for f in qa['frames']:page.append(f'<details><summary>{f["id"]} · {f["time"]:.2f}초</summary><img src="{Path(f["path"]).name}"></details>')
    page.append('</main></html>');(Q/'ENDING_REVIEW.html').write_text('\n'.join(page),'utf8')
    oldpage=E/'review_v2/ENDING_REVIEW.html';body=oldpage.read_text('utf8')
    body=body.replace('<main>','<main><p><a href="../review_v3/ENDING_REVIEW.html">최신 설치본 v3 — 유리의 실 — 보기</a></p>',1)
    body=body.replace('엔딩 한국어화 — 설치된 검수본 v2','엔딩 한국어화 — 이전 검수본 v2')
    body=body.replace('사용자 승인으로 게임에 설치한 v2 검수본.','이전 v2 검수본입니다. 현재 설치본은 위 링크의 v3입니다.')
    oldpage.write_text(body,'utf8')
    progress=read(E/'PROGRESS.json')
    progress.update(status='ENDING_V3_INSTALLED_VERIFIED_NOT_RUNTIME_PLAYED',version='v3',updated_at=now().isoformat(),
       installed_assets=assets,installation_record=str(I/'INSTALL_RECORD.json'),review_page=str(Q/'ENDING_REVIEW.html'),
       canonical_song_title='유리의 실',title_decision=str(E/'TITLE_DECISION_v3.json'),
       candidate_dirs={'ED_TRUE':str(C),'other_endings':str(E/'candidate_v2')})
    progress.pop('candidate_dir',None)
    progress['movies']=[qa if r['asset']=='ED_TRUE' else r for r in progress['movies']]
    progress['remaining']=[s.replace('installed v2 endings','installed v3 endings') for s in progress['remaining']]
    dump(E/'PROGRESS.json',progress)
    (I/'RESTORE.txt').write_text('복구 대상: '+str(target)+'\n현재 해시 '+expected+' 확인 후 '+str(old)+' (해시 '+OLD+')을 복원하면 v2로 돌아갑니다. 다른 엔딩과 OP는 변경하지 않습니다.','utf8')
    print(json.dumps({'status':rec['status'],'target':str(target),'sha256':expected,'review_page':str(Q/'ENDING_REVIEW.html'),'backup':str(B)},ensure_ascii=False),flush=True)

if __name__=='__main__':
    if '--prepare' in sys.argv:prepare()
    if '--install' in sys.argv:install()

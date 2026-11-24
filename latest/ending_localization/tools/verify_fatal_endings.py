"""Validate the actual persisted review movies, not their earlier prototypes."""
from pathlib import Path
import sys,subprocess,json,hashlib,html,re,shutil
sys.path.insert(0,'P:/AI/Codex/projects/fatal-twelve-ko/raster_localization_20260927/deps')
from PIL import Image,ImageDraw,ImageFont
E=Path('P:/AI/Codex/projects/fatal-twelve-ko/ending_localization_20261003')
S=E/'subtitles_v2';C=E/'candidate_v2';Q=E/'review_v2';Q.mkdir(exist_ok=True)
FF=Path('F:/DOWN/ffmpeg-7.1.1-essentials_build/ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe');FP=FF.with_name('ffprobe.exe')
sys.stdout.reconfigure(encoding='utf8')
def run(args):return subprocess.check_output([str(x) for x in args],creationflags=subprocess.CREATE_NO_WINDOW)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
def packets(p,sel):return json.loads(run([FP,'-v','error','-select_streams',sel,'-show_packets','-show_data_hash','sha256','-show_entries','packet=pts_time,duration_time,data_hash,size','-of','json',p]))['packets']
def getframe(p,t,out):run([FF,'-y','-v','error','-ss',t,'-i',p,'-frames:v','1',out])
metadata_only='--metadata-only' in sys.argv
results=[];screens=[];inv=json.loads((E/'SOURCE_INVENTORY.json').read_text('utf8'))
if metadata_only:
 previous=json.loads((Q/'MEDIA_VALIDATION.json').read_text('utf8'))
 results=previous['movies'];screens=previous['contact_sheets']
 for r in results:
  assert sha(Path(r['candidate']))==r['sha256'],('cached video changed',r['asset'])
  assert sha(S/f'{r["asset"]}.ass')==r['ass_sha256'],('ASS changed: render and verify required',r['asset'])
labels={'ED_BAD':'배드 엔딩','ED_MHR_UNH':'미하루·언해피 엔딩 — Unveil','ED_TRUE':'진엔딩 — 유리실'}
for m in ([] if metadata_only else inv['movies']):
 n=Path(m['logical_asset']).stem;src=E/'source'/m['logical_asset'];out=C/f'{n}_KO_REVIEW.webm'
 assert out.exists();assert sha(src)==m['sha256']
 source_audio=packets(src,'a');output_audio=packets(out,'a')
 assert source_audio==output_audio,(n,'audio packets changed')
 v0=packets(src,'v');v1=packets(out,'v')
 assert [x['pts_time'] for x in v0]==[x['pts_time'] for x in v1],(n,'video timeline changed')
 run([FF,'-v','error','-i',out,'-f','null','-'])
 text=(S/f'{n}.ass').read_text('utf8')
 lr=json.loads((S/f'{n}_LYRICS.json').read_text('utf8'));cr=json.loads((S/f'{n}_CREDITS.json').read_text('utf8'))
 # Inspect all full subtitle pairs at their midpoint plus representative credit intervals.
 times=sorted(set([6.,20.,40.,float(m['media']['format']['duration'])-4]+[round((r['start']+r['end'])/2,2) for r in lr]))
 cells=[]
 for i,t in enumerate(times):
  png=Q/f'{n}_{i:02d}.png';getframe(out,t,png)
  im=Image.open(png);assert im.size==(1280,720)
  mini=im.resize((512,288));cell=Image.new('RGB',(512,314),(20,20,20));cell.paste(mini,(0,26));ImageDraw.Draw(cell).text((8,5),f'{n}  {t:.2f}s',fill='white');cells.append(cell)
 for page in range(0,len(cells),12):
  subset=cells[page:page+12];sheet=Image.new('RGB',(1536,314*((len(subset)+2)//3)),(20,20,20))
  for j,im in enumerate(subset):sheet.paste(im,((j%3)*512,(j//3)*314))
  p=Q/f'{n}_CONTACT_{page//12+1:02d}.jpg';sheet.save(p,quality=92);screens.append(p.name)
 results.append({'asset':n,'candidate':str(out),'sha256':sha(out),'bytes':out.stat().st_size,'source_sha256':m['sha256'],'frame_count':len(v1),'video_pts_exact':True,'audio_packets_exact':True,'audio_packet_count':len(output_audio),'full_decode_errors':0,'size':[1280,720],'sample_frames':len(times),'lyric_cues':len(lr),'credit_cells':len(cr['rows']),'ass_sha256':sha(S/f'{n}.ass')})
 print(n,'validated',len(v1),'frames; unchanged',len(output_audio),'audio packets',flush=True)
if not metadata_only:
 dump(Q/'MEDIA_VALIDATION.json',{'status':'STATIC_MEDIA_GATES_PASS_NOT_RUNTIME_PLAYED','movies':results,'contact_sheets':screens,'does_not_prove':['Vocal-aligned lyric timing by human listening','Actual retrieval of Glass Thread YouTube captions','Runtime playback'],'source_movie_archive_unchanged':sha(Path(inv['archive']))==inv['archive_sha256']})
manifest=json.loads((E/'DRAFT_MANIFEST_v2.json').read_text('utf8'))
pending=manifest['uncertain_source_lyrics']
page=['<!doctype html><html lang="ko"><meta charset="utf-8"><title>Fatal Twelve 엔딩 한국어화 검수</title><style>body{margin:24px;background:#121214;color:#eee;font:17px system-ui}main{max-width:1440px;margin:auto}video{width:100%;background:black}section{margin:34px 0;padding:20px;border:1px solid #444;border-radius:8px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:12px}button,a{color:#a9d7ff}button{background:#222;padding:9px;border:1px solid #777;border-radius:5px;cursor:pointer}td{padding:10px;border-bottom:1px solid #444}small{color:#bbb}.hold{color:#ffd598}details{margin:14px 0}img{max-width:100%}</style><main><h1>엔딩 한국어화 — 검수 후보 v2</h1><p>원음·프레임 시점 유지 / 검은 배경의 흰색 명조체 크레딧 / 원문 위·한국어 아래 48px 자막</p><p class="hold">미설치 검수본. 가사 원문은 사용자 지정 유튜브 자막을 기준으로 확정합니다. Unveil의 기존 판독 보류 2곳은 해제했습니다. 유리실은 유튜브 자막 본문을 아직 가져오지 못해 기존 초안이며, 후반 라라라 구간도 작업 중입니다.</p>']
for r in results:
 n=r['asset'];page.append(f'<section id="{n}"><h2>{labels[n]}</h2><div class="pair"><div><p>원본 (무음 비교)</p><video muted controls preload="metadata" src="../source/movies/{n}.mkv" id="src_{n}"></video><small>브라우저가 원본 Theora/MKV를 지원하지 않으면 원본은 로컬 플레이어로 확인합니다.</small></div><div><p>한국어 후보</p><video controls preload="metadata" src="../candidate_v2/{n}_KO_REVIEW.webm" id="ko_{n}"></video></div></div><p><button onclick="document.getElementById(\'src_{n}\').currentTime=document.getElementById(\'ko_{n}\').currentTime">원본을 후보 시간에 맞추기</button>　{r["frame_count"]:,}프레임 · 원음 패킷 일치 · 가사 {r["lyric_cues"]}구간</p>')
 lr=json.loads((S/f'{n}_LYRICS.json').read_text('utf8'))
 if lr:
  page.append('<details><summary>가사·원문 확인 대상</summary><table>')
  for l in lr:
   note=pending.get(l['id'],'');css=' class="hold"' if note else ''
   page.append(f'<tr{css}><td><button onclick="document.getElementById(\'ko_{n}\').currentTime={max(0,l["start"]-1)}">{l["id"]} {l["start"]:.2f}s</button></td><td>{html.escape(l["source"])}<br>{html.escape(l["target_ko"])}<br><small>{html.escape(note)}</small></td></tr>')
  page.append('</table></details>')
 for p in screens:
  if p.startswith(n):page.append(f'<details><summary>{p}</summary><img src="{p}"></details>')
 page.append('</section>')
page.append('<h2>검증 범위</h2><p>세 원본 엔딩을 추출해 보존했습니다. 원음 패킷·오디오 시각, 영상 프레임 수·시각, 전 구간 디코딩을 실제 후보 파일에서 검사했습니다. 실제 게임 재생은 하지 않았습니다. 가사의 원문 보류와 기계 보조 타이밍은 별도입니다.</p><p>가사 원문의 기준은 지정 유튜브 채널입니다. 음성 인식과의 차이만으로 보류하거나 가사집을 다시 요구하지 않습니다. 한국어 해석은 Codex internal이 작성합니다. 유리실의 현재 초안을 유튜브 확인본으로 표시하지 않으며, 자막 수집 실패는 원문 신뢰 여부와 별개로 기록합니다.</p></main></html>')
(Q/'ENDING_REVIEW.html').write_text('\n'.join(page),'utf8')
dump(E/'PROGRESS.json',{'status':'YOUTUBE_SOURCE_POLICY_APPLIED_GLASS_CAPTION_RETRIEVAL_PENDING','translator_model':'Codex internal','review_page':str(Q/'ENDING_REVIEW.html'),'candidate_dir':str(C),'movies':results,'completed':['Three original ending movie hashes and consumer paths inventoried','Full credit roster read and Korean-authored','82 bilingual lyric cues drafted','Independent read-only credit and lyric review; fixes applied','Original audio packets and timestamps preserved','Original video frame count and timestamps preserved','Full candidate decode checked','Primary visually inspected all 10 contact sheets (94 sampled frames including all 82 lyric midpoints)','User-selected YouTube lyric authority recorded; Unveil U33/U37 released from STT holds'],'remaining':['Retrieve actual Glass Thread YouTube caption body; user source authority already decided','Verify/synchronize the final Glass Thread la-la section (currently not captioned)','User runtime approval and separately approved installation'],'source_policy':manifest['source_policy'],'pending_source_ids':list(pending),'glass_captions_not_yet_checked':['G%02d'%i for i in range(1,37)],'runtime_modified_by_ending_task':False,'original_op_v62_installed':True,'youtube_ending_reference':'https://www.youtube.com/watch?v=pYyVyNISNHs','audio_hearing_claim':False})
# Keep the review page and progress honest after a user-authorized installation.
# A later render with different bytes must not inherit an old installed claim.
latest=E/'LATEST_INSTALL.json'
if latest.exists():
 install=json.loads(latest.read_text('utf8'))
 by_asset={r['asset']:r for r in results}
 assets=install.get('assets',[])
 installed=(install.get('status')=='INSTALLED_VERIFIED_NOT_RUNTIME_PLAYED' and len(assets)==3
   and all(a['preview_sha256']==by_asset[a['asset']]['sha256'] and Path(a['target']).is_file()
       and sha(Path(a['target']))==a['sha256'] for a in assets))
 if installed:
  hp=Q/'ENDING_REVIEW.html';body=hp.read_text('utf8')
  body=body.replace('엔딩 한국어화 — 검수 후보 v2','엔딩 한국어화 — 설치된 검수본 v2')
  body=body.replace('미설치 검수본.','사용자 승인으로 게임에 설치한 v2 검수본. 실제 게임 재생 확인은 아직 하지 않았습니다.')
  hp.write_text(body,'utf8')
  pp=E/'PROGRESS.json';state=json.loads(pp.read_text('utf8'))
  state.update(status='ENDING_V2_INSTALLED_VERIFIED_NOT_RUNTIME_PLAYED',runtime_modified_by_ending_task=True,
    installation_record=install['record'],installed_assets=assets,
    remaining=state['remaining'][:2]+['Optional in-game playback confirmation of the installed v2 endings'])
  dump(pp,state)
print(Q/'ENDING_REVIEW.html',flush=True)

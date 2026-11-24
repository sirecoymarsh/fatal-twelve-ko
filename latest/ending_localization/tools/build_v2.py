"""Build separate, review-only ending candidates. Never touches runtime or archives."""
import sys,json,re,hashlib,subprocess,shutil,math
from pathlib import Path
from content_v2 import *
E=Path('P:/AI/Codex/projects/fatal-twelve-ko/ending_localization_20261003')
V2='--v2' in sys.argv
S=E/('subtitles_v2' if V2 else 'subtitles')
C=E/('candidate_v2' if V2 else 'candidate')
S.mkdir(exist_ok=True);C.mkdir(exist_ok=True)
O=E.parent/'opening_localization_20261002'
FF=Path('F:/DOWN/ffmpeg-7.1.1-essentials_build/ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe')
FP=FF.with_name('ffprobe.exe')
sys.path.insert(0,str(E.parent/'raster_localization_20260927/deps'))
from PIL import Image,ImageDraw,ImageFont
sys.stdout.reconfigure(encoding='utf8')
FONT='C:/Windows/Fonts/NotoSerifKR-VF.ttf'
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def stamp(t):return f'{int(t)//3600}:{int(t)//60%60:02d}:{t%60:05.2f}'
def assfilter(p):return "ass='%s'"%str(p).replace('\\','/').replace(':','\\:')
def run(args):return subprocess.check_output([str(x) for x in args],creationflags=subprocess.CREATE_NO_WINDOW)
BASE='''[Script Info]
Title: Fatal Twelve ending localization — REVIEW CANDIDATE
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Credit,Noto Serif KR,29,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,8,20,20,0,1
Style: CreditEN,Noto Serif KR,18,&H00D0D0D0,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,8,20,20,0,1
Style: Original,Noto Serif KR,48,&H00FFFFFF,&H000000FF,&H00101010,&H80101010,-1,0,0,0,100,100,0,0,1,2.6,1.0,2,40,40,73,1
Style: Korean,Noto Serif KR,48,&H00E8E8E8,&H000000FF,&H00101010,&H80101010,0,0,0,0,100,100,0,0,1,2.6,1.0,2,40,40,12,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
def event(start,end,style,text,layer=0):return f'Dialogue: {layer},{stamp(start)},{stamp(end)},{style},,0,0,0,,{text}'

def credits(name,duration):
 rows=[];y=0
 def row(cells,kind='body'):
  nonlocal y
  xpositions=[640] if len(cells)==1 else [462,842]
  maxw=1050 if len(cells)==1 else 530
  for x,c in zip(xpositions,cells):
   jp,ko,en=c
   rows.append(dict(y=y,x=x,jp=jp,ko=ko,en=en,kind=kind,max_width=maxw))
  y+=68 if kind=='body' else 62
 def gap(n=96):
  nonlocal y;y+=n
 def section(jp,ko,en,people):
  gap();row([(jp,ko,en)],'heading');gap(10)
  for keys in people:row([PEOPLE[k] for k in keys])
 row([('出演','출연','Cast')],'heading');gap(8)
 cast=CAST+(TRUE_EXTRA if name=='ED_TRUE' else [])+[NEIGHBOR]
 for r in cast:
  # Original two columns are role right-aligned and actor left-aligned.
  row([r[:3],r[3:]])
  rows[-2]['x']=616;rows[-2]['align']=9;rows[-2]['max_width']=560
  rows[-1]['x']=652;rows[-1]['align']=7;rows[-1]['max_width']=555
 for s in SECTIONS:
  if s[0] in ('OPENING','ENDING'):
   ending=s[0]=='ENDING'
   if ending and name!='ED_TRUE':continue
   gap();row([('エンディングテーマ' if ending else 'オープニングテーマ','엔딩 테마' if ending else '오프닝 테마','Ending Theme' if ending else 'Opening Theme')],'heading')
   gap(12);row([('「硝子の糸」','「유리실」','“Garasu no Ito”')] if ending else [('「Unveil」','「Unveil」','“Unveil”')]);gap(16)
   for jp,ko,en,p in [('歌','노래','Vocals','kuyuri'),('ギターソロ','기타 솔로','Guitar Solo','ges'),('作詞','작사','Lyrics','akeo' if ending else 'toshi'),('作曲／編曲','작곡·편곡','Composition/Arrangement','low')]:
    row([(jp,ko,en),PEOPLE[p]])
    rows[-2]['x']=616;rows[-2]['align']=9
    rows[-1]['x']=652;rows[-1]['align']=7
  else:section(*s)
 # Preserve the source's closing production credit as a held card, rather than scrolling it out.
 height=y+35;viewport=720 if name=='ED_BAD' else 568
 start=1.0;finish=duration-9;speed=(height+viewport)/(finish-start)
 ev=[]
 for r in rows:
  t0=start+r['y']/speed
  # Each entry enters the original top-to-bottom viewport and exits continuously.
  enter=start+r['y']/speed;exit=start+(r['y']+viewport+80)/speed
  exit=min(exit,duration-7)
  if exit<=enter:raise ValueError(r)
  an=r.get('align',8)
  size=24 if r['kind']=='heading' else 29
  f=ImageFont.truetype(FONT,size)
  length=f.getlength(r['ko']);scale=min(100,100*r['max_width']/max(1,length))
  if scale<72:raise ValueError(('Credit too wide',r,scale))
  r.update(font_size=size,horizontal_scale=round(scale,2),enter=enter,exit=exit)
  end_y=viewport-speed*(exit-enter)
  move=f'{{\\an{an}\\clip(0,0,1280,{viewport})\\move({r["x"]},{viewport},{r["x"]},{end_y:.3f})\\fs{size}\\fscx{scale:.2f}}}'
  ev.append(event(enter,exit,'Credit',move+r['ko']))
  enf=ImageFont.truetype(FONT,18);enscale=min(100,100*r['max_width']/max(1,enf.getlength(r['en'])))
  enmove=f'{{\\an{an}\\clip(0,0,1280,{viewport})\\move({r["x"]},{viewport+35},{r["x"]},{end_y+35:.3f})\\fscx{enscale:.2f}}}'
  ev.append(event(enter,exit,'CreditEN',enmove+r['en']))
 for y1,size,c in [(270,24,('制作','제작','Produced by')),(332,31,PEOPLE['company'])]:
  rows.append(dict(jp=c[0],ko=c[1],en=c[2],closing_card=True))
  ev.append(event(duration-7,duration-.5,'Credit',f'{{\\pos(640,{y1})\\fs{size}\\fad(350,900)}}'+c[1]))
  ev.append(event(duration-7,duration-.5,'CreditEN',f'{{\\pos(640,{y1+37})\\fad(350,900)}}'+c[2]))
 return rows,ev

def opening_first_verse():
 p=O/'typeset/all_groups_v62/OP_large.ass'
 es=[s.split(',',9) for s in p.read_text('utf8').splitlines() if s.startswith('Dialogue:')]
 rows=[]
 def sec(x):h,m,s=x.split(':');return int(h)*3600+int(m)*60+float(s)
 # Recorded opening and full Unveil have a roughly 3.8-second arrangement offset.
 # This is deliberately marked provisional until waveform-aligned below.
 offset=json.loads((E/'analysis/UNVEIL_OFFSET.json').read_text('utf8'))['offset_seconds'] if (E/'analysis/UNVEIL_OFFSET.json').exists() else 3.8
 for i in range(0,34,2):
  a,b=es[i:i+2];rows.append((sec(a[1])+offset,sec(a[2])+offset,re.sub(r'\{[^}]*\}','',a[9]),re.sub(r'\{[^}]*\}','',b[9])))
 return rows

def prepare():
 inv=json.loads((E/'SOURCE_INVENTORY.json').read_text('utf8'))
 artifacts=[]
 for m in inv['movies']:
  name=Path(m['logical_asset']).stem;dur=float(m['media']['format']['duration'])
  cr,ev=credits(name,dur)
  lyric=GLASS if name=='ED_TRUE' else opening_first_verse()+UNVEIL_LATE if name=='ED_MHR_UNH' else []
  lr=[]
  for i,(start,end,src,ko) in enumerate(lyric,1):
   assert 0<=start<end<=dur
   ident=('G' if name=='ED_TRUE' else 'U')+f'{i:02d}'
   # No automatic shrink or extra wrapping: preserve the user's 48px choice.
   for tx in (src,ko):
    width=ImageFont.truetype(FONT,48).getlength(tx)
    if width>1192:raise ValueError(('Lyric needs semantic split',ident,tx,width))
   ev += [event(start,end,'Original',src,1),event(start,end,'Korean',ko,1)]
   pending=GLASS_PENDING if name=='ED_TRUE' else UNVEIL_PENDING
   source_status='youtube_source_selected_by_user' if name=='ED_MHR_UNH' else 'local_source_draft_youtube_caption_retrieval_pending'
   note=None if name=='ED_MHR_UNH' else ('YouTube source authority accepted; actual caption body retrieval is pending. '+pending.get(ident,''))
   lr.append(dict(id=ident,start=start,end=end,source=src,target_ko=ko,translator_model='Codex internal',source_status=source_status,timing_status='machine-assisted draft; not listened to',note=note))
  for a,b in zip(lr,lr[1:]):assert a['end']<=b['start'],(a,b)
  ass=S/f'{name}.ass';ass.write_text(BASE+'\n'.join(ev)+'\n','utf8')
  dump(S/f'{name}_LYRICS.json',lr)
  dump(S/f'{name}_CREDITS.json',{'translator_model':'Codex internal','source_movie_sha256':m['sha256'],'rows':cr,'design':'Source-derived white serif bilingual credit roll on black; lyrics get separate lower lane. Original person/role attribution preserved; no Korean localization staff claims added.','layout_reflow':True,'original_background_art':'none; black field','original_english_credit_typos':'preserved, including Recording Director under sound editing','name_authority':'name_unification_20261003/guides/GLOSSARY.json; current UI has stale Oguma/Sofiya spellings not inherited'})
  artifacts.append({'asset':name,'credit_cells':len(cr),'lyric_cues':len(lr),'source_sha256':m['sha256'],'ass_sha256':sha(ass)})
 source_access_pending={k:'YouTube source authority accepted; caption retrieval pending. Previous draft note: '+v for k,v in GLASS_PENDING.items()}
 dump(E/('DRAFT_MANIFEST_v2.json' if V2 else 'DRAFT_MANIFEST.json'),{'status':'REVIEW_DRAFT_NOT_INSTALLED','translator_model':'Codex internal','artifacts':artifacts,'source_policy':SOURCE_POLICY,'uncertain_source_lyrics':source_access_pending,'unverified':['Real-time vocal synchronization','User approval of original-design reflow','Glass Thread YouTube caption text has not been retrieved','Glass Thread ending la-la vocal tail timing (not yet subtitled)']})
 build_snapshot=Path(__file__).read_text('utf8')
 if V2:build_snapshot=build_snapshot.replace('from content_v2 import *','from content_v2 import *')
 (E/'tools'/('build_v2.py' if V2 else Path(__file__).name)).write_text(build_snapshot,'utf8')
 shutil.copy2(Path(__file__).with_name('fatal_ending_content.py'),E/'tools'/('content_v2.py' if V2 else 'fatal_ending_content.py'))
 print(json.dumps(artifacts,ensure_ascii=False))

def render():
 inv=json.loads((E/'SOURCE_INVENTORY.json').read_text('utf8'))
 for m in inv['movies']:
  name=Path(m['logical_asset']).stem
  out=C/f'{name}_KO_REVIEW.webm';src=E/'source'/m['logical_asset']
  if out.exists():continue
  ass=S/f'{name}.ass'
  # Keep the original source frame timeline. All original visible content is the audited credit layer.
  cmd=[FF,'-y','-v','error','-i',src,'-vf','drawbox=x=0:y=0:w=iw:h=ih:color=black:t=fill,'+assfilter(ass),'-map','0:v:0','-map','0:a:0','-c:v','libvpx','-b:v','12M','-crf','6','-qmin','0','-qmax','8','-threads','6','-deadline','good','-cpu-used','3','-auto-alt-ref','0','-lag-in-frames','0','-c:a','copy','-fps_mode','passthrough',out]
  print('Rendering',name,flush=True)
  run(cmd)
  print('Rendered',out.stat().st_size,flush=True)
if __name__=='__main__':
 if '--prepare' in sys.argv:prepare()
 if '--render' in sys.argv:render()

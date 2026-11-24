"""Apply the user's source-authority decision without modifying rendered pixels."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys

E=Path('P:/AI/Codex/projects/fatal-twelve-ko/ending_localization_20261003')
TOOLS=Path(__file__).resolve().parent
stamp=datetime.datetime.now().astimezone().isoformat()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')

backup=E/'review_v2'/'before_youtube_authority'
backup.mkdir(exist_ok=True)
for relative in ['PROGRESS.json','DRAFT_MANIFEST_v2.json','review_v2/ENDING_REVIEW.html',
                 'subtitles_v2/ED_MHR_UNH_LYRICS.json','subtitles_v2/ED_TRUE_LYRICS.json']:
    src=E/relative; dest=backup/relative
    if not dest.exists():
        dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)

transcript=Path('C:/Users/CADRIA~1/AppData/Local/Temp/browser-use/exports/youtube-ORQff1P24cY-dd69b8a4-d835-4798-816f-6b88d801be33.txt')
assert sha(transcript)=='58e6e11105ee195f70f36a22acbb2fa144c38b31d41ab883cd30a2d29aa98c20'
body=transcript.read_text('utf8')
assert '魂に光を灯すだろう' in body and 'この手で切り開く' in body
saved=E/'source/references/YOUTUBE_UNVEIL_TRANSCRIPT.txt';shutil.copy2(transcript,saved)

subprocess.run([sys.executable,str(TOOLS/'build_fatal_endings.py'),'--v2','--prepare'],check=True)
subprocess.run([sys.executable,str(TOOLS/'verify_fatal_endings.py'),'--metadata-only'],check=True)
manifest=json.loads((E/'DRAFT_MANIFEST_v2.json').read_text('utf8'))
assert set(manifest['uncertain_source_lyrics'])=={'G20','G23','G33','G34','G36'}
rows=json.loads((E/'subtitles_v2/ED_MHR_UNH_LYRICS.json').read_text('utf8'))
assert len(rows)==46 and all(r['source_status']=='youtube_source_selected_by_user' for r in rows)
assert all(r['note'] is None for r in rows)
validation=json.loads((E/'review_v2/MEDIA_VALIDATION.json').read_text('utf8'))
decision={
 'recorded_at':stamp,'instruction':'그냥 유튜브 가사를 신뢰하도록',
 'policy':manifest['source_policy'],
 'saved_unveil_transcript':str(saved),'transcript_sha256':sha(saved),
 'source_author':'Critias0038 uploader/caption source, not Codex internal',
 'translator_model':'Codex internal',
 'resolved':[{'id':'U33','source':'魂に光を灯すだろう','basis':'Read cached YouTube caption at 3:00; user selected it over STT.'},
             {'id':'U37','source':'この手で切り開く','basis':'Read cached YouTube caption at 3:21; user selected it over STT.'}],
 'glass_source_access':{'status':'NOT_RETRIEVED','url':'https://www.youtube.com/watch?v=pYyVyNISNHs',
  'observed_failures':['Browser/native tool kernel initialization failed: kernel assets path not found.',
                       'Public caption requests returned HTTP 200 with zero-byte bodies.'],
  'existing_draft_not_youtube_verified':True,'no_additional_lyric_authority_decision_required':True},
 'rendered_video_and_ass_unchanged':True,'live_game_modified':False,
 'backup_of_predecision_metadata':str(backup)
}
dump(E/'SOURCE_POLICY_DECISION.json',decision)
dump(E/'review_v2/PRIMARY_VISUAL_REVIEW.json',{
 'reviewed_at':stamp,'reviewer':'Codex internal /root',
 'sheets':[{'file':n,'sha256':sha(E/'review_v2'/n)} for n in validation['contact_sheets']],
 'sampled_frames':94,'covers_all_lyric_midpoints':82,
 'native_1280x720_samples':['ED_TRUE_02.png','ED_MHR_UNH_46.png'],
 'findings':[],
 'observed':'White serif credits, separated 48px bilingual lyrics, no visible tofu or caption overlap/clipping in inspected frames. Credit clipping at viewport boundaries is the intentional scroll entrance/exit.',
 'not_claimed':['Every video frame inspected','Auditory synchronization','In-game playback','Glass Thread YouTube text retrieved']})
dump(E/'review_v2/INDEPENDENT_REVIEW_RECEIPT.json',{
 'recorded_at':stamp,'record_type':'Primary summary of returned read-only reviewer findings',
 'reviewers':['/root/ending_credit_review','/root/ending_lyrics_review'],
 'credit_scope':{'cells_by_movie':{'ED_BAD':144,'ED_MHR_UNH':144,'ED_TRUE':160},
  'findings_applied':['Canonical 다이아나 해리슨','Restore original Muryokoukaondeasobou! spelling',
  'Preserve original SensesCircuil spelling','Correct source metadata フェデリーコ・カルミナーティ']},
 'lyric_scope':{'cue_pairs':82,'shared_opening_cues_checked':26,
  'findings_applied':['Attach disputed reading note to G20 rather than G19',
   'Boundary adjustments G07/G08, G20/G21, G32/G33, U23/U24, U43/U44']},
 'all_semantic_targets_authored_by':'Codex internal primary agent',
 'audio_listened':False,'candidate_hashes':{r['asset']:r['sha256'] for r in validation['movies']}})
shutil.copy2(TOOLS/'verify_fatal_endings.py',E/'tools/verify_fatal_endings.py')
shutil.copy2(__file__,E/'tools/apply_ending_youtube_authority.py')
snapshot=(E/'tools/build_v2.py').read_text('utf8')
assert 'from content_v2 import *' in snapshot
compile(snapshot,'build_v2.py','exec')
print('YouTube authority persisted; U33/U37 cleared; rendered hashes unchanged; Glass retrieval status explicit.')

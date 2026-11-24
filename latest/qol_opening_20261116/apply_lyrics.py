"""Apply the player's chosen rendering to every matching cue in the two active masters."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
OUT=HERE/'delivery'
ED=BASE/'ending_localization_20261003'
OP=BASE/'opening_localization_20261002'
FF=Path('F:/DOWN/ffmpeg-7.1.1-essentials_build/ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe')
NEW='남이 정한 시간 속에선 살고 싶지 않아'
OLD='한정된 시간 속에서 살고 싶진 않아'
def sha(file):return hashlib.file_digest(open(file,'rb'),'sha256').hexdigest()
def ass_filter(path):return "ass='"+path.as_posix().replace(':',r'\:')+"'"
def run():
    OUT.mkdir(exist_ok=True)
    records=[]
    for key,src,nmatch in [('OP',OP/'delivery_v62/reference/OP_large.ass',1),('ED_MHR_UNH',ED/'subtitles_v2/ED_MHR_UNH.ass',3)]:
        raw=src.read_bytes();rows=raw.decode('utf-8-sig').splitlines()
        cues=[]
        for i,line in enumerate(rows):
            if 'in a limited time' in line.lower():
                pair=rows[i+1].split(',',9);orig=line.split(',',9)
                assert pair[1:3]==orig[1:3] and pair[3]=='Korean' and pair[-1]==OLD,(key,pair)
                cues.append(pair[1:3])
        assert len(cues)==nmatch and raw.count(OLD.encode())==nmatch
        dest=OUT/(key+'.ass');dest.write_bytes(raw.replace(OLD.encode(),NEW.encode()))
        records.append(dict(movie=key,source_subtitle=str(src),source_sha256=sha(src),result_sha256=sha(dest),times=cues))
    (OUT/'lyrics.json').write_text(json.dumps(dict(korean=NEW,wording_source='user-supplied verbatim',translator_model='Codex internal',cues=records),ensure_ascii=False,indent=2),'utf8')
    print([(r['movie'],r['times']) for r in records],flush=True)
    if 'ending' in sys.argv:
        path=ED/'source/movies/ED_MHR_UNH.mkv'
        assert sha(path)=='a13658c4fdcfa5403090d9776b043cba406be4139f318d52b0b26fb3bd20474a'
        # Existing verified ending has a black credit plate with the original timed credit design.
        out=OUT/'ED_MHR_UNH.mkv'
        cmd=[str(FF),'-y','-hide_banner','-nostdin','-v','error','-i',str(path),'-vf','drawbox=x=0:y=0:w=iw:h=ih:color=black:t=fill,'+ass_filter(OUT/'ED_MHR_UNH.ass'),'-map','0:v:0','-map','0:a:0','-c:v','libvpx','-b:v','12M','-crf','6','-qmin','0','-qmax','8','-threads','6','-deadline','good','-cpu-used','3','-auto-alt-ref','0','-lag-in-frames','0','-c:a','copy','-fps_mode','passthrough',str(out)]
        subprocess.run(cmd,check=True,creationflags=subprocess.CREATE_NO_WINDOW)
        print('ending encoded',sha(out),flush=True)
if __name__=='__main__':run()
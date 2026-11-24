"""Check every packet timestamp, unchanged audio, decoded subtitle renders and framing."""
from pathlib import Path
import hashlib,subprocess,json
import cv2,numpy as np
from apply_lyrics import OUT,HERE,BASE,OP,ED,FF,NEW,OLD,ass_filter,sha
PROBE=FF.with_name('ffprobe.exe')
ORIGINAL={'OP':OP/'source/movies/OP.mkv','ED_MHR_UNH':ED/'source/movies/ED_MHR_UNH.mkv'}
runtime=BASE/'runtime_review/game/tl/korean/movies'
def capture(cmd,data=None):
    return subprocess.run([str(s) for s in cmd],input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True,creationflags=subprocess.CREATE_NO_WINDOW).stdout
def structure(p):
    return json.loads(capture([PROBE,'-v','error','-show_entries','format=duration:stream=codec_name,width,height,time_base,r_frame_rate,sample_rate,channels,start_time','-of','json',p]))
def packets(p,stream):
    return capture([PROBE,'-v','error','-select_streams',stream,'-show_packets','-show_entries','packet=pts,dts,duration','-of','csv=p=0',p]).splitlines()
def audio(p):
    return capture([FF,'-v','error','-i',p,'-map','0:a','-c','copy','-f','hash','-hash','sha256','-']).decode().strip()
def frame(cap,n):
    cap.set(cv2.CAP_PROP_POS_FRAMES,n)
    ok,im=cap.read();assert ok,n
    return im
def shown(bg,n,ass):
    raw=capture([FF,'-v','error','-f','rawvideo','-pix_fmt','bgr24','-s','1280x720','-r','30000/1001','-i','pipe:0','-vf','setpts=PTS+'+str(n)+','+ass_filter(ass),'-frames:v','1','-f','rawvideo','-pix_fmt','bgr24','-'],bg.tobytes())
    return np.frombuffer(raw,'uint8').reshape(720,1280,3)
def main():
    reports=[]; proof=HERE/'game_qa'
    for name,times in [('OP',[48.5]),('ED_MHR_UNH',[52.2,124.5,189.1])]:
        new=OUT/(name+'.mkv');old=runtime/(name+'.mkv');original=ORIGINAL[name]
        old_ass=OP/'delivery_v62/reference/OP_large.ass' if name=='OP' else ED/'subtitles_v2/ED_MHR_UNH.ass'
        versions=[structure(p) for p in [old,new]];assert versions[0]==versions[1],versions
        pulses={}; audio1=audio(old);audio2=audio(new);assert audio1==audio2
        for stream in ('v:0','a:0'):
            a=packets(old,stream);b=packets(new,stream);assert a==b,(name,stream,[(x,y) for x,y in zip(a,b) if x!=y][:2],len(a),len(b))
            pulses[stream]=len(a)
        capture([FF,'-xerror','-v','error','-i',new,'-map','0:v:0','-map','0:a:0','-f','null','-'])
        caps=[cv2.VideoCapture(str(p)) for p in (new,original)]
        readings=[]
        for j,t in enumerate(times):
            n=round(t*30000/1001);actual=frame(caps[0],n)
            bg=frame(caps[1],n) if name=='OP' else np.zeros((720,1280,3),'uint8')
            expected=shown(bg,n,OUT/(name+'.ass')); previous=shown(bg,n,old_ass)
            diff=np.max(np.abs(expected.astype('int16')-previous),axis=2)>30
            ys,xs=np.where(diff);assert len(xs)>500
            a=np.abs(actual.astype('int16')-expected).mean(2)[diff].mean()
            b=np.abs(actual.astype('int16')-previous).mean(2)[diff].mean()
            assert a<b*.30,(name,n,a,b)
            bounds=(int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max()))
            assert 8<bounds[0]<bounds[2]<1272 and 350<bounds[1]<bounds[3]<718,bounds
            cv2.imwrite(str(proof/('lyrics_%s_%d.jpg'%(name,j+1))),actual,[cv2.IMWRITE_JPEG_QUALITY,93])
            readings.append({'time':t,'frame':n,'text':NEW,'translated_change_bounds':bounds,'pixel_error_to_user_text':round(a,3),'pixel_error_to_previous_text':round(b,3)})
        for cap in caps:cap.release()
        reports.append({'movie':name,'sha256':sha(new),'bytes':new.stat().st_size,'streams':versions[1],'packet_timings_equal':pulses,'matching_audio':audio2,'full_decode_errors':0,'cue_frames':readings})
    (HERE/'movie_validation.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),'utf8');print([(r['movie'],r['packet_timings_equal'],r['cue_frames']) for r in reports],flush=True)
if __name__=='__main__':main()

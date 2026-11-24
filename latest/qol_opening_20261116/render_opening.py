"""Rebuild from the original frames and the complete v68 edit history, before burning lyrics."""
from pathlib import Path
import collections,json,sys,subprocess,time
import cv2,numpy as np
from compare_plates import *
from apply_lyrics import OUT,FF,ass_filter
SRC=OP/'source/movies/OP.mkv'
GROUPS=['T%02d'%i for i in range(1,18)]
PLATES={'T01','T02','T05','T06','T07','T08','T12','T15'}
FIXED={'T01','T02','T03','T04','T13','T14','T15','T16','T17'}
V65={r['frame']:r for r in json.loads((TEMP/'geometry_repair_v65/assembly/PATCH_INDEX.json').read_text('utf8'))['records']}
CV=lambda im:cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype('float32')
META={g:json.loads((JOBS/g/'job.json').read_text()) for g in GROUPS}
MET={g:json.loads((JOBS/g/'metrics.json').read_text()) for g in GROUPS}
def curves():
    fitted={}
    for g in FIXED:
        if MET[g]['opacity']:
            fitted.update({(int(k),g):r['fitted'] for k,r in MET[g]['opacity'].items()})
            continue
        meta=META[g];x,y,X,Y=meta['box'];job=JOBS/g
        def pair(n):
            return CV(rgb(job/'frames'/('%04d.png'%n))),CV(rgb(job/'result/frames/frames'/('%04d.png'%(n-meta['first']))))
        ref={'T04':444,'T13':1010,'T14':1088,'T15':1980,'T16':2202,'T17':2290}[g]
        s,c=pair(ref); core=(s>220)&(c<145)&(mask_at(ref,g)[y:Y,x:X]>0)
        estimates={}
        for n in meta['active']:
            s1,bg=pair(n)
            if g=='T04':
                # The small title scales along with its parent logo; measure its
                # strongest negative contrasts within that frame's tracked native glyphs.
                use=(mask_at(n,g)[y:Y,x:X]>0)&(bg>175)
                estimates[n]=float(np.mean(np.percentile((bg-s1)[use],[96,98]))) if use.sum()>30 else 0
            else:
                record=LATE.get((n,g),{})
                if record.get('effect'): continue
                use=core&(bg<150)
                if use.sum()<65:continue
                v=float(np.median((s1[use]-bg[use])/(s[use]-bg[use])))
                if v>.97:v=1.
                estimates[n]=float(np.clip(v,0,1))
        if g=='T04':
            norm=np.median([v for n,v in estimates.items() if 426<=n<=470])
            est={n:np.clip(v/norm,0,1) for n,v in estimates.items()}
            for n,v in est.items():
                v=float(np.median([est[k] for k in (n-1,n,n+1) if k in est]))
                estimates[n]=1. if v>=.93 else (0. if v<.03 else v)
        fitted.update({(n,g):round(v,5) for n,v in estimates.items()})
    return fitted
FIT=curves()
def base_clean(n,g):
    if (n,g) in LATE:return rgb(LATE[n,g]['artifacts']['CLEAN']['path'])
    if n in V65 and V65[n]['group']==g:return rgb(V65[n]['clean'])
    dir=V41/('clean_proofs/%04d_%s'%(n,g))
    if n in OVERRIDES and OVERRIDES[n]['group']==g:
        q=Path(OVERRIDES[n]['source_proof']).parent/'CLEAN.png'
        if q.exists():return rgb(q)
    return rgb(dir/'CLEAN.png')
def process(n,g,current):
    meta=META[g];x,y,X,Y=meta['box'];roi=np.s_[y:Y,x:X]
    ref=current[roi].copy(); job=JOBS/g
    if g not in PLATES and (n,g) not in FIT:return 0
    orig=rgb(job/'frames'/('%04d.png'%n))
    lay=latest_layer(n,g)[roi]
    la=lay[:,:,3:4].astype('float32')/255
    a0=LATE.get((n,g),{}).get('opacity',OPACITY[n,g])
    ao=la*a0
    mask=mask_at(n,g)[roi]>0
    w=np.clip(cv2.distanceTransform(mask.astype('uint8'),cv2.DIST_L2,3)/2.2,0,1)
    new=ref.copy()
    if g in PLATES:
        plate=rgb(job/'result/frames/frames'/('%04d.png'%(n-meta['first'])))
        # Preserve the native art which prior layers deliberately left intact,
        # including unaffected divider lines and foreground animation.
        direct=(abs(ref.astype('int16')-orig).max(2)<=1).astype('uint8')
        intact=(direct>0)&(cv2.boxFilter(direct.astype('float32'),-1,(3,3))>.54)
        w[intact]=0
        w[la[:,:,0]>0]=0
        nw=w[:,:,None]
        new=np.rint(new*(1-nw)+plate*nw).clip(0,255).astype('uint8')
    if (n,g) in FIT:
        a1=FIT[n,g];a=la*a1; use=la[:,:,0]>0
        if g in ('T01','T02'):
            # Unmasked areas of the new ink sit over exact original pixels. At
            # the old Japanese text draw the same anti-aliased ink on a moving clean plate.
            background=orig.copy()
            background[mask]=plate[mask]
            rgba=np.rint(background*(1-a)+lay[:,:,:3]*a)
        elif g=='T04':
            background=base_clean(n,g)[roi]
            rgba=np.rint(background*(1-a)+lay[:,:,:3]*a)
        else:
            # Recover the old composite's actual background contribution. This
            # keeps the prior geometry even on floor seams, the school sign and spotlights.
            safe=(1-ao)>0.015
            factor=np.divide(a-ao,1-ao,out=np.zeros_like(a),where=safe)
            rgba=ref+(lay[:,:,:3].astype('float32')-ref)*factor
            if np.any((~safe)&(a1<a0-.01)):
                old_bg=base_clean(n,g)[roi]
                rgba=np.where(~safe,old_bg*(1-a)+lay[:,:,:3]*a,rgba)
        new[use]=np.rint(rgba[use]).clip(0,255).astype('uint8')
    for other in CUTS[n]['groups']:
        if other!=g:
            foreign=latest_layer(n,other)[roi][:,:,3]>0
            new[foreign]=ref[foreign]
    changed=np.any(ref!=new,axis=2);assert not np.any(changed & ~(mask|(la[:,:,0]>0)))
    current[roi]=new
    return int(changed.sum())
def render():
    cv2.setNumThreads(3);stats=collections.Counter();frames=collections.Counter();changed_frames=0;out=OUT/'OP.mkv'
    cmd=[str(FF),'-y','-hide_banner','-nostdin','-loglevel','warning','-f','rawvideo','-pix_fmt','bgr24','-s','1280x720','-r','30000/1001','-i','pipe:0','-i',str(SRC),'-vf',ass_filter(OUT/'OP.ass'),'-map','0:v:0','-map','1:a:0','-c:v','libvpx','-b:v','40M','-crf','4','-qmin','0','-qmax','4','-deadline','good','-cpu-used','3','-threads','6','-auto-alt-ref','0','-lag-in-frames','0','-c:a','copy',str(out)]
    cap=cv2.VideoCapture(str(SRC))
    try:
        with open(HERE/'render.log','wb') as log,subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=log,stderr=log,creationflags=subprocess.CREATE_NO_WINDOW) as enc:
            for n in range(3057):
                ok,src=cap.read();assert ok,n
                result=old_frame(n,src); dirty=False
                for g in CUTS[n]['groups']:
                    count=process(n,g,result)
                    if count:stats[g]+=count;frames[g]+=1;dirty=True
                changed_frames+=int(dirty)
                if n in [65,72,80,88,411,446,478]:cv2.imwrite(str(HERE/('op_%04d.png'%n)),result)
                enc.stdin.write(result.tobytes())
                if n%500==0:print(n,dict(frames),flush=True)
            assert not cap.read()[0]
            enc.stdin.close()
            if enc.wait():raise RuntimeError('OP encoding failed')
    finally:cap.release()
    report=dict(total_frames=3057,frames_changed_before_lyrics=changed_frames,coverage=GROUPS,per_group_changed=dict(frames),background_rebuilt=sorted(PLATES),opacity_fits={g:{str(n):v for (n,k),v in FIT.items() if k==g} for g in sorted(FIXED)},candidate_motion_comparison={g:MET[g]['residual_old_new_external'] for g in GROUPS})
    (HERE/'opening_repair.json').write_text(json.dumps(report,indent=1),'utf8');print('ready',changed_frames,flush=True)
if __name__=='__main__':render()
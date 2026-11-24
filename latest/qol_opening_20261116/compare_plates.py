"""Compare temporally restored source plates with the shipped/approved local layers."""
from pathlib import Path
import collections, json, hashlib
import cv2
import numpy as np
from prepare_video import HERE, OP, V41, JOBS, CUTS, mask_at
cv2.setNumThreads(3)
TEMP=OP/'temporal_repair_20261009'
V57=OP/'typeset/all_groups_v57'
OVERRIDES={r['frame']:r for r in json.loads((V57/'ASSEMBLY.json').read_text('utf8'))['overrides']}
PATCHES=collections.defaultdict(list)
LATE={}
for tag in ('review_v63_final','full_repair_v64','geometry_repair_v65','late_credits_v66','cast_completion_v67','allan_flicker_v68'):
    path=TEMP/tag/('PATCH_INDEX.json' if tag=='review_v63_final' else 'assembly/PATCH_INDEX.json')
    doc=json.loads(path.read_text('utf8'))
    for f,proposals in doc['patches'].items():
        PATCHES[int(f)].extend(proposals if isinstance(proposals,list) else [proposals])
    for r in doc.get('records',[]):
        if 'TARGET_LAYER' in r.get('artifacts',{}):
            LATE[r['frame'],r['group']]=r
OPACITY={(r['frame'],r['id']):r['opacity'] for r in json.loads((V41/'RENDER_REPORT.json').read_text('utf8'))['records']}
def rgb(p):
    im=cv2.imread(str(p),cv2.IMREAD_COLOR)
    if im is None:raise ValueError(str(p))
    return im
def old_frame(n,source=None):
    item=OVERRIDES.get(n) or CUTS[n]
    if n in OVERRIDES or not CUTS[n]['source_reused']:
        path=(V57 if n in OVERRIDES else V41)/item['file']
        old=rgb(path)
    else:
        if source is None:raise ValueError(n)
        old=source.copy()
    for patch in PATCHES[n]:
        with np.load(patch) as d:
            x,y=int(d['x']),int(d['y']);delta=d['delta'];h,w=delta.shape[:2]
            roi=old[y:y+h,x:x+w]
            roi[:]=np.clip(roi.astype(np.int16)+delta,0,255)
    return old
def latest_layer(n,g):
    row=LATE.get((n,g))
    if row:
        p=Path(row['artifacts']['TARGET_LAYER']['path'])
    else:
        proof=V41/('clean_proofs/%04d_%s'%(n,g))
        if n in OVERRIDES and OVERRIDES[n]['group']==g:
            p=Path(OVERRIDES[n]['source_proof']).parent/'TARGET_LAYER.png'
            if not p.exists():p=proof/'TARGET_LAYER.png'
        else:p=proof/'TARGET_LAYER.png'
    return cv2.imread(str(p),cv2.IMREAD_UNCHANGED)
def proposal(n,g,meta,old):
    x,y,X,Y=meta['box'];roi=np.s_[y:Y,x:X];ref=old[roi].copy()
    job=JOBS/g
    plate=rgb(job/'result/frames/frames'/('%04d.png'%(n-meta['first'])))
    original_mask=mask_at(n,g)[roi]
    # All edits stay within the original clean-plate mask.
    alpha=(original_mask>0).astype(np.uint8)
    distance=cv2.distanceTransform(alpha,cv2.DIST_L2,3)
    weight=np.clip(distance/2.2,0,1).astype('float32')
    target=latest_layer(n,g)[roi]; a=target[:,:,3:4].astype('float32')/255
    if not LATE.get((n,g)):
        a*=OPACITY[n,g]
    else:
        a*=float(LATE[n,g].get('opacity',1.0))
    # Preserve exact anti-aliased letterforms when a later pass attached effects
    # or a partially transparent wipe. Use the original pixels along this edge.
    for other in CUTS[n]['groups']:
        if other!=g:
            weight[latest_layer(n,other)[roi][:,:,3]>0]=0
    cand=np.rint(plate.astype('float32')*(1-a)+target[:,:,:3]*a).clip(0,255)
    weight[a[:,:,0]>0]=0
    new=np.rint(ref*(1-weight[:,:,None])+cand*weight[:,:,None]).clip(0,255).astype('uint8')
    valid=(alpha>0)&(a[:,:,0]==0)&(weight>.7)
    return new,ref,valid,plate
def sample(g):
    meta=json.loads((JOBS/g/'job.json').read_text())
    frames=[round(v) for v in np.linspace(meta['active'][0]+4,meta['active'][-1]-4,6)]
    x,y,X,Y=meta['box']
    rows=[]
    for n in frames:
        src=rgb(JOBS/g/'frames'/('%04d.png'%n))
        old=old_frame(n);new,ref,valid,plate=proposal(n,g,meta,old)
        def label(im,t):
            b=cv2.copyMakeBorder(im,20,0,0,0,cv2.BORDER_CONSTANT)
            cv2.putText(b,t,(4,15),0,.42,(110,240,140),1)
            return b
        rows.append(np.hstack([label(src,str(n)+' Japanese'),label(ref,'v68'),label(new,'proposed')]))
    cv2.imwrite(str(HERE/('pilot_'+g+'.jpg')),np.vstack(rows),[cv2.IMWRITE_JPEG_QUALITY,94])
if __name__=='__main__':
    import sys
    for g in sys.argv[1:]:sample(g)
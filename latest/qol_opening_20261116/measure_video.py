"""Score original-frame motion residuals around each caption and recover fixed credit opacity."""
from pathlib import Path
import json,sys
import cv2,numpy as np
from compare_plates import *
cv2.setNumThreads(3)
GRAY=lambda im:cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
def do_opacity(g,meta):
    first,last=meta['active'][0],meta['active'][-1]
    ref={'T01':50,'T02':153,'T03':281}.get(g)
    if ref is None:return {}
    x,y,X,Y=meta['box']; job=JOBS/g
    def pair(n):
        frame=GRAY(rgb(job/'frames'/('%04d.png'%n))).astype('float32')
        clean=GRAY(rgb(job/'result/frames/frames'/('%04d.png'%(n-meta['first'])))).astype('float32')
        return frame,clean
    ref_src,ref_bg=pair(ref)
    core=(ref_src>220)&(ref_bg<145)&(mask_at(ref,g)[y:Y,x:X]>0)
    evidence={}
    for n in meta['active']:
        src,bg=pair(n)
        valid=core&(bg<150)
        if valid.sum()<50:continue
        ratio=(src[valid]-bg[valid])/(ref_src[valid]-bg[valid])
        measure=float(np.median(ratio));measure=float(np.clip(measure,0,1))
        if measure>.97:measure=1.0
        evidence[n]={'fitted':round(measure,4),'pixels':int(valid.sum()),'estimate':round(float(OPACITY[n,g]),4)}
    good=np.array(sorted(evidence))
    for n in meta['active']:
        if n not in evidence:
            # With the camera completely overexposed there is no usable white ink.
            # Keep the authored source fade until contrast first becomes measurable.
            if n<good.min() or n>good.max():value=OPACITY[n,g]
            else:value=float(np.interp(n,good,[evidence[int(t)]['fitted'] for t in good]))
            evidence[n]={'fitted':value,'pixels':0,'estimate':OPACITY[n,g]}
    return evidence
def factor_flow(orig,mask):
    # Estimate motion in the scene without letting overlaid stationary glyphs
    # anchor the flow. Deblend masks at low resolution using only source pixels.
    mono=GRAY(orig); h,w=mono.shape; small=cv2.resize(mono,((w+1)//2,(h+1)//2),interpolation=cv2.INTER_AREA)
    sm=cv2.resize(mask.astype('uint8'),(small.shape[1],small.shape[0]),interpolation=cv2.INTER_AREA)
    return cv2.inpaint(small,(sm>20).astype('uint8'),3,cv2.INPAINT_TELEA) if np.any(sm) else small
def brief(data):
    if not data:return [None,None,None]
    return np.round(np.mean(np.asarray(data),axis=0),3).tolist()
def score(g):
    job=JOBS/g; meta=json.loads((job/'job.json').read_text()); x,y,X,Y=meta['box']
    curves=do_opacity(g,meta); res=[]; prev=None; dis=cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_FAST)
    h,w=Y-y,X-x; xx,yy=np.meshgrid(np.arange(w,dtype='float32'),np.arange(h,dtype='float32'))
    samples=[]; points=np.linspace(3,len(meta['active'])-4,5).astype(int)
    for j,n in enumerate(meta['active']):
        orig=rgb(job/'frames'/('%04d.png'%n)); old=old_frame(n); cand,base,valid,plate=proposal(n,g,meta,old)
        mask=mask_at(n,g)[y:Y,x:X]
        maskfull=np.maximum(mask,(latest_layer(n,g)[y:Y,x:X,3]>0).astype('uint8')*255)
        reduced=factor_flow(orig,maskfull)
        if prev is not None and n==prev[0]+1:
            pn,pr,pbase,pnew,pvalid,pbg=prev
            flow=dis.calc(reduced,pr,None)
            flow=cv2.resize(flow,(w,h),interpolation=cv2.INTER_LINEAR)*2
            bx=xx+flow[:,:,0];by=yy+flow[:,:,1]
            def warp(im,flags=cv2.INTER_LINEAR):return cv2.remap(im,bx,by,flags,borderMode=cv2.BORDER_REPLICATE)
            good=valid&(warp(pvalid.astype('uint8'),cv2.INTER_NEAREST)>0)
            # Exclude antialias neighbourhood of Korean strokes on both clocks.
            good=cv2.erode(good.astype('uint8'),np.ones((3,3),np.uint8))>0
            good&=(bx>2)&(bx<w-3)&(by>2)&(by<h-3)
            if good.sum()>100:
                a=np.abs(GRAY(base).astype('float32')-warp(pbase)).astype('float32')
                b=np.abs(GRAY(cand).astype('float32')-warp(pnew)).astype('float32')
                ring=(cv2.dilate(maskfull,np.ones((17,17),np.uint8))>0)&(maskfull==0)
                if ring.sum()>0:
                    scene=np.abs(GRAY(orig).astype('float32')-warp(pbg)).astype('float32')
                    samples.append([float(a[good].mean()),float(b[good].mean()),float(scene[ring].mean())])
                res.append([n,round(float(a[good].mean()),3),round(float(b[good].mean()),3),int(good.sum())])
        if j in points:
            def fit(ar):return cv2.resize(ar,(min(310,w),max(24,int(min(310,w)*h/w))),interpolation=cv2.INTER_AREA)
            samples_png=[fit(t) for t in (orig,base,cand)]
            if 'rows' not in locals():rows=[]
            rows.append(np.hstack(samples_png))
        prev=(n,reduced,GRAY(base),GRAY(cand),valid,GRAY(orig))
    page=np.vstack(rows);cv2.imwrite(str(job/'contact.jpg'),page,[cv2.IMWRITE_JPEG_QUALITY,91])
    out={'group':g,'frames':len(meta['active']),'paired':len(res),'residual_old_new_external':brief(samples),'opacity':curves,'per_frame':res}
    (job/'metrics.json').write_text(json.dumps(out,indent=1),'utf8')
    print(g,out['residual_old_new_external'], 'reference-opacity median difference:',(round(float(np.median([abs(r['fitted']-r['estimate']) for r in curves.values()])),3) if curves else None),flush=True)
if __name__=='__main__':
    for g in sys.argv[1:]:score(g)
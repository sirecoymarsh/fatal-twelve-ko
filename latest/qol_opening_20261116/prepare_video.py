"""Prepare lossless source plates for motion-consistent localized credit repairs."""
from pathlib import Path
import argparse, json
import cv2
import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
OP = BASE / "opening_localization_20261002"
V41 = OP / "typeset/all_groups_v41"
CUTS = [json.loads(line) for line in (V41/"CACHE_INDEX.jsonl").read_text("utf-8").splitlines()]
SOURCE = OP / "source/movies/OP.mkv"
JOBS = HERE / "video_jobs"

def mask_at(n, group):
    if n < 0 or n >= len(CUTS) or group not in CUTS[n]["groups"]:
        return None
    directory = V41 / ("clean_proofs/%04d_%s" % (n, group))
    image = cv2.imread(str(directory / "MASK.png"), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(str(directory))
    return image

def prepare(group):
    indices = [r["frame"] for r in CUTS if group in r["groups"]]
    box_px=[]
    for n in indices:
        mask=mask_at(n,group)
        if np.any(mask):
            x,y,w,h=cv2.boundingRect(mask)
            box_px.append((x,y,x+w,y+h))
    # Supply motion context and preserve full native ink resolution.
    x0,y0,x1,y1=np.min(box_px,axis=0)[0],np.min(box_px,axis=0)[1],np.max(box_px,axis=0)[2],np.max(box_px,axis=0)[3]
    x0=max(0,(int(x0)-70)//8*8);y0=max(0,(int(y0)-55)//8*8)
    x1=min(1280,((int(x1)+77)//8)*8);y1=min(720,((int(y1)+62)//8)*8)
    first=max(0,indices[0]-8);last=min(3056,indices[-1]+8)
    job=JOBS/group
    for dn in ("frames","masks"):
        (job/dn).mkdir(parents=True,exist_ok=True)
    cap=cv2.VideoCapture(str(SOURCE));cap.set(cv2.CAP_PROP_POS_FRAMES,first)
    for n in range(first,last+1):
        got,frame=cap.read()
        if not got:raise ValueError(n)
        mask=mask_at(n,group)
        if mask is None: mask=np.zeros((720,1280),np.uint8)
        # Keep masks from other groups out of reference frames on adjoining wipes.
        for other in CUTS[n]["groups"]:
            if other!=group:mask=np.maximum(mask,mask_at(n,other))
        mask=cv2.dilate((mask>0).astype('uint8')*255,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
        nfile="%04d.png"%n
        cv2.imwrite(str(job/"frames"/nfile),frame[y0:y1,x0:x1],[cv2.IMWRITE_PNG_COMPRESSION,1])
        cv2.imwrite(str(job/"masks"/nfile),mask[y0:y1,x0:x1])
    cap.release()
    meta=dict(group=group,active=indices,first=first,last=last,box=[x0,y0,x1,y1],source=str(SOURCE))
    (job/"job.json").write_text(json.dumps(meta,indent=2),"utf-8")
    print(group,len(indices),meta["box"],flush=True)

if __name__=="__main__":
    import sys
    for g in sys.argv[1:]:prepare(g)

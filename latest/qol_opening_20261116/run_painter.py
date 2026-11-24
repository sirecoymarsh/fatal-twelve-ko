"""Reuse the pinned local ProPainter model on sequences of Japanese source plates."""
import os, runpy, sys
from pathlib import Path
WORK=Path(__file__).resolve().parent
REPO=Path("P:/AI/Codex/projects/forest-opening-korean/tools/ProPainter-e870e79321c31b733e2031af5aa2fb1fe3ac7eec")
for var in ("TEMP","TMP","MPLCONFIGDIR","TORCH_HOME","CUDA_CACHE_PATH"):
    folder=WORK/"cache"/var
    folder.mkdir(parents=True,exist_ok=True)
    os.environ[var]=str(folder)
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
sys.path.insert(0,str(REPO))
os.chdir(REPO)
import imageio
imageio.mimwrite=lambda *args,**kwargs: None
jobs=list(sys.argv[1:])
for group in jobs:
    job=WORK/"video_jobs"/group
    args=["--video",str(job/"frames"),"--mask",str(job/"masks"),"--output",str(job/"result"),"--save_frames",
        "--mask_dilation","0","--subvideo_length","32","--neighbor_length","6","--ref_stride","5","--fp16"]
    sys.argv=[str(REPO/"inference_propainter.py")]+args
    print("PROCESSING",group,flush=True)
    runpy.run_path(str(REPO/"inference_propainter.py"),run_name="__main__")

"""Build and exercise the overlay with the game's own Ren'Py engine and an isolated save directory."""
from pathlib import Path
import os,shutil,subprocess,hashlib,sys,json
HERE=Path(__file__).resolve().parent
BASE=HERE.parent;LIVE=BASE/'runtime_review';GAME=LIVE/'game';OUT=HERE/'delivery'
FIX=HERE/'fixture';FG=FIX/'game';QA=HERE/'game_qa'
def asset(s,d):
    d.parent.mkdir(parents=True,exist_ok=True)
    if s.suffix in {'.rpy','.rpyc','.rpyb'}:
        if not d.exists():shutil.copy2(s,d)
    elif not d.exists():
        try:os.link(s,d)
        except OSError:shutil.copy2(s,d)
def prepare():
    for folder in ('lib','renpy'):
        dst=FIX/folder
        if not dst.exists():shutil.copytree(LIVE/folder,dst)
    for name in ('fatal.exe','fatal.py'):
        if not (FIX/name).exists():shutil.copy2(LIVE/name,FIX/name)
    for s in GAME.rglob('*'):
        rel=s.relative_to(GAME)
        if not s.is_file() or 'cache' in rel.parts or 'saves' in rel.parts or 'movies' in rel.parts or s.suffix=='.bak':continue
        asset(s,FG/rel)
    for name in ('f12_bonus_access','f12_flowchart'):
        shutil.copyfile(OUT/(name+'.rpy'),FG/(name+'.rpy'))
    shutil.copyfile(HERE/'fixture_probe.rpy',FG/'zz_bonus_isolated_test.rpy')
def execute(stage,timeout=180):
    QA.mkdir(exist_ok=True)
    env=dict(os.environ)
    for k,n in [('TEMP','temp'),('TMP','temp'),('APPDATA','appdata'),('LOCALAPPDATA','localappdata')]:
        q=FIX/n;q.mkdir(exist_ok=True);env[k]=str(q)
    env.update(RENPY_LOG_BASE=str(FIX),RENPY_LOG_TO=str(FIX),RENPY_SKIP_MAIN_MENU='1',RENPY_SKIP_SPLASHSCREEN='1',RENPY_DISABLE_SOUND='1',SDL_AUDIODRIVER='dummy',SDL_VIDEO_WINDOW_POS='30,40',F12_QA_ROOT=str(QA),F12_QA_PHASE=stage,PYTHONDONTWRITEBYTECODE='1')
    sd=FIX/'saves';sd.mkdir(exist_ok=True)
    args=[str(FIX/'fatal.exe'),str(FIX)]+(['compile','--keep-orphan-rpyc'] if stage=='compile' else ['run'])+['--savedir',str(sd)]
    si=subprocess.STARTUPINFO();si.dwFlags|=subprocess.STARTF_USESHOWWINDOW;si.wShowWindow=0
    cp=subprocess.run(args,cwd=FIX,env=env,capture_output=True,timeout=timeout,startupinfo=si,creationflags=subprocess.CREATE_NO_WINDOW)
    (QA/(stage+'.log')).write_bytes(cp.stdout+cp.stderr)
    if cp.returncode or b'Full traceback:' in cp.stdout+cp.stderr:raise RuntimeError((stage,cp.returncode,cp.stdout[-800:],cp.stderr[-800:]))
    if stage!='compile':
        report=json.loads((QA/(stage+'.json')).read_text('utf8'));print(report,flush=True);assert report['status']=='PASS'
def main():
    if 'build' in sys.argv:
        prepare();execute('compile')
        for n in ('f12_bonus_access','f12_flowchart'):
            f=FG/(n+'.rpyc');src=(OUT/(n+'.rpy')).read_bytes().replace(b'\r\n',b'\n').replace(b'\r',b'\n')
            assert f.read_bytes()[-16:]==hashlib.md5(src).digest(),n
            shutil.copy2(f,OUT/f.name)
    for name in ('functional','reopen'):
        if name in sys.argv:execute(name)
if __name__=='__main__':main()

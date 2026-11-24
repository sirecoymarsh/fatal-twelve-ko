from pathlib import Path
import os,sys,shutil,subprocess,json,hashlib
from build_fix import HERE,HISTORY,BASE,GAME,PAYLOAD,sha
FIX=HERE/'fixture';FG=FIX/'game';QA=HERE/'qa';ENGINE=HISTORY/'fixture/fatal.exe'
NAMES=('f12_flowchart','f12_bonus_access')
def setup():
    for dir in (FG,QA,FIX/'temp',FIX/'appdata',FIX/'localappdata',FIX/'saves'):
        dir.mkdir(parents=True,exist_ok=True)
    # Reuse the verified Ren'Py engine and local game archives. Only static assets
    # are hardlinked; neither script compilation nor persistence can reach live files.
    for s in GAME.rglob('*'):
        rel=s.relative_to(GAME)
        if not s.is_file() or any(k in rel.parts for k in ('cache','saves','movies')):continue
        if s.suffix in ('.rpy','.rpyc') or (rel.parts[0]=='tl' and 'gui' in rel.parts) or s.suffix=='.rpa':
            d=FG/rel;d.parent.mkdir(parents=True,exist_ok=True)
            if d.exists():continue
            if s.suffix in ('.rpy','.rpyc'):shutil.copy2(s,d)
            else:
                try:os.link(s,d)
                except OSError:shutil.copyfile(s,d)
    shutil.copy2(HERE/'probe.rpy',FG/'zz_chart_regression.rpy')
def run(phase,cli='run'):
    env=dict(os.environ)
    for key,dir in [('TEMP','temp'),('TMP','temp'),('APPDATA','appdata'),('LOCALAPPDATA','localappdata')]:env[key]=str(FIX/dir)
    env.update(PYTHONDONTWRITEBYTECODE='1',RENPY_LOG_BASE=str(FIX),RENPY_LOG_TO=str(FIX),RENPY_SKIP_MAIN_MENU='1',RENPY_SKIP_SPLASHSCREEN='1',RENPY_DISABLE_SOUND='1',SDL_AUDIODRIVER='dummy',SDL_VIDEO_WINDOW_POS='-12000,-12000',RENPY_PERFORMANCE_TEST='0',F12_CHART_PHASE=phase,F12_CHART_QA=str(QA))
    args=[str(ENGINE),str(FIX),cli]+(['--keep-orphan-rpyc'] if cli=='compile' else [])+['--savedir',str(FIX/'saves')]
    si=subprocess.STARTUPINFO();si.dwFlags|=subprocess.STARTF_USESHOWWINDOW;si.wShowWindow=0
    cp=subprocess.run(args,env=env,cwd=FIX,capture_output=True,timeout=100,startupinfo=si,creationflags=subprocess.CREATE_NO_WINDOW)
    (QA/(phase+'.log')).write_bytes(cp.stdout+cp.stderr)
    if cp.returncode or b'Full traceback:' in cp.stdout+cp.stderr:raise RuntimeError((phase,cp.returncode,(cp.stdout+cp.stderr)[-1050:]))
    if cli=='compile':return
    report=json.loads((QA/(phase+'.json')).read_text('utf8'));print(phase,report['status'],report.get('error',''),flush=True)
    assert report['status']=='PASS',report
def fixed_scripts():
    for name in NAMES:shutil.copy2(PAYLOAD/(name+'.rpy'),FG/(name+'.rpy'))
    run('compile_fixed','compile')
    for name in NAMES:
        p=FG/(name+'.rpyc');src=(PAYLOAD/(name+'.rpy')).read_bytes().replace(b'\r\n',b'\n').replace(b'\r',b'\n')
        assert p.read_bytes()[-16:]==hashlib.md5(src).digest()
        shutil.copy2(p,PAYLOAD/p.name)
        # Execute the compiled patch that will actually be installed.
        (FG/(name+'.rpy')).unlink()
def main():
    for mode in sys.argv[1:]:
        if mode=='setup':setup()
        elif mode=='fixed':fixed_scripts()
        else:run(mode)
if __name__=='__main__':main()
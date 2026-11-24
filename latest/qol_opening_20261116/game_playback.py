from test_feature import *
def run():
    path=FG/'tl/korean/movies/OP.mkv'
    path.parent.mkdir(parents=True,exist_ok=True)
    if not path.exists():os.link(OUT/'OP.mkv',path)
    assert path.stat().st_size==(OUT/'OP.mkv').stat().st_size
    shutil.copy2(HERE/'fixture_movie.rpy',FG/'zz_movie_playback_check.rpy')
    env=dict(os.environ);env.pop('RENPY_DISABLE_SOUND',None)
    for k,n in [('TEMP','temp'),('TMP','temp'),('APPDATA','appdata'),('LOCALAPPDATA','localappdata')]:env[k]=str(FIX/n)
    env.update(RENPY_SKIP_SPLASHSCREEN='1',RENPY_SKIP_MAIN_MENU='1',PYTHONDONTWRITEBYTECODE='1',SDL_AUDIODRIVER='dummy',SDL_VIDEO_WINDOW_POS='30,40',F12_QA_ROOT=str(QA),F12_QA_PHASE='movie',RENPY_LOG_TO=str(FIX))
    cp=subprocess.run([str(FIX/'fatal.exe'),str(FIX),'run','--savedir',str(FIX/'saves')],env=env,cwd=FIX,capture_output=True,timeout=190,creationflags=subprocess.CREATE_NO_WINDOW)
    (QA/'playback.log').write_bytes(cp.stdout+cp.stderr)
    assert cp.returncode==0,cp.returncode
    proof=json.loads((QA/'movie.json').read_text('utf8'));print(proof['status'],proof.get('elapsed'),max(proof.get('seconds') or [0]),flush=True)
if __name__=='__main__':run()
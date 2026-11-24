"""Install the validated Korean assets in the playable project with bounded rollback."""
from pathlib import Path
import json,os,subprocess,hashlib,shutil,time,datetime
from apply_lyrics import HERE,BASE,OUT,OP,ED,sha,NEW
GAME=BASE/'runtime_review/game'
REC=HERE/'install'
REPORT=REC/'INSTALL.json'
def dump(p,data):
    tmp=p.with_suffix(p.suffix+'.pending');tmp.write_text(json.dumps(data,indent=2,ensure_ascii=False),'utf8');os.replace(tmp,p)
def inside(path,root):
    return path.resolve().is_relative_to(root.resolve())
def has_player():
    # Live gameplay, isolated QA, and the launcher have the same executable name.
    # Block only the played game's executable and its child, identified by path.
    root=str(GAME.parent.resolve()).replace("'","''")
    script="$a = @(Get-CimInstance Win32_Process -Filter \"Name='fatal.exe'\" -ErrorAction Stop | Where-Object { $_.ExecutablePath -like '"+root+"\\*' }); $a.Count"
    output=subprocess.check_output(['powershell.exe','-NoProfile','-Command',script],creationflags=subprocess.CREATE_NO_WINDOW,text=True)
    return int(output.strip())!=0
def main():
    REC.mkdir(exist_ok=True)
    if REPORT.exists():
        r=json.loads(REPORT.read_text('utf8'))
        if r['status']=='INSTALLED':
            assert all(sha(GAME/f['path'])==f['after'] for f in r['files']);return
        raise RuntimeError('Prior transaction requires inspection.')
    movie=json.loads((HERE/'movie_validation.json').read_text('utf8'))
    expected={p['movie']:p['sha256'] for p in movie}
    for k in ['functional','reopen','movie']:
        q=json.loads((HERE/'game_qa'/(k+'.json')).read_text('utf8'))
        assert q['status']=='PASS',k
        if k=='movie':assert q['selected_file_sha256']==expected['OP']
    old={'OP':'0d5eae4f3a49fa2b98cd16eb0b2066b09153b63a0c33bed3ec877923d7d3e10c','ED_MHR_UNH':'f9892e9fd4e658b0d48f3c03bb15e75426f18e29bd37a3f0c2bdb925f7811e79'}
    mapping={f'tl/korean/movies/{k}.mkv':(OUT/(k+'.mkv'),h,expected[k]) for k,h in old.items()}
    for name in ('f12_bonus_access','f12_flowchart'):
        source=OUT/(name+'.rpy');binary=OUT/(name+'.rpyc')
        norm=lambda b:b.replace(b'\r\n',b'\n').replace(b'\r',b'\n')
        assert binary.read_bytes()[-16:]==hashlib.md5(norm(source.read_bytes())).digest()
        orig=None
        if name=='f12_flowchart':
            orig=json.loads((HERE/'feature_source.json').read_text('utf8'))['before_chart']
            native_src=GAME/source.name;native_bin=GAME/binary.name
            assert sha(native_src)==orig
            # The game's active bytecode matches the copy used to make this change.
            known=(BASE/'argon_20261116/apply_20261116_1759/engine_check/game'/binary.name)
            check=hashlib.md5(norm(native_src.read_bytes())).digest()
            assert native_bin.read_bytes()[-16:]==check or known.exists() and sha(native_bin)==sha(known)
        mapping[source.name]=(source,orig,sha(source))
        mapping[binary.name]=(binary,sha(GAME/binary.name) if orig else None,sha(binary))
    assert not has_player(), 'Playable game was reopened during preparation'
    rows=[]
    for rel,(src,prev,after) in mapping.items():
        dst=GAME/rel;backup=REC/'before'/rel;stage=REC/'stage'/rel
        assert inside(dst,GAME) and inside(backup,REC) and inside(stage,REC)
        assert (sha(dst) if dst.exists() else None)==prev,(rel,'baseline changed')
        if prev:
            backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(dst,backup);assert sha(backup)==prev
        stage.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,stage);assert sha(stage)==after
        rows.append(dict(path=rel,before=prev,after=after,backup=str(backup) if prev else None))
    for root in (ED,OP):
        shutil.copy2(root/'LATEST_INSTALL.json',REC/('previous_'+root.name+'.json'))
    record=dict(status='STAGED',files=rows,updated=datetime.datetime.now().astimezone().isoformat(),wording=NEW,feature_test=str(HERE/'game_qa/functional.json'),video_validation=str(HERE/'movie_validation.json'),playback=str(HERE/'game_qa/movie.json'),subtitle_sources=[str(OUT/'OP.ass'),str(OUT/'ED_MHR_UNH.ass')])
    dump(REPORT,record);done=[]
    try:
        assert not has_player()
        for r in rows:
            dest=GAME/r['path'];os.replace(REC/'stage'/r['path'],dest);done.append(r)
        assert all(sha(GAME/r['path'])==r['after'] for r in rows)
        # Historical build inputs stay immutable. The active pointers reference the
        # new authored subtitle sources so subsequent builds can inherit the change.
        dump(OP/'LATEST_INSTALL.json',{'record':str(REPORT),'target':str(GAME/'tl/korean/movies/OP.mkv'),'sha256':expected['OP'],'status':'INSTALLED_RUNTIME_PLAYBACK_VERIFIED','subtitle_source':str(OUT/'OP.ass'),'source_frames':3057})
        ed=json.loads((ED/'LATEST_INSTALL.json').read_text('utf8'))
        ed['version']='v3 + 20261116 lyric';ed['record']=str(REPORT)
        for e in ed['assets']:
            if e['asset']!='ED_MHR_UNH':continue
            e.update(sha256=expected['ED_MHR_UNH'],bytes=(OUT/'ED_MHR_UNH.mkv').stat().st_size,stage=str(OUT/'ED_MHR_UNH.mkv'),subtitle_source=str(OUT/'ED_MHR_UNH.ass'),patched_backup=str(OUT/'ED_MHR_UNH.mkv'),previous_version_backup=str(REC/'before/tl/korean/movies/ED_MHR_UNH.mkv'),preview_sha256=expected['ED_MHR_UNH'],full_decode_errors=0)
        dump(ED/'LATEST_INSTALL.json',ed)
        record['status']='INSTALLED';dump(REPORT,record)
    except BaseException:
        for r in reversed(done):
            dest=GAME/r['path']
            if r['backup']:shutil.copy2(r['backup'],dest)
            elif dest.exists() and sha(dest)==r['after']:dest.unlink()
        for root in (ED,OP):shutil.copy2(REC/('previous_'+root.name+'.json'),root/'LATEST_INSTALL.json')
        record['status']='ROLLED_BACK';dump(REPORT,record);raise
    print([(r['path'],r['after'][:12]) for r in rows],flush=True)
if __name__=='__main__':main()
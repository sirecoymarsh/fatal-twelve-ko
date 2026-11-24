"""Install the four verified scripts in the live game and the current build package."""
from pathlib import Path
import datetime,hashlib,json,os,shutil
from build_fix import HERE,HISTORY,BASE,GAME,PAYLOAD,BUILD,GENERATED,sha
CHECKS=('old_setup','old_reopen','old_save_fixed','cancel_after_reopen','verify_reclosed')
REC=HERE/'install';RECEIPT=REC/'INSTALL.json'
def read(p):return json.loads(p.read_text('utf8'))
def write(p,item):p.write_text(json.dumps(item,ensure_ascii=False,indent=2)+'\n','utf8')
def main():
    REC.mkdir(exist_ok=True)
    if RECEIPT.exists() and read(RECEIPT).get('status')=='INSTALLED':
        assert all(sha(BASE/f['path'])==f['after'] for f in read(RECEIPT)['files'])
        return
    for phase in CHECKS:
        r=read(HERE/'qa'/(phase+'.json'))
        assert r['status']=='PASS' and r['phase']==phase
    baseline=read(HERE/'baseline.json')
    for name in ('f12_bonus_access','f12_flowchart'):
        src=(PAYLOAD/(name+'.rpy')).read_bytes().replace(b'\r\n',b'\n').replace(b'\r',b'\n')
        assert (PAYLOAD/(name+'.rpyc')).read_bytes()[-16:]==hashlib.md5(src).digest()
    stamp=datetime.datetime.now().astimezone().isoformat()
    previous=HISTORY/'install/INSTALL.json'; manifest=read(previous)
    mapping={}
    for name in ('f12_flowchart.rpy','f12_flowchart.rpyc','f12_bonus_access.rpy','f12_bonus_access.rpyc'):
        for root in (GAME,GENERATED):
            target=root/name
            assert sha(target)==baseline[name],('Game or delivery changed',target)
            mapping[target]=PAYLOAD/name
        entry=next(x for x in manifest['files'] if x['path']==name)
        assert entry['after']==baseline[name]
        entry['after']=sha(PAYLOAD/name)
    for name in ('bonus_functions.txt','build_bonus.py'):
        mapping[HISTORY/name]=BUILD/name
    record={"status":"PREPARED","installed_at":stamp,"files":[],"checks":list(CHECKS),
            "official_reference":"https://www.renpy.org/doc/html/persistent.html",
            "engine":"Ren'Py 6.99.14.3.3347","player_save_files_written":[]}
    manifest['flowchart_cancel_fix']=str(RECEIPT)
    next_manifest=REC/'next_install_record.json';write(next_manifest,manifest);mapping[previous]=next_manifest
    progress_path=HISTORY/'PROGRESS.json';progress=read(progress_path)
    progress['status']='installed_verified'
    progress['flowchart_cancel_fix']={'record':str(RECEIPT),'qa':str(HERE/'qa'),'status':'PASS'}
    if str(progress.get('next','')).startswith('Check the isolated full-length opening playback'):progress.pop('next')
    next_progress=REC/'next_progress.json';write(next_progress,progress);mapping[progress_path]=next_progress
    auth_paths={GAME,GENERATED,HISTORY,HISTORY/'install'}
    for path,source in mapping.items():
        assert path.resolve().parent in auth_paths
        rel=path.relative_to(BASE);backup=REC/'before'/rel;stage=REC/'stage'/rel
        for t in (backup,stage):
            assert t.resolve().is_relative_to(REC.resolve())
            t.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,backup);shutil.copy2(source,stage)
        rec={'path':str(rel),'before':sha(path),'after':sha(source)}
        assert sha(backup)==rec['before'] and sha(stage)==rec['after']
        record['files'].append(rec)
    # The patch applies on load. Nothing in the process, player profile, or save slots is modified.
    done=[]
    try:
        for f in record['files']:
            path=BASE/f['path']
            assert sha(path)==f['before'],('changed during staging', path)
            os.replace(REC/'stage'/f['path'],path);done.append(f)
        assert all(sha(BASE/f['path'])==f['after'] for f in record['files'])
        record['status']='INSTALLED';tmp=REC/'receipt.tmp';write(tmp,record);os.replace(tmp,RECEIPT)
    except BaseException:
        for f in reversed(done):
            path=BASE/f['path'];backup=REC/'before'/f['path']
            assert sha(backup)==f['before']
            if sha(path)==f['after']:shutil.copy2(backup,path)
        raise
    print(record['status'],[(Path(f['path']).name,f['after'][:12]) for f in record['files'][:8:2]],flush=True)
if __name__=='__main__':main()
import ast, json, re
from pathlib import Path
base=Path(r"P:\AI\Codex\projects\fatal-twelve-ko\work\extracted")
LIT=r'(?:"""(?:(?!"{3})[\s\S]|\\.)*"""|"(?:\\.|[^"\\])*")'
rx_u=re.compile(r'_\(\s*(?P<lit>'+LIT+r')\s*\)')
rx_old=re.compile(r'(?m)^[ \t]*old[ \t]+(?P<lit>'+LIT+r')')
out={}
for name in ('characters','gamedata'):
    src=(base/'system'/f'{name}.rpy').read_text(encoding='utf-8')
    slot=(base/'tl'/'tl'/'english'/f'{name}.rpy').read_text(encoding='utf-8')
    src_vals=[ast.literal_eval(m.group('lit')) for m in rx_u.finditer(src)]
    old_vals=[ast.literal_eval(m.group('lit')) for m in rx_old.finditer(slot)]
    su=list(dict.fromkeys(src_vals)); ou=list(dict.fromkeys(old_vals))
    out[name]={
      'source_occurrences':len(src_vals),'source_unique':len(su),
      'official_old_occurrences':len(old_vals),'official_old_unique':len(ou),
      'old_only':[x for x in ou if x not in set(su)],
      'source_only':[x for x in su if x not in set(ou)],
    }
Path(r"work\system_ui\_key_diff.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

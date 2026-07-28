#!/usr/bin/env python3
import argparse,re,json
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('skill_dir'); a=p.parse_args(); root=Path(a.skill_dir)
rules={'critical':[r'curl[^\n|]*\|\s*(?:bash|sh)',r'-----BEGIN .*PRIVATE KEY-----'], 'high':[r'\beval\s+',r'\brm\s+-rf\b',r'(?i)(?:api[_-]?key|token|password)\s*[:=]\s*["\'][^"\']+["\']'], 'medium':[r'(?i)cookies?-from-browser',r'(?i)subprocess|os\.system|child_process']}
findings=[]
for f in root.rglob('*'):
 if not f.is_file() or f.stat().st_size>1_000_000: continue
 try:t=f.read_text(errors='ignore')
 except:continue
 for level,patterns in rules.items():
  for pattern in patterns:
   if re.search(pattern,t): findings.append({'level':level,'file':str(f.relative_to(root)),'pattern':pattern})
print(json.dumps({'root':str(root),'findings':findings,'note':'静态扫描需人工复核'},ensure_ascii=False,indent=2))
raise SystemExit(1 if any(x['level']=='critical' for x in findings) else 0)

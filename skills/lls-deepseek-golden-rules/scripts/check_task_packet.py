#!/usr/bin/env python3
"""检查公开任务包 JSON 是否具备分阶段执行所需字段。"""
import argparse,json,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('packet');a=p.parse_args()
try:d=json.loads(Path(a.packet).read_text())
except Exception as e: print(json.dumps({'ok':False,'error':str(e)},ensure_ascii=False));sys.exit(2)
required=['objective','audience','inputs','constraints','deliverable','acceptance']; missing=[k for k in required if not d.get(k)]
route=d.get('route'); allowed={'fast','deep','tool','high-impact-review'}
issues=[]
if route not in allowed: issues.append('route 必须是 fast/deep/tool/high-impact-review')
if route in {'tool','high-impact-review'} and not d.get('human_gate'): issues.append('该路线必须声明 human_gate')
print(json.dumps({'ok':not missing and not issues,'missing':missing,'issues':issues,'stages':['facts','draft','challenge','final','verify']},ensure_ascii=False,indent=2));sys.exit(0 if not missing and not issues else 1)

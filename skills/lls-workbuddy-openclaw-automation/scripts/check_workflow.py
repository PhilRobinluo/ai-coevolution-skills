#!/usr/bin/env python3
"""检查自动化 JSON 的权限、幂等、人工关口与回执字段。"""
import argparse,json,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('workflow');a=p.parse_args();d=json.loads(Path(a.workflow).read_text())
issues=[]; steps=d.get('steps') or []
if not d.get('trigger'):issues.append('缺少 trigger')
if not d.get('idempotency_key'):issues.append('缺少 idempotency_key')
if not d.get('receipt'):issues.append('缺少 receipt')
for i,s in enumerate(steps,1):
 for k in ['name','type','permissions','on_failure']:
  if not s.get(k):issues.append(f'步骤{i}缺少{k}')
 if s.get('type') in {'publish','delete','payment','external-write'} and not s.get('human_gate'):issues.append(f'步骤{i}高影响动作缺少 human_gate')
print(json.dumps({'ok':not issues,'issues':issues,'steps':len(steps)},ensure_ascii=False,indent=2));sys.exit(0 if not issues else 1)

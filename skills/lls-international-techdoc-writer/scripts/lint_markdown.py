#!/usr/bin/env python3
"""对技术文档 Markdown 做发布前的最小结构检查。"""
import argparse,json,re,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('file');a=p.parse_args();t=Path(a.file).read_text()
issues=[]
for h in ['前置条件','步骤','故障排查','版本']:
 if not re.search(r'^#{1,4}\s+.*'+h,t,re.M):issues.append('缺少章节:'+h)
if re.search(r'\b(?:TODO|TBD|FIXME)\b',t,re.I):issues.append('存在未关闭占位符')
steps=re.findall(r'^\d+\.\s+.+',t,re.M)
if not steps:issues.append('没有编号步骤')
print(json.dumps({'ok':not issues,'issues':issues,'numbered_steps':len(steps)},ensure_ascii=False,indent=2));sys.exit(0 if not issues else 1)

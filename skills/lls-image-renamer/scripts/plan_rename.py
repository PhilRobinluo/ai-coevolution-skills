#!/usr/bin/env python3
import argparse,json,re
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('file'); p.add_argument('--description',required=True); a=p.parse_args()
src=Path(a.file); safe=re.sub(r'[^0-9A-Za-z\u4e00-\u9fff-]+','-',a.description).strip('-')
dst=src.with_name(f"{safe}__{src.name}")
print(json.dumps({'from':str(src),'to':str(dst),'dry_run':True},ensure_ascii=False))

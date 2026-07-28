#!/usr/bin/env python3
"""生成可审阅的图片改名清单；显式 --apply 后才执行，且绝不覆盖现有文件。"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path

def safe_name(text:str,max_len:int=40)->str:
    name=re.sub(r'[^0-9A-Za-z\u4e00-\u9fff-]+','-',text.strip()).strip('-')
    name=re.sub(r'-+','-',name)[:max_len].rstrip('-')
    if not name: raise ValueError('描述无法生成有效文件名')
    return name

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument('file',nargs='?'); p.add_argument('--description'); p.add_argument('--mapping',type=Path,help='JSON 列表：file, description'); p.add_argument('--root',type=Path,default=Path('.')); p.add_argument('--manifest',type=Path); p.add_argument('--apply',action='store_true'); a=p.parse_args()
    if a.mapping:
        raw=json.loads(a.mapping.read_text()); entries=raw
    elif a.file and a.description: entries=[{'file':a.file,'description':a.description}]
    else: p.error('使用 file + --description，或 --mapping')
    root=a.root.resolve(); plan=[]; targets=set(); errors=[]
    for item in entries:
        src=(root/item['file']).resolve() if not Path(item['file']).is_absolute() else Path(item['file']).resolve()
        try: src.relative_to(root)
        except ValueError: errors.append({'file':str(src),'error':'文件不在 root 内'}); continue
        if not src.is_file(): errors.append({'file':str(src),'error':'源文件不存在'}); continue
        try: prefix=safe_name(item['description'])
        except ValueError as e: errors.append({'file':str(src),'error':str(e)}); continue
        dst=src.with_name(f'{prefix}__{src.name}')
        if dst==src: errors.append({'file':str(src),'error':'目标与源相同'}); continue
        if dst.exists() or str(dst) in targets: errors.append({'file':str(src),'error':f'目标冲突：{dst}'}); continue
        targets.add(str(dst)); plan.append({'from':str(src),'to':str(dst),'description':item['description'],'status':'planned'})
    result={'root':str(root),'dry_run':not a.apply,'count':len(plan),'errors':errors,'items':plan}
    if errors: result['applied']=False
    elif a.apply:
        # 所有项目先完成冲突检查，再逐项 rename；Path.rename 在这里不覆盖已存在目标。
        for item in plan:
            Path(item['from']).rename(item['to']); item['status']='renamed'
        result['applied']=True
    if a.manifest: a.manifest.parent.mkdir(parents=True,exist_ok=True); a.manifest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())

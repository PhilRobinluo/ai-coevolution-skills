#!/usr/bin/env python3
"""把用户合法取得的 SRT/VTT 字幕转成可引用的时间证据索引。"""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
TIME=re.compile(r'(?:(\d+):)?(\d{2}):(\d{2})[,.](\d{3})')
def sec(s):
 m=TIME.search(s); return None if not m else int(m.group(1) or 0)*3600+int(m.group(2))*60+int(m.group(3))+int(m.group(4))/1000
def fmt(v): return f'{int(v)//3600:02d}:{int(v)%3600//60:02d}:{int(v)%60:02d}'
def parse(text):
 blocks=re.split(r'\n\s*\n',text.replace('\r','')); rows=[]
 for b in blocks:
  lines=[x.strip() for x in b.splitlines() if x.strip() and x.strip()!='WEBVTT'];
  if lines and lines[0].isdigit(): lines=lines[1:]
  if not lines: continue
  idx=next((i for i,x in enumerate(lines) if '-->' in x),None)
  if idx is None: continue
  a,btime=lines[idx].split('-->',1); start=sec(a); end=sec(btime); content=' '.join(lines[idx+1:]); content=re.sub(r'<[^>]+>','',content)
  if start is not None and end is not None and content: rows.append({'start':start,'end':end,'text':content})
 return rows
def main():
 p=argparse.ArgumentParser(); p.add_argument('input',type=Path); p.add_argument('output',type=Path); p.add_argument('--chunk-seconds',type=int,default=120); a=p.parse_args()
 if not a.input.is_file(): raise SystemExit('字幕文件不存在')
 if not 30<=a.chunk_seconds<=900: raise SystemExit('--chunk-seconds 必须在 30 到 900')
 rows=parse(a.input.read_text(errors='replace')); 
 if not rows: raise SystemExit('未解析到带时间字幕')
 chunks=[]; current=[]; start=rows[0]['start']
 for r in rows:
  if current and r['start']-start>=a.chunk_seconds: chunks.append({'start':start,'end':current[-1]['end'],'text':' '.join(x['text'] for x in current)}); current=[]; start=r['start']
  current.append(r)
 if current: chunks.append({'start':start,'end':current[-1]['end'],'text':' '.join(x['text'] for x in current)})
 out={'source':str(a.input),'segments':len(rows),'chunks':[{'start':fmt(x['start']),'end':fmt(x['end']),'text':x['text']} for x in chunks]}
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n'); print(json.dumps({'segments':len(rows),'chunks':len(chunks),'output':str(a.output)},ensure_ascii=False))
if __name__=='__main__':main()

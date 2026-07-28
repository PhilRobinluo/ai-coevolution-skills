#!/usr/bin/env python3
"""按人工确认坐标生成脱敏副本和复核报告；默认使用不可读的纯色遮挡。"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageColor, ImageDraw, ImageFilter


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        x, y, w, h = (int(v.strip()) for v in value.split(','))
    except Exception as e:
        raise argparse.ArgumentTypeError('box 格式必须是 x,y,w,h') from e
    if min(x, y) < 0 or min(w, h) <= 0:
        raise argparse.ArgumentTypeError('坐标非负，宽高必须大于 0')
    return x, y, w, h


def digest(path: Path) -> str:
    h=hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()


def main() -> int:
    p=argparse.ArgumentParser(description='按坐标生成图片脱敏副本')
    p.add_argument('input',type=Path); p.add_argument('output',type=Path)
    p.add_argument('--box',type=parse_box,action='append',required=True,help='可重复：x,y,w,h')
    p.add_argument('--method',choices=('solid','pixelate','blur'),default='solid')
    p.add_argument('--color',default='#111111'); p.add_argument('--padding',type=int,default=8)
    p.add_argument('--report',type=Path); p.add_argument('--force',action='store_true')
    a=p.parse_args()
    if not a.input.is_file(): raise SystemExit(f'输入不存在：{a.input}')
    if a.input.resolve()==a.output.resolve(): raise SystemExit('输出必须是新文件，原图保持不变')
    if not 0 <= a.padding <= 100: raise SystemExit('--padding 必须在 0 到 100 之间')
    if a.output.exists() and not a.force: raise SystemExit('输出已存在；更换路径或显式使用 --force')
    try: color=ImageColor.getrgb(a.color)
    except ValueError as e: raise SystemExit(f'颜色无效：{a.color}') from e
    with Image.open(a.input) as src: image=src.convert('RGB')
    width,height=image.size; applied=[]
    for x,y,w,h in a.box:
        # padding 向四周扩展，降低字符边缘或行高估计不准造成的漏字风险。
        left=max(0,x-a.padding); top=max(0,y-a.padding); right=min(width,x+w+a.padding); bottom=min(height,y+h+a.padding)
        if left>=right or top>=bottom or x+w>width or y+h>height:
            raise SystemExit(f'box 超出图片范围：{x},{y},{w},{h}; image={width}x{height}')
        box=(left,top,right,bottom)
        if a.method=='solid': ImageDraw.Draw(image).rectangle(box,fill=color)
        elif a.method=='blur': image.paste(image.crop(box).filter(ImageFilter.GaussianBlur(radius=18)),box)
        else:
            crop=image.crop(box); tiny=crop.resize((max(1,crop.width//24),max(1,crop.height//24)),Image.Resampling.BILINEAR)
            image.paste(tiny.resize(crop.size,Image.Resampling.NEAREST),box)
        applied.append({'requested':[x,y,w,h],'applied':[left,top,right-left,bottom-top]})
    a.output.parent.mkdir(parents=True,exist_ok=True)
    backup=None
    if a.output.exists():
        backup=a.output.with_name(f'{a.output.name}.bak-{datetime.now().strftime("%Y%m%d-%H%M%S")}'); a.output.rename(backup)
    image.save(a.output)
    report={'input':str(a.input),'input_sha256':digest(a.input),'output':str(a.output),'output_sha256':digest(a.output),'image_pixels':[width,height],'method':a.method,'padding':a.padding,'boxes':applied,'backup':str(backup) if backup else None,'review_required':True,'warning':'发布前必须重新查看整张脱敏图；纯色遮挡最适合账号、密钥和身份信息，模糊/像素化仅用于低风险视觉匿名。'}
    if a.report: a.report.parent.mkdir(parents=True,exist_ok=True); a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
    return 0
if __name__=='__main__': raise SystemExit(main())

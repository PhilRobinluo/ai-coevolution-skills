#!/usr/bin/env python3
import argparse
from pathlib import Path
from PIL import Image,ImageEnhance,ImageFilter
p=argparse.ArgumentParser(); p.add_argument('input'); p.add_argument('output'); a=p.parse_args()
im=Image.open(a.input).convert('RGB'); im=ImageEnhance.Contrast(im).enhance(1.12); im=im.filter(ImageFilter.UnsharpMask(.6,80,2))
w,h=(2480,3508) if im.height>=im.width else (3508,2480); page=Image.new('RGB',(w,h),'white'); scale=min((w-160)/im.width,(h-160)/im.height); im=im.resize((int(im.width*scale),int(im.height*scale)),Image.Resampling.LANCZOS); page.paste(im,((w-im.width)//2,(h-im.height)//2)); Path(a.output).parent.mkdir(parents=True,exist_ok=True); page.save(a.output,resolution=300.0)
print(a.output)

#!/usr/bin/env python3
"""把可辨认的纸质文件照片保守增强并排版成 A4 PDF；不补写缺失内容。"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

A4_PORTRAIT = (2480, 3508)  # 300 DPI


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="保守增强文件照片并制作 A4 PDF")
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--orientation", choices=("auto", "portrait", "landscape"), default="auto")
    p.add_argument("--margin-mm", type=float, default=12.0)
    p.add_argument("--contrast", type=float, default=1.12)
    p.add_argument("--sharpness", type=float, default=1.08)
    p.add_argument("--preview", type=Path, help="另存实际排版预览 PNG")
    p.add_argument("--report", type=Path, help="写入可复核 JSON 报告")
    p.add_argument("--force", action="store_true", help="目标存在时先备份再写入")
    return p.parse_args()


def validate(a: argparse.Namespace) -> None:
    if not a.input.is_file():
        raise SystemExit(f"输入文件不存在：{a.input}")
    if a.output.suffix.lower() != ".pdf":
        raise SystemExit("输出必须是 .pdf")
    if not 0 <= a.margin_mm <= 40:
        raise SystemExit("--margin-mm 必须在 0 到 40 之间")
    if not 0.8 <= a.contrast <= 1.8 or not 0.8 <= a.sharpness <= 2.0:
        raise SystemExit("增强参数超出保守范围")
    if a.output.exists() and not a.force:
        raise SystemExit("输出已存在；更换路径或显式使用 --force")


def backup_existing(path: Path) -> Path | None:
    if not path.exists():
        return None
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = path.with_name(f"{path.name}.bak-{stamp}")
    path.rename(backup)
    return backup


def main() -> int:
    a = parse_args(); validate(a)
    with Image.open(a.input) as raw:
        # EXIF 方向先归一化，避免手机竖拍图在 PDF 中横置。
        image = ImageOps.exif_transpose(raw).convert("RGB")
    original_size = image.size
    image = ImageEnhance.Contrast(image).enhance(a.contrast)
    image = ImageEnhance.Sharpness(image).enhance(a.sharpness)
    image = image.filter(ImageFilter.UnsharpMask(radius=0.6, percent=60, threshold=3))

    if a.orientation == "portrait":
        page_size = A4_PORTRAIT
    elif a.orientation == "landscape":
        page_size = A4_PORTRAIT[::-1]
    else:
        page_size = A4_PORTRAIT if image.height >= image.width else A4_PORTRAIT[::-1]
    margin_px = round(a.margin_mm / 25.4 * 300)
    usable = (page_size[0] - 2 * margin_px, page_size[1] - 2 * margin_px)
    if min(usable) <= 0:
        raise SystemExit("页边距导致可用区域为空")
    scale = min(usable[0] / image.width, usable[1] / image.height)
    resized = image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), Image.Resampling.LANCZOS)
    page = Image.new("RGB", page_size, "white")
    offset = ((page_size[0] - resized.width) // 2, (page_size[1] - resized.height) // 2)
    page.paste(resized, offset)

    a.output.parent.mkdir(parents=True, exist_ok=True)
    backup = backup_existing(a.output) if a.force else None
    temp = a.output.with_name(f".{a.output.name}.writing-{datetime.now().strftime('%H%M%S%f')}")
    page.save(temp, "PDF", resolution=300.0)
    temp.replace(a.output)
    if a.preview:
        a.preview.parent.mkdir(parents=True, exist_ok=True)
        page.save(a.preview, "PNG", dpi=(300, 300))
    report = {
        "input": str(a.input), "input_sha256": sha256(a.input),
        "output": str(a.output), "output_sha256": sha256(a.output),
        "original_pixels": original_size, "page_pixels": page_size,
        "placed_pixels": resized.size, "offset_pixels": offset,
        "settings": {"orientation": a.orientation, "margin_mm": a.margin_mm, "contrast": a.contrast, "sharpness": a.sharpness},
        "backup": str(backup) if backup else None,
        "warning": "仅做可见内容增强与排版；未恢复、猜测或补写缺失文字、数字、签名或印章。",
    }
    if a.report:
        a.report.parent.mkdir(parents=True, exist_ok=True)
        a.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

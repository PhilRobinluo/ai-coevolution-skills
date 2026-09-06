#!/usr/bin/env python3
"""初始化 WorkBuddy 仓颉蒸馏工作区，不复制原始内容。"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="初始化仓颉知识蒸馏工作区")
    parser.add_argument("--source", required=True, help="源文本文件路径")
    parser.add_argument("--output", required=True, help="蒸馏工作区目录")
    parser.add_argument("--title", required=True, help="材料标题")
    parser.add_argument("--creator", required=True, help="作者或讲者")
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"源文本不存在：{source}")
    if output.exists() and any(output.iterdir()):
        # 避免误覆盖正在进行的蒸馏；续跑应直接读取 PIPELINE_STATE.md。
        raise SystemExit(f"输出目录非空，请续跑或选择新目录：{output}")

    for relative in ("candidates", "rejected", "skills"):
        (output / relative).mkdir(parents=True, exist_ok=True)

    manifest = {
        "title": args.title,
        "creator": args.creator,
        "source_path": str(source),
        "source_sha256": sha256(source),
        "source_bytes": source.stat().st_size,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_copied": False,
        "note": "仅记录本地来源和哈希，未把原材料复制进构建产物。",
    }
    (output / "SOURCE_MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    state = """# PIPELINE_STATE

- [x] 阶段 0A：工作区初始化
- [ ] 阶段 0B：全局理解
- [ ] 阶段 1：五视角提取
- [ ] 阶段 2：三重验证与用户确认
- [ ] 阶段 3：制作独立 Skill
- [ ] 阶段 4：关联与压力测试
- [ ] 阶段 5：验证、交付与安装

## 下一步

读取 SOURCE_MANIFEST.json 指向的源文本，生成 CONTENT_OVERVIEW.md。
"""
    (output / "PIPELINE_STATE.md").write_text(state, encoding="utf-8")
    print(f"OK: 已初始化 {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

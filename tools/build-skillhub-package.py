#!/usr/bin/env python3
"""从标准 Agent Skill 源码构建 SkillHub 专用临时发布包。"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import yaml


PLATFORM_KEYS = ("slug", "displayName", "version", "summary", "license")


def split_frontmatter(text: str) -> tuple[str, str]:
    """只解析文件开头的 YAML；正文保持逐字不变，避免渠道构建改变 Skill 行为。"""
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md 缺少开头 frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter 未闭合")
    return text[4:end], text[end + 5 :]


def main() -> int:
    parser = argparse.ArgumentParser(description="构建 SkillHub 临时发布包")
    parser.add_argument("source", type=Path, help="标准公开 Skill 目录")
    parser.add_argument("output", type=Path, help="必须不存在的临时输出目录")
    parser.add_argument("--version", required=True)
    parser.add_argument("--display-name", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--license", default="MIT")
    args = parser.parse_args()

    source_md = args.source / "SKILL.md"
    if not source_md.is_file():
        raise SystemExit(f"缺少 {source_md}")
    if args.output.exists():
        raise SystemExit(f"输出目录已存在，为避免混入旧文件已停止：{args.output}")

    frontmatter_text, body = split_frontmatter(source_md.read_text(encoding="utf-8"))
    original = yaml.safe_load(frontmatter_text)
    if not isinstance(original, dict) or not original.get("name"):
        raise SystemExit("标准源缺少 name")
    slug = str(original["name"])

    # SkillHub 平台字段只存在于临时包；公开源和 WorkBuddy 运行副本不受影响。
    platform = {
        "slug": slug,
        "displayName": args.display_name,
        "version": args.version,
        "summary": args.summary,
        "license": args.license,
    }
    merged = {**platform, **original}

    shutil.copytree(args.source, args.output)
    # SkillHub 拒绝 .upstream 扩展名；仅在临时发布包中改成 Markdown，
    # 保留上游许可证正文，公开源码中的来源文件名保持不变。
    upstream_license = args.output / "LICENSE.upstream"
    if upstream_license.is_file():
        upstream_license.rename(args.output / "LICENSE.md")
    rendered = yaml.safe_dump(merged, allow_unicode=True, sort_keys=False).strip()
    (args.output / "SKILL.md").write_text(
        f"---\n{rendered}\n---\n{body}", encoding="utf-8"
    )
    print(f"built {slug}@{args.version}: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""移除 SkillHub 平台字段，使 WorkBuddy 副本恢复标准 Agent Skill YAML。"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

import yaml


PLATFORM_ONLY_KEYS = {"slug", "displayName", "version", "summary"}
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md 缺少开头 frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter 未闭合")
    return text[4:end], text[end + 5 :]


def main() -> int:
    parser = argparse.ArgumentParser(description="标准化 WorkBuddy Skill frontmatter")
    parser.add_argument("skill_dir", type=Path)
    parser.add_argument("--backup-root", type=Path, required=True)
    parser.add_argument("--apply", action="store_true", help="确认写入；默认只预检")
    args = parser.parse_args()

    skill_md = args.skill_dir / "SKILL.md"
    meta_path = args.skill_dir / "_meta.json"
    frontmatter_text, body = split_frontmatter(skill_md.read_text(encoding="utf-8"))
    data = yaml.safe_load(frontmatter_text)
    if not isinstance(data, dict):
        raise SystemExit("frontmatter 不是对象")

    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    actual_name = str(data.get("name") or "")
    expected_slug = str(meta.get("slug") or data.get("slug") or actual_name)
    platform_slug = str(data.get("slug") or expected_slug)
    if actual_name != expected_slug or platform_slug != expected_slug:
        raise SystemExit(
            f"slug 对账失败：目录={expected_slug}, name={actual_name}, slug={platform_slug}"
        )

    normalized = {key: value for key, value in data.items() if key not in PLATFORM_ONLY_KEYS}
    unexpected = set(normalized) - ALLOWED_KEYS
    if unexpected:
        raise SystemExit(f"标准化后仍有额外字段：{sorted(unexpected)}")
    rendered = yaml.safe_dump(normalized, allow_unicode=True, sort_keys=False).strip()
    output = f"---\n{rendered}\n---\n{body}"

    if not args.apply:
        print(f"dry-run {expected_slug}: remove {sorted(set(data) & PLATFORM_ONLY_KEYS)}")
        return 0

    # 备份放在运行目录之外，避免 WorkBuddy 把备份误识别为 Skill 内容。
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_dir = args.backup_root / expected_slug / stamp
    backup_dir.mkdir(parents=True, exist_ok=False)
    (backup_dir / "SKILL.md").write_text(skill_md.read_text(encoding="utf-8"), encoding="utf-8")
    skill_md.write_text(output, encoding="utf-8")
    print(f"normalized {expected_slug}; backup={backup_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

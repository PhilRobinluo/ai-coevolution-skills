#!/usr/bin/env python3
"""检查仓颉 WorkBuddy 构建产物是否达到最小交付标准。"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED_ROOT = ("SOURCE_MANIFEST.json", "PIPELINE_STATE.md", "CONTENT_OVERVIEW.md", "verified.md")
REQUIRED_SECTIONS = ("## R：", "## I：", "## A1：", "## A2：", "## E：", "## B：")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    result: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="检查仓颉 WorkBuddy 构建产物是否达到最小交付标准"
    )
    parser.add_argument("build_directory", type=Path, help="蒸馏构建目录")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.build_directory.expanduser().resolve()
    errors: list[str] = []
    if not root.is_dir():
        raise SystemExit(f"构建目录不存在：{root}")

    for name in REQUIRED_ROOT:
        if not (root / name).is_file():
            fail(errors, f"缺少根文件：{name}")

    skill_dirs = sorted(path.parent for path in (root / "skills").glob("*/SKILL.md"))
    if not skill_dirs:
        fail(errors, "skills/ 中至少需要一个独立 Skill")

    for skill_dir in skill_dirs:
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        meta = frontmatter(text)
        name = meta.get("name", "")
        description = meta.get("description", "")
        if not SLUG_RE.fullmatch(name):
            fail(errors, f"{skill_dir.name}: name 不是合法 slug")
        if name != skill_dir.name:
            fail(errors, f"{skill_dir.name}: 目录名与 name 不一致")
        if len(description) < 30:
            fail(errors, f"{skill_dir.name}: description 太短，触发边界不清楚")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                fail(errors, f"{skill_dir.name}: 缺少 {section}")
        tests_path = skill_dir / "test-prompts.json"
        if not tests_path.is_file():
            fail(errors, f"{skill_dir.name}: 缺少 test-prompts.json")
            continue
        try:
            data = json.loads(tests_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(errors, f"{skill_dir.name}: test-prompts.json 解析失败：{exc}")
            continue
        cases = data.get("cases", [])
        counts = {kind: sum(case.get("type") == kind for case in cases) for kind in (
            "should_trigger", "should_not_trigger", "edge_case"
        )}
        if counts["should_trigger"] < 3:
            fail(errors, f"{skill_dir.name}: should_trigger 少于 3 条")
        if counts["should_not_trigger"] < 2:
            fail(errors, f"{skill_dir.name}: should_not_trigger 少于 2 条")
        if counts["edge_case"] < 1:
            fail(errors, f"{skill_dir.name}: edge_case 少于 1 条")

    # 这是 WorkBuddy 适配的负面检查：构建产物中不应残留专属安装路径。
    for path in root.rglob("*"):
        if path.is_file() and path.stat().st_size < 2_000_000:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if ".claude/skills" in text or ".cursor/skills" in text:
                fail(errors, f"{path.relative_to(root)}: 残留 Claude/Cursor 安装路径")

    if errors:
        print("FAIL:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: {len(skill_dirs)} 个 Skill 通过 WorkBuddy 蒸馏产物检查")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

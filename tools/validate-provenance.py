#!/usr/bin/env python3
"""校验公开 Skill 的来源类型，防止原创、改编和推荐条目混在一起。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise ValueError(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path}: JSON 读取失败: {exc}")


def require_text(item: dict, key: str, context: str) -> str:
    value = item.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{context}: 缺少非空字段 {key}")
    return value.strip()


def validate(root: Path) -> None:
    registry = load_json(root / "registry.json")
    skills = registry.get("skills")
    if not isinstance(skills, list):
        fail("registry.json: skills 必须是数组")

    seen: set[str] = set()
    registered_paths: dict[str, str] = {}
    for item in skills:
        if not isinstance(item, dict):
            fail("registry.json: 每个 skill 必须是对象")
        name = require_text(item, "name", "registry skill")
        if name in seen:
            fail(f"registry.json: 重复 skill: {name}")
        seen.add(name)

        provenance = require_text(item, "provenance", name)
        path = require_text(item, "path", name)
        if provenance == "lls-original":
            if not path.startswith("skills/"):
                fail(f"{name}: LLS Original 必须放在 skills/")
        elif provenance == "lls-adapted":
            if not path.startswith("adapted/"):
                fail(f"{name}: LLS Adapted 必须放在 adapted/")
            origin = item.get("origin")
            if not isinstance(origin, dict):
                fail(f"{name}: LLS Adapted 缺少 origin 对象")
            for key in ("author", "source_url", "license", "changes", "adapted_version"):
                require_text(origin, key, f"{name}.origin")
            if not origin["source_url"].startswith("https://"):
                fail(f"{name}: origin.source_url 必须是 HTTPS 地址")
        else:
            fail(f"{name}: 未知 provenance: {provenance}")

        if not (root / path / "SKILL.md").is_file():
            fail(f"{name}: 找不到 {path}/SKILL.md")
        registered_paths[path] = provenance

    # 目录和台账双向核对：新增文件夹却忘记登记来源时，校验会直接失败。
    for folder, expected in (("skills", "lls-original"), ("adapted", "lls-adapted")):
        base = root / folder
        for child in base.iterdir():
            if not child.is_dir():
                continue
            relative = child.relative_to(root).as_posix()
            if registered_paths.get(relative) != expected:
                fail(f"{relative}: 未以 {expected} 登记到 registry.json")
            if expected == "lls-adapted" and not (child / "ORIGIN.md").is_file():
                fail(f"{relative}: 改编目录缺少 ORIGIN.md")

    catalog = load_json(root / "community" / "catalog.json")
    items = catalog.get("items")
    if not isinstance(items, list):
        fail("community/catalog.json: items 必须是数组")
    for item in items:
        if not isinstance(item, dict):
            fail("community catalog: 每个条目必须是对象")
        name = require_text(item, "name", "community item")
        for key in (
            "category",
            "author",
            "source_url",
            "license",
            "verified_version",
            "verified_at",
            "recommendation",
            "distribution",
        ):
            require_text(item, key, name)
        if not item["source_url"].startswith("https://"):
            fail(f"{name}: source_url 必须是 HTTPS 地址")
        if item["distribution"] != "link-only":
            fail(f"{name}: Community Pick 默认必须使用 link-only")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        validate(args.root.resolve())
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("OK: provenance policy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

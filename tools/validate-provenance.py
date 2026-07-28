#!/usr/bin/env python3
"""校验公开 Skill 的来源与许可证分流，避免原创、改编和第三方条款混用。"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ORIGINAL_CONTENT_LICENSE = "CC-BY-NC-SA-4.0"
CODE_LICENSE = "PolyForm-Noncommercial-1.0.0"
REQUIRED_ROOT_FILES = {
    "LICENSE": "许可证分流说明",
    "LICENSES/CC-BY-NC-SA-4.0.txt": "Attribution-NonCommercial-ShareAlike 4.0 International",
    "LICENSES/PolyForm-Noncommercial-1.0.0.txt": "PolyForm Noncommercial License 1.0.0",
    "ADDITIONAL-PERMISSIONS.md": "企业内部普通办公",
    "COMMERCIAL-LICENSE.md": "Commercial License",
    "THIRD_PARTY_NOTICES.md": "Third-Party Notices",
}


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


def frontmatter(path: Path) -> dict[str, str]:
    """读取顶层简单字段；许可证字段必须是一行纯文本，避免 YAML 依赖。"""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"{path}: 读取失败: {exc}")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        fail(f"{path}: 缺少 YAML frontmatter")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(\S.*?)\s*$", line)
        if field:
            values[field.group(1)] = field.group(2).strip().strip('"\'')
    return values


def has_material_scripts(skill_dir: Path) -> bool:
    scripts = skill_dir / "scripts"
    return scripts.is_dir() and any(path.is_file() for path in scripts.rglob("*"))


def validate_root_licenses(root: Path) -> None:
    # 双库隔离优先于发布便利：符号链接可能把私有目录悄悄带入公开构建。
    links = sorted(path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_symlink())
    if links:
        fail(f"公开仓库包含符号链接，违反隔离规则: {', '.join(links)}")
    for relative, marker in REQUIRED_ROOT_FILES.items():
        path = root / relative
        if not path.is_file():
            fail(f"缺少许可证治理文件: {relative}")
        if marker not in path.read_text(encoding="utf-8"):
            fail(f"{relative}: 未找到预期许可证标识")
    routing = (root / "LICENSE").read_text(encoding="utf-8")
    for marker in ("skills/**/scripts/**", "tools/**", ORIGINAL_CONTENT_LICENSE, CODE_LICENSE):
        if marker not in routing:
            fail(f"LICENSE: 缺少许可证分流标识 {marker}")


def validate(root: Path) -> None:
    validate_root_licenses(root)
    registry = load_json(root / "registry.json")
    skills = registry.get("skills")
    if not isinstance(skills, list):
        fail("registry.json: skills 必须是数组")

    seen: set[str] = set()
    registered_paths: dict[str, tuple[str, dict]] = {}
    for item in skills:
        if not isinstance(item, dict):
            fail("registry.json: 每个 skill 必须是对象")
        name = require_text(item, "name", "registry skill")
        if name in seen:
            fail(f"registry.json: 重复 skill: {name}")
        seen.add(name)

        provenance = require_text(item, "provenance", name)
        path = require_text(item, "path", name)
        registry_license = require_text(item, "license", name)
        if provenance == "lls-original":
            if not path.startswith("skills/"):
                fail(f"{name}: LLS Original 必须放在 skills/")
            if registry_license != ORIGINAL_CONTENT_LICENSE:
                fail(f"{name}: 原创内容 license 必须是 {ORIGINAL_CONTENT_LICENSE}")
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
            if registry_license != origin["license"].strip():
                fail(f"{name}: license 必须与 origin.license 一致")
        else:
            fail(f"{name}: 未知 provenance: {provenance}")

        skill_dir = root / path
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            fail(f"{name}: 找不到 {path}/SKILL.md")
        metadata = frontmatter(skill_file)
        skill_license = metadata.get("license", "")
        if not skill_license:
            fail(f"{path}/SKILL.md: 缺少 license frontmatter")
        if skill_license != registry_license:
            fail(f"{name}: SKILL.md license 必须与 registry.json 一致")
        if provenance == "lls-original" and skill_license != ORIGINAL_CONTENT_LICENSE:
            fail(f"{name}: 原创 SKILL.md 必须使用 {ORIGINAL_CONTENT_LICENSE}")
        if "code_license" in metadata:
            fail(f"{name}: code_license 不写入 SKILL.md 顶层，改由 registry 与 LICENSE 文件声明")
        if has_material_scripts(skill_dir):
            if item.get("code_license") != CODE_LICENSE:
                fail(f"{name}: registry.json 含 scripts/ 时 code_license 必须是 {CODE_LICENSE}")
        elif item.get("code_license"):
            fail(f"{name}: 不含实质 scripts/ 时 registry 不应声明 code_license")
        registered_paths[path] = (provenance, item)

    # 目录和台账双向核对：新增文件夹却忘记登记来源或许可证时，校验会直接失败。
    for folder, expected in (("skills", "lls-original"), ("adapted", "lls-adapted")):
        base = root / folder
        for child in base.iterdir():
            if not child.is_dir():
                continue
            relative = child.relative_to(root).as_posix()
            registration = registered_paths.get(relative)
            if not registration or registration[0] != expected:
                fail(f"{relative}: 未以 {expected} 登记到 registry.json")
            if expected == "lls-adapted" and not (child / "ORIGIN.md").is_file():
                fail(f"{relative}: 改编目录缺少 ORIGIN.md")
            if expected == "lls-adapted" and not (child / "LICENSE.upstream").is_file():
                fail(f"{relative}: 改编目录缺少 LICENSE.upstream")

    catalog = load_json(root / "community" / "catalog.json")
    items = catalog.get("items")
    if not isinstance(items, list):
        fail("community/catalog.json: items 必须是数组")
    for item in items:
        if not isinstance(item, dict):
            fail("community catalog: 每个条目必须是对象")
        name = require_text(item, "name", "community item")
        for key in (
            "category", "author", "source_url", "license", "verified_version", "verified_at",
            "recommendation", "distribution",
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
    print("OK: provenance and license policy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

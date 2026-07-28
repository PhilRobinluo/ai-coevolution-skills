#!/usr/bin/env python3
"""把公开仓库的许可与 WorkBuddy 入口规则应用到 registry 中的每个 Skill。"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_LICENSE = "CC-BY-NC-SA-4.0"
CODE_LICENSE = "PolyForm-Noncommercial-1.0.0"


def replace_field(frontmatter: str, key: str, value: str | None) -> str:
    pattern = rf"(?m)^{re.escape(key)}:.*\n?"
    if value is None:
        return re.sub(pattern, "", frontmatter)
    line = f"{key}: {value}"
    if re.search(pattern, frontmatter):
        return re.sub(pattern, line + "\n", frontmatter, count=1).rstrip("\n")
    anchor = re.search(r"(?m)^version:.*$", frontmatter) or re.search(r"(?m)^name:.*$", frontmatter)
    if not anchor:
        raise ValueError(f"frontmatter 缺少 name/version，无法写入 {key}")
    return frontmatter[: anchor.end()] + f"\n{line}" + frontmatter[anchor.end() :]


def update_skill(path: Path, entry: dict) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"{path}: frontmatter 不完整")
    frontmatter = match.group(1)
    provenance = entry["provenance"]
    license_name = (
        CONTENT_LICENSE
        if provenance == "lls-original"
        else entry["origin"]["license"]
    )
    frontmatter = replace_field(frontmatter, "version", entry["version"])
    frontmatter = replace_field(frontmatter, "license", license_name)
    # Codex 官方 Skill schema 不接收 code_license 顶层字段；代码许可由
    # registry.json、LICENSE.md 与 LICENSES/ 中的 PolyForm 正文共同声明。
    frontmatter = replace_field(frontmatter, "code_license", None)
    body = text[match.end() :]
    body = re.sub(
        r"(?m)^(>\s*当前版本[：:]\s*)`?\d+\.\d+\.\d+`?\s*$",
        rf"\g<1>{entry['version']}",
        body,
        count=1,
    )
    marker = f"<!-- workbuddy-install: {entry['skillhub_status']}; slug: {entry['name']} -->"
    if marker not in body:
        slug = entry["name"]
        guide = f"""
{marker}
## 在 WorkBuddy 中找到并安装

**Skill slug：`{slug}`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `{slug}`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/{slug}/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `{slug}` 后安装；界面文字可能随 WorkBuddy 版本变化。

"""
        body = guide.lstrip() + body
    return f"---\n{frontmatter}\n---\n\n{body.lstrip()}"


def update_readme(path: Path, entry: dict) -> str:
    text = path.read_text(encoding="utf-8")
    slug = entry["name"]
    version_line = (
        f"- **当前源码版本：`{entry['version']}`**"
        f"（最近 Release：`{entry['release_version']}`）"
    )
    old_version = re.compile(
        r"(?m)^-\s*(?:\*\*)?(?:当前仓库版本|当前源码版本|版本)[：:].*$"
    )
    if old_version.search(text):
        text = old_version.sub(version_line, text, count=1)
    else:
        heading = re.search(r"(?m)^# .+$", text)
        if not heading:
            raise ValueError(f"{path}: README 缺少一级标题")
        text = text[: heading.end()] + f"\n\n{version_line}" + text[heading.end() :]
    status_text = {
        "published": "已发布",
        "pending_review": "审核中",
        "pending": "待核验",
    }[entry["skillhub_status"]]
    text = re.sub(
        r"(?m)^-[ \t]*\*\*SkillHub 状态：.*\*\*[ \t]*\n(?:[ \t]*\n)?",
        f"- **SkillHub 状态：{status_text}**\n\n",
        text,
        count=1,
    )
    if f"**Skill slug：`{slug}`**" not in text:
        text = text.rstrip() + f"""

## 在 WorkBuddy 安装

- **Skill slug：`{slug}`**
- **SkillHub 状态：{status_text}**

把下面内容粘贴到 WorkBuddy 新会话：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `{slug}`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/{slug}/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `{slug}` 后安装；界面文字可能随 WorkBuddy 版本变化。
"""
    if "## 许可证与商业使用" not in text:
        if entry["provenance"] == "lls-original":
            code = ""
            if entry.get("code_license") == CODE_LICENSE:
                code = "本目录的 `scripts/` 采用 [PolyForm Noncommercial 1.0.0](../../LICENSES/PolyForm-Noncommercial-1.0.0.txt)。"
            license_text = (
                "本 Skill 的原创内容采用 [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt)。"
                f"{code}企业内部普通办公可按[额外许可](../../ADDITIONAL-PERMISSIONS.md)免费使用；"
                "收费课程、转售、客户交付、SaaS、代运营等须取得[商业授权](../../COMMERCIAL-LICENSE.md)。"
            )
        else:
            license_text = (
                f"本改编 Skill 保持上游 `{entry['license']}` 许可；来源与修改见 [ORIGIN.md](ORIGIN.md)。"
                "仓库默认许可不覆盖上游权利。"
            )
        text = text.rstrip() + f"\n\n## 许可证与商业使用\n\n{license_text}\n"
    return text


def update_install_catalog(path: Path, entries: list[dict]) -> str:
    text = path.read_text(encoding="utf-8")
    rows = [
        "## 当前公开 Skill 与 SkillHub 状态",
        "",
        "| Skill slug | 当前源码 / Release | SkillHub 状态 |",
        "| --- | --- | --- |",
    ]
    for entry in entries:
        status = {
            "published": "已检索到",
            "pending_review": "审核中",
            "pending": "本仓版本未确认已上架",
        }[entry["skillhub_status"]]
        rows.append(
            f"| [`{entry['name']}`](../{entry['path']}/README.md) "
            f"| `{entry['version']}` / `{entry['release_version']}` | {status} |"
        )
    rows.extend(
        [
            "",
            "“已检索到”只表示 SkillHub 有精确 slug；安装后仍要读回 `SKILL.md` 的 name、version 和路径。",
            "",
            "",
        ]
    )
    block = "\n".join(rows)
    pattern = re.compile(
        r"(?ms)^## 当前公开 Skill 与 SkillHub 状态\n.*?(?=^## 手动安装)"
    )
    if not pattern.search(text):
        raise ValueError(f"{path}: 找不到 SkillHub 状态章节")
    return pattern.sub(block, text, count=1)


def update_root_readme(path: Path, entries: list[dict]) -> str:
    text = path.read_text(encoding="utf-8")
    originals = sum(entry["provenance"] == "lls-original" for entry in entries)
    adapted = sum(entry["provenance"] == "lls-adapted" for entry in entries)
    text = re.sub(
        r"skills-\d+-blue",
        f"skills-{len(entries)}-blue",
        text,
        count=1,
    )
    text = re.sub(
        r"- \[浏览 \d+ 个原创 Skill\]\(skills/\)；另有 \[\d+ 个透明改编 Skill\]\(adapted/\)",
        f"- [浏览 {originals} 个原创 Skill](skills/)；另有 [{adapted} 个透明改编 Skill](adapted/)",
        text,
        count=1,
    )
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    registry_path = ROOT / "registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    changes: list[str] = []
    for entry in registry["skills"]:
        folder = ROOT / entry["path"]
        for path, expected in (
            (folder / "SKILL.md", update_skill(folder / "SKILL.md", entry)),
            (folder / "README.md", update_readme(folder / "README.md", entry)),
        ):
            current = path.read_text(encoding="utf-8")
            if current == expected:
                continue
            changes.append(path.relative_to(ROOT).as_posix())
            if args.apply:
                path.write_text(expected, encoding="utf-8")
    install_doc = ROOT / "docs" / "how-to-install.md"
    expected_install_doc = update_install_catalog(install_doc, registry["skills"])
    if install_doc.read_text(encoding="utf-8") != expected_install_doc:
        changes.append(install_doc.relative_to(ROOT).as_posix())
        if args.apply:
            install_doc.write_text(expected_install_doc, encoding="utf-8")
    root_readme = ROOT / "README.md"
    expected_root_readme = update_root_readme(root_readme, registry["skills"])
    if root_readme.read_text(encoding="utf-8") != expected_root_readme:
        changes.append(root_readme.relative_to(ROOT).as_posix())
        if args.apply:
            root_readme.write_text(expected_root_readme, encoding="utf-8")
    if changes and not args.apply:
        for path in changes:
            print(f"MISSING_OR_STALE: {path}")
        print(f"ERROR: {len(changes)} 个文件未满足仓库规则")
        return 1
    print(f"OK: entries={len(registry['skills'])} changed={len(changes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

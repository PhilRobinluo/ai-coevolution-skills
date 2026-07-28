# Bilingual Reader Maker

Turn English PDFs or long articles into polished bilingual study readers.

The default reading experience is mobile-friendly:

```text
English paragraph
Chinese translation

English paragraph
Chinese translation
```

This avoids hard-to-read side-by-side columns on phones while keeping the material useful for language learning, quoting, parsing, and annotation.

## What It Produces

- HTML: real text, editable, searchable, parseable
- PDF: exported from HTML for sharing
- Optional source-style cover/chapter pages
- Optional subtle final attribution/colophon

## 在 WorkBuddy 安装

- **Skill slug：`bilingual-reader-maker`**
- **SkillHub 状态：本仓当前版本未确认已上架 SkillHub。**

### 路径一：在 WorkBuddy 对话中粘贴

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub CLI。
搜索 Skill `bilingual-reader-maker`；只有搜索结果的 slug 与 `bilingual-reader-maker` 完全一致时，才安装到 `~/.workbuddy/skills/`。
安装后读取 `~/.workbuddy/skills/bilingual-reader-maker/SKILL.md`，核对 name 和 version（如有），确认实际安装路径；然后新开或重启 WorkBuddy 会话。
若没有完全一致的 slug，请报告未找到，不要安装同名但不同 slug 的条目。
```

若搜索不到完全一致的 slug，请不要安装同名条目；请按仓库的手动安装说明复制此目录。后续发布 Release 时，也可从 Release 安装包安装。

### 路径二：用左侧「技能」界面

在 WorkBuddy 左侧打开 **「技能」** → **「添加技能」或「查找技能」** → 搜索 `bilingual-reader-maker` → 核对 slug 完全一致后安装。不同 WorkBuddy 版本的界面名称可能略有变化。安装后确认文件在 `~/.workbuddy/skills/bilingual-reader-maker/SKILL.md`，再新开或重启 WorkBuddy 会话。

## Install

Copy this folder into your skills directory:

```bash
cp -R skills/bilingual-reader-maker ~/.codex/skills/
```

or:

```bash
cp -R skills/bilingual-reader-maker ~/.claude/skills/
```

## Example Prompt

```text
Please turn this English PDF into a Chinese-English bilingual mobile reading edition.
Keep the original cover style, but make the body single-column for phone reading.
Export both HTML and PDF.
```


## 许可证与商业使用

本 Skill 的原创内容采用 [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt)。本目录的 `scripts/` 采用 [PolyForm Noncommercial 1.0.0](../../LICENSES/PolyForm-Noncommercial-1.0.0.txt)。企业内部普通办公可按[额外许可](../../ADDITIONAL-PERMISSIONS.md)免费使用；收费课程、转售、客户交付、SaaS、代运营等须取得[商业授权](../../COMMERCIAL-LICENSE.md)。历史 MIT 版本已授予的权利继续有效。

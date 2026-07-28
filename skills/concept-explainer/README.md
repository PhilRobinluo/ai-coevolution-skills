# Concept Explainer

Explain unfamiliar tools, commands, files, configs, architecture layers, and troubleshooting chains while still doing the user's task.

This skill turns important concepts into short knowledge cards:

```text
In one sentence
In this task
Remember this
Common mistake
Next time
```

It is useful when a user is working through a real task but lacks the mental model for parts of the workflow. For example:

- CLI, npm, package.json, environment variables, and access credentials
- APIs, databases, services, ports, logs, and error messages
- AI review, backend settlement, smart contracts, and responsibility boundaries
- Build, test, deployment, and local development commands

## 在 WorkBuddy 安装

- **Skill slug：`concept-explainer`**
- **SkillHub 状态：本仓当前版本未确认已上架 SkillHub。**

### 路径一：在 WorkBuddy 对话中粘贴

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub CLI。
搜索 Skill `concept-explainer`；只有搜索结果的 slug 与 `concept-explainer` 完全一致时，才安装到 `~/.workbuddy/skills/`。
安装后读取 `~/.workbuddy/skills/concept-explainer/SKILL.md`，核对 name 和 version（如有），确认实际安装路径；然后新开或重启 WorkBuddy 会话。
若没有完全一致的 slug，请报告未找到，不要安装同名但不同 slug 的条目。
```

若搜索不到完全一致的 slug，请不要安装同名条目；请按仓库的手动安装说明复制此目录。后续发布 Release 时，也可从 Release 安装包安装。

### 路径二：用左侧「技能」界面

在 WorkBuddy 左侧打开 **「技能」** → **「添加技能」或「查找技能」** → 搜索 `concept-explainer` → 核对 slug 完全一致后安装。不同 WorkBuddy 版本的界面名称可能略有变化。安装后确认文件在 `~/.workbuddy/skills/concept-explainer/SKILL.md`，再新开或重启 WorkBuddy 会话。

## Install

Copy this folder into your skills directory:

```bash
cp -R skills/concept-explainer ~/.codex/skills/
```

or:

```bash
cp -R skills/concept-explainer ~/.claude/skills/
```

## Example Prompt

```text
Help me use this CLI. I do not understand npm, package.json, access credentials, or where commands should be run. Explain the key parts as knowledge cards while you help me proceed.
```

## What Good Output Looks Like

The assistant should not stop at:

```text
Run npm install, then npm run dev.
```

It should also explain:

```text
Knowledge Card: npm
In one sentence: npm is the JavaScript project's toolbox.
In this task: it installs the tools this CLI needs and runs shortcuts from package.json.
Remember this: npm run xxx means "run the shortcut named xxx from package.json."
```

## 许可证与商业使用

本 Skill 的原创内容采用 [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt)。企业内部普通办公可按[额外许可](../../ADDITIONAL-PERMISSIONS.md)免费使用；收费课程、转售、客户交付、SaaS、代运营等须取得[商业授权](../../COMMERCIAL-LICENSE.md)。历史 MIT 版本已授予的权利继续有效。

# 安装公开 Skill

每个 Skill 的 README 都提供对应的 WorkBuddy slug 和两条安装路径。安装前先决定：优先从 SkillHub 精确搜索，还是从本仓库手动复制。**不要因为名称相似就安装别的 Skill。**

## WorkBuddy：推荐路径一（对话粘贴）

在 WorkBuddy 新开一个对话，粘贴并把 `<slug>` 替换成目标 Skill 的 slug：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub CLI。
搜索 Skill `<slug>`；只有搜索结果的 slug 与 `<slug>` 完全一致时，才安装到 `~/.workbuddy/skills/`。
安装后读取 `~/.workbuddy/skills/<slug>/SKILL.md`，核对 name 和 version（如有），确认实际安装路径；然后新开或重启 WorkBuddy 会话。
若没有完全一致的 slug，请报告未找到，不要安装同名但不同 slug 的条目。
```

SkillHub 安装说明要求通过 `--dir` 指向 Agent 的 skills 目录；WorkBuddy 的目录是 `~/.workbuddy/skills/`。如果 CLI 尚未安装，按该安装说明的步骤安装后再搜索。

## WorkBuddy：路径二（左侧「技能」）

1. 在 WorkBuddy 左侧打开 **「技能」**。
2. 选择 **「添加技能」** 或 **「查找技能」**。
3. 搜索 README 中列出的精确 slug。
4. 核对搜索结果的 slug 完全一致后安装。
5. 检查 `~/.workbuddy/skills/<slug>/SKILL.md` 是否存在，必要时读取其中的 `version`，再新开或重启 WorkBuddy 会话。

不同 WorkBuddy 版本的菜单名称可能略有变化，但都应遵循“搜索精确 slug → 安装到 WorkBuddy skills 目录 → 读回文件验证”的顺序。

## 当前公开 Skill 与 SkillHub 状态

| Skill slug | SkillHub 状态 | 找不到精确 slug 时 |
| --- | --- | --- |
| `bilingual-reader-maker` | 本仓版本未确认已上架 | 手动复制仓库目录；后续可使用 Release 包 |
| `concept-explainer` | 本仓版本未确认已上架；同名条目不代表本 Skill | 手动复制仓库目录；后续可使用 Release 包 |
| `lls-learning-guide` | 已检索到 | 使用 README 的 GitHub Release |
| `lls-ppt-briefing-coach` | 已检索到 | 使用 README 的 GitHub Release |
| `lls-skill-lifecycle-manager` | 已检索到 | 使用 README 的 GitHub Release |
| `lls-workbuddy-guide` | 已检索到 | 使用 README 的 GitHub Release |

“已检索到”仅表示 SkillHub 有该 slug；安装后仍要读回 `SKILL.md` 的 name/version，以确认平台版本是否已同步到本仓版本。

## 手动安装（公开仓库）

先克隆仓库：

```bash
git clone https://github.com/PhilRobinluo/ai-coevolution-skills.git
cd ai-evolution-skills
```

复制目标目录；下面以 `bilingual-reader-maker` 为例：

```bash
mkdir -p ~/.workbuddy/skills
cp -R skills/bilingual-reader-maker ~/.workbuddy/skills/
```

其他兼容客户端：

```bash
# Codex
mkdir -p ~/.codex/skills
cp -R skills/bilingual-reader-maker ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -R skills/bilingual-reader-maker ~/.claude/skills/
```

安装后新开会话，让客户端重新加载 Skill 列表。

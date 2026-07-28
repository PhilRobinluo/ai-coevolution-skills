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

| Skill slug | 当前源码 / Release | SkillHub 状态 |
| --- | --- | --- |
| [`lls-code-anatomy`](../skills/lls-code-anatomy/README.md) | `1.0.2` / `1.0.2` | 已检索到 |
| [`bilingual-reader-maker`](../skills/bilingual-reader-maker/README.md) | `1.1.0` / `1.1.0` | 本仓版本未确认已上架 |
| [`concept-explainer`](../skills/concept-explainer/README.md) | `1.1.0` / `1.1.0` | 本仓版本未确认已上架 |
| [`lls-workbuddy-guide`](../skills/lls-workbuddy-guide/README.md) | `2.1.0` / `2.0.0` | 已检索到 |
| [`lls-ppt-briefing-coach`](../skills/lls-ppt-briefing-coach/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-learning-guide`](../skills/lls-learning-guide/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-skill-lifecycle-manager`](../skills/lls-skill-lifecycle-manager/README.md) | `3.0.0` / `2.0.1` | 已检索到 |
| [`lls-dialogue-subtext-reader`](../skills/lls-dialogue-subtext-reader/README.md) | `1.2.0` / `1.1.1` | 已检索到 |
| [`lls-local-excel-vba-data-processor`](../skills/lls-local-excel-vba-data-processor/README.md) | `1.2.0` / `1.1.1` | 已检索到 |
| [`lls-article-screenshot`](../skills/lls-article-screenshot/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-best-minds-consultation`](../adapted/lls-best-minds-consultation/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-best-practices-researcher`](../skills/lls-best-practices-researcher/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-chinese-humor`](../skills/lls-chinese-humor/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-document-print-restorer`](../skills/lls-document-print-restorer/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-github-profile-writer`](../skills/lls-github-profile-writer/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-headline-summary-maker`](../skills/lls-headline-summary-maker/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-human-writing-editor`](../skills/lls-human-writing-editor/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-image-privacy-redactor`](../skills/lls-image-privacy-redactor/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-image-renamer`](../skills/lls-image-renamer/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-international-techdoc-writer`](../skills/lls-international-techdoc-writer/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-mermaid-validator`](../skills/lls-mermaid-validator/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-mirror-debate`](../skills/lls-mirror-debate/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-naming-coach`](../skills/lls-naming-coach/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-short-video-breakdown`](../skills/lls-short-video-breakdown/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-skill-builder`](../skills/lls-skill-builder/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-skill-security-auditor`](../skills/lls-skill-security-auditor/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-video-digester`](../skills/lls-video-digester/README.md) | `1.1.0` / `1.0.0` | 已检索到 |
| [`lls-ip-positioning-coach`](../skills/lls-ip-positioning-coach/README.md) | `1.2.0` / `1.1.1` | 已检索到 |
| [`lls-mermaid-diagram`](../skills/lls-mermaid-diagram/README.md) | `1.2.0` / `1.1.0` | 已检索到 |
| [`lls-ppt-workflow-builder`](../skills/lls-ppt-workflow-builder/README.md) | `1.2.0` / `1.1.0` | 已检索到 |
| [`lls-prompt-basics-coach`](../skills/lls-prompt-basics-coach/README.md) | `1.2.0` / `1.1.0` | 已检索到 |
| [`lls-douyin-oral-script-writer`](../skills/lls-douyin-oral-script-writer/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-ai-video-script-planner`](../skills/lls-ai-video-script-planner/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-ai-drawing-prompt-coach`](../skills/lls-ai-drawing-prompt-coach/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-ai-poster-design-coach`](../skills/lls-ai-poster-design-coach/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-jimeng-image-editing-coach`](../skills/lls-jimeng-image-editing-coach/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-ai-data-analysis-starter`](../skills/lls-ai-data-analysis-starter/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-government-publicity-data-analyst`](../skills/lls-government-publicity-data-analyst/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-geo-brand-visibility-coach`](../skills/lls-geo-brand-visibility-coach/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-aida-marketing-copywriter`](../skills/lls-aida-marketing-copywriter/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-leader-speechwriter-expert`](../skills/lls-leader-speechwriter-expert/README.md) | `1.1.1` / `1.1.1` | 已检索到 |
| [`lls-slide-storyline-planner`](../skills/lls-slide-storyline-planner/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-ai-microdrama-planner`](../skills/lls-ai-microdrama-planner/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-ai-novel-prompt-engineer`](../skills/lls-ai-novel-prompt-engineer/README.md) | `1.1.0` / `1.1.0` | 已检索到 |
| [`lls-education-illustration-maker`](../skills/lls-education-illustration-maker/README.md) | `1.1.0` / `1.1.0` | 已检索到 |

“已检索到”只表示 SkillHub 有精确 slug；安装后仍要读回 `SKILL.md` 的 name、version 和路径。

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

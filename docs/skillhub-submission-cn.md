# 腾讯 SkillHub / OpenClaw 投稿文案

这份文案用于把 `ai-coevolution-skills` 投稿到腾讯 SkillHub、OpenClaw/ClawHub、Claude/Agent Skills 目录或中文 AI 工具导航。

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 名称 | AI 协同进化能力包 |
| 英文名 | AI Co-Evolution Skills |
| 仓库 | https://github.com/PhilRobinluo/ai-coevolution-skills |
| 类型 | Agent Skill / SKILL.md 能力包 |
| 分类 | 学习成长 / 知识管理 / AI Agent 工作流 / 开发工具 |
| 适配 | Codex、Claude Code、OpenClaw、SkillHub，以及兼容 `SKILL.md` 的 Agent Skills 平台 |
| 当前能力包 | bilingual-reader-maker、concept-explainer |

## 一句话介绍

让 AI 不只是回答和执行，而是在真实任务中判断用户懂不懂，自动生成可复习的知识卡片，帮助人与 AI 协同进化。

## 简短介绍

AI 协同进化能力包是一组可复用的 Agent Skills，面向学习型 AI 工作流、知识管理和真实任务协作。它把人与 AI 一起做事时跑通的方法沉淀成 `SKILL.md` 能力包，让 AI 在执行任务时保留清晰的输入、输出、边界和解释方式。

当前重点能力 `concept-explainer` 可以在用户使用 CLI、npm、package.json、环境变量、API、智能合约、部署、排障等复杂工具链时，自动判断用户知识水平，并生成短、准、好记的知识卡片。它避免 AI 一味输出命令，也避免重复解释用户已经掌握的概念。

## 适合谁

- 使用 AI Agent 但经常看不懂工具链的人；
- 想让 AI 边做事边教学的学习者；
- 做知识管理、Obsidian、LLM Wiki、PKM 的用户；
- 需要把 AI 工作流沉淀成可复用 Skill 的开发者；
- 使用 Codex、Claude Code、OpenClaw、SkillHub 的 Agent 用户。

## 核心亮点

1. **边做事边学习**  
   AI 不只是完成任务，还会把任务里的关键概念讲成知识卡片。

2. **知识水平判定**  
   通过 `已掌握 / 会用但不懂原理 / 完全陌生 / 反复没懂 / 高风险必懂` 来决定是否解释。

3. **减少重复解释**  
   支持配合本地知识卡片库，记录概念是否讲过、解释次数和用户掌握状态。

4. **通俗易记**  
   每张卡片包含一句话解释、在当前任务里的位置、要记住的点、常见误区和下次判断方法。

5. **开放格式**  
   基于 `SKILL.md`，适合 Codex、Claude Code、OpenClaw、SkillHub 等 Agent Skills 生态。

## 推荐展示文案

```text
AI 协同进化能力包：让 AI 在做事时判断你哪里不懂，并自动生成可复习的知识卡片。

它不是普通 prompt 集，而是一组 SKILL.md 能力包。比如 concept-explainer 会在你使用 CLI、npm、package.json、环境变量、智能合约等工具链时，先判断你是否已经掌握，再决定跳过、短复习、完整解释或换一种讲法。

适合 AI Agent 用户、知识管理用户、AI 编程学习者，以及希望把 AI 工作流沉淀成可复用 Skill 的人。
```

## 安装说明

如果平台支持 GitHub 导入：

```text
https://github.com/PhilRobinluo/ai-coevolution-skills
```

如果手动安装到 Codex：

```bash
mkdir -p ~/.codex/skills
cp -R skills/concept-explainer ~/.codex/skills/
```

如果手动安装到 Claude Code：

```bash
mkdir -p ~/.claude/skills
cp -R skills/concept-explainer ~/.claude/skills/
```

OpenClaw / SkillHub 用户可将 `skills/concept-explainer/` 放入对应 skills 目录，或使用平台提供的 GitHub 导入能力。

## 标签建议

```text
AI Agent
Agent Skills
SKILL.md
OpenClaw
SkillHub
Codex
Claude Code
知识卡片
协同进化
知识管理
LLM Wiki
PKM
AI学习
```

## 安全说明

当前公开能力包不包含密钥、私有路径或用户学习数据。  
如果配合本地知识卡片库使用，个人掌握度、解释次数和学习反馈应默认保存在本地，不建议直接公开。

---
name: lls-cangjie-knowledge-distiller
license: MIT
description: 把书籍、课程、访谈、播客或长视频文字稿中的方法论，蒸馏成一组 WorkBuddy 可调用、可测试的独立 Skill。当用户说“仓颉、拆书、把这份课程做成 Skill、把长视频的方法提炼成能力、不要摘要而要可执行方法”时使用；不用于普通摘要、读后感或模仿作者口吻。
---

<!-- workbuddy-install: pending; slug: lls-cangjie-knowledge-distiller -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-cangjie-knowledge-distiller`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-cangjie-knowledge-distiller`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-cangjie-knowledge-distiller/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-cangjie-knowledge-distiller` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师仓颉知识蒸馏器

> 类型：LLS Adapted
> 当前版本：1.0.0
## 一句话用途

不是把长内容压缩成摘要，而是把其中能够反复使用的方法，制作成一组会在正确场景出现、能按步骤干活、也知道何时停下的 AI 员工。

## WorkBuddy 适配原则

1. **串行可完成**：默认由当前 WorkBuddy 会话依次完成五种提取视角，不把并行子智能体当作必要条件。
2. **阶段可续跑**：每完成一阶段就更新 `PIPELINE_STATE.md`，中断后读取状态继续。
3. **先在工作区制作**：构建产物放在用户指定工作区；只有通过测试的单个 Skill 才进入 `~/.workbuddy/skills/`。
4. **逐个安装**：一本书可能生成多个 Skill，WorkBuddy 安装的是每个独立 Skill 目录，不是整个构建工作区。
5. **保留来源边界**：记录来源、作者、日期和定位信息；不把长篇受限内容复制进公开 Skill。

## 输入合同

开始前确认并记录：

- 可读取的文本路径或用户已经粘贴的文本；
- 标题、作者或讲者、年份或发布时间；
- 本次要解决的实际问题；
- 产物只在本地使用，还是准备公开分享；
- 首次试点默认只处理一份材料，先生成 1—3 个 Skill。

没有完整文本时，可以先做“输入准备清单”，但不根据记忆代替原材料蒸馏。视频和音频应先取得合法可用的字幕或转写稿。

## 六阶段流程

### 0. 初始化与全局理解

如果可以执行 Python，先运行：

```bash
python3 scripts/init_workspace.py \
  --source "<SOURCE_TEXT>" \
  --output "<WORKSPACE>/cangjie-builds/<source-slug>" \
  --title "<标题>" \
  --creator "<作者或讲者>"
```

阅读材料后生成 `CONTENT_OVERVIEW.md`：写清核心问题、内容骨架、关键术语、作者假设、可迁移领域和明显盲点。详细格式见 `references/workflow.md`。

### 1. 五视角提取

默认按以下顺序分别阅读并记录，避免后一视角覆盖前一视角的判断：

1. 框架：决策模型、步骤和结构；
2. 原则：规则、清单和判断条件；
3. 案例：作者真正使用方法的情境；
4. 反例：失败模式、误用与警告；
5. 术语：有特殊含义的关键词。

提取问题和候选格式见 `references/extraction-lenses.md`。若宿主明确支持并行任务，可以并行加速，但最终输出格式保持一致。

### 2. 三重验证与人工检查点

每个候选方法必须同时回答：

- **跨段支持**：材料中是否至少有两处相互独立的证据？
- **预测能力**：是否能指导一个原文没有直接回答的新问题？
- **独特价值**：是否比常识或一句口号更具体？

通过项写入 `verified.md`，淘汰项及原因写入 `rejected/`。把“保留 N 项、淘汰 M 项”的标题列表交给用户确认，再进入制作阶段。

### 3. 制作独立 Skill

每个通过项使用 `assets/generated-skill-template.md` 创建独立目录，并补齐：

- R：短引用或可定位证据；
- I：用自己的话解释方法；
- A1：原材料中的真实应用；
- A2：未来什么任务应触发；
- E：可执行步骤；
- B：边界、反例和停止条件。

`description` 必须同时写清“什么时候用”和“什么时候不用”。每个生成 Skill 使用独立、小写、连字符 slug。

### 4. 关联与压力测试

为每个 Skill 创建 `test-prompts.json`，至少包含：

- 3 条应该触发；
- 2 条不应该触发；
- 1 条边界模糊；
- 如果有兄弟 Skill，再加 1 条容易串岗的混淆题。

测试契约和评分规则见 `references/quality-gates.md`。没有独立评测会话时，可以由当前会话自测，但必须在结果中标记“同会话自测”，不要写成独立盲测。

### 5. 验证、交付与安装

先运行：

```bash
python3 scripts/validate_distillation.py "<WORKSPACE>/cangjie-builds/<source-slug>"
```

只有验证通过的 Skill 才可以复制到：

```text
~/.workbuddy/skills/<generated-skill-slug>/
```

安装后必须读回目标目录中的 `SKILL.md`，核对 slug、版本和文件完整性；再开一个新会话，用一条“应该触发”和一条“不应该触发”的题做验证。发布到 GitHub、飞书或 SkillHub 前，单独确认目标、许可、隐私和版本。

## 默认输出结构

```text
<workspace>/cangjie-builds/<source-slug>/
├── SOURCE_MANIFEST.json
├── PIPELINE_STATE.md
├── CONTENT_OVERVIEW.md
├── verified.md
├── candidates/
├── rejected/
├── skills/
│   └── <generated-skill-slug>/
│       ├── SKILL.md
│       ├── test-prompts.json
│       └── test-results.md
├── INDEX.md
├── GLOSSARY.md
└── DIGEST.md
```

## 完成检查

- [ ] 来源文本、元信息和使用权已经记录；
- [ ] 五种视角分别执行，没有只做摘要；
- [ ] 每个保留方法通过三重验证；
- [ ] 每个 Skill 包含 R / I / A1 / A2 / E / B；
- [ ] 测试覆盖触发、不触发、边界和串岗；
- [ ] 验证脚本通过；
- [ ] 构建目录中不依赖其他宿主的专属安装目录；
- [ ] WorkBuddy 安装后已读回，并用新会话检查触发。

## 来源

本公开适配版基于 kangarooking 的 `cangjie-skill` 方法重新整理，保留 RIA-TV++、五视角提取、三重验证、知识关联和压力测试思想，并将宿主流程改写为 WorkBuddy 串行可执行、逐个安装和读回验证。完整来源、许可证和改动见 `ORIGIN.md`。

<div align="center">

# AI Co-Evolution Skills

**把人与 AI 协同进化中跑通的工作流，整理成可以直接复用的能力包。**  
**Reusable capability packs for human-AI co-evolution in real work.**

[中文](#中文) · [English](#english)

[![GitHub Stars](https://img.shields.io/github/stars/PhilRobinluo/ai-coevolution-skills?style=social)](https://github.com/PhilRobinluo/ai-coevolution-skills)
[![License](https://img.shields.io/badge/license-CC_BY--NC--SA_4.0_%2B_PolyForm_NC-blue)](LICENSE)
![Skills](https://img.shields.io/badge/skills-39-blue)
![Status](https://img.shields.io/badge/status-growing-brightgreen)

</div>

> **一套可以直接下载、安装和使用的中文 AI Skills。**
> 如果某个 Skill 帮你节省了时间，请点右上角 ⭐ **Star** 收藏这个仓库。你的 Star，也决定我下一步优先更新哪个 Skill。

---

## 中文

很多人用 AI，问题不在于不会写提示词。

真正的问题是：每次都从零开始。

今天让 AI 翻译一份 PDF，明天让 AI 整理一篇文章，后天又想做一个可以分享的读物。每次都要重新解释背景、重新讲标准、重新调格式。时间久了，你会发现自己不是在用 AI 提效，而是在不断训练一个临时工。

这个仓库想解决的是另一件事：

> 把人与 AI 一起做事、一起学习、一起改进时跑通的工作流，沉淀成一个个可以复用、可以安装、可以分享的「能力包」。

它不是一个 prompt 大杂烩，也不是我的私人配置备份。  
它更像一个逐步长出来的工具箱：每个能力包都应该能完成一个真实任务，并且有清楚的输入、输出、边界和使用方式。

### 来源一眼看清

本仓库包含罗老师原创并持续维护的 AI Skills，也会收录经过实际测试的社区优秀 Skills。社区 Skill 的版权归原作者所有，我们优先链接原仓库，并鼓励用户支持原作者。

| 标识 | 类型 | 仓库处理方式 |
|---|---|---|
| 🔵 `LLS Original` | 罗老师原创 | 收录完整源码和安装包 |
| 🟡 `LLS Adapted` | 在许可证允许范围内改编 | 标明原作者、原仓库、许可证和修改内容 |
| 🟢 `Community Pick` | 罗老师实测推荐 | 默认只提供中文介绍和原仓库链接 |

- [查看透明的来源与归属政策](docs/provenance-policy.md)
- [查看社区精选目录](community/)
- [查看获得许可的改编区](adapted/)

> 社区 Skill 由原作者创作，请优先前往原仓库给作者一个 ⭐ Star。
> 如果你认可罗老师的筛选、测试和中文说明，也欢迎 ⭐ Star 本导航仓库。

### 此前新增 18 个可安装 Skill

覆盖 Skill 创建、标题、命名、Mermaid、截图隐私、最佳实践、GitHub 首页、决策辩论、文件整理、纸质文件修复、视频学习、安全审计、中文幽默、真人化写作、短视频拆解和国际技术文档。完整清单见 [`registry.json`](registry.json)。

另有 3 个 [`Community Pick`](community/) 仅做中文介绍和上游导航。


### 精选开源能力已经在仓库内实现

下面三项已经从“推荐链接”升级为可安装的 `LLS Adapted` 公开版。每项都保留上游作者、固定提交、MIT 许可证和罗老师改编记录。

| 能力包 | 它负责什么 | 上游项目 |
|---|---|---|
| [`lls-colleague-skill-distiller`](adapted/lls-colleague-skill-distiller/) | 蒸馏同事、导师或岗位“怎么把工作做好” | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill/tree/dot-skill) |
| [`lls-nuwa-cognitive-distiller`](adapted/lls-nuwa-cognitive-distiller/) | 蒸馏公开人物或主题“怎样思考、判断与表达” | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) |
| [`lls-darwin-skill-optimizer`](adapted/lls-darwin-skill-optimizer/) | 用基线、单变量实验和配对测试持续进化 Skill | [alchaincyf/darwin-skill](https://github.com/alchaincyf/darwin-skill) |

三者组成一条完整链路：

```text
同事经验 / 公开高手资料
          ↓
同事 Skill / 女娲 Skill：生成第一版能力
          ↓
达尔文 Skill：测试、改进、保留或恢复
          ↓
进入公开仓库、飞书教程与 SkillHub 发布流程
```

### 现在有什么？

| 能力包 | 来源 | 它解决什么问题 | 状态 |
| --- | --- | --- | --- |
| [`bilingual-reader-maker`](skills/bilingual-reader-maker/) | 🔵 LLS Original | 把英文 PDF / 长文做成中英双语移动阅读版，输出 HTML + PDF。 | Stable |
| [`concept-explainer`](skills/concept-explainer/) | 🔵 LLS Original | 在做真实任务时，把陌生工具、命令、配置、架构和报错链路解释成通俗知识卡片。 | Stable |
| [`lls-workbuddy-guide`](skills/lls-workbuddy-guide/) | 🔵 LLS Original | 带新手从真实任务开始，跑通 WorkBuddy 的执行、验收与复用。 | Stable |
| [`lls-ppt-briefing-coach`](skills/lls-ppt-briefing-coach/) | 🔵 LLS Original | 用七阶段访谈澄清 PPT 需求，生成可执行的制作指令。 | Stable |
| [`lls-learning-guide`](skills/lls-learning-guide/) | 🔵 LLS Original | 陪孩子逐步答题、费曼复述并沉淀学习档案。 | Stable |
| [`lls-skill-lifecycle-manager`](skills/lls-skill-lifecycle-manager/) | 🔵 LLS Original | 隔离管理私有母库与公开分享库的版本、发布和运行副本。 | Stable |
| [`lls-dialogue-subtext-reader`](skills/lls-dialogue-subtext-reader/) | 🔵 LLS Original | 分开原话事实与推测，生成可验证、低冲突的沟通回应。 | Stable |
| [`lls-local-excel-vba-data-processor`](skills/lls-local-excel-vba-data-processor/) | 🔵 LLS Original | 用本地 Excel VBA 处理敏感数据，附测试、日志、回滚和验收。 | Stable |
| [`lls-ip-positioning-coach`](skills/lls-ip-positioning-coach/) | 🔵 LLS Original | 用七步互动找到真实可信、能持续表达并可小步验证的个人 IP 定位。 | Stable |
| [`lls-mermaid-diagram`](skills/lls-mermaid-diagram/) | 🔵 LLS Original | 选择正确图型、压缩结构并真实编译 Mermaid 图。 | Stable |
| [`lls-ppt-workflow-builder`](skills/lls-ppt-workflow-builder/) | 🔵 LLS Original | 从演示目标推进到逐页制作、演练与验收。 | Stable |
| [`lls-prompt-basics-coach`](skills/lls-prompt-basics-coach/) | 🔵 LLS Original | 用真实任务和样例测试教普通用户写提示词。 | Stable |
| [`lls-code-anatomy`](skills/lls-code-anatomy/) | 🔵 LLS Original | 把一小段代码拆成数据流、语法解剖、亲手运行和可复习学习卡片。 | Stable |
| [`lls-short-video-breakdown`](skills/lls-short-video-breakdown/) | 🔵 LLS Original | 用时间点和原文证据拆解短视频结构、留存、口语与镜头。 | Stable |
| [`lls-douyin-oral-script-writer`](skills/lls-douyin-oral-script-writer/) | 🔵 LLS Original | 把真实观点写成自然、可信并经过朗读计时的抖音口播稿。 | Stable |
| [`lls-ai-video-script-planner`](skills/lls-ai-video-script-planner/) | 🔵 LLS Original | 从传播任务推进到分镜、素材、生成提示和制作验收。 | Stable |
| [`lls-ai-drawing-prompt-coach`](skills/lls-ai-drawing-prompt-coach/) | 🔵 LLS Original | 从画面意图到可测试、可迭代的文生图提示词。 | Stable |
| [`lls-ai-poster-design-coach`](skills/lls-ai-poster-design-coach/) | 🔵 LLS Original | 从传播目标和信息层级推进到海报版式与导出验收。 | Stable |
| [`lls-jimeng-image-editing-coach`](skills/lls-jimeng-image-editing-coach/) | 🔵 LLS Original | 保留原图关键结构，分区、小步完成图片编辑。 | Stable |

第一个能力包来自一个很具体的需求：  
把一份英文创业手册，做成适合中文读者学习英语的双语读物。

最后我们定下来的标准是：

- 保留原材料的视觉气质，比如封面、章节图、配色、图标。
- 正文不强行左右分栏，而是手机友好的单栏阅读。
- 英文一段，中文一段，方便查词、跟读、复制和解析。
- HTML 是真文本，不是截图；PDF 从 HTML 导出，方便分发。
- 署名放在文末，克制一点，不打扰阅读。

### 为什么叫「能力包」？

因为对普通使用者来说，`skill` 这个词还是太技术。

他们真正关心的不是：

```text
这个 prompt 怎么写？
这个 agent 怎么调用？
这个脚本怎么跑？
```

他们关心的是：

```text
我给你一个英文 PDF，你能不能变成一份好看的双语读物？
我有一批笔记，你能不能帮我整理成文章？
我有一个工作流，能不能下次不用重新解释？
```

所以这里的每个 skill，都会尽量被打磨成一个「能力包」：  
让 AI 不只是聊天，而是稳定地完成一类任务。

### 许可证与商业使用

原创 Skill 的 `SKILL.md`、references、README/docs 和原创素材采用 [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt)；`skills/**/scripts/**` 与 `tools/**` 中的实质软件代码采用 [PolyForm Noncommercial 1.0.0](LICENSES/PolyForm-Noncommercial-1.0.0.txt)。`adapted/`、`community/` 与第三方材料保持各自上游许可证。

企业内部普通办公可按[额外许可](ADDITIONAL-PERMISSIONS.md)免费使用。收费课程、转售、客户交付、SaaS、代运营及其他商业使用须取得[商业授权](COMMERCIAL-LICENSE.md)。[历史 MIT 版本](LICENSE)已经授予的权利继续有效；完整分流说明见 [LICENSE](LICENSE) 和 [第三方通知](THIRD_PARTY_NOTICES.md)。

### 安装

#### WorkBuddy：先用精确 slug 安装

每个 Skill 页面都写明唯一 slug，并提供两条安装路径。最省事的方式是在 WorkBuddy 对话中粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub CLI。
搜索目标 Skill 的精确 slug；只有 slug 完全一致时，才安装到 `~/.workbuddy/skills/`。
安装后读取 `~/.workbuddy/skills/<slug>/SKILL.md`，核对 name 和 version（如有），再新开或重启 WorkBuddy 会话。
```

也可在左侧 **「技能」** → **「添加技能」或「查找技能」** 中搜索精确 slug 后安装；不同 WorkBuddy 版本的界面名称可能略有变化。若没有精确匹配，请不要安装同名条目，改用该 Skill README 的 GitHub Release 或手动复制目录。

- [查看全部 WorkBuddy 安装步骤与当前发布状态](docs/how-to-install.md)
- [浏览 32 个原创 Skill](skills/)；另有 [4 个透明改编 Skill](adapted/)

#### Codex / Claude Code 手动安装

```bash
# Codex
mkdir -p ~/.codex/skills
cp -R skills/bilingual-reader-maker ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -R skills/bilingual-reader-maker ~/.claude/skills/
```

安装后开启新的会话，让客户端刷新 Skill 列表。

### 仓库原则

```text
私有母库与公开分享库各自是真源
两库之间没有复制、镜像、同步或一键公开
GitHub 只承载公开分享库的源码与下载
手机/H5 是普通人的入口
Skill/CLI 是进阶用户的工具层
```

这个仓库会优先保证三件事：

- **可复用**：不是一次性的聊天记录，而是能重复执行的流程。
- **可理解**：尽量讲人话，让非技术用户也知道它能干什么。
- **可公开**：不放私人路径、账号密钥、个人数据库、微信文件路径和不可分享的材料。

### 接下来

这个仓库会慢慢加入更多能力包：

- 双语读物制作
- 任务中的概念解释与知识卡片
- 文章与公众号发布准备
- 知识库整理
- 学习材料转 HTML / PDF
- 面向普通人的 AI 工作流模板

如果你只是想看热闹，可以先 Star。  
如果你也在把自己的 AI 工作流产品化，欢迎 fork、改造，或者提 issue 分享你的场景。

### 收藏与更新

- ⭐ **Star**：收藏项目、表达支持，方便以后找回来。
- 🔔 **Watch → Custom → Releases**：接收新版本发布通知。
- 📦 **Download**：在每个 Skill 页面下载对应的 ZIP 安装包。

> 如果某个 Skill 帮你节省了时间，请点右上角 ⭐ Star 收藏这个仓库。你的 Star，也决定我下一步优先更新哪个 Skill。

---

## English

Most people do not fail with AI because they lack prompts.

They fail because every workflow starts from scratch.

One day you ask AI to translate a PDF. The next day you ask it to turn an article into a shareable document. Then you need a mobile-friendly reader, a publishing checklist, or a reusable writing process. Each time, you explain the background again, restate the standard again, and fix the format again.

This repository is built around a different idea:

> Turn proven human-AI co-evolution workflows into reusable capability packs.

It is not a random prompt dump.  
It is not a private config backup.  
It is a growing library of practical skills that are meant to do real work.

### Provenance

- 🔵 **LLS Original**: created and maintained by Luo Laoshi.
- 🟡 **LLS Adapted**: transparently adapted under the upstream license.
- 🟢 **Community Pick**: tested recommendation linking to the original repository by default.

Community skills remain the property of their original authors. Please support the upstream author first; Star this repository as well if the testing and Chinese guidance help you.

### What is inside?

| Capability Pack | What it does | Status |
| --- | --- | --- |
| [`bilingual-reader-maker`](skills/bilingual-reader-maker/) | Turns English PDFs or long articles into polished Chinese-English mobile readers, with HTML and PDF output. | Stable |
| [`concept-explainer`](skills/concept-explainer/) | Explains unfamiliar tools, commands, configs, architecture, and troubleshooting chains as short knowledge cards during real tasks. | Stable |
| [`lls-workbuddy-guide`](skills/lls-workbuddy-guide/) | Guides beginners through real WorkBuddy tasks, verification, and reusable workflows. | Stable |
| [`lls-ppt-briefing-coach`](skills/lls-ppt-briefing-coach/) | Clarifies presentation needs through a seven-stage interview and produces an actionable brief. | Stable |
| [`lls-learning-guide`](skills/lls-learning-guide/) | Guides students through problem solving, Feynman retelling, and learning records. | Stable |
| [`lls-skill-lifecycle-manager`](skills/lls-skill-lifecycle-manager/) | Governs the full skill lifecycle across source, releases, documentation, and runtime copies. | Stable |
| [`lls-dialogue-subtext-reader`](skills/lls-dialogue-subtext-reader/) | Separates observable dialogue facts from interpretations and produces verifiable, low-conflict replies. | Stable |
| [`lls-local-excel-vba-data-processor`](skills/lls-local-excel-vba-data-processor/) | Builds privacy-preserving local Excel VBA workflows with tests, logs, rollback, and acceptance checks. | Stable |
| [`lls-ip-positioning-coach`](skills/lls-ip-positioning-coach/) | Uses a seven-step coaching flow to create credible, sustainable, testable personal-brand positioning. | Stable |
| [`lls-mermaid-diagram`](skills/lls-mermaid-diagram/) | Selects the right diagram type and validates Mermaid by real compilation. | Stable |
| [`lls-ppt-workflow-builder`](skills/lls-ppt-workflow-builder/) | Runs a presentation from decision goal and evidence through production and rehearsal. | Stable |
| [`lls-prompt-basics-coach`](skills/lls-prompt-basics-coach/) | Teaches prompting through clear goals, constraints, formats, and test cases. | Stable |
| [`lls-short-video-breakdown`](skills/lls-short-video-breakdown/) | Breaks down short videos with timestamps, evidence, retention logic, delivery, and visuals. | Stable |
| [`lls-douyin-oral-script-writer`](skills/lls-douyin-oral-script-writer/) | Turns real ideas and evidence into natural, timed Douyin spoken scripts. | Stable |
| [`lls-ai-video-script-planner`](skills/lls-ai-video-script-planner/) | Plans video beats, storyboards, assets, generation prompts, and production acceptance. | Stable |
| [`lls-ai-drawing-prompt-coach`](skills/lls-ai-drawing-prompt-coach/) | Turns visual intent into testable and iterative text-to-image prompts. | Stable |
| [`lls-ai-poster-design-coach`](skills/lls-ai-poster-design-coach/) | Designs poster information hierarchy, layout, assets, and export acceptance. | Stable |
| [`lls-jimeng-image-editing-coach`](skills/lls-jimeng-image-editing-coach/) | Preserves key image structure through masked, single-variable editing and inspection. | Stable |

The first pack came from a concrete use case: turning an English startup playbook into a bilingual study edition for Chinese readers.

The resulting standard is simple:

- Keep the source material's visual identity when appropriate.
- Do not force side-by-side columns when they hurt mobile reading.
- Put the English paragraph first, then the Chinese translation.
- Keep HTML as real text, so it can be copied, searched, parsed, and restyled.
- Export PDF from HTML for easy sharing.

### Why "capability packs"?

Because most users do not care about the internal words: prompt, agent, script, tool call.

They care about the job:

```text
Can you turn this PDF into a good bilingual reader?
Can you convert my notes into a publishable article?
Can we make this workflow reusable next time?
```

That is what each skill here is trying to become:  
a reusable unit of work that makes AI more dependable.

### Install

#### WorkBuddy

Each skill README contains its exact slug and two WorkBuddy installation paths. In a WorkBuddy chat, ask it to follow `https://skillhub.cn/install/skillhub.md`, search the exact slug, install only an exact match to `~/.workbuddy/skills/`, then read back `~/.workbuddy/skills/<slug>/SKILL.md` and start a new session. The left **Skills** → **Add/Find Skill** flow is the equivalent UI path; labels may vary by version.

If no exact slug is found, do not install a similarly named skill. Use the release or manual-copy fallback documented for that skill instead. See the [full WorkBuddy install guide](docs/how-to-install.md).

#### Codex / Claude Code

```bash
# Codex
mkdir -p ~/.codex/skills
cp -R skills/bilingual-reader-maker ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -R skills/bilingual-reader-maker ~/.claude/skills/
```

Start a new session after installation.

### Direction

```text
The private factory and public sharing repository are separate sources of truth.
There is no copy, mirror, sync, or one-click-public path between them.
GitHub serves only the public sharing repository.
Mobile/H5 is the beginner-friendly front door.
Skills and CLIs are the advanced working layer.
```

This repository will grow slowly, with a bias toward useful, understandable, and shareable workflows.

### Save and follow updates

- ⭐ **Star** saves the project and shows your support.
- 🔔 **Watch → Custom → Releases** follows new release notifications.
- 📦 **Download** gets the installable ZIP from each skill page.

### License

Original Skill content (`SKILL.md`, references, README/docs, and original assets) is licensed under [CC BY-NC-SA 4.0](LICENSES/CC-BY-NC-SA-4.0.txt). Material software code in `skills/**/scripts/**` and `tools/**` is licensed under [PolyForm Noncommercial 1.0.0](LICENSES/PolyForm-Noncommercial-1.0.0.txt). Adapted, community, and third-party material remains under its upstream license.

Free additional permission is available for ordinary internal office use; see [ADDITIONAL-PERMISSIONS.md](ADDITIONAL-PERMISSIONS.md). Paid courses, resale, client delivery, SaaS, managed operations, and other commercial uses require a [commercial license](COMMERCIAL-LICENSE.md). Rights granted for historical MIT releases continue; see [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

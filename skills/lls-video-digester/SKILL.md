---
name: lls-video-digester
license: CC-BY-NC-SA-4.0
description: 把用户提供或公开可用的字幕整理成带时间证据的观点、质疑点和行动清单。 当用户要处理相关材料并需要可验证交付物时使用。
---

<!-- workbuddy-install: published; slug: lls-video-digester -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-video-digester`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-video-digester`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-video-digester/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-video-digester` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师视频消化助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 一句话用途

不是只写一段“视频大意”，而是把字幕变成可回看、可核验的时间证据索引，再判断哪些内容值得看、值得信、值得行动。

## 输入边界

使用用户提供的 SRT/VTT、平台公开字幕，或用户在其正常访问权限内导出的字幕。记录视频标题、作者、URL、发布日期、字幕语言和取得方式。遇到付费墙、访问控制或无授权素材时，停在元数据和用户已提供材料，不尝试绕过限制。

## 3 分钟上手

```text
请用 lls-video-digester 处理这份字幕：先建立时间证据索引，再给核心观点、说话者主张、你的分析、最值得回看的 3 段和行动清单；每条重要结论标时间戳。
```

建立证据索引：

```bash
python3 scripts/index_transcript.py input.srt --output evidence.json
```

脚本解析 SRT/VTT 并输出带起止时间的 JSON 段落；它不下载视频，也不读取浏览器凭证。

## 标准工作流

1. **登记来源**：标题、作者、链接、日期、时长、字幕语言、字幕来源。
2. **检查字幕质量**：缺段、自动转写错误、多人混淆、术语误识别要先标出。
3. **建立证据索引**：保留时间戳，合并过碎句子但不打乱先后顺序。
4. **按主题切块**：以论点转折为边界，而不是机械每 5 分钟切一段。
5. **分三层写结论**：`视频事实`、`说话者主张`、`分析判断`；三者不混写。
6. **找关键片段**：选能代表论证、反例或操作演示的时间段，并说明为什么值得回看。
7. **做可信度检查**：指出证据来源、利益立场、样本局限、自相矛盾和待核验事实。
8. **转成行动**：行动项写负责人、最小动作、完成标准；不把泛泛启发当计划。

成品模板见 [references/evidence-note-template.md](references/evidence-note-template.md)。

## 输出结构

- 30 秒判断：适合谁、是否值得完整观看。
- 5–8 条核心观点，每条带时间戳。
- 关键概念与说话者原意，必要时标注转写不确定。
- 最值得回看的 3 段：起止时间 + 选择理由。
- 反例、证据空缺、需要外部核验的事实。
- 行动清单与不行动清单。

## 质量红线

- 没有字幕证据时，不编造逐字内容和时间戳。
- 不把说话者的预测写成已发生事实。
- 短引用只服务于核验，主体用自己的话概括。
- 涉及医学、法律、投资等高影响主张，单独列入待核验清单。
- 发布前移除私人会议参与人、账号、未公开链接和内部项目细节。

## 失败处理

- **字幕乱码/错轴**：停止总结，先修正编码或时间轴。
- **只有视频没有字幕**：说明当前证据缺口，先请求用户提供或使用公开字幕。
- **自动字幕质量差**：在结论中标置信心等级，关键术语回看原片。
- **内容过长**：先生成主题地图，再逐章处理，最后做跨章节综合。

## 验收

至少确认：主要观点都能回到时间证据；事实、主张、分析分开；没有虚构引用；来源元数据完整；行动项可执行。

## 版本记录

- 1.1.0：新增 SRT/VTT 时间证据索引脚本、来源边界、三层结论法和自动测试。
- 1.0.0：首次公开教学版。

## 三端入口

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-video-digester
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-video-digester-v1.1.0
- 飞书中文教程：https://m2wlgni9k4.feishu.cn/wiki/Kd5WwxI7dikwGFkHxEJcWBC6nus
- SkillHub：搜索唯一 slug `lls-video-digester`

## 支持项目

如果这个 Skill 帮你节省了时间，欢迎给总仓库点一个 ⭐ Star；需要新版通知时，请使用 Watch Releases：

https://github.com/PhilRobinluo/ai-coevolution-skills

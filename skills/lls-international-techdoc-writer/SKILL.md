---
name: lls-international-techdoc-writer
license: CC-BY-NC-SA-4.0
description: 把原始材料重构为面向任务、警示可执行、术语一致并适合翻译与交付的技术文档。 当用户面对相应复杂任务并需要可验证结果时使用。
---

<!-- workbuddy-install: published; slug: lls-international-techdoc-writer -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-international-techdoc-writer`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-international-techdoc-writer`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-international-techdoc-writer/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-international-techdoc-writer` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师国际技术文档助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 文档不是排版美化

先保证读者能在正确条件下安全完成任务，再处理字体和版式。适用于操作手册、安装指南、维护说明、培训教材和技术交付；品牌复刻与未经核准的工程参数不进入成品。

## 信息架构

1. **文档控制页**：编号、版本、状态、所有者、适用产品/版本、发布日期。
2. **读者与前置条件**：角色、所需知识、工具、权限、环境。
3. **任务型章节**：一个章节完成一个目标；标题用动作词。
4. **步骤**：一个编号只包含一个主要动作；先条件、再动作、再可观察结果。
5. **风险信息**：危险源、后果、避免方法三者齐全；警示必须放在危险动作之前。
6. **故障排查**：症状 → 可能原因 → 检查 → 处理 → 升级条件。
7. **参考信息**：参数、术语、兼容矩阵与变更记录独立维护。

## 国际化写作规则

短句、主动语态、一个术语只表达一个概念；按钮和字段名与界面一致；避免双关、文化梗、含糊代词和只有本地读者懂的缩写；数字带单位，日期使用无歧义格式；不要把文字嵌在图片里。

## 标准流程

盘点事实与缺口 → 建内容模型 → 写最危险/高频任务 → 技术审核 → 编辑审核 → 用户试走 → 链接/目录/打印检查 → 批准发布。未知参数保留 `TBD` 并指定责任人，禁止由写作者猜值。

使用 [references/techdoc-review.md](references/techdoc-review.md) 完成评审。

## 验收

随机选择一个新读者，按文档完成关键任务；每一步均有可观察结果；警示位置正确；术语与界面一致；所有 `TBD` 已关闭或明确阻止发布；目录、交叉链接、代码块、分页和打印正常。

## 推荐启动语

```text
请用 lls-international-techdoc-writer 把材料整理成【文档类型】。读者是【】、适用版本是【】。先列事实缺口和内容模型，再写任务步骤、警示、故障排查及用户试走验收。
```

## 版本与三端入口

- 1.1.0：实质重写独有方法、边界与验收。
- GitHub：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-international-techdoc-writer
- Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-international-techdoc-writer-v1.1.0
- 飞书：https://m2wlgni9k4.feishu.cn/wiki/ScG0wCkB1iBb1nkO8MbcnopqnDx
- SkillHub：搜索 `lls-international-techdoc-writer`

有帮助欢迎 Star；需要更新通知请 Watch Releases：https://github.com/PhilRobinluo/ai-coevolution-skills

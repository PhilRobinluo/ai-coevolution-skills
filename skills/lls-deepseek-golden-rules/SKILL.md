---
name: lls-deepseek-golden-rules
license: CC-BY-NC-SA-4.0
description: 把复杂任务拆成可核验阶段，为速度、深度、工具和隐私选择合适的 DeepSeek 使用方式。 当用户面对相应复杂任务并需要可验证结果时使用。
---

<!-- workbuddy-install: published; slug: lls-deepseek-golden-rules -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-deepseek-golden-rules`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-deepseek-golden-rules`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-deepseek-golden-rules/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-deepseek-golden-rules` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 DeepSeek 使用黄金法则

> 类型：LLS Original  
> 当前版本：1.1.0
## 核心原则

模型名称会变化，稳定的是任务设计：先定义交付，再分阶段；先建立事实包，再推理；先小样验方向，再扩大；重要输出用证据和测试验收。涉及当前模型、价格、上下文长度、联网或 API 能力时，以本轮官方文档为准，不把旧课件参数当现状。

## 四级任务路由

- **快速处理**：改写、分类、格式转换；目标清楚、风险低。
- **深度推理**：多约束决策、复杂分析；要求列假设与反证。
- **工具执行**：读取文件、运行代码、调用接口；先声明权限、路径和写入范围。
- **高影响复核**：财务、法律、医学、对外发布；模型只产出草案与核验清单，保留人工确认。

## 黄金工作流

1. 写任务包：目标、受众、输入、约束、交付格式、成功标准。
2. 把任务拆成“事实整理 → 方案生成 → 反例检查 → 成品 → 验收”，每阶段只解决一个问题。
3. 根据阶段选择快速或深度模式，不用最重模型完成所有小动作。
4. 长材料先建目录与证据索引，再按块处理；禁止只凭开头概括全文。
5. 先做 10% 小样，检查口径、风格和事实，再批量扩展。
6. 关键数字、引用、链接和现实状态从原始来源读回。
7. 保存可复用任务包和失败案例，而不是只保存一句“万能提示词”。

任务包见 [references/task-packet.md](references/task-packet.md)。

## 常见失败与修复

问题过大→拆成交付阶段；回答漂移→锁定输出合同；事实过时→刷新官方来源；长文漏读→先建证据索引；反复重写→先确认小样；敏感材料→脱敏、本地处理、限制上传范围。

## 推荐启动语

```text
请用 lls-deepseek-golden-rules 处理【任务】。先生成任务包并选择快速/深度/工具/高影响复核路线；先做小样，重要事实给核验方法，最后按成功标准验收。
```

## 版本与三端入口

- 1.1.0：实质重写独有方法、边界与验收。
- GitHub：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-deepseek-golden-rules
- Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-deepseek-golden-rules-v1.1.0
- 飞书：https://m2wlgni9k4.feishu.cn/wiki/PZu7w4ObYiSovDkyerfckBE4nah
- SkillHub：搜索 `lls-deepseek-golden-rules`

有帮助欢迎 Star；需要更新通知请 Watch Releases：https://github.com/PhilRobinluo/ai-coevolution-skills

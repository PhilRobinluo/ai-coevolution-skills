---
name: lls-best-minds-consultation
license: MIT
description: 为高不确定决策选择少量相关专家视角，分别论证后汇总共识、冲突、行动和反证条件。 当用户面对相应复杂任务并需要可验证结果时使用。
---

<!-- workbuddy-install: published; slug: lls-best-minds-consultation -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-best-minds-consultation`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-best-minds-consultation`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-best-minds-consultation/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-best-minds-consultation` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师最强大脑会诊

> 类型：LLS Adapted  
> 当前版本：1.1.0
## 使用边界

用于战略选择、产品方向、组织难题和重大取舍。它模拟的是**公开思想框架**，不是冒充真人，也不编造专家的私人意见、逐字引语或对当前事件的态度。简单事实、纯执行任务和持证专业判断不进入多人会诊。

## 会诊协议

1. **问题手术**：把原问题改写为决策、期限、约束、不可接受结果和成功指标。
2. **选择席位**：按问题所需能力选 2–4 个视角；每个席位写“为什么相关”和“可能的盲区”，不按名气凑人数。
3. **建立公开依据卡**：记录作者、公开来源、核心框架、适用年代与边界；没有依据时改用通用角色视角。
4. **独立首轮**：各视角先单独给诊断、关键证据、反对意见、建议和最大风险，避免互相迎合。
5. **交叉质询**：每个视角指出另一方案最脆弱的假设，并给可观察反证。
6. **综合而非投票**：整理共识、真实分歧、分歧来源，以及在什么条件下选择哪条路径。
7. **行动处方**：给 7 天内可做的最小实验、负责人、指标、停止条件和复盘日期。
8. **决策留痕**：保存假设、未决问题和未来推翻本结论的信号。

使用 [references/consultation-board.md](references/consultation-board.md) 记录会诊。

## 输出合同

问题重构｜席位与选择理由｜公开依据｜独立意见｜交叉质询｜共识｜不可调和分歧｜综合建议｜最小实验｜反证与复盘日期。

## 质量门禁

- 每个席位必须带来不同决策变量，而不是换语气复述。
- 引用可核验，思想框架与本次推断分开。
- 少数意见不能因“多数票”被删除。
- 不确定信息明确标注，不制造权威感。
- 最终建议必须能被实验或指标证伪。

## 推荐启动语

```text
请用 lls-best-minds-consultation 会诊【决策】。先重构问题，再选择 2–4 个真正相关的公开专家框架；独立作答、交叉质询，最后给共识、分歧、7 天实验和推翻结论的信号。
```

## 版本与三端入口

- 1.1.0：实质重写独有方法、边界与验收。
- GitHub：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/adapted/lls-best-minds-consultation
- Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-best-minds-consultation-v1.1.0
- 飞书：https://m2wlgni9k4.feishu.cn/wiki/YnPbwZm7KimkTkkW71YcjsBPnqh
- SkillHub：搜索 `lls-best-minds-consultation`

有帮助欢迎 Star；需要更新通知请 Watch Releases：https://github.com/PhilRobinluo/ai-coevolution-skills

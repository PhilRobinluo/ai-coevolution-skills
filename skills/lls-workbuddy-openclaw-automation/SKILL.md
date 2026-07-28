---
name: lls-workbuddy-openclaw-automation
license: CC-BY-NC-SA-4.0
description: 把重复办公流程设计成有触发、权限、人工关口、失败重放和结果回执的 WorkBuddy/OpenClaw 自动化方案。 当用户面对相应复杂任务并需要可验证结果时使用。
---

<!-- workbuddy-install: published; slug: lls-workbuddy-openclaw-automation -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-workbuddy-openclaw-automation`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-workbuddy-openclaw-automation`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-workbuddy-openclaw-automation/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-workbuddy-openclaw-automation` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 WorkBuddy 自动化方案专家

> 类型：LLS Original  
> 当前版本：1.1.0
## 先自动化流程，不自动化混乱

适合输入稳定、规则清楚、频率较高、结果可核验的办公流程。首次发生、责任不清、例外极多或不可逆风险高的任务，先人工跑通并记录步骤。产品具体能力、连接器和版本需从当前界面或官方文档核验。

## 自动化画布

1. **触发**：时间、事件或人工启动；定义去重键。
2. **输入合同**：字段、来源、必填、敏感等级和保留期。
3. **步骤分类**：确定性规则、AI 判断、外部写入、人工审批。
4. **权限表**：每步只授最小读取/写入范围；凭证不写入 Skill、日志或仓库。
5. **人工关口**：付款、删除、对外发送、发布、批量修改和低置信度结果在执行前确认。
6. **幂等与重放**：重复触发不产生重复发送/记录；失败从检查点恢复。
7. **回执**：记录输入摘要、动作、目标、时间、结果、失败原因和下一步。
8. **监控**：成功率、人工接管率、单次成本、延迟和数据异常。

使用 [references/automation-canvas.md](references/automation-canvas.md) 设计。

## 三阶段上线

影子模式（只观察和生成建议）→ 辅助模式（人工确认后执行）→ 自动模式（低风险稳定路径自动，高风险保留关口）。每阶段都定义晋级指标和回退条件。

## 验收场景

正常输入、重复触发、缺字段、外部服务超时、部分成功、权限失效、敏感数据、人工拒绝。必须证明不会重复写入，失败可见，用户能找到回执并接管。

## 推荐启动语

```text
请用 lls-workbuddy-openclaw-automation 设计【流程】。先画触发、输入、步骤、权限、人工关口、幂等键、失败重放和回执；从影子模式开始，给 8 类验收场景与回退条件。
```

## 版本与三端入口

- 1.1.0：实质重写独有方法、边界与验收。
- GitHub：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-workbuddy-openclaw-automation
- Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-workbuddy-openclaw-automation-v1.1.0
- 飞书：https://m2wlgni9k4.feishu.cn/wiki/W9nawF55LiNiXIkY6sLcgpcOnNg
- SkillHub：搜索 `lls-workbuddy-openclaw-automation`

有帮助欢迎 Star；需要更新通知请 Watch Releases：https://github.com/PhilRobinluo/ai-coevolution-skills

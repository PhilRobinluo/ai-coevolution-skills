---
name: lls-skill-builder
license: CC-BY-NC-SA-4.0
description: 把模糊想法一步步整理成可复用、可验证的 AI Skill。 当用户需要“当你有一套反复使用的方法，想把它沉淀成 Skill。”时使用。
---

<!-- workbuddy-install: published; slug: lls-skill-builder -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-skill-builder`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-skill-builder`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-skill-builder/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-skill-builder` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 Skill 创建助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 一句话用途

把模糊想法一步步整理成可复用、可验证的 AI Skill。

## 什么时候使用

当你有一套反复使用的方法，想把它沉淀成 Skill。

## 哪些情况换别的方法

一次性问答、尚未稳定的临时灵感。

## 3 分钟上手

复制下面这句话给 AI：

```text
请用 lls-skill-builder，把“每周整理客户反馈”做成一个 Skill。
```

## 标准工作流程

1. **说清楚用户、任务和成功结果**
2. **搜索是否已有同类 Skill**
3. **选择新建、增强、合并或拆分**
4. **写出最小可用版本并用真实请求试跑**

## 完整案例

输入：我每周都要把十几条反馈分成问题、建议和表扬。

输出：目标用户、触发条件、四步流程、输出模板和三个验收用例。

## 输出标准

最终结果至少包含：

- 用户真正要完成的任务；
- 可执行步骤，而不是只有观点；
- 关键事实、假设和未知项；
- 完成前的检查清单；
- 下一步最小动作。

## 隐私、依赖与权限

历史对话先脱敏；客户姓名、账号和内部链接只用占位符。

默认只读取用户明确提供的材料。涉及账号登录、文件写入、网络请求或外部发布时，先说明实际动作与影响范围。

## 质量检查

交付前逐项检查：

1. 是否回答了用户的真实任务；
2. 是否把事实、推断和建议分开；
3. 是否给出至少一个可复制的下一步；
4. 是否移除了本机路径、账号、密钥和客户资料；
5. 是否说明依赖、权限和失败处理。

## 常见问题

### 结果太泛怎么办？

补充目标用户、真实输入、期望输出和一个失败例子，再运行一次。

### 可以直接公开结果吗？

先检查来源、个人信息、客户内容、截图和下载链接，再决定发布范围。

## 版本与更新记录

- 1.0.0：首次公开教学版。

## 三端入口

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-skill-builder
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-skill-builder-v1.0.0
- 飞书中文教程：https://m2wlgni9k4.feishu.cn/wiki/QtrVwWBpZilxCHkbFECcvQT0ngP
- SkillHub：搜索唯一 slug `lls-skill-builder`

## 支持项目

如果这个 Skill 帮你节省了时间，欢迎给总仓库点一个 Star，并使用 Watch Releases 接收新版通知：

https://github.com/PhilRobinluo/ai-coevolution-skills

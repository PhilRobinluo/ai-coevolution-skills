---
name: lls-skill-security-auditor
license: CC-BY-NC-SA-4.0
description: 在安装前检查Skill的权限、脚本、外部请求、提示词注入和数据外传风险。 当用户需要“准备安装社区Skill、插件或包含脚本的能力包。”时使用。
---

<!-- workbuddy-install: published; slug: lls-skill-security-auditor -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-skill-security-auditor`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-skill-security-auditor`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-skill-security-auditor/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-skill-security-auditor` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 Skill 安全审计助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 一句话用途

在安装前检查Skill的权限、脚本、外部请求、提示词注入和数据外传风险。

## 什么时候使用

准备安装社区Skill、插件或包含脚本的能力包。

## 哪些情况换别的方法

把静态扫描结果当成绝对安全证明。

## 3 分钟上手

复制下面这句话给 AI：

```text
请用 lls-skill-security-auditor，审计这个Skill目录，先只读。
```

## 标准工作流程

1. **列出文件、脚本、权限和依赖**
2. **扫描危险命令、凭证读取和网络外传模式**
3. **人工阅读命中上下文并区分误报**
4. **给出风险等级、安装建议和最小权限方案**

## 完整案例

输入：含SKILL.md和两个shell脚本的目录。

输出：文件清单、命中证据、风险分级、误报说明和处理建议。

## 输出标准

最终结果至少包含：

- 用户真正要完成的任务；
- 可执行步骤，而不是只有观点；
- 关键事实、假设和未知项；
- 完成前的检查清单；
- 下一步最小动作。

## 隐私、依赖与权限

审计报告只记录模式与相对路径，不抄录真实密钥内容。

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

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-skill-security-auditor
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-skill-security-auditor-v1.0.0
- 飞书中文教程：https://m2wlgni9k4.feishu.cn/wiki/H2Dhw1uuliyAqck3CDxcCMYcnnh
- SkillHub：搜索唯一 slug `lls-skill-security-auditor`

## 支持项目

如果这个 Skill 帮你节省了时间，欢迎给总仓库点一个 Star，并使用 Watch Releases 接收新版通知：

https://github.com/PhilRobinluo/ai-coevolution-skills

---
name: lls-image-privacy-redactor
slug: lls-image-privacy-redactor
displayName: 罗老师图片隐私打码助手
version: 1.1.0
summary: 检查公开截图中的账号、路径、密钥和个人资料，并生成可复核的打码版本。
license: CC-BY-NC-SA-4.0
description: 检查公开截图中的账号、路径、密钥和个人资料，并生成可复核的打码版本。 当用户需要“截图准备放进文章、课程、GitHub或飞书。”时使用。
---

<!-- workbuddy-install: published; slug: lls-image-privacy-redactor -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-image-privacy-redactor`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-image-privacy-redactor`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-image-privacy-redactor/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-image-privacy-redactor` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师图片隐私打码助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 一句话用途

检查公开截图中的账号、路径、密钥和个人资料，并生成可复核的打码版本。

## 什么时候使用

截图准备放进文章、课程、GitHub或飞书。

## 哪些情况换别的方法

原图必须作为证据保全且禁止像素修改的场景。

## 3 分钟上手

复制下面这句话给 AI：

```text
请用 lls-image-privacy-redactor，检查并打码这张教程截图。
```

## 标准工作流程

1. **列出截图中的敏感区域和风险等级**
2. **让用户确认保留与打码范围**
3. **用坐标生成像素化或纯色遮挡版本**
4. **重新看图确认遮挡完整且正文仍可读**

## 完整案例

输入：包含用户名、主目录路径和API Key的终端截图。

输出：风险清单、坐标方案、脱敏图和复检结果。

## 输出标准

最终结果至少包含：

- 用户真正要完成的任务；
- 可执行步骤，而不是只有观点；
- 关键事实、假设和未知项；
- 完成前的检查清单；
- 下一步最小动作。

## 隐私、依赖与权限

处理后保留原图在本地；公开版本仅使用脱敏副本。

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

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-image-privacy-redactor
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-image-privacy-redactor-v1.0.0
- 飞书中文教程：https://m2wlgni9k4.feishu.cn/wiki/NYC6wTWBEi9QjbkIdOmchBx3nZq
- SkillHub：搜索唯一 slug `lls-image-privacy-redactor`

## 支持项目

如果这个 Skill 帮你节省了时间，欢迎给总仓库点一个 Star，并使用 Watch Releases 接收新版通知：

https://github.com/PhilRobinluo/ai-coevolution-skills

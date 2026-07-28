---
name: lls-mermaid-validator
slug: lls-mermaid-validator
displayName: 罗老师 Mermaid 验证器
version: 1.0.0
summary: 生成并校验 Mermaid 图，减少中文标签、括号和保留字导致的渲染错误。
license: MIT
description: 生成并校验 Mermaid 图，减少中文标签、括号和保留字导致的渲染错误。 当用户需要“需要流程图、架构图、时序图或状态图。”时使用。
---

# 罗老师 Mermaid 验证器

> 类型：LLS Original  
> 当前版本：1.0.0

## 一句话用途

生成并校验 Mermaid 图，减少中文标签、括号和保留字导致的渲染错误。

## 什么时候使用

需要流程图、架构图、时序图或状态图。

## 哪些情况换别的方法

需要照片级视觉或自由插画的任务。

## 3 分钟上手

复制下面这句话给 AI：

```text
请用 lls-mermaid-validator，把这段发布流程画成流程图并校验。
```

## 标准工作流程

1. **选择正确图表类型**
2. **为中文节点加双引号并保持ID简短**
3. **运行Mermaid CLI语法校验**
4. **失败时定位行号、修复并再次校验**

## 完整案例

输入：准备→审核→发布→读回。

输出：通过mmdc校验的Mermaid代码和纯文字版流程。

## 输出标准

最终结果至少包含：

- 用户真正要完成的任务；
- 可执行步骤，而不是只有观点；
- 关键事实、假设和未知项；
- 完成前的检查清单；
- 下一步最小动作。

## 隐私、依赖与权限

图中用角色和占位符代替真实账号、客户和内部域名。

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

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-mermaid-validator
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-mermaid-validator-v1.0.0
- 飞书中文教程：https://m2wlgni9k4.feishu.cn/wiki/FUN1wZmSWigrl3kpEMmcSXkgn2f
- SkillHub：搜索唯一 slug `lls-mermaid-validator`

## 支持项目

如果这个 Skill 帮你节省了时间，欢迎给总仓库点一个 Star，并使用 Watch Releases 接收新版通知：

https://github.com/PhilRobinluo/ai-coevolution-skills

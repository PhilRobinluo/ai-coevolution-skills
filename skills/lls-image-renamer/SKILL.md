---
name: lls-image-renamer
slug: lls-image-renamer
displayName: 罗老师图片智能改名助手
version: 1.0.0
summary: 根据图片内容生成可搜索的文件名，同时保留原始时间戳或设备编号。
license: MIT
description: 根据图片内容生成可搜索的文件名，同时保留原始时间戳或设备编号。 当用户需要“笔记和项目里出现IMG_1234、Pasted image等难搜索图片名。”时使用。
---

# 罗老师图片智能改名助手

> 类型：LLS Original  
> 当前版本：1.0.0

## 一句话用途

根据图片内容生成可搜索的文件名，同时保留原始时间戳或设备编号。

## 什么时候使用

笔记和项目里出现IMG_1234、Pasted image等难搜索图片名。

## 哪些情况换别的方法

文件名参与外部系统签名、数据库主键或固定URL。

## 3 分钟上手

复制下面这句话给 AI：

```text
请用 lls-image-renamer，整理这个目录里的截图名称，先只预览。
```

## 标准工作流程

1. **识别图片内容和原文件名信息**
2. **生成10字内描述并与原名组合**
3. **先dry-run列出重命名映射**
4. **执行后搜索并更新全部Markdown引用**

## 完整案例

输入：IMG_1234.png，内容是GitHub Release页面。

输出：GitHub发布页__IMG_1234.png，并列出受影响引用。

## 输出标准

最终结果至少包含：

- 用户真正要完成的任务；
- 可执行步骤，而不是只有观点；
- 关键事实、假设和未知项；
- 完成前的检查清单；
- 下一步最小动作。

## 隐私、依赖与权限

文件名本身会公开显示；避免写入客户姓名、手机号和内部项目代号。

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

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-image-renamer
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-image-renamer-v1.0.0
- 飞书中文教程：https://m2wlgni9k4.feishu.cn/wiki/CPi8wqiefiPDDrkA0XOcklW8n0b
- SkillHub：搜索唯一 slug `lls-image-renamer`

## 支持项目

如果这个 Skill 帮你节省了时间，欢迎给总仓库点一个 Star，并使用 Watch Releases 接收新版通知：

https://github.com/PhilRobinluo/ai-coevolution-skills

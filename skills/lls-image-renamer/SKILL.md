---
name: lls-image-renamer
license: CC-BY-NC-SA-4.0
description: 批量规划可搜索、可追溯的图片文件名，在真正改名之前检查重名、越界和引用影响。 当用户要处理相关材料并需要可验证交付物时使用。
---

<!-- workbuddy-install: published; slug: lls-image-renamer -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-image-renamer`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-image-renamer`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-image-renamer/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-image-renamer` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师图片智能改名助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 一句话用途

把 `IMG_1234.png`、`Pasted image 2026...png` 这类难搜索名称，整理成“内容描述 + 原始标识”的稳定文件名，并留下可审计映射。

## 适用与边界

适合笔记附件、课程素材、项目截图的批量整理。若文件名是数据库主键、签名参数、固定 URL、代码导入路径或同步软件的外部索引，先盘点依赖，不直接改名。

## 3 分钟上手

```text
请用 lls-image-renamer 扫描这个图片目录：先输出命名规则和 manifest，只预览、不改文件；列出重名与可能受影响的 Markdown 引用。
```

命令示例：

```bash
python3 scripts/plan_rename.py --root ./assets --manifest rename-plan.json mapping.json
python3 scripts/plan_rename.py --root ./assets --manifest rename-result.json --apply mapping.json
```

`mapping.json` 是旧相对路径到新相对路径的对象，例如：

```json
{"IMG_1234.png": "GitHub发布页__IMG_1234.png"}
```

## 标准工作流

1. **盘点**：记录扩展名、原名、时间或设备编号；搜索 Markdown、HTML、代码和数据库引用。
2. **定规则**：使用“可检索描述 + 双下划线 + 原始稳定标识”；描述短、客观，不写敏感信息。
3. **人工复核描述**：AI 只提供候选；不从模糊图像猜测姓名、客户、地点或机密项目。
4. **生成 manifest**：先 dry-run；逐项显示源、目标、状态和原因。
5. **阻断风险**：目标已存在、同批目标重名、源文件越出根目录时整批停止。
6. **执行改名**：用户确认 manifest 后才使用 `--apply`。
7. **更新引用**：按 manifest 另行修改引用；不要把二进制改名与笔记正文替换混成不可回滚的一步。
8. **读回验收**：旧路径不存在、新路径可打开、引用搜索无遗漏、文件数量与哈希一致。

详细复核表见 [references/rename-review.md](references/rename-review.md)。

## 命名判断

- 保留原扩展名；大小写策略在同一目录保持一致。
- 描述优先回答“这张图以后靠什么词找到”，而不是堆视觉细节。
- 使用跨平台字符；避开 `/\:*?"<>|`、控制字符、尾随句点和空格。
- 同一事件多图使用稳定序号，例如 `产品发布会-01__IMG_1234.jpg`。
- 文件名是公开元数据：客户名、手机号、账号、内网域名用中性类别替代。

## 失败处理

- **目标重名**：停止，调整规则或序号；不覆盖。
- **源文件缺失**：重新盘点，不凭旧清单执行。
- **引用过多**：分批改名，每批提交独立 manifest。
- **执行中断**：以 manifest 和实际目录为准重建状态，不盲目重跑。

## 交付物与验收

至少交付命名规则、dry-run manifest、风险项、执行结果、引用更新结果。验收时确认：数量不变、无覆盖、文件可打开、旧引用已清零、manifest 可用于追溯。

## 版本记录

- 1.1.0：新增批量 manifest、根目录约束、重名阻断、dry-run/apply 和自动测试。
- 1.0.0：首次公开教学版。

## 三端入口

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-image-renamer
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-image-renamer-v1.1.0
- 飞书中文教程：https://m2wlgni9k4.feishu.cn/wiki/CPi8wqiefiPDDrkA0XOcklW8n0b
- SkillHub：搜索唯一 slug `lls-image-renamer`

## 支持项目

如果这个 Skill 帮你节省了时间，欢迎给总仓库点一个 ⭐ Star；需要新版通知时，请使用 Watch Releases：

https://github.com/PhilRobinluo/ai-coevolution-skills

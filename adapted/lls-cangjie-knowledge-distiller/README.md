# 罗老师仓颉知识蒸馏器

- **当前源码版本：`1.0.0`**（最近 Release：`1.0.0`）

把书籍、课程、访谈、播客和长视频文字稿中的方法论，蒸馏成 WorkBuddy 可以逐个调用、测试和安装的独立 Skill。

## WorkBuddy 适配了什么

- 默认串行执行五种提取视角，不强制依赖并行子智能体；
- 构建工作区与最终安装目录分开；
- 生成的每个 Skill 独立安装到 `~/.workbuddy/skills/`；
- 增加初始化、结构验证和 WorkBuddy 安装后读回步骤；
- 保留上游的 RIA-TV++、三重验证、知识关联和压力测试思想。

## 快速调用

```text
请使用 lls-cangjie-knowledge-distiller，把这份课程文字稿蒸馏成 1—3 个 WorkBuddy Skill。先做全局理解和候选清单，等我确认后再生成 Skill。
```

## 来源

这是 LLS Adapted 公开版。上游为 [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)，MIT 许可证；详情见 [ORIGIN.md](ORIGIN.md)。

## 在 WorkBuddy 安装

- **Skill slug：`lls-cangjie-knowledge-distiller`**
- **SkillHub 状态：待核验**

把下面内容粘贴到 WorkBuddy 新会话：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-cangjie-knowledge-distiller`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-cangjie-knowledge-distiller/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-cangjie-knowledge-distiller` 后安装；界面文字可能随 WorkBuddy 版本变化。

## 许可证与商业使用

本改编 Skill 的方法与文档保持上游 `MIT` 许可；来源与修改见 [ORIGIN.md](ORIGIN.md)。本适配版新增的 `scripts/` 使用 [PolyForm Noncommercial 1.0.0](../../LICENSES/PolyForm-Noncommercial-1.0.0.txt)。仓库默认许可不覆盖上游权利。

# 罗老师达尔文 Skill 进化器

- **当前源码版本：`1.0.0`**（最近 Release：`1.0.0`）

为已有 Skill 建立基线、测试集、单变量实验和配对验证，让每次修改都有证据、有回退点。

## 快速调用

```text
请使用 lls-darwin-skill-optimizer，只读体检这个 Skill，先给测试集、基线和一项最高价值改进。
```

## 核心原则

- 先测再改；
- 一次只改一个主要变量；
- 新旧版本使用同一组任务；
- 配对比较优先于一次绝对打分；
- 发布与合并保留人工检查点。

## 来源

这是 LLS Adapted 公开版。上游为 [alchaincyf/darwin-skill](https://github.com/alchaincyf/darwin-skill)，MIT 许可证；详情见 [ORIGIN.md](ORIGIN.md)。

## 在 WorkBuddy 安装

- **Skill slug：`lls-darwin-skill-optimizer`**
- **SkillHub 状态：待核验**

把下面内容粘贴到 WorkBuddy 新会话：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-darwin-skill-optimizer`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-darwin-skill-optimizer/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-darwin-skill-optimizer` 后安装；界面文字可能随 WorkBuddy 版本变化。

## 许可证与商业使用

本改编 Skill 保持上游 `MIT` 许可；来源与修改见 [ORIGIN.md](ORIGIN.md)。仓库默认许可不覆盖上游权利。

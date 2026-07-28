# 罗老师代码解剖学习法

- 类型：🔵 `LLS Original`
- **当前源码版本：`1.0.2`**（最近 Release：`1.0.1`）
- 唯一 slug：`lls-code-anatomy`
- 用途：把一小段代码拆成看得懂、跑得通、能复习的中文学习卡片。
- 飞书教程：https://m2wlgni9k4.feishu.cn/wiki/ToAuwccD2iVp6WkrXPSc0Zuen1c
- SkillHub：https://skillhub.cn/skills/lls-code-anatomy
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-code-anatomy-v1.0.2

## 它不是普通的“逐行翻译”

这个 Skill 要求用户经历：

```text
流程地图 → 意图注释 → 最难行逐 token 解剖
→ 预测一个小改动 → 亲手运行 → 提炼模式 → 自测
```

只有“听懂”还不算完成；能够预测、改动、运行和迁移，才算真的掌握。

## 一句话启动

```text
请用 lls-code-anatomy 解剖下面这段代码。先讲数据怎么流动，再逐 token 拆最难的一行；让我先预测一个安全小改动的结果，然后带我运行验证，最后生成学习卡片和 3 道自测题。
```

## WorkBuddy 安装

推荐把下面这句话直接发给 WorkBuddy：

```text
请检查 SkillHub，用唯一 slug `lls-code-anatomy` 查找并安装到 `~/.workbuddy/skills/`。安装后报告版本和实际路径，并新开会话用“解剖这段代码”做一次真实触发。
```

也可以在 WorkBuddy 左侧进入“技能”→“添加技能 / 查找技能”，搜索 `lls-code-anatomy` 后安装。安装后新开会话；如未识别，重启 WorkBuddy。

## 隐私提醒

粘贴代码前先移除 `.env`、Token、Cookie、客户数据、生产连接串和本机绝对路径。示例和笔记只保留理解语法所需的最小片段。

## 许可

Skill 教学内容采用 `CC-BY-NC-SA-4.0`。类型为罗老师原创；不复制私人母库文件，公开版在分享库独立维护。

## 在 WorkBuddy 安装

- **Skill slug：`lls-code-anatomy`**
- **SkillHub 状态：审核中**

把下面内容粘贴到 WorkBuddy 新会话：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-code-anatomy`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-code-anatomy/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-code-anatomy` 后安装；界面文字可能随 WorkBuddy 版本变化。

## 许可证与商业使用

本 Skill 的原创内容采用 [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt)。企业内部普通办公可按[额外许可](../../ADDITIONAL-PERMISSIONS.md)免费使用；收费课程、转售、客户交付、SaaS、代运营等须取得[商业授权](../../COMMERCIAL-LICENSE.md)。

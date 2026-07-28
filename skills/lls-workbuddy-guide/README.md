# 罗老师教你 WorkBuddy

让第一次安装 WorkBuddy 的同学，在一个真实任务中完成首次成功，并通过学习档案、五级阶梯和十关课程逐渐独立。

- **当前源码版本：`2.1.0`**（最近 Release：`2.0.0`）
- 来源：🔵 `LLS Original`
- [飞书专项教程：从第一次安装到独立工作](https://m2wlgni9k4.feishu.cn/wiki/DAv2wAGDXig5sDks5wJcz9yWnAb)
- [WorkBuddy 学习版块首页](https://m2wlgni9k4.feishu.cn/wiki/GaPjwSvF3iENCjkPy97cIrPOnTh)
- [在 SkillHub 查看和安装](https://skillhub.cn/skills/lls-workbuddy-guide)
- [查看 SKILL.md](SKILL.md)
- [下载 2.0.0 安装包](https://github.com/PhilRobinluo/ai-coevolution-skills/releases/download/lls-workbuddy-guide-v2.0.0/lls-workbuddy-guide-2.0.0.zip)
- [校验文件](https://github.com/PhilRobinluo/ai-coevolution-skills/releases/download/lls-workbuddy-guide-v2.0.0/lls-workbuddy-guide-2.0.0.zip.sha256)

## 在 WorkBuddy 安装

- **Skill slug：`lls-workbuddy-guide`**
- **SkillHub 状态：已在 SkillHub 检索到同 slug 条目。**

### 路径一：在 WorkBuddy 对话中粘贴

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub CLI。
搜索 Skill `lls-workbuddy-guide`；只有搜索结果的 slug 与 `lls-workbuddy-guide` 完全一致时，才安装到 `~/.workbuddy/skills/`。
安装后读取 `~/.workbuddy/skills/lls-workbuddy-guide/SKILL.md`，核对 name 和 version（如有），确认实际安装路径；然后新开或重启 WorkBuddy 会话。
若没有完全一致的 slug，请报告未找到，不要安装同名但不同 slug 的条目。
```

若搜索不到完全一致的 slug，请使用本页列出的 GitHub Release；若本页没有 Release，按仓库的手动安装说明复制此目录。

### 路径二：用左侧「技能」界面

在 WorkBuddy 左侧打开 **「技能」** → **「添加技能」或「查找技能」** → 搜索 `lls-workbuddy-guide` → 核对 slug 完全一致后安装。不同 WorkBuddy 版本的界面名称可能略有变化。安装后确认文件在 `~/.workbuddy/skills/lls-workbuddy-guide/SKILL.md`，再新开或重启 WorkBuddy 会话。

## 2.0.0 自适应学习教练

- 首次接待：两分钟识别设备、任务、AI经验和练习材料。
- 学习档案：记住等级、已会能力、最近卡点和下一关。
- 五级阶梯：跟着做 → 一起做 → 自己做 → 教别人 → 沉淀工作流。
- 十关课程：从整理文字一直练到创建个人工作流或 Skill。
- 渐隐提示：同类任务越熟练，教练给出的提示越少。
- 四证验收：成品、事实、格式、外部读回。
- 三分钟复盘：用自己的话讲明白，再更新下一关。
- 错误诊断：从目标、资料、能力、执行、验收和权限六类问题定向恢复。

## 目录

```text
lls-workbuddy-guide/
├── SKILL.md
├── README.md
├── references/
│   ├── curriculum.md
│   ├── scenario-cards.md
│   ├── error-diagnosis.md
│   └── publish-fields.md
├── assets/
│   ├── learning-profile-template.md
│   ├── task-card.md
│   └── review-card.md
└── scripts/
    └── learning_profile.py
```

## 三端闭环

```text
SkillHub 发现与安装
        ↓
飞书学习课程、案例、启动语与常见问题
        ↓
GitHub 源码、Release、Star 与 Watch
        ↓
回到 WorkBuddy 继续下一关
```

## 安装完成后

如果这个 Skill 帮你完成了第一个真实任务，欢迎给[总仓库点一个 ⭐ Star](https://github.com/PhilRobinluo/ai-coevolution-skills)。

- ⭐ Star：收藏项目
- 🔔 Watch → Custom → Releases：接收新版通知
- 📦 Release：下载独立安装包

## 许可证与商业使用

本 Skill 的原创内容采用 [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt)。本目录的 `scripts/` 采用 [PolyForm Noncommercial 1.0.0](../../LICENSES/PolyForm-Noncommercial-1.0.0.txt)。企业内部普通办公可按[额外许可](../../ADDITIONAL-PERMISSIONS.md)免费使用；收费课程、转售、客户交付、SaaS、代运营等须取得[商业授权](../../COMMERCIAL-LICENSE.md)。历史 MIT 版本已授予的权利继续有效。

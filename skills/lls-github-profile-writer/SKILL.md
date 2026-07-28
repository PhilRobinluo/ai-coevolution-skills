---
name: lls-github-profile-writer
description: "把 GitHub 个人主页或项目 README 设计成访客能在一分钟内判断价值、找到代表作、成功运行并知道如何继续关注的公开门面。用于重写 Profile README、开源仓库首页、作品集目录或 Skill 总仓说明时；必须先核验仓库真实内容、安装命令、许可证和维护状态，区分个人主页与单项目任务，不用徽章、口号或 Star 请求掩盖空仓和失效入口。"
license: CC-BY-NC-SA-4.0
metadata:
  short-description: 从访客任务到首屏、证据、安装和可验证入口
---

<!-- workbuddy-install: published; slug: lls-github-profile-writer -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-github-profile-writer`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-github-profile-writer`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-github-profile-writer/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-github-profile-writer` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 GitHub 首页助手

## 先判断是哪一种首页

### 个人 Profile README

回答“你是谁、主要解决什么问题、有哪些代表作、怎么联系或继续关注”。入口仓库通常与 GitHub 用户名同名。

### 单个项目 README

回答“这个项目解决什么、适合谁、如何在几分钟内成功运行、证据在哪里、如何贡献和获取更新”。

### 多 Skill/作品集总仓

回答“有哪些可用能力、如何筛选和下载、来源如何区分、版本如何更新”。

不要把三种页面套成同一个自我介绍模板。

## 必要输入

```text
页面类型：Profile / 单项目 / 作品集总仓
目标访客：用户 / 开发者 / 学员 / 合作者 / 招聘方
希望访客完成的首要动作：
现有仓库、Release、演示和文档：
已验证安装命令：
许可证和来源边界：
维护状态与反馈渠道：
可公开的个人信息：
```

## 一、做真实资产盘点

只使用可点击、可运行或可展示的资产：

- 当前存在的仓库与默认分支；
- 真实 Release 和安装包；
- 已验证命令；
- 截图、演示或在线产品；
- 文档、教程和案例；
- 许可证、来源与维护状态；
- Issues、Discussions 或其他反馈入口。

把计划中的功能标为 Roadmap，不写成“已支持”。空链接和伪造数据比没有数据更伤信任。

## 二、定义访客的一分钟路径

```text
看懂一句话价值
→ 选择一个代表作
→ 看到真实效果或证据
→ 完成一次最小安装/体验
→ Star 收藏或 Watch Releases
```

首屏只服务最重要的一种访客。其他人通过目录进入对应章节。

## 三、写首屏

建议包含：

1. 名称；
2. 一句具体价值；
3. 适合谁；
4. 主要入口按钮或链接；
5. Star 徽章或状态徽章；
6. 一个真实结果或代表作。

一句话价值公式：

```text
帮助【具体人群】用【能力/方法】完成【可观察结果】。
```

避免“热爱技术、持续学习、赋能未来”这类无法验证的表述。

## 四、选择代表作

个人主页保留 3–6 个；单项目展示 1 个完整主路径。每项写：

- 名称；
- 一句话用途；
- 适用人群；
- 当前状态；
- 运行/下载/演示入口；
- 为什么值得看。

代表作按访客价值排序，不按创建日期或作者偏爱排序。

## 五、写可验证的快速开始

快速开始必须能在干净环境复现：

```text
前置条件
→ 安装
→ 最小输入
→ 预期输出
→ 如何判断成功
→ 常见失败与卸载/回滚
```

命令复制前检查路径、包名、版本和 shell。不要把维护者本机绝对路径写进公开 README。

## 六、建立信任区

- 当前版本与最近更新时间；
- 测试/构建状态（真实 CI 才放徽章）；
- 原创、改编、社区推荐的来源标识；
- 许可证和商业使用边界；
- 隐私与安全说明；
- 已知限制；
- 贡献、反馈和行为规范。

社区项目优先链接原作者，不把导航写成自己原创。

## 七、设计 Star 与更新引导

在用户看懂价值和成功体验后再邀请：

> 如果这个项目帮你节省了时间，请点右上角 Star 收藏；需要新版提醒时，请订阅 Watch → Releases。

准确区分：

- Star：收藏、认可和发现；
- Watch Releases：接收新版本通知；
- Release：下载版本化资产；
- Fork：创建自己的开发副本。

不写“点 Star 就能自动收到更新”。

## 八、做两层信息结构

### 首屏

价值、代表作、开始按钮、Star。

### 深入区

完整目录、安装矩阵、来源、架构、贡献、FAQ、许可证。长说明使用折叠块或独立文档，不让首屏变成目录墙。

## 输出格式

1. 页面类型和访客任务；
2. 真实资产盘点与缺口；
3. 首屏文案；
4. 代表作卡片；
5. 快速开始；
6. 完整 README 结构和正文；
7. Star/Watch/Release 引导；
8. 链接、命令、来源和隐私验收结果。

## 失败处理

- 仓库没有可运行内容：先写最小交付与 Roadmap，不做大规模引流。
- 安装命令未验证：标记未验证并给测试步骤，不放“复制即用”。
- 项目太多：按访客任务分组并只选代表作。
- 个人信息过多：只保留公开需要的渠道，移除私人邮箱、手机号和位置。
- 徽章失效：删除或修正来源，不保留装饰性红叉。
- 中英文混乱：先确定主要读者，另一语言用锚点或独立文档。

## 质量门禁

- [ ] 页面类型与首要访客清楚；
- [ ] 首屏一分钟内能回答价值、受众和下一步；
- [ ] 代表作真实存在且入口可点击；
- [ ] 安装命令在干净环境验证；
- [ ] 预期输出和成功信号明确；
- [ ] 计划功能没有冒充已实现；
- [ ] 来源、许可证和维护状态清楚；
- [ ] Star、Watch、Release 和 Fork 解释准确；
- [ ] 没有本机路径、凭证、客户资料或私人联系信息；
- [ ] 所有相对链接、锚点、图片和下载入口已检查；
- [ ] 移动端阅读没有超宽表格或首屏信息墙；
- [ ] README 的承诺与仓库当前内容一致。

审查表见 [references/readme-visitor-test.md](references/readme-visitor-test.md)。

## 使用入口

- [飞书中文教程](https://m2wlgni9k4.feishu.cn/wiki/VGD7woXEKivcbikHFE2cPCZ6nhf)
- [SkillHub 安装页](https://skillhub.cn/skills/lls-github-profile-writer)
- [GitHub 源码](https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-github-profile-writer)
- [GitHub 1.1.0 安装包](https://github.com/PhilRobinluo/ai-coevolution-skills/releases/download/lls-github-profile-writer-v1.1.0/lls-github-profile-writer-1.1.0.zip)

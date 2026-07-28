---
name: lls-article-screenshot
description: "为教程、产品复盘和操作说明规划并采集能证明关键步骤的真实界面截图。用于决定截图证据点、清理演示环境、在 macOS 选择区域/窗口/全屏模式、规范命名、生成 Markdown 引用和交付前隐私复核时；必须先写每张图要证明的事实，优先最小范围截图，不用装饰性图片冒充执行证据。"
license: CC-BY-NC-SA-4.0
metadata:
  short-description: 从证据点规划到安全截图、命名和文章引用
---

<!-- workbuddy-install: published; slug: lls-article-screenshot -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-article-screenshot`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-article-screenshot`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-article-screenshot/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-article-screenshot` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师文章截图助手

## 截图不是装饰，是证据

一篇教程里的截图应回答一个明确问题：读者应该看到什么，才能确认自己走到了正确步骤？

先规划证据，再打开截图工具。不要为了“图文并茂”平均每两段塞一张图。

## 必要输入

```text
文章或教程主题：
读者要完成的任务：
关键成功步骤：
容易误解或失败的位置：
目标软件/网页和版本：
图片最终放到哪里：
项目 assets 目录：
需要隐藏的信息：
```

## 一、建立证据地图

逐步阅读文章，把候选图分为：

- **入口证据**：按钮、菜单、设置位置；
- **动作证据**：用户具体选择了什么；
- **状态证据**：版本号、登录状态、任务状态；
- **结果证据**：成品、回执、外部读回；
- **故障证据**：报错原文及相关上下文。

每张图写一句：

```text
这张图证明【事实】，读者需要看清【区域】，与正文【哪一步】对应。
```

无法写出证明对象的图先删除。

## 二、选择最小截图范围

优先级：

1. 区域：只需要一个局部或终端回执；
2. 窗口：界面位置关系重要；
3. 全屏：跨应用关系或系统级状态必须同时出现。

全屏暴露通知、菜单栏、用户名、其他窗口和客户资料的概率最高。能用窗口就不截全屏，能用区域就不截窗口。

## 三、截图前整理现场

- 关闭通知和无关窗口；
- 用合成账号、示例项目和占位数据；
- 清理终端滚屏，只保留命令与必要回执；
- 把鼠标移出关键信息；
- 确认窗口缩放、系统主题和界面版本；
- 检查浏览器书签栏、头像、标签页标题和下载记录；
- 检查终端主机名、用户目录、Token、历史命令和代理地址。

不要计划“先截了再说”；最安全的敏感信息是从未进入画面。

## 四、执行 macOS 截图

先预检命令：

```bash
scripts/capture.sh   --mode region   --output assets/03-login-success.png   --dry-run
```

确认后执行同一命令并去掉 `--dry-run`。模式：

- `region`：交互框选区域；
- `window`：选择窗口并去掉窗口阴影；
- `full`：截取全屏；
- `--delay 5`：延迟 5 秒，适合菜单或悬浮状态。

目标存在时脚本默认停止；显式 `--force` 后，旧图会先改名备份，再换入新图。

## 五、命名与目录

推荐：

```text
assets/
├── 01-open-settings.png
├── 02-select-api-key.png
├── 03-login-success.png
└── 04-publish-receipt.png
```

规则：

- 序号对应文章阅读顺序；
- 名称描述所证明的动作或结果；
- 不用 `截屏2026...`、`final-final2.png`；
- 同一文章保持统一扩展名和宽度策略；
- 原始高分辨率图与发布图可分目录保存。

## 六、生成文章引用

```markdown
![登录成功后显示当前账号与角色](assets/03-login-success.png)
```

替代文本描述图的结论，不重复“截图”“图片”。正文应在图片前告诉读者为什么看它，在图片后说明如何判断成功。

## 七、隐私与真实性复核

放大到 100% 检查：

- 账号、姓名、头像、手机号、邮箱；
- 绝对路径、主机名、局域网地址；
- API Key、Cookie、二维码、会话串；
- 客户名、文件名、日历和聊天预览；
- 后台管理入口和内部域名；
- 截图是否对应当前版本和真实动作。

需要打码时交给 `lls-image-privacy-redactor` 生成独立公开副本，并再次查看整图。

## 输出格式

1. 截图证据地图；
2. 每张图的模式、范围与准备动作；
3. 规范文件名；
4. 可执行 capture 命令；
5. Markdown 引用与替代文本；
6. 隐私、版本和真实性复核结果；
7. 缺图与需重拍项。

## 失败处理

- 用户取消框选：明确提示未生成文件，不把空路径当成功。
- 菜单一截图就消失：使用延时，或改用系统快捷键。
- 截图太宽：重新截最小区域，不只靠文章端缩小。
- 字太小：缩小截图范围或重新放大界面，不做过度锐化。
- 页面内容变化：记录软件版本和日期，必要时重拍而非继续沿用旧图。
- 隐私太密集：回到合成账号/示例数据重新截图，优先于大面积打码。

## 质量门禁

- [ ] 每张图都有唯一、可说清的证明对象；
- [ ] 关键成功状态和最终结果都有证据；
- [ ] 截图范围是完成证明所需的最小范围；
- [ ] 文件名与正文顺序一致；
- [ ] Markdown 路径在实际项目中可读取；
- [ ] 100% 放大检查过隐私和边缘区域；
- [ ] 画面来自真实步骤，没有用示意图冒充回执；
- [ ] 软件版本与文章描述一致；
- [ ] 原图与脱敏公开图分开保存；
- [ ] 用户取消或脚本失败时没有产生伪成功记录。

规划表见 [references/screenshot-evidence-plan.md](references/screenshot-evidence-plan.md)。

## 使用入口

- [飞书中文教程](https://m2wlgni9k4.feishu.cn/wiki/C9QqwoWa9iz9oNk2fgIcovFRnme)
- [SkillHub 安装页](https://skillhub.cn/skills/lls-article-screenshot)
- [GitHub 源码](https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-article-screenshot)
- [GitHub 1.1.0 安装包](https://github.com/PhilRobinluo/ai-coevolution-skills/releases/download/lls-article-screenshot-v1.1.0/lls-article-screenshot-1.1.0.zip)

---
name: lls-image-privacy-redactor
description: "在截图、照片和教程图片公开前，建立敏感信息清单，按人工确认坐标生成不覆盖原图的脱敏副本，并输出遮挡范围、哈希和复核报告。用于隐藏账号、路径、密钥、身份信息、客户资料、二维码或界面侧栏时；高风险文本默认使用带边距的纯色遮挡，模糊和像素化只用于低风险视觉匿名，发布前必须重新查看整张成品。"
license: CC-BY-NC-SA-4.0
metadata:
  short-description: 从风险清单到确定性遮挡、报告和整图复核
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

## 核心原则

打码的目标不是“看起来模糊”，而是让公开副本中不再可读、可扫码、可放大恢复或可从上下文拼出敏感信息，同时保留读者理解教程所需内容。

原图始终保留在私有位置；公开版本使用新文件。

## 必要输入

```text
输入图片：
发布渠道和受众：
必须保留的教学区域：
已知敏感项：
坐标或允许进行的人工框选：
输出副本与报告路径：
是否允许像素化/模糊：
```

## 一、建立风险清单

### 凭证与访问

API Key、Token、Cookie、二维码、登录链接、恢复码、私钥、验证码、会话 ID。

### 身份与联系

姓名、头像、手机号、邮箱、身份证件、地址、车牌、学号、工号。

### 设备与系统

用户目录、主机名、IP、内部域名、设备序列号、浏览器书签和标签标题。

### 业务与关系

客户名、文件名、群聊、日历、价格、合同、项目代号、后台数据和侧栏列表。

### 可推断信息

即使单项不敏感，多个字段组合也可能识别个人或组织。检查窗口标题、路径层级、时间、地点和画面背景。

## 二、按风险选择处理

优先顺序：

1. 重新截图，使用合成数据或裁掉无关区域；
2. 对高风险文本使用纯色实心遮挡；
3. 对低风险人脸或背景使用像素化/模糊；
4. 若遮挡面积过大，改用重新制作的示意图并明确标注。

密钥、二维码、账号、证件号和可复制文字不用轻微模糊。纯色遮挡更容易验收。

## 三、确认坐标

坐标格式为 `x,y,w,h`，相对原图左上角。每个框应覆盖完整字符并留边距。

先记录：

| 编号 | 敏感内容类型 | 坐标 | 处理方法 | 为什么必须遮挡 |
| --- | --- | --- | --- | --- |

坐标不确定时先生成带网格/标注的审阅副本或让用户确认，不猜测范围。

## 四、生成脱敏副本

高风险默认命令：

```bash
python3 scripts/redact_image.py   source/original.png   output/tutorial-redacted.png   --box 120,80,360,46   --box 900,40,180,180   --method solid   --padding 8   --report qa/tutorial-redaction.json
```

脚本特性：

- 拒绝输入与输出为同一文件；
- 坐标越界时停止；
- 默认给遮挡框四周增加 8 像素；
- 输出输入/成品 SHA256、实际应用坐标和复核提醒；
- 目标存在时默认停止；显式 `--force` 会先备份旧目标。

`--method pixelate` 与 `--method blur` 只用于低风险视觉匿名；报告会保留方法，便于审核。

## 五、处理元数据与派生文件

本脚本重新编码像素输出，通常不会复制原图 EXIF；交付时仍需检查：

- 文件名是否含人名、客户名或日期；
- 同目录是否误带原图、缩略图、编辑工程文件；
- 文档或网页缓存是否仍引用旧图；
- 云盘分享是否包含整个文件夹；
- Git 历史是否已经提交过未脱敏原图。

图像打码不等于清除所有发布链路风险。

## 六、整图复核

发布前由未参与打码的人或第二轮检查完成：

1. 100% 和 200% 放大查看遮挡边缘；
2. 扫描画面四角、标题栏、侧栏、菜单栏和通知；
3. 尝试扫描所有二维码；
4. 检查上下文能否推断被遮挡内容；
5. 确认必要教学内容没有被遮掉；
6. 只把脱敏副本加入文章、飞书或 GitHub。

## 输出格式

1. 风险清单与等级；
2. 保留/裁剪/遮挡决策；
3. 已确认坐标和执行命令；
4. 脱敏副本与 JSON 报告；
5. 整图复核结果；
6. 未解决风险和是否适合公开。

## 失败处理

- 画面敏感信息过多：重做合成截图，不堆满遮挡块。
- 坐标不确定：停止写出成品，先制作审阅标注。
- 遮挡后仍见字符边缘：扩大 padding 并从原图重新生成。
- 二维码只挡中心：覆盖完整二维码及静区，重新扫码测试。
- 教学内容被遮掉：重排截图或用占位数据重拍。
- 未脱敏图已提交 Git：暂停发布，处理仓库历史与缓存，不只新增一张安全副本。

## 质量门禁

- [ ] 发布渠道和受众已明确；
- [ ] 凭证、身份、设备、业务和可推断信息均已检查；
- [ ] 原图未被覆盖或放入公开目录；
- [ ] 高风险文本使用实心遮挡并留安全边距；
- [ ] 所有坐标经过人工确认且未越界；
- [ ] 输入/输出哈希和实际遮挡范围已记录；
- [ ] 100% 与 200% 放大复核通过；
- [ ] 二维码、条形码和链接经过可读性测试；
- [ ] 文件名、同目录文件和文章引用没有泄露；
- [ ] 必要教学信息仍完整可读；
- [ ] 公开系统只使用脱敏副本；
- [ ] 残余风险明确记录。

复核表见 [references/redaction-review.md](references/redaction-review.md)。

## 使用入口

- [飞书中文教程](https://m2wlgni9k4.feishu.cn/wiki/NYC6wTWBEi9QjbkIdOmchBx3nZq)
- [SkillHub 安装页](https://skillhub.cn/skills/lls-image-privacy-redactor)
- [GitHub 源码](https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-image-privacy-redactor)
- [GitHub 1.1.0 安装包](https://github.com/PhilRobinluo/ai-coevolution-skills/releases/download/lls-image-privacy-redactor-v1.1.0/lls-image-privacy-redactor-1.1.0.zip)

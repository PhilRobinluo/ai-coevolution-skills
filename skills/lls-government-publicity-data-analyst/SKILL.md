---
name: lls-government-publicity-data-analyst
description: "分析政务公开宣传、政策解读、活动传播和公共服务内容的触达、互动、转化与服务效果。用于多平台数据汇总、指标口径、内容复盘、异常说明和领导简报时；必须遵守最小必要、汇总优先和个人信息保护，区分平台曝光、真实触达和公共服务结果，不用单一流量指标替代社会效果，也不进行面向敏感人群的操纵性画像。"
license: CC-BY-NC-SA-4.0
metadata:
  short-description: 以统一口径分析政务传播与公共服务效果
---

<!-- workbuddy-install: published; slug: lls-government-publicity-data-analyst -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-government-publicity-data-analyst`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-government-publicity-data-analyst`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-government-publicity-data-analyst/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-government-publicity-data-analyst` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师政务宣传数据分析师

## 分析目标

政务传播分析需要回答的不只是“阅读量多少”，而是：

- 目标公众是否有机会看见；
- 是否理解关键信息；
- 是否完成查询、预约、申报或参与；
- 高频疑问是否被解决；
- 不同渠道是否承担了合适职责；
- 数据是否足以支撑结论。

## 一、先建立任务与边界

```text
传播事项：
公开目标：
目标公众：
发布周期：
渠道：
期望公共行动：
可用数据：
敏感或受限字段：
报告对象：
```

只使用完成分析必要的数据。个人级追踪优先改成汇总统计；涉及未成年人、健康、困难群体等信息时提高保护等级。

## 二、建立指标树

### 供给

- 发布数量；
- 内容形式；
- 发布时效；
- 重点信息覆盖率；
- 无障碍与多语言版本。

### 触达

- 展现、阅读、独立访客；
- 完读或有效播放；
- 渠道覆盖；
- 线下发放或现场触达。

平台“展现”不等于真实看见，跨平台数据不可直接相加为“总人数”。

### 理解与互动

- 重点段落停留；
- 收藏、转发、评论；
- 问答和热线咨询主题；
- 纠错和误解类型；
- 常见问题页面访问。

### 行动与服务

- 点击办事入口；
- 预约、申报、下载、参与；
- 完成率和中断环节；
- 咨询量变化；
- 服务等待时间或重复咨询。

### 质量与风险

- 更正次数；
- 负面反馈类型；
- 无效链接；
- 内容发布延迟；
- 个人信息或版权风险。

## 三、统一口径

每个指标写明：

| 指标 | 定义 | 公式 | 数据源 | 去重 | 时间 | 局限 |
| --- | --- | --- | --- | --- | --- | --- |

特别处理：

- 自然日与工作日；
- 发布日与统计日；
- 播放量与有效播放；
- 独立用户与设备；
- 同一内容多平台重复；
- 线上行动与最终办结。

口径变化需要在趋势图中标记断点。

## 四、数据质量检查

- 平台导出是否完整；
- 是否存在补录、删帖或重复发布；
- 链接参数是否一致；
- 活动期间是否有异常投放；
- 统计权限和抓取时间；
- 样本量是否足够；
- 评论与咨询是否经过脱敏。

不能确认的数据标“待核验”，不为了简报完整而补数字。

## 五、分析方法

### 内容比较

按主题、形式、发布时间和渠道比较，但同时控制投放资源和受众差异。

### 漏斗

```text
展现 → 有效阅读 → 办事入口 → 开始办理 → 完成
```

每一层都要确认是否有可连接的数据，缺失时不要伪造完整漏斗。

### 时间趋势

标记政策发布、活动节点、平台故障、天气或其他可能影响传播的事件。

### 问题主题

评论、热线和问答只做去标识化主题聚类，并保留人工抽查；不根据公开表达推断个人政治、健康或经济属性。

### 地域与人群

优先使用足够大的汇总单元，检查小样本和再识别风险；比较公共服务可达性，不进行操纵性微定向。

## 六、形成简报

推荐结构：

1. 本期公共传播任务；
2. 三条已确认事实；
3. 与上期或基线的变化；
4. 主要公众疑问；
5. 服务转化与中断点；
6. 数据限制；
7. 三项改进动作和负责人。

图表标题直接表达结论，脚注写口径、数据源和统计时间。

## 质量门禁

- [ ] 公共目标与报告使用者明确；
- [ ] 指标树覆盖供给、触达、理解、行动和质量；
- [ ] 跨平台数据没有错误相加；
- [ ] 个体数据最小化并完成脱敏；
- [ ] 小样本和再识别风险已检查；
- [ ] 评论主题经过人工抽查；
- [ ] 平台流量没有替代公共服务结果；
- [ ] 所有关键图表有口径、来源和时间；
- [ ] 事实、解释、局限和行动分开。

口径表见 [references/metric-dictionary.md](references/metric-dictionary.md)。

## 使用入口

- [飞书中文教程](https://m2wlgni9k4.feishu.cn/wiki/IlRcwUV3IijczkkO7Fpc156Ondc)
- [SkillHub 安装页](https://skillhub.cn/skills/lls-government-publicity-data-analyst)
- [GitHub 源码](https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-government-publicity-data-analyst)
- [GitHub 1.1.0 安装包](https://github.com/PhilRobinluo/ai-coevolution-skills/releases/download/lls-government-publicity-data-analyst-v1.1.0/lls-government-publicity-data-analyst-1.1.0.zip)

如果这套口径让传播报告更可信，欢迎给总仓库点一个 Star；需要新版提醒时，请订阅 GitHub Releases。

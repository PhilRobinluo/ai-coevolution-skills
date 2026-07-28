---
name: lls-best-practices-researcher
license: CC-BY-NC-SA-4.0
description: 把“大家都这么做”改造成一份有来源等级、有适用条件、能落地验证的研究结论。 当用户需要把相关任务变成有证据、可验证的交付时使用。
---

<!-- workbuddy-install: published; slug: lls-best-practices-researcher -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-best-practices-researcher`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-best-practices-researcher`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-best-practices-researcher/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-best-practices-researcher` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师最佳实践研究助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 何时触发

当用户问“成熟团队怎么做”“官方推荐什么”“这个方案是否符合行业惯例”，或需要把多个来源转成执行方案时使用。一个稳定事实直接查官方资料即可；没有场景约束时先写明保守假设。

## 研究问题卡

开始前压成一句话：**谁，在什么场景和约束下，为了什么可观察结果，应该采用哪种做法？** 同时记录核验日期、目标版本、预算、团队能力、风险等级和交付格式。

## 证据阶梯

1. 用户提供的真实系统、日志和仓库；2. 官方文档、标准、RFC、发布说明；3. 成熟项目源码与权威实践；4. 近期社区实证；5. 泛化文章。后一级不能轻易推翻前一级。卖方白皮书只证明其产品主张，不自动代表行业共识。

## 标准工作流

1. 写研究问题卡与排除范围。
2. 为结论设“证据需求”：时效、独立来源数、是否必须一手资料。
3. 先检索官方与原始来源，再补不同立场的实证。
4. 每条证据记录 URL/本地相对路径、作者、日期、版本、直接支持什么。
5. 将材料标为：共识、条件成立、冲突、过时、营销主张、证据不足。
6. 对冲突做解释：版本不同、规模不同、目标不同，还是利益立场不同。
7. 把结论适配到用户约束，明确放弃了什么。
8. 转成最小实施步骤、验收指标和重新评估触发条件。

使用 [references/evidence-matrix.md](references/evidence-matrix.md) 留证。

## 输出合同

- **一句话结论**：推荐做法及适用范围。
- **证据矩阵**：关键来源、质量、日期、支持/反驳的主张。
- **共识与冲突**：不把争议藏起来。
- **适配方案**：现在做、暂缓做、明确不做。
- **验收**：指标、检查命令或读回方式。
- **失效条件**：版本、法规、成本、团队规模变化到什么程度需要重查。

## 质量门禁

核心建议至少由两个独立高质量来源支持，或明确标“单一来源”；涉及当前版本、价格、政策、安全等变化事实时刷新网页；引用链接直达支持该主张的页面；事实、推断、建议分开；证据不足时保留空结论，不用数量较多的低质量文章投票。

## 推荐启动语

```text
请用 lls-best-practices-researcher 研究【问题】。目标用户是【】、约束是【】、版本/日期是【】。先给研究问题卡和证据标准，再输出证据矩阵、共识、冲突、落地步骤和失效条件。
```

## 隐私

内部材料只以脱敏相对路径和结论进入证据表；公开报告不暴露本机路径、客户正文、账号、Token 或内部域名。


## 版本记录

- 1.1.0：重写独有方法、证据与验收门禁，消除模板化。
- 1.0.0：首次公开版。

## 三端入口

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-best-practices-researcher
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-best-practices-researcher-v1.1.0
- 飞书教程：https://m2wlgni9k4.feishu.cn/wiki/NdYhwEXjhiFXN9kDA0acyjr8n8c
- SkillHub：搜索 `lls-best-practices-researcher`

## 支持项目

有实际帮助时，欢迎 Star 总仓库；需要更新通知请 Watch Releases：https://github.com/PhilRobinluo/ai-coevolution-skills

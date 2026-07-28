---
name: lls-skill-builder
license: CC-BY-NC-SA-4.0
description: 把反复出现的真实任务提炼成触发准确、流程独特、可测试、可维护的 Skill。 当用户需要把相关任务变成有证据、可验证的交付时使用。
---

<!-- workbuddy-install: published; slug: lls-skill-builder -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-skill-builder`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-skill-builder`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-skill-builder/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-skill-builder` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 Skill 创建助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 先判断是否值得做成 Skill

只有同时满足“任务会重复、方法相对稳定、输入输出可描述、结果可验收”才适合。一次性问答、尚未验证的灵感和只有人设没有方法的提示词，先留作笔记或试验。

## 四种决策

- **新建**：现有 Skill 没覆盖，边界清楚。
- **增强**：同一用户目标，只缺步骤、工具或质量门禁。
- **合并**：两个 Skill 触发语高度重叠，用户难以选择。
- **拆分**：一个 Skill 同时服务不同角色、输入或高风险权限。

## 标准工作流

1. 收集 3 个真实成功请求和 2 个失败/不该触发请求。
2. 写任务合同：用户、输入、输出、成功标准、权限和不做什么。
3. 搜索本地与公开目录，做触发语和能力重叠对比。
4. 选择新建/增强/合并/拆分，并记录理由。
5. 先写最小 `SKILL.md`：准确 description、独有流程、失败路径、验收。
6. 重复且确定的动作放 `scripts/`；背景资料和模板放 `references/`，避免正文无限膨胀。
7. 用正例、反例、边界例逐个试跑；检查模型是否在该触发时触发、在不该触发时保持沉默。
8. 扫描隐私、硬编码路径、密钥、外部依赖和许可证。
9. 版本化发布，记录变更、回滚点和三端映射。

需求卡见 [references/skill-contract.md](references/skill-contract.md)。

## SKILL.md 写法

frontmatter 保持短：`name` 与目录一致；`description` 同时写“做什么”和“何时用”。正文重点写模型无法从常识稳定推断的流程、优先级、失败条件与输出合同，不堆“认真、专业、全面”等形容词。

## 五类验收用例

1. 标准正例：能完成主要任务。
2. 缺输入例：只补最关键缺口，或按明确假设推进。
3. 反触发例：相近但不属于本 Skill。
4. 失败例：依赖缺失、格式错误、外部系统失败时不伪报成功。
5. 隐私例：输入含账号、路径、客户资料时输出正确脱敏。

## 反注水门禁

- 至少有一套该 Skill 独有的判断框架或工具。
- 与同仓其他 Skill 的大段正文不重复。
- 案例包含真实形态的输入、输出和失败条件。
- “输出标准、隐私、常见问题”不能成为复制粘贴主体。
- 发布前必须运行结构校验和至少一个功能试跑。

## 推荐启动语

```text
请用 lls-skill-builder 把【重复任务】做成 Skill。先用 3 个成功请求和 2 个反例定义边界，再检查现有 Skill，给出新建/增强/合并/拆分决定，并生成可测试的最小版本。
```

## 权限与发布

创建本地草稿不等于公开发布。涉及 GitHub、SkillHub、飞书或商店时，分别验证目标账号、公开内容、许可证、安装包和读回结果；私有母库与公开分享库保持物理分离。


## 版本记录

- 1.1.0：重写独有方法、证据与验收门禁，消除模板化。
- 1.0.0：首次公开版。

## 三端入口

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-skill-builder
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-skill-builder-v1.1.0
- 飞书教程：https://m2wlgni9k4.feishu.cn/wiki/QtrVwWBpZilxCHkbFECcvQT0ngP
- SkillHub：搜索 `lls-skill-builder`

## 支持项目

有实际帮助时，欢迎 Star 总仓库；需要更新通知请 Watch Releases：https://github.com/PhilRobinluo/ai-coevolution-skills

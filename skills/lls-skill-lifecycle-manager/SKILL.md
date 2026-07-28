---
name: lls-skill-lifecycle-manager
description: 管理相互隔离的私有 Skill 母库与公开 Skill 分享库。用于在选定仓库内新建、升级、查重、审计、打包、发布或恢复 Skill，并维护该仓库自己的版本、来源、许可证、GitHub Release、飞书说明、WorkBuddy 与 SkillHub 状态。两库各自是真源，公开版只能独立创作和审核；不建立复制、镜像、同步、自动导出或一键公开链路。
license: CC-BY-NC-SA-4.0
---

<!-- workbuddy-install: published; slug: lls-skill-lifecycle-manager -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-skill-lifecycle-manager`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-skill-lifecycle-manager`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-skill-lifecycle-manager/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-skill-lifecycle-manager` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 Skill 全生命周期与仓库治理管家

## 核心使命

把 Skill 当作持续迭代的产品，而不是散落的 ZIP、提示词和平台副本。

始终维护两条彼此隔离的生产链：

```text
私有母库                         公开分享库
  → 私有编辑与版本                  → 公开版独立创作与版本
  → 私有安装包与运行副本             → GitHub Release
  → 私有反馈回到私有库               → 飞书 / SkillHub / WorkBuddy

两库之间只允许：阅读思路后在目标库重新创作
两库之间明确排除：复制、镜像、同步、跨库脚本、一键公开
```

私有母库和公开分享库分别是真源；两边允许同名、不同版本、不同内容和不同历史。

## 开始前

先声明：

```text
使用 skill：lls-skill-lifecycle-manager，原因：本任务涉及 Skill 的仓库治理、版本、发布或渠道联动。
```

然后执行只读盘点，不要先改文件：

1. 先选定本轮唯一写入库：私有母库或公开分享库。
2. 读取项目级 `AGENTS.md`、`CLAUDE.md` 和现有台账。
3. 检查 Git 状态、远程地址、当前版本和工作区修改。
4. 查找重复 Skill、历史包、平台副本和来源信息。
5. 明确本轮模式、范围、验收标准和高风险边界。

可以运行：

```bash
python3 scripts/audit-repository.py \
  --repository <current-repo> \
  --role private \
  --runtime <runtime-skills-dir>
```

## 选择工作模式

| 模式 | 典型请求 | 核心结果 |
|---|---|---|
| 新建 | “把这个流程做成 Skill” | 在选定仓库内新建 Skill、台账和包 |
| 升级 | “把现有 Skill 提升一下” | 只更新选定仓库中的版本 |
| 公开发布 | “发布 GitHub 和飞书” | 从公开分享库发布 Release 和说明 |
| 对账 | “WorkBuddy 里这些要不要导回” | 来源分类、版本差异、回收建议 |
| 审计 | “看看体系有没有乱” | 真源、重复、漂移、隐私和未闭环项 |
| 恢复 | “平台版本比母库新” | 隔离回收、差异审查、确认后合并 |

如果已有 Skill 覆盖主要职责，优先升级、合并或补参考资料。只有边界和用户群明显不同才新建。

## 双库双真源

先按对象选择真源，不跨库决定版本：

- 私有对象：私有母库的 `skills/`、私有台账、私有安装包和私有运行副本。
- 公开对象：分享库的 `skills/` / `adapted/`、公开台账、GitHub Release、飞书和 SkillHub。
- 平台副本出现独有修改时，先进入该对象所属仓库的恢复区，不跨库覆盖。

分享库的脚本、CI、Token 和发布流程不读取私有母库路径或 Git 历史。

详细角色和目录约定见 [references/repository-architecture.md](references/repository-architecture.md)。

## 来源与版权决策

每个公开条目必须选定且展示一种来源：

| 标识 | 类型 | 处理 |
|---|---|---|
| 🔵 `LLS Original` | 罗老师原创 | 完整源码和安装包 |
| 🟡 `LLS Adapted` | 获得许可的改编 | 原作者、原仓库、许可证、版权和修改记录 |
| 🟢 `Community Pick` | 社区实测推荐 | 默认只做中文目录和原仓库链接 |

来源或许可状态不清时，保持链接推荐，不复制源码和安装包。

社区项目优先引导用户支持原作者；罗老师仓库的价值是筛选、测试、中文说明和持续维护目录。

详细规则见 [references/provenance-and-trust.md](references/provenance-and-trust.md)。

## 许可证决策

发布前先按文件类型判断，不用一个许可证笼统覆盖所有材料：

1. 原创 `SKILL.md`、references、README/docs 与原创 assets 默认 `CC-BY-NC-SA-4.0`；
2. `scripts/` 和仓库 `tools/` 中的实质软件代码默认 `PolyForm-Noncommercial-1.0.0`；
3. `adapted/` 与第三方内容始终服从上游许可证，保留 `ORIGIN.md`、版权和修改记录；
4. 企业内部普通办公可按 `ADDITIONAL-PERMISSIONS.md` 免费使用；收费课程、转售、客户交付、SaaS、代运营等必须走 `COMMERCIAL-LICENSE.md`；
5. 每个 Skill 都要在 frontmatter 和 `registry.json` 写 `license`；含 `scripts/` 的原创 Skill 还写 `code_license`；
6. 历史 MIT 版本已经授予的权利继续有效，新规则不追溯撤销。

公开仓根目录必须同步维护 `LICENSE`、`LICENSES/`、`ADDITIONAL-PERMISSIONS.md`、`COMMERCIAL-LICENSE.md`、`THIRD_PARTY_NOTICES.md`，并执行：

```bash
python3 tools/validate-provenance.py
```

详细决策与发布门禁见 [references/licensing-strategy.md](references/licensing-strategy.md)。

## 标准执行流程

### 1. 定义本轮交付

写清楚：

- 目标结果
- 修改范围与明确不做项
- 版本变化
- 2 到 5 条可测试的验收标准
- 测试方式
- 删除、迁移、凭证、付费、最终提交等确认门禁

确认规则：

| 动作 | 执行条件 |
|---|---|
| 只读审计、本地编辑、校验、临时打包 | 明确执行目标后可以推进 |
| GitHub push / Release | 用户本轮明确要求“发布、上线、同步 GitHub”时覆盖本次发布；否则先确认 |
| 飞书写入 | 用户明确要求联动或更新飞书时覆盖本次写入；否则先确认 |
| WorkBuddy 覆盖、批量迁移 | 每次单独确认，并先准备回滚副本 |
| SkillHub 最终提交 | 每次单独确认 |
| 删除旧包、附件、Release、页面 | 每次单独确认 |

### 2. 锁定单一工作区

- 私有任务只修改私有母库；公开任务只修改公开分享库。
- 不把另一个仓库设置成复制源、构建输入或自动化参数。
- 不把 WorkBuddy、飞书附件或 Release 当编辑源。
- 核心流程、判定优先级、失败路径和高风险边界写入 Skill。
- 详细资料放 `references/`，确定性重复操作放 `scripts/`。
- 保持 `SKILL.md` 简洁，避免把完整项目历史塞入上下文。

### 3. 选择版本

- 文案修正、触发优化：patch
- 新增流程、平台或检查项：minor
- 改变核心定位、目录职责或兼容关系：major

两个仓库分别维护自己的版本入口。私有版本不驱动公开版本，公开版本也不反向覆盖私有版本。

更新：

- `publish-info.md`
- Skill 总台账
- 发布队列或发布记录
- 产品功能与交互台账

### 4. 校验与隐私检查

至少检查：

- frontmatter、名称和目录一致
- 必填章节、输出和质量门禁完整
- 无本机绝对路径、密钥、Cookie、账号和客户资料
- 来源类型、许可证和上游链接清楚
- 脚本实际执行通过
- 真实用户请求能够触发并产生交付结果
- 外部命令、Python/Node 包、MCP、账号权限和平台登录要求已在正文或 references 中声明并验证可用

用 [references/test-scenarios.md](references/test-scenarios.md) 的夹具做最小触发测试；根据 Skill 类型补充真实场景。

### 5. 生成可安装包

安装包只包含运行所需文件：

- `SKILL.md`
- `agents/`
- `references/`
- `scripts/`
- `assets/`

生成后必须：

1. 列出 ZIP 内容；
2. 确认包结构为 `<slug>/SKILL.md`，同级放 `agents/`、`references/`、`scripts/`、`assets/`；
3. 在临时目录解压，并确认恰有预期的 `SKILL.md`；
4. 执行随包脚本的代表性测试；
5. 计算 SHA256；
6. 记录版本和证据。

### 6. 在公开分享库独立制作公开版

1. 在私有母库中只读理解功能目标，不复制文件。
2. 结束私有库阅读，切换到独立的公开分享库。
3. 仅使用公开资料和明确许可材料，在分享库重新写公开版。
4. 在分享库独立确定版本、来源、许可证和测试夹具。
5. 运行公开库自己的隐私、来源、许可证和功能校验。
6. 人工检查公开 diff 与包清单后，再进入发布。

禁止 Git 子模块、共享工作树、符号链接、`cp` / `rsync`、跨库相对路径或 CI 拉取私有库。

### 7. GitHub 发布

按顺序执行并读回：

1. 确认当前目录和 remote 都属于公开分享库；
2. 提交并推送公开源码；
3. 等待 GitHub Actions 校验成功；
4. 为单个 Skill 生成版本化 Release；
5. 上传 ZIP 和 SHA256；
6. 用公网地址实际下载并复验；
7. 记录源码、Release 和下载地址。

幂等规则：

- 目标 tag 或 Release 不存在：创建。
- 已存在且资产哈希、源码 commit 和版本一致：读回并复用。
- 已存在但内容不同：停止并标记 REWORK，升级版本后重新发布；不覆盖同名历史 Release。
- Actions 默认每 3 到 10 秒读一次，等待 5 分钟；失败先读日志并修复，最多重跑一次。只有同一外部阻塞连续出现至少三轮才标记 BLOCKED。

Star、Watch 和 Download 分开说明：

- ⭐ Star：收藏与支持
- 🔔 Watch Releases：版本通知
- 📦 Download：安装包

### 8. 飞书联动

每个说明页至少包含：

- 一句话用途
- 适用场景
- 来源标识
- 当前版本
- GitHub 源码
- ZIP 下载链接
- 启动语
- 隐私或依赖提醒
- Star / Watch / Download 说明

飞书只负责中文解释和入口，不作为源文件仓库。写入后必须读回标题、版本、源码、下载和来源字段。

使用稳定的 wiki node token 或文档 token 定位现有页面；总索引以 Skill slug 作为唯一键。找不到旧节点时先搜索和查重，再创建新页，避免同名重复。

### 9. WorkBuddy 与 SkillHub 对账

按来源分类：

- 当前选定仓库已有的运行副本
- 社区或市场安装项
- 本地实验项
- 来源未知项

只在运行副本包含母库没有的新修改时进入恢复流程：

1. 以所属仓库的“上次正式版本”为基准，对真源、正式版本、WorkBuddy 做三方比较；
2. 复制 WorkBuddy 当前副本到带时间和版本的隔离恢复区；
3. 比较文件、版本和哈希；
4. 判断新旧方向；
5. 人工确认后合并；
6. 重新走完整发布链。

如果 WorkBuddy 明确比母库旧且没有独有修改：

1. 记录旧文件清单和哈希；
2. 生成可恢复副本；
3. 获得覆盖确认；
4. 用已验证的 Release 包更新；
5. 重载或重新打开运行工具；
6. 执行最小触发测试；
7. 失败时恢复旧副本。

不要把平台安装目录批量倒回任何真源仓库，更不要跨库回收。

SkillHub 的最终提交、删除旧附件和批量迁移保留用户确认。

### 10. 收口与留下证据

最终报告使用：

| 状态 | 含义 |
|---|---|
| PASS | 已执行并有读回证据 |
| REWORK | 已执行但未达到验收标准 |
| UNCOVERED | 本轮范围内尚未执行 |
| BLOCKED | 连续验证后仍依赖外部变化 |

报告必须包含：

- 改了什么
- 哪些测试通过
- 源码、安装包、GitHub 和飞书入口
- 工作区与远程是否一致
- 未验证项和残余风险
- 下一次最小升级动作

详细检查表见 [references/operating-checklists.md](references/operating-checklists.md)。

## 持续升级机制

每次真实使用后，把反馈分成：

- 触发问题
- 流程缺口
- 平台变化
- 质量门禁不足
- 用户理解成本
- 自动化机会

遵循同一循环：

```text
真实任务
→ 记录证据
→ 找到最小改动
→ 更新所属真源和版本
→ 重跑该仓库自己的交付闭环
→ 读回验证
```

不要为一次偶发现象无限扩张 Skill。重复出现两次以上，或会影响发布正确性、来源可信度和隐私安全时，再沉淀为正式规则。

## 最终质量门禁

- 本轮是否只写入一个已明确选择的真源仓库？
- 两库之间是否仍然没有复制、镜像、同步或一键公开链路？
- 本轮是否更新了原有 Skill，而不是制造重复 Skill？
- 版本号和变更范围是否匹配？
- 来源、作者和许可证是否清楚？
- 是否区分了限制商用与 ShareAlike/Copyleft？
- Skill 内容、实质代码和第三方材料是否分别标明许可？
- ZIP 是否实际解压测试？
- GitHub Actions、Release 和下载是否读回？
- 飞书页面是否写后读回？
- WorkBuddy 副本是否保持下游身份？
- 高风险动作是否保留用户控制权？
- 台账和下一次升级入口是否更新？

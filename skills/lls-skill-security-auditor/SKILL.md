---
name: lls-skill-security-auditor
license: CC-BY-NC-SA-4.0
description: 安装前对 Skill 做静态证据审计、权限建模和人工复核，不把一次扫描当作安全证明。 当用户需要把相关任务变成有证据、可验证的交付时使用。
---

<!-- workbuddy-install: published; slug: lls-skill-security-auditor -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-skill-security-auditor`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-skill-security-auditor`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-skill-security-auditor/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-skill-security-auditor` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 Skill 安全审计助手

> 类型：LLS Original  
> 当前版本：1.1.0
## 审计目标

回答四件事：它读取什么、写入什么、连接哪里、在什么条件下执行高影响动作。适用于社区 Skill、插件和含脚本的能力包；扫描结果只代表当前文件快照。

## 只读快速扫描

```bash
python3 scripts/audit_skill.py TARGET_SKILL > audit.json
```

退出码 1 表示发现 critical 模式，需要人工复核；0 只表示未命中当前 critical 规则，不代表绝对安全。

## 标准工作流

1. **固定证据**：记录来源 URL、版本/提交、下载 SHA256、许可证和审计时间。
2. **列文件**：识别脚本、二进制、大文件、隐藏文件、符号链接和生成物。
3. **建能力图**：文件读取/写入、环境变量、钥匙串、浏览器态、网络域名、子进程、持久化和发布权限。
4. **静态扫描**：查管道执行、递归删除、`eval`、硬编码凭证、浏览器 Cookie、动态下载和可疑编码。
5. **读上下文**：区分文档示例、测试夹具和实际执行路径；不把正则命中直接定罪。
6. **追数据流**：敏感输入从哪里来，经过什么处理，发送到哪里，日志是否留存。
7. **最小权限试跑**：在隔离副本中禁用真实凭证和写权限，观察实际请求与文件变化。
8. **给决策**：允许、限权后允许、待修复、隔离观察；每项附证据和复验方法。

使用 [references/audit-report.md](references/audit-report.md) 出报告。

## 风险等级

- **Critical**：直接私钥、无确认远程执行、明显凭证外传、不可逆广泛破坏。
- **High**：读取凭证/Cookie、动态执行字符串、未限定域名上传、系统级持久化。
- **Medium**：范围过宽的文件访问、未锁版本依赖、日志可能含敏感数据。
- **Low/Info**：文档不足、哈希缺失、可维护性问题。

等级由“能力 + 可达性 + 数据敏感度 + 用户确认 + 可恢复性”共同决定，不只看关键词。

## 输出合同

报告包含快照身份、执行摘要、能力清单、逐项发现（相对路径/行号/证据模式/影响/可达条件）、误报说明、最小权限建议、修复优先级、复验步骤和未覆盖范围。密钥只显示类型与脱敏指纹，不抄录值。

## 推荐启动语

```text
请用 lls-skill-security-auditor 对这个 Skill 先做只读审计：固定版本和 SHA，列能力图，运行静态扫描并人工复核上下文；给风险等级、最小权限方案、复验步骤和未覆盖范围。
```

## 局限

静态扫描看不到运行时下载、远端服务行为、条件触发和供应链后续变化；通过扫描后仍需固定版本、隔离试跑和更新时重审。


## 版本记录

- 1.1.0：重写独有方法、证据与验收门禁，消除模板化。
- 1.0.0：首次公开版。

## 三端入口

- GitHub 源码：https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-skill-security-auditor
- GitHub Release：https://github.com/PhilRobinluo/ai-coevolution-skills/releases/tag/lls-skill-security-auditor-v1.1.0
- 飞书教程：https://m2wlgni9k4.feishu.cn/wiki/H2Dhw1uuliyAqck3CDxcCMYcnnh
- SkillHub：搜索 `lls-skill-security-auditor`

## 支持项目

有实际帮助时，欢迎 Star 总仓库；需要更新通知请 Watch Releases：https://github.com/PhilRobinluo/ai-coevolution-skills

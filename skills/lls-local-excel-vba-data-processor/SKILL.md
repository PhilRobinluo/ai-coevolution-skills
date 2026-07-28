---
name: lls-local-excel-vba-data-processor
license: CC-BY-NC-SA-4.0
description: 在数据不离开本机的前提下，设计、审查和交付 Excel VBA 数据处理方案。用于批量清洗、匹配、拆分、汇总、生成报表或处理敏感表格；必须先确认工作簿结构、备份与样例，再给出带中文注释、日志、异常处理、回滚和验收步骤的宏，不要求上传真实数据。
metadata:
  short-description: 数据留在本地的 Excel VBA 处理与验收
---

<!-- workbuddy-install: published; slug: lls-local-excel-vba-data-processor -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-local-excel-vba-data-processor`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-local-excel-vba-data-processor`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-local-excel-vba-data-processor/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-local-excel-vba-data-processor` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师 Excel VBA 本地数据处理

## 核心目标

帮助用户把重复的 Excel 操作变成可审计、可回滚、可复用的本地宏。

这个 Skill 的重点不是“快速吐出一段 VBA”，而是：

1. 先理解表格结构和业务规则；
2. 用脱敏样例验证规则；
3. 生成有保护措施的 VBA；
4. 明确运行、备份、日志和验收方法；
5. 让真实数据始终保留在用户自己的电脑中。

## 适用场景

- 多张工作表批量合并或拆分；
- 按编号、姓名或组合键匹配数据；
- 清洗空格、日期、金额、重复记录和异常值；
- 生成分类汇总、月报或部门报表；
- 批量建立文件、工作表或打印区域；
- 处理人事、财务、客户等不适合上传的数据。

## 不适用场景

- 多人实时协作或需要数据库级并发；
- 超过 Excel 可稳定承载的数据规模；
- 用户需要绕过工作簿保护、访问控制或审计机制；
- 规则尚未明确，却要求直接在唯一原件上运行。

## 隐私优先规则

1. 默认不要求上传真实工作簿；
2. 优先使用字段名、三到十行脱敏样例和规则描述；
3. 姓名、手机号、身份证号、银行卡号和客户编号使用占位符；
4. 宏默认不联网、不发邮件、不调用外部 API；
5. 任何文件写入位置都由用户明确指定；
6. 第一次运行只处理副本。

## 开始前的最小信息

询问不超过五个关键问题：

1. Excel 是 Windows 版还是 Mac 版，版本大致是什么？
2. 输入工作簿、工作表和表头分别是什么？
3. 唯一键是什么，重复时采用哪条？
4. 希望得到什么输出，保存在哪里？
5. 能否提供脱敏样例和三个验收案例？

如果用户不熟悉 Excel 术语，解释：

- 工作簿：一个 Excel 文件；
- 工作表：底部的一个标签页；
- 表头：第一行字段名称；
- 唯一键：能认出一条记录的编号或字段组合。

## 标准交付流程

### 第一步：把需求写成数据契约

使用下面结构确认：

```text
输入文件：
输入工作表：
表头行：
唯一键：
处理规则：
输出工作表/文件：
遇到空值：
遇到重复：
错误记录放到：
```

没有确认的数据契约，不进入正式宏编写。

### 第二步：制作脱敏测试夹具

至少覆盖：

- 正常记录；
- 空值；
- 重复键；
- 格式错误；
- 找不到匹配项；
- 中文、英文、数字混合；
- 日期或金额边界。

真实数据量很大时，先用二十行以内样例验证。

### 第三步：选择实现方式

| 情况 | 优先方案 |
|---|---|
| 一次性小批量 | Power Query 或公式 |
| 多次重复、规则稳定 | VBA |
| 十万行以上或多文件复杂关联 | Python / 数据库，本 Skill 只做需求与迁移建议 |
| Mac 与 Windows 都要运行 | 避开仅 Windows 可用的 ActiveX、COM 和文件对话框 |

不要为了使用 VBA 而强行使用 VBA。

### 第四步：设计安全护栏

正式宏至少包含：

- `Option Explicit`；
- 关闭与恢复 `ScreenUpdating`、`EnableEvents`；
- 统一错误处理；
- 输入工作表存在性检查；
- 表头检查；
- 最后一行、最后一列的可靠识别；
- 运行日志或错误清单；
- 不使用 `Select`、`Activate` 依赖当前焦点；
- 不覆盖原始数据；
- 结束时恢复 Excel 状态。

### 第五步：生成宏

代码注释必须解释业务目的和失败路径，而不是只翻译语句。

推荐结构：

```vb
Option Explicit

Public Sub RunLocalProcessing()
    On Error GoTo FailHandler

    ' 记录 Excel 原状态，确保成功或失败后都能恢复。
    Dim oldCalc As XlCalculation
    oldCalc = Application.Calculation

    Application.ScreenUpdating = False
    Application.EnableEvents = False
    Application.Calculation = xlCalculationManual

    ' 1. 校验输入
    ' 2. 读取到数组
    ' 3. 执行业务规则
    ' 4. 写入新工作表
    ' 5. 记录处理数量和异常

CleanExit:
    Application.ScreenUpdating = True
    Application.EnableEvents = True
    Application.Calculation = oldCalc
    Exit Sub

FailHandler:
    MsgBox "处理停止：" & Err.Description, vbExclamation
    Resume CleanExit
End Sub
```

### 第六步：提供运行说明

面向普通用户说明：

1. 先另存为 `.xlsm`；
2. 复制原文件作为测试副本；
3. `Alt + F11` 打开 VBA 编辑器；
4. 插入模块并粘贴代码；
5. 修改顶部配置区；
6. 回到 Excel 运行宏；
7. 检查输出页和错误清单；
8. 验收通过后再处理正式副本。

Mac 的快捷键和安全设置可能不同，要提示用户按界面进入“工具 → 宏”。

### 第七步：执行验收

至少核对：

- 输入记录数；
- 成功处理数；
- 跳过数；
- 错误数；
- 输出记录数；
- 金额或数量合计；
- 三个抽样记录；
- 原始工作表是否保持不变。

## 输出格式

```markdown
## 需求与假设

## 数据契约

## 处理规则

## VBA 代码

## 安装与运行

## 测试数据

## 验收清单

## 回滚方法

## 隐私说明
```

完整门禁见 [references/vba-safety-checklist.md](references/vba-safety-checklist.md)。

## 性能规则

- 大批量数据优先一次读入数组、一次写回；
- 查找表优先使用 Dictionary，但 Mac 兼容场景采用 late binding；
- 避免逐单元格读写；
- 明确复杂度和预计数据量；
- 运行超过一分钟时显示进度或分批处理；
- 不在循环里频繁保存工作簿。

## 质量门禁

- [ ] 已确认 Excel 平台与版本；
- [ ] 已使用脱敏样例；
- [ ] 已定义唯一键、空值和重复规则；
- [ ] 宏不覆盖唯一原件；
- [ ] 代码包含错误处理与状态恢复；
- [ ] 输出包含错误清单或日志；
- [ ] 提供安装、运行、回滚和验收步骤；
- [ ] 没有真实路径、账号、密码或客户数据；
- [ ] 至少三个测试案例通过。

## 失败处理

- 表头缺失：停止并列出缺失字段；
- 工作表重名：生成带时间或序号的新名称；
- 唯一键重复：进入错误清单，不静默覆盖；
- 文件正在被占用：停止写入并提示关闭占用；
- Mac 不支持某组件：提供兼容替代；
- 数据规模超出 Excel：输出迁移建议，不继续堆叠宏。

## 使用入口

- [飞书中文教程](https://m2wlgni9k4.feishu.cn/wiki/Gcc5wSTLhiTDMXkQLSUcYTI7nad)
- [SkillHub 安装页](https://skillhub.cn/skills/lls-local-excel-vba-data-processor)
- [GitHub 源码](https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-local-excel-vba-data-processor)
- [GitHub 1.1.1 安装包](https://github.com/PhilRobinluo/ai-coevolution-skills/releases/download/lls-local-excel-vba-data-processor-v1.2.0/lls-local-excel-vba-data-processor-1.2.0.zip)

如果这个 Skill 帮你节省了时间，欢迎给总仓库点一个 Star；需要版本提醒时，请在 GitHub 订阅 Releases。

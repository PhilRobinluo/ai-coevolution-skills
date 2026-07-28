# 🟡 LLS Adapted

这里存放基于他人项目、并在许可证允许范围内完成实质改编的罗老师改编版 Skill。

## 当前条目

| Skill | 用途 | 上游来源 |
|---|---|---|
| [`lls-best-minds-consultation`](lls-best-minds-consultation/) | 多位公开专家视角会诊 | [Ceeon/best-minds](https://github.com/Ceeon/best-minds) |

只有发生了清晰、可说明的实质改动，才进入本目录。单纯认可、推荐、写中文介绍或做安装引导的项目进入 [`community/`](../community/)，不包装成罗老师改编版。

每个改编目录必须包含：

- `SKILL.md`：可安装的改编版；
- `README.md`：中文用途与上手说明；
- `ORIGIN.md`：原作者、上游仓库、固定提交与修改记录；
- `LICENSE.upstream`：上游许可证全文。

新增或升级条目前必须：

1. 核验原作者、原仓库和许可证；
2. 保留上游要求的许可证与版权声明；
3. 使用 [`ORIGIN.template.md`](ORIGIN.template.md) 记录来源和实质修改；
4. 通过 `python3 tools/validate-provenance.py`。

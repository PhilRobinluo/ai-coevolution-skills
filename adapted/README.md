# 🟡 LLS Adapted

这里存放基于他人项目、并在许可证允许范围内完成的罗老师改编版 Skill。

## 当前条目

| Skill | 用途 | 上游来源 |
|---|---|---|
| [`lls-best-minds-consultation`](lls-best-minds-consultation/) | 多位公开专家视角会诊 | [Ceeon/best-minds](https://github.com/Ceeon/best-minds) |
| [`lls-nuwa-cognitive-distiller`](lls-nuwa-cognitive-distiller/) | 蒸馏公开人物或主题的认知框架 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) |
| [`lls-darwin-skill-optimizer`](lls-darwin-skill-optimizer/) | 用实验与配对测试持续进化 Skill | [alchaincyf/darwin-skill](https://github.com/alchaincyf/darwin-skill) |
| [`lls-colleague-skill-distiller`](lls-colleague-skill-distiller/) | 蒸馏同事、导师或岗位的工作经验 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill/tree/dot-skill) |

每个目录均包含：

- `SKILL.md`：可安装的公开改编版；
- `README.md`：中文用途与上手说明；
- `ORIGIN.md`：原作者、上游仓库、固定提交与修改记录；
- `LICENSE.upstream`：上游许可证全文。

新增或升级条目前必须：

1. 核验原作者、原仓库和许可证；
2. 保留上游要求的许可证与版权声明；
3. 使用 [`ORIGIN.template.md`](ORIGIN.template.md) 记录来源和修改内容；
4. 只从公开资料独立整理，不读取私有母库文件；
5. 通过 `python3 tools/validate-provenance.py`。

来源或许可状态仍待核验的项目只进入 [`community/`](../community/) 做链接推荐。

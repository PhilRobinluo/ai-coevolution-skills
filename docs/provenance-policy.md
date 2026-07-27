# Skill 来源与归属政策

本仓库的价值不是搬运数量，而是提供：

> **罗老师原创 Skill + 获得许可的透明改编 + 经过实测的中文 Skill 精选目录。**

## 三类来源

| 类型 | 标识 | 存放位置 | 分发方式 |
|---|---|---|---|
| 罗老师原创 | 🔵 `LLS Original` | `skills/` | 完整源码和安装包 |
| 基于他人改编 | 🟡 `LLS Adapted` | `adapted/` | 保留来源、许可证、版权和修改记录后分发 |
| 社区精选推荐 | 🟢 `Community Pick` | `community/` | 默认只提供中文介绍、核验结果和原仓库链接 |

## LLS Adapted 必填信息

每个 `adapted/<slug>/` 必须包含：

- `SKILL.md`
- `ORIGIN.md`
- 上游要求保留的许可证和版权文件

`ORIGIN.md` 至少写明：

- 原作者
- 原始项目链接
- 原始许可证
- 罗老师修改内容
- 改编版本
- 上游核验版本或提交

如果上游没有明确许可证，只进入 `Community Pick` 做链接推荐。

## Community Pick 收录标准

1. 来源和作者清楚；
2. 许可证状态清楚；
3. 实际安装测试通过；
4. 用途具体；
5. 未发现明显凭证泄露和隐私风险；
6. 最近仍可使用；
7. 写明推荐理由和最后核验日期。

社区精选默认不复制源码。`community/catalog.json` 保存机器可读的原仓库地址和核验信息，后续安装工具应直接从原作者指定版本下载。

## Star 原则

> 这个 Skill 由原作者创作，请优先前往原仓库给作者一个 ⭐ Star。  
> 如果你认可罗老师的筛选、测试和中文说明，也欢迎 ⭐ Star 本导航仓库。

## 许可证说明

- 改编与再分发前必须遵守上游许可证。
- 原项目版权声明和许可证文件按上游要求保留。
- GitHub 公开可见不代表自动获得复制、修改和再发布许可。
- 大幅改编时优先使用 GitHub Fork，让上游关系保持透明。

参考：

- [GitHub Fork 官方说明](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)
- [GitHub 许可证官方说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)


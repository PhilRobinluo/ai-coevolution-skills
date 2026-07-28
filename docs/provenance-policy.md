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

## 许可证与商业使用

本仓库按文件类型分流许可，完整法律文本见根目录 [`LICENSE`](../LICENSE)。

| 范围 | 默认规则 | 机器可读位置 |
|---|---|---|
| `skills/` 下 `lls-original` 的 `SKILL.md`、references、README/docs、原创 assets | `CC-BY-NC-SA-4.0` | `SKILL.md` frontmatter 与 `registry.json` 的 `license` |
| `skills/**/scripts/**` 和仓库 `tools/**` 的实质软件代码 | `PolyForm-Noncommercial-1.0.0` | 含 scripts 的 Skill 在 `registry.json` 声明 `code_license`，并随包携带许可证正文 |
| `adapted/` | 上游许可证优先 | `ORIGIN.md`、上游许可证、frontmatter 与 registry 必须一致 |
| `community/` | 上游许可证；默认仅链接 | `community/catalog.json` |

原创内容的 CC BY-NC-SA 4.0 要求署名、限制商业使用，并要求公开传播的改编采用相同许可。软件代码不使用 CC 许可证，改用 PolyForm Noncommercial 1.0.0。

企业内部普通办公可依据 [`ADDITIONAL-PERMISSIONS.md`](../ADDITIONAL-PERMISSIONS.md) 免费使用。收费课程、转售、客户交付、SaaS、代运营、托管或其他商业使用需要 [`COMMERCIAL-LICENSE.md`](../COMMERCIAL-LICENSE.md) 所述的单独商业授权。

历史 MIT 版本已经授予的权利继续有效。本仓默认许可不覆盖第三方内容；详情见 [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md)。

每次新增或更新 Skill 都运行：

```bash
python3 tools/validate-provenance.py
```

该校验会阻止缺少 `license` 的 Skill、原创内容误用非 CC BY-NC-SA 许可、含脚本却在 registry 漏标 PolyForm、在 SKILL 顶层误加非标准 `code_license`，以及改编内容与上游许可证不一致的情况。

# 公开 Skill 许可证决策

## 已采用的公开仓基线

| 内容 | 许可证 | 边界 |
|---|---|---|
| 原创 `SKILL.md`、references、README/docs、原创 assets | CC BY-NC-SA 4.0 | 署名、非商业、相同方式共享 |
| `skills/**/scripts/**` 与 `tools/**` 的实质软件代码 | PolyForm Noncommercial 1.0.0 | 软件代码的非商业使用；不使用 CC 许可证 |
| 第三方改编内容 | 上游许可证 | 保留作者、来源、版权、许可证与修改记录 |
| 社区推荐 | 原仓库链接 | 默认不复制源码 |

根目录的 [`LICENSE`](../../../LICENSE) 负责分流说明；两份完整法律文本在 `LICENSES/`。每个原创 Skill 的 frontmatter 和 `registry.json` 都要含 `license: CC-BY-NC-SA-4.0`；含 `scripts/` 的 Skill 还要含 `code_license: PolyForm-Noncommercial-1.0.0`。

## 企业内部普通办公与商业授权

企业内部普通办公可按 [`ADDITIONAL-PERMISSIONS.md`](../../../ADDITIONAL-PERMISSIONS.md) 免费使用。以下场景必须取得单独商业授权：收费课程、转售、客户交付、SaaS、托管、代运营、商业咨询交付与付费会员内容。申请范围见 [`COMMERCIAL-LICENSE.md`](../../../COMMERCIAL-LICENSE.md)。

不要把“内部普通办公免费”解释为可面向客户提供服务，也不要把公开仓库误称为 OSI 开源。

## 改编与历史版本

- `adapted/` 必须以 `ORIGIN.md` 和上游许可证为准；本仓默认许可不覆盖它。
- `community/` 仅链接时不重新授权其源码。
- 新许可证只约束采用新许可证发布的新版本；历史 MIT 版本已经授予的权利继续有效。
- 外部贡献者内容换证前须取得相应授权。

## 发布门禁

发布前运行：

```bash
python3 tools/validate-provenance.py
```

它校验每个 Skill 的 `license` 字段、原创内容的 CC BY-NC-SA 默认值、脚本的 PolyForm 标记、改编内容的上游一致性以及根许可证文件存在性。

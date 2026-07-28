# Skill 发布检查清单

发布前逐项确认：

- [ ] `SKILL.md` 有清晰的 `name`、`slug`、`version`、`description` 和 `license` frontmatter。
- [ ] Skill 不含私人路径、密钥、私有数据或只能在个人机器运行的假设。
- [ ] 脚本足够确定、可复用；示例为合成内容或可再分发素材。
- [ ] README 用通俗语言说明用途，并且有唯一的 `**Skill slug：` 标签。
- [ ] README 有两条 WorkBuddy 安装路径：对话粘贴提示词、左侧「技能」界面；两条路径都包含精确 slug、`https://skillhub.cn/install/skillhub.md` 和 `~/.workbuddy/skills/`。
- [ ] README 明确 SkillHub 状态；未发布或未确认同步时，不把同名搜索结果写成已上架。
- [ ] `SKILL.md` 含 `<!-- workbuddy-install: published|pending; slug: ... -->` 标记和对应安装/备用说明。
- [ ] `registry.json` 记录 `version`、`license`、`provenance`、`skillhub_status`；有下载包时，同时记录仍可下载的 `release_version`。
- [ ] 原创 `SKILL.md`、references、README/docs 和原创 assets 标为 `CC-BY-NC-SA-4.0`；含 `scripts/` 的原创 Skill 同时标出 `code_license: PolyForm-Noncommercial-1.0.0`。
- [ ] 实质代码只放入 `skills/**/scripts/**` 或 `tools/**`，并适用 `PolyForm-Noncommercial-1.0.0`；第三方/改编内容保留上游许可证与 `ORIGIN.md`。
- [ ] 用 `tools/package-skill.sh <slug> <version>` 生成自包含 ZIP，并核验包内有内容许可、代码许可、额外许可和商业授权说明。
- [ ] README 链接根 `LICENSE`、`ADDITIONAL-PERMISSIONS.md` 与 `COMMERCIAL-LICENSE.md`；商业场景不承诺免费使用。
- [ ] 已运行 `tools/validate-skill.sh skills/<skill-name>`。
- [ ] 已运行 `python3 tools/validate-workbuddy-install.py` 和 `python3 tools/validate-provenance.py`。
- [ ] 如有测试目录，已运行对应单元测试。

正式发布前还要：打包、核验 ZIP 和 SHA256、读回 Release/SkillHub 的实际版本与安装路径。版本未同步时，保留真实状态，不能把本仓新版本写成平台已发布版本。

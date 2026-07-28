# 公开 Skill 分享库规则

本仓库是公开 Skill 的独立真源，不是私有母库的镜像。

## 双库隔离

- 公开版只能在本仓库内独立创作、审核、定版本和测试。
- 可以只读理解私有 Skill 的功能目标；结束阅读后，使用公开资料重新编写公开版。
- 禁止 `cp`、`rsync`、镜像、自动导出、一键公开、Git 子模块、共享 worktree、符号链接或跨库相对路径。
- 本仓库的 CI、脚本、Token、Deploy Key 和打包器不得读取私有母库。
- 私有版和公开版可以同名，但版本、内容、哈希和历史不要求一致。

## 许可证

- LLS Original 的 `SKILL.md`、references、README/docs 和原创 assets：`CC-BY-NC-SA-4.0`。
- 原创 Skill 含实质 `scripts/` 时：`registry.json` 声明 `code_license: PolyForm-Noncommercial-1.0.0`，安装包携带 PolyForm 正文；`SKILL.md` 顶层不增加 `code_license`。
- LLS Adapted 与第三方材料保持上游许可证、来源、版权和修改记录。
- 企业内部普通办公按 `ADDITIONAL-PERMISSIONS.md`；收费课程、客户交付、转售、SaaS、代运营等进入商业授权。
- 历史 MIT 版本已授予的权利继续有效；新版本换证不追溯撤销。
- 带非商业限制时对外称“源码公开 / 受限开放”，不称 OSI 开源。

## WorkBuddy 与发布

- 每个 Skill 的 `SKILL.md` 和 README 必须写唯一 slug、WorkBuddy 内安装方法、`~/.workbuddy/skills/` 路径和安装后读回。
- `registry.json` 同时保存当前源码版本、已发布 `release_version`、SkillHub 状态、内容许可和代码许可。
- Release ZIP 必须使用 `tools/package-skill.sh`，并包含完整许可证、额外许可和商业授权说明。
- GitHub push、Release、飞书写入和 SkillHub 最终提交分别保留确认与读回，不用一次确认覆盖后续所有版本。

## 公开内容与隐私

- 不提交本机绝对路径、凭证、API Key、个人数据库、微信文件路径、Notion ID 或用户专属源材料。
- 公开示例使用小型合成夹具或明确可再分发的来源。
- 本地路径统一写成 `<workspace>`、`TARGET` 或 `~/work/<project>` 等可配置占位符。
- Skill 必须产品化：`SKILL.md` 清楚、默认值可复用、有示例、边界和验收；质量优先于堆数量。

## 每次新增或更新后

```bash
python3 tools/apply-repository-policy.py
python3 tools/validate-provenance.py
python3 tools/validate-workbuddy-install.py
python3 skills/lls-skill-lifecycle-manager/scripts/audit-repository.py \
  --repository . --role public
```

然后逐个运行 `tools/validate-skill.sh <skill-path>`，并用
`tools/package-skill.sh <slug> <version>` 验证自包含安装包。

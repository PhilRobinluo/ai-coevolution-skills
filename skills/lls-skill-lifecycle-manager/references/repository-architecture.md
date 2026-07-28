# 双库隔离架构

## 两套独立真源

```text
private-factory/                 public-repository/
├── skills/                      ├── skills/
├── packages/                    ├── adapted/
├── registry/                    ├── community/
├── scripts/                     ├── registry.json
└── docs/                        ├── tools/
                                 └── .github/workflows/
```

| 对象 | 真源 | 下游渠道 |
|---|---|---|
| 私有 Skill | 私有母库 | 私有安装包、私有运行副本 |
| 公开 Skill | 公开分享库 | GitHub Release、飞书、SkillHub、WorkBuddy |

## 允许与禁止

允许：

- 有权限的人或 AI 只读理解私有 Skill 的功能目标；
- 退出私有库后，在公开分享库重新创作公开版；
- 两库存在同名但版本、内容和历史不同的 Skill。

禁止：

- `cp`、`rsync`、镜像或自动导出；
- Git 子模块、共享 worktree、符号链接和跨库相对路径；
- 公开仓 CI、脚本、Token 或 Deploy Key 读取私有库；
- 用文件哈希相同证明“公开成功”；
- 从私有母库一键发布 GitHub、飞书或 SkillHub。

## 冲突处理

| 冲突 | 处理 |
|---|---|
| WorkBuddy 与所属真源不同 | 先隔离和 diff，再决定恢复方向 |
| 私有版与公开版不同 | 视为正常；分别按各自需求维护 |
| 公开 Release 与分享库版本不同 | 停止渠道更新，在分享库修正 |
| 飞书链接失效 | 先验证公开 Release，再修入口 |
| 来源许可不清 | 保持 link-only 社区推荐 |

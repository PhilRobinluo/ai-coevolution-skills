# 仓库架构与角色

## 目录角色

```text
private-factory/
├── skills/               # 唯一生产母版
├── packages/             # 本地安装包产物
├── registry/             # 版本、状态、队列和证据
├── scripts/              # 校验、打包、公开同步
├── inbox/                # 待整理或恢复的候选
└── docs/                 # 决策、标准和产品台账

public-repository/
├── skills/               # LLS Original 公开镜像
├── adapted/              # 透明改编
├── community/            # 链接型社区精选
├── registry.json         # 机器可读目录
├── tools/                # 公开校验
└── .github/workflows/    # 校验和单 Skill Release
```

## 平台职责

| 平台 | 职责 | 不承担 |
|---|---|---|
| 私有生产母库 | 编辑、版本、台账、隐私材料、打包 | 公开展示 |
| GitHub | 公开源码、历史、Actions、Release、Star | 私有生产状态 |
| 飞书 | 中文解释、课程入口、分类和下载导航 | 源码真源、长期保存重复 ZIP |
| WorkBuddy / Codex | 安装和运行 | 编辑母版 |
| SkillHub | 分发和审核 | 保存唯一源码 |

## 稳定标识

- Skill slug：长期稳定，如 `lls-skill-lifecycle-manager`
- 显示名称：可以迭代
- Release tag：`<slug>-v<semver>`
- 安装包：`<slug>-<semver>.zip`
- 来源类型：`lls-original`、`lls-adapted`、`community-pick`

## 冲突处理

| 冲突 | 处理 |
|---|---|
| WorkBuddy 比母库内容不同 | 先隔离和 diff，不覆盖 |
| GitHub 与母库不同 | 母库重新生成公开镜像 |
| Release 与源码版本不同 | 停止飞书更新，重新打包发布 |
| 飞书链接失效 | 先验证 Release，再修入口 |
| 来源许可不清 | 退回 link-only 社区推荐 |


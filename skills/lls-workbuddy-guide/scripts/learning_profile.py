#!/usr/bin/env python3
"""创建、读取和更新 WorkBuddy 学习档案。

业务目的：
- 让公开 Skill 在不同宿主中都能用一个纯本地 Markdown 文件延续学习进度；
- 状态只保存能力、关卡和证据摘要，避免把真实材料写进学习档案；
- 所有操作显式接收 --file，不绑定任何个人目录。
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path

MARKER_RE = re.compile(r"<!-- LLS_PROFILE_STATE (\{.*\}) -->")
RISK_RE = re.compile(
    r"(?i)(?:api[_ -]?key|token|password|secret|cookie|authorization)\s*[:=]|"
    r"skh_[a-z0-9]{20,}|gh[pousr]_[a-z0-9]{20,}|bearer\s+[a-z0-9._-]{16,}"
)

LEVEL_NAMES = {
    1: "L1：跟着做",
    2: "L2：一起做",
    3: "L3：自己做",
    4: "L4：教别人",
    5: "L5：沉淀工作流",
}


def default_state() -> dict:
    return {
        "schema_version": 1,
        "level": 1,
        "completed_lessons": [],
        "mastered": [],
        "practicing": ["完成第一个真实任务"],
        "latest_blocker": "",
        "evidence": [],
        "next_lesson": "第1关：整理结构化文档",
        "updated_at": "",
    }


def unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(item.strip() for item in items if item.strip()))


def bullets(items: list[str], empty: str = "暂无") -> str:
    values = unique(items)
    return "\n".join(f"- {item}" for item in values) if values else f"- {empty}"


def validate_summary(value: str) -> str:
    """证据只允许摘要；出现常见凭证形态时直接拒绝写入。"""
    value = value.strip()
    if RISK_RE.search(value):
        raise ValueError("学习档案检测到凭证类内容，请改写成不含具体值的摘要。")
    return value


def render(state: dict) -> str:
    state["updated_at"] = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    marker = json.dumps(state, ensure_ascii=False, separators=(",", ":"))
    level = max(1, min(5, int(state.get("level", 1))))
    return f"""# 我的 WorkBuddy 学习档案

<!-- LLS_PROFILE_STATE {marker} -->

## 当前等级

{LEVEL_NAMES[level]}

## 已完成关卡

{bullets([f"第{x}关" for x in state.get("completed_lessons", [])])}

## 已经掌握

{bullets(state.get("mastered", []))}

## 正在练习

{bullets(state.get("practicing", []))}

## 最近卡点

{bullets([state.get("latest_blocker", "")])}

## 本次证据

{bullets(state.get("evidence", []))}

## 下一关

{bullets([state.get("next_lesson", "")])}

## 隐私说明

本档案只记录学习进度和证据摘要，不记录密码、Token、客户原文、证件、银行卡或内部敏感资料。
"""


def load(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = MARKER_RE.search(text)
    if not match:
        raise ValueError("档案缺少 LLS_PROFILE_STATE 状态标记。")
    state = json.loads(match.group(1))
    if state.get("schema_version") != 1:
        raise ValueError("档案 schema_version 与当前工具不匹配。")
    return state


def save(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(state), encoding="utf-8")


def cmd_init(args: argparse.Namespace) -> None:
    path = Path(args.file).expanduser()
    if path.exists() and not args.force:
        raise FileExistsError(f"档案已存在：{path}")
    save(path, default_state())
    print(f"CREATED {path}")


def cmd_show(args: argparse.Namespace) -> None:
    path = Path(args.file).expanduser()
    state = load(path)
    print(json.dumps(state, ensure_ascii=False, indent=2))


def cmd_complete(args: argparse.Namespace) -> None:
    path = Path(args.file).expanduser()
    state = load(path)
    lesson = int(args.lesson)
    if lesson < 1 or lesson > 10:
        raise ValueError("lesson 需在 1 到 10 之间。")
    state["completed_lessons"] = sorted(
        set(int(x) for x in state.get("completed_lessons", [])) | {lesson}
    )
    if args.mastered:
        state["mastered"] = unique(state.get("mastered", []) + [validate_summary(args.mastered)])
    if args.evidence:
        state["evidence"] = unique(
            (state.get("evidence", []) + [validate_summary(args.evidence)])[-10:]
        )
    if args.blocker is not None:
        state["latest_blocker"] = validate_summary(args.blocker)
    if args.next:
        state["next_lesson"] = validate_summary(args.next)
    # 完成关卡后按阶段自动建议等级；最终升级仍需教练结合复述与验收判断。
    suggested = 1 + len(state["completed_lessons"]) // 2
    state["level"] = max(int(state.get("level", 1)), min(5, suggested))
    state["practicing"] = unique([state["next_lesson"]] if state["next_lesson"] else [])
    save(path, state)
    print(f"UPDATED {path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="管理 WorkBuddy 本地学习档案")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="创建学习档案")
    init.add_argument("--file", required=True)
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=cmd_init)

    show = sub.add_parser("show", help="读取学习档案状态")
    show.add_argument("--file", required=True)
    show.set_defaults(func=cmd_show)

    complete = sub.add_parser("complete", help="记录完成关卡")
    complete.add_argument("--file", required=True)
    complete.add_argument("--lesson", required=True, type=int)
    complete.add_argument("--mastered")
    complete.add_argument("--evidence")
    complete.add_argument("--blocker")
    complete.add_argument("--next")
    complete.set_defaults(func=cmd_complete)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        args.func(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""只读审计一个 Skill 真源仓库；刻意不接受另一个仓库作为输入。"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def skill_dirs(root: Path) -> dict[str, Path]:
    if not root.is_dir():
        return {}
    return {
        child.name: child
        for child in root.iterdir()
        if child.is_dir() and (child / "SKILL.md").is_file()
    }


def symlink_paths(root: Path) -> list[str]:
    """符号链接可能绕过双库边界，因此单独列出供发布前拦截。"""
    if not root.is_dir():
        return []
    return sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_symlink()
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--role", choices=("private", "public"), required=True)
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repository = args.repository.expanduser().resolve()
    skills = skill_dirs(repository / "skills")
    links = symlink_paths(repository)
    report: dict[str, object] = {
        "role": args.role,
        "repository": {
            "path": str(repository),
            "exists": repository.is_dir(),
            "branch": git(repository, "branch", "--show-current"),
            "clean": git(repository, "status", "--porcelain") == "",
            "remote": git(repository, "remote", "get-url", "origin"),
            "head": git(repository, "rev-parse", "--short", "HEAD"),
        },
        "skill_count": len(skills),
        "symlinks": links,
        "isolation_pass": not links,
    }

    if args.runtime:
        runtime = args.runtime.expanduser().resolve()
        runtime_skills = skill_dirs(runtime)
        report["runtime"] = {
            "path": str(runtime),
            "installed_top_level": len(runtime_skills),
            "overlap": sorted(runtime_skills.keys() & skills.keys()),
        }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        repo = report["repository"]
        assert isinstance(repo, dict)
        print(f"Role: {args.role}")
        print(f"Repository: {repo['path']}")
        print(f"Skills: {len(skills)}")
        print(f"Git clean: {repo['clean']}")
        print(f"Symlinks: {len(links)}")
        print(f"Isolation: {'PASS' if not links else 'REWORK'}")
        if "runtime" in report:
            runtime_report = report["runtime"]
            assert isinstance(runtime_report, dict)
            print(f"Runtime overlap: {len(runtime_report['overlap'])}")
    return 0 if not links else 1


if __name__ == "__main__":
    raise SystemExit(main())

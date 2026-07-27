#!/usr/bin/env python3
"""只读审计 Skill 生产母库、公开镜像和运行副本的一致性。"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

RUNTIME_ENTRIES = ("SKILL.md", "agents", "references", "scripts", "assets")


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


def runtime_digest(skill: Path) -> str:
    digest = hashlib.sha256()
    files: list[Path] = []
    for entry in RUNTIME_ENTRIES:
        target = skill / entry
        if target.is_file():
            files.append(target)
        elif target.is_dir():
            files.extend(path for path in target.rglob("*") if path.is_file())
    for path in sorted(files):
        digest.update(path.relative_to(skill).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def repo_state(repo: Path) -> dict:
    return {
        "path": str(repo),
        "exists": repo.is_dir(),
        "branch": git(repo, "branch", "--show-current"),
        "clean": git(repo, "status", "--porcelain") == "",
        "remote": git(repo, "remote", "get-url", "origin"),
        "head": git(repo, "rev-parse", "--short", "HEAD"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--factory", type=Path, required=True)
    parser.add_argument("--public", type=Path)
    parser.add_argument("--workbuddy", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    factory = args.factory.expanduser().resolve()
    factory_skills = skill_dirs(factory / "skills")
    report: dict = {
        "factory": repo_state(factory),
        "counts": {
            "factory_skills": len(factory_skills),
            "packages": len(list((factory / "packages").glob("*.zip"))),
        },
    }

    if args.public:
        public = args.public.expanduser().resolve()
        public_skills = skill_dirs(public / "skills")
        shared = sorted(factory_skills.keys() & public_skills.keys())
        exact, drift = [], []
        for slug in shared:
            target = exact if runtime_digest(factory_skills[slug]) == runtime_digest(public_skills[slug]) else drift
            target.append(slug)
        report["public"] = repo_state(public)
        report["counts"]["public_original_skills"] = len(public_skills)
        report["mirror"] = {
            "exact": exact,
            "drift": drift,
            "factory_only": sorted(factory_skills.keys() - public_skills.keys()),
            "public_only": sorted(public_skills.keys() - factory_skills.keys()),
        }

    if args.workbuddy:
        runtime = args.workbuddy.expanduser().resolve()
        runtime_skills = skill_dirs(runtime)
        report["workbuddy"] = {
            "path": str(runtime),
            "installed_top_level": len(runtime_skills),
            "overlap_with_factory": sorted(runtime_skills.keys() & factory_skills.keys()),
        }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Factory skills: {report['counts']['factory_skills']}")
        print(f"Packages: {report['counts']['packages']}")
        print(f"Factory clean: {report['factory']['clean']}")
        if "mirror" in report:
            print(f"Public exact: {len(report['mirror']['exact'])}")
            print(f"Public drift: {len(report['mirror']['drift'])}")
            print(f"Factory only: {len(report['mirror']['factory_only'])}")
        if "workbuddy" in report:
            print(f"WorkBuddy top-level: {report['workbuddy']['installed_top_level']}")
            print(f"WorkBuddy overlap: {len(report['workbuddy']['overlap_with_factory'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

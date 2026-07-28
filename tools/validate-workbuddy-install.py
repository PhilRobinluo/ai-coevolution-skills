#!/usr/bin/env python3
"""Validate the public WorkBuddy install contract for every registry Skill."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLHUB_GUIDE = 'https://skillhub.cn/install/skillhub.md'
WORKBUDDY_DIR = '~/.workbuddy/skills/'


def fail(message: str) -> None:
    print(f'ERROR: {message}', file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    registry = json.loads((ROOT / 'registry.json').read_text(encoding='utf-8'))
    entries = registry.get('skills')
    if not isinstance(entries, list):
        fail('registry.json skills must be a list')

    registered_paths: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            fail('registry skill must be an object')
        slug = entry.get('name')
        status = entry.get('skillhub_status')
        version = entry.get('version')
        if not isinstance(slug, str) or not slug:
            fail('registry skill missing name')
        if not isinstance(version, str) or not version:
            fail(f'{slug}: registry version must be a non-empty string')
        relative = entry.get('path')
        if not isinstance(relative, str) or not relative:
            fail(f'{slug}: registry path must be a non-empty string')
        if relative in registered_paths:
            fail(f'duplicate registry slug: {slug}')
        registered_paths.add(relative)
        if status not in {'published', 'pending', 'pending_review'}:
            fail(f'{slug}: skillhub_status must be published, pending_review or pending')

        skill_dir = ROOT / relative
        readme = skill_dir / 'README.md'
        skill_md = skill_dir / 'SKILL.md'
        if not readme.is_file() or not skill_md.is_file():
            fail(f'{slug}: missing README.md or SKILL.md')
        readme_text = readme.read_text(encoding='utf-8')
        release_version = entry.get('release_version')
        if not isinstance(release_version, str) or not release_version:
            fail(f'{slug}: release_version must be a non-empty string')
        expected_version_line = (
            f'**当前源码版本：`{version}`**（最近 Release：`{release_version}`）'
        )
        if expected_version_line not in readme_text:
            fail(f'{slug}: README version line is stale or missing')
        # The slug label is deliberately unique so a reader can copy one authoritative value.
        if readme_text.count(f'**Skill slug：`{slug}`**') != 1:
            fail(f'{slug}: README must contain exactly one canonical Skill slug label')
        for required in ('在 WorkBuddy 安装', SKILLHUB_GUIDE, WORKBUDDY_DIR, f'`~/.workbuddy/skills/{slug}/SKILL.md`'):
            if required not in readme_text:
                fail(f'{slug}: README missing WorkBuddy install requirement: {required}')

        skill_text = skill_md.read_text(encoding='utf-8')
        frontmatter = skill_text.split('---', 2)[1]
        # WorkBuddy 加载的是标准 Agent Skill，而不是 SkillHub 的发布清单。
        # 版本以 registry/README/Release 为权威，标准 SKILL.md 不保留平台专用
        # version 字段；发布时由 build-skillhub-package.py 注入临时包。
        if any(
            line.split(':', 1)[0].strip() == 'version'
            for line in frontmatter.splitlines()
            if ':' in line
        ):
            fail(f'{slug}: standard SKILL.md must not contain top-level version')
        expected_marker = f'<!-- workbuddy-install: {status}; slug: {slug} -->'
        if expected_marker not in skill_text:
            fail(f'{slug}: SKILL.md missing status marker {expected_marker}')
        for required in (SKILLHUB_GUIDE, WORKBUDDY_DIR, f'`~/.workbuddy/skills/{slug}/SKILL.md`'):
            if required not in skill_text:
                fail(f'{slug}: SKILL.md missing WorkBuddy install requirement: {required}')

    actual_paths = {
        path.parent.relative_to(ROOT).as_posix()
        for base in ('skills', 'adapted')
        for path in (ROOT / base).glob('*/SKILL.md')
    }
    if registered_paths != actual_paths:
        fail(f'registry/path mismatch: registry={sorted(registered_paths)}, actual={sorted(actual_paths)}')
    print(f'OK: WorkBuddy install contract for {len(registered_paths)} public skills')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

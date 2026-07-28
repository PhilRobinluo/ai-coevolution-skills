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

    skill_dirs = {path.parent.name for path in (ROOT / 'skills').glob('*/SKILL.md')}
    registry_names = set()
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
        if slug in registry_names:
            fail(f'duplicate registry slug: {slug}')
        registry_names.add(slug)
        if status not in {'published', 'pending'}:
            fail(f'{slug}: skillhub_status must be published or pending')

        readme = ROOT / 'skills' / slug / 'README.md'
        skill_md = ROOT / 'skills' / slug / 'SKILL.md'
        if not readme.is_file() or not skill_md.is_file():
            fail(f'{slug}: missing README.md or SKILL.md')
        readme_text = readme.read_text(encoding='utf-8')
        # The slug label is deliberately unique so a reader can copy one authoritative value.
        if readme_text.count(f'**Skill slug：`{slug}`**') != 1:
            fail(f'{slug}: README must contain exactly one canonical Skill slug label')
        for required in ('在 WorkBuddy 安装', SKILLHUB_GUIDE, WORKBUDDY_DIR, f'`~/.workbuddy/skills/{slug}/SKILL.md`'):
            if required not in readme_text:
                fail(f'{slug}: README missing WorkBuddy install requirement: {required}')

        skill_text = skill_md.read_text(encoding='utf-8')
        skill_version = f'version: {version}'
        if skill_version not in skill_text.split('---', 2)[1]:
            fail(f'{slug}: SKILL.md version does not match registry version {version}')
        expected_marker = f'<!-- workbuddy-install: {status}; slug: {slug} -->'
        if expected_marker not in skill_text:
            fail(f'{slug}: SKILL.md missing status marker {expected_marker}')
        for required in (SKILLHUB_GUIDE, WORKBUDDY_DIR, f'`~/.workbuddy/skills/{slug}/SKILL.md`'):
            if required not in skill_text:
                fail(f'{slug}: SKILL.md missing WorkBuddy install requirement: {required}')

    if registry_names != skill_dirs:
        fail(f'registry/skills mismatch: registry={sorted(registry_names)}, skills={sorted(skill_dirs)}')
    print(f'OK: WorkBuddy install contract for {len(registry_names)} public skills')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

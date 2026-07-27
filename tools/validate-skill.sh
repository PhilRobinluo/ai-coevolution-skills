#!/usr/bin/env bash
set -euo pipefail

skill_dir="${1:-}"

if [[ -z "$skill_dir" ]]; then
  echo "Usage: tools/validate-skill.sh skills/<skill-name>" >&2
  exit 2
fi

if [[ ! -d "$skill_dir" ]]; then
  echo "Not a directory: $skill_dir" >&2
  exit 1
fi

if [[ ! -f "$skill_dir/SKILL.md" ]]; then
  echo "Missing SKILL.md in $skill_dir" >&2
  exit 1
fi

if ! grep -q '^---$' "$skill_dir/SKILL.md"; then
  echo "SKILL.md appears to be missing YAML frontmatter delimiters" >&2
  exit 1
fi

if ! grep -q '^name:' "$skill_dir/SKILL.md"; then
  echo "SKILL.md missing name field" >&2
  exit 1
fi

if ! grep -q '^description:' "$skill_dir/SKILL.md"; then
  echo "SKILL.md missing description field" >&2
  exit 1
fi

if grep -R -nE '(OPENAI_API_KEY|ANTHROPIC_API_KEY|WECHAT_APP_SECRET|/Users/philrobin|xwechat_files|notion\\.site|password[[:space:]]*[:=]|secret[[:space:]]*[:=]|token[[:space:]]*[:=]|cookie[[:space:]]*[:=])' "$skill_dir"; then
  echo "Potential private/secret content found; review before publishing." >&2
  exit 1
fi

echo "OK: $skill_dir"

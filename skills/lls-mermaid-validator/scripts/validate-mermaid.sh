#!/usr/bin/env bash
set -euo pipefail
file=${1:?用法: validate-mermaid.sh <diagram.mmd>}
command -v npx >/dev/null || { echo "需要 Node.js 与 npx" >&2; exit 2; }
out=$(mktemp -t mermaid-XXXXXX.svg)
trap 'rm -f "$out"' EXIT
npx --yes @mermaid-js/mermaid-cli -i "$file" -o "$out" >/dev/null
echo "PASS: $file"

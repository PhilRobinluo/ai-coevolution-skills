#!/usr/bin/env bash
set -euo pipefail
file=""; output=""; report=""; dry_run=false
while [[ $# -gt 0 ]]; do case "$1" in --output) output=${2:?}; shift 2;; --report) report=${2:?}; shift 2;; --dry-run) dry_run=true; shift;; -h|--help) echo 'validate-mermaid.sh diagram.mmd [--output diagram.svg] [--report report.json] [--dry-run]'; exit 0;; *) [[ -z "$file" ]] && { file=$1; shift; } || { echo "未知参数 $1" >&2; exit 2; };; esac; done
[[ -n "$file" && -f "$file" ]] || { echo '缺少可读 diagram.mmd' >&2; exit 2; }
output=${output:-"${file%.*}.validated.svg"}
[[ ! -e "$output" ]] || { echo '输出已存在，请更换路径' >&2; exit 3; }
if command -v mmdc >/dev/null 2>&1; then cmd=(mmdc -i "$file" -o "$output")
elif command -v npx >/dev/null 2>&1 && npx --no-install mmdc --version >/dev/null 2>&1; then cmd=(npx --no-install mmdc -i "$file" -o "$output")
else echo '未找到本地 Mermaid CLI；请先安装 @mermaid-js/mermaid-cli' >&2; exit 4; fi
if $dry_run; then printf 'DRY_RUN '; printf '%q ' "${cmd[@]}"; echo; exit 0; fi
"${cmd[@]}" >/dev/null
[[ -s "$output" ]] || { echo '渲染未产生非空 SVG' >&2; exit 5; }
if [[ -n "$report" ]]; then mkdir -p "$(dirname "$report")"; printf '{"ok":true,"input":"%s","output":"%s","bytes":%s}\n' "$file" "$output" "$(wc -c < "$output" | tr -d ' ')" > "$report"; fi
echo "PASS: $file -> $output"

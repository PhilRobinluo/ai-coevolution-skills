#!/usr/bin/env bash
set -euo pipefail

mode="region"
out=""
delay="0"
dry_run="false"
force="false"

usage() {
  cat <<'EOF'
用法：capture.sh [--mode region|window|full] [--output FILE.png] [--delay SECONDS] [--dry-run] [--force]

默认交互选择区域，并保存到 assets/screenshot-时间戳.png。
--force 不直接丢弃旧文件：成功截图后会先把旧文件改名为 .bak-时间戳。
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode) mode=${2:?--mode 缺少值}; shift 2 ;;
    --output) out=${2:?--output 缺少值}; shift 2 ;;
    --delay) delay=${2:?--delay 缺少值}; shift 2 ;;
    --dry-run) dry_run="true"; shift ;;
    --force) force="true"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "未知参数：$1" >&2; usage >&2; exit 2 ;;
  esac
done

case "$mode" in region|window|full) ;; *) echo "--mode 只能是 region、window 或 full" >&2; exit 2 ;; esac
[[ "$delay" =~ ^[0-9]+$ ]] || { echo "--delay 必须是非负整数" >&2; exit 2; }
out=${out:-"assets/screenshot-$(date +%Y%m%d-%H%M%S).png"}
[[ "${out##*.}" == "png" ]] || { echo "输出必须是 .png" >&2; exit 2; }
if [[ -e "$out" && "$force" != "true" ]]; then
  echo "输出已存在；请更换路径，或显式使用 --force（旧文件会备份）" >&2
  exit 3
fi

command -v screencapture >/dev/null 2>&1 || { echo "未找到 macOS screencapture" >&2; exit 4; }
mkdir -p "$(dirname "$out")"
tmp="${out%.png}.capturing-$$.png"
args=(-x)
case "$mode" in
  region) args=(-i -x) ;;
  window) args=(-W -o -x) ;;
  full) args=(-x) ;;
esac
if [[ "$delay" != "0" ]]; then args+=(-T "$delay"); fi
args+=("$tmp")

if [[ "$dry_run" == "true" ]]; then
  printf 'DRY_RUN mode=%s output=%s delay=%s command=' "$mode" "$out" "$delay"
  printf '%q ' screencapture "${args[@]}"
  printf '\n'
  exit 0
fi

# 先写临时文件并核对非空，再原子换入目标；用户取消交互截图时不会留下“成功”假象。
screencapture "${args[@]}"
[[ -s "$tmp" ]] || { echo "未生成截图，可能已取消" >&2; exit 5; }
if [[ -e "$out" ]]; then
  backup="${out}.bak-$(date +%Y%m%d-%H%M%S)"
  mv "$out" "$backup"
  echo "backup=$backup"
fi
mv "$tmp" "$out"
printf 'output=%s\nmode=%s\n' "$out" "$mode"

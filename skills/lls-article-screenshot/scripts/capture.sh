#!/usr/bin/env bash
set -euo pipefail
mode=${1:-region}; out=${2:-assets/screenshot-$(date +%Y%m%d-%H%M%S).png}
mkdir -p "$(dirname "$out")"
case "$mode" in region) screencapture -i -x "$out";; window) screencapture -W -o -x "$out";; full) screencapture -x "$out";; *) echo "mode: region|window|full" >&2; exit 2;; esac
[[ -f "$out" ]] && echo "$out"

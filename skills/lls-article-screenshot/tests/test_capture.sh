#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
tmp=$(mktemp -d)
mkdir -p "$tmp/bin"
cat > "$tmp/bin/screencapture" <<'EOF'
#!/usr/bin/env bash
out=${!#}
printf 'fake-png' > "$out"
EOF
chmod +x "$tmp/bin/screencapture"
PATH="$tmp/bin:$PATH" "$root/scripts/capture.sh" --mode full --output "$tmp/out.png"
[[ -s "$tmp/out.png" ]]
PATH="$tmp/bin:$PATH" "$root/scripts/capture.sh" --mode region --output "$tmp/dry.png" --dry-run | grep -q DRY_RUN
if PATH="$tmp/bin:$PATH" "$root/scripts/capture.sh" --mode bad --output "$tmp/x.png" 2>/dev/null; then exit 1; fi
echo PASS

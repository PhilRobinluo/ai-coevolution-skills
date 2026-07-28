#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd); tmp=$(mktemp -d); mkdir -p "$tmp/bin"
cat > "$tmp/bin/mmdc" <<'EOF'
#!/usr/bin/env bash
while [[ $# -gt 0 ]]; do case "$1" in -o) out=$2; shift 2;; *) shift;; esac; done
printf '<svg></svg>' > "$out"
EOF
chmod +x "$tmp/bin/mmdc"; echo 'flowchart LR; A-->B' > "$tmp/a.mmd"
PATH="$tmp/bin:$PATH" "$root/scripts/validate-mermaid.sh" "$tmp/a.mmd" --output "$tmp/a.svg" --report "$tmp/r.json"
[[ -s "$tmp/a.svg" ]] && grep -q '"ok":true' "$tmp/r.json"
echo PASS

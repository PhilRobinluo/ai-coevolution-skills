#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SLUG="${1:-}"
VERSION="${2:-}"
OUTPUT="${3:-$ROOT/dist}"

if [[ ! "$SLUG" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "invalid slug: $SLUG" >&2
  exit 2
fi
if [[ ! "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "invalid semantic version: $VERSION" >&2
  exit 2
fi

# 输入版本与目录必须来自 registry，避免漏掉 adapted/ 或手工触发错误 tag。
SKILL_REL="$(python3 - "$ROOT/registry.json" "$SLUG" "$VERSION" <<'PY'
import json
import sys
from pathlib import Path

registry = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
slug, requested = sys.argv[2], sys.argv[3]
item = next((item for item in registry["skills"] if item["name"] == slug), None)
if item is None:
    raise SystemExit(f"{slug}: not registered")
if item["version"] != requested:
    raise SystemExit(f"{slug}: registry version {item['version']} != requested {requested}")
print(item["path"])
PY
)"
SKILL_DIR="$ROOT/$SKILL_REL"
"$ROOT/tools/validate-skill.sh" "$SKILL_DIR"

STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$STAGE/$SLUG" "$OUTPUT"

# ZIP 只取公开分享库的白名单内容；许可证文件显式加入，使离线下载包也能独立说明权利边界。
for entry in SKILL.md agents references scripts assets ORIGIN.md LICENSE.upstream; do
  if [[ -e "$SKILL_DIR/$entry" ]]; then
    cp -R "$SKILL_DIR/$entry" "$STAGE/$SLUG/"
  fi
done
cp "$ROOT/LICENSE" "$STAGE/$SLUG/LICENSE.md"
cp -R "$ROOT/LICENSES" "$STAGE/$SLUG/"
cp "$ROOT/ADDITIONAL-PERMISSIONS.md" "$STAGE/$SLUG/"
cp "$ROOT/COMMERCIAL-LICENSE.md" "$STAGE/$SLUG/"
cp "$ROOT/THIRD_PARTY_NOTICES.md" "$STAGE/$SLUG/"

PACKAGE="$OUTPUT/$SLUG-$VERSION.zip"
if [[ -f "$PACKAGE" ]]; then
  unlink "$PACKAGE"
fi
(
  cd "$STAGE"
  zip -Xqr "$PACKAGE" "$SLUG" \
    -x '*/.DS_Store' \
    -x '*/__pycache__/*' \
    -x '*.pyc'
)
(
  cd "$OUTPUT"
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$SLUG-$VERSION.zip" > "$SLUG-$VERSION.zip.sha256"
  else
    shasum -a 256 "$SLUG-$VERSION.zip" > "$SLUG-$VERSION.zip.sha256"
  fi
)
unzip -tq "$PACKAGE"
for required in \
  "$SLUG/SKILL.md" \
  "$SLUG/LICENSE.md" \
  "$SLUG/LICENSES/CC-BY-NC-SA-4.0.txt" \
  "$SLUG/LICENSES/PolyForm-Noncommercial-1.0.0.txt" \
  "$SLUG/ADDITIONAL-PERMISSIONS.md" \
  "$SLUG/COMMERCIAL-LICENSE.md"; do
  unzip -Z1 "$PACKAGE" "$required" >/dev/null 2>&1 || {
    echo "package missing: $required" >&2
    exit 1
  }
done
if [[ -f "$SKILL_DIR/ORIGIN.md" ]]; then
  for required in "$SLUG/ORIGIN.md" "$SLUG/LICENSE.upstream"; do
    unzip -Z1 "$PACKAGE" "$required" >/dev/null 2>&1 || {
      echo "adapted package missing: $required" >&2
      exit 1
    }
  done
fi
echo "Created: $PACKAGE"

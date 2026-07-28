from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.index("\n---\n", 4)
    return yaml.safe_load(text[4:end])


class ChannelAdapterTest(unittest.TestCase):
    def test_build_and_normalize_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            tmp_path = Path(raw)
            source = tmp_path / "source"
            source.mkdir()
            (source / "SKILL.md").write_text(
                "---\n"
                "name: demo-skill\n"
                "description: 用于测试渠道字段隔离的演示 Skill。\n"
                "metadata:\n"
                "  short-description: 渠道适配测试\n"
                "---\n\n# Demo\n",
                encoding="utf-8",
            )
            package = tmp_path / "package"
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools/build-skillhub-package.py"),
                    str(source),
                    str(package),
                    "--version",
                    "1.2.3",
                    "--display-name",
                    "演示 Skill",
                    "--summary",
                    "验证平台字段只进入临时包",
                ],
                check=True,
            )
            built = frontmatter(package / "SKILL.md")
            self.assertEqual(built["slug"], "demo-skill")
            self.assertEqual(built["version"], "1.2.3")
            self.assertNotIn("slug", frontmatter(source / "SKILL.md"))

            (package / "_meta.json").write_text(
                json.dumps({"slug": "demo-skill", "version": "1.2.3"}), encoding="utf-8"
            )
            backup_root = tmp_path / "backups"
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools/normalize-workbuddy-frontmatter.py"),
                    str(package),
                    "--backup-root",
                    str(backup_root),
                    "--apply",
                ],
                check=True,
            )
            normalized = frontmatter(package / "SKILL.md")
            self.assertNotIn("slug", normalized)
            self.assertNotIn("version", normalized)
            self.assertEqual(normalized["name"], "demo-skill")
            self.assertTrue(list(backup_root.rglob("SKILL.md")))


if __name__ == "__main__":
    unittest.main()

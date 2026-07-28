import json
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "learning_profile.py"


class LearningProfileTests(unittest.TestCase):
    def run_cli(self, *args: str, ok: bool = True) -> subprocess.CompletedProcess:
        result = subprocess.run(
            ["python3", str(SCRIPT), *args],
            text=True,
            capture_output=True,
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def test_init_show_complete(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile = Path(tmp) / "profile.md"
            self.run_cli("init", "--file", str(profile))
            shown = self.run_cli("show", "--file", str(profile))
            self.assertEqual(json.loads(shown.stdout)["level"], 1)

            self.run_cli(
                "complete",
                "--file",
                str(profile),
                "--lesson",
                "1",
                "--mastered",
                "会填写任务卡",
                "--evidence",
                "结构化文档已打开",
                "--next",
                "第2关：会议纪要",
            )
            state = json.loads(self.run_cli("show", "--file", str(profile)).stdout)
            self.assertEqual(state["completed_lessons"], [1])
            self.assertIn("会填写任务卡", state["mastered"])
            self.assertEqual(state["next_lesson"], "第2关：会议纪要")

    def test_rejects_credential_like_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile = Path(tmp) / "profile.md"
            self.run_cli("init", "--file", str(profile))
            result = self.run_cli(
                "complete",
                "--file",
                str(profile),
                "--lesson",
                "1",
                "--evidence",
                "api_" + "key=EXAMPLE_VALUE",
                ok=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("凭证类内容", result.stdout)


if __name__ == "__main__":
    unittest.main()

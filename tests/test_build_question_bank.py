import json
import tempfile
import unittest
from pathlib import Path

from tools.build_question_bank import build_questions, write_questions


class BuildQuestionBankTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)

        sql_project = self.root / "exercises" / "01-sample-sql"
        sql_project.mkdir(parents=True)
        (sql_project / "README.md").write_text(
            "# 1. Sample SQL\n\n> Medium-1 15 mins\n\n## 题目\n\nReturn rows.\n\n## Database Schema\n\nA sample table.\n\n## 解析\n\nUse a filter.\n",
            encoding="utf-8",
        )
        (sql_project / "solution.sql").write_text("SELECT * FROM rows;\n", encoding="utf-8")
        (sql_project / "test_solution.py").write_text("pass\n", encoding="utf-8")

        programming_project = self.root / "programming-projects" / "01-sample-programming"
        programming_project.mkdir(parents=True)
        (programming_project / "README.md").write_text(
            "# 1. Sample Programming\n\n> 难度与建议用时：Easy-1 10 mins\n\narray\n\n## Problem Statement\n\nReturn an item.\n\n## Python 解法\n\n### 思路\n\nScan the list.\n\n### 复杂度\n\n- 时间复杂度：`O(n)`\n",
            encoding="utf-8",
        )
        (programming_project / "solution.py").write_text("def solution():\n    return 1\n", encoding="utf-8")
        (programming_project / "test_solution.py").write_text("pass\n", encoding="utf-8")

    def tearDown(self):
        self.tempdir.cleanup()

    def test_build_questions_discovers_sql_and_programming_projects(self):
        records = build_questions(self.root)

        self.assertEqual([(record["domain"], record["number"]) for record in records], [("sql", 1), ("programming", 1)])
        self.assertEqual(records[0]["answerLanguage"], "sql")
        self.assertEqual(records[1]["answerLanguage"], "python")
        self.assertEqual(records[0]["explanationMarkdown"], "Use a filter.")
        self.assertIn("Database Schema", records[0]["promptMarkdown"])
        self.assertIn("数组", records[1]["topics"])

    def test_write_questions_emits_valid_json(self):
        output = self.root / "site" / "data" / "questions.json"

        write_questions(self.root, output)

        payload = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(payload["questions"][0]["title"], "Sample SQL")
        self.assertEqual(payload["questions"][1]["answer"], "def solution():\n    return 1")

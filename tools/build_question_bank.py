#!/usr/bin/env python3
"""Build browser-ready question data from the repository's canonical projects."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_RE = re.compile(r"^(?P<number>\d+)-(?P<slug>.+)$")
TITLE_RE = re.compile(r"^#\s+(?P<number>\d+)\.\s+(?P<title>.+)$", re.MULTILINE)
META_RE = re.compile(r"^>\s*(?:难度与建议用时：)?(?P<meta>.+)$", re.MULTILINE)
HEADING_RE = re.compile(r"^##\s+(?P<name>.+?)\s*$", re.MULTILINE)


def section(markdown: str, name: str) -> str:
    """Return an H2 section body without its heading."""
    match = re.search(rf"^##\s+{re.escape(name)}\s*$", markdown, re.MULTILINE)
    if not match:
        return ""
    next_heading = HEADING_RE.search(markdown, match.end())
    return markdown[match.end() : next_heading.start() if next_heading else len(markdown)].strip()


def between_sections(markdown: str, start_name: str, end_name: str | None = None) -> str:
    """Extract content between named headings, preserving nested H2 headings."""
    start = re.search(rf"^##\s+{re.escape(start_name)}\s*$", markdown, re.MULTILINE)
    if not start:
        return ""
    if not end_name:
        return markdown[start.end() :].strip()
    end = re.search(rf"^##\s+{re.escape(end_name)}\s*$", markdown[start.end() :], re.MULTILINE)
    return markdown[start.end() : start.end() + end.start() if end else len(markdown)].strip()


def first_nonempty_line(markdown: str) -> str:
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def parse_metadata(readme: str, fallback_number: int, fallback_slug: str) -> tuple[int, str, str, str]:
    title_match = TITLE_RE.search(readme)
    if title_match:
        number = int(title_match.group("number"))
        title = title_match.group("title").strip()
    else:
        number = fallback_number
        title = fallback_slug.replace("-", " ").title()
    meta_match = META_RE.search(readme)
    meta = meta_match.group("meta").strip() if meta_match else ""
    difficulty_match = re.search(r"\b(Easy|Medium|Hard)(?:-\d+)?\b", meta, re.IGNORECASE)
    duration_match = re.search(r"\b\d+\s*mins?\b", meta, re.IGNORECASE)
    difficulty = difficulty_match.group(0).title() if difficulty_match else "未标注"
    duration = duration_match.group(0) if duration_match else ""
    return number, title, difficulty, duration


def derive_topics(domain: str, slug: str, readme: str) -> list[str]:
    # Programming prompts often mention broad concepts (for example "sequence")
    # incidentally. Their project labels and preamble are the stable taxonomy source.
    preamble = readme.split("##", 1)[0] if domain == "programming" else readme
    haystack = f"{slug} {preamble}".lower()
    candidates = (
        [
            ("recursive", "递归 CTE"),
            ("window", "窗口函数"),
            ("aggregate", "聚合"),
            ("group by", "聚合"),
            ("subquery", "子查询"),
            ("date", "日期"),
            ("join", "JOIN"),
        ]
        if domain == "sql"
        else [
            ("array", "数组"),
            ("string", "字符串"),
            ("linked list", "链表"),
            ("linked-list", "链表"),
            ("tree", "树"),
            ("graph", "图"),
            ("substring", "字符串"),
            ("sequence", "动态规划"),
            ("subarray", "数组"),
            ("sort", "排序"),
        ]
    )
    topics = [label for needle, label in candidates if needle in haystack]
    return list(dict.fromkeys(topics)) or (["SQL 查询"] if domain == "sql" else ["基础编程"])


def project_record(project: Path, domain: str, solution_name: str, root: Path) -> dict[str, object] | None:
    match = PROJECT_RE.match(project.name)
    readme_path = project / "README.md"
    solution_path = project / solution_name
    if not match or not readme_path.is_file() or not solution_path.is_file():
        return None

    readme = readme_path.read_text(encoding="utf-8")
    number, title, difficulty, duration = parse_metadata(readme, int(match.group("number")), match.group("slug"))
    if domain == "sql":
        prompt = between_sections(readme, "题目", "解析")
        explanation = between_sections(readme, "解析", "SQL 答案")
        notes = between_sections(readme, "运行测试")
    else:
        prompt = between_sections(readme, "Problem Statement", "Python 解法") or readme
        explanation = between_sections(readme, "Python 解法")
        notes = "\n\n".join(
            part for part in (section(explanation, heading) for heading in ("正确性说明", "复杂度", "代码与测试")) if part
        )

    answer = solution_path.read_text(encoding="utf-8").strip()
    test_path = project / "test_solution.py"
    relative = lambda path: str(path.relative_to(root))
    return {
        "id": f"{domain}-{number:02d}",
        "domain": domain,
        "number": number,
        "title": title,
        "difficulty": difficulty,
        "duration": duration,
        "topics": derive_topics(domain, match.group("slug"), readme),
        "promptMarkdown": prompt.strip(),
        "explanationMarkdown": explanation.strip(),
        "answer": answer,
        "answerLanguage": "sql" if domain == "sql" else "python",
        "notesMarkdown": notes.strip(),
        "paths": {
            "readme": relative(readme_path),
            "solution": relative(solution_path),
            "test": relative(test_path) if test_path.is_file() else "",
        },
    }


def discover_projects(directory: Path, domain: str, solution_name: str, root: Path) -> list[dict[str, object]]:
    if not directory.is_dir():
        return []
    records = [project_record(path, domain, solution_name, root) for path in directory.iterdir() if path.is_dir()]
    return [record for record in records if record is not None]


def build_questions(root: Path) -> list[dict[str, object]]:
    sql = discover_projects(root / "exercises", "sql", "solution.sql", root)
    programming = discover_projects(root / "programming-projects", "programming", "solution.py", root)
    domain_order = {"sql": 0, "programming": 1}
    return sorted([*sql, *programming], key=lambda record: (domain_order[record["domain"]], record["number"]))


def write_questions(root: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {"questions": build_questions(root)}
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "site" / "data" / "questions.json")
    arguments = parser.parse_args()
    write_questions(ROOT, arguments.output)

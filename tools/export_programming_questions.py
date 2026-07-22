#!/usr/bin/env python3
"""Split programming.md into one normalized Markdown file per question."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "programming.md"
OUTPUT = ROOT / "programming-questions"

TITLE_RE = re.compile(
    r"^(?:#\s*)?(?P<number>\d+)\.\s*(?P<title>.+?)\s*--\s*(?P<meta>.+?)\s*$"
)


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "question"


def normalize_body(lines: list[str]) -> str:
    """Normalize heading levels and remove coding-platform chrome."""
    cleaned: list[str] = []
    skipping_languages = False

    for line in lines:
        stripped = line.strip()
        if stripped == "Languages Available":
            skipping_languages = True
            continue
        if skipping_languages:
            if stripped == "AddPreview":
                skipping_languages = False
            continue
        if stripped == "AddPreview":
            continue

        # The question title is H1, so all source headings belong below it.
        if line.startswith("#"):
            line = "#" + line
        cleaned.append(line.rstrip())

    text = "\n".join(cleaned).strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def parse_questions(text: str) -> list[tuple[int, str, str, list[str]]]:
    questions: list[tuple[int, str, str, list[str]]] = []
    current: tuple[int, str, str] | None = None
    body: list[str] = []

    for line in text.splitlines():
        match = TITLE_RE.match(line)
        if match and 1 <= int(match.group("number")) <= 85:
            if current is not None:
                questions.append((*current, body))
            current = (
                int(match.group("number")),
                match.group("title").strip(),
                match.group("meta").strip(),
            )
            body = []
        elif current is not None:
            body.append(line)

    if current is not None:
        questions.append((*current, body))
    return questions


def main() -> None:
    questions = parse_questions(SOURCE.read_text(encoding="utf-8"))
    numbers = [number for number, _, _, _ in questions]
    expected = list(range(1, 86))
    if numbers != expected:
        raise SystemExit(f"Expected questions 1..85, found: {numbers}")

    OUTPUT.mkdir(exist_ok=True)
    index = ["# Programming Interview Questions", ""]
    for number, title, meta, body_lines in questions:
        filename = f"{number:02d}-{slugify(title)}.md"
        content = (
            f"# {number}. {title}\n\n"
            f"> 难度与建议用时：{meta}\n\n"
            f"{normalize_body(body_lines)}\n"
        )
        (OUTPUT / filename).write_text(content, encoding="utf-8")
        index.append(f"{number}. [{title}]({filename})")

    (OUTPUT / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"Exported {len(questions)} questions to {OUTPUT}")


if __name__ == "__main__":
    main()

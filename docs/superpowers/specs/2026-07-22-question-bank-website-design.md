# Question Bank Website Design

## Goal

Create a static, reader-first website for all SQL and programming interview questions in this repository. Each question must display its prompt, explanation, answer, and supporting material without requiring a server at runtime.

## Chosen Approach

Use a build-time Python generator to scan the canonical question projects and create one browser-ready JSON data file. This avoids a hand-maintained frontend question list, keeps source Markdown authoritative, and makes deployment a static-files-only operation.

Two alternatives were considered:

1. Read Markdown files directly in the browser. This would couple the UI to repository paths and require numerous runtime requests.
2. Hand-author a frontend question dataset. This is quick initially but inevitably becomes stale when questions change.

The generated data approach is selected because it preserves one source of truth while retaining a fast, client-only reader.

## Information Architecture

The app has a persistent left navigation and a focused reading workspace.

- The compact header contains global search, a source count, and a reset control.
- The sidebar groups the library into SQL and programming domains, then into derived topic groups. It offers domain, difficulty, and topic filters.
- The question list shows ordered items within the current filtered group and keeps the selected item visible.
- The reader shows a metadata strip, the prompt, approach/explanation, reference answer, complexity or test notes, and links to the original project files.
- On narrow screens, the navigation becomes a collapsible overlay so the reader remains usable.

## Content Model

Each generated question record contains:

- `id`, `domain`, `number`, `title`, `difficulty`, `duration`, `topics`;
- `promptMarkdown`, `explanationMarkdown`, `answer`, `answerLanguage`, `notesMarkdown`;
- canonical repository paths for README, solution, and tests.

SQL questions are discovered from `exercises/*/README.md` and `solution.sql`. Programming questions are discovered from `programming-projects/*/README.md` and `solution.py`. The generator obtains title and metadata from the normalized README, divides content by its existing heading structure, and derives conservative topics from directory names and known prompt terms. Empty optional sections remain valid empty strings.

## Rendering And Interaction

Vanilla HTML, CSS, and browser JavaScript are used so no package-manager setup is required. A small Markdown renderer supports the repository's headings, paragraphs, lists, code blocks, tables, block quotes, horizontal rules, and inline code while escaping source HTML. The reader state lives in the URL hash and query string: selected question is hash-addressable and active filters/search can be shared.

Search matches title, topics, domain, and the prompt. Filters combine with AND semantics. The visible result count and an accessible empty state update immediately.

## Verification

- Python unit tests cover discovery, markdown section splitting, metadata parsing, and JSON output for fixtures representing one SQL and one programming question.
- The generator runs against the full repository and produces a valid `site/data/questions.json` with all discoverable questions.
- A browser smoke test verifies the generated page loads, search narrows results, a question can be selected, and its answer section renders.

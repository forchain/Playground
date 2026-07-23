# Question Bank Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a static reader-first website that indexes every SQL and programming question project with its prompt, explanation, and answer.

**Architecture:** A Python build script scans canonical project files and emits `site/data/questions.json`. The dependency-free static frontend fetches that file and renders filterable navigation plus an accessible question reader, using URL state for selected question and filters.

**Tech Stack:** Python 3 standard library, HTML, CSS, browser JavaScript, Playwright for UI smoke verification.

---

### Task 1: Add Question Data Generator Tests

**Files:**
- Create: `tests/test_build_question_bank.py`
- Create: `tools/build_question_bank.py`

- [ ] **Step 1: Write the failing generator tests**

```python
def test_build_questions_discovers_sql_and_programming_projects(tmp_path):
    records = build_questions(fixture_root)
    assert [(record["domain"], record["number"]) for record in records] == [("sql", 1), ("programming", 1)]
    assert records[0]["answerLanguage"] == "sql"
    assert records[1]["answerLanguage"] == "python"

def test_write_questions_emits_valid_json(tmp_path):
    output = tmp_path / "questions.json"
    write_questions(fixture_root, output)
    assert json.loads(output.read_text(encoding="utf-8"))["questions"][0]["title"] == "Sample SQL"
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m unittest -v tests.test_build_question_bank`

Expected: FAIL because `tools.build_question_bank` does not exist.

- [ ] **Step 3: Implement question discovery and JSON writing**

```python
def build_questions(root: Path) -> list[dict[str, object]]:
    sql = discover_projects(root / "exercises", "sql", "solution.sql")
    programming = discover_projects(root / "programming-projects", "programming", "solution.py")
    return sorted([*sql, *programming], key=lambda record: (record["domain"], record["number"]))

def write_questions(root: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"questions": build_questions(root)}, ensure_ascii=False), encoding="utf-8")
```

- [ ] **Step 4: Run generator tests**

Run: `python3 -m unittest -v tests.test_build_question_bank`

Expected: PASS.

### Task 2: Generate The Website Dataset

**Files:**
- Modify: `tools/build_question_bank.py`
- Create: `site/data/questions.json`

- [ ] **Step 1: Add a command-line entry point and topic derivation**

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "site" / "data" / "questions.json")
    arguments = parser.parse_args()
    write_questions(ROOT, arguments.output)
```

- [ ] **Step 2: Generate the complete dataset**

Run: `python3 tools/build_question_bank.py`

Expected: `site/data/questions.json` contains a `questions` list with at least 117 records.

- [ ] **Step 3: Validate the output contract**

Run: `python3 -c 'import json; d=json.load(open("site/data/questions.json")); assert len(d["questions"]) >= 117; assert all(q["answer"] for q in d["questions"]); print(len(d["questions"]))'`

Expected: prints the question count without an assertion failure.

### Task 3: Implement The Static Reader UI

**Files:**
- Create: `site/index.html`
- Create: `site/styles.css`
- Create: `site/app.js`

- [ ] **Step 1: Create the semantic reader shell**

```html
<header class="app-header"><a class="brand" href="#">题库</a><label><span class="sr-only">搜索题目</span><input id="search" type="search"></label></header>
<main class="library-layout"><aside class="library-nav" aria-label="题目导航"></aside><article id="reader" tabindex="-1"></article></main>
```

- [ ] **Step 2: Implement responsive visual hierarchy**

```css
.library-layout { display: grid; grid-template-columns: minmax(16rem, 22rem) minmax(0, 1fr); min-height: calc(100vh - 4rem); }
@media (max-width: 48rem) { .library-layout { grid-template-columns: 1fr; } .library-nav { display: none; } .library-nav.is-open { display: block; } }
```

- [ ] **Step 3: Implement loading, URL state, filtering, and reader rendering**

```javascript
const state = { query: "", domain: "all", topic: "all", difficulty: "all", selectedId: "" };
const visibleQuestions = () => questions.filter(matchesActiveFilters);
window.addEventListener("hashchange", selectFromLocation);
```

- [ ] **Step 4: Build the data and manually verify static serving**

Run: `python3 tools/build_question_bank.py && python3 -m http.server 4173 --directory site`

Expected: the page loads at `http://localhost:4173` and selecting a question displays its answer.

### Task 4: Verify The Full User Workflow

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add local build and serve commands**

```markdown
## Question Bank Website

```bash
python3 tools/build_question_bank.py
python3 -m http.server 4173 --directory site
```
```

- [ ] **Step 2: Run tests and generate production data**

Run: `python3 -m unittest -v tests.test_build_question_bank && python3 tools/build_question_bank.py`

Expected: unit tests pass and `site/data/questions.json` is regenerated.

- [ ] **Step 3: Execute the browser smoke test**

Run: `npx playwright test`

Expected: the page renders non-empty navigation, searching for `customer` narrows the list, and opening a result reveals a reference answer section.

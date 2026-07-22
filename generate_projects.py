#!/usr/bin/env python3
"""Generate standalone SQLite exercises from the imperfect source document."""

from __future__ import annotations

import re
import shutil
import sqlite3
from pathlib import Path


ROOT = Path(__file__).parent
SOURCE = ROOT / "SQL.md"
OUTPUT = ROOT / "exercises"


SOLUTIONS = {
    1: """SELECT c.customer_name, o.order_total
FROM customers AS c JOIN orders AS o ON o.customer_id = c.customer_id
WHERE o.order_date >= '2023-01-01' AND o.order_date < '2024-01-01'
ORDER BY c.customer_name, o.order_total;""",
    2: "SELECT book_name FROM books WHERE book_name LIKE 'L%' ORDER BY book_id;",
    3: """SELECT COUNT(*) FROM books_issued AS bi
JOIN users AS u ON u.user_id = bi.user_id
WHERE u.name = 'Willian Mathew';""",
    4: """SELECT a.account_name FROM accounts AS a
JOIN city AS c ON c.city_id = a.city_id
JOIN transactions AS t ON t.account_id = a.account_id
WHERE a.account_type = 'Savings' AND c.name = 'New York' AND t.transaction_type = 'Credit'
GROUP BY a.account_id, a.account_name HAVING COUNT(*) > 1 ORDER BY a.account_id;""",
    5: "SELECT SUM(amount) FROM transactions WHERE transaction_type = 'Credit' AND date = '2017-05-27';",
    6: "SELECT SUM(amount) FROM transactions WHERE date BETWEEN '2017-05-01' AND '2017-05-31';",
    7: "SELECT title FROM books ORDER BY title;\n\nSELECT author FROM books ORDER BY author;",
    8: """SELECT DISTINCT b.book_name FROM books AS b JOIN books_issued AS bi ON bi.book_id = b.book_id
WHERE bi.date_of_issue BETWEEN '2017-02-01' AND '2022-02-28' ORDER BY b.book_id;""",
    9: """SELECT b.title FROM books AS b JOIN authors AS a ON a.author_id = b.author_id
WHERE b.year_published > 2000 AND a.author_name LIKE '%a'
ORDER BY a.author_name, b.title;""",
    10: """SELECT b.book_name, u.name FROM books_issued AS bi
JOIN books AS b ON b.book_id = bi.book_id JOIN users AS u ON u.user_id = bi.user_id
ORDER BY u.user_id, bi.issue_id;""",
    11: """SELECT b.book_name FROM books AS b LEFT JOIN books_issued AS bi ON bi.book_id = b.book_id
WHERE bi.book_id IS NULL ORDER BY b.book_id;""",
    12: """SELECT c.name FROM customers AS c JOIN orders AS o ON o.customer_id = c.id
GROUP BY c.id, c.name ORDER BY COUNT(*) DESC, c.id LIMIT 1;""",
    13: """SELECT s.student_name FROM students AS s JOIN courses AS c ON c.student_id = s.student_id
GROUP BY s.student_id, s.student_name HAVING COUNT(*) > 1 AND MIN(c.grade) >= 80
ORDER BY s.student_name;""",
    14: """SELECT e.emp_name FROM employees AS e JOIN employees AS m ON m.emp_id = e.manager_id
WHERE e.salary > m.salary ORDER BY e.emp_name;""",
    15: """SELECT u.username FROM users AS u
WHERE NOT EXISTS (SELECT 1 FROM posts AS p JOIN users AS h ON h.user_id = p.user_id
                  WHERE h.username = 'Harry' AND NOT EXISTS
                    (SELECT 1 FROM likes AS l WHERE l.user_id = u.user_id AND l.post_id = p.post_id))
AND EXISTS (SELECT 1 FROM posts AS p JOIN users AS h ON h.user_id = p.user_id WHERE h.username = 'Harry')
ORDER BY u.user_id;""",
    16: """SELECT u.region, u.user_name, SUM(t.amount) AS total_spending,
MAX(t.transaction_date) AS last_transaction_date
FROM users AS u JOIN transactions AS t ON t.user_id = u.user_id
GROUP BY u.user_id, u.region, u.user_name HAVING SUM(t.amount) > 10000
ORDER BY u.region, total_spending DESC, last_transaction_date DESC;""",
    17: """SELECT d.dept_name, SUM(e.amount) AS total_expenses,
SUM(e.amount) - d.annual_budget AS overspend
FROM departments AS d JOIN expenses AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name, d.annual_budget HAVING SUM(e.amount) > d.annual_budget
ORDER BY overspend DESC, d.dept_name;""",
    18: """SELECT p.product_name,
CAST(SUM(s.quantity * p.price * (100 - d.discount_percentage) / 100.0) AS INTEGER) AS total_revenue
FROM products AS p JOIN sales AS s ON s.product_id = p.product_id
JOIN discounts AS d ON d.product_id = p.product_id AND s.sale_date BETWEEN d.start_date AND d.end_date
WHERE d.discount_percentage >= 20 GROUP BY p.product_id, p.product_name
HAVING SUM(s.quantity * p.price * (100 - d.discount_percentage) / 100.0) > 50000
ORDER BY total_revenue DESC, p.product_name;""",
    19: """SELECT d.dept_name, SUM(x.amount) AS total_expenses, MAX(x.amount) AS max_individual_expense
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
JOIN expenses AS x ON x.emp_id = e.emp_id GROUP BY d.dept_id, d.dept_name
HAVING SUM(x.amount) > 50000 AND MAX(x.amount) >= 10000
ORDER BY total_expenses DESC, d.dept_name;""",
    20: """SELECT d.dept_name, COUNT(e.emp_id) AS total_employees,
SUM(CASE WHEN e.salary BETWEEN 40000 AND 60000 THEN 1 ELSE 0 END) AS mid_salary_employees,
SUM(CASE WHEN e.salary > 60000 THEN 1 ELSE 0 END) AS high_salary_employees
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING SUM(CASE WHEN e.salary >= 40000 THEN 1 ELSE 0 END) >= 2 ORDER BY d.dept_name;""",
    21: """SELECT d.dept_name,
SUM(CASE WHEN e.expense_type = 'Travel' THEN e.amount ELSE 0 END) AS travel_expenses,
SUM(e.amount) AS total_expenses, COUNT(DISTINCT e.expense_type) AS distinct_expense_types
FROM departments AS d JOIN expenses AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING 2 * SUM(CASE WHEN e.expense_type = 'Travel' THEN e.amount ELSE 0 END) >= SUM(e.amount)
AND COUNT(DISTINCT e.expense_type) >= 2
ORDER BY distinct_expense_types DESC, d.dept_name;""",
    22: """WITH revenue AS (
  SELECT p.product_id, p.product_name, SUM(o.quantity * p.price) AS total_revenue
  FROM products AS p JOIN orders AS o ON o.product_id = p.product_id
  GROUP BY p.product_id, p.product_name
)
SELECT product_name FROM revenue WHERE total_revenue > (SELECT AVG(total_revenue) FROM revenue)
ORDER BY product_name;""",
    23: """WITH totals AS (
  SELECT e.emp_id, e.emp_name, e.department, SUM(p.score) AS total_score, SUM(p.hours_worked) AS total_hours
  FROM employees AS e JOIN performance AS p ON p.emp_id = e.emp_id
  GROUP BY e.emp_id, e.emp_name, e.department
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY total_score DESC, total_hours DESC, emp_name) AS rn FROM totals
)
SELECT department, emp_name, total_score, total_hours FROM ranked WHERE rn = 1 ORDER BY department;""",
    24: """SELECT e.emp_name, SUM(p.hours_worked) AS total_hours,
COUNT(DISTINCT p.project_id) AS project_count
FROM employees AS e JOIN projects AS p ON p.emp_id = e.emp_id WHERE p.start_date > '2023-01-01'
GROUP BY e.emp_id, e.emp_name ORDER BY total_hours DESC, project_count DESC, e.emp_name LIMIT 3;""",
    25: """SELECT d.dept_name, MAX(e.salary) AS max_salary
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id WHERE e.salary > 50000
GROUP BY d.dept_id, d.dept_name HAVING COUNT(*) >= 2 ORDER BY max_salary;""",
    26: """WITH totals AS (
  SELECT customer_id, SUM(order_amount) AS total_amount FROM orders GROUP BY customer_id
), ranked AS (
  SELECT *, RANK() OVER (ORDER BY total_amount DESC) AS spending_rank FROM totals
)
SELECT customer_id, total_amount FROM ranked WHERE spending_rank <= 3
ORDER BY total_amount DESC, customer_id;""",
    27: """WITH ranked AS (
  SELECT d.dept_name, e.emp_name, e.performance_score,
  ROW_NUMBER() OVER (PARTITION BY d.dept_id ORDER BY e.performance_score DESC, e.emp_name) AS rn
  FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
)
SELECT dept_name, emp_name, performance_score FROM ranked WHERE rn <= 2
ORDER BY dept_name, performance_score DESC, emp_name;""",
    28: """WITH totals AS (
  SELECT s.store_id, s.store_name, s.region, SUM(x.amount) AS total_sales
  FROM stores AS s JOIN sales AS x ON x.store_id = s.store_id
  GROUP BY s.store_id, s.store_name, s.region HAVING SUM(x.amount) > 5000
), board AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_sales DESC, store_name) AS rank,
  SUM(total_sales) OVER (PARTITION BY region ORDER BY total_sales DESC, store_name ROWS UNBOUNDED PRECEDING) AS cumulative_sales
  FROM totals
)
SELECT region, store_name, rank, total_sales, cumulative_sales FROM board ORDER BY region, rank;""",
    29: """WITH RECURSIVE reports(manager_id, emp_id) AS (
  SELECT manager_id, manager_id FROM hierarchy GROUP BY manager_id
  UNION ALL
  SELECT r.manager_id, h.emp_id FROM reports AS r JOIN hierarchy AS h ON h.manager_id = r.emp_id
)
SELECT r.manager_id, e.emp_name AS manager_name, COUNT(*) AS total_reports
FROM reports AS r JOIN employees AS e ON e.emp_id = r.manager_id
GROUP BY r.manager_id, e.emp_name ORDER BY total_reports DESC, manager_name;""",
    30: """WITH pairs AS (
  SELECT dept_id_1 AS dept_id, dept_id_2 AS other_id, hours_worked FROM collaborations
  UNION ALL SELECT dept_id_2, dept_id_1, hours_worked FROM collaborations
)
SELECT d.dept_name, SUM(p.hours_worked) AS total_hours,
COUNT(DISTINCT p.other_id) AS unique_collaborations
FROM departments AS d JOIN pairs AS p ON p.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name HAVING COUNT(DISTINCT p.other_id) >= 3 AND SUM(p.hours_worked) >= 100
ORDER BY total_hours DESC, d.dept_name;""",
    31: """WITH last_date AS (SELECT MAX(sale_date) AS d FROM sales), totals AS (
  SELECT product, store_id, SUM(quantity) AS total_sales FROM sales, last_date
  WHERE sale_date >= date(d, '-6 days') AND sale_date <= d GROUP BY product, store_id
), ranked AS (
  SELECT *, DENSE_RANK() OVER (PARTITION BY product ORDER BY total_sales DESC) AS rn FROM totals
)
SELECT product, store_id, total_sales FROM ranked WHERE rn = 1 ORDER BY product, store_id;""",
    32: """WITH type_totals AS (
  SELECT dept_id, task_type, SUM(task_count) AS type_count FROM tasks GROUP BY dept_id, task_type
), metrics AS (
  SELECT dept_id, SUM(type_count) AS total_tasks, COUNT(*) AS distinct_task_types FROM type_totals GROUP BY dept_id
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY type_count DESC, task_type) AS rn FROM type_totals
)
SELECT d.dept_name, m.total_tasks, m.distinct_task_types,
r.task_type AS largest_task_type, r.type_count AS largest_task_count
FROM metrics AS m JOIN ranked AS r ON r.dept_id = m.dept_id AND r.rn = 1
JOIN departments AS d ON d.dept_id = m.dept_id WHERE m.total_tasks > 50
ORDER BY m.total_tasks DESC, d.dept_name;""",
}


EXPLANATIONS = {
    1: "用左闭右开的日期范围筛选 2023 年，可使用索引，也满足不使用 YEAR 函数的限制。",
    2: "LIKE 'L%' 匹配以 L 开头的书名，再按 book_id 保持题目要求的顺序。",
    3: "先按用户名连接到借阅记录，再对记录计数；COUNT(*) 在无匹配时返回 0。",
    4: "连接城市、账户和交易，先过滤账户与交易类型，再按账户分组筛选信用交易超过一次的账户。",
    5: "同时限定交易类型与准确日期，然后对金额求和。",
    6: "SQLite 的 ISO 日期文本可按字典序比较，BETWEEN 包含起止日期。",
    7: "题目要求两个独立结果集，因此 solution.sql 保留两条查询，分别排序书名和作者。",
    8: "按借阅日期过滤后用 DISTINCT 去除同一本书的重复借阅，并按书籍主键排序。",
    9: "连接作者与书籍，组合出版年份和作者名后缀条件，再按作者、书名排序。",
    10: "从借阅事实表连接书籍与用户；加入 issue_id 作为同一用户内的稳定排序键。",
    11: "LEFT JOIN 后保留没有任何借阅匹配的书籍，可准确表达“从未借出”。",
    12: "按客户统计订单数并降序取第一名；客户 ID 用作确定性的并列规则。",
    13: "COUNT 保证选课超过一门，MIN(grade) >= 80 等价于所有课程成绩均达标。",
    14: "员工表自连接到经理记录，直接比较双方工资。",
    15: "双重 NOT EXISTS 表达关系除法：不存在任何一篇 Harry 的帖子未被该用户点赞。",
    16: "每位用户聚合交易金额和最后交易日期，再用 HAVING 筛选总消费。",
    17: "按部门汇总费用，以预算为基准计算超支并在 HAVING 中排除未超支部门。",
    18: "只连接发生在折扣有效期内且折扣至少 20% 的销售，按折后单价计算收入。",
    19: "部门级 SUM 和 MAX 同时得到总费用与最大单笔费用，并在 HAVING 中应用两项门槛。",
    20: "条件聚合分别统计中薪和高薪人数；salary >= 40000 正好是两组人数之和。",
    21: "条件聚合计算差旅费用，用两倍差旅额不小于总额避免浮点百分比比较。",
    22: "CTE 先计算每个产品收入，再与这些产品收入的平均值比较。",
    23: "先聚合员工总分和工时，再按题目给定的三级规则使用 ROW_NUMBER 选每部门第一名。",
    24: "限定项目开始日期后按员工聚合工时及项目数，并依次应用三个排序规则取前三。",
    25: "WHERE 先排除低薪员工，分组后要求合格员工至少两人并计算最高工资。",
    26: "RANK 按总消费排名并让并列者占用相应名次数，因此前三名及第三名并列者都会保留。",
    27: "ROW_NUMBER 在每个部门内按绩效降序、姓名升序编号，保留前两行。",
    28: "先汇总并过滤门店，再用两个窗口函数生成确定性排名和逐行累计销售额。",
    29: "递归 CTE 从每位经理自身出发扩展全部下属，最终计数自然包含经理本人。",
    30: "UNION ALL 将无向协作拆成两个方向，再按部门统计总工时和不同合作部门数。",
    31: "以数据中的最大日期为基准取包含该日的七天窗口，聚合后用 DENSE_RANK 保留并列冠军。",
    32: "先合并同部门同类型记录，再计算部门指标，并用 ROW_NUMBER 按数量和名称选最大任务类型。",
}


# The source contains demonstrably incorrect or malformed expected outputs. These
# replacements are explicit so tests remain independent from the solution query.
EXPECTED_OVERRIDES = {
    (7, 2): [["1984"], ["Brave New World"], ["Moby-Dick"], ["Pride and Prejudice"],
             ["The Great Gatsby"], ["To Kill a Mockingbird"], ["War and Peace"],
             ["Aldous Huxley"], ["F. Scott Fitzgerald"], ["George Orwell"], ["Harper Lee"],
             ["Herman Melville"], ["Jane Austen"], ["Leo Tolstoy"]],
    (8, 1): [["The Power of Now"]],
    (11, 2): [["Brutal Simplicity of thought"], ["Life Lessons"]],
    (16, 2): [["East", "Frank", 11000, "2024-02-05"]],
    (19, 1): [["HR", 65000, 40000], ["IT", 55000, 30000]],
    (20, 1): [["Engineering", 3, 3, 0], ["HR", 2, 2, 0], ["Marketing", 2, 2, 0]],
    (23, 2): [["Marketing", "Grace", 170, 130], ["Sales", "Frank", 180, 95]],
    (28, 1): [["North", "Beta Bazaar", 1, 8000, 8000],
              ["North", "Gamma Goods", 2, 8000, 16000],
              ["North", "Alpha Mart", 3, 7000, 23000],
              ["South", "Delta Deals", 1, 7000, 7000],
              ["South", "Omega Outlet", 2, 7000, 14000]],
    (30, 2): [["Logistics", 230, 3], ["Sales", 150, 3], ["Support", 150, 3],
              ["Research and Development", 140, 3]],
    (31, 1): [["Apples", 1, 60], ["Apples", 2, 60], ["Apples", 3, 60], ["Oranges", 2, 50]],
    (31, 2): [["Bananas", 1, 200], ["Grapes", 2, 200], ["Grapes", 3, 200]],
}


CORRECTION_NOTES = {
    8: "样例 1 的 Lean In 借阅日期为 2022-11-23，不在截止到 2022-02-28 的范围内，故已从期望结果移除。",
    11: "样例 2 实际从未借出的书是 ID 4 和 5；原文的空结果及“全部借出”说明与数据矛盾，已修正。",
    16: "题目要求消费严格大于 10000，样例 2 中恰好消费 10000 的 Ivan 不应入选。",
    19: "样例 1 的 HR 总费用应为 20000 + 40000 + 5000 = 65000，原文误写为 60000。",
    20: "样例 1 的 Marketing 两名员工工资 48000 和 52000 均属中薪区间，原文漏算 Grace。",
    23: "样例 2 已按题意将部门按字母顺序排列为 Marketing、Sales。",
    28: "样例 1 的 Alpha Mart 行分隔符错位，已恢复为 North|Alpha Mart。",
    30: "样例 2 的同分部门按题意以名称升序排列，因此 Sales 位于 Support 之前。",
    31: "原文输出用空格代替列分隔符，且样例 1 漏掉并列第一的 Store 1；均已按数据和题意修正。",
}


def clean_cell(value: str):
    value = value.strip()
    link = re.fullmatch(r"\[([^]]+)]\([^)]+\)", value)
    if link:
        value = link.group(1)
    if value.upper() == "NULL":
        return None
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value)
    return value


def split_exercises(text: str):
    pattern = re.compile(r"(?m)^(?:# )?(\d+)\.([^\n]+ -- [^\n]+)$")
    matches = list(pattern.finditer(text))
    result = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        if number not in SOLUTIONS:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        title_bits = match.group(2).split(" -- ", 1)
        result[number] = {
            "title": title_bits[0].strip(),
            "meta": title_bits[1].strip() if len(title_bits) > 1 else "",
            "body": text[match.end():end].strip(),
        }
    return result


def table_name(lines: list[str], index: int) -> str:
    before = lines[max(0, index - 8):index]
    for line in reversed(before):
        heading = re.search(r"`([A-Za-z_][A-Za-z0-9_]*)`", line)
        if heading:
            return heading.group(1)
    nonempty = [line.strip() for line in before if line.strip()]
    for pos in range(len(nonempty) - 2, -1, -1):
        if nonempty[pos] == "```" and pos + 2 < len(nonempty) and nonempty[pos + 2] == "```":
            return nonempty[pos + 1]
    raise ValueError(f"Cannot determine table name near: {lines[index]}")


def parse_tables(case_text: str, default_table: str | None = None):
    lines = case_text.splitlines()
    tables = {}
    i = 0
    while i + 1 < len(lines):
        if lines[i].strip().startswith("|") and re.fullmatch(r"[| :\-]+", lines[i + 1].strip()):
            try:
                name = table_name(lines, i)
            except ValueError:
                if default_table is None:
                    raise
                name = default_table
            headers = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [clean_cell(cell) for cell in lines[i].strip().strip("|").split("|")]
                if len(cells) == len(headers):
                    rows.append(cells)
                i += 1
            tables[name] = (headers, rows)
            continue
        i += 1
    return tables


def parse_expected(case_text: str):
    marker = list(re.finditer(r"(?im)^#{0,5}\s*(?:\*\*)?(?:Expected )?Output(?::)?(?:\*\*)?\s*$", case_text))
    if not marker:
        raise ValueError("Missing expected output")
    tail = case_text[marker[-1].end():]
    block = re.search(r"```\s*\n(.*?)\n```", tail, re.S)
    if not block:
        raise ValueError("Missing output code block")
    rows = []
    for raw in block.group(1).splitlines():
        raw = raw.strip()
        if not raw:
            continue
        cells = [clean_cell(cell) for cell in raw.strip("|").split("|")]
        rows.append(cells)
    return rows


def parse_cases(number: int, body: str):
    matches = list(re.finditer(r"(?m)^##+ Sample Testcase (\d+)\s*$", body))
    cases = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        chunk = body[match.end():end]
        case_number = int(match.group(1))
        expected = EXPECTED_OVERRIDES.get((number, case_number), parse_expected(chunk))
        cases.append({"tables": parse_tables(chunk, {2: "books"}.get(number)), "expected": expected})
    return cases


def sql_type(column: str, values: list[object]) -> str:
    if all(value is None or isinstance(value, int) for value in values):
        return "INTEGER"
    if all(value is None or isinstance(value, (int, float)) for value in values):
        return "REAL"
    return "TEXT"


def create_database(path: Path, tables):
    with sqlite3.connect(path) as db:
        for name, (headers, rows) in tables.items():
            types = [sql_type(header, [row[i] for row in rows]) for i, header in enumerate(headers)]
            columns = ", ".join(f'"{header}" {kind}' for header, kind in zip(headers, types))
            db.execute(f'CREATE TABLE "{name}" ({columns})')
            placeholders = ", ".join("?" for _ in headers)
            db.executemany(f'INSERT INTO "{name}" VALUES ({placeholders})', rows)


def normalized_question(body: str) -> str:
    schema = re.search(r"(?ims)^#+ Database Schema\s*$.*?(?=^#+ User Task\s*$)", body)
    task = re.search(r"(?ims)^#+ User Task\s*$.*?(?=^#+ (?:Sample Testcases|Testcases|Sample Testcase 1)\s*$)", body)
    pieces = []
    for match in (schema, task):
        if match:
            text = re.sub(r"(?m)^#{1,6}\s*", lambda m: "#" * max(2, len(m.group(0).strip()) - 1) + " ", match.group(0))
            pieces.append(text.strip())
    return "\n\n".join(pieces).replace("------", "---")


def python_literal(value) -> str:
    return repr(value)


def write_project(number: int, exercise: dict, cases: list[dict]):
    slug = re.sub(r"[^a-z0-9]+", "-", exercise["title"].lower()).strip("-")
    directory = OUTPUT / f"{number:02d}-{slug}"
    directory.mkdir(parents=True)
    solution = SOLUTIONS[number].strip() + "\n"
    (directory / "solution.sql").write_text(solution, encoding="utf-8")
    create_database(directory / "database.sqlite3", cases[0]["tables"])
    corrections = "原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。"
    if number in CORRECTION_NOTES:
        corrections += "\n\n**勘误：**" + CORRECTION_NOTES[number]
    readme = f"""# {number}. {exercise['title']}

> {exercise['meta']}

## 题目

{normalized_question(exercise['body'])}

## 解析

{EXPLANATIONS[number]}

{corrections}

## SQL 答案

```sql
{solution.strip()}
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。
"""
    (directory / "README.md").write_text(readme, encoding="utf-8")

    case_literal = repr(cases)
    test = f'''import sqlite3
import unittest
from pathlib import Path


CASES = {case_literal}


def create_case(case):
    db = sqlite3.connect(":memory:")
    for name, (headers, rows) in case["tables"].items():
        values_by_column = list(zip(*rows)) if rows else [[] for _ in headers]
        types = []
        for values in values_by_column:
            non_null = [value for value in values if value is not None]
            types.append("INTEGER" if all(isinstance(value, int) for value in non_null) else "TEXT")
        columns = ", ".join(f'"{{header}}" {{kind}}' for header, kind in zip(headers, types))
        db.execute(f'CREATE TABLE "{{name}}" ({{columns}})')
        placeholders = ", ".join("?" for _ in headers)
        db.executemany(f'INSERT INTO "{{name}}" VALUES ({{placeholders}})', rows)
    return db


class SolutionTests(unittest.TestCase):
    def test_sample_cases(self):
        sql = (Path(__file__).parent / "solution.sql").read_text(encoding="utf-8")
        statements = [statement.strip() for statement in sql.split(";") if statement.strip()]
        for index, case in enumerate(CASES, 1):
            with self.subTest(sample=index), create_case(case) as db:
                actual = []
                for statement in statements:
                    actual.extend([list(row) for row in db.execute(statement).fetchall()])
                self.assertEqual(case["expected"], actual)


if __name__ == "__main__":
    unittest.main()
'''
    (directory / "test_solution.py").write_text(test, encoding="utf-8")
    return directory


def main():
    exercises = split_exercises(SOURCE.read_text(encoding="utf-8"))
    missing = sorted(set(SOLUTIONS) - set(exercises))
    if missing:
        raise RuntimeError(f"Missing exercises: {missing}")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    directories = []
    for number in sorted(exercises):
        cases = parse_cases(number, exercises[number]["body"])
        if len(cases) != 2:
            raise RuntimeError(f"Exercise {number}: expected 2 cases, found {len(cases)}")
        directories.append(write_project(number, exercises[number], cases))
    index = "# SQLite SQL 笔试题独立工程\n\n共 32 个独立工程。每个目录均可单独运行测试。\n\n"
    index += "\n".join(f"- [{path.name}]({path.name}/README.md)" for path in directories) + "\n"
    (OUTPUT / "README.md").write_text(index, encoding="utf-8")
    runner = '''#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


root = Path(__file__).parent
tests = sorted(root.glob("*/test_solution.py"))
failures = 0
for test in tests:
    print(f"\\n==> {test.parent.name}", flush=True)
    failures += subprocess.run([sys.executable, str(test), "-v"], check=False).returncode != 0
print(f"\\nRan {len(tests)} exercise test suites; failures: {failures}")
raise SystemExit(1 if failures else 0)
'''
    (OUTPUT / "run_all_tests.py").write_text(runner, encoding="utf-8")
    print(f"Generated {len(directories)} projects in {OUTPUT}")


if __name__ == "__main__":
    main()

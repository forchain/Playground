# 23. Departmental Top Scorer

> Expert-1 40 mins

## 题目

## Database Schema

You manage a database of employees and their performance metrics. The database consists of two tables: `employees` and `performance`.

## Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- text column `department` (name of the employee's department)

## Table: `performance`

- integer column `record_id` (primary key)
- integer column `emp_id` (foreign key referencing `employees.emp_id`)
- integer column `score` (performance score, ranging from 1 to 100)
- integer column `hours_worked` (total hours worked by the employee in that record)

---

## User Task

Write an SQL query to find the **top-performing employee** in each department based on the following criteria:

1. Select the employee with the **highest total score** in each department.
2. If two or more employees have the same highest total score, choose the one who has worked the most total hours across all their performance records.
3. If there is still a tie, select the employee whose name comes first alphabetically.

The output should include:

- `department`
- `emp_name`
- `total_score`
- `total_hours`

## Constraints:

- Sort the results by `department` alphabetically.

---

## 解析

先聚合员工总分和工时，再按题目给定的三级规则使用 ROW_NUMBER 选每部门第一名。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**样例 2 已按题意将部门按字母顺序排列为 Marketing、Sales。

## SQL 答案

```sql
WITH totals AS (
  SELECT e.emp_id, e.emp_name, e.department, SUM(p.score) AS total_score, SUM(p.hours_worked) AS total_hours
  FROM employees AS e JOIN performance AS p ON p.emp_id = e.emp_id
  GROUP BY e.emp_id, e.emp_name, e.department
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY total_score DESC, total_hours DESC, emp_name) AS rn FROM totals
)
SELECT department, emp_name, total_score, total_hours FROM ranked WHERE rn = 1 ORDER BY department;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

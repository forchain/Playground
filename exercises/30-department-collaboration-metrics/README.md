# 30. Department Collaboration Metrics

> Expert-2 30 mins

## 题目

## Database Schema

You have two tables: `departments` and `collaborations`.

## Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

## Table: `collaborations`

- integer column `collab_id` (primary key)
- integer column `dept_id_1` (ID of the first department, references `departments.dept_id`)
- integer column `dept_id_2` (ID of the second department, references `departments.dept_id`)
- integer column `hours_worked` (total hours worked together by the two departments)

---

## User Task

Write an SQL query to calculate the **collaboration metrics** for each department:

1. For each department, find:
   - `total_hours` worked with other departments (sum of all hours where the department was either `dept_id_1` or `dept_id_2`).
   - `unique_collaborations` count (number of distinct departments this department collaborated with).
2. A department should only be included in the results if:
   - It has collaborated with **at least 3 distinct departments**.
   - It has contributed to **at least 100 total hours** of collaboration.

The output should include:

- `dept_name`
- `total_hours`
- `unique_collaborations`

## Constraints:

- Sort the results by:
  1. `total_hours` in descending order.
  2. `dept_name` alphabetically in case of ties.

---

## 解析

UNION ALL 将无向协作拆成两个方向，再按部门统计总工时和不同合作部门数。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**样例 2 的同分部门按题意以名称升序排列，因此 Sales 位于 Support 之前。

## SQL 答案

```sql
WITH pairs AS (
  SELECT dept_id_1 AS dept_id, dept_id_2 AS other_id, hours_worked FROM collaborations
  UNION ALL SELECT dept_id_2, dept_id_1, hours_worked FROM collaborations
)
SELECT d.dept_name, SUM(p.hours_worked) AS total_hours,
COUNT(DISTINCT p.other_id) AS unique_collaborations
FROM departments AS d JOIN pairs AS p ON p.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name HAVING COUNT(DISTINCT p.other_id) >= 3 AND SUM(p.hours_worked) >= 100
ORDER BY total_hours DESC, d.dept_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

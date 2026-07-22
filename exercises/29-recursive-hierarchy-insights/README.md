# 29. Recursive Hierarchy Insights

> Expert-2 30 mins

## 题目

## Database Schema

You have two tables: `employees` and `hierarchy`.

## Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)

## Table: `hierarchy`

- integer column `emp_id` (ID of the employee; references `employees.emp_id`)
- integer column `manager_id` (ID of the employee's manager; references `employees.emp_id`)

---

## User Task

Write an SQL query to calculate the **total number of employees reporting directly and indirectly** to each manager, including the manager themselves. For simplicity:

- A manager is anyone who has at least one direct report in the `hierarchy` table.
- Include managers who report to another manager (mid-level managers).

The output should include:

- `manager_id`
- `manager_name`
- `total_reports` (total employees directly and indirectly reporting to the manager, including the manager).

## Constraints:

- Sort the results by `total_reports` in descending order, and in case of ties, by `manager_name` alphabetically.

---

## 解析

递归 CTE 从每位经理自身出发扩展全部下属，最终计数自然包含经理本人。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
WITH RECURSIVE reports(manager_id, emp_id) AS (
  SELECT manager_id, manager_id FROM hierarchy GROUP BY manager_id
  UNION ALL
  SELECT r.manager_id, h.emp_id FROM reports AS r JOIN hierarchy AS h ON h.manager_id = r.emp_id
)
SELECT r.manager_id, e.emp_name AS manager_name, COUNT(*) AS total_reports
FROM reports AS r JOIN employees AS e ON e.emp_id = r.manager_id
GROUP BY r.manager_id, e.emp_name ORDER BY total_reports DESC, manager_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

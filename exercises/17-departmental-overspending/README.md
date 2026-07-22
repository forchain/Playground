# 17. Departmental Overspending

> Hard-1 20 mins

## 题目

## Database Schema

You have two tables, `departments` and `expenses`:

## Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)
- integer column `annual_budget` (total annual budget for the department)

## Table: `expenses`

- integer column `expense_id` (primary key)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- integer column `amount` (amount of the expense)
- date column `expense_date` (date the expense was recorded)

---

## User Task

Write an SQL query to find departments that have exceeded their annual budget.

For each department:

1. Calculate the **total expenses** incurred.
2. Determine how much they have **overspent** (`overspend = total_expenses - annual_budget`).

Only include departments where **total_expenses > annual_budget**.

Sort the results by:

- The **overspend** amount in descending order.
- The department name alphabetically in case of a tie.

The output should include:

- `dept_name`
- `total_expenses`
- `overspend`

---

## 解析

按部门汇总费用，以预算为基准计算超支并在 HAVING 中排除未超支部门。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT d.dept_name, SUM(e.amount) AS total_expenses,
SUM(e.amount) - d.annual_budget AS overspend
FROM departments AS d JOIN expenses AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name, d.annual_budget HAVING SUM(e.amount) > d.annual_budget
ORDER BY overspend DESC, d.dept_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

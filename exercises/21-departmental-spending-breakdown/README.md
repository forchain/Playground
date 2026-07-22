# 21. Departmental Spending Breakdown

> Hard-2 30 mins

## 题目

## Database Schema

You have two tables: `departments` and `expenses`.

## Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

## Table: `expenses`

- integer column `expense_id` (primary key)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- integer column `amount` (expense amount in dollars)
- text column `expense_type` (type of the expense, e.g., 'Travel', 'Supplies', 'Miscellaneous')

---

## User Task

Write an SQL query to find departments where:

1. **Travel expenses** account for at least **50% of departmental spending**.
2. The department has **at least 2 distinct expense types** (e.g., 'Travel' and 'Supplies').

For each qualifying department, return:

1. `dept_name`
2. `travel_expenses` (total amount spent on 'Travel' expenses)
3. `total_expenses` (total departmental spending)
4. `distinct_expense_types` (number of distinct expense types in the department)

Sort the results by:

1. `distinct_expense_types` in descending order.
2. `dept_name` alphabetically in case of ties.

---

## 解析

条件聚合计算差旅费用，用两倍差旅额不小于总额避免浮点百分比比较。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT d.dept_name,
SUM(CASE WHEN e.expense_type = 'Travel' THEN e.amount ELSE 0 END) AS travel_expenses,
SUM(e.amount) AS total_expenses, COUNT(DISTINCT e.expense_type) AS distinct_expense_types
FROM departments AS d JOIN expenses AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING 2 * SUM(CASE WHEN e.expense_type = 'Travel' THEN e.amount ELSE 0 END) >= SUM(e.amount)
AND COUNT(DISTINCT e.expense_type) >= 2
ORDER BY distinct_expense_types DESC, d.dept_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

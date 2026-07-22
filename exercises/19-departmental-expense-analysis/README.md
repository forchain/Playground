# 19. Departmental Expense Analysis

> Hard-2 30 mins

## 题目

## Database Schema

You have three tables, `departments`, `employees`, and `expenses`:

## Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

## Table: `employees`

- integer column `emp_id` (primary key)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- text column `emp_name` (name of the employee)

## Table: `expenses`

- integer column `expense_id` (primary key)
- integer column `emp_id` (foreign key referencing `employees.emp_id`)
- integer column `amount` (amount of the expense)
- date column `expense_date` (date of the expense)

---

## User Task

Write an SQL query to find the **total expenses for each department** along with the **highest individual expense** recorded by any employee in that department.

Include only departments where:

1. The total expenses exceed **$50,000**.
2. At least one employee in the department has recorded an individual expense of **$10,000 or more**.

For each department that meets the criteria, return:

- `dept_name` (name of the department)
- `total_expenses` (sum of all expenses in the department)
- `max_individual_expense` (highest expense by any single employee in the department)

Sort the results by `total_expenses` in descending order. In case of a tie, sort by `dept_name` alphabetically.

---

## 解析

部门级 SUM 和 MAX 同时得到总费用与最大单笔费用，并在 HAVING 中应用两项门槛。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**样例 1 的 HR 总费用应为 20000 + 40000 + 5000 = 65000，原文误写为 60000。

## SQL 答案

```sql
SELECT d.dept_name, SUM(x.amount) AS total_expenses, MAX(x.amount) AS max_individual_expense
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
JOIN expenses AS x ON x.emp_id = e.emp_id GROUP BY d.dept_id, d.dept_name
HAVING SUM(x.amount) > 50000 AND MAX(x.amount) >= 10000
ORDER BY total_expenses DESC, d.dept_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

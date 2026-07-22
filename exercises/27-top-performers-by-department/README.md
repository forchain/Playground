# 27. Top Performers by Department

> Expert-1 30 mins

## 题目

## Database Schema

You have two database tables, `departments` and `employees`:

## Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

## Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- integer column `performance_score` (employee's performance score)

## User Task

Write an SQL query to find the **top two performers** from each department based on their `performance_score`.

- If there is a tie in `performance_score`, sort the results by `emp_name` alphabetically.
- Include the department name, employee name, and their performance score in the result.

The output should have the following columns:

- `dept_name`
- `emp_name`
- `performance_score`

Sort the results by `dept_name` alphabetically and, within each department, by `performance_score` in descending order, then by `emp_name` alphabetically.

---

## 解析

ROW_NUMBER 在每个部门内按绩效降序、姓名升序编号，保留前两行。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
WITH ranked AS (
  SELECT d.dept_name, e.emp_name, e.performance_score,
  ROW_NUMBER() OVER (PARTITION BY d.dept_id ORDER BY e.performance_score DESC, e.emp_name) AS rn
  FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
)
SELECT dept_name, emp_name, performance_score FROM ranked WHERE rn <= 2
ORDER BY dept_name, performance_score DESC, emp_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

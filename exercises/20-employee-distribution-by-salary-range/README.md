# 20. Employee Distribution by Salary Range

> Hard-2 20 mins

## 题目

## Database Schema

You have two tables, `departments` and `employees`:

## Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

## Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- integer column `salary`
- integer column `dept_id` (foreign key referencing `departments.dept_id`)

## User Task

Write an SQL query to calculate the following for each department:

- The **total number of employees** in the department (`total_employees`).
- The **number of employees earning between 40000 and 60000 inclusive** (`mid_salary_employees`).
- The **number of employees earning more than 60000** (`high_salary_employees`).

Only include departments where there are at least **2 mid-salary or high-salary employees combined**.

Sort the results by `dept_name` alphabetically.

The output should have the following columns:

- `dept_name`
- `total_employees`
- `mid_salary_employees`
- `high_salary_employees`

---

## 解析

条件聚合分别统计中薪和高薪人数；salary >= 40000 正好是两组人数之和。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**样例 1 的 Marketing 两名员工工资 48000 和 52000 均属中薪区间，原文漏算 Grace。

## SQL 答案

```sql
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees,
SUM(CASE WHEN e.salary BETWEEN 40000 AND 60000 THEN 1 ELSE 0 END) AS mid_salary_employees,
SUM(CASE WHEN e.salary > 60000 THEN 1 ELSE 0 END) AS high_salary_employees
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING SUM(CASE WHEN e.salary >= 40000 THEN 1 ELSE 0 END) >= 2 ORDER BY d.dept_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

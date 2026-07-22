# 24. Employee With Most Working Hours

> Expert-1 20 mins

## 题目

## Database Schema

You have two tables, `employees` and `projects`:

## Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- text column `department` (department of the employee)

## Table: `projects`

- integer column `project_id` (primary key)
- integer column `emp_id` (foreign key referencing `employees.emp_id`)
- text column `project_name` (name of the project)
- integer column `hours_worked` (hours the employee worked on the project)
- date column `start_date` (start date of the project)

## User Task

Write an SQL query to find the **top 3 employees** who worked the **most total hours** across all their projects that started after Jan 1st, 2023

In the case of a tie in total hours worked, sort the employees:

1. First by the number of distinct projects they worked on (higher first).
2. Then alphabetically by their name.

The output should include the employee name (`emp_name`), their total hours worked (`total_hours`), and the number of distinct projects they contributed to (`project_count`).

The output should have three columns:

- `emp_name`
- `total_hours`
- `project_count`

---

## 解析

限定项目开始日期后按员工聚合工时及项目数，并依次应用三个排序规则取前三。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT e.emp_name, SUM(p.hours_worked) AS total_hours,
COUNT(DISTINCT p.project_id) AS project_count
FROM employees AS e JOIN projects AS p ON p.emp_id = e.emp_id WHERE p.start_date > '2023-01-01'
GROUP BY e.emp_id, e.emp_name ORDER BY total_hours DESC, project_count DESC, e.emp_name LIMIT 3;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

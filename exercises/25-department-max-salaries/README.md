# 25. Department Max Salaries

> Expert-1 30 mins

## 题目

## Database Schema

You have two database tables, `departments` and `employees`:

## Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name`

## Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name`
- integer column `salary`
- integer column `dept_id` (foreign key referencing `departments.dept_id`)

## User Task

Write an SQL query that returns each department's name and the **maximum salary** of its employees who earn more than 50000.

- Only include departments where at least two employees meet this salary condition.
- Sort the results by the maximum salary in ascending order.

---

## 解析

WHERE 先排除低薪员工，分组后要求合格员工至少两人并计算最高工资。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT d.dept_name, MAX(e.salary) AS max_salary
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id WHERE e.salary > 50000
GROUP BY d.dept_id, d.dept_name HAVING COUNT(*) >= 2 ORDER BY max_salary;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

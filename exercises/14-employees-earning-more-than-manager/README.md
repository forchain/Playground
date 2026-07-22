# 14. Employees Earning More Than Manager

> Medium-2 20 mins

## 题目

## Database Schema

You have a single table, `employees`:

## Table: `employees`

- integer column `emp_id` (primary key)
- text column `emp_name` (name of the employee)
- integer column `manager_id` (ID of the employee's manager; references `emp_id`)
- integer column `salary`

## User Task

Write an SQL query to return the names of employees who earn **more than their manager**.

- Sort the results by the employee's name in ascending order.

The output should have a single column:

- `emp_name`

---

## 解析

员工表自连接到经理记录，直接比较双方工资。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT e.emp_name FROM employees AS e JOIN employees AS m ON m.emp_id = e.manager_id
WHERE e.salary > m.salary ORDER BY e.emp_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

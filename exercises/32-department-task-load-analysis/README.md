# 32. Department Task Load Analysis

> Expert-2 30 mins

## 题目

## Database Schema

You manage a task tracking system with two tables: `departments` and `tasks`.

## Table: `departments`

- integer column `dept_id` (primary key)
- text column `dept_name` (name of the department)

## Table: `tasks`

- integer column `task_id` (primary key)
- integer column `dept_id` (foreign key referencing `departments.dept_id`)
- text column `task_type` (type of the task; e.g., 'critical', 'major', 'minor')
- integer column `task_count` (number of tasks of this type assigned to the department)

---

## User Task

Write an SQL query to calculate the **task distribution metrics** for each department, with the following requirements:

1. **Total Tasks**: Calculate the total number of tasks assigned to each department.
2. **Distinct Task Types**: Count the number of distinct task types (`task_type`) in each department.
3. **Largest Task Type**: Identify the task type with the highest `task_count` in each department.
   - If two task types have the same `task_count`, choose the one that comes first alphabetically.

Include only departments where:

- The **total number of tasks** is greater than `50`.

The output should include:

- `dept_name`
- `total_tasks`
- `distinct_task_types`
- `largest_task_type`
- `largest_task_count`

## Constraints:

- Sort the results by `total_tasks` in descending order. If there is a tie, sort alphabetically by `dept_name`.

---

## 解析

先合并同部门同类型记录，再计算部门指标，并用 ROW_NUMBER 按数量和名称选最大任务类型。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
WITH type_totals AS (
  SELECT dept_id, task_type, SUM(task_count) AS type_count FROM tasks GROUP BY dept_id, task_type
), metrics AS (
  SELECT dept_id, SUM(type_count) AS total_tasks, COUNT(*) AS distinct_task_types FROM type_totals GROUP BY dept_id
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY type_count DESC, task_type) AS rn FROM type_totals
)
SELECT d.dept_name, m.total_tasks, m.distinct_task_types,
r.task_type AS largest_task_type, r.type_count AS largest_task_count
FROM metrics AS m JOIN ranked AS r ON r.dept_id = m.dept_id AND r.rn = 1
JOIN departments AS d ON d.dept_id = m.dept_id WHERE m.total_tasks > 50
ORDER BY m.total_tasks DESC, d.dept_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

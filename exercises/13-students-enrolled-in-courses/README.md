# 13. Students Enrolled in Courses

> Medium-2 20 mins

## 题目

## Database Schema

You have two tables: `students` and `courses`.

## Table: `students`

- integer column `student_id` (primary key)
- text column `student_name`
- integer column `age`

## Table: `courses`

- integer column `course_id` (primary key)
- integer column `student_id` (foreign key references `students(student_id)`)
- text column `course_name`
- integer column `grade`

---

## User Task

Write an SQL query to find the names of students who have enrolled in more than one course and have scored a grade of 80 or higher in all their courses.

- Sort the results by `student_name` in ascending order.

The output should have a single column:

- `student_name`

---

## 解析

COUNT 保证选课超过一门，MIN(grade) >= 80 等价于所有课程成绩均达标。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT s.student_name FROM students AS s JOIN courses AS c ON c.student_id = s.student_id
GROUP BY s.student_id, s.student_name HAVING COUNT(*) > 1 AND MIN(c.grade) >= 80
ORDER BY s.student_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

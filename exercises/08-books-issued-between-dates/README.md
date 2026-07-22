# 8. Books Issued Between Dates

> Medium-1 15 mins

## 题目

## Database Schema

You have a database with tables

- `users`
- `books`
- `books_issued`

The `users` table has the following columns:

- integer column `user_id` (primary key)
- text column `name`
- text column `email`
- integer column `phone_number`

The `books` table has the following columns:

- integer column `book_id` (primary key)
- text column `book_name`

The `books_issued` table has the following columns:

- integer column `issue_id` (primary key)
- integer column `book_id` references the `book_id` column of the `books` table (foreign key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- text column `return_status`
- date column `date_of_issue`

## User Task

Your task is to return the distinct names of books ordered by book_id which were issued between `2017-02-01` to `2022-02-28`

## 解析

按借阅日期过滤后用 DISTINCT 去除同一本书的重复借阅，并按书籍主键排序。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**样例 1 的 Lean In 借阅日期为 2022-11-23，不在截止到 2022-02-28 的范围内，故已从期望结果移除。

## SQL 答案

```sql
SELECT DISTINCT b.book_name FROM books AS b JOIN books_issued AS bi ON bi.book_id = b.book_id
WHERE bi.date_of_issue BETWEEN '2017-02-01' AND '2022-02-28' ORDER BY b.book_id;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

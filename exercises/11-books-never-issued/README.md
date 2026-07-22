# 11. Books Never Issued

> Medium-2 15 mins

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

Your task is to return the names of books which were never issued, ordered by `book_id` .

## 解析

LEFT JOIN 后保留没有任何借阅匹配的书籍，可准确表达“从未借出”。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**样例 2 实际从未借出的书是 ID 4 和 5；原文的空结果及“全部借出”说明与数据矛盾，已修正。

## SQL 答案

```sql
SELECT b.book_name FROM books AS b LEFT JOIN books_issued AS bi ON bi.book_id = b.book_id
WHERE bi.book_id IS NULL ORDER BY b.book_id;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

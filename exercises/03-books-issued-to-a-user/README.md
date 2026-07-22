# 3. Books Issued To A User

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

Your task is to return the count of number of the books issued to user `Willian Mathew`

## 解析

先按用户名连接到借阅记录，再对记录计数；COUNT(*) 在无匹配时返回 0。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT COUNT(*) FROM books_issued AS bi
JOIN users AS u ON u.user_id = bi.user_id
WHERE u.name = 'Willian Mathew';
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

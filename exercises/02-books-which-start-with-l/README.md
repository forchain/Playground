# 2. Books Which Start With L

> Medium-1 15 mins

## 题目

## Database Schema

You have a database with table `books` which has the following columns

- integer column `book_id` (primary key)
- text column book_name

## User Task

Your task is to return the names of books whose names start with L ordered by `book_id`.

## 解析

LIKE 'L%' 匹配以 L 开头的书名，再按 book_id 保持题目要求的顺序。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT book_name FROM books WHERE book_name LIKE 'L%' ORDER BY book_id;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

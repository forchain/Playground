# 7. Book Titles And Author Names

> Medium-1 15 mins

## 题目

## Database Schema

You have a database table `books` containing the following columns:

- integer column `id` (primary key)
- text column `title`
- text column `author`

## User Task

Your task is to write two separate queries to do the following:

1. Return a list of titles of all books, sorted alphabetically.
2. Return a list of all authors, sorted alphabetically.

## 解析

题目要求两个独立结果集，因此 solution.sql 保留两条查询，分别排序书名和作者。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT title FROM books ORDER BY title;

SELECT author FROM books ORDER BY author;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

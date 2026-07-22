# 9. Post-2000 A-Ending Authors

> Medium-1 15 mins

## 题目

## Database Schema

You have two database tables, `authors` and `books`, with the following columns:

## Table: `authors`

- integer column `author_id` (primary key)
- text column `author_name` (name of the author)

## Table: `books`

- integer column `book_id` (primary key)
- integer column `author_id` (foreign key referencing `authors.author_id`)
- text column `title` (book title)
- integer column `year_published`

## User Task

Your task is to write a query that returns the titles of all books published after the year 2000, authored by writers whose names end with the letter `'a'`. The results should be sorted by the `author_name` in ascending order, and if multiple books are by the same author, sort those books by `title` in ascending order.

---

## 解析

连接作者与书籍，组合出版年份和作者名后缀条件，再按作者、书名排序。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT b.title FROM books AS b JOIN authors AS a ON a.author_id = b.author_id
WHERE b.year_published > 2000 AND a.author_name LIKE '%a'
ORDER BY a.author_name, b.title;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

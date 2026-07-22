# 15. Social Media Query

> Medium-2 20 mins

## 题目

## Database Schema

Consider a database schema for a social media platform with three tables:

- `users`
- `posts`
- `likes`

The `users` table has the following columns:

- integer column `user_id` (primary key)
- text column username

The `posts` table has the following columns:

- integer column `post_id` (primary key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- text column `post_content`

The `likes` table has the following columns:

- integer column `like_id` (primary key)
- integer column `user_id` references the `user_id` column of the `users` table (foreign key)
- integer column `post_id` references the `post_id` column of the `posts` table (foreign key)

## User Task

Write an SQL query to find the users who have liked **all** the posts created by user with username `Harry` ordered by `user_id`

## 解析

双重 NOT EXISTS 表达关系除法：不存在任何一篇 Harry 的帖子未被该用户点赞。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT u.username FROM users AS u
WHERE NOT EXISTS (SELECT 1 FROM posts AS p JOIN users AS h ON h.user_id = p.user_id
                  WHERE h.username = 'Harry' AND NOT EXISTS
                    (SELECT 1 FROM likes AS l WHERE l.user_id = u.user_id AND l.post_id = p.post_id))
AND EXISTS (SELECT 1 FROM posts AS p JOIN users AS h ON h.user_id = p.user_id WHERE h.username = 'Harry')
ORDER BY u.user_id;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

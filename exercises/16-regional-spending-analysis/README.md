# 16. Regional Spending Analysis

> Hard-1 20 mins

## 题目

## Database Schema

You have two tables, `users` and `transactions`:

## Table: `users`

- integer column `user_id` (primary key)
- text column `user_name` (name of the user)
- text column `region` (region where the user is located)

## Table: `transactions`

- integer column `transaction_id` (primary key)
- integer column `user_id` (foreign key referencing `users.user_id`)
- integer column `amount` (amount of the transaction in dollars)
- date column `transaction_date` (date of the transaction)

---

## User Task

Write an SQL query to calculate the **cumulative spending per user** for each transaction they made, grouped by `region`.
For each region, output the user’s name (`user_name`), their total spending (`total_spending`), and the date of their last transaction (`last_transaction_date`).
Only include users who have spent more than $10,000 cumulatively.

Sort the results by `region` alphabetically, `total_spending` in descending order, and then by `last_transaction_date` in descending order.

The output should include the following columns:

- `region`
- `user_name`
- `total_spending`
- `last_transaction_date`

---

## 解析

每位用户聚合交易金额和最后交易日期，再用 HAVING 筛选总消费。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**题目要求消费严格大于 10000，样例 2 中恰好消费 10000 的 Ivan 不应入选。

## SQL 答案

```sql
SELECT u.region, u.user_name, SUM(t.amount) AS total_spending,
MAX(t.transaction_date) AS last_transaction_date
FROM users AS u JOIN transactions AS t ON t.user_id = u.user_id
GROUP BY u.user_id, u.region, u.user_name HAVING SUM(t.amount) > 10000
ORDER BY u.region, total_spending DESC, last_transaction_date DESC;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

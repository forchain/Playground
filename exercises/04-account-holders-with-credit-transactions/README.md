# 4. Account Holders With Credit Transactions

> Medium-1 15 mins

## 题目

## Database Schema

You have a database with tables

- `city`
- `accounts`
- `transactions`

The `city` table has the following columns:

- integer column `city_id` (primary key)
- text column `name`

The `accounts` table has the following columns:

- integer column `account_id` (primary key)
- text column `account_name`
- text column `account_type`
- integer column `city_id` references the `city_id` column of the `city` table (foreign key)

The `transactions` table has the following columns:

- integer column `transaction_id` (primary key)
- integer column `account_id` references the `account_id` column of the `accounts` table (foreign key)
- text column `transaction_type`
- text column `account_type`
- integer column `amount`
- date column `date`

## User Task

Your task is to return the name of all account holders having a `Savings` account, living in `New York` with more than `1` credit transaction ordered by `account_id`.

## 解析

连接城市、账户和交易，先过滤账户与交易类型，再按账户分组筛选信用交易超过一次的账户。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT a.account_name FROM accounts AS a
JOIN city AS c ON c.city_id = a.city_id
JOIN transactions AS t ON t.account_id = a.account_id
WHERE a.account_type = 'Savings' AND c.name = 'New York' AND t.transaction_type = 'Credit'
GROUP BY a.account_id, a.account_name HAVING COUNT(*) > 1 ORDER BY a.account_id;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

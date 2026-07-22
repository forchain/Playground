# 6. Total Transaction Amounts Between Dates

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

Your task is to return the sum of amounts of transactions between made `1st May 2017` - `31st May 2017`

## 解析

SQLite 的 ISO 日期文本可按字典序比较，BETWEEN 包含起止日期。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT SUM(amount) FROM transactions WHERE date BETWEEN '2017-05-01' AND '2017-05-31';
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

# 5. Sum Of All Credit Transactions

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

Your task is to return the sum of all credit transactions on `27th May 2017`

## 解析

同时限定交易类型与准确日期，然后对金额求和。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT SUM(amount) FROM transactions WHERE transaction_type = 'Credit' AND date = '2017-05-27';
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

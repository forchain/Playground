# 12. Maximum Orders

> Medium-2 15 mins

## 题目

## Database schema

You have a database, which contains two tables:

- `customers`
- `orders`

The `customers` table contains the following columns:

- integer column `id`
- text column `name`

The `orders` table contains the following columns:

- integer column `id`
- integer column `amount`
- integer column `customer_id` is a foreign key which references the `id` column of the `customers` table

## User Task

Your task is to find the name of the customer who has the maximum number of orders.

## 解析

按客户统计订单数并降序取第一名；客户 ID 用作确定性的并列规则。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT c.name FROM customers AS c JOIN orders AS o ON o.customer_id = c.id
GROUP BY c.id, c.name ORDER BY COUNT(*) DESC, c.id LIMIT 1;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

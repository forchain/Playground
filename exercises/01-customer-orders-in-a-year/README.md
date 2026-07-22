# 1. Customer Orders In A Year

> Medium-1 15 mins

## 题目

## Database Schema

You have two database tables, `customers` and `orders`:

## Table: `customers`

- integer column `customer_id` (primary key)
- text column `customer_name`

## Table: `orders`

- integer column `order_id` (primary key)
- integer column `customer_id` (foreign key referencing `customers.customer_id`)
- integer column `order_total`
- date column `order_date`

## User Task

Write an SQL query to return the `customer_name` and `order_total` of all orders placed in the year 2023. **Do not use the YEAR function**

- Results should be sorted by `customer_name` in ascending order.
- If a customer has multiple orders in 2023, those orders should be listed with ascending `order_total`.

---

## 解析

用左闭右开的日期范围筛选 2023 年，可使用索引，也满足不使用 YEAR 函数的限制。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT c.customer_name, o.order_total
FROM customers AS c JOIN orders AS o ON o.customer_id = c.customer_id
WHERE o.order_date >= '2023-01-01' AND o.order_date < '2024-01-01'
ORDER BY c.customer_name, o.order_total;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

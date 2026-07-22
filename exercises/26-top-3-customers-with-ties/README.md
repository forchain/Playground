# 26. Top 3 Customers (with ties)

> Expert-1 30 mins

## 题目

## Database Schema

You have a single table, `orders`:

## Table: `orders`

- integer column `order_id` (primary key)
- integer column `customer_id` (ID of the customer who placed the order)
- date column `order_date` (date when the order was placed)
- integer column `order_amount` (amount of the order in dollars)

## User Task

Write an SQL query to find the **top 3 customers** who have spent the highest total amount across all their orders, along with the total amount spent. If there is a tie for the third position, include all customers who tied.

- Sort the results by the `total_amount` in descending order. In case of a tie, sort by `customer_id` in ascending order.

The output should have the following columns:

- `customer_id`
- `total_amount`

---

## 解析

RANK 按总消费排名并让并列者占用相应名次数，因此前三名及第三名并列者都会保留。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
WITH totals AS (
  SELECT customer_id, SUM(order_amount) AS total_amount FROM orders GROUP BY customer_id
), ranked AS (
  SELECT *, RANK() OVER (ORDER BY total_amount DESC) AS spending_rank FROM totals
)
SELECT customer_id, total_amount FROM ranked WHERE spending_rank <= 3
ORDER BY total_amount DESC, customer_id;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

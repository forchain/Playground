# 22. Products Above Average Revenue

> Hard-2 30 mins

## 题目

## Database Schema

You have two database tables, `orders` and `products`:

## Table: `orders`

- integer column `order_id` (primary key)
- integer column `product_id` (foreign key referencing `products.product_id`)
- integer column `quantity` (quantity of the product ordered)

## Table: `products`

- integer column `product_id` (primary key)
- text column `product_name`
- integer column `price` (price of the product)

## User Task

Write an SQL query to return the names of products that have been ordered for a **total revenue greater than the average revenue of all products**.

- Total revenue for a product is calculated as `SUM(quantity * price)` for all its orders.
- Sort the results by `product_name` in ascending order.

The output should have a single column:

- `product_name`

---

## 解析

CTE 先计算每个产品收入，再与这些产品收入的平均值比较。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
WITH revenue AS (
  SELECT p.product_id, p.product_name, SUM(o.quantity * p.price) AS total_revenue
  FROM products AS p JOIN orders AS o ON o.product_id = p.product_id
  GROUP BY p.product_id, p.product_name
)
SELECT product_name FROM revenue WHERE total_revenue > (SELECT AVG(total_revenue) FROM revenue)
ORDER BY product_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

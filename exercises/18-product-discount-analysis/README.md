# 18. Product Discount Analysis

> Hard-2 30 mins

## 题目

## Database Schema

## Table: `products`

- integer column `product_id` (primary key)
- text column `product_name` (name of the product)
- integer column `price` (price of the product)

## Table: `sales`

- integer column `sale_id` (primary key)
- integer column `product_id` (foreign key referencing `products.product_id`)
- integer column `quantity` (number of units sold)
- date column `sale_date` (date of the sale)

## Table: `discounts`

- integer column `discount_id` (primary key)
- integer column `product_id` (foreign key referencing `products.product_id`)
- integer column `discount_percentage` (discount percentage applied to the product)
- date column `start_date` (start date of the discount period)
- date column `end_date` (end date of the discount period)

---

## User Task

Write an SQL query to identify products that generated **total revenue greater than $50,000** during periods when discounts of **20% or more** were applied.

For these products, return:

1. `product_name` (name of the product)
2. `total_revenue` (total revenue during qualifying discount periods)

Sort the results by:

1. `total_revenue` in descending order.
2. `product_name` alphabetically in case of ties.

Note: Use `CAST(NUM) AS INTEGER` to convert a number to an integer.

---

## 解析

只连接发生在折扣有效期内且折扣至少 20% 的销售，按折后单价计算收入。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

## SQL 答案

```sql
SELECT p.product_name,
CAST(SUM(s.quantity * p.price * (100 - d.discount_percentage) / 100.0) AS INTEGER) AS total_revenue
FROM products AS p JOIN sales AS s ON s.product_id = p.product_id
JOIN discounts AS d ON d.product_id = p.product_id AND s.sale_date BETWEEN d.start_date AND d.end_date
WHERE d.discount_percentage >= 20 GROUP BY p.product_id, p.product_name
HAVING SUM(s.quantity * p.price * (100 - d.discount_percentage) / 100.0) > 50000
ORDER BY total_revenue DESC, p.product_name;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

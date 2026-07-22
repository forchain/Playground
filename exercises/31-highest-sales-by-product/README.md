# 31. Highest Sales By Product

> Expert-2 30 mins

## 题目

## Database Schema

You have a table `sales` that tracks daily sales across various stores:

## Table: `sales`

- integer column `store_id` (ID of the store)
- text column `product` (name of the product sold)
- integer column `quantity` (quantity of the product sold)
- date column `sale_date` (date of the sale)

---

## User Task

Write an SQL query to find the store(s) with the highest total sales (in terms of `quantity`) for each product during the last week of recorded sales in the database.

- If multiple stores have the same highest total sales for a product, include all of them.
- Sort the output by `product` in ascending order and then by `store_id` in ascending order.

The output should have the following columns:

- `product`
- `store_id`
- `total_sales`

---

## 解析

以数据中的最大日期为基准取包含该日的七天窗口，聚合后用 DENSE_RANK 保留并列冠军。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**原文输出用空格代替列分隔符，且样例 1 漏掉并列第一的 Store 1；均已按数据和题意修正。

## SQL 答案

```sql
WITH last_date AS (SELECT MAX(sale_date) AS d FROM sales), totals AS (
  SELECT product, store_id, SUM(quantity) AS total_sales FROM sales, last_date
  WHERE sale_date >= date(d, '-6 days') AND sale_date <= d GROUP BY product, store_id
), ranked AS (
  SELECT *, DENSE_RANK() OVER (PARTITION BY product ORDER BY total_sales DESC) AS rn FROM totals
)
SELECT product, store_id, total_sales FROM ranked WHERE rn = 1 ORDER BY product, store_id;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

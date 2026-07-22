# 28. Store Sales Leaderboard

> Expert-2 30 mins

## 题目

## Database Schema

You manage a sales system with two tables: `stores` and `sales`.

## Table: `stores`

- integer column `store_id` (primary key)
- text column `store_name` (name of the store)
- text column `region` (region of the store)

## Table: `sales`

- integer column `sale_id` (primary key)
- integer column `store_id` (foreign key referencing `stores.store_id`)
- integer column `amount` (amount of the sale in dollars)

---

## User Task

Write an SQL query to calculate a **regional sales leaderboard** for all stores. For each store in every region:

1. Assign a **rank** to each store based on their total sales within the region (highest to lowest). If two stores have the same total sales, rank them alphabetically by their name.
2. Calculate the **cumulative sales** for each region, up to the current store's rank.
3. Include only stores where the **total sales** are greater than `5000`.

The output should include:

- `region`
- `store_name`
- `rank`
- `total_sales`
- `cumulative_sales`

## Constraints:

- Sort the output by `region` alphabetically, then by `rank` in ascending order.

---

## 解析

先汇总并过滤门店，再用两个窗口函数生成确定性排名和逐行累计销售额。

原文中的标题层级、围栏标记、表格对齐和输出末尾空格已规范化。

**勘误：**样例 1 的 Alpha Mart 行分隔符错位，已恢复为 North|Alpha Mart。

## SQL 答案

```sql
WITH totals AS (
  SELECT s.store_id, s.store_name, s.region, SUM(x.amount) AS total_sales
  FROM stores AS s JOIN sales AS x ON x.store_id = s.store_id
  GROUP BY s.store_id, s.store_name, s.region HAVING SUM(x.amount) > 5000
), board AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_sales DESC, store_name) AS rank,
  SUM(total_sales) OVER (PARTITION BY region ORDER BY total_sales DESC, store_name ROWS UNBOUNDED PRECEDING) AS cumulative_sales
  FROM totals
)
SELECT region, store_name, rank, total_sales, cumulative_sales FROM board ORDER BY region, rank;
```

## 运行测试

```bash
python3 -m unittest -v test_solution.py
```

`database.sqlite3` 使用样例 1 初始化；测试文件会为每个样例创建独立的内存数据库。

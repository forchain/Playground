WITH last_date AS (SELECT MAX(sale_date) AS d FROM sales), totals AS (
  SELECT product, store_id, SUM(quantity) AS total_sales FROM sales, last_date
  WHERE sale_date >= date(d, '-6 days') AND sale_date <= d GROUP BY product, store_id
), ranked AS (
  SELECT *, DENSE_RANK() OVER (PARTITION BY product ORDER BY total_sales DESC) AS rn FROM totals
)
SELECT product, store_id, total_sales FROM ranked WHERE rn = 1 ORDER BY product, store_id;

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

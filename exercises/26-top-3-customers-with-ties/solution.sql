WITH totals AS (
  SELECT customer_id, SUM(order_amount) AS total_amount FROM orders GROUP BY customer_id
), ranked AS (
  SELECT *, RANK() OVER (ORDER BY total_amount DESC) AS spending_rank FROM totals
)
SELECT customer_id, total_amount FROM ranked WHERE spending_rank <= 3
ORDER BY total_amount DESC, customer_id;

WITH revenue AS (
  SELECT p.product_id, p.product_name, SUM(o.quantity * p.price) AS total_revenue
  FROM products AS p JOIN orders AS o ON o.product_id = p.product_id
  GROUP BY p.product_id, p.product_name
)
SELECT product_name FROM revenue WHERE total_revenue > (SELECT AVG(total_revenue) FROM revenue)
ORDER BY product_name;

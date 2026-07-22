SELECT p.product_name,
CAST(SUM(s.quantity * p.price * (100 - d.discount_percentage) / 100.0) AS INTEGER) AS total_revenue
FROM products AS p JOIN sales AS s ON s.product_id = p.product_id
JOIN discounts AS d ON d.product_id = p.product_id AND s.sale_date BETWEEN d.start_date AND d.end_date
WHERE d.discount_percentage >= 20 GROUP BY p.product_id, p.product_name
HAVING SUM(s.quantity * p.price * (100 - d.discount_percentage) / 100.0) > 50000
ORDER BY total_revenue DESC, p.product_name;

SELECT c.customer_name, o.order_total
FROM customers AS c JOIN orders AS o ON o.customer_id = c.customer_id
WHERE o.order_date >= '2023-01-01' AND o.order_date < '2024-01-01'
ORDER BY c.customer_name, o.order_total;

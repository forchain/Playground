SELECT c.name FROM customers AS c JOIN orders AS o ON o.customer_id = c.id
GROUP BY c.id, c.name ORDER BY COUNT(*) DESC, c.id LIMIT 1;

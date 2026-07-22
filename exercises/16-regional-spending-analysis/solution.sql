SELECT u.region, u.user_name, SUM(t.amount) AS total_spending,
MAX(t.transaction_date) AS last_transaction_date
FROM users AS u JOIN transactions AS t ON t.user_id = u.user_id
GROUP BY u.user_id, u.region, u.user_name HAVING SUM(t.amount) > 10000
ORDER BY u.region, total_spending DESC, last_transaction_date DESC;

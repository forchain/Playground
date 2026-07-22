SELECT a.account_name FROM accounts AS a
JOIN city AS c ON c.city_id = a.city_id
JOIN transactions AS t ON t.account_id = a.account_id
WHERE a.account_type = 'Savings' AND c.name = 'New York' AND t.transaction_type = 'Credit'
GROUP BY a.account_id, a.account_name HAVING COUNT(*) > 1 ORDER BY a.account_id;

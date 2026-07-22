SELECT d.dept_name, SUM(x.amount) AS total_expenses, MAX(x.amount) AS max_individual_expense
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
JOIN expenses AS x ON x.emp_id = e.emp_id GROUP BY d.dept_id, d.dept_name
HAVING SUM(x.amount) > 50000 AND MAX(x.amount) >= 10000
ORDER BY total_expenses DESC, d.dept_name;

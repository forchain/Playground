SELECT d.dept_name,
SUM(CASE WHEN e.expense_type = 'Travel' THEN e.amount ELSE 0 END) AS travel_expenses,
SUM(e.amount) AS total_expenses, COUNT(DISTINCT e.expense_type) AS distinct_expense_types
FROM departments AS d JOIN expenses AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING 2 * SUM(CASE WHEN e.expense_type = 'Travel' THEN e.amount ELSE 0 END) >= SUM(e.amount)
AND COUNT(DISTINCT e.expense_type) >= 2
ORDER BY distinct_expense_types DESC, d.dept_name;

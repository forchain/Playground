SELECT d.dept_name, SUM(e.amount) AS total_expenses,
SUM(e.amount) - d.annual_budget AS overspend
FROM departments AS d JOIN expenses AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name, d.annual_budget HAVING SUM(e.amount) > d.annual_budget
ORDER BY overspend DESC, d.dept_name;

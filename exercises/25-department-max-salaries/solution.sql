SELECT d.dept_name, MAX(e.salary) AS max_salary
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id WHERE e.salary > 50000
GROUP BY d.dept_id, d.dept_name HAVING COUNT(*) >= 2 ORDER BY max_salary;

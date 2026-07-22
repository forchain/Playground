SELECT d.dept_name, COUNT(e.emp_id) AS total_employees,
SUM(CASE WHEN e.salary BETWEEN 40000 AND 60000 THEN 1 ELSE 0 END) AS mid_salary_employees,
SUM(CASE WHEN e.salary > 60000 THEN 1 ELSE 0 END) AS high_salary_employees
FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING SUM(CASE WHEN e.salary >= 40000 THEN 1 ELSE 0 END) >= 2 ORDER BY d.dept_name;

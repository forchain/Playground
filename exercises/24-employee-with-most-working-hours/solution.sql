SELECT e.emp_name, SUM(p.hours_worked) AS total_hours,
COUNT(DISTINCT p.project_id) AS project_count
FROM employees AS e JOIN projects AS p ON p.emp_id = e.emp_id WHERE p.start_date > '2023-01-01'
GROUP BY e.emp_id, e.emp_name ORDER BY total_hours DESC, project_count DESC, e.emp_name LIMIT 3;

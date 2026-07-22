SELECT e.emp_name FROM employees AS e JOIN employees AS m ON m.emp_id = e.manager_id
WHERE e.salary > m.salary ORDER BY e.emp_name;

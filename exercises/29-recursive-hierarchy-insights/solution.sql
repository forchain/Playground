WITH RECURSIVE reports(manager_id, emp_id) AS (
  SELECT manager_id, manager_id FROM hierarchy GROUP BY manager_id
  UNION ALL
  SELECT r.manager_id, h.emp_id FROM reports AS r JOIN hierarchy AS h ON h.manager_id = r.emp_id
)
SELECT r.manager_id, e.emp_name AS manager_name, COUNT(*) AS total_reports
FROM reports AS r JOIN employees AS e ON e.emp_id = r.manager_id
GROUP BY r.manager_id, e.emp_name ORDER BY total_reports DESC, manager_name;

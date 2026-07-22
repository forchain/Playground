WITH pairs AS (
  SELECT dept_id_1 AS dept_id, dept_id_2 AS other_id, hours_worked FROM collaborations
  UNION ALL SELECT dept_id_2, dept_id_1, hours_worked FROM collaborations
)
SELECT d.dept_name, SUM(p.hours_worked) AS total_hours,
COUNT(DISTINCT p.other_id) AS unique_collaborations
FROM departments AS d JOIN pairs AS p ON p.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name HAVING COUNT(DISTINCT p.other_id) >= 3 AND SUM(p.hours_worked) >= 100
ORDER BY total_hours DESC, d.dept_name;

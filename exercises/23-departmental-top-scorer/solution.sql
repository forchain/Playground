WITH totals AS (
  SELECT e.emp_id, e.emp_name, e.department, SUM(p.score) AS total_score, SUM(p.hours_worked) AS total_hours
  FROM employees AS e JOIN performance AS p ON p.emp_id = e.emp_id
  GROUP BY e.emp_id, e.emp_name, e.department
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY total_score DESC, total_hours DESC, emp_name) AS rn FROM totals
)
SELECT department, emp_name, total_score, total_hours FROM ranked WHERE rn = 1 ORDER BY department;

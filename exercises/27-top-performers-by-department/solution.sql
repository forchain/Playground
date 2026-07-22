WITH ranked AS (
  SELECT d.dept_name, e.emp_name, e.performance_score,
  ROW_NUMBER() OVER (PARTITION BY d.dept_id ORDER BY e.performance_score DESC, e.emp_name) AS rn
  FROM departments AS d JOIN employees AS e ON e.dept_id = d.dept_id
)
SELECT dept_name, emp_name, performance_score FROM ranked WHERE rn <= 2
ORDER BY dept_name, performance_score DESC, emp_name;

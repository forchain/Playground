WITH type_totals AS (
  SELECT dept_id, task_type, SUM(task_count) AS type_count FROM tasks GROUP BY dept_id, task_type
), metrics AS (
  SELECT dept_id, SUM(type_count) AS total_tasks, COUNT(*) AS distinct_task_types FROM type_totals GROUP BY dept_id
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY type_count DESC, task_type) AS rn FROM type_totals
)
SELECT d.dept_name, m.total_tasks, m.distinct_task_types,
r.task_type AS largest_task_type, r.type_count AS largest_task_count
FROM metrics AS m JOIN ranked AS r ON r.dept_id = m.dept_id AND r.rn = 1
JOIN departments AS d ON d.dept_id = m.dept_id WHERE m.total_tasks > 50
ORDER BY m.total_tasks DESC, d.dept_name;

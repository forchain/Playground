SELECT s.student_name FROM students AS s JOIN courses AS c ON c.student_id = s.student_id
GROUP BY s.student_id, s.student_name HAVING COUNT(*) > 1 AND MIN(c.grade) >= 80
ORDER BY s.student_name;

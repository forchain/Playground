SELECT b.title FROM books AS b JOIN authors AS a ON a.author_id = b.author_id
WHERE b.year_published > 2000 AND a.author_name LIKE '%a'
ORDER BY a.author_name, b.title;

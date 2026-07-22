SELECT b.book_name, u.name FROM books_issued AS bi
JOIN books AS b ON b.book_id = bi.book_id JOIN users AS u ON u.user_id = bi.user_id
ORDER BY u.user_id, bi.issue_id;

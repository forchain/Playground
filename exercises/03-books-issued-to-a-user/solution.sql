SELECT COUNT(*) FROM books_issued AS bi
JOIN users AS u ON u.user_id = bi.user_id
WHERE u.name = 'Willian Mathew';

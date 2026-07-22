SELECT b.book_name FROM books AS b LEFT JOIN books_issued AS bi ON bi.book_id = b.book_id
WHERE bi.book_id IS NULL ORDER BY b.book_id;

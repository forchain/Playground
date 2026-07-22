SELECT DISTINCT b.book_name FROM books AS b JOIN books_issued AS bi ON bi.book_id = b.book_id
WHERE bi.date_of_issue BETWEEN '2017-02-01' AND '2022-02-28' ORDER BY b.book_id;

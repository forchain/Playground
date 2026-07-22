SELECT u.username FROM users AS u
WHERE NOT EXISTS (SELECT 1 FROM posts AS p JOIN users AS h ON h.user_id = p.user_id
                  WHERE h.username = 'Harry' AND NOT EXISTS
                    (SELECT 1 FROM likes AS l WHERE l.user_id = u.user_id AND l.post_id = p.post_id))
AND EXISTS (SELECT 1 FROM posts AS p JOIN users AS h ON h.user_id = p.user_id WHERE h.username = 'Harry')
ORDER BY u.user_id;

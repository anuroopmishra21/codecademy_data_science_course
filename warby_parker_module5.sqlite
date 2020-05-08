 SELECT * FROM survey LIMIT 10;
 
 SELECT question, COUNT(DISTINCT user_id) FROM survey GROUP BY 1;
 
SELECT DISTINCT q.user_id,
h.user_id IS NOT NULL AS 'is_home_try_on',
h.number_of_pairs,
p.user_id IS NOT NULL AS 'is_purchase'
FROM quiz AS 'q' LEFT JOIN home_try_on AS 'h' ON q.user_id=h.user_id LEFT JOIN purchase AS 'p' ON h.user_id=p.user_id LIMIT 10;

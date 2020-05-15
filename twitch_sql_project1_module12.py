SELECT * FROM stream LIMIT 20;
SELECT * FROM chat LIMIT 20;
SELECT DISTINCT game FROM stream;
SELECT DISTINCT channel FROM stream;
SELECT COUNT(*) AS 'number of viewers', game FROM stream GROUP BY 2;
SELECT COUNT(*) AS 'number of LoL viewers',country FROM stream WHERE game = 'League of Legends' GROUP BY 2;
SELECT player, COUNT(*) AS 'number of streamers' FROM stream GROUP BY 1;
SELECT game,
  CASE
  WHEN (game='League of Legends') OR (game='DOTA 2') OR (game='Heroes of the Strom') THEN 'MOBA'
  WHEN (game='Counter-Strike: Global Offensive') THEN 'FPS'
  WHEN (game='DayZ') OR (game='Survival Evolved') THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*) FROM stream GROUP BY 1 ORDER BY 3 DESC;
SELECT time FROM stream LIMIT 10;
SELECT time, strftime('%S',time) FROM stream GROUP BY 1 LIMIT 20;
SELECT strftime('%H',time),COUNT(*) FROM stream WHERE country='US' GROUP BY 1;
SELECT * FROM stream JOIN chat ON stream.device_id=chat.device_id;

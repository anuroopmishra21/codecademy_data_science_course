 SELECT * FROM page_visits LIMIT 10;
 
 SELECT * FROM page_visits WHERE user_id=10069 AND utm_source='buzzfeed';
 
 SELECT * FROM page_visits WHERE user_id=10069;
 
 SELECT * FROM page_visits WHERE user_id=10329;
 
 SELECT user_id,MAX(timestamp) AS 'last_touch_at' FROM page_visits GROUP BY 1;

SELECT user_id,MAX(timestamp) AS 'last_touch_at' FROM page_visits WHERE user_id=10069 GROUP BY 1;

WITH last_touch AS
(
  SELECT user_id, MAX(timestamp) AS'last_touch_at' FROM page_visits GROUP BY 1
)
SELECT lt.user_id,lt.last_touch_at,pv.utm_source FROM last_touch AS 'lt' JOIN page_visits AS 'pv' ON lt.user_id = pv.user_id AND lt.last_touch_at= pv.timestamp;

WITH last_touch AS
(
  SELECT user_id, MAX(timestamp) AS'last_touch_at' FROM page_visits WHERE user_id=10069 GROUP BY 1
)
SELECT lt.user_id,lt.last_touch_at,pv.utm_source FROM last_touch AS 'lt' JOIN page_visits AS 'pv' ON lt.user_id = pv.user_id AND lt.last_touch_at= pv.timestamp;

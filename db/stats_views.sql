
CREATE VIEW vw_day_counts AS 
SELECT 
dayname(c5messages_messagelog.logtime) AS day_of_week, 
dayofweek(c5messages_messagelog.logtime) AS day_num, 
to_days(c5messages_messagelog.logtime) AS date,
COUNT(*) AS msg_count 
FROM c5messages_messagelog 
GROUP BY to_days(c5messages_messagelog.logtime);


CREATE VIEW vw_day_avgs AS 
SELECT vw_day_counts.day_of_week AS day_of_week,
vw_day_counts.day_num AS day_num,
AVG(vw_day_counts.msg_count) AS average_msgs 
FROM vw_day_counts 
GROUP BY vw_day_counts.day_of_week 
ORDER BY vw_day_counts.day_num;

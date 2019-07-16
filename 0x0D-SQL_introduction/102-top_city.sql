-- Getting more temperature data
-- Average data for 2 months
SELECT city, avg_temp FROM (
       SELECT DISTINCT city, AVG(value) as avg_temp
       FROM temperatures WHERE `month` = 8 or `month` = 7 GROUP BY `city`)
AS t2 GROUP BY avg_temp DESC, city LIMIT 3;

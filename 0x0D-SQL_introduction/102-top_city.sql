-- Getting more temperature data
-- Average data for 2 months
SELECT MAX(test) as city, avg_temp FROM (
       SELECT DISTINCT MAX(city) AS test, ROUND(AVG(avg_temp), 4) AS avg_temp FROM (
       	      SELECT DISTINCT city, month, ROUND(AVG(value), 4) as AVG_temp
       	      FROM temperatures WHERE `month` = 8 or `month` = 7
	      GROUP BY `city`, month)
	      AS t2 GROUP BY `city`)
AS t3 GROUP BY avg_temp DESC LIMIT 3;

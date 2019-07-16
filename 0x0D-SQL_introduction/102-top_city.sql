-- Getting more temperature data
-- Average data for 2 months
SELECT MAX(city) as city, avg_temp FROM (
       SELECT DISTINCT MAX(city) AS city, AVG(avg_temp) AS avg_temp FROM (
       	      SELECT DISTINCT city, month, AVG(value) as AVG_temp
       	      FROM temperatures WHERE `month` = 8 or `month` = 7
	      GROUP BY city, month)
	      AS t2 GROUP BY city)
AS t3 GROUP BY avg_temp DESC LIMIT 3;

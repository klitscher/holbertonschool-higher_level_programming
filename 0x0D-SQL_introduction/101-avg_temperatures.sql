-- Create script that displays average temp
-- See above
SELECT MAX(city) AS city, avg_temp FROM (SELECT DISTINCT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city) AS T2 GROUP BY avg_temp DESC;

-- Find max temperature
-- Of all states?
SELECT DISTINCT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;

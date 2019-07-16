-- Find max temperature
-- Of all states?
SELECT DISTINCT state, MAX(value) FROM temperatures GROUP BY state;

-- Script that lists all cities in cali
-- See above
SELECT id, name FROM cities WHERE state_id = 1 GROUP BY id ASC;

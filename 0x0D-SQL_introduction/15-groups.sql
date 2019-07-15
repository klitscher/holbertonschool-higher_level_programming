-- List number of records
-- Have to have same score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY number DESC HAVING number >= 1;

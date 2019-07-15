-- List number of records
-- Have to have same score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC HAVING number >= 1;

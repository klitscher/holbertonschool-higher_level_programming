-- List all records
-- With some constraints
SELECT score, name FROM second_table WHERE name IS NOT NULL GROUP BY score DESC, name;

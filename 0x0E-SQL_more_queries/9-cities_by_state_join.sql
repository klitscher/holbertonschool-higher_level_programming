-- lists all cities in a database
-- See above
SELECT cities.id, cities.name FROM cities NATURAL JOIN states.name GROUP BY cities.id ASC;

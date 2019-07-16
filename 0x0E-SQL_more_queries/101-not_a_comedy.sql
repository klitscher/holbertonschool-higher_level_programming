-- List all movies that are not a comedy
-- See above
SELECT tv_shows.title FROM tv_shows
LEFT JOIN (
     SELECT tv_shows.title AS negative FROM tv_shows
     INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
     INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
     WHERE tv_genres.name = 'Comedy' ORDER BY tv_shows.title ASC)
AS tbl2 ON tv_shows.title = negative WHERE negative IS NULL
ORDER BY tv_shows.title ASC;

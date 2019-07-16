-- Script to list all shows and all genres linked to that show
-- See above
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_shows.title, tv_genres.name ORDER BY tv_shows.title ASC, tv_genres.name ASC;

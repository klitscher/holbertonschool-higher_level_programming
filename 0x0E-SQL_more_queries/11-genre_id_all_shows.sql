-- Lists all shows, but also show NULL
-- See above
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

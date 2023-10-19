-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_gen.name AS gen_name,
       COUNT(*) AS no_of_shows
FROM tv_genres AS tv_gen
INNER JOIN tv_show_genres AS show_gen
ON tv_gen.id = show_gen.genre_id
GROUP BY gen_name
ORDER BY no_of_shows DESC;


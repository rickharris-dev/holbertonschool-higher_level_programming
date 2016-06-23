\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
SELECT TVShow.name AS name
    FROM TVShow
    JOIN Season
    WHERE TVShow.id = Season.tvshow_id
    GROUP BY name
    HAVING count(Season.id) >= 4
    ORDER BY name ASC;

\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
SELECT TVShow.name AS name
    FROM TVShow
    JOIN TVShowGenre, Genre
    WHERE TVShow.id = TVShowGenre.tvshow_id
    AND TVShowGenre.genre_id = Genre.id
    AND Genre.name = 'Comedy'
    ORDER BY name ASC;

\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
SELECT Actor.name AS name
    FROM TVShow
    JOIN TVShowActor, Actor
    WHERE TVShow.id = TVShowActor.tvshow_id
    AND TVShowActor.actor_id = Actor.id
    AND TVShow.name = 'The Big Bang Theory'
    ORDER BY name ASC;

\! echo "\nTop 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
SELECT Actor.name AS name, count(TVShowActor.tvshow_id) AS nb_tvshows
    FROM Actor
    JOIN TVShowActor
    WHERE Actor.id = TVShowActor.actor_id
    GROUP BY Actor.id
    ORDER BY nb_tvshows DESC
    LIMIT 10;

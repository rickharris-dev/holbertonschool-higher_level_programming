\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT TVShow.name AS name, count(Season.id) AS nb_seasons
    FROM TVShow
    JOIN Season
    WHERE TVShow.id = Season.tvshow_id
    GROUP BY name
    ORDER BY name ASC;

\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVShow.name, Network.name
    FROM TVShow
    JOIN Network
    WHERE TVShow.network_id = Network.id
    ORDER BY TVShow.name;

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT TVShow.name AS name
    FROM TVShow
    JOIN Network
    WHERE TVShow.network_id = Network.id
    AND Network.name = 'FOX (US)'
    ORDER BY name ASC;

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT TVShow.name AS name, count(Episode.id) AS nb_episodes
    FROM TVShow
    JOIN Season, Episode
    WHERE TVShow.id = Season.tvshow_id
    AND Season.id = Episode.season_id
    GROUP BY name
    ORDER BY name ASC;

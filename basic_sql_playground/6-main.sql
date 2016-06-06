SELECT DISTINCT TVShow.name, sum(Person.age) FROM TVShow
    JOIN TVShowPerson ON TVShowPerson.tvshow_id=TVShow.id,
    Person ON TVShowPerson.person_id=Person.id
    GROUP BY TVShow.name
    ORDER BY sum(Person.age) ASC;

SELECT TVShow.name, Person.first_name, Person.last_name, min(Person.age) FROM TVShow
    JOIN TVShowPerson ON TVShowPerson.tvshow_id=TVShow.id,
    Person ON TVShowPerson.person_id=Person.id
    GROUP BY TVShow.name
    ORDER BY min(Person.age) ASC;

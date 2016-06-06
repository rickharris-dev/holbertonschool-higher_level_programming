SELECT DISTINCT last_name FROM Person
    JOIN TVShowPerson ON Person.id=TVShowPerson.person_id,
    TVShow ON TVShowPerson.tvshow_id=TVShow.id
    WHERE TVShow.name="Game of Thrones";

SELECT COUNT(*) FROM Person WHERE age > 30;

SELECT Person.id, first_name, last_name, age, Eyescolor.color, TVShow.name FROM Person
    JOIN TVShowPerson ON Person.id=TVShowPerson.person_id,
    TVShow ON TVShowPerson.tvshow_id=TVShow.id,
    Eyescolor ON Eyescolor.person_id=Person.id;

SELECT SUM(age) FROM Person;

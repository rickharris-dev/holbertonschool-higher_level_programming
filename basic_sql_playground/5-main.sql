/* Displays the unique last names of Game of Thrones characters */
SELECT DISTINCT last_name FROM Person
    JOIN TVShowPerson ON Person.id=TVShowPerson.person_id,
    TVShow ON TVShowPerson.tvshow_id=TVShow.id
    WHERE TVShow.name="Game of Thrones";

/* Counts the number of people older than 30 */
SELECT COUNT(*) FROM Person WHERE age > 30;

/* Displays Person info with eye color and tv show */
SELECT Person.id, first_name, last_name, age, Eyescolor.color, TVShow.name FROM Person
    JOIN TVShowPerson ON Person.id=TVShowPerson.person_id,
    TVShow ON TVShowPerson.tvshow_id=TVShow.id,
    Eyescolor ON Eyescolor.person_id=Person.id;

/* Displays the total of the age of all persons */
SELECT SUM(age) FROM Person;

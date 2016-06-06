/* Displays the first name of all records in the Person database */
SELECT first_name FROM Person;

/* Displays the name and age of all rows in the Person database */
SELECT first_name,age FROM Person;

/* Displays the unique eye colors in the Eyescolor database */
SELECT DISTINCT color FROM Eyescolor;

/* Displays first, last and age of each row in the Person DB ordered by Age */
SELECT first_name,last_name,age FROM Person ORDER BY age ASC;

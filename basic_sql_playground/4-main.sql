/* Sets the eye color for Jon Snow */
INSERT INTO Eyescolor (person_id, color)
    VALUES ((SELECT id FROM Person WHERE first_name="Jon" AND last_name="Snow"), "Brown");

/* Sets the eye color for Arya Stark */
INSERT INTO Eyescolor (person_id, color)
    VALUES ((SELECT id FROM Person WHERE first_name="Arya" AND last_name="Stark"), "Green");

/* Creates a TVShow table */
CREATE TABLE TVShow (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name CHAR(128)
);

/* Creates a TVShowPerson table */
CREATE TABLE TVShowPerson (
    tvshow_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(tvshow_id) REFERENCES TVShow(id),
    FOREIGN KEY(person_id) REFERENCES Person(id)
);

/* Adds records into TVShow table */
INSERT INTO TVShow (name)
    VALUES ("Homeland"),
    ("The big bang theory"),
    ("Game of Thrones"),
    ("Breaking bad");

/* Links each person to a TV show */
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (
    (SELECT id FROM TVShow WHERE name="Breaking bad"),
    (SELECT id FROM Person WHERE first_name="Walter Junior" AND last_name="White")),
    ((SELECT id FROM TVShow WHERE name="Game of Thrones"),
    (SELECT id FROM Person WHERE first_name="Jaime" AND last_name="Lannister")),
    ((SELECT id FROM TVShow WHERE name="The big bang theory"),
    (SELECT id FROM Person WHERE first_name="Sheldon" AND last_name="Cooper")),
    ((SELECT id FROM TVShow WHERE name="Game of Thrones"),
    (SELECT id FROM Person WHERE first_name="Tyrion" AND last_name="Lannister")),
    ((SELECT id FROM TVShow WHERE name="Game of Thrones"),
    (SELECT id FROM Person WHERE first_name="Jon" AND last_name="Snow")),
    ((SELECT id FROM TVShow WHERE name="Game of Thrones"),
    (SELECT id FROM Person WHERE first_name="Arya" AND last_name="Stark"));

/* Displays all rows in the Person table */
SELECT * FROM Person;

/* Displays all rows in the EyesColor table */
SELECT * FROM EyesColor;

/* Displays all rows in the TVShow table */
SELECT * FROM TVShow;

/* Displays all rows in the TVShowPerson table */
SELECT * FROM TVShowPerson;

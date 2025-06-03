BEGIN TRANSACTION;
DELETE FROM city;
DELETE FROM sqlite_sequence WHERE name='city';

INSERT INTO city (id, name, description) VALUES (1, "Berlin", "Die Hauptstadt Deutschlands");
COMMIT;

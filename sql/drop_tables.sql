--Löscht die alten Tabellen, falls man sie ersetzten/ändern will

BEGIN TRANSACTION;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS user;
COMMIT;
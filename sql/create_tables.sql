--mit dieser Datei werden die benötigten Tabellen erstellt. Sollte man eine Tabelle hinzufügen zu der Liste sollte man die alten erstmal löschen, damit sie sihc nicht doppeln -> mit Delete Datei
BEGIN TRANSACTION;
--City-Tabelle
CREATE TABLE IF NOT EXISTS city (
    name TEXT PRIMARY KEY NOT NULL,
    description TEXT NOT NULL,
    image_path TEXT
); 



--User-Tabelle
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL 
);

--Review-Tabelle
CREATE TABLE IF NOT EXISTS review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL,
    username TEXT, -- wenn du später Users integrierst
    overall_rating INTEGER NOT NULL,
    uni_rating INTEGER,
    freetime_rating INTEGER,
    nightime_rating INTEGER,
    campus_life_rating INTEGER,
    transportation_rating INTEGER,
    cost_rating INTEGER,
    living_rating INTEGER,
    workopportunities_rating INTEGER,
    safety_rating INTEGER,
    food_rating INTEGER,
    comunication_rating INTEGER,
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(city_name) REFERENCES city(name),
    FOREIGN KEY(username) REFERENCES user(username)
);

--Tabelle für das Bulletin Board
CREATE TABLE IF NOT EXISTS bulletin(
    bulletin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL,
    username TEXT NOT NULL,
    message TEXT NOT NULL,
    bulletin_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(city_name) REFERENCES city(name),
    FOREIGN KEY(username) REFERENCES user(username)
);
COMMIT;

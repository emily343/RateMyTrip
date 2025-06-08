BEGIN TRANSACTION;
--City-Tabelle
CREATE TABLE IF NOT EXISTS city (
    name TEXT PRIMARY KEY NOT NULL,
    description TEXT NOT NULL,
    image_path TEXT
); 
COMMIT;


--User-Tabelle
CREATE TABLE IF NOT EXISTS user (
    username TEXT PRIMARY KEY NOT NULL UNIQUE,
    password TEXT NOT NULL 
);

--Review-Tabelle
CREATE TABLE IF NOT EXISTS review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name INTEGER NOT NULL,
    user_id INTEGER, -- wenn du später Users integrierst
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
    FOREIGN KEY(city_name) REFERENCES city(name)
);
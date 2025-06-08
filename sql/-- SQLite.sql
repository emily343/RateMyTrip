--Datei um DB anpassen
-- Bestehende flasche Einträge löschen
DELETE FROM city WHERE name = 'Istanbul';
DELETE FROM city WHERE name = 'Copenhagen';

-- Neue richtige Einträge einfügen
INSERT INTO city (name, description, image_path)
VALUES (
    'Istanbul',
    'Istanbul is a vibrant city that bridges Europe and Asia, rich in history and culture. Famous landmarks like the Hagia Sophia and the Blue Mosque showcase its unique blend of Byzantine and Ottoman heritage.',
    'istanbul_pic.jpg'
);

INSERT INTO city (name, description, image_path)
VALUES (
    'Copenhagen',
    'Copenhagen is known for its high quality of life, bike-friendly streets, and rich Danish culture. The city blends modern design with historical charm.',
    'copenhagen.webp'
);

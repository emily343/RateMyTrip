--Datei die genutzt wird um Änderungen durch SQL-Statements an der DB durchzuführen 

UPDATE city
SET image_path = CASE
    WHEN name = 'Berlin' THEN 'berlin_pic.jpg'
    WHEN name = 'Barcelona' THEN 'barcelona.jpg'
END
WHERE name IN ('Berlin', 'Barcelona');




BEGIN TRANSACTION;



INSERT INTO city (name, description, image_path)
VALUES 

  ('Barcelona', 'Barcelona is a vibrant city on the Mediterranean coast, known for its unique architecture and student-friendly atmosphere. With top universities like Universitat de Barcelona, it offers a dynamic Erasmus experience and a sunny lifestyle.', 'barcelona_jpg'),
  
  ('Berlin', 'Berlin combines rich history with a modern, creative vibe. The city is home to many universities such as Humboldt University and offers affordable living, a diverse culture, and countless opportunities for international students.', 'berlin_pic_jpg'),
  
  ('Lisbon', 'Lisbon is a picturesque coastal city with a laid-back lifestyle and welcoming people. Erasmus students enjoy the mild climate, affordable prices, and academic options at Universidade de Lisboa and other institutions.', 'lisbon.jpeg'),
  
  ('Prague', 'Prague is known for its fairy-tale architecture and excellent universities like Charles University. The city offers a low cost of living, a strong Erasmus network, and a central location in Europe.', 'prague.jpg'),
  
  ('Vienna', 'Vienna offers high academic standards and quality of life. The city blends classical charm with modern student life and is home to institutions like the University of Vienna, popular among Erasmus students.', 'vienna.webp'),
  
  ('Budapest', 'Budapest stands out with its stunning architecture and affordable student lifestyle. Erasmus students benefit from vibrant nightlife, great public transport, and universities like Eötvös Loránd University.', 'budapest_pic.jpg'),
  
  ('Amsterdam', 'Amsterdam is a progressive, international city with top-ranked universities. It is known for its open-mindedness, bike culture, and English-taught study programs that attract many Erasmus students.', 'amsterdam_pic.jpg'),
  
  ('Warsaw', 'Warsaw is a growing Erasmus hub in Eastern Europe. It offers modern infrastructure, respected universities like the University of Warsaw, and a friendly atmosphere for international students.', 'warsaw.jpg'),
  
  ('Milan', 'Milan is Italy’s fashion and business capital, but also a strong academic center. Erasmus students enjoy cultural diversity, dynamic city life, and study opportunities at institutions like Università degli Studi di Milano.', 'milan.jpg'),
  
  ('Copenhagen', 'Copenhagen offers a clean, modern, and safe environment with world-class education. It’s ideal for students who value sustainability, design, and a high quality of life during their Erasmus exchange.', 'copenhagen.webp');




INSERT INTO user (username, password)
VALUES
    ('sarah', 'passwort1234'),
    ('emmy', 'passwort1234');


INSERT INTO review (
    city_name, username, overall_rating, uni_rating, freetime_rating, nightime_rating,
    campus_life_rating, transportation_rating, cost_rating, living_rating,
    workopportunities_rating, safety_rating, food_rating, comunication_rating, comment
) VALUES 
    ('Berlin', 'sarah', 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 'Berlin is great for students!'),
    ('Amsterdam', 'emmy', 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 'Beautiful city with good infrastructure.');
COMMIT;


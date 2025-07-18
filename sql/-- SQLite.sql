--Datei die genutzt wird um Änderungen durch SQL-Statements an der DB durchzuführen 
-- Descriptions, die vorherigen descriptions ersetzt
-- Creating City description (ChatGPT Quelle [4]) -->

UPDATE city SET description = 'Amsterdam is a vibrant and open-minded city, popular among Erasmus students for its high-quality universities and diverse international community. With its bike-friendly streets and rich cultural scene, it''s perfect for both study and exploration.' WHERE name = 'Amsterdam';

UPDATE city SET description = 'Barcelona offers Erasmus students a dynamic mix of academic excellence and Mediterranean lifestyle. From Gaudí’s architecture to sunny beaches, the city blends culture and fun effortlessly.' WHERE name = 'Barcelona';

UPDATE city SET description = 'Berlin is a top Erasmus destination thanks to its affordable cost of living, progressive vibe, and strong academic institutions. Its rich history and creative energy make it an inspiring place to study.' WHERE name = 'Berlin';

UPDATE city SET description = 'As the heart of the EU, Brussels offers a unique Erasmus experience with international connections and multilingual culture. The city combines historical charm with a lively student atmosphere.' WHERE name = 'Brussels';

UPDATE city SET description = 'Budapest is an emerging Erasmus hotspot known for its stunning architecture, thermal baths, and low living costs. The vibrant nightlife and friendly locals make it a student favorite.' WHERE name = 'Budapest';

UPDATE city SET description = 'Copenhagen offers a high standard of living and modern academic facilities for Erasmus students. Its sustainable lifestyle and cozy urban vibe make it an ideal place for international exchange.' WHERE name = 'Copenhagen';

UPDATE city SET description = 'Helsinki combines innovative education with a calm, safe environment perfect for Erasmus students. The city’s nature-focused lifestyle and modern design create a unique Nordic experience.' WHERE name = 'Helsinki';

UPDATE city SET description = 'Istanbul offers Erasmus students a rich blend of European and Asian influences, with a deep historical legacy. Its dynamic culture and hospitality make for an unforgettable exchange.' WHERE name = 'Istanbul';

UPDATE city SET description = 'Krakow is a charming, affordable Erasmus destination with a strong student community and rich cultural heritage. Its medieval old town and vibrant nightlife make it a favorite in Eastern Europe.' WHERE name = 'Krakow';

UPDATE city SET description = 'Lisbon is known for its sunny weather, relaxed pace of life, and welcoming locals. Erasmus students enjoy its ocean views, colorful neighborhoods, and lively social scene.' WHERE name = 'Lisbon';

UPDATE city SET description = 'Lyon offers a perfect mix of academic prestige and French lifestyle. With its beautiful old town and strong culinary culture, it’s an enriching destination for Erasmus students.' WHERE name = 'Lyon';

UPDATE city SET description = 'Milan blends Italian fashion, business, and education, making it a cosmopolitan choice for Erasmus students. The city’s fast pace is balanced by cultural treasures and social life.' WHERE name = 'Milan';

UPDATE city SET description = 'Paris offers world-renowned universities and a culturally rich setting for Erasmus students. From cafés to museums, the city invites intellectual and artistic exploration.' WHERE name = 'Paris';

UPDATE city SET description = 'Prague is a fairy-tale city known for its beauty, affordability, and welcoming atmosphere. Erasmus students are drawn to its historic charm and buzzing student life.' WHERE name = 'Prague';

UPDATE city SET description = 'Rome offers an unforgettable Erasmus experience with ancient ruins, delicious food, and world-class education. The city’s timeless beauty makes studying there a unique adventure.' WHERE name = 'Rome';

UPDATE city SET description = 'Seville is a warm, vibrant Erasmus destination known for its flamenco spirit and friendly locals. Its historic charm and sunny climate make student life especially enjoyable.' WHERE name = 'Seville';

UPDATE city SET description = 'Thessaloniki is a lively Greek city with a youthful energy and strong Erasmus culture. Its coastal vibe, great food, and relaxed lifestyle are perfect for international students.' WHERE name = 'Thessaloniki';

UPDATE city SET description = 'Valencia offers Erasmus students beautiful beaches, modern universities, and a laid-back Mediterranean lifestyle. The city’s festivals and outdoor life add to its appeal.' WHERE name = 'Valencia';

UPDATE city SET description = 'Vienna is a cultural capital with top-ranked universities and a high quality of life. Its mix of tradition and modernity offers Erasmus students a balanced and enriching stay.' WHERE name = 'Vienna';

UPDATE city SET description = 'Warsaw is a growing Erasmus destination with a dynamic student scene and affordable living. Its mix of history, innovation, and nightlife creates a well-rounded exchange experience.' WHERE name = 'Warsaw';

ALTER TABLE user ADD COLUMN name TEXT;
ALTER TABLE user ADD COLUMN age INTEGER;
ALTER TABLE user ADD COLUMN interests TEXT;
ALTER TABLE user ADD COLUMN about TEXT;

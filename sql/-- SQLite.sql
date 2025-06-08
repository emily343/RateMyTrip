DELETE FROM review WHERE id IN (1, 2);

INSERT INTO review (
    id, city_name, user_id, overall_rating, uni_rating, freetime_rating, nightime_rating,
    campus_life_rating, transportation_rating, cost_rating, living_rating,
    workopportunities_rating, safety_rating, food_rating, comunication_rating, comment, created_at
) VALUES
(
    1, 'Berlin', 'sarah',
    5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
    'Berlin is great for students!',
    '2025-06-08 11:27:24'
),
(
    2, 'Amsterdam', 'emmy',
    5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
    'Beautiful city with good infrastructure.',
    '2025-06-08 11:27:24'
);

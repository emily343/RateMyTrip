---
title: Data Model
parent: Technical Docs
nav_order: 2
---

{: .label }
[Sarah Abdulsayed]

{: .no_toc }
# Data model

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Data Model

Our `ratemytrip.sqlite` database defines the structure of the application. It consists of four tables that were defined in the SQL script "create_tables.sql".
All tables are created with `IF NOT EXISTS` to avoid duplication

---

### `city`
This table stores the information about the cities that users can find on our application. 

| Column       | Type | Constraints                    | Description/Info |
|--------------|------|--------------------------------|-------------|
| `name`       | TEXT | `PRIMARY KEY`, `NOT NULL`      | Unique name of the city (used as ID in URLs) |
| `description`| TEXT | `NOT NULL`                     | A short textual description of the city |
| `image_path` | TEXT | *(optional)*                       | Path to a city image file, stored in the `/static/` folder |


**Usage in the App:**
- Provides the content that fills the city.overview in our city pages.
- Our City sites (`/city/<name>`) are generated based on this data.
- Acts as the reference point for all related reviews and bulletin board entries.


**Relationships:**
- Referenced by `review.city_name` and `bulletin.city_name`



---

### `user`
Stores user credentials for authentication.

| Column     | Type     | Constraints                          | Description |
|------------|----------|--------------------------------------|-------------|
| `id`       | INTEGER  | `PRIMARY KEY AUTOINCREMENT`          | Unique user ID |
| `username` | TEXT     | `NOT NULL`, `UNIQUE`                 | Unique username |
| `password` | TEXT     | `NOT NULL`                           | password  |

**Usage in the App:**
- Enables log-in and registration in our app.

**Relationships:**
- Referenced by `review.username` and `bulletin.username`


---

### `review`
Stores user-submitted and by us inserted ratings for a city, across multiple categories.
| Column                      | Type      | Constraints                     | Description |
|-----------------------------|-----------|----------------------------------|-------------|
| `id`                        | INTEGER   | `PRIMARY KEY AUTOINCREMENT`      | Unique review ID |
| `city_name`                 | TEXT      | `NOT NULL`, `FOREIGN KEY`       | References `city.name` |
| `username`                  | TEXT      | *(optional)* `FOREIGN KEY`      | References `user.username` |
| `overall_rating`            | INTEGER   | `NOT NULL`                       | General overall score |
| `uni_rating`                | INTEGER   | *(optional)*                     | Rating for university life |
| `freetime_rating`           | INTEGER   | *(optional)*                     | Rating for Leisure activities |
| `nightime_rating`           | INTEGER   | *(optional)*                     |Rating for  Nightlife experience |
| `campus_life_rating`        | INTEGER   | *(optional)*                     | Rating for Campus atmosphere and experience|
| `transportation_rating`     | INTEGER   | *(optional)*                     | Rating for Public transport |
| `cost_rating`               | INTEGER   | *(optional)*                     | Rating for Living costs |
| `living_rating`             | INTEGER   | *(optional)*                     |Rating for Housing quality and availability |
| `workopportunities_rating`  | INTEGER   | *(optional)*                     | Rating for availability of  Job/internship opportunities |
| `safety_rating`             | INTEGER   | *(optional)*                     | Rating for  Safety in the city |
| `food_rating`               | INTEGER   | *(optional)*                     | Rating for  Local food and options |
| `comunication_rating`       | INTEGER   | *(optional)*                     | Rating for  Communication with others  |
| `comment`                   | TEXT      | *(optional)*                     | Free-form feedback |
| `created_at`                | TIMESTAMP | `DEFAULT CURRENT_TIMESTAMP`      | Auto-set timestamp on submission |

**Usage in the App:**
- Reviews from this table are displayed on each city page under **"Reviews about `<city_name>`"**.
- New reviews are added via the review form at `/review/<city_name>`.
- Ratings are visualized in cards and charts to provide quick insight into different aspects of student life.

**Relationships:**
- References `city.name` and `user.username`.


---

### `bulletin`
This table stores public messages that were posted on the black-boards for each city, which are only accessible to logged-in users. Each message on it is linked to the specific city and a user.

| Column         | Type      | Constraints                     | Description |
|----------------|-----------|----------------------------------|-------------|
| `bulletin_id`  | INTEGER   | `PRIMARY KEY AUTOINCREMENT`      | Unique ID for each message |
| `city_name`    | TEXT      | `NOT NULL`, `FOREIGN KEY`       | References `city.name` |
| `username`     | TEXT      | `NOT NULL`, `FOREIGN KEY`       | References `user.username` |
| `message`      | TEXT      | `NOT NULL`                       | Text content of the message |
| `bulletin_time`| TIMESTAMP | `DEFAULT CURRENT_TIMESTAMP`      | Time the message was posted |

**Usage in the App:**
- Each entry of this table is shown in  `/bulletin/<city_name>`.

**Relationships:**
- References `city.name` and `user.username`.

---
### Relationships Summary

- `review.city_name` and `bulletin.city_name` reference `city.name`
- `review.username` and `bulletin.username` reference `user.username`

--- 
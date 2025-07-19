---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
Sarah Abdulsayed

{: .no_toc }
# Reference documentation

This page documents all available routes and internal functions used in our web application.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Routes

### `home()`

**Route:** `/`  
**Methods:** `GET`  
**Purpose:** Displays the homepage.

**Sample output:**  
![`home()` sample](static/images/images_outputs/homepage.png)


---

### `profile()`

**Route:** `/profile`  
**Methods:** `GET`  
**Purpose:** Displays the profile page of the currently logged-in user.  
**Authentication required**

**Requires login**

**Sample output:**  
![`/profile` sample](static/images/images_outputs/profile.png)


---

### `user()`

**Route:** `/user/<username>`  
**Methods:** `GET` , `POST` 
**Purpose:** Displays the profile page of the user that wrote the message on the bulletin board.  
**Authentication required**

**Requires login**

**Sample output:**  
![`/profile` sample](static/images/images_outputs/profile_bulletin.png)


---

### `search()`

**Route:** `/search`  
**Methods:** `GET`, `POST`  
**Purpose:** Displays a search form to look for cities by name. If a valid city is entered, redirects to `/city/<city_name>`.

**Sample output:**  
![Search Page](static/images/images_outputs/search.png)


---

### `city_view(city_name)`

**Route:** `/city/<city_name>`  
**Methods:** `GET`  
**Purpose:** Displays details about a city and its reviews.

**Sample output:**  
![City Page](static/images/images_outputs/city.png)


---

### `review(city_name)`

**Route:** `/review/<city_name>`  
**Methods:** `GET`, `POST`  
**Purpose:** Displays a form to submit a new review for a specific city.  
**Requires login**

**Sample output:**  
![Review Page](static/images/images_outputs/submit_review.png)


---

### `bulletin(city_name)`

**Route:** `/bulletin/<city_name>`  
**Methods:** `GET`, `POST`  
**Purpose:** Allows logged-in users to view and post public messages on the bulletin board for a city.

**Requires login**

**Sample output:**  
![Bulletin Page](static/images/images_outputs/bulletin.png)


---

### `register()`

**Route:** `/register`  
**Methods:** `GET`, `POST`  
**Purpose:** Allows new users to create an account with a username and password.

**Sample output:**  
![Register Page](static/images/images_outputs/register.png)


---

### `login()`

**Route:** `/login`  
**Methods:** `GET`, `POST`  
**Purpose:** Authenticates existing users and starts a session.

**Sample output:**  
![Login Page](static/images/images_outputs/login.png)


---

### `logout()`

**Route:** `/logout`  
**Methods:** `GET`  
**Purpose:** Logs out the current user and redirects to login page.

**Sample output:**  
None (redirects)


---

### `run_insert_sample()`

**Route:** `/insert/sample`  
**Methods:** `GET`  
**Purpose:** Fills database with sample data using `insert_sample()` from `db.py`.
_For development/testing purposes only._

**Sample output:**  
Text return: `Data added to Database.`


---


## Internal Functions


### `load_user(user_id)`

**Purpose:** Callback function used by Flask-Login to load current user.

**Returns:**  
`User.get(user_id)`



### `User.get(user_id)`

**Purpose:** Retrieves a user object from the database using the user ID. Used for Flask-Login session handling.

**Returns:**  
A `User` object if found.

---
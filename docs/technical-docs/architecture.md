---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
Emily Apitzsch

{: .no_toc }
# Architecture

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Overview

CityRate is a web application that allows students and young travellers to search for cities for their Erasmus stay. Users can see an overview of the city, read and write reviews about cities, and interact on a bulletin board. The idea is to give students a platform to share personal travel and study experiences and look for tips from other students. 

The Web-Application is built using Flask as the main web framework. We use Jinja2 templates to render the HTML pages. The backend logic, which includes the route handling and form processing, is implemented with Python using Flask. To store the data, we use an SQLite database and access it through 'plain' SQL-Queries. To manage user input we use Flask-WTF, and the styling of the pages is handled with Bootstrap and CSS. 

## Codemap

Our project is structured in separated files and folders, that are each responsible for a specific function in our web-application. Below you will find an overview of the most important parts. 

### `app.py`

App.py is the main entry point of the appliation. It initializes the Flask app with all the important flask extensions, such as Flask-Login for the user sessions and Flaks-WTF for form handling. It also implements the route logic and connects the templates with the backend logic. 

### `forms.py`

Forms.py contains all WTForms form classes used for user input, such as user registration and login, city search and reviews. Using FLask-WTF helps us manage validation and rendering the forms.

### `db.py`

Db.py handles the conection the the SQLite database. It contains the functions for executing SQL-Queries and to open and close connections to the database.

### `sql/`

This folder contains the SQL scripts that were used during the development to set up and reset the database. In create_tables.sql, we initialized the database by creating the tables. In Insert_sample.sql, we added initial sample data to our database, such as cities and users. The file --SQLite-sql was used to change the data or the tables in our database. 

### `templates/`

The template folder contains all HTML templates that were rendered using Jinja2. Each template was made for a specific page in our web-app, such as the city-page (city.html), the homepage (home.html) or the review-page (review.html). Each route has a corresponding template. 

### `static/`

This folder contains the the images for the cities (in images/) and our css-stylesheet. 


## Cross-cutting concerns

**Authentication and User Sessions:**

- We use Flask-Login to manage user-sessions and protect the routes that user can only access if they are logged in 
- Manage sessions across the entire app (e.g. by restricting access to certain routes, such as access profile and write reviews)
- Define User class that inherits from UserMixin to work with Flask-Login
- Current user can be accesssed through 'current_user' 
- Routes that need authentication use '@login_required' decorator

more about the Design Decision [here](../design-decisions.md#05-using-flask-login-for-user-authentication)

**Form Handling:**

- We implemented forms that require user-input using Flask-WTF und WTForms
- Built-in validation and CSRF protection
- Form fields and validation are defined in forms.py
- Routes in app.py processes form input by handling the logic and validation results
- Templates (e.g. review.html or bulletin.html) display form 

more about the Design Decision [here](../design-decisions.md#04-using-flask-wtf-for-form-handling) 

**Styling with Bootstrap and CSS:**

- We use [Bootstrap](../design-decisions.md#03-using-bootstrap-for-styling-and-layout) for a responsive and consistent Layout 
- All templates include Bootstrap
- Bootstrap copmonents, such as container, card, btn and navbar, are reused in nearly all templates 
- Styling logic is centralized, [custom CSS](../design-decisions.md#01-centralizing-css-styling-in-style.css) is used for spacing and colors 


**Database access:**

- We use plain SQL queries to acess SQLite database
- SQL-Queries are used directly in route functions inside app.py to access data in the database (e.g. to load reviews)
- Influences backend and frontend, determines what data is available for templates

more about the Design Decision [here](../design-decisions.md#02-using-plain-sql-or-orm-to-access-database) 

**Flash Messages:**

- We used Flask flash() function
- Used to give user feedback for actions like login or registration
- Example: "Wrong username or password. Try again"
- Written in app.py routes and displayed using 'render_messages()' in templates











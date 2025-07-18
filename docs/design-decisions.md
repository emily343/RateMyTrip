---
title: Design Decisions
nav_order: 3
---

{: .label }
Sarah Abdulsayed, Emily Apitzsch

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Centralizing CSS Styling in style.css

### Meta

Status
: Decided

Updated
: 01-May-2025

### Problem statement

We needed to apply custom styles (e.g., padding, font, image size) without making HTML templates too crowded and repetitive.


### Decision

We created a central CSS file (static/css/style.css) and used it for all templates. Only page-specific styles are defined in each template.


### Regarded options

+ style in every HTML file
+ Centralized CSS file

| Criterion |  In HTML | External CSS |
| --- | --- | --- |
| **Maintainability** | ❌ Hard to manage  | ✔️ Easy to change |
| **Reusability** | ❌ None | ✔️ Styles can be reused |

---
## 02: Using Plain SQL or ORM to access database

### Meta

Status
: Decided

Updated
: 15-May-2025

### Problem statement

In our project we need to interact with a database, for example, to get city pictures or save user reviews. The question is if we use plain SQL or use SQLAlchemy as object-relational mapper.

### Decision 

We decided to use plain SQL. 

The main reasosn is that our group has plenty of experience using plain SQL, but no prior experience with ORM tools like SQLAlchemy. To make the best use of our learning capacities, we chose to focus on technologies that are essential and cannot easily be replaced (such as Bootstrap or WTForms).

### Regarded options

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Knowledge** | ✔️ We can already use it  | ❌ We must learn it from scartch |
| **Readabilitya** | ✔️ SQL is directly visible in code | ❌ SQL is abstract |

---
## 03:  Using Bootstrap for Styling and Layout

### Meta

Status
: Decided

Updated
: 05-Jun-2025

### Problem statement

We need an appealing and responsive layout for our web application. Instead of creating layout manually using CSS, which would be immensely time consuming, we want to use a CSS framework.


### Decision 

We decided to use Bootstrap to handle layout, styling, and component structure.

Bootstrap provides pre-styled components (e.g., navbar, carousel), which helps us implement a consistent and appealing UI faster.


### Regarded options

+ Manually written CSS and HTML structure
+ Bootstrap framework

| Criterion | Manually written CSS  | Bootstrap framework |
| --- | --- | --- |
| **Development Speed** | ❌ Time consuming  | ✔️ Fast |
| **Responsiveness** | ❌ Needs to be manually implemented  | ✔️ Built in |
| **Design** | ❌  Inconsitent | ✔️ Consistent and appealing |

---
## 04: Using Flask-WTF for Form Handling

### Meta

Status
: Decided

Updated
: 05-Jun-2025

### Problem statement

Our web application requires forms for several purposes. For example for searching for cities and submitting user reviews. Handling forms using plain HTML  can quickly become error-prone and repetitive. We needed a better way to manage forms.


### Decision 

We decided to use Flask-WTF, a Flask extension that integrates WTForms into Flask.

Using Flask-WTF, we define each form as a separate Python class in forms.py. This keeps the form logic such as validation rules, field types, and labels separated from the HTML templates, which improves maintainability and readability.
The form instance is then passed to the template via the route function in app.py.

### Regarded options

+ HTML forms with manual handling
+ Flask-WTF with WTForms

| Criterion | Manual HTML Form | Flask-WTF |
| --- | --- | --- |
| **Validation** | ❌ Must be implemented manually  | ✔️ Built-in |
| **Maintainability** | ❌ Code spread across HTML and Python  | ✔️ Seperated |
| **Security** | ❌  No CSRF protection by default | ✔️ Built-in CSRF token |

---
## 05: Using Flask-Login for User Authentication

### Meta

Status
: Decided

Updated
: 18-Jun-2025

### Problem statement

Our web application requires user authentication to allow users to write reviews or messages, manage their profile and give access to certain pages only to logged in users. We needed a simple way to manage user login sessions and to protect the pages from unauthorized access. 


### Decision 

We decided to use Flask-Login, a Flask extension that provides user session management. Flask-Loging helps us to manage user sessions and remembering which user is logged in. It protects the routes using @login-required and helps us access the current user easily through 'current_user'. 
Overall, using Flask-Login offered us an easier and more secure way to implement the Login and Logout functionality. 



### Regarded options

+ Manual Session Handling
+ Flask-Login

| Criterion | Manual Session Handling | Flask-Login |
| --- | --- | --- |
| **Logic for Authentication** | ❌ Must be implemented manually  | ✔️ Built-in |
| **Protecting Routes** | ❌ manual checks each time  | ✔️ use of @login_required |
| **Current User Access** | ❌  implement manually | ✔️ current_user built-in |

---

## 06: Not using base.html

### Meta

Status
: Decided

Updated
: 18-Jun-2025

### Problem statement

Flask with Jinja allows the use of a base.html template to define shared layout components, so individiual pages can extend the base.html for a common structure.
In the beginning we thought our project was small enough that we would not need a base template, and that it would be easier to write each page individually. 

### Decision 

We decided not to implement a base.html. Instead, we repeated the shared html-structures, such as the navigation bar, in every page. At first, this helped us make faster progress in the beginning. As the project grew, we noticed that it resulted in repetitive code. Updating shared elements became more time-consuming.  
We have recognized that this approach was not the best way and we would do it differently in future projects. 


### Regarded options

+ no base.html
+ use base.html

| Criterion | no base.html| use base.html |
| --- | --- | --- |
| **Initial Work** | ✔️  simpler at first  |  ❌ slightly more effort to set up |
| **Maintain Code** | ❌ harder to maintain | ✔️ easier to update |
| **Readability** | ❌  repetitive code, longer templates | ✔️ 'cleaner' templated |

## 07: Using Flash Messages

### Meta

Status
: Decided

Updated
: 19-Jun-2025

### Problem statement

To give our users feedback on actions when registering or logging in/out of the account, we wanted a way to show them the status of the action (e.g if the login succeeded or failed).

### Decision 

We decided to use Flask's flash-messages. Flash-messages allows us to display temporary messages in an easy and efficient way. It keeps the user informed and improves their usability. 


### Regarded options

+ manually implement a messaging system
+ use Flask flash()

| Criterion | manual system| Flask Flash |
| --- | --- | --- |
| **Easiness to use** | ❌ more effort to implement   | ✔️ built-in and easy to use |
| **Integration** | ❌ harder to integrate | ✔️ easier to inegrate |


## 08: Include Instance Folder in Git 

### Meta

Status
: Decided

Updated
: 19-Jun-2025

### Problem statement

It is recommended to keep the instance-folder  out of version control, because it often contains sensitive data and the database. However, during the development as a team, it might be helpful to share the database in the repository. 

### Decision 

For now, we decided to include the instance-folder in Git. This allows for all team members to access the same database file during the development of our web-application. We know that in a 'real-life' project it is not recommended, where we would then add it to the .gitignore file. 


### Regarded options

+ keep instance-folder in .gitignore
+ include instance-folder in version control

| Criterion | keep instance-folder in .gitignore| include instance-folder |
| --- | --- | --- |
| **Security** | ✔️  secure, sensitive data not shared |  ❌ sensitive data exposed |
| **Development Convenience** | ❌ needs manual setup | ✔️ easier to share database |


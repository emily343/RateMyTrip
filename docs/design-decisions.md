---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

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
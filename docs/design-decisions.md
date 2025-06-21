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
: 21-Jun-2025

### Problem statement

We needed to apply custom styles (e.g., padding, font, image size) without makung HTML templates too crowded. and .


### Decision

We created a central CSS file (static/css/style.css) and used it for all templates. Only very page-specific styles are defined in each template.


### Regarded options

+ <style> in every HTML file
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
: 21-Jun-2025

### Problem statement

In our project we need to interact with a database, for example, to get city pictures or save user reviews. The question is if we use plain SQL or use SQLAlchemy as object-relational mapper.

### Decision

We decided to use plain SQL. 

The main reasosn is that our group has plenty of experience using plain SQL but none using ORM. Therefore it is better to focus our resources regarding learning new technologies on crusical ones that we can not replace (such as Bootstrap or WTForms).

### Regarded options

+ Plain SQL
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Knowledge** | ✔️ We can already use it  | ❌ We must learn it from scartch |
| **Readabilitya** | ✔️ SQL is directly visible in code | ❌ SQL is abstract |
# RateMyTrip 

**RateMyTrip** is a web application that creates a travel community where users can share city reviews, rate destinations, and connect via a public bulletin board. Most content is publicly viewable, but users must be logged in to post reviews or messages.

## Features

- User-generated city reviews and ratings
- Public bulletin board for travel discussions
- User authentication (register/login) via Flask-Login
- Responsive UI using Bootstrap and Jinja2
- SQLite database to store users, cities, reviews, and messages

---

## Tech 

- **Backend:** Flask (Python)
- **Frontend:** Jinja2, Bootstrap
- **Forms:** Flask-WTF, WTForms
- **Database:** SQLite (via Flask-SQLAlchemy)

---

## Requirements

- Python 3.10+
- Virtual Environment
- Packages as listed in `requirements.txt`

---

## Setup & Run Instructions

1. **Clone or download the repository**
   git clone <repo-url>


2. **Create and activate a virtual environment**
   Windows: python -m venv venv
   Mac: python3 -m venv venv
   
3. **Install required packages**
   pip install -r requirements.txt

4. **Run the app**
   flask run

---

## Structure

Your project should now look like this (simplified):

RateMyTrip/
├── docs/
├── instance/
├── sql/
├── static/
    └── CSS/
    └── Images/
├── templates/
│   ├── bulletin.html
│   ├── city.html
│   └── ...
├── venv/
    ├── ...
    └── ...
├── app.py
├── forms.py
├── db.py
├── requirements.txt
└── README.md

---

## Login

You can only view certain pages and use certain functions when logged in. You can either create your own account or use these test-credentials:

Username: testuser
Password: test1234


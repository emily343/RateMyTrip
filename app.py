from flask_bootstrap import Bootstrap5 #(1.)
import db
import os
from forms import SearchCityForm, ReviewForm #Formulare werden von forms importiert
from db import get_db_con
from flask import Flask, render_template, redirect, url_for





app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    DATABASE = os.path.join(app.instance_path, 'ratemytrip.sqlite'),
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'  # (2.)
)
app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)

bootstrap = Bootstrap5(app)  # (3.)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/search', methods=['GET', 'POST']) #Route zeigt Suchformular an und verarbeitet es mit Get und Post
def search():
    form = SearchCityForm()  #  zuerst das Formular erstellen
    if form.validate_on_submit(): #Prüft valide Absendung
        city = form.cityField.data.strip()  #holt Eingabe und speichert sie als city
        print(f"User requested city: '{city}'")
        return redirect(url_for('city_view', city_name=city)) #fehlt noch, führt dann zur Seite der City
    return render_template('search.html', form=form)


@app.route('/city/<city_name>', methods=['GET', 'POST'])
def city_view(city_name):
    if not city_name:
        return "No city specified", 400

    db_con = get_db_con()
    city = db_con.execute(
        'SELECT * FROM city WHERE LOWER(name) = LOWER(?)',
        (city_name.lower(),)  # Optional: gleich `.lower()` mitgeben
    ).fetchone()

    if city is None:
        print("City not found in DB.")
        return "City not found", 404

    form = ReviewForm()

    if form.validate_on_submit():
        db_con.execute("""
            INSERT INTO review (
                city_name,
                overall_rating,
                uni_rating,
                freetime_rating,
                nightime_rating,
                campus_life_rating,
                transportation_rating,
                cost_rating,
                living_rating,
                workopportunities_rating,
                safety_rating,
                food_rating,
                comunication_rating,
                comment
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            city['name'], #übernimmt name von Seite
            form.overall_rating.data,
            form.uni_rating.data,
            form.freetime_rating.data,
            form.nightime_rating.data,
            form.campus_life_rating.data,
            form.transportation_rating.data,
            form.cost_rating.data,
            form.living_rating.data,
            form.workopportunities_rating.data,
            form.safety_rating.data,
            form.food_rating.data,
            form.comunication_rating.data,
            form.comment.data
        ))
        db_con.commit()
        return redirect(url_for('city_view', city_name=city_name))

    # Bewertungen anzeigen
    reviews = db_con.execute(
        'SELECT * FROM review WHERE city_name = ? ORDER BY created_at DESC',
        (city['name'],)
    ).fetchall()

    return render_template('city.html', city=city, form=form, reviews=reviews)



@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.route('/insert/images')
def insert_images():
    db.insert_image_paths()
    return 'Bilderpfade wurden ergänzt.'

@app.route('/db/add_image_column')
def add_image_column():
    db.add_image_column()
    return "Spalte 'image_path' wurde hinzugefügt."

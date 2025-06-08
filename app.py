from flask_bootstrap import Bootstrap5 #(1.)
import db
import os
from forms import SearchCityForm #Formular wird von forms importiert
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
    form = SearchCityForm() #Formularobjekt wird erzeugt
    if form.validate_on_submit(): #Prüft valide Absendung
        city = form.cityField.data #holt Eingabe und speichert sie als city
        return redirect(url_for('city_view', city_name=city)) #fehlt noch, führt dann zur Seite der City
    return render_template('search.html', form=form)

@app.route('/city/<city_name>')
def city_view(city_name):
    if not city_name:
        return "No city specified", 400
    
    db_con = get_db_con()
    city = db_con.execute(
        'SELECT * FROM city WHERE LOWER(name) = LOWER(?)', #damit es nicht case-sensitive ist
        (city_name,)
    ).fetchone()

    if city is None:
        return "City not found", 404

    return render_template('city.html', city=city)



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

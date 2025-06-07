from flask import Flask, render_template
from flask_bootstrap import Bootstrap5 #(1.)
import db
import os
from forms import SearchCityForm #Formular wird von forms importiert




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
        city = form.description.data #holt Eingabe und speichert sie als city
        return redirect(url_for('city', city_name=city)) #fehlt noch, führt dann zur Seite der City
    return render_template('search.html', form=form)


@app.route('/city')
def city():
    city_name = request.args.get('city_name', 'Unknown') #zeigt die Seite mit der Stadt als übergebenen Parameter von Search
    return render_template('city.html')

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

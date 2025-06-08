from flask_bootstrap import Bootstrap5 #(1.)
import db
import os
from forms import SearchCityForm, ReviewForm #Formulare werden von forms importiert
from db import get_db_con
from flask import Flask, render_template, redirect, url_for





app = Flask(__name__) #Erstellt die Flask-App

app.config.from_mapping( 
    SECRET_KEY = 'secret_key_just_for_dev_environment', #Sessions und CSRF-Schutz.Sessions und CSRF-Schutz
    DATABASE = os.path.join(app.instance_path, 'ratemytrip.sqlite'), #Pfad zur SQLite-Datenbank
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse' #Bestimmt das Styling-Theme von Bootstrap
)
app.cli.add_command(db.init_db) #Ermöglicht über das Terminal flask init-db auszuführen
app.teardown_appcontext(db.close_db_con) #Schließt DB-Verbindung am Ende des Requests 

bootstrap = Bootstrap5(app) #bindet Bootstrap in die Flask-App ein


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

#Suchformular
@app.route('/search', methods=['GET', 'POST']) #Route zeigt Suchformular über Get an und sendet es mit Post
def search(): #Funktion namen "search" wird definiert, die die Request verarbeitet
    form = SearchCityForm()  # Erstellt Instanz des Formulars (aus forms)
    if form.validate_on_submit(): #Prüft valide Absendung (ob Regeln in Forms definiert sind eingehalten wurden)
        city = form.cityField.data.strip()  #holt Eingabe und speichert sie als city
        return redirect(url_for('city_view', city_name=city)) #Weiterleistung zu City-Unterseite mit der gegebenen city als Parameter über Funktion city_view (in city-route definiert)
    return render_template('search.html', form=form) #wenn Request nicht erfolgreich wird Search-Seite wieder angezeigt
    #Übergabe des Form-Objekts, damit HTML-Seite auf  das WTForm-Objekt zugreifen kann



@app.route('/city/<city_name>', methods=['GET', 'POST']) #URL mit dynamischem Parameter city_name
#Methode Get (Seite anzeigen) und Post (Bewertung abschicken)

#City-Unterseite anzeigen
#Funktion namen "city_view" wird definiert, die die Request verarbeitet, Parameter der City in Search gegeben
def city_view(city_name):
    if not city_name: #Falls kein city_name übergeben wurde 
        return "No city choosen", 400

    db_con = get_db_con() #baut Vebrindung zur DB auf
    city = db_con.execute( #das folgende SQL-Statement wird ausgeführt
         #Städte aus DB, wo Name aus DB = Name des weiteregebenen Parameters
        'SELECT * FROM city WHERE LOWER(name) = LOWER(?)', #über Lower nicht mehr case-sensitive
        (city_name.lower(),)  #def des Platzhalters "?"
    ).fetchone() #über fetchone wird Datensatz der Stadt zurückgegeben

    if city is None: #wenn Stadt angegeben wurde, sie aber nicht in DB existiert
        #-> in city=db_con.execute() (darüber) nicht gefunden
        print("City not found in DB.") #printet Info in Terminal -> zur Fehlerbehebung
        return "City not found", 404 #gibt Fehlermeldung aus


    #Reviews senden und sehen
    #leeres WTForm-Objekt wird erstellt für das Bewertungsformular, das auf der Seite angezeigt wird
    form = ReviewForm()

    #prüft ob das Formular valide abgeschickt worden ist
    if form.validate_on_submit(): #wenn ja wird
         #wenn ja werden diese SQL-Statements durchgeführt
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
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) #Platzhalter
        """, (
            city['name'], #übernimmt Name der Stadt aus der DB
            form.overall_rating.data, #liest den Inhalt aus dem jeweiligen Feld und ersetzt damit Platzhalter
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
        db_con.commit() #Statements in DB commited
        return redirect(url_for('city_view', city_name=city_name)) #nach  Absenden des Formulars wird City-Unterseite neu geladen

    # Bewertungen anzeigen
    #keine If-Bedingung, wird immer gemacht bei Öffnung der Seite
    reviews = db_con.execute( #SQL-Statement durchgeführt
        #alle Reviews der Stadt angezeigt und nach Datum sortiert (absteigend)
        'SELECT * FROM review WHERE city_name = ? ORDER BY created_at DESC',
        (city['name'],) #Wert für ?-Platzhalter
    ).fetchall() #holt alle Ergebnisse der SQL-Abfrage auf einmal

    #Rendert das HTML-Template mit city->gegebene Stadt, die Review-Form und die reviews aus der DB
    return render_template('city.html', city=city, form=form, reviews=reviews)



@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/user')
def user():
    return render_template('user.html')

#benutzt um Daten manuell in DB einzufügen
@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()
    return 'Data added to Database.'

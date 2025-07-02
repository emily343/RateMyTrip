from flask import Flask, flash, render_template, redirect, request, url_for # Flask [1]
import flask
from flask_bootstrap import Bootstrap5 # Flask-Bootstrap5 [2]
import db
import os
from forms import BulletinForm, LoginForm, SearchCityForm, ReviewForm, RegisterForm #Formulare werden von forms importiert
from db import get_db_con
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user 


#Initialisiert eine neue Flask-App
app = Flask(__name__) 

#Konfiguriert die App
app.config.from_mapping( 
    #Sessions und CSRF-Schutz.Sessions und CSRF-Schutz
    SECRET_KEY = 'secret_key_just_for_dev_environment', 
    #Pfad zur SQLite-Datenbank
    DATABASE = os.path.join(app.instance_path, 'ratemytrip.sqlite'), 
    #Bestimmt das Styling-Theme von Bootstrap
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse' 
)

#Ermöglicht über das Terminal flask init-db auszuführen
app.cli.add_command(db.init_db)
#Schließt DB-Verbindung am Ende des Requests 
app.teardown_appcontext(db.close_db_con) 

#bindet Bootstrap in die Flask-App ein
bootstrap = Bootstrap5(app) 
    


#Flask Login initialisieren
 #lässt app und Flask-Login zusammen arbeiten
login_manager = LoginManager()
login_manager.init_app(app)


#Die Startseite (/) zeigt die home.html-Datei an
@app.route('/')
def home():
    return render_template('home.html')

#Diese Seite ist geschützt, nur für eingeloggte User
#Zeigt profile.html an
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


#Seite für das Bulletinboard
@app.route('/bulletin/<city_name>', methods=['GET', 'POST'])
@login_required
def bulletin(city_name):

    #Stellt DB-Verbindung her
    db_con = get_db_con()
    form = BulletinForm() 

    #Holt Stadt mit SQL-Query aus der Tabelle city (Case-Insensitive durch LOWER())
    #Stadt wo der Name aus DB = Name des weiteregebenen Parameters
    city = db_con.execute( 
        'SELECT * FROM city WHERE LOWER(name) = LOWER(?)', 
        #Def des Platzhalters "?"
        (city_name.lower(),)  
        #Über fetchone nur einen Datensatz einer Stadt zurückgegeben
    ).fetchone() 

    #Wenn Stadt angegeben wurde, sie aber nicht in DB existiert
    if city is None: 
        return "City not found", 404 
    
    """
    if form.validate_on_submit():

        message = 

    

        db_con.execute(
            INSERT INTO bulletin (city_name,username,message) VALUES (?,?,?) #Platzhalter
        , (
            city['name'], #Übernimmt Name der Stadt aus der DB
            user['username']
            form.message.data, #Liest den Inhalt aus dem jeweiligen Feld und ersetzt damit Platzhalter
          
        ))
        #Statements in DB commited
        db_con.commit()
    """

    return render_template('bulletin.html', city=city, form=form)






#Suchformular
#Route zeigt Suchformular über Get an oder sendet es mit Post
@app.route('/search', methods=['GET', 'POST']) 

#Funktion namen "search" wird definiert, die die Request verarbeitet
def search(): 
    #Erstellt Instanz des Formulars SearchCityForm (aus forms.py) mit dem Namen form
    #Diese wird in der html-Seite referenziert
    form = SearchCityForm()  

    #Prüft valide Absendung (ob die in Forms definierten Regeln eingehalten wurden)
    if form.validate_on_submit(): 
        #holt Eingabe aus cityField und speichert sie als city
        city = form.cityField.data.strip()  

        #Man wird zur URL weitergeleitet
        #Dabei wird die Funktion 'city_view' aufgerufen mit dem Stadtnamen als Paramter
        #Diese Funktion ist in @app.route('/city/<city_name>' definiert
        #Durch diese 'city_view'-Funktion wird die Stadtseite geladen
        return redirect(url_for('city_view', city_name=city)) 
    
    #Wenn Request nicht valude und man somit nicht zur 'city_view'-Funktion weitergeleitet wurde
    #Search-HTNL-Seite wieder angezeigt
    #Übergabe des Form-Objekts, damit HTML-Seite auf das WTForm-Formular zugreifen kann
    return render_template('search.html', form=form) 
    



#City-Unterseite
#URL mit dynamischem Parameter city_name (/city/Berlin, /city/Madrid usw.)
#Methode Get (Seite anzeigen) und Post (Bewertung abschicken)
@app.route('/city/<city_name>', methods=['GET', 'POST']) 


#City-Unterseite anzeigen
#Funktion namen "city_view" wird definiert 
def city_view(city_name):

    #Falls keine Stadt angegeben wurde: Fehler 400 (Bad Request)
    if not city_name: #Falls kein city_name übergeben wurde 
        return "No city chosen", 400

    
    #Stellt DB-Verbindung her
    db_con = get_db_con()

    #Holt Stadt mit SQL-Query aus der Tabelle city (Case-Insensitive durch LOWER())
    #Stadt wo der Name aus DB = Name des weiteregebenen Parameters
    city = db_con.execute( 
        'SELECT * FROM city WHERE LOWER(name) = LOWER(?)', 
        #Def des Platzhalters "?"
        (city_name.lower(),)  
        #Über fetchone nur einen Datensatz einer Stadt zurückgegeben
    ).fetchone() 

    #Wenn Stadt angegeben wurde, sie aber nicht in DB existiert
    if city is None: 
        return "City not found", 404 



    #Reviews senden
    #Erstellt Instanz des Formulars ReviewForm (aus forms.py) mit dem Namen form
    #Diese wird in der html-Seite referenziert
    form = ReviewForm()

    #Prüft ob das Formular valide abgeschickt worden ist, d.h. ob alle Regeln in forms.py eingehalten worden sind
    #Wenn ja werden diese SQL-Statements durchgeführt
    if form.validate_on_submit(): 
        #Alle Werte, die Nutzer in Formular eingegeben hat werden in die Tabelle "review" eingefüht
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
            city['name'], #Übernimmt Name der Stadt aus der DB
            form.overall_rating.data, #Liest den Inhalt aus dem jeweiligen Feld und ersetzt damit Platzhalter
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
        #Statements in DB commited
        db_con.commit() 
        #Nach dem Speichern wird die City-Unterseite neu geladen
        #Somit wird die Seite jetzt sofort mit der neuen Review angezeigt
        return redirect(url_for('city_view', city_name=city_name)) 

    #Bewertungen anzeigen
    #Keine If-Bedingung, wird immer gemacht bei Öffnung der Seite
    #SQL-Statement durchgeführt
    #Speichert Liste der zurückgegebenen Bewertungen als reviews
    reviews = db_con.execute( 
        #Alle Reviews der Stadt angezeigt und nach Datum sortiert (absteigend)
        'SELECT * FROM review WHERE city_name = ? ORDER BY created_at DESC',
        (city['name'],) #Def für ?-Platzhalter
        #Holt alle Ergebnisse der SQL-Abfrage auf einmal, d.h. alle Bewertungen
    ).fetchall() 

    #Rendert das HTML-Template city.html mit city (gegebene Stadt, Überschrift bei City-Unterseite) 
    #Und dem Review-Forular form
    #Und alle reviews aus der DB
    return render_template('city.html', city=city, form=form, reviews=reviews)


#Route zum Schreiben einer Review 
@app.route('/review')
@login_required
def review():
    return render_template('review.html')


@app.route('/user')
def user():
    return render_template('user.html')


#Route zum Registrieren eines neuen Nutzers 
@app.route('/register', methods=['GET', 'POST'])
def register():

    db_con = get_db_con() #baut Verbindung zur DB auf
    form = RegisterForm()

    #wenn user schon eingeloggt wird auf Userprofil verwiesen, damit sich der User nicht zweimal einloggen kann 
    if current_user.is_authenticated:
        return redirect(url_for('profile'))


    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        passwordRepeat = form.passwordRepeat.data

        #password und passwordRepeat müssen gleich sein
        if password != passwordRepeat:
            flash('Passwords do not match')
            return redirect(url_for('register'))
        
        #prüft ob username bereits vergeben ist 
        checkuser = db_con.execute( 
        'SELECT * FROM user WHERE username = ?', (username,)).fetchone()
        
        if checkuser:
            flash('username already taken :( Please choose a diferrent one')
            print('username already taken :( Please choose a diferrent one') #erstmal zum testen, später entfernen 
            return redirect(url_for('register'))
        
        
        db_con.execute('INSERT INTO user(username, password) VALUES (?, ?)',(username, password))
        db_con.commit()
        flash('registration successfull :) You can now log in!')
        print('registration successfull :) You can now log in!') #erstmal zum testen, später entfernen 
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


#LOGIN
#user class(für flask_login)
class User(UserMixin): # von UserMixin werden Methoden vererbt
    def __init__(self, id, username, password):
        self.id = str(id)
        self.username = username
        self.password = password


    #getter-Methode um user aus Datenbank zu holen 
    @staticmethod
    def get(user_id):
        db_con = get_db_con()
        #sucht nach id in Datenbank 
        getuser = db_con.execute( 
            'SELECT * FROM user WHERE id = ?', (user_id,)).fetchone()

        if getuser:
            return User(id=getuser['id'],username= getuser['username'], password=getuser['password'] )
    
        return None


#user_loader: reload user-Objekt
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) 


#Route für den Login-Bereich 
@app.route('/login', methods=['GET', 'POST'])
def login():

    db_con = get_db_con() #baut Verbindung zur DB auf
    form = LoginForm()

    #wenn user schon eingeloggt, wird auf Userprofil verwiesen
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == 'POST' and form.validate_on_submit():

        username = form.loginUsername.data
        password = form.loginPassword.data

        #sucht nach username in der Datenbank
        existuser = db_con.execute( 
        'SELECT * FROM user WHERE username = ?', (username,)).fetchone()

       
        if existuser and existuser['password'] == password:
            
            user = User(id=existuser['id'], username= existuser['username'], password=existuser['password'])
            login_user(user) #user wird eingeloggt
            flask.flash('Logged in successfully.')
            print('Login hat funktioniert') #erstmal zum testen 
            return redirect(url_for('profile'))
        else: 
            flask.flash('wrong username or password')
            print('Login fehlgeschlagen')

    return render_template('login.html', form=form)


#loggt den user wieder aus   
@app.route('/logout')
@login_required
def logout():

    logout_user() #aus FLask_Login
    print('logout hat funtioniert')

    return redirect(url_for('login'))





#Benutzt um Daten manuell in DB einzufügen
#Wenn diese Route aufgerufen wird, insert_sample()-Funktion aus db.py ausgeführt
@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()

    return 'Data added to Database.'

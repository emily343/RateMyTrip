
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm # Flask-WTF [4]
from wtforms import SelectMultipleField, StringField, SubmitField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, EqualTo, Optional

#Datei um Formen zu definieren


#In Search
#Definiert neues Formular namens SearchCityForm, das von FlaskForm erbt 
#FlaskForms ist Basis-Klasse in Flask
class SearchCityForm(FlaskForm):  
    #cityField ist Eingabefeld für String-Variable
    #Pflichtfeld
    cityField = StringField(validators=[InputRequired()])  
    
    #Button, mit dem das Formular abgeschickt wird
    submit = SubmitField('Search') 


#In City/Cityname
#Definiert neues Formular namens ReviewForm, das von FlaskForm erbt 
#FlaskForms ist Basis-Klasse in Flask
class ReviewForm(FlaskForm): 
    #Overall-Rating
    #Pflichtfeld für Interger-Variable, zwischen 1-5 Punkten
    overall_rating = IntegerField('Rating (1–5)', validators=[InputRequired(), NumberRange(min=1, max=5)]) 
    
    #Detail-Ratings
    #IntegerFields mit erlaubten Werten von 1-5
    uni_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)]) 
    freetime_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    nightime_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    campus_life_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    transportation_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    cost_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    living_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    workopportunities_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    safety_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    food_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])
    comunication_rating = IntegerField('Rating (1–5)', validators=[NumberRange(min=1, max=5)])

    #Eingabefeld für Review-Text mit max. 700 Zeichen
    comment = TextAreaField('Comment', validators=[Length(max=700)]) 

    #Button für Abschicken der Review
    submit = SubmitField('Submit Review') 


#In Register
class RegisterForm(FlaskForm): #Basisklasse
    username = StringField(validators=[InputRequired(), Length(min=3, max=20)])  
    password = PasswordField(validators=[InputRequired(), Length(min=5, max=20)])  
    passwordRepeat = PasswordField(validators=[InputRequired(), EqualTo('password')])  
    register = SubmitField('register') #Button für Bestätigung

#In Login
class LoginForm(FlaskForm): #Basisklasse
    loginUsername = StringField(validators=[InputRequired(), Length(min=3, max=20)])  
    loginPassword = PasswordField(validators=[InputRequired(), Length(min=5, max=20)])  
    login = SubmitField('Login') #Button für Bestätigung

#In Bulletin Board
class BulletinForm(FlaskForm):
    message = TextAreaField(validators=[InputRequired(), Length(min=10, max=700)])
    submitMessage = SubmitField('submit') #Button für Bestätigung


#in Profile
class ProfileForm(FlaskForm):
    name = StringField(validators=[Optional(),Length(min=2, max=30)])
    age = IntegerField(validators=[Optional(),NumberRange(min=1, max=120)])
    interests = StringField(validators=[Optional(),Length(min=2, max=60)])
    about = TextAreaField(validators=[Optional(),Length(min=2, max=700)])
    submitProfile = SubmitField('Save Changes')
  
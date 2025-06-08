from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange

#Datei um benutze Formen festzulegen


#in Search
class SearchCityForm(FlaskForm):  #FlaskForms ist Basis-Klasse in Flask
    cityField = StringField(validators=[InputRequired()])  #cityField ist Eingabefeld für String-Variable, es muss Text eingeben werden
    submit = SubmitField('Search') #Button für Bestätigung


#in City/Cityname
class ReviewForm(FlaskForm): #Basis-Klasse 
    overall_rating = IntegerField('Rating (1–5)', validators=[InputRequired(), NumberRange(min=1, max=5)]) #Eingabefeld für Interger-Variable, zwischen 1-5 Stars, jede Bewertung braucht dieses Rating
    #optionale, Detail-Ratings
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

    comment = TextAreaField('Comment', validators=[Length(max=700)]) #Eingabefeld für Reviw-Text, ist nicht zwingend notwendig, max. 700 Zeichen
    submit = SubmitField('Submit Review') #Button für Abschicken der Reviw

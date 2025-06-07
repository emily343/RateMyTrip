from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

#in Search
class SearchCityForm(FlaskForm):  #FlaskForms ist Basis-Klasse n Flask
    cityField = StringField(validators=[InputRequired()])  #cityField ist Eingabefeld für String-Variable, es muss Text eingeben werden
    submit = SubmitField('Search') #Button für Bestätigung
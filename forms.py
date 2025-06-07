from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

#in Search
class SearchCityForm(FlaskForm):  #FlaskForms ist Basis-Klasse n Flask
    description = StringField(validators=[InputRequired()])  #description ist Eingabefeld für String-Variable, es muss Text eingeben werden
    submit = SubmitField('Search') #Button für Bestätigung
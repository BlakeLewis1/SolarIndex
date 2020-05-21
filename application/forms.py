from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class PlanetForm(FlaskForm):
    planet_name = StringField('Planet Name',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    astronomical_type = StringField('Astronomical Type',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    describe = StringField('Describe the Planet',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    ssystem = IntegerField("solar system",
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField('Add Planet')

class SolarForm(FlaskForm):
    solar_name = StringField('Solar Name',
    validators = [
        DataRequired(),
        Length(min=2, max=50)

        ]
    )
    submit = SubmitField('Add SolarSystem')

#class UpdatePlanetForm(FlaskForm):
   # planet_name = StringField('Planet Name',
    #validators = [
       # DataRequired(),
        #Length(min=2, max=50)
        #]
    #)
    #astronomical_type = StringField('astronomical Type',
       # validators = [
           # DataRequired(),
            #Length(min=2, max=50)
        #]
    #)
    #describe = StringField('Describe the Planet',
       # validators = [
           # DataRequired(),
           # Length(min=2, max=1000)
        #]
    #)
    #submit = SubmitField('Add Planet')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PlanetForm(FlaskForm):
    planet_name = StringField('Planet Name',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
<<<<<<< HEAD
    astronomical_type = StringField('Astronomical Type',
=======
    astronomical_type = StringField('astronomical Type',
>>>>>>> b9f344988710d63e3275185c5545f7ca51cef5ec
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
    submit = SubmitField('Add Planet')

<<<<<<< HEAD
=======

>>>>>>> b9f344988710d63e3275185c5545f7ca51cef5ec
class SolarForm(FlaskForm):
    solar_name = StringField('Solar Name',
    validators = [
        DataRequired(),
        Length(min=2, max=50)

        ]
    )
    submit = SubmitField('Add SolarSystem')

class UpdatePlanetForm(FlaskForm):
    planet_name = StringField('Planet Name',
    validators = [
        DataRequired(),
        Length(min=2, max=50)
        ]
    )
    astronomical_type = StringField('astronomical Type',
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
    submit = SubmitField('Add Planet')
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
    planet_type = StringField('Planet Type',
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


class SolarForm(FlaskForm):
    solar_name = StringField('Solar Name',
      validators = [
          DataRequired(),
          Length(min=2, max=50)

        ]
    )
    submit = SubmitField('Add SolarSystem')

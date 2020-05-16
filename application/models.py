from application import db

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(30), nullable=False)
    planet_type = db.Column(db.String(30), nullable=False)
    Descibe = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Planet: ', self.planet_name, ' ', self.planet_type, '\r\n',
            'Description ', self.describe
            ])

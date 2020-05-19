from application import db

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    planet_name = db.Column(db.String(30), nullable=False)
=======
    planet_name = db.Column(db.String(50), nullable=False, unique=True)
>>>>>>> b9f344988710d63e3275185c5545f7ca51cef5ec
    astronomical_type = db.Column(db.String(30), nullable=False)
    describe = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Planet: ', self.planet_name, ' ', self.astronomical_type, '\r\n',
            'Description ', self.describe
            ]) 
    
class Solar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solar_name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return ''.join([
            'Solar: ', self.solar_name, '\r\n'
            ])

class Solar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solar_name = db.Column(db.String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return ''.join([
            'Solar: ', self.solar_name, '\r\n'
            ])

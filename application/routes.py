from flask import render_template, redirect, url_for
from application import app, db
from application.models import Planets
from application.forms import PlanetForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

 
@app.route('/planet', methods=['GET', 'POST'])
def post():
    form = PlanetForm()
    if form.validate_on_submit():
        planetData = Planets(
            planet_name = form.planet_name.data,
            planet_type = form.planet_type.data,
            describe = form.describe.data
        )

        db.session.add(planetData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('planet.html', title='add Planet', form=form)


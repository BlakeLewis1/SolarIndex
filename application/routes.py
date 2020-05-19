from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Planets, Solar
from application.forms import PlanetForm, SolarForm

@app.route('/')
@app.route('/home')

def home():
    planets = Planets.query.all()
    return render_template('home.html', title='Home', planets = planets)

 
@app.route('/planet', methods=['GET', 'POST'])
def planet():
    form = PlanetForm()
    
    if form.validate_on_submit():
        planetData = Planets(
            planet_name = form.planet_name.data,
            astronomical_type = form.astronomical_type.data,
            describe = form.describe.data
        )

        db.session.add(planetData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)
        


    return render_template('planet.html', title='Create the Planet', form=form)

@app.route('/solar', methods=['GET', 'POST'])
def solar():
    form = SolarForm()
    if form.validate_on_submit():
        solarData = Solar(
                solar_name = form.solar_name.data
                )
        db.session.add(solarData)
        db.session.commit()

        return redirect(url_for('planet'))
    else:
        print(form.errors)
    return render_template('solar.html', title='start your solar system', form=form)

@app.route('/<name>/update', methods=['GET', 'POST'])
def updateplanet(name):
    planets = Planets.query.filter_by(planet_name=name).first()
    form = PlanetForm()
    if form.validate_on_submit():
        planets.planet_name=form.planet_name.data
        planets.astronomical_type=form.astronomical_type.data
        planets.describe=form.describe.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.planet_name.data = planets.planet_name
        form.astronomical_type.data=planets.astronomical_type
        form.describe.data=planets.describe
    return render_template('planet.html', title='update planet', form=form)


       
    



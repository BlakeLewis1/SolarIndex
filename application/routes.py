from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Planets, Solar
from application.forms import PlanetForm, SolarForm

@app.route('/')
@app.route('/home')

def home():
    solars = Solar.query.all()
    planets = Planets.query.all()
    return render_template('home.html', title='Home', planets = planets, solar=solars)

 
@app.route('/planet', methods=['GET', 'POST'])
def planet():
    form = PlanetForm()
    solar = Solar.query.all()
    if form.validate_on_submit():
        planetData = Planets(
            planet_name = form.planet_name.data,
            astronomical_type = form.astronomical_type.data,
            describe = form.describe.data,
            ssystem_id = form.ssystem.data
        )

        db.session.add(planetData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)
        


    return render_template('planet.html', title='Create the Planet', form=form, solars=solar)

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
    solar = Solar.query.all()

    planets = Planets.query.filter_by(planet_name=name).first()
    form = PlanetForm()
    if form.validate_on_submit():
        planets.planet_name=form.planet_name.data
        planets.astronomical_type=form.astronomical_type.data
        planets.describe=form.describe.data
        planets.ssystem_id=form.ssystem.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.planet_name.data = planets.planet_name
        form.astronomical_type.data=planets.astronomical_type
        form.describe.data=planets.describe
        form.ssystem.data=planets.ssystem_id
    return render_template('planet.html', title='update planet', form=form, solars=solar)

@app.route('/<name>/delete', methods=['GET', 'POST'])
def deleteplanet(name):
    planet = Planets.query.filter_by(planet_name=name)
    for p in planet:
        db.session.delete(p)

        db.session.commit()
    return redirect(url_for('home'))

@app.route('/home/<name>/delete', methods=['GET', 'POST'])
def deletesolar(name):
    solar = Solar.query.filter_by(id=name).first()
    planets = Planets.query.filter_by(ssystem_id=name).all()
    for planet in planets:
        db.session.delete(planet) 
    db.session.delete(solar)
        

    db.session.commit()
    return redirect(url_for('home'))


       
    



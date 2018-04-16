import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Country, Fighter

app = Flask(__name__)

engine = create_engine('sqlite:///tournament.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# @app.route('/')
# def hello():
#     return render_template('home.html')
    
@app.route('/')
def showFighters():
    #bingo
    person = session.query(Fighter)
    place = session.query(Country)
    # everything gets loaded into the id. fighter passes it in there
    return render_template('home.html', person = person, place = place)
 
    
@app.route('/fighter/<int:f_id>/')
def showTheFighter(f_id):
    #bingo
    person = session.query(Fighter).get(f_id)
    # everything gets loaded into the id. fighter passes it in there
    return render_template('fighter.html', fighter = person)

# @app.route('/')
@app.route('/countries/<int:c_id>/')
def showCountryFighters(c_id):
    #bingo
    country = session.query(Country).get(c_id)
    person = session.query(Fighter).filter_by(country_id = c_id)

    # everything gets loaded into the id. fighter passes it in there
    return render_template('country.html', person = person, country = country)

@app.route('/fighters/new')
def newFighters():
    #newPerson = session.query(Fighter).filter_by(id=fighter_id).one()
    # Create new button
    # NewHtml and form
    # Create flash
    return  render_template('new.html')

@app.route('/edit/')
def editFighters():
    person = session.query(Fighter)
    place = session.query(Country)
    # everything gets loaded into the id. fighter passes it in there
    return render_template('edit.html', person = person, place = place)
    
@app.route('/countries/edit/<int:c_id>/', methods = ['GET','POST'])
def editCountry(c_id):
    country = session.query(Country).get(c_id)
    if request.method == 'GET':
        return render_template('countryform.html', country = country)
    elif request.method == 'POST':
        name = request.form['name']
        country.name = name 
        
        session.commit()
        print "It posted!"
        url = '/countries/'+ str(c_id) + '/'
        return redirect(url)
        

@app.route('/fighter/edit/<int:f_id>/', methods=['GET','POST'])
def editFighter(f_id):
    person = session.query(Fighter).get(f_id)
    if request.method == 'GET':
        return render_template('fighterform.html', fighter = person)
    elif request.method == 'POST':
        name = request.form['name']
        person.name = name 
        
        style = request.form['style']
        person.style = style 
        
        description = request.form['description']
        person.description = description
        
        session.commit()
        print "It posted!"
        url = '/fighter/'+ str(f_id) + '/'
        return redirect(url)
 


@app.route('/fighter/delete/', methods=['GET'])
def deleteFighters():
    # person = session.query(Fighter).get(f_id)
    
    # session.delete(person)
    # session.commit()
    
    # print "delete!"
    # url = '/fighter/'+ str(f_id) + '/'
    
    return 'delete'

@app.route('/login/')
def loginFighters():
    return render_template('login.html')


if __name__ == '__main__':
    app.secret_key = "kennedy's secret"
    # app.run('localhost', 8080, debug=True)
    app.run(host=os.getenv('IP', '0.0.0.0'), debug=True, port=int(os.getenv('PORT', 8080)))

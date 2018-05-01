import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Gym, Fighter

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
    gym = session.query(Gym)
    # everything gets loaded into the id. fighter passes it in there
    return "Show Fighter"
    
@app.route('/edit')
def editFighter():
    return "Edit Fighter"





if __name__ == '__main__':
    app.secret_key = "kennedy's secret"
    # app.run('localhost', 8080, debug=True)
    app.run(host=os.getenv('IP', '0.0.0.0'), debug=True, port=int(os.getenv('PORT', 8080)))

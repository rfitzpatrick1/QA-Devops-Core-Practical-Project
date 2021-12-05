from flask import Flask, redirect, render_template
from creature_name.application.routes import name
from flask_sqlalchemy import SQLAlchemy
from application.models import Creatures
import requests
from application import app, db

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///char.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/',methods=['GET', 'POST'])
def index():
    creature_type = requests.get('http://creture_type:5000/type')
    continent = requests.get('http://continent:5000/continent')
    creature_name = requests.post('http://creature_name:5000/creature_name',data=name.text)
    db.session.add()
    db.session.commit()
    return render_template('index.html',creature_type=type.text,continent=continent.text,creature_name=name.text)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

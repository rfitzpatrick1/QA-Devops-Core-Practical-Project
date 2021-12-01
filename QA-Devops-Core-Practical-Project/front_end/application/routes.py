from flask import Flask, render_template
import requests

from application.models import Creatures

@app.route('/')
def homepage():
    render_template('index.html')

@app.route('/',methods=['GET', 'POST'])
def index():
    creture_type = requests.get('http://creture_type:5000/type')
    continent = requests.get('http://continent:5000/continent')
    creature_name = requests.post('http://creature_name:5000/creature_name',data=creature_name.text)
    return render_template('index.html',creature_type=creature_type.text,continent=continent.text,creature_name=creature_name.text)



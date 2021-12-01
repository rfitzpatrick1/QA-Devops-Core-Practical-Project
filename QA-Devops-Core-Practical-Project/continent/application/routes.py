from flask import Flask, Response, request
import random
app = Flask(__name__)

@app.route('/continent',methods=['GET'])
def continent():
    continent_list = ['Europe','Africa','Asia','North America','South America','Australasia']
    continent = random.choice(continent_list)
    return Response(continent,mimetype='text/plain')

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
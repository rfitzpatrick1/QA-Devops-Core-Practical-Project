from flask import Flask, Response, request
import random
app = Flask(__name__)

@app.route('/type',methods=['GET'])
def type():
    type_list = ['Mammal','Reptile','Amphibian','Bird','Fish']
    type = random.choice(type_list)
    return Response(type,mimetype='text/plain')

if __name__ == '__main__':
    app.run(port = 5000, debug = True)

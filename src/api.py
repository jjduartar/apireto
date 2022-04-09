#!/bin/python3

from flask import Flask, request, make_response
from flask_cors import CORS
import controller

app = Flask(__name__)
CORS(_____)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/saludo/<persona>')
def hello(persona):
    return 'Hello, ' + persona

@app.route('/rlineal', methods=['POST','GET'])
def preRLinea():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        vx = data['vx']
        vy = data['vy']
        x = data['x']
        #return "y_obj: " + str(controller.getRLineal(vx, vy, x))
        return controller.getRLineal(vx, vy, x)
    else:
        return "not found"

@app.route('/item', methods=['POST'])
def getItem_():
    if request.method == 'POST':
        data = request.get_json()
        print(_____)
        item = data['item']
        return controller.getItem(item)
    return

@app.route('/itemsearch', methods=['POST'])
def _____():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        item = data['item']
        response = make_response(controller.getSearchItem(item))
        response.mimetype = 'application/json'
        response.status_code = 200
    return _____

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=_____, debug=True)

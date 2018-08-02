from flask import Flask, render_template, request, jsonify
import os
from os import environ
import json

from flask_cors import CORS


data=""




app = Flask(__name__)
CORS(app)



port = int(os.getenv('PORT', 8000))

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/menu')
def recipe():
    return render_template('recipe.html')


@app.route('/get-orders')
def orderget():
    global data
    res=data
    if res!="":
        data=""
    return json.dumps({"value": res})

@app.route('/set-orders')
def orderset():
    global data
    food=request.args.get('food')
    quantity=request.args.get('quantity')
    import random
    x=random.randint(0, 3)
    if x==0:
        value= "You ordered "+quantity+" "+food+". Got it!"
    elif x==1:
        value = "So I have " + quantity + " " + food + "!"
    else:
        value = "Great! Let me get you " + quantity + " " + food + "."
    data="Table 5: "+quantity+" "+food

    return json.dumps({"value":value})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

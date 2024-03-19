# -*- coding: utf-8 -*-
import random

from flask import Flask, abort, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#les absences, c'est pour un dictionnaire qui pour un entier donne le nom et le nombre d'absences
# structure absences : { 1:{'nom':'toto', 'abs':3}, 2:{'nom':'bob', 'abs':3} }
nb_random = random.randint(0, 100000)
toGuess = random.randint(0, 100)


@app.route("/")
def index():
    return render_template('helloWorld.html', nb = nb_random)

@app.route("/appli", methods=['GET'])
def appli():
    return render_template('app.html')

@app.route("/form", methods=['GET'])
def form():
    return render_template('form.html')

@app.route("/form/result", methods=['POST'])
def result():
    data = request.form["value"]
    return render_template('resultForm.html', value = data)

@app.route("/game", methods=['GET'])
def game():
    return render_template('moreLess.html', clue="", target=toGuess)

@app.route("/game/started", methods=['POST'])
def gameStarted():
    data = int(request.form["nb"])
    clue = ""
    if (data > toGuess):
        clue = "C'est plus petit"
    elif (data < toGuess):
        clue = "C'est plus grand"
    else:
        return render_template('win.html', toGuess=toGuess)
    return render_template('moreLess.html', clue=clue, target=toGuess)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

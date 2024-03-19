# -*- coding: utf-8 -*-
import random

from flask import Flask, abort, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

gamesList = []

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form", methods=['GET'])
def form():
    return render_template('form.html')

@app.route("/form/list", methods=['POST'])
def send():
    title = request.form["title"]
    price = request.form["price"]
    desc = request.form["desc"]
    gamesList.append({"title":title, "price":price, "desc":desc})
    return render_template('list.html', gamesList = gamesList)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template
import requests
app = Flask(__name__)


@app.route('/weatherstation')
def läggIn():
    värme = randint(99,700)
    hej= randint(12,99)
    bla = randint(1,10)
    return jsonify(värme, hej, bla)


if __name__ == '__main__':
    app.run()
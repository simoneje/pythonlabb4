import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template
import requests
import time
app = Flask(__name__)


@app.route('/weatherstation')
def läggIn():
    regn = randint(99,700)
    snow = randint(12,99)
    heat = randint(1,10)
    while True:
        time.sleep(10)
        return jsonify(regn, snow, heat)


if __name__ == '__main__':
    app.run()
import sqlite3
from flask import Flask, escape, request, jsonify, render_template
import requests
import numpy as np
app = Flask(__name__)

@app.route('/')
def databaspost():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT regn FROM väder")
    values = c.fetchall()
    while values is not None:
        regn = values
        # snow = values'
        # heat = values
    return render_template('databas.html', rain=regn)

if __name__ == '__main__':
    app.run()

# , snow=snow, heat=heat
    
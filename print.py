import sqlite3
from flask import Flask, escape, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def databaspost():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT regn FROM väder")
    r = c.fetchall()
    rain = ''
    for x in r:
        rain = rain + x[0] + " "

    c.execute("SELECT snö FROM väder")
    s = c.fetchall()
    snow = ''
    for y in s:
        snow = snow + y[0] + ", "

    c.execute("SELECT värme FROM väder")
    h = c.fetchall()
    heat = ''
    for z in h:
        heat = heat + z[0] + ", "
       
    return render_template('databas.html', rain=rain, snow=snow, heat=heat)

if __name__ == '__main__':
    app.run()

    
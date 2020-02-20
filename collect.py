
import sqlite3
from flask import Flask, escape, request, jsonify, render_template
import requests

def hejhej():
    svar = requests.get('http://127.0.0.1:5000/weatherstation')
    hej = svar.json()

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

# c.execute("""CREATE TABLE väder(
#     regn text,
#     snö text,
#     värme text
# )""")

    c.execute("INSERT INTO väder (regn, snö, värme) VALUES (?,?,?)", hej)
    c.execute("SELECT * FROM väder")

    conn.commit()
    conn.close()
hejhej()


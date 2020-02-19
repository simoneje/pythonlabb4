import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template

conn = sqlite3.connect(data.db)
c = conn.cursor()



c.execute("""CREATE TABLE väder(
    regn text,
    snö text,
    värme text
)""")

conn.commit()
conn.close()
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

def hej(firstname):
    return firstname
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
if request.method == 'POST':
    firstname = request.form.get('fname')
    lastname = request.form.get('ename')
    address = request.form.get('address')
    postnmr = request.form.get('zipcode')
    ort = request.form.get('city')
    mobilnmr = request.form.get('cellphone')
    email = request.form.get('email')

    hej(firstname)


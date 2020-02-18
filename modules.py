from flask import Flask, render_template, jsonify
from flask import request
app = Flask(__name__)

def hej(firstname):
    return firstname
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # print(request.fot set')rm.values)
    # print(request.form.get('payment','No)
    killer = [
    request.form.get('fname'),
    request.form.get('ename'),
    request.form.get('address'),
    request.form.get('zipcode'),
    request.form.get('city'),
    request.form.get('cellphone'),
    request.form.get('email'),
    request.form.get('paymenttype'),
    request.form.get('offers'),
    request.form.get('format'),
    request.form.get('comment')]

    f_name = killer[0]
    e_name = killer[1]
    address = killer[2]
    postnmr = killer[3]
    stad = killer[4]
    telnmr = killer[5]
    email = killer[6]
    betala = killer[7]
    offer = killer[8]
    form = killer[9]
    kommentar = killer[10]
    return render_template('test.html', fname = f_name, ename =e_name, address=address, postnmr =postnmr, stad=stad, tele=telnmr, email=email, pay=betala, offer=offer, for_mat=form, kommentar=kommentar)

# @app.route('/register', methods=['POST'])
# def register():
#     print(request.form.values)
#     print(request.form.get('payment','Not set'))
#     killer = jsonify({
#     'firstname' : request.form.get('fname'),
#     'lastname' : request.form.get('ename'),
#     'address' : request.form.get('address'),
#     'postnmr' : request.form.get('zipcode'),
#     'ort' : request.form.get('city'),
#     'mobilnmr' : request.form.get('cellphone'),
#     'email' : request.form.get('email')})

#     data = killer['firstname']
#     return 
    





@app.route('/test')
def test():
    print(jsonify)
    return render_template('test.html')
if __name__ == '__main__':
    app.run()
    
    
# if request.method == 'POST':
#     firstname = request.form.get('fname')
#     lastname = request.form.get('ename')
#     address = request.form.get('address')
#     postnmr = request.form.get('zipcode')
#     ort = request.form.get('city')
#     mobilnmr = request.form.get('cellphone')
#     email = request.form.get('email')

#     hej(firstname)
#     print(hej)


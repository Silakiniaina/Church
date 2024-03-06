import decimal
import random
from flask import Flask, redirect, render_template,request, url_for,session
from models.croyant import Croyant
from models.offrande import Offrande
from models.eglise import Eglise
from models.pret import Pret

app = Flask(__name__)
app.secret_key = 'DashDashGo2K23!!'

@app.route('/church')
def show_login():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def authetification():
    email = request.form['mail']
    pwd = request.form['pwd']
    actif = Croyant.authentificate(email,pwd)
    if(actif != None):
        session['id_actif'] = actif.id
        return render_template('home.html')
    else: 
        return render_template('login.html')

@app.route('/show_offrande')
def show_offrande():
    ls = Eglise.get_all_eglise()
    length = len(ls)
    return render_template('insertOffrande.html',list_eglise=ls,length_eglise=length)

@app.route('/insert_offrande',methods=['POST'])
def insert_offrande():
    montant = float(request.form['montant'])
    num_dim = int(request.form['num_dim'])
    egl = int(request.form['eglise'])
    nombre = random.randint(0,500)
    o = Offrande(4,montant,num_dim,2024,nombre,egl)
    o.insert()
    return redirect(url_for('show_offrande'))

@app.route('/show_demande')
def show_demande():
    ls = Eglise.get_all_eglise()
    length = len(ls)
    return render_template('insert_demande.html',list_eglise=ls,length_eglise=length)

@app.route('/insert_demande',methods=['POST'])
def insert_demande():
    montant = float(request.form['montant'])
    num_dim = int(request.form['num_dim'])
    egl = int(request.form['eglise'])
    id_croyant = int(session.get('id_actif'))
    d = Pret(2,num_dim,2024,montant,egl,id_croyant)
    res = d.get_estimation()
    d.insert()
    return render_template('resultat.html',resultat=res)
    

if __name__ == '__main__':
    app.run(debug=True)




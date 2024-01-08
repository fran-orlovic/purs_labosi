from flask import Flask, request, redirect, url_for, render_template, session, make_response
from flask import g
import MySQLdb

app = Flask("Prva flask aplikacija")

app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

@app.before_request
def before_request_func():
    g.connection = MySQLdb.connect(host = "localhost", user = "app",
                                   passwd = "1234", db = "lvj6")
    g.cursor = g.connection.cursor()
    if request.path.startswith('/login') or request.path.startswith('/static') or request.path.startswith('/temperatura'):
        return
    if session.get('username') is None:
        return redirect(url_for('login_page'))

@app.after_request
def after_request_func(response):
    g.connection.commit()
    g.connection.close()
    return response

@app.get('/')
def home_page():
    id = request.args.get('id')
    if id == None or id == '1':
        g.cursor.execute(render_template('getKorisnikTemp.sql', id_korisnika = session.get('id')))
        list_temp = g.cursor.fetchall()
        response = render_template('index5.html', naslov = 'Početna stranica',
                                   username = session.get('username').capitalize(), tip='Temperatura',
                                   podatci = list_temp, tip_podatka = id)
        return response, 200
    elif id == '2':
        g.cursor.execute(render_template('getKorisnikVlage.sql', id_korisnika = session.get('id')))
        list_vlage = g.cursor.fetchall()
        response = render_template('index5.html', naslov='Početna stranica',
                                   username=session.get('username').capitalize(), tip='Vlaga',
                                   podatci = list_vlage, tip_podatka = id)
        return response, 200

@app.get('/login')
def login_page():
    response = render_template('login4.html', title='Login stranica'), 200
    return response

@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login_page'))

@app.post('/login')
def login():
    g.cursor.execute(render_template('getKorisnik.sql', user=request.form.get('username'), passwd=request.form.get('password')))
    korisnik = g.cursor.fetchall()
    if korisnik != ():
        session['username'] = korisnik[0][3]
        session['id'] = korisnik[0][0]
        return redirect(url_for('home_page'))
    else:
        return render_template('login4.html', title='Login stranica',
                               poruka="Uneseni su pogrešni podatci")

@app.post('/temperatura')
def put_temperatura():
    global temperatura
    response = make_response()
    if request.json.get('temperatura') is not None:
        query = render_template('writeTemperature.sql',
                                value=request.json.get('temperatura'))
        g.cursor.execute(query)
        response.data = 'Uspješno ste postavili temperaturu'
        response.status_code = 201
    else:
        response.data = 'Niste napisali ispravan ključ'
        response.status_code = 404
    return response

@app.route('/temperatura/<int:id_stupca>', methods = ['POST'])
def delete(id_stupca):
    id_podatka = request.args.get('id_podatka')

    if id_podatka == '' or id_podatka == '1' and id_stupca is not None:
        query = render_template('deleteTemp.sql', id_temp = id_stupca)
        g.cursor.execute(query)
        if id_podatka == '1':
            return redirect(url_for('home_page', id = id_podatka))
        else:
            return redirect(url_for('home_page'))
    
    elif id_podatka == '2' and id_stupca is not None:
        query = render_template('deleteVlaga.sql', id_vlage = id_stupca)
        g.cursor.execute(query)
        return redirect(url_for('home_page', id = id_podatka))

    else:
        return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
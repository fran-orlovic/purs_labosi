from flask import Flask, request, redirect, url_for, render_template, session

app = Flask("Prva flask aplikacija")
app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

list = [
    {
        'datum': '18.1.2001',
        'vrijednost': 18
    },
    {
        'datum': '11.4.2004',
        'vrijednost': 11
    },
    {
        'datum': '17.6.1998',
        'vrijednost': 17
    },
    {
        'datum': '18.3.1973',
        'vrijednost': 18
    }
]

# Zadatak 2-4
@app.before_request
def before_request_func():
    if request.path.startswith('/static'):
         return
    if request.path == '/login':
        return
    if session.get('username') is None:
        return redirect(url_for('login_page'))

@app.get('/')
def home_page():
    global list
    response = render_template('index5.html', title='Početna stranica', username=session.get("username"), temperature=list)
    return response

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
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'PURS' and password == '1234':
        session['username'] = username
        return redirect(url_for('home_page'))
    else:
        return render_template('login4.html', title='Login stranica', poruka="Uneseni su pogrešni podatci")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

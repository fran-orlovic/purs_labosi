from flask import Flask, request, redirect, url_for, render_template, session

app = Flask("Prva flask aplikacija")
app.secret_key = '_5#y2L"F4Q8z-n-xec]/'


# Zadatak 1
@app.get('/')
def index():
    return render_template('index.html'), 200

@app.get('/login')
def login():
    return render_template('login.html'), 200

# Zadatak 2-4
@app.before_request
def before_request_func():
    if request.path == '/login':
            return
    if session.get('username') is None:
            return redirect(url_for('login_page'))

@app.get('/')
def home_page():
    response = render_template('index.html')
    return response

@app.get('/login')
def login_page():
    response = render_template('login.html')
    return response

@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login_page'))

@app.post('/login')
def log1n():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'PURS' and password == '1234':
        session['username'] = username
        return redirect(url_for('home_page'))
    else:
        return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

from flask import Flask, request, redirect, url_for, render_template, session

app = Flask("Prva flask aplikacija")
app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

list = ['pon', 'uto','sri','cet']

@app.get('/')
def home_page():
    global list
    response = render_template('index5_ispit.html', title='Početna stranica'), 200
    return response

@app.get('/login')
def login_page():
    response = render_template('login5_ispit.html', title='Login stranica', list=list, blabla="blabla"), 200
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
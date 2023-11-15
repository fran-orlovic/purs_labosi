from flask import Flask, request, redirect, url_for, render_template, session

app = Flask("Prva flask aplikacija")

# Zadatak 2
@app.get('/pocetna_stranica')
def index():
    return render_template('index3_ispit.html')

@app.post('/korisnicki_unos')
def korisnicki_unos():
    text = request.form.get('text')
    password = request.form.get('password')
    email = request.form.get('email')

    return f"{text} + {password} + {email}"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
from flask import Flask, request, redirect, url_for

app = Flask("Prva flask aplikacija")

list = []

# Zadatak 1
@app.get('/')
def index():
    return 'Pocetna stranica'

@app.get('/login')
def login():
    return 'Stranica za prijavu'

# Zadatak 2
@app.post('/login')
def params():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is not None and password is not None:
        if username == 'PURS' and password == '1234':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

# Zadatak 3
@app.post('/temperatura')
def temps():
    temperatura = request.json.get('temperatura')

    if temperatura is not None:
        global list
        list.append(temperatura)
        return "Uspješno ste postavili temperaturu", 201
    else:
        return "Niste upisali ispravan ključ", 404

# Zadatak 4
@app.get('/temperatura')
def zadnja_temp():
    global list
    json = {'temperatura': list[-1]}
    return json

# Zadatak 5
@app.delete('/temperatura')
def brisanje():
    temperatura = request.args.get('temperatura')

    if temperatura is not None:
        global list
        if int(temperatura) < (len(list) - 1):
            list.remove[int(temperatura) - 1]
            return "Uspješno ste obrisali temperaturu", 202
        else:
            return "Upisali ste neispravan ključ", 404
    else:
        return "Upisali ste neispravan ključ", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

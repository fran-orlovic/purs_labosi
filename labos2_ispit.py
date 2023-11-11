from flask import Flask, request, redirect, url_for

app = Flask("Prva flask aplikacija")


# Zadatak 1
@app.put('/putanja_put')
def putanja_za_put():
    return "putanja_za_bod", 405

# Zadatak 2
@app.get('/putanja_get')
def putanja_za_get():
    statusni_kod = request.args.get('samo_jako')
    return "hocu_bodove", statusni_kod

# Zadatak 3
@app.get('/jos_malo_pa_gotovo')
def putanja():
    json = {'moji_bodovi': 3}
    return json, 201

# Zadatak 4
@app.post('/hocu_sve_bodove')
def cetvrti():
    json = request.json.get('svi_bodovi')
    return "svi_bodovi", json
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
# from flask import Flask, request, make_response

# app = Flask("Predavanje")

# @app.post('/temperatura')
# def post_temperatura():
#     response = make_response()
#     print(request.data)
#     response.data = 'Uspješno ste postavili temperaturu'
#     response.status_code = 201
#     return response

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=80)

import requests

response = requests.get('http://192.168.86.215')

argumenti5={
    "temperatura" : -18
}
response = requests.post('http://192.168.86.215', json=argumenti5)

response = requests.post('http://192.168.86.215', data="ON")
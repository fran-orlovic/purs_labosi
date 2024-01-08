import requests

argumenti5={
    "temperatura" : -18
}
response = requests.post('http://192.168.86.214/temperatura', json=argumenti5)
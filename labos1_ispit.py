import requests
# Zadatak 1
print("Zadatak 1")
json={
    "ime" : "Fran",
    "prezime" : "Orlovic",
    "ip" : "192.168.86.211"
}

response = requests.post('http://192.168.86.210/', json=json)

if response.status_code == requests.codes.ok:
    print("Statusni kod je OK")

print(response.status_code)

print()
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.text)
print()
##

# Zadatak 2
print("Zadatak 2")
params={
    "id" : 202
}
response = requests.get('http://192.168.86.210/hocu_bod', params=params)
print()
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.text)
print()
##

# Zadatak 3
print("Zadatak 3")
response = requests.post('http://192.168.86.210/svi_bodovi')
print()
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.text)
print()
##
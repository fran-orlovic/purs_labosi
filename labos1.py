import requests


response = requests.get('http://192.168.86.210/')

# Zadatak 2a
print("Zadatak 2a")
if response.status_code == requests.codes.ok:
    print('Statusni kod je OK 2a')

print()

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print()
##

# Zadatak 2b
print("Zadatak 2b")
response = requests.get('http://192.168.86.210/login')

if response.status_code == requests.codes.ok:
    print('Statusni kod je OK 2b')

print()

for k, v in response.headers.items():
    print(f'{k}: {v}')

print(response.text)
print()
##

# Zadatak 3
print("Zadatak 3")
argumenti = {
    "username" : "PURS",
    "password" : "1234"
}

response = requests.post('http://192.168.86.210/login', json=argumenti)

if response.status_code == requests.codes.ok:
    print('Statusni kod je OK 3')
else:
    print('Statusni kod je neispravan!')


print()
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.text)
print()
##

# Zadatak 4
print("Zadatak 4")
response = requests.get('http://192.168.86.210/temperatura')

if response.status_code == requests.codes.ok:
    print('Statusni kod je OK 4')

print()
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.text)
print()
if response.headers.get('Content-Type') == 'application/json':
    print("temp=")
    print(response.json().get('temperatura'))
print()
##

# Zadatak 5
print("Zadatak 5")
argumenti5={
    "temperatura" : -18
}
response = requests.post('http://192.168.86.210/temperatura', json=argumenti5)

if response.status_code == requests.codes.ok:
    print('Statusni kod je OK 5')
else:
    print(response.status_code)

print()
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.text)
print()
##

# Zadatak 6
print("Zadatak 6")
argumenti6={
    "id" : 10
}
response = requests.delete('http://192.168.86.210/temperatura', params=argumenti6)

if response.status_code == requests.codes.ok:
    print('Statusni kod je OK 6')
else:
    print(response.status_code)

print()
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.text)
print()
##

# Zadatak 7
print("Zadatak 7")
response = requests.get('http://ip.jsontest.com/')

if response.status_code == requests.codes.ok:
    print('Statusni kod je OK 7')
else:
    print(response.status_code)

print()
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.text)
print()
print("Ovo je IP:")
print(response.json().get('ip'))
##
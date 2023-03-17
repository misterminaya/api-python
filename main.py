import requests
from getpass import getpass

# Query -> GET
# Cuerpo de petición -> POST
# Encabezado -> para todos los verbos


# SOLICITAR INFORMACIÓN
URL = 'http://httpbin.org/get'
response = requests.get(URL) #GET
print(response)
print(response.status_code)
print(response.text) #string
print(response.json()) #json

payload = response.json()
print(payload.get('origin')) #dict

print(response.url)

print("*******************************************************")

# ENVIAR INFORMACIÓN
URL = 'http://httpbin.org/get'
params = {
    'name' : 'minaya',
    'password' : '123',
    'email' : 'me@joel.com'
}

response = requests.get(URL, params=params)


if response.status_code == 200:
    payload = response.json()
    params = payload['args']
    print(params['name'])
    print(params['password'])
    print(params['email'])

print("*******************************************************")

# POST

URL = 'http://httpbin.org/post'

data = {
    'username': 'minaya',
    'password': 'password123'
}

response = requests.post(URL, data=data)

if response.status_code == 200:
    payload = response.json()
    print(response.text)
    print(response.url)


print("*******************************************************")

headers = {
    'course': 'Curso de Python',
    'version' : '2.0',
    'author' : 'minayape'
}

params = {
    'platform' : 'CodigoFacilito'
}

data = {
    'username': 'joelito',
    'password': 'password567'
}

response = requests.post(URL, headers=headers, params=params, data=data)

if response.status_code == 200:
    print(response.text)


print("*******************************************************")

URL = 'https://randomuser.me/api/'

count = int(input('Ingresa la cantidad de usuarios: '))
response = requests.get(URL, params={'results': count})

if response.status_code == 200:
    payload = response.json()
    results = payload.get('results')

    for user in results:
        name = user.get('name') #dict 

        #print(f"{name['title']} {name['first']} {name['last']}")
        print("{title} {first} {last}".format(**name))


print("*******************************************************")

URL = 'http://httpbin.org/put'
response = requests.put(URL, 
                        params={'name': 'minaya'}, 
                        headers={'version': '2.0'},
                        data={'id':1})

if response.status_code == 200:
    print(response.text)

print("*******************************************************")

URL = 'https://codigofacilito.com/images/cody' # png

response = requests.get(URL, stream=True)

if response.status_code == 200:
    with open('images/cody.png', 'wb') as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)


print("*******************************************************")

URL = 'http://httpbin.org/cookies'

cookies = {
    'sessions': 'abc123',
    'name': 'Cody',
    'email': 'info@gmail.com'
}

response = requests.get(URL, cookies=cookies)

if response.status_code == 200:
    print(response.json())


print("*******************************************************")

URL = 'http://httpbin.org/basic-auth/cody/1234'

password = getpass('Ingresa la contraseña : ')

session = requests.Session()
session.auth = ('cody', password)

response = session.get(URL)

if response.status_code == 200:
    print(response.json())

if response.status_code == 401:
    print('Unsuccesfull authentication')





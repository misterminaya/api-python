import requests
from settings import *


code = 'd6e1356b12a1444f65c8'

URL = 'https://github.com/login/oauth/access_token'

params = {
    'client_id': CLIENT_ID,
    'client_secret': SECRET_ID,
    'code': code
}

headers = {
    'Accept': 'application/json'
}

response = requests.post(URL, params=params, headers=headers)

if response.status_code == 200:
    print(response.json())


# Obtener al usuario autenticado

access_token = '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'

URL = 'https://api.github.com/user'

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization' : f'Bearer {access_token}'
}


# Creamos una aplicacion en GITHUB
# Obtenemos el código del usuarios --> https://github.com/login/oauth/authorize?client_id<ClientId>&scope=user
# Obtener el access token -> https://github.com/login/oauth/access_token


response = requests.get(URL, headers=headers)

if response.status_code == 200:
    username = response.json().get('login')
    print(username)


print("**************************************************************")
print(response.status_code)
print(response.text)





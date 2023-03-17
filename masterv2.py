#Generar aplicación
#Obtener código
#Obtener Access Token
#Obtener al usuario autenticado


import requests
import webbrowser

from settings import *



#obtener codigo
#codigo: d3c9e6454e79bc2a62f8

def get_url_code():
    url = 'https://github.com/login/oauth/authorize'
    params = {
        'client_id' : CLIENT_ID,
        'scope': 'user'

    }

    response = requests.get(url, params=params)
    return response.url

# Obtener Access Token

def get_access_token(code):
    url= 'https://github.com/login/oauth/access_token'
    params = {
        'client_id' : CLIENT_ID,
        'client_secret': SECRET_ID,
        'code': code
    }

    headers = {'Accept': 'application/json'}

    response =  requests.post(url,params=params, headers=headers)
    if response.status_code == 200:
        payload = response.json()
        return payload.get('access_token')


#Obtener al usuario autenticado 

def get_user(access_token):
    url = 'https://api.github.com/user'

    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization' : f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()





if __name__ == '__main__':
    url = get_url_code()
    webbrowser.open(url)
    
    code = input('Ingresa el codigo :  ')
    code = code.strip().replace('\n', '')

    access_token = get_access_token(code)
    print(access_token)

    user = get_user(access_token)
    print(user)
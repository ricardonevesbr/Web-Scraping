import requests
from pprint import pprint

def getEndereco(endereco):
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" +
                     endereco + "&key=SUA_KEY_AQUI")
    return r.json()

#Pretty print - Impressão bonita
pprint(getEndereco("Rua+Sete+Vitoria+ES+"))
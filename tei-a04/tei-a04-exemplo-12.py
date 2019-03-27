import json
import requests

url = 'http://fipeapi.appspot.com/api/1/carros/marcas.json'

data = requests.get(url=url)
print(data.json())

#mostrar as marcas
for marca in data.json():
    print(marca)

#mostrar somente os nomes das marcas
for marca in data.json():
    print(marca['name'])
    


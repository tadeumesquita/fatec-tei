import json
import requests

data = requests.get(url="http://fipeapi.appspot.com/api/1/carros/marcas.json")
for marca in data.json():
    print("Marca:",marca['name'],"- ID:", marca['id'])

idMarca = int(input("Digite o ID da marca: "))
data = requests.get(url="http://fipeapi.appspot.com/api/1/carros/veiculos/"+str(idMarca)+".json")
for veiculo in data.json():
    print("Modelo:",veiculo['name'],"- ID:", veiculo['id'])

idModelo = int(input("Digite o ID da modelo: "))
data = requests.get(url="http://fipeapi.appspot.com/api/1/carros/veiculo/"+str(idMarca)+"/"+str(idModelo)+".json")
for veiculo in data.json():
    print("Ano e Combustivel:",veiculo['name'],"- ID:", veiculo['id'])

idAnoCombustivel = input("Digite o ID da Ano/Combustível: ")
#data = requests.get(url="http://fipeapi.appspot.com/api/1/carros/veiculo/"+str(idMarca)+"/"+str(idModelo)+"/"+str(idAnoCombustivel)+".json")
data = requests.get(url="http://fipeapi.appspot.com/api/1/carros/veiculo/21/4828/2013-1.json")
for veiculo in data.json():
    print(veiculo)

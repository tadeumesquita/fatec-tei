import json

data = {}
data["vermelho"] = {"nome":"Vermelho","rgb":"255,0,0","hex":"#FF0000"}
data["verde"] = {"nome":"Verde","rgb":"0,255,0","hex":"#00FF00"}
data["azul"] = {"nome":"Azul","rgb":"0,0,255","hex":"#0000FF"}

#ecrever formato JSON
f = open("cores.json","w")
json.dump(data,f, sort_keys=True,indent=4)
f.close()

#ler formato JSON
f = open("cores.json","r")
data = json.load(f)
f.close()

print(data)
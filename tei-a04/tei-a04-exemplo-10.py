import json

data = {}
data["sp"] = "São Paulo"
data["rj"] = "Rio de Janeiro"
data["mg"] = "Minas Gerais"

#ecrever formato JSON
f = open("output.json","w",encoding="utf8")
json.dump(data,f, sort_keys=True,ensure_ascii=False)
f.close()

#ler formato JSON
f = open("output.json","r",encoding="utf8")
data = json.load(f)
f.close()

print(data)
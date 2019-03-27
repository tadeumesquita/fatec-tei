import csv
import json

#o programa a seguir le um arquivo csv e cria um json

termos = []
data = {}

#leitura do arquivo csv
fcsv = open("output.csv","r",newline='',encoding='utf8')
reader = csv.reader(fcsv)

for row in reader:
    termos = row[0].split(";")
    data[termos[0]] = {"nome":termos[1],"email":termos[2]}

fcsv.close()

#criacao arquivo json
fjson = open("csv-to-json.json","w",encoding="utf-8")
json.dump(data,fjson,sort_keys=True,indent=4)
fjson.close()
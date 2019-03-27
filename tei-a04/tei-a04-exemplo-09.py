import csv

data = []
data.append((1, "João da Silva", "joao@joao.com"))
data.append((2, "Ana Maria", "ana@ana.com"))

#escrita no arquivo
f=open("output.csv","w",newline='', encoding="utf-8")
writer = csv.writer(f,delimiter=";")

for linha in data:
    writer.writerow(linha)
f.close()

#leitura
f = open("output.csv","r",newline='',encoding="utf-8")
reader = csv.reader(f)
for row in reader:
    print(row)

f.close
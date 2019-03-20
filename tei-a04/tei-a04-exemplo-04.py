f = open("paises.txt","r",encoding="utf-8")

linha = f.readline()
print(linha.strip("\n"))

data = f.read(3)
print(data)

f.seek(0) #volta pro inicio do arquivo
linhas = f.readlines()
print(linhas)

f.close()
paises = []
f = open("paises.txt",'r',encoding="utf-8")

#splitlines cria uma lista com cada linha do arquivo
paises = f.read().splitlines()

print(paises)
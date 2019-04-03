from random import randint

imagem = []

for i in range(10):
    linha = []
    for j in range(10):
        linha.append(randint(0,255))
    imagem.append(linha)

for linha in imagem:
    print(linha)
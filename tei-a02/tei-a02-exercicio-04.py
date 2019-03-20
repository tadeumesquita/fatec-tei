import os
os.system('cls')

nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))

if valor >=0 and valor < 50:
    res = valor
elif valor >=50 and valor < 200:
    res = valor*0.95
elif valor >= 200 and valor < 500:
    res = valor*0.94
elif valor >= 500 and valor < 1000:
    res = valor*0.93
elif valor >= 1000:
    res = valor*0.92
else:
    print("Produto com valor negativo!")

print("Produto: {0}\nValor Original: {1}\nValor com Desconto: {2}".format(nome,round(valor,2),round(res,2)))

ano = int(input("Digite um ano: "))

print(ano//100 if ano%100 == 0 else ano//100+1)
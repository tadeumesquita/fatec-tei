#limpar console
import os
os.system('cls')

#entrada de dados
precoReajustado = float(input("Informe o o valor do produto: "))*1.12

#saida de dados
print("Valor reajustado: %.2f" %precoReajustado)
#limpar console
import os
os.system('cls')

#entrada de dados
peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

imc = peso/altura**2

#saida de dados
print("Peso: {0}\nAltura: {1}\nIMC = {2}".format(peso,altura,imc))
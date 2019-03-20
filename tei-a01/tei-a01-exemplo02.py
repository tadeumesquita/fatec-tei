#limpar console
import os
os.system('cls')

#entrada de dados
nome = input("Qual seu nome? ")

print("Olá,", nome, "seja bem-vindo!")

msg = "Olá, {} seja bem-vindo".format(nome)
print(msg)
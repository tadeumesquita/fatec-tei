#limpar console
import os
os.system('cls')

#entrada de dados
n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
res = "{0} + {1} = {2}".format(n1,n2,(n1+n2))

print(res)
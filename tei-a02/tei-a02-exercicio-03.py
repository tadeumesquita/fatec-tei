numero = int(input("Digite um numero: "))

print("Tabuada do",numero)

for i in range(1,11):
    print("{0} x {1} = {2}".format(numero,i,(numero*i)))
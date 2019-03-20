v1 = float(input("Valor 1: "))
v2 = float(input("Valor 2: "))
op = input("Operação {+,-,*,/}: ")

if op == '+':
    res = v1+v2
elif op == '-':
    res = v1-v2
elif op == '*':
    res = v1*v2
elif op == '/':
    if v2 != 0:
        res = v1/v2
    else:
        res = "Divisão por ZERO!"
else:
    res = "Operação inválida!"

print(res)



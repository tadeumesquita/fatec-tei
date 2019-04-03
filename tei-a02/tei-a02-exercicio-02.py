resistencias = []

for i in range(4):
    resistencias.append(int(input("Digite o valor da resistencia: ")))

print("Resistencias fornecidas:")
for resistencia in resistencias:
    print(resistencia,end=", ")

print("\nA resistencia equivalente e:",sum(resistencias))
print("A maior resistencia e:",max(resistencias))
print("A menor resistencia e:",min(resistencias))
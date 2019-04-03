from random import randint

vetor = []

for i in range(15):
    vetor.append(randint(0,255))

print("Vetor antes da divisao:",vetor)

maiorValor = max(vetor)
print("Maior valor: ",maiorValor)

for i in range(len(vetor)):
    vetor[i] = vetor[i]/maiorValor

print("Vetor depois da divisao:",vetor)

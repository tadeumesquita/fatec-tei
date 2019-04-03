from random import randint

vetor = []

def maiorProduto(vetor):
    maxProduto=-101 #definido o valor máximo como um valor a menos do menor valor possível conforme o randint
    for i in range(len(vetor)-1):
        if vetor[i]*vetor[i+1] > maxProduto:
            maxProduto=vetor[i]*vetor[i+1]
    
    return maxProduto

for i in range(5):
    vetor.append(randint(-10,10))

print(vetor)

print(maiorProduto(vetor))
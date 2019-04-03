def isPar(valor):
    if valor % 2 == 0:
        return True
    else:
        return False

def qtdPares(valores):
    count = 0
    for valor in valores:
        if isPar(valor):
            count+=1
    return count

def qtdImpares(valores):
    return len(valores)-qtdPares(valores)

def main():
    numeros = (1,2,3,4,5,6)

    print(numeros)
    print("Quantidade de pares:", qtdPares(numeros))
    print("Quantidade de impares:", qtdImpares(numeros))
    print("Maior valor:", max(numeros))
    print("Menor valor:", min(numeros))
    print("Soma dos valores:", sum(numeros))
    print("Quantidade de itens:", len(numeros))
    
main()
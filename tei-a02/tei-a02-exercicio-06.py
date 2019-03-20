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

def maiorItem(valores):
    return max(valores)

def menorItem(valores):
    return min(valores)

def mediaItens(valores):
    return sum(valores)/len(valores)

def main():
    numeros = []
    vaiOuRacha = True

    while vaiOuRacha:
        try:
            #entrada de dados
            numeros.append(int(input("\nDigite um número: ")))
        except ValueError:
            print("Digite um valor numérico")

        vaiOuRacha = input("\nDigite s para continuar: ")
        if(vaiOuRacha != "s"):
            vaiOuRacha = False
    print(numeros)
    print("Quantidade de pares:", qtdPares(numeros))
    print("Quantidade de impares:", qtdImpares(numeros))
    
    #as duas próximas chamadas não fazem sentido ter uma função, ja que existe a função nativa no python
    print("Maior valor:", maiorItem(numeros))
    print("Menor valor:", menorItem(numeros))

    print("Média dos valores:", mediaItens(numeros))
    
main()
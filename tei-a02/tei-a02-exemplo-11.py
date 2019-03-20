def exibir_intervalo(inicio=0, fim=10, passo=1):
    for item in range(inicio,fim,passo):
        print(item)

exibir_intervalo(1,6,2)
exibir_intervalo(fim=5,passo=2)

def exibir_valores(*valores):
    for valor in valores:
        print(valor)

exibir_valores(10,20,30)
#limpar console
import os
os.system('cls')
vaiOuRacha = True

while vaiOuRacha:
    try:
        #entrada de dados
        peso = float(input("\nInforme o peso: "))
        altura = float(input("Informe a altura: "))

        imc = peso/altura**2
    
        #saida de dados
        print("Peso: {0}\nAltura: {1}\nIMC = {2}".format(peso,altura,imc))
    except ValueError:
        print("Digite um valor numérico")
    
    vaiOuRacha = input("\nDeseja continuar? [s/n]: ")
    if(vaiOuRacha == "n"):
        vaiOuRacha = False
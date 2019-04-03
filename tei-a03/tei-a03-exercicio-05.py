def checkPalindrome(lista):
    listaAoContrario = lista.copy()
    listaAoContrario.reverse()
    
    if lista == listaAoContrario:
        return True
    else:
        return False
    
def main():
    print(checkPalindrome(list(input("Digite uma palavra ou frase para saber se e um palindromo: "))))
        
main()
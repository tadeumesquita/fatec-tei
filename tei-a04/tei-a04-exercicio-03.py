def countPalavras(file,word):
    lista = []
    f = open(file,'r',encoding="utf-8")
    lista = f.read().replace(" ","\n").replace("(","").replace(")","").splitlines()
    f.close()

    print(lista)

    return lista.count(word)


def main():
    word = input("Digite uma palavra: ")
    file = "paises.txt"
    countPalavras(file,word)

    print("A palavra",word,"aparece: ",countPalavras(file,word)," vezes")

main()

def lerArquivo(file,n):
    f = open(file,'r',encoding="utf-8")
    for i in range(n):
        print(f.readline().strip('\n'))
    f.close()

def main():
    n = int(input("Digite o numero de linhas: "))
    file = "paises.txt"
    lerArquivo(file,n)

main()

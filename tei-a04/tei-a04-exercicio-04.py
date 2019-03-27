def copyFile(fileOrigin,fileTarget):

    f1 = open(fileOrigin,'r',encoding="utf-8")
    f2 = open(fileTarget,'w+',encoding="utf-8")
    
    f2.write(f1.read())

    f1.close()
    f2.close()

def main():
    file1 = "paises.txt"
    file2 = "paises-cp.txt"
    copyFile(file1,file2)

main()

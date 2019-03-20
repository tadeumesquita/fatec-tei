f = open("data.txt","w")
f.write("Primeira linha de texto \n")
f.write("Segunda linha de texto \n")
f.close()

f = open("data.txt","a")
f.write("Terceira linha de texto \n")
f.close()

f = open("data.txt","r")
print(f.read())
f.close
lista = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]

#modo leitura/escrita
f = open("data.txt","r+")

#escrever conteúdo da listas
f.writelines(lista)

linhas = f.readlines()
print(linhas)
f.close()
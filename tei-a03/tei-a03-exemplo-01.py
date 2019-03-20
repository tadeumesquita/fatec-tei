#Tuplas
mat = ((1,2,3),(4,5,6))
print(mat[0][0])
print(mat[1])

#Tuplas Nomeadas
import os
import collections

os.system('cls')

Pessoa = collections.namedtuple("Pessoa","id nome idade email")

pessoas = []
pessoas.append(Pessoa(1, "João da Silva", 22, "joaodasilva@gmail.com"))
pessoas.append(Pessoa(2, "Ana Maria", 19, "anamaria@gmail.com"))

for p in pessoas:
    print("Id: %d" %p.id)
    print("Nome: %s" %p.nome)
    print("Idade: %d" %p.idade)
    print("Email: %s\n" %p.email)
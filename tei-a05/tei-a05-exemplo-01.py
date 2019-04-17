import pessoa as p

#para fazer assim não tem que ter construtor
joao = p.pessoa()

joao.nome = "João da Silva"
joao.idade = 22

print("%s %d"%(joao.nome, joao.idade))
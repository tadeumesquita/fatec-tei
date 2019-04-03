import collections

Aluno = collections.namedtuple("Aluno","nome nota1 nota2 media situacao")

alunos = []
somaMedia, aprovados, reprovados = 0, 0, 0

#alunos.append(Aluno("João da Silva", 5, 6, (5+6/2), "Aprovado" if (5+6/2) >= 5 else "Reprovado"))

for i in range(6):
    nome = input("Digite o nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1+nota2)/2
    alunos.append(Aluno(nome,nota1,nota2,media, "Aprovado" if media >= 5 else "Reprovado"))

print("Relatório das Notas")
print("Aluno  Nota1  Nota2  Media  Situacao")
for aluno in alunos:
    print("%s" %aluno.nome,end="  ")
    print("%f" %aluno.nota1,end="  ")
    print("%f" %aluno.nota2,end="  ")
    print("%f" %aluno.media,end="  ")
    print("%s" %aluno.situacao,end="  ")
    print("")

    somaMedia = somaMedia + aluno.media
    if aluno.situacao == "Aprovado":
        aprovados = aprovados + 1 
    if aluno.situacao == "Reprovado":
        reprovados = reprovados + 1 

print("Media da sala:",somaMedia/len(alunos))
print("Total de aprovados:",aprovados)
print("Total de reprovados:",reprovados)
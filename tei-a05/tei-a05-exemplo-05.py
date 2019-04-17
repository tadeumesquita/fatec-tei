import pessoa as person

p = person.pessoaFisica("Ana Maria", 21, "123.456.789-00")

print(isinstance(p,person.pessoa))
print(isinstance(p,person.pessoaFisica))

#descobrir quem é a superclasse
print(person.pessoaFisica.__bases__)
print(person.pessoa.__bases__)

#descobrir se uma classe é uma subclasse de outra
print(issubclass(person.pessoaFisica,person.pessoa))
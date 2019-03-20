
import math
import decimal

msg = "Hello World!"

print(msg)

#comentario de uma linha
"""Documentação, não deve ser usado para comentário de bloco"""

a = 1
print(type(a))
a = "1"
print(type(a))
a = 1.0
print(type(a))

#tipo de dados inteiro
x=2
y=3
print(x+y)

#potenciação
print(pow(x,y))

#arredondamento
print(round(x/y))

#conversoes
x=12
print("em binário é " + bin(x))
print("em hexadecimal é " + hex(x))
print("em octal é " + oct(x))

y = "25"
z = 3 + int(y) #string para int
print(z)

#booleano
a = True
b = False

print(a and b)
print(a or b)

#uso da biblioteca math
i = 2.56
j = 3.66
k = i+j
print(k)

print(math.ceil(k))
print(math.floor(k))
print(round(k,2))

#uso da biblioteca decimal
x = 23
y = 1.05
d = decimal.Decimal(23) / decimal.Decimal("1.05")

print(x/y)
print(d)

#uso de strings
s1 = 'Olá \"Mundo\"!!!'
s2 = "Linguagem de programação 'Python'"
s3 = 'Linguagem de Programação "Python"'
s4 = """Lorem ipsum is
simply dummy text
 of the printing and
  typesetting indutry."""

print(s1)
print(s2)
print(s3)
print(s4)

s = "João da Silva"
print(s[0])
print(s[1])
print(s[:4])
print(s[5:7])

s = "aeiou"
print(s[0]) #acessar item
print(s[-2]) #acessar item pelo fim
print(s[0]*20) #cópias concatenadas
print("a" in s) #teste inclusão
print("x" not in s) #teste inclusão negativo

print(s[0:2])
print(s[2:])
print(s[:2])
print(s[:])

s = "Abcdefg   "
print(chr(65))
print(ord(s[0]))
print(repr(s))
print(len(s))
print(len(s.strip()))
print(s.upper())
print(s.lower())
print(s.capitalize())

#operadores aritméticos
a = 2
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#operadores lógicos
a = 10
b = 20
print(a == b)
print(a !=b )
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

#Operadores Booleanos
v1 = True
v2 = False

print(v1 and v2)
print(v1 or v2)
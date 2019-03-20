s = "aeiou"
try:
    print(s[5])
except IndexError as erro:
    print("A posição não foi encontrada")
    print(erro)
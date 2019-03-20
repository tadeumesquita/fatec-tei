def gerarCurriculo(*valores):

    print("<!DOCTYPE html>",
    "<html>",
    "<head>",
    "<meta charset=\"utf-8\" />",
    "<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">",
    "<title>",valores[0] ,"</title>",
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
    "<link rel=\"stylesheet\" type=\"text/css\" media=\"screen\" href=\"main.css\" />",
    "<script src=\"main.js\"></script>",
    "</head>",
    "<body>",
    "<h1>",valores[0],"</h1>",
    "<h3>",valores[1],"</h3>",
    "<h3>",valores[2],"</h3>",
    "<h3>",valores[3],"</h3>",
    "<p>",valores[4],"</p>",
    "<p>",valores[5],"</p>",
    "</body>",
    "</html>")

def main():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    escolaridade = input("Escolaridade: ")
    experiencia = input("Experiencia Profissional: ")

    gerarCurriculo(nome,endereco,telefone,email,escolaridade,experiencia)
    
main()
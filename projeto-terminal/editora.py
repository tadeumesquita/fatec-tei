#Importação das bibliotecas
import psycopg2
import os

#funções auxiliares
def limparTela():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print("=======LIVRARIA FATEC=======")

def conectarDB():
    pg = psycopg2

    try:
        conexao = pg.connect(
            database="projeto-final-tei",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        return conexao
        #conexao.cursor()
    except Exception as erro:
        print(erro)

def executeSql(cursor,sql):
    cursor.execute(sql)
    return cursor.fetchall()

def login():
    #Entrada dos dados do usuario:
    limparTela()
    print("=======LOGIN=======")
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    
    #conexão com o banco
    conexao = conectarDB()
    cursor = conexao.cursor()

    #verifica se o usuario e a senha estão cadastrados no banco
    sql = "SELECT login FROM usuario WHERE login=%s AND senha=%s"
    cursor.execute(cursor.mogrify(sql,(usuario,senha)))
    linhas = cursor.fetchall()

    conexao.close()

    #se tiver um registro correspondente o login está ok
    if len(linhas) == 1:
        return True
    else:
        return False

#Funções de CRUD

#READ
def listar(tabela, fromMenu=True):
    
    conexao = conectarDB()
    cursor = conexao.cursor()
    limparTela()
    if tabela == "editora":
        sql = "SELECT id,nome FROM editora ORDER BY id"
        print("=====EDITORAS=====\nid | nome")
        linhas = executeSql(cursor,sql)
        for linha in linhas:
            print("---------")
            print(linha[0], '|',linha[1])
    elif tabela == "livro":
        print("=====LIVROS=====\nid | nome | autor | editora")
        sql = "SELECT livro.id, livro.nome, livro.autor, editora.nome as editora FROM livro, editora WHERE livro.id_editora = editora.id ORDER BY livro.id"
        linhas = executeSql(cursor,sql)
        for linha in linhas:
            print("---------")
            print(linha[0], '|',linha[1], '|',linha[2], '|',linha[3])
    elif tabela == "usuario":
        print("=====USUARIOS=====\nlogin | nome")
        sql = "SELECT login,nome FROM usuario ORDER BY login"
        linhas = executeSql(cursor,sql)
        for linha in linhas:
            print("---------")
            print(linha[0], '|',linha[1])
    
    #Se quem chama a função listar for a opção do menu e fica esperando um enter do usuario, caso contrario retorna uma lista com a consulta.
    if fromMenu: 
        input()
    
    conexao.close()


#CREATE
def cadastrar(tabela):
    conexao = conectarDB()
    cursor = conexao.cursor()
    limparTela()

    if tabela == "editora":
        nome = input("=====CADASTRAR EDITORA=====\nDigite o nome editora: ")
        sql = "INSERT INTO editora (nome) values ('{0}')".format(nome)
        cursor.execute(sql)
        conexao.commit()
    elif tabela == "livro":
        listar("editora", False)
        nome = input("=====CADASTRAR LIVRO=====\nDigite o nome do livro: ")
        autor = input("\nDigite o nome do autor: ")
        id_editora = int(input("\nDigite o ID da editora: "))
        sql = "INSERT INTO livro (nome,autor,id_editora) values ('{0}','{1}','{2}')".format(nome,autor,id_editora)
        cursor.execute(sql)
        conexao.commit()
    elif tabela == "usuario":
        login = input("=====CADASTRAR USUARIO=====\nDigite o login do usuario: ")
        senha = input("\nDigite a senha do usuario: ")
        nome = input("\nDigite o nome do usuario: ")
        sql = "INSERT INTO usuario (login,senha,nome) values ('{0}','{1}','{2}')".format(login,senha,nome)
        cursor.execute(sql)
        conexao.commit()

    conexao.close()

#UPDATE
def atualizar(tabela):
    listar(tabela,False)
    conexao = conectarDB()
    cursor = conexao.cursor()
    
    if tabela == "editora":
        id = int(input("\nDigite o ID da editora que deseja atualizar: "))
        nome = input("\nDigite o nome correto da editora: ")
        sql = "UPDATE editora SET nome=%s WHERE id=%s"
        cursor.execute(cursor.mogrify(sql,(nome,id)))
        conexao.commit()
    elif tabela == "livro":
        id = int(input("\nDigite o ID do livro que deseja atualizar: "))
        nome = input("\nDigite o nome correto do livro: ")
        autor = input("\nDigite o nome correto do autor: ")
        sql = "UPDATE livro SET nome=%s, autor=%s WHERE id=%s"
        cursor.execute(cursor.mogrify(sql,(nome,autor,id)))
        conexao.commit()
    elif tabela == "usuario":
        login = input("\nDigite o login do usuario que deseja atualizar: ")
        nome = input("\nDigite o nome correto do usuário: ")
        senha = input("\nDigite a senha nova do usuário: ")
        sql = "UPDATE usuario SET nome=%s, senha=%s WHERE login=%s"
        cursor.execute(cursor.mogrify(sql,(nome,senha,login)))
        conexao.commit()

#DELETE
def excluir(tabela):
    listar(tabela,False)
    conexao = conectarDB()
    cursor = conexao.cursor()
    
    if tabela == "editora":
        id = int(input("\nDigite o ID da editora que deseja excluir: "))
        sql = "DELETE FROM editora WHERE id={0}".format(id)
        cursor.execute(sql)
        conexao.commit()
    elif tabela == "livro":
        id = int(input("\nDigite o ID do livro que deseja excluir: "))
        sql = "DELETE FROM livro WHERE id={0}".format(id)
        cursor.execute(sql)
        conexao.commit()
    elif tabela == "usuario":
        id = input("\nDigite o login do usuario que deseja excluir: ")
        sql = "DELETE FROM usuario WHERE login='{0}'".format(id)
        cursor.execute(sql)
        conexao.commit()

    conexao.close()

def exportarDados():
    return True

def sobre():
    limparTela()
    print("O projeto apresenta de forma simplificada um sistema de uma livraria")
    print("onde são cadastrados os livros e as editoras dos livros.")
    print("Além disso tem os usuários do sistema que podem fazer qualquer ação.")
    print("\n=====DESENVOLVEDORES=====\nAntonio Tadeu Campos Mesquita - RA: 2840481621003\nGuilherme Aroxa - RA: 2840481621025")
    input()

def main():

    opcao = -1

    while opcao!=0:
        if login():
            while opcao!=0:
                limparTela()
                print("=======Editoras=======")
                print("[1] Listar Editoras")
                print("[2] Cadastrar Editora")
                print("[3] Atualizar Editora")
                print("[4] Excluir Editora")
                
                print("======================\n\n=======Livros=======")
                print("[5] Listar Livros")
                print("[6] Cadastrar Livro")
                print("[7] Atualizar Livro")
                print("[8] Excluir Livro")
                
                print("====================\n\n=======Usuários=======")
                print("[9] Listar Usuários")
                print("[10] Cadastrar Usuário")
                print("[11] Atualizar Usuário")
                print("[12] Excluir Usuário")

                print("======================\n\n=======Administração=======")
                print("[13] Exportar dados")

                print("======================\n\n=======Créditos=======")
                print("[14] Sobre o Projeto")
                
                print("\n[0] Sair\n")
                opcao = int(input("Digite uma opção: "))

                if opcao == 1:
                    listar("editora")
                elif opcao == 2:
                    cadastrar("editora")
                elif opcao == 3:
                    atualizar("editora")
                elif opcao == 4:
                    excluir("editora")
                elif opcao == 5:
                    listar("livro")
                elif opcao == 6:
                    cadastrar("livro")
                elif opcao == 7:
                    atualizar("livro")
                elif opcao == 8:
                    excluir("livro")
                elif opcao == 9:
                    listar("usuario")
                elif opcao == 10:
                    cadastrar("usuario")
                elif opcao == 11:
                    atualizar("usuario")
                elif opcao == 12:
                    excluir("usuario")
                elif opcao == 13:
                    exportarDados()
                elif opcao == 14:
                    sobre()
                elif opcao != 0:
                    print("ops... esta opção não é válida!")

        else:
            limparTela()
            print("=======ERRO=======")
            print("Usuario ou senha incorretos!")
            opcao = int(input("Digite 1 para tentar novamente ou 0 para sair: "))

main()
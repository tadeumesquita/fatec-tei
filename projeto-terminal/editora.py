import psycopg2
pg = psycopg2

try:
    conexao = pg.connect(
        database="projeto-final-tei",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    print("Conexão realizada com sucesso!")
    '''
    sql = "CREATE TABLE tb_editora(id_editora SERIAL, nome VARCHAR(50), CONSTRAINT pk_id_editora PRIMARY KEY(id_editora))"
    sql2 = "CREATE TABLE tb_livros(id_livro SERIAL, id_editora INTEGER, titulo VARCHAR(50), CONSTRAINT pk_id_livro PRIMARY KEY(id_livro),CONSTRAINT fk_id_editora FOREIGN KEY(id_editora) REFERENCES tb_editora(id_editora))"
    sql3 = "INSERT INTO tb_editora(nome) values ('FATEC Ribeirão Preto')"
    sql4 = "INSERT INTO tb_livros(id_editora, titulo) values (%s,%s) RETURNING id"
    sql5 = "SELECT * FROM tb_editora"
    sql6 = "UPDATE tb_editora SET nome=%s WHERE id_editora=%s"
    sql7 = "DELETE FROM tb_editora WHERE id=%s"

    cursor = conexao.cursor()
    #cursor.execute(sql5)
    #cursor.execute(cursor.mogrify(sql4,(1,'Python Cookbook'))) #Insert com anti SQL inject, serve para o sql4
    #cursor.execute(cursor.mogrify(sql6,('FATEC RP', 1))) #Insert com anti SQL inject
    cursor.execute(cursor.mogrify(sql7,('FATEC RP', 1))) #Insert com anti SQL inject

    #Retornar o ID inserido
    #id = cursor.fetchone()[0]
    #print("ID = %s" %id)
    
    conexao.commit()
    print("Total de linhas atualizadas: %s" %cursor.rowcount)

    #linhas = cursor.fetchall()

    #for linha in linhas:
    #    print("ID = %d " %linha[0])
    #    print("Nome = %s " %linha[1])
    
    conexao.close()

    print("Operação realizada com sucesso!")
    '''
except Exception as erro:
    print(erro)
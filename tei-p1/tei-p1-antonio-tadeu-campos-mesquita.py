#Tópicos especiais em informática
#Prova 1
#Antonio Tadeu Campos Mesquita | RA: 2840481621003
import os
import json

os.system('cls')

produtos = []

#Questao 2
def cadastrarProduto(produtos):
    #incrementar o codigo do produto
    if len(produtos) == 0:
        codigoProduto = 1
    else:
        codigoProduto = produtos[-1][1] + 1

    print("\n=======CADASTRO DE PRODUTO=======")
    nome = input("Nome do produto: ")
    valorCompra = float(input("Valor de compra: "))
    qtdeEstoque = int(input("Quantidade em estoque: "))
    produto = [nome,codigoProduto,valorCompra,qtdeEstoque]
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

#Questão 3
def relatorioDeProdutos(produtos):
    print("\n=======RELATÓRIO DE PRODUTOS=======")
    print("Codigo | Nome | Valor de Compra | Valor de Venda | Quantidade no estoque")
    produtos.sort()
    for produto in produtos:
        print(produto[1],"|",produto[0],"|",produto[2],"|",produto[2]*1.25,"|",produto[3])
    
#Questão 4
def relatorioEstoqueBaixo(produtos):
    print("\n=======PRODUTOS COM ESTOQUE BAIXO=======")
    print("Nome | Quantidade no estoque")
    produtos.sort()
    for produto in produtos:
        if(produto[3]<=5):
            print(produto[0],"|",produto[1])

#Questão 5
def exportarDados(produtos):
    dados = {}
    for produto in produtos:
        dados[produto[1]] = {"codigo":produto[1],"nome":produto[0],"valor_compra":produto[2],"quantidade":produto[3]}

    fjson = open("relatorioDeProdutos.json","w",encoding="utf-8")
    json.dump(dados,fjson,sort_keys=True,indent=4)
    fjson.close()

def main():
    opcao = -1

    #Questao 1
    while opcao!=0:
        print("\n=======Varejão do João=======")
        print("[1] Cadastrar produto")
        print("[2] Relatório de Produtos")
        print("[3] Relatório de Estoque Baixo")
        print("[4] Exportar dados")
        print("[0] Sair")
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            cadastrarProduto(produtos)
        elif opcao == 2:
            relatorioDeProdutos(produtos)
        elif opcao == 3:
            relatorioEstoqueBaixo(produtos)
        elif opcao == 4:
            exportarDados(produtos)
        elif opcao != 0:
            print("ops... esta opção não é válida!")

main()
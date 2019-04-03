import collections

Produto = collections.namedtuple("Produto","nome preco")

produtos = []
valoresMedios = []
qtdeBaratos, qtdeCaros, somaPrecoCaros = 0, 0, 0

for i in range(5):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    produtos.append(Produto(nome,preco))

for produto in produtos:
    if produto.preco < 50:
        qtdeBaratos = qtdeBaratos + 1
    elif 50 <= produto.preco <= 100:
        valoresMedios.append(produto.nome)
    else:
        qtdeCaros = qtdeCaros + 1
        somaPrgitecoCaros = somaPrecoCaros + produto.preco

print("Quantidade de produtos abaixo de R$50,00:",qtdeBaratos)
print("Produtos com preço entre R$50,00 e R$100,00:")
for produto in valoresMedios:
    print(produto)
print("Média de preços dos produtos acima de R$100,00:",somaPrecoCaros/qtdeCaros)
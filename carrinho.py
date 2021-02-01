carrinho = []
produto = ''

while produto != 'sair':
    produto = input("adicione produtos ao carrinho, se quiser sair digite a palavar 'sair': ")
    if produto != 'sair':
        carrinho.append(produto)
        print(produto)

    #print('lista de compras: ',carrinho)

for produto in carrinho:
    print(produto)
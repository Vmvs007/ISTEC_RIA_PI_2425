produtos = {
    "bolachas": [15, 2.9],
    "água": [50, 1.0],
    "cenouras": [5, 0.2],
    "batatas": [20, 0.5]
}

opcao = 1

while (opcao != 0):
    print("\n\n********** Gestão de Vendas/Produtos **********")
    print("1. Adicionar Venda")
    print("2. Calcular Total de Vendas - Produto")
    print("3. Calcular Total de Vendas - Loja")
    print("4. Consultar Vendas")
    print("0. Sair")
    opcao = int(input("Insira a opção: "))

    match (opcao):

        case 1:  # Adicionar Venda
            produtoVendido = input("Produto Vendido: ")
            quantidadeVendida = int(input("Quantidade Vendida: "))

            if (produtoVendido in produtos):
                # O produto já existe
                produtos[produtoVendido][0] += quantidadeVendida
            else:
                # O produto não existe
                precoUnitario = float(input("Preço Unitário: "))
                produtos[produtoVendido] = [quantidadeVendida, precoUnitario]

        case 2:  # Calcular Total de Vendas - Produto
            produtoConsulta = input("Produto : ")

            if (produtoConsulta in produtos):
                totalVendasProduto = produtos[produtoConsulta][0] * produtos[produtoConsulta][1]

                print(f"Total de Vendas de {produtoConsulta}: {totalVendasProduto} €")
            else:
                print(f"{produtoConsulta} nunca foi vendido na loja.")

        case 3:  # Calcular Total de Vendas - Loja

            totalVendas=0.0

            for produto in produtos:
                totalVendas+= produtos[produto][0]*produtos[produto][1]

            print(f"Total Vendas: {totalVendas} €")


        case 4:  # Consultar Vendas
            print(produtos)
        case 0:
            print("Sair do Programa...")
        case _:
            print("Opção Inválida")

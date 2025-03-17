listaCompras = {}

opcao = 1

while (opcao != 0):
    print("\n**** Lista de Compras *****")
    print("1. Listar Produtos")
    print("2. Adicionar Novo Produto")
    print("3. Calcular Total")
    print("0. Sair")

    opcao = int(input("\nInsira a sua opção: "))

    match opcao:
        case 1:  # Listar Produtos
            print(listaCompras)

        case 2:  # Adicionar Novo Produto
            novoProduto = input("Novo Produto: ")
            novoPreco = float(input("Novo Preço: "))

            if novoProduto not in listaCompras:  # Se ainda não existe
                listaCompras[novoProduto] = novoPreco
            else:  # Se já existe, acrescenta o valor
                listaCompras[novoProduto] += novoPreco

        case 3:  # Calcular Total
            total = 0.0

            for produto in listaCompras:
                total += listaCompras[produto]

            print(f"Total da Lista: {total} €")

        case 0:  # Sair
            print("Sair do Programa...")

        case _:  # Opção Inválida
            print("Opção Inválida!")

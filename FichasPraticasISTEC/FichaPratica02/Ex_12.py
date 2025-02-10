# Apresentar as opções
print("1. Criar")
print("2. Atualizar")
print("3. Eliminar")
print("4. Sair")

opcao = int(input("Insira a sua opção: "))

match (opcao):
    case 1:
        print("***** Criar *****")

    case 2:
        print("***** Atualizar *****")

    case 3:
        print("***** Eliminar *****")

    case 4:
        print()

    case _:
        print("***** Opcão Inválida *****")

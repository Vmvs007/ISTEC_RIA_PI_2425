listaContactos = []

opcao = 1

while (opcao != 0):
    print("\n***** Gestão de Contactos *****")
    print("1. Adicionar Novo Contacto")
    print("2. Atualizar Contacto")
    print("3. Excluir Contacto")
    print("4. Listar Contactos")
    print("0. Sair")

    opcao = int(input("Insira a opção: "))

    match opcao:
        case 1:
            print("\nAdicionar Novo Contacto")

            nomeInserido = input("Insira o nome: ")
            telefoneInserido = input("Insira o telefone: ")
            emailInserido = input("Insira o email: ")
            cidadeInserida = input("Insira a cidade: ")

            contactoNovo = {
                "nome": nomeInserido,
                "telefone": telefoneInserido,
                "email": emailInserido,
                "cidade": cidadeInserida
            }

            listaContactos.append(contactoNovo)
            print("Novo contacto adicionado com sucesso!")

        case 2:
            print("\nAtualizar Contacto")

            nomeAlterar= input("Insira o nome completo:")

            # Encontrar o contacto
            for i in range(len(listaContactos)):
                if(listaContactos[i]["nome"] == nomeAlterar):
                    listaContactos[i]["telefone"]= input("Insira o telefone: ")
                    listaContactos[i]["email"] = input("Insira o email: ")
                    listaContactos[i]["cidade"] = input("Insira a cidade: ")


        case 3:
            print("\nExcluir Contacto")

        case 4:
            print("\nListar Contactos")

            for i in range(len(listaContactos)):
                print("-------------------------------------------------------------------------")
                print(listaContactos[i])

            print("-------------------------------------------------------------------------")

        case 0:
            print("\nSair do Programa...")

        case _:
            print("\nOpção Inválida")

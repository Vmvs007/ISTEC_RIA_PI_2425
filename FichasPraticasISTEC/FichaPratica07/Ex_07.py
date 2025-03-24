biblioteca = []

opcao = 1

while (opcao != 0):
    print("\n********** Gestão da Biblioteca **********")
    print("1. Adicionar Livro")
    print("2. Emprestar/Receber Livros")
    print("3. Listar Disponíveis")
    print("4. Remover Livro")
    print("0. Sair")

    opcao = int(input("Selecione uma opção: "))

    match (opcao):
        case 1:  # Adicionar Livro
            print("***** NOVO LIVRO *****")
            novoISBN = input("ISBN: ")
            novoTitulo = input("Título: ")
            novoAutor = input("Autor: ")
            novoAno = int(input("Ano Publicação: "))

            novoLivro = {
                "isbn": novoISBN,
                "titulo": novoTitulo,
                "autor": novoAutor,
                "ano": novoAno,
                "disponibilidade": True
            }

            biblioteca.append(novoLivro)

        case 2:  # Emprestar/Receber Livros
            print("***** EMPRESTAR/RECEBER *****")

            encontreiLivro = False
            isbnUtilizador = input("ISBN: ")

            for livro in biblioteca:
                if (livro["isbn"] == isbnUtilizador):
                    # Encontramos o livro
                    encontreiLivro = True

                    if (livro["disponibilidade"] == True):
                        livro["disponibilidade"] = False
                    else:
                        livro["disponibilidade"] = True

                    print("Disponibilidade Atualizada")

            if (encontreiLivro == False):
                print("ISBN não encontrado...")

        case 3:  # Listar Disponíveis
            print("***** LIVROS DISPONIVEIS *****")
            for livro in biblioteca:
                if (livro["disponibilidade"] == True):
                    print(livro)

        case 4:  # Remover Livro
            print("***** REMOVER LIVRO *****")

            encontreiLivro = False
            isbnRemover = input("ISBN: ")

            for livro in biblioteca:
                if (livro["isbn"] == isbnRemover):
                    # É este o livro a remover
                    encontreiLivro = True
                    biblioteca.remove(livro)
                    print("Livro Removido...")

            if(encontreiLivro==False):
                print("ISBN não encontrado...")

        case 0:  # Sair
            print("Sair do Programa...")

        case _:  # Opção Inválida
            print("Opção Inválida!")

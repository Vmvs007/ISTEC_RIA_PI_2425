import json


def pesquisarPorArtista(dados, artistaPesquisar):
    for musica in dados:
        if (musica["Artista"] == artistaPesquisar):
            print(musica)


def menu(dados):
    opcao = 1

    while (opcao != 0):
        print("\n********** Músicas **********")
        print("1. Pesquisar por Género")
        print("2. Pesquisar por Artista")
        print("3. Maior Música")
        print("4. Músicas acima de X duração")
        print("5. Quantidade de Músicas")

        print("0. Sair")

        opcao = int(input("Opção: "))
        print()

        match (opcao):
            case 1:
                print("Pesquisar por Género")

            case 2:
                print("Pesquisar por Artista")
                artistaInput = input("Artista")
                pesquisarPorArtista(dados, artistaInput)

            case 3:
                print("Maior Música")

            case 4:
                print("Músicas acima de X duração")

            case 5:
                print("Quantidade de Músicas")

            case 0:
                print("*** Sair ***")

            case _:
                print("*** Opção Inválida ***")

    return dados


def carregar_dados(caminho):
    with open(caminho, 'r') as ficheiro:
        dados = json.load(ficheiro)

    return dados


def guardar_dados(caminho, dados):
    with open(caminho, 'w') as ficheiro:
        json.dump(dados, ficheiro, indent=4)


if __name__ == "__main__":
    caminhoFicheiro = "../Ficheiros/musicas.json"

    dados = carregar_dados(caminhoFicheiro)
    dados = menu(dados)
    guardar_dados(caminhoFicheiro, dados)

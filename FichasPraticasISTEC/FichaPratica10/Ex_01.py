import json


def imprimir_funcionario(funcionario):
    print(f"Nome: {funcionario["nome"]}")
    print(f"Idade: {funcionario["idade"]}")
    print(f"Cargo: {funcionario["cargo"]}")
    print(f"Salario: {funcionario["salario"]}")
    print("_________________________________________")


def listar_funcionarios(dadosFuncionarios):
    for funcionario in dadosFuncionarios:
        imprimir_funcionario(funcionario)


def filtrar_salario_5000(dadosFuncionarios):
    for funcionario in dadosFuncionarios:

        if (funcionario["salario"] >= 5000):
            imprimir_funcionario(funcionario)


def adicionar_funcionario(dadosFuncionarios, nome, idade, cargo, salario):
    dadosFuncionarios.append({"nome": nome, "idade": idade, "cargo": cargo, "salario": salario})
    return dadosFuncionarios


def menu(dadosFuncionarios):
    opcao = 1

    while (opcao != 0):
        print("\n********** Gestão de Funcionários **********")
        print("1. Listar Funcionários")
        print("2. Funcionários que ganham acima de 5000 €")
        print("3. Subir salários em 10%")
        print("4. Adicionar novo funcionário")
        print("0. Sair")

        opcao = int(input("Opção: "))
        print()

        match (opcao):
            case 1:
                print("*** Listar Funcionários ***")
                listar_funcionarios(dadosFuncionarios)

            case 2:
                print("*** Funcionários que ganham acima de 5000 € ***")
                filtrar_salario_5000(dadosFuncionarios)
            case 3:
                print("*** Subir salários em 10% ***")

            case 4:
                print("*** Adicionar novo funcionário ***")
                nomeInput = input("Nome: ")
                idadeInput = int(input("Idade: "))
                cargoInput = input("Cargo: ")
                salarioInput = float(input("Salário: "))

                dadosFuncionarios = adicionar_funcionario(dadosFuncionarios, nomeInput, idadeInput, cargoInput,
                                                          salarioInput)

            case 0:
                print("*** Sair ***")

            case _:
                print("*** Opção Inválida ***")

    return dadosFuncionarios


def carregar_dados(caminho):
    with open(caminho, 'r') as ficheiro:
        dados = json.load(ficheiro)

    return dados


def guardar_dados(caminho, dados):
    with open(caminho, 'w') as ficheiro:
        json.dump(dados, ficheiro, indent=4)


if __name__ == "__main__":
    caminhoFicheiro = "../Ficheiros/funcionarios.json"

    dadosFuncionarios = carregar_dados(caminhoFicheiro)
    dadosFuncionarios = menu(dadosFuncionarios)
    guardar_dados(caminhoFicheiro, dadosFuncionarios)

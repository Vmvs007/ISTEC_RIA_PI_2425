opcaoLogin = 1
userAdmin = "admin"
passAdmin = "123456"

taxas = {"USD": 1.0, "EUR": 0.85, "BRL": 5.25, "MEX_PESO": 20.15, "FIL_PESO": 58.04, "GBP": 0.78}

while (opcaoLogin != 0):
    print("\n\n********** PROGRAMA TAXAS DE CÂMBIO **********")
    print("1. Utilizador")
    print("2. Administrador")
    print("0. Sair")
    opcaoLogin = int(input("Tipo de Utilizador: "))

    match (opcaoLogin):
        case 1:  # Utilizador ________________________________________________________________________

            opcaoUtilizador = 1

            while (opcaoUtilizador != 0):
                print("\n\n********** PROGRAMA TAXAS DE CÂMBIO: UTILIZADOR **********")
                print("1. Consultar Taxas")
                print("2. Cambiar Moedas")
                print("0. Voltar")

                opcaoUtilizador = int(input("Opção: "))

                match (opcaoUtilizador):
                    case 1:
                        print("\n***** CONSULTAR TAXAS *****")
                        print(taxas)

                    case 2:
                        print("\n***** CAMBIAR MOEDAS *****")

                        moedaOrigem = input("Moeda Original: ")
                        moedaDestino = input("Moeda Destino: ")
                        valorCambio = float(input("Valor: "))

                        if (moedaOrigem in taxas and moedaDestino in taxas):  # Ambas as moedas são válidas
                            valorConvertido = (taxas[moedaDestino] * valorCambio) / taxas[moedaOrigem]
                            print(f"{valorCambio} {moedaOrigem} = {valorConvertido} {moedaDestino}")
                        else:
                            print("Moeda não reconhecida! ")
                    case 0:
                        print()

                    case _:
                        print("Opção não reconhecida!")

        case 2:  # Administrador ________________________________________________________________________
            userInput = input("Username: ")
            passwordInput = input("Password: ")

            if (userInput == userAdmin and passwordInput == passAdmin):  # Acesso Válido

                opcaoAdmin = 1

                while (opcaoAdmin != 0):
                    print("\n\n********** PROGRAMA TAXAS DE CÂMBIO: ADMINISTRADOR **********")
                    print("1. Alterar Taxas Câmbio")
                    print("2. Nova Moeda")
                    print("3. Alterar Password")
                    print("0. Voltar")

                    opcaoAdmin = int(input("Opção: "))

                    match (opcaoAdmin):
                        case 1:  # Alterar Taxas Câmbio
                            print("\n***** ALTERAR TAXAS CÂMBIO *****")

                            # Perguntar moeda
                            moedaAlterar = input("Moeda: ")

                            if(moedaAlterar in taxas):
                                # Imprimir a taxa atual
                                print(f"{moedaAlterar}:{taxas[moedaAlterar]}")

                                # Perguntar a nova taxa
                                novaTaxa = input("Nova Taxa: ")

                                # Aplicar a nova taxa
                                taxas[moedaAlterar] = novaTaxa

                                # Imprimir a nova taxa
                                print(f"{moedaAlterar}:{taxas[moedaAlterar]}")

                            else:
                                print("Moeda não reconhecida...")

                        case 2:  # Nova Moeda
                            print("\n***** NOVA MOEDA *****")

                            moedaNova =input("Moeda Nova: ")

                            if(moedaNova not in taxas):
                                valorNovo= float(input("Valor: "))
                                taxas[moedaNova]=valorNovo
                            else:
                                print("Moeda já existe...")

                        case 3:  # Alterar Password
                            print("\n***** ALTERAR PASSWORD *****")
                            passAdmin=input("Password Nova: ")

                        case 0:
                            print()

                        case _:
                            print("Opção não reconhecida!")
            else:
                print("Acesso negado...")
        case 0:
            print("Sair do Programa...")

        case _:
            print("Opção não reconhecida!")

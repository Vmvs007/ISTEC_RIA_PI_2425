lugar = int(input("Insira o seu lugar na corrida: "))

match lugar:
    case 1:
        print("Ganhou 10 pontos")

    case 2:
        print("Ganhou 8 pontos")

    case 3:
        print("Ganhou 6 pontos")

    case 4:
        print("Ganhou 5 pontos")

    case 5:
        print("Ganhou 4 pontos")

    case 6:
        print("Ganhou 3 pontos")

    case 7:
        print("Ganhou 2 pontos")

    case 8:
        print("Ganhou 1 pontos")

    case _:
        print("Não ganhou pontos")

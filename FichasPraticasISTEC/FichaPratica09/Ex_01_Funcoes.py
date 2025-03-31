def lerInteiroPositivo():
    num = -1

    while (num < 0):
        num = int(input("Insira número inteiro positivo: "))

    return num



def imprimirAsteriscos(numAsteriscos):

    for i in range(numAsteriscos):
        print("*", end="")

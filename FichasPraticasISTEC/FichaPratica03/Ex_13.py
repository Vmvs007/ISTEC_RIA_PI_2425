inicio = int(input("Início do Intervalo: "))
fim = int(input("Fim do Intervalo: "))
salto = 1

while (inicio <= fim):
    if (inicio % 5 == 0):
        print(inicio)

    inicio = inicio + salto

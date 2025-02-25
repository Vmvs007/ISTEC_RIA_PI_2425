lista = []

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

maiorPar = -1
lista.sort()

for i in lista:
    if (i % 2 == 0):
        maiorPar = i

if (maiorPar % 2 == 0):
    print("Maior Par:", maiorPar)
else:
    print("Não há pares")

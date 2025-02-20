lista = []

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

menor = lista[0]

for i in range(10):
    if (lista[i] < menor):
        menor = lista[i]

print("Menor:", menor)

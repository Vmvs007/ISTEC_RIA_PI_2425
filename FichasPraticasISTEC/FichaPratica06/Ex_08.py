lista = []

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

for i in range(len(lista) - 1, -1, -1):
    print(lista[i])

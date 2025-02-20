lista = []

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

maior = lista[0]

for i in range(10):
    if (lista[i] > maior):
        maior = lista[i]

print("Maior:", maior)

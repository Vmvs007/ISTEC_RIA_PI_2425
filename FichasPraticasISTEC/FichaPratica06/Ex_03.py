lista = []

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

lista.sort()
maior=lista[9]


print("Maior:",maior)

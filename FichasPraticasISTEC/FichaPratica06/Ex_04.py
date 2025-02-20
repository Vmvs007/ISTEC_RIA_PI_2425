lista = []

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

lista.sort()
menor=lista[0]


print("Maior:",menor)

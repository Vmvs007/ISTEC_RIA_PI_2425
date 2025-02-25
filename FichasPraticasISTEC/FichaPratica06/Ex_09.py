lista = []

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

numPesquisa = int(input("Numero a pesquisar: "))
existe = False

for i in lista:
    if (i == numPesquisa):
        existe = True

if (existe):
    print(f"O número {numPesquisa} existe na lista.")
else:
    print(f"O número {numPesquisa} não existe na lista.")

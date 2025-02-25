lista = []

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

numPesquisa = int(input("Numero a pesquisar: "))
existe = False

for i in range(0, len(lista)):
    if (lista[i] == numPesquisa): # Encontramos o número a pesquisar
       existe=True
       print(f"Existe na lista[{i}]")

if (not existe): # A mesma coisa que: existe == False
    print(f"O número {numPesquisa} não existe na lista.")

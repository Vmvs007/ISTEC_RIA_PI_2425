lista = []
crescente = True

for i in range(10):
    lista.append(int(input(f"Insira na lista[{i}]: ")))

for i in range(1,10):
    if (lista[i]<=lista[i-1]):
        crescente=False

print(lista)

if(crescente):
    print("Lista crescente")
else:
    print("Lista não crescente")

num = 0
somatorio = 1
contador = -1

while (num != -1):
    num = int(input("Introduza um número: "))
    somatorio += num
    contador += 1

print("Somatório:", somatorio)
print("Contador:", contador)

media = somatorio / contador

print("Média:", media)

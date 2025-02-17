numeroInserido = int(input("Insira um número para calcular os divisores: "))

print("Divisores:")

for i in range(1, numeroInserido + 1):
    if (numeroInserido % i == 0):
        print(i)

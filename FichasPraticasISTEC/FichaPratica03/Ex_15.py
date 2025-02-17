num = int(input("Insira um número para calcular o fatorial: "))
fatorial = 1

while (num > 0):
    fatorial = fatorial * num
    num -= 1

print("Fatorial:", fatorial)

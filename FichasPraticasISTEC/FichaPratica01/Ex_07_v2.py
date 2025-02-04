total = 0

# Ler 3 preços
preco = float(input("Insira o preço do 1º produto: "))

total = total + preco

preco = float(input("Insira o preço do 2º produto: "))

total = total + preco

preco = float(input("Insira o preço do 3º produto: "))

total = total + preco

total = total * 0.9

print("Total com 10% de desconto:", total)

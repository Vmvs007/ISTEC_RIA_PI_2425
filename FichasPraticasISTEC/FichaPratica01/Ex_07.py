# Ler 3 preços
preco1 = float(input("Insira o preço do 1º produto: "))
preco2 = float(input("Insira o preço do 2º produto: "))
preco3 = float(input("Insira o preço do 3º produto: "))

# Somar 3 preços
total = preco1+preco2+preco3

# Aplicar 10% de desconto
totalComDesconto= total*0.9

# Apresentar o preço com desconto
print("Total com 10% de desconto:",totalComDesconto)

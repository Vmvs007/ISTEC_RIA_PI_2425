# Declarar a lista e as variáveis
lista = []
numInserido = 0

# Permitir que o utilizador preencha a lista (até introduzir um número negativo)
while (numInserido >= 0):
    numInserido = int(input("Insira um número: "))
    lista.append(numInserido)

# Função len() dá o tamanho da lista em questão
print("Tamanho da Lista:", len(lista))

# Declarar a variável soma que vai acumular todos os valores da lista
soma = 0

# Ciclo que vai correr com i entre 0 e tamanho da lista (exclusive)
# Se o tamanho da lista é 6, i será todos os valores inteiros entre 0 e 6 (exclusive)
for i in range(len(lista)):
    soma += lista[i]

print(lista)

# Calcular a média (dividir o somatorio pela quantidade de elementos)
media = soma / len(lista)

print("Média:", media)

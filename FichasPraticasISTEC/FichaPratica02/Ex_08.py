# Ler 3 notas
nota1 = float(input("Insira a 1º nota: "))
nota2 = float(input("Insira a 2º nota: "))
nota3 = float(input("Insira a 3º nota: "))

# Calcular a média ponderada
mediaPonderada = (nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.4)

# print("Média",mediaPonderada)

# Avaliar se a média ponderada é positiva
if (mediaPonderada >= 9.5):
    print("Aprovado")
else:
    print("Reprovado")

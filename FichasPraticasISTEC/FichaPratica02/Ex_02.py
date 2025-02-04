# Ler salario
salario = float(input("Insira o salário anual: "))

# Avaliar se o salário é abaixo de 15.000
if (salario <= 15000):
    taxa = salario * 0.2
    print("Taxa 20%:", taxa)
else:
    taxa = salario * 0.3
    print("Taxa 30%:", taxa)

# Ler salario
salario = float(input("Insira o salário anual: "))

if (salario <= 15000):
    taxa = salario * 0.2
    print("Taxa 20%:", taxa)

if (salario > 15000 and salario <= 20000):
    taxa = salario * 0.3
    print("Taxa 30%:", taxa)

if (salario > 20000 and salario <= 25000):
    taxa = salario * 0.35
    print("Taxa 35%:", taxa)

if (salario > 25000):
    taxa = salario * 0.4
    print("Taxa 40%:", taxa)
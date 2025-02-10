# Ler saldo
saldo = float(input("Insira o seu saldo: "))

# Ler movimento
movimento = float(input("Montante a creditar/debitar: "))

saldoAposMovimento = saldo + movimento

if (saldoAposMovimento >= 0):  # Temos saldo para concluir a operacao
    saldo = saldoAposMovimento
else:  # Não temos saldo
    print("Operação Inválida. Saldo Insuficiente")

print("Saldo Atual:", saldo)

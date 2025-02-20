comissoes = []
total = 0.0

for i in range(12):
    comissoes.append(float(input(f"Insira comissão no mês {i + 1}: ")))
    total+=comissoes[i]

print(comissoes)
print(f"Total Anual: {total} €")

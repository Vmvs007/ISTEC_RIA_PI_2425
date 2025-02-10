# Ler dois números
num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

# Ler a operação
operacao = input("Operação Desejada ( + - * / ): ")

# Apresentar o resultado
if (operacao == "+"):
    resultado = num1 + num2
    print("Soma:", resultado)

elif (operacao == "-"):
    resultado = num1 - num2
    print("Subtração:", resultado)

elif (operacao == "*"):
    resultado = num1 * num2
    print("Multiplicação:", resultado)

elif (operacao == "/"):
    resultado = num1 / num2
    print("Divisão:", resultado)

else:
    print("Operação não reconhecida!")

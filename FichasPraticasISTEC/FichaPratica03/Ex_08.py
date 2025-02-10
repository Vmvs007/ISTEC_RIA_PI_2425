numero = int(input("Insira um número: "))

antecessor = numero - 5
sucessor = numero + 5

while (antecessor < numero):
    print(antecessor)
    antecessor += 1

while(numero<sucessor):
    print(numero+1)
    numero+=1
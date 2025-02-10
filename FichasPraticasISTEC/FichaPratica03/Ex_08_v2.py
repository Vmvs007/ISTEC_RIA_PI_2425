numero = int(input("Insira um número: "))

antecessor = numero - 5
sucessor = numero + 5

while(antecessor<=sucessor):
    if(antecessor!=numero):
        print(antecessor)
    antecessor+=1
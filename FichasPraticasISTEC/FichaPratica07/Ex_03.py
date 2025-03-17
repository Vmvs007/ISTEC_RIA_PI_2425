tradutor = {
    "dog": "cachorro",
    "cat": "gato",
    "house": "casa",
    "car": "carro",
    "computer": "computador"
}

while True:
    palavraInput = input("\nEnter a word: ")

    if palavraInput in tradutor:
        print("Translation:", tradutor[palavraInput])
    else:
        print("Translation not found")

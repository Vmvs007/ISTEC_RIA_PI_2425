alunos = {
    "João": [8, 7, 9],
    "Maria": [16, 19, 18],
    "Ana": [19, 18, 20]
}

alunoPesquisar = input("Pesquisa de Aluno: ")

if alunoPesquisar in alunos:
    # Temos este aluno no dicionário
    somaNotas = 0
    for i in range(len(alunos[alunoPesquisar])):
        somaNotas += alunos[alunoPesquisar][i]

    mediaNotas = somaNotas / len(alunos[alunoPesquisar])
    print("Média:", mediaNotas)

else:
    print("Aluno não encontrado!")

# Crie uma função que recebe um dicionário onde as chaves são nomes de alunos e os valores são listas com suas notas. A função deve calcular a média das notas de cada aluno e retornar um novo dicionário com os nomes e suas respectivas médias.

# {"nome aluno" : lista_notas }
# item = conjunto chave-valor
dicionario_notas = {
    "Ana": [7, 8, 9],
    "João": [6, 5, 7],
    "Maria": [9, 9, 10],}

def calcular_media(dicionario_notas):
    medias = {}
    for aluno, notas in dicionario_notas.items():
        media = sum(notas)/len(notas)
        medias[aluno] = media
    return medias
print(f"Alunos e suas respectivas médias: {calcular_media(dicionario_notas)}")


# outra maneira mais simplificada:

dicionario_notas = {
    "Ana": [7, 8, 9],
    "João": [6, 5, 7],
    "Maria": [9, 9, 10],
}

def calcular_media(dicionario_notas):
    # Compreensão de dicionário para calcular a média de cada aluno
    return {aluno: sum(notas) / len(notas) for aluno, notas in dicionario_notas.items()}

# Chamada da função e impressão do resultado
print(f"Alunos e suas respectivas médias: {calcular_media(dicionario_notas)}")

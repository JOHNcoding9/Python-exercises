#o professor quer sortear um dos 4 alunos para apagar o quadro. faça um programa que leia e escreva o nome do escolhido
alunos=list()
for i in range(0,4):
    aluno=input(f"digite o nome do {i+1} aluno: ")
    alunos.append(aluno)
import random
posicao=random.randint(0,3)
print("o aluno sorteado foi: ", alunos[posicao])


# ou então, ao invés de random.randint  posso usar também o random.choice (opção melhor para string):

lunos=list()
for i in range(0,4):
    aluno=input(f"digite o nome do {i+1} aluno: ")
    alunos.append(aluno)
import random
print(f"o aluno sorteado foi {random.choice(alunos)}")
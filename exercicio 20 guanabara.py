#o mesmo professor do exercicio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos faça um programa que mostre o nome dos 4 alunos e a ordem sorteada
alunos=list()
for i in range(0,4): # a variavel i assumirá valores de 0 a 3 (4 numeros). Toda a vez que chegar no fim do bloco de código, o valor será trocado para o próximo número e ciclo repete
    aluno=input(f"digite o nome do {i+1} aluno: ") # o i começará sendo i=0
    alunos.append(aluno) #concatena a variavel aluno para a lista de alunoS
import random
random.shuffle(alunos) #embaralha a lista de alunoS
print(f""" o primeiro aluno será {alunos[0]}
      o segundo aluno será {alunos[1]}
      o terceiro aluno será {alunos[2]} 
      o quarto aluno será {alunos[3]}""") # os números entre [] se referem á posições da lista alunoS

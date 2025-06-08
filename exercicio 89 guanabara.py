# crie um programa que leia o nome  duas notas  de vários alunos e guarde todos em uma lista composta> No final, mostre um boletim contendo a média de cada um e permita que o usuario solicite mostrar as notas de cada aluno individualmente.

lista_composta = [[],[],[]]
cont = 0

while True:
    
    resposta = str(input("Quer Prosseguir? [S/N] "))

    if resposta in "Nn":
        break

    nome = str(input("Digite o nome do aluno: "))
    nota_1 = float(input("Primeira nota do aluno: "))
    nota_2 = float(input("Segunda nota do aluno: "))
   
    lista_composta[2].insert(cont, nota_1)
    lista_composta[2].insert(cont + 1, nota_2)

    media = (nota_1 + nota_2) / 2
    
    lista_composta[0].insert(cont, nome)         
    lista_composta[1].insert(cont, media)
    cont += 1

print(f"{'No.':<5} {'NOME':<15} {'MÉDIA':<10}")

for x in range(cont):
    print(f"{x:<5} {lista_composta[0][x]:<15} {lista_composta[1][x]:<10.2f}")

while True:
 print("=" * 50)
 pergunta = int(input("Mostrar as notas de qual aluno? [-1 para encerrar]: "))

 if pergunta == -1:
    break
 
 print(f" Notas do {lista_composta[0][pergunta]}: {lista_composta[2][pergunta], lista_composta[2][pergunta + 1]}")

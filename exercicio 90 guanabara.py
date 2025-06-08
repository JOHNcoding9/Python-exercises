# Faça um programa que leia  nome e média de um aluno, guardando tambem a situação em um dicionario

aluno = {}
aluno["nome"] = str(input("digite o nome do aluno: "))
aluno["média"] = float(input("digite a sua média: "))
if aluno["média"] < 5:
    aluno["situação"] = "reprovado"

elif 5 < aluno["média"] < 7:
    aluno["situação"] = "recuperação"

else:
    aluno["situação"] =  "aprovado"

for keys,values in aluno.items():
    print(f"{keys} é igual a {values}")


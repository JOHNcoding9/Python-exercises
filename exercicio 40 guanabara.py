#calcule a média de um aluno e exiba as seguintes mensagens de acordo com as médias
notas=[]
quantidade=int(input("Insira a quantidade de provas realizadas: "))
for i in range(quantidade):
    nota=float(input(f"Insira a nota da prova {i+1}: "))
    notas.append(nota)
media=sum(notas)/len(notas)
if media<5:
    print("REPROVADO",media)
if 5<media<6.9:
    print("Recuperação",media)
else:
    print("Aprovado",media)
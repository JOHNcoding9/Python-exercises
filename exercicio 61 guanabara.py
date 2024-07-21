# crie um programa que leia o primeiro termo e a razão de um a PA (progressão aritimética). mostre os 10 primeiros termos da progressão USANDO A FUNÇÃO "WHILE" APENAS
print("=-="*30)
print("                Os 10 primeiros termos de qualquer PA")
print("=-="*30)
#definidno o termo e a razao da PA
termo=int(input("Insira o primeiro termo da PA: "))
razao=int(input("Digite a razão desta PA: "))
contador=0
while contador<10:
    print(f"{termo} -> ",end=" ")
    termo+=razao
    contador+=1
print("FIM")
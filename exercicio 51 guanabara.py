# crie um programa que leia o primeiro termo e a razão de um a PA (progressão aritimética). mostre os 10 primeiros termos da progressão

print("=-="*30)
print("                Os 10 primeiros termos de qualquer PA")
print("=-="*30)
#definidno o termo e a razao da PA
termo=int(input("Insira o primeiro termo da PA: "))
razao=int(input("Digite a razão desta PA: "))
dez_primeiros=[]
# definir a range da PA para apenas 10 numeros
for i in range(1,11):
 #progressão da PA no laço for
 termo+=razao
 #armazenamento da progressão da PA na lista "dez_primeiros"
 dez_primeiros.append(termo)
print(f"os dez primeiros numeros desta PA são: {dez_primeiros}")

# OU

print("=-="*30)
print("                Os 10 primeiros termos de qualquer PA")
print("=-="*30)
#definidno o termo e a razao da PA
termo=int(input("Insira o primeiro termo da PA: "))
razao=int(input("Digite a razão desta PA: "))
dez_primeiros=[]

# definir a range da PA, sendo o numero inicial aquele digitado pelo usuário, enquanto que o numero final será a repetição do termo mais a razão 10 vezes.
# o ultimo numero da range é a razão da Pa escolhida pelo usuario
for i in range(termo,(termo+razao*10),razao):
 dez_primeiros.append(i)
print(f"os dez primeiros numeros desta PA são: {dez_primeiros}")

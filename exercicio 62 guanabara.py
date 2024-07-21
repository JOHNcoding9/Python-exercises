# melhore o exercicio anterior, perguntando ao usuário se ele quer continuar a mostrar mais termos da PA (o programa se encerra quando ele digitar 0 termos)
print("=-="*30)
print("                Os 10 primeiros termos de qualquer PA")
print("=-="*30)
#definidno o termo e a razao da PA
termo=int(input("Insira o primeiro termo da PA: "))
razao=int(input("Digite a razão desta PA: "))
contador=0
# enquanto o contador for menor que 10
while contador<10:
    print(f"{termo} -> ",end=" ")
    termo+=razao
    contador+=1
print("FIM")
while True:
 escolha=int(input("Deseja ver quantos termos a mais? "))
 if escolha==0:
  print(f"progressão finalizada com {contador} termos mostrados")
  break
 # enquanto a escolha não for igual a zero
 while escolha!=0:
    print(f"{termo} -> ",end=" ")
    termo+=razao
    escolha-=1
    contador+=1
 print("FIM")



# melhore o exercicio anterior, perguntando ao usuário se ele quer continuar a mostrar mais termos da PA (o programa se encerra quando ele digitar 0 termos)
# agora usando o laço FOR
print("=-="*30)
print("                Os 10 primeiros termos de qualquer PA")
print("=-="*30)
#definidno o termo e a razao da PA
termo=int(input("Insira o primeiro termo da PA: "))
razao=int(input("Digite a razão desta PA: "))
contador=0
for i in range(termo,(termo+razao*10),razao):
 print(f"{i} -> ",end=" ")
 contador+=1
print("FIM")
while True:
 escolha=int(input("Deseja ver quantos termos a mais? "))
 if escolha==0:
  print(f" progressão finalizada com {contador} termos mostrados")
  break
 while escolha!=0:
  print(f"{i} -> ",end=" ")
  i+=razao
  escolha-=1
  contador+=1
 print("FIM")
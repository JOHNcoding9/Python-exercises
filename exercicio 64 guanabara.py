# crie um programa que leia varios numeros inteiros , o programa só vai parar quando o usuario digitar 999 ( mostre quantos numeros foram digitados e qual é a soma deles)
# o Flag não deve ser considerado na soma
cont=0
numeros=[]
while True:
 num=int(input("Digite qualquer numero inteiro (digite 999 para sair): "))
 if num==999:
  break
 numeros.append(num)
 cont+=1
print(f"Você digitou {cont} numeros inteiros e a soma de todos deu:  {sum(numeros)}")
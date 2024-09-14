# leia varios numeros inteiros pelo tecaldo, pare quando o valor for 999, exiba a soma desconsiderando o flag
cont=0
soma=0
while True:
    num=int(input("Digite um valor (999 para sair): "))
    if num==999:
        break
    cont+=1
    soma+=num
print(f"Digitou {cont} numeros e sau soma deu: {soma}")
#faça um programa que leia de 0 a 9999 e mostre na tela cada uma de suas casas decimais

numero=int(input("digite um numero positivio entre 0 e 9999:  "))
while (numero<0) or (numero>9999): # se o primeiro numero digitado pelo usuario não respeitar o intervalo de numeros propostos, ele terá que digitar novamente
    numero=int(input("digite um número entre 0 e 9999: "))
unidade=numero//1%10 #é realizada uma divisão inteira  com o numero escohido e em seguida  uma divisão por 10, porém apenas nos importará  o resto desta ultima divisão ( a qual é a respectiva casa decimal)
dezena=numero//10%10
centena=numero//100%10
milhar=numero//1000%10
print("unidades: ",unidade)
print("dezenas: ", dezena)
print("centenas",centena)
print("milhar", milhar)

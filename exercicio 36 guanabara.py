#escreva um programa para aprovaar um empréstimo bancário para comprar uma casa. Pergunte Valor da casa, salário do comprador e em quantos anos ele irá pagar
#a prestação mensal não pode exceder 30% do salário (será negado)
valor_casa=float(input("Digite o valor da casa a ser comprada: "))
salario=float(input("Digite seu salário mensal: "))
anos=int(input("em quantos anos deseja pagar: "))
prestacao=valor_casa/(anos*12)
if prestacao>salario*0.30:
    print(f"Compra negada: valor de 30% do salario {salario*0.30}, valor da prestacao: {prestacao:,.2f}")
else:
    print(f"Compra aprovada, a prestacao será de R$ {prestacao:,.2f} em um peródo de {anos} anos. (30% do salario, {salario*0.30})")
#escreve um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento para salarios superiores a 1250 calcule aumento de 10%
#para inferioes ou iguais o aumento é de 15%
salario=float(input("digite seu salário na empresa: "))
if salario>1250:
    aumento=salario*1.1
else:
   aumento=salario*1.15
print(f"seu aumento salarial irá para : {aumento:,.2f}")
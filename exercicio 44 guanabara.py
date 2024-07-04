#elabore um script que calcule o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento
print("-=-"*50)
print(" Loja Telaskavara ")
preco=float(input("Preço das compras R$: "))
print("FORMAS DE PAGAMENTO")
print("""[1] à vista em dinheiro/cheque
[2] à vista cartão
[3] x2 no cartão
[4] x3 ou mais no cartão """)
cod={1:("à vista em dinheiro/cheque",preco-preco*0.1),
     2:("à vista cartão",preco-preco*0.05),
     3:("x2 cartão",preco/2),
     4:("x3 ou mais no cartão",preco+preco*0.2)}
while True:
 opcao=int(input("qual a sua opção? "))
 if 1<=opcao<=4:
    break
if opcao==4:
    parcelas=int(input("Quantas parecals seriam? "))
    print(f" você escolheu {cod[opcao][0]}, sua compra original de {preco} ao final, será parcelada em R$ {cod[opcao][1]/parcelas:,.2f} COM JUROS")
elif opcao==3:
    print(f" você escolheu {cod[opcao][0]}, sua compra original de {preco} ao final, será parcelada em R$ {cod[opcao][1]/2} SEM JUROS")
else:
   print(f" você escolheu {cod[opcao][0]}, sua compra original de {preco} ao final, valerá R$ {cod[opcao][1]} ")
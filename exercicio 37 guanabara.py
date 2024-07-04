#escreva um programa que leia um número inteiro qualquer  e peça ao usuário qual será a base de conversão
try:
 numero=int(input("Digite um numero qualquer: "))
 print("><"*40)
 print("""Escolha qual será a conversão desejada:
 Digite 1 para converter de decimal para Octal
 Digite 2 para converter de decimal para Hexadecimal
 Digite 3 para converter de decimal para Binário""")
 print("><"*40)
 conversoes={1: ("Octal",oct(numero)),
            2:("Hexadecimal",hex(numero)),
            3:("Binário",bin(numero))}
 digito=int(input("Digite  aqui: "))
 print(f" esse numero em {conversoes[digito][0]} fica desta forma: {conversoes[digito][1]}")
except:
 print("algo deu errado, certifique-se de preencher os campos corretamente")
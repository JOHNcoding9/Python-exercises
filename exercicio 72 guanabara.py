#  seu programa deverá ler um numero pelo teclado  entre 0 a 20 e escrever ele por extenso 
numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", 
    "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", 
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    try:
        numero_int = int(input("Digite um numero de 0 a 20: "))
        if 0<=numero_int<=20:
         print(f"Você digitou o numero {numeros_por_extenso[numero_int]}")
         break
        else:
           print("numero inválido")
    except (ValueError) :
     print("valor inválido")
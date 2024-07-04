#leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
ano=int(input("informe seu ano de nascimento: "))
if 2024-ano>26:
    print("você pertence a categoria MASTER")
elif 0<(2024-ano)<=9:
    print("você pertence a categoria Mirim")
elif 2024-ano<=14:
    print("você pertence a categoria Infantil")
elif 2024-ano<=19:
    print("você pertence a categoria Junior")
else:
    print("você pertence a categoria Sênior")
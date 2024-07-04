#faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se ele ainda vai se alistar ao serviço militarm, se é hora de se alistar ou se já passou da hora de se alistar
nascimento=int(input("Digite o seu ano de nascimento: "))
if 2024-nascimento>18:
    print(f"quem nasceu em {nascimento}, completa {2024-nascimento} anos em 2024 .Você ja passou da hora de se alistar, PROCURE FAZER ISSO O MAIS RÁPIDO POSSÍVEL")
    print(f"você deveria ter se alistado fazem {(2024-nascimento)-18} anos")
    print(f"no ano de {nascimento+18}")
elif 2024-nascimento==18:
    print(f"quem nasceu em {nascimento}, completa {2024-nascimento} anos em 2024 .Você está na hora certa de se alistar")
else:
    print(f"quem nasceu em {nascimento}, completa {2024-nascimento} anos em 2024 .Você ainda se alistará")
    print(f"terá de se alistar daqui {18-(2024-nascimento)} anos") 
    print(f"Seu alistamento será em {nascimento+18} ") 
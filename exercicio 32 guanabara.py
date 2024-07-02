#define se um ano é ou não bissexto (divisível por 4 e não divisivel por 100 ou divisivel por 400)
ano=int(input("digite um ano qualquer: "))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("ano bissexto")
else:
    print("ano normal")
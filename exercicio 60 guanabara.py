# faça um programa que leia um numero qualquer e leia o seu fatorial
numero=int(input("Digite qualquer numero inteiro: "))
fatorial_resultado=1
print(f"Calculando {numero}!")
for fat in range(1,numero+1):
    fatorial_resultado*=fat
    if fat < numero:
        print(f"{fat} X ", end="")
    else:
        print(f"{fat} = {fatorial_resultado}")
# crie um programa que leia idade e sexo de várias pessoas. exiba
# quantas pessoas têm mais de 18 anos
# quantos homens foram foram cadastrados
# quantas mulheres têm menos de 20 anos
mais_18=0
quant_homens=0
mulher_menos_20=0
while True:
    print("="*40)
    idade=int(input("Digite sua idade: "))
    if idade>18:
        mais_18+=1
    sexo=str(input("sexo [F/M] ")).strip().upper()
    print("="*40)
    if sexo=="M":
        quant_homens+=1
    if sexo=="F" and idade<20:
        mulher_menos_20+=1
    continuar=str(input("Deseja continuar? [s/n] ")).strip().upper()
    print("="*40)
    if continuar=="N":
        break
print(f"Há {mais_18} pessoas com mais de 18 anos, Há {quant_homens} homens e {mulher_menos_20} mulheres com menos de 20 anos")
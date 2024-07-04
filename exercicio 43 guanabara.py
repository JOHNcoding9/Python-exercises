#desenvolva um programa que leia a altura e o peso de uma pessoa e calcule o seu imc e msotre os seus status
altura=float(input("Digite sua altura (m): "))
peso=float(input("Digite seu peso (Kg): "))
Imc=peso/(altura**2)
if Imc>40:
    print("Obesidade Mórbida",Imc)
elif Imc<18.5:
    print("Abaixo do peso",Imc)
elif 18.5<Imc<=25:
    print("Peso ideal",Imc)
elif 25<Imc<=30:
    print("Sobrepeso",Imc)
else:
    print("Obesidade",Imc)
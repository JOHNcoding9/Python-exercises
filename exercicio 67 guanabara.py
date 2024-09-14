# faça um programa que mostre a tabuada de varios numeros , o programa qserá interrompido se o valor for negativo
tabuada_resultado=0
while True:
    tabuada=int(input("Digite a tabuada desejada: "))
    if tabuada<0:
        break
    for i in range(1,11):
        tabuada_resultado=tabuada * i
        print(f"{tabuada} X {i} = {tabuada_resultado}")
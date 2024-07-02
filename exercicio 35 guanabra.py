#desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
print("-=-"*20)
print(" Condição de existência de um triângulo ")
print("-=-"*20)
reta1=float(input("digite a medida desta reta: "))
reta2=float(input("digite a medida desta reta: "))
reta3=float(input("digite a medida desta reta: "))
if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print("triângulo viável")
else:
     print("não é possível formar um triãngulo com essas mdedidas")
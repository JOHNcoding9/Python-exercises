#acrescente ao exercicio 35 a opçao de mostrar o tipo de triângulo que será formado
print("-=-"*20)
print(" Condição de existência de um triângulo ")
print("-=-"*20)
reta1=float(input("digite a medida desta reta: "))
reta2=float(input("digite a medida desta reta: "))
reta3=float(input("digite a medida desta reta: "))
if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print("triângulo viável")
    if reta1==reta2 and reta2==reta3:
     print("o triângulo formado será equilátero")
    elif reta1==reta2 or reta2==reta3 or reta1==reta3:
     print("o triângulo formado será Isóceles ")
    else:
     print("o triângulo formado será Escaleno")

else:
   print("não é possível formar um triângulo com essas dedidas")
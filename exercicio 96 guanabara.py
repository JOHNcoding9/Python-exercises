# faça um programa que tenha uma função chamada area() que receba as dimensões de uma area retangular e mostre a area do terreno

print("--Controle de terrenos--")

largura = float(input("Largura terreno: "))
comprimento = float(input("comprimento terreno: "))

def area(largura,comprimento):
    return largura * comprimento

print(f"a area do terreno de comprimento {comprimento} e largura {largura} é de {area(largura,comprimento)} m²")


# faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro  e mostre uma mensagem com vvalor adptável

def escreva(texto):
    tamanho = len(texto)
    print("~" * tamanho)
    print(  texto)
    print("~" * tamanho)

escreva("olá mundo, bom dia a todos e muito obrigado")
escreva('oi')
escreva('Adeus, muito obrigado')
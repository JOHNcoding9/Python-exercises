# crie um programa que leia uma frase qualquer e diga se ela é palíndromo (desconsiderando os espaços)

#armazenando a palavra do usuário e desconsiderando os espaços com .strip()
frase=str(input("Digite uma frase: ")).strip().upper()
palavras=frase.split()
juntar_novamente="".join(palavras)
if  juntar_novamente[::-1]==juntar_novamente:
    print("A frase é um palíndromo")
else:
    print("essa frase não é um palíndromo")
# crie um programa que tenha uma tupla com varias palavras . mostrar  para cada palavra quais são suas vogais

print("=" * 20 , "Detector de Vogais","=" * 20 )

palavras = ("Python","Aprender","Guanabara","Curso","Engenharia","Software","VALORANT","quadro")
vogais = "aeiouAEIOU"
def mostrar_vogais():
    for cada_palavra in palavras: # Percorre diretamente cada palavra na tupla
        print(f"Na palavra {cada_palavra} temos: ", end='')
        for cada_letra in cada_palavra: # Verifica se a letra é uma vogal
            if cada_letra in "aeiouAEIOU":
             print(cada_letra, end=' ')
        print() # Adiciona uma quebra de linha após a impressão de todas as vogais
mostrar_vogais()
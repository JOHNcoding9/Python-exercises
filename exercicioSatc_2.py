# Crie uma função que recebe uma string e retorna um dicionário com a contagem de cada caractere presente na string.

# {key : valor}
# {"s" : quantidade_apareceu}
# código que eu fiz 
def letras_frase(frase):
    dicionario = {}
    for letra in frase:
        dicionario[letra] = {frase.count(letra)}
    return dicionario
frase = "ABACAXIXIXI"
print(f"contagem de cada letra: {letras_frase(frase)}")

# sugestão do amigo :  O problema com o código atual é que frase.count(letra) é chamado dentro do loop, o que resulta em uma complexidade de tempo O(n^2) para strings grandes, pois count() percorre toda a string para cada letra. A abordagem mais eficiente é usar um único loop para contar as letras, acumulando os resultados em um dicionário

def letras_frase(frase):
    dicionario = {}
    for letra in frase:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1
    return dicionario

# Exemplo de uso:
frase = "ABACAXIXIXI"
print(f"contagem de cada letra: {letras_frase(frase)}")

# O código 1 tem uma complexidade de tempo O(n^2) no pior caso. O método frase.count(letra) percorre toda a string para cada caractere, resultando em um comportamento quadrático porque é chamado dentro do loop para cada caractere.

#  O código 2 tem uma complexidade de tempo O(n), onde n é o número de caracteres na string frase. Cada caractere é processado uma vez, e o acesso e a atualização do dicionário são operações rápidas e eficientes.

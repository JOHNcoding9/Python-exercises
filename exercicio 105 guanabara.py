def notas(*notas,sit=False):

    """ Calcula o maior, menor, quantidade e média das notas. Opcionalmente, avalia a situação com base na média. Parâmetros: notas (list): Lista de notas (float ou int). sit (bool): Se True, retorna a situação com base na média. Retorna: tuple: Contendo maior nota, menor nota, quantidade de notas, média das notas e situação (opcional). OS dados são devolvidos em um dicionário """

    dicionario = {}
    soma = 0
    dicionario['quantidade'] = len(notas)

    for i in range(dicionario['quantidade']):
        soma += notas[i]

        if i == 0:
            dicionario['maior'] = notas[i]
            dicionario['menor'] = notas[i]
        else:
         if  notas[i] > dicionario['maior']:
           dicionario['maior'] = notas[i]
         if  notas[i] < dicionario['menor']:
            dicionario['menor'] = notas[i]

    dicionario['media'] = soma / dicionario['quantidade']

    if sit:
        if dicionario['media'] >= 7:
         sit = 'EXCELENTE' if dicionario['media'] > 7 else 'REGULAR'
        else:
            sit =  "TAIS FUDIDO"
     
        dicionario['sit'] = sit

    return dicionario

reusltado = notas(8.2,7,8, sit =True)
print(reusltado)
reusltado = notas(4,4,10,3,5,6)
print(reusltado)

help(notas)
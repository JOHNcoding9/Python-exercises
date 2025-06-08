# crie um programa que tenha uma função fatorial() que receba dois parâmetros: o numero e outro chamado show que será um valor lógico(opcional) indicando se será mostrado ou não o processo do cálculo


def fatorial(valor,show=False):
    """
      --> Calcular o fatorial de um numero

         :parâmemetro valor: O numero a ser calculado
         :parâmetro show: Opcionalmente mostrar a conta(True) ou não(False)
         :parâmetro return: Resultado do fatorial de valor


    """

    fatorial = 1
    valor_original = valor

    while valor > 1:
     fatorial *= valor
     valor -= 1

    if show:
        for i in range(valor_original, 0, -1): 
         print(i, "x " if i > 1 else "= ", end="")

    return fatorial


help(fatorial)
   

print(fatorial(5, show=True))
print('=========================')
print(fatorial(5))
    






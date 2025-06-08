
def ficha(jogador,gols):

    if nome == '':
        jogador="<desconhecido>"
    if gols == '' or not gols.isdigit(): # o método retorna True apenas se o valor for uma string de números inteiros
        gols = 0

    print(f"O jogador {jogador} fez {gols} gol(s)")

nome = str(input("Insira o nome do jogador: ")).strip()
gols = (input("Insira o numero de gols realizados pelo jogador: ")).strip()

ficha(nome,gols)
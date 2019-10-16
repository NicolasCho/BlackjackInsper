import random


def saque(baralho):
    random.shuffle(baralho)
    carta = baralho.pop()
    return carta


def soma(mao):
    a = False
    listasemas = []
    i = 0
    while i < len(mao):
        if mao[i] != 1:
            listasemas.append(mao[i])
            i += 1
        elif mao[i] == 1 and '1' not in listasemas:
            a = True
            for e in mao[i + 1:]:
                if mao[i] == e:
                    listasemas.append(e)
            i += 1
    somatoriosemas = 0
    for g in listasemas:
        somatoriosemas = somatoriosemas + g
    if somatoriosemas <= 10 and a == True:
        soma = somatoriosemas + 11
    elif somatoriosemas > 10 and a == True:
        soma = somatoriosemas + 1
    else:
        soma = somatoriosemas
    return soma


def maior_soma(lista_jogadores, dic_mao):
    somatorias_jogadores = []
    for e in lista_jogadores:
        somatorias_jogadores.append(soma(dic_mao[e]))
    return max(somatorias_jogadores)


b = True
while b is True:
    print('Bem vindos ao Black Jack! Vamos começar!')
    n = int(input('Quantas pessoas vao jogar? '))
    lista_jogadores = []
    mao_dealer = []
    dic_mao = {}
    dic_carteira = {}
    dic_apostas = {}

    numero_de_baralhos = int(input('Quantos baralhos? '))
    baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4 * numero_de_baralhos
    print('O seguinte baralho sera usado: {}'.format(baralho))

import random


def contador(mao):
    a = False
    listasemas = []
    i = 0
    while i < len(mao):
        if mao[i][1] != 1:
            listasemas.append(mao[i][1])
            i += 1
        elif mao[i][1] == 1 and '1' not in listasemas:
            a = True
            for e in mao[i + 1:]:
                if mao[i][1] == e[1]:
                    listasemas.append(e[1])
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


quantidade_de_jogadores = int(input('Insira a quantidade de jogadores: '))
lista_jogadores = []
j = 0

while j < quantidade_de_jogadores:
    x = input('Jogador {}, insira seu nick: '.format(j + 1))
    lista_jogadores.append(x)
    j += 1

valores_carteiras = []
z = 0
while z < len(lista_jogadores):
    valor = float(input("Insira o valor da sua carteira {}: ".format(lista_jogadores[z])))
    valores_carteiras.append(valor)
    z += 1

saldo = []

for carteira in valores_carteiras:
    while carteira > 0:
        v = False
        n = False
        x = True
        y = True

        c = 0
        lista_apostas = []
        while c < len(lista_jogadores):
            aposta = float(input('Insira o valor da sua aposta, {}: '.format(lista_jogadores[c])))
            while aposta > carteira:
                print('Você não tem esse tanto de dinheiro! Faça uma aposta possível')
                aposta = float(input('Insira o valor da sua aposta, {}: '.format(lista_jogadores[c])))
            lista_apostas.append(aposta)
            saldo.append(valores_carteiras[c] - lista_apostas[c])
            c += 1

        cartas = {
            'Ás de  paus (♣)': 1,
            '2 de paus (♣)': 2,
            '3 de paus (♣)': 3,
            '4 de paus (♣)': 4,
            '5 de paus (♣)': 5,
            '6 de paus (♣)': 6,
            '7 de paus (♣)': 7,
            '8 de paus (♣)': 8,
            '9 de paus (♣)': 9,
            '10 de paus (♣)': 10,
            'Q de paus (♣)': 10,
            'J de paus (♣)': 10,
            'K de paus (♣)': 10,

            'Ás de copas (♥)': 1,
            '2 de copas (♥)': 2,
            '3 de copas (♥)': 3,
            '4 de copas (♥)': 4,
            '5 de copas (♥)': 5,
            '6 de copas (♥)': 6,
            '7 de copas (♥)': 7,
            '8 de copas (♥)': 8,
            '9 de copas (♥)': 9,
            '10 de copas (♥)': 10,
            'Q de copas (♥)': 10,
            'J de copas (♥)': 10,
            'K de copas (♥)': 10,

            'Ás de espadas (♠))': 1,
            '2 de espadas (♠)': 2,
            '3 de espadas (♠)': 3,
            '4 de espadas (♠)': 4,
            '5 de espadas (♠)': 5,
            '6 de espadas (♠)': 6,
            '7 de espadas (♠)': 7,
            '8 de espadas (♠)': 8,
            '9 de espadas (♠)': 9,
            '10 de espadas (♠)': 10,
            'Q de espadas (♠)': 10,
            'J de espadas (♠)': 10,
            'K de espadas (♠)': 10,

            'Ás de ouros (♦)': 1,
            '2 de ouros (♦)': 2,
            '3 de ouros (♦)': 3,
            '4 de ouros (♦)': 4,
            '5 de ouros (♦)': 5,
            '6 de ouros (♦)': 6,
            '7 de ouros (♦)': 7,
            '8 de ouros (♦)': 8,
            '9 de ouros (♦)': 9,
            '10 de ouros (♦)': 10,
            'Q de ouros (♦)': 10,
            'J de ouros (♦)': 10,
            'K de ouros (♦)': 10
        }
        soma = 0
        mao_dealer = []
        valores_soma = []
        mao = []

        for b in range(len(lista_jogadores)):
            PRIMEIRA_CARTA = random.choice(list(cartas.items()))
            del (cartas[PRIMEIRA_CARTA[0]])
            SEGUNDA_CARTA = random.choice(list(cartas.items()))
            del (cartas[SEGUNDA_CARTA[0]])
            CARTA_DEALER_CIMA = random.choice(list(cartas.items()))
            del (cartas[CARTA_DEALER_CIMA[0]])
            mao.append(PRIMEIRA_CARTA)
            mao.append(SEGUNDA_CARTA)
            print('{}, você retirou {} e {}. Sua soma é {}.'.format(lista_jogadores[b], PRIMEIRA_CARTA[0],
                                                                    SEGUNDA_CARTA[0], contador(mao)))
            valores_soma.append(contador(mao))

        CARTA_DEALER_BAIXO = random.choice(list(cartas.items()))
        del (cartas[CARTA_DEALER_BAIXO[0]])
        CARTA_DEALER_CIMA = random.choice(list(cartas.items()))
        del (cartas[CARTA_DEALER_CIMA[0]])
        mao_dealer.append(CARTA_DEALER_CIMA)
        mao_dealer.append(CARTA_DEALER_BAIXO)
        print('A carta virada para cima do dealer é {}'.format(CARTA_DEALER_CIMA[0]))

        lista_verifica_saida = []
        for t1 in range(len(lista_jogadores)):
            if valores_soma[t1] == 21:
                print('Blackjack! {}, você fez 21!'.format(lista_jogadores[t1]))
                saldo[t1] = saldo[t1] + 1.5 * lista_apostas[c]
                print('{}, seu novo saldo é de R${}.'.format(lista_jogadores[t1], saldo[t1]))
                lista_verifica_saida.append('hold')
            else:
                lista_verifica_saida.append('hit')

        for t2 in range(len(lista_jogadores)):
            if lista_verifica_saida[t2] == 'hold':
                print('{}, você não está mais no jogo.'.format(lista_jogadores[t2]))
                valores_soma[t2] = valores_soma[t2]

            else:
                print('Vez de {}'.format(lista_jogadores[t2]))
                mais_carta = str(
                    input('{}, digite [hit] para mais cartas ou [hold] para fechar a mão:'.format(lista_jogadores[t2])))
                lista_verifica_saida[t2] = mais_carta

                while mais_carta == 'hit':
                    v = True
                    CARTA_EXTRA = random.choice(list(cartas.items()))
                    del (cartas[CARTA_EXTRA[0]])
                    mao.clear()
                    valores_soma[t2] = valores_soma[t2] + CARTA_EXTRA
                    mao.append(valores_soma[t2])
                    print('Você retirou {}. Sua mão é {}. A soma é {}.'.format(CARTA_EXTRA[0], mao, contador(mao)))

                    if valores_soma[t2] > 21:
                        print('{}, você estorou!'.format(lista_jogadores[t2]))
                        saldo[t2] = saldo[t2]
                        print('{}, seu novo saldo é de R${}.'.format(lista_jogadores[t2], carteira))
                        lista_verifica_saida[t2] = 'hold'

                    elif valores_soma[t2] == 21:
                        print('{}, você fez 21!'.format(lista_jogadores[t2]))
                        saldo[t2] = saldo[t2] + 1.5 * lista_apostas[t2]
                        print('{}, seu novo saldo é de R${}.'.format(lista_jogadores[t2], saldo[t2]))
                        lista_verifica_saida[t2] = 'hold'

                    else:
                        mais_carta = str(input('Digite [hit] para mais cartas ou [hold] para fechar a mão:'))
                        lista_verifica_saida[t2] = mais_carta

                    if lista_verifica_saida[0:] == 'hold':
                        menor = valores_soma[0]
                        for elemento1 in valores_soma:
                            if elemento1 < menor:
                                menor = elemento1

                        n = True
                        print('A carta virada para baixo do dealer é {}.A soma do dealer é {}'.format(
                            CARTA_DEALER_BAIXO[0],
                            contador(mao_dealer)))
                        while contador(mao_dealer) < 17:
                            CARTA_DEALER_EXTRA = random.choice(list(cartas.items()))
                            del (cartas[CARTA_DEALER_EXTRA[0]])
                            mao_dealer.append(CARTA_DEALER_EXTRA)
                        while contador(mao_dealer) < menor:
                            CARTA_DEALER_EXTRA2 = random.choice(list(cartas.items()))
                            del (cartas[CARTA_DEALER_EXTRA2[0]])
                            mao_dealer.append(CARTA_DEALER_EXTRA2)

                        print('O dealer puxou as cartas. A nova mão do dealer é {}. A soma do dealer é {}'.format(
                            mao_dealer,
                            contador(
                                mao_dealer)))

                        # mostar os resultados

                        for u in range(len(lista_jogadores)):
                            if valores_soma[u] < 21:
                                if contador(mao_dealer) > 21:
                                    print('{}, você GANHOU!')
                                    saldo[u] = saldo[u] + 1.5 * lista_apostas[u]
                                    print('{}, seu novo saldo é de R${}.'.format(lista_jogadores[u], saldo[u]))
                                elif contador(mao_dealer) > contador(mao):
                                    print('Você PERDEU!')
                                    saldo[t2] = saldo[t2]
                                    print('Seu novo saldo é de R${}.'.format(saldo[u]))
                                elif contador(mao_dealer) == contador(mao):
                                    print('EMPATE!')
                                    saldo[t2] = saldo[t2] + lista_jogadores[u]
                                    print('Seu novo saldo é de R${}.'.format(saldo[u]))

# plotar tabela com valores --> Resultados:
# Nome / Carteira / Aposta/ Soma das Cartas / Saldo
# Perguntar quem quer jogar novamente --> fazer lista de saída

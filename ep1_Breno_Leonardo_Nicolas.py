    i = 0
    while i < n:
        nome = input('Nome do jogador: ')
        carteira = int(input('{}, quanto você possui na carteira? '.format(nome)))
        lista_jogadores.append(nome)
        dic_carteira[lista_jogadores[i]] = carteira
        i += 1

    aposta = 0
    e = 0
    while e < len(lista_jogadores):
        aposta = float(input('{}, quanto você quer apostar? '.format(lista_jogadores[e])))
        while aposta > dic_carteira[lista_jogadores[e]] or aposta <= 0:
            aposta = float(input('Aposta impossível! Digite um valor possível: '))
        dic_apostas[lista_jogadores[e]] = aposta
        e += 1

    i = 0
    while i < len(lista_jogadores):
        carta1 = saque(baralho)
        carta2 = saque(baralho)
        lista = [carta1, carta2]
        dic_mao[lista_jogadores[i]] = lista

        if soma(dic_mao[lista_jogadores[i]]) == 21:
            dic_carteira[lista_jogadores[i]] = dic_carteira[lista_jogadores[i]] + dic_apostas[lista_jogadores[i]] * 1.5
            del (lista_jogadores[i])
            i -= 1
        i += 1

    print('As carts foram sortadas. As mãos dos jogadores são: {}.'.format(dic_mao))

    baixo_dealer = saque(baralho)
    cima_dealer = saque(baralho)
    mao_dealer.append(baixo_dealer)
    mao_dealer.append(cima_dealer)
    print('Carta de cima do dealer: {}'.format(cima_dealer))

    i = 0
    while i < len(lista_jogadores):
        continuidade = str(
            input('{}, digite [1] para pedir mais cartas ou [2] para parar: '.format(lista_jogadores[i])))

        while continuidade == '1':
            carta_extra = saque(baralho)
            dic_mao[lista_jogadores[i]].append(carta_extra)
            print('{}, sua nova mão: {}'.format(lista_jogadores[i], dic_mao[lista_jogadores[i]]))

            if soma(dic_mao[lista_jogadores[i]]) > 21:
                print('{}, você ESTOUROU!'.format(lista_jogadores[i]))
                dic_carteira[lista_jogadores[i]] = dic_carteira[lista_jogadores[i]] - dic_apostas[lista_jogadores[i]]
                del (lista_jogadores[i])
                i -= 1
                break
            elif soma(dic_mao[lista_jogadores[i]]) == 21:
                print('BLACKJACK!.{}, você fez 21'.format(lista_jogadores[i]))
                dic_carteira[lista_jogadores[i]] = dic_carteira[
                                                       lista_jogadores[i]] + dic_apostas[lista_jogadores[i]] * 1.5
                del (lista_jogadores[i])
                i -= 1
                break
            else:
                continuidade = str(
                    input('{}, digite [1] para pedir mais cartas ou [2] para parar: '.format(lista_jogadores[i])))
        i += 1

    if len(lista_jogadores) > 0:
        print('Mão do dealer: {}'.format(mao_dealer))
        while soma(mao_dealer) < 17:
            carta_extra_dealer = saque(baralho)
            mao_dealer.append(carta_extra_dealer)
        while soma(mao_dealer) < maior_soma(lista_jogadores, dic_mao):
            carta_extra_dealer2 = saque(baralho)
            mao_dealer.append(carta_extra_dealer2)

        print(
            'Após puxar cartas, a nova mão do dealer: {}. A soma do dealer foi {}'.format(mao_dealer, soma(mao_dealer)))

        for e in lista_jogadores:
            if soma(mao_dealer) > 21:
                print('{}, você GANHOU!'.format(e))
                dic_carteira[e] = dic_carteira[e] + dic_apostas[e] * 1.5
            elif soma(dic_mao[e]) < soma(mao_dealer) and soma(mao_dealer) <= 21:
                print('{}, você PERDEU!'.format(e))
                dic_carteira[e] = dic_carteira[e] - dic_apostas[e]
            elif soma(dic_mao[e]) == soma(mao_dealer):
                print('{}, você EMPATOU!'.format(e))

    print('\n')
    print('RESULTADOS')
    print('MÃOS:{}'.format(dic_mao))
    print('CARTEIRAS:{}'.format(dic_carteira))
    print('\n')

import random

jogador = input('Insira seu nome: ')
print('Olá {}. Vamos começar!'.format(jogador))

valor_carteira = float(input("Insira o valor da sua carteira: "))
aposta = float(input('Insira o valor da sua aposta: '))
saldo = valor_carteira - aposta


def baralho():
    Cartas = {
        'Ás de  paus (♣)': 11,
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

        'Ás de copas (♥)': 11,
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

        'Ás de espadas (♠))': 11,
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

        'Ás de ouros (♦)': 11,
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

    carta_pegada = random.choice(list(Cartas.items()))
    return carta_pegada


while saldo >= 0:
    carta_retirada_1 = baralho()
    carta_retirada_2 = baralho()
    soma = carta_retirada_1[1] + carta_retirada_2[1]
    print('Você retirou {} e {}. Sua soma é {}.'.format(carta_retirada_1[0], carta_retirada_2[0], soma))

    carta1_croupier = baralho()
    carta2_croupier = baralho()
    soma_croupier = carta1_croupier[1] + carta2_croupier[1]

    if soma == 21:
        print('Black Jack!')
        saldo = saldo + aposta * 1.5
        print('Seu novo saldo é de {}'.format(saldo))
    else:
        varifica_se_retira = str(input('Deseja retirar mais uma carta? '))
        while varifica_se_retira == 'sim':
            nova_carta_retirada = baralho()
            print('Sua nova carta: {}'.format(nova_carta_retirada[0]))
            soma = soma + nova_carta_retirada[1]
            print('Sua nova soma é de {}'.format(soma))
            nova_carta_croupier = baralho()
            soma_croupier = soma_croupier + nova_carta_croupier[1]

            if soma > 21:
                print('Você estourou! Sua soma foi de {}'.format(soma))
                saldo = saldo
                print('Seu novo saldo é de {}'.format(saldo))
                break

            elif soma == 21:
                print('Black Jack!')
                saldo = saldo + aposta * 1.5
                print('Seu novo saldo é de {}'.format(saldo))
                break

            varifica_se_retira = str(input('Deseja retirar mais uma carta? '))

        else:
            if soma < 21 and soma_croupier > 21:
                print('Você Ganhou! Sua soma foi de {} e o Croupier estourou com {}. '.format(soma, soma_croupier))
                saldo = saldo + aposta * 1.5
                print('Seu novo saldo é de {}'.format(saldo))
                break

            elif 21 > soma > soma_croupier and soma > soma_croupier:
                print('Você Ganhou! Sua soma foi de {} e o Croupier estourou com {}. '.format(soma, soma_croupier))
                saldo = saldo + aposta * 1.5
                print('Seu novo saldo é de {}'.format(saldo))
                break

            elif 21 > soma and 21 > soma_croupier > soma:
                print('Você perdeu! Sua soma foi de {} de a do Croupier de {}'.format(soma, soma_croupier))
                saldo = saldo
                print('Seu novo saldo é de {}'.format(saldo))
                break
while saldo < 0:
    print('Você não possui dinheiro para fazer essa transação!')
    break

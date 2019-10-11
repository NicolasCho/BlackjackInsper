import random

def contador(mao):
    a=False
    listasemas=[]
    i=0
    while i<len(mao):
        if mao[i][1]!=1:
            listasemas.append(mao[i][1])
            i+=1
        elif mao[i][1]==1 and '1' not in listasemas:
            a=True
            for e in mao[i+1:]:
                if mao[i][1]==e[1]:
                    listasemas.append(e[1])
            i+=1
            
    somatoriosemas=0
    for g in listasemas:
        somatoriosemas=somatoriosemas+g
    if somatoriosemas<=10 and a==True:
        soma=somatoriosemas+11
    elif somatoriosemas>10 and a==True:
        soma=somatoriosemas+1
    else:
        soma=somatoriosemas
    return soma


            
        
        

jogador = input('Insira seu nome: ')
print('Olá {}. Vamos começar!'.format(jogador))
carteira = float(input("Insira o valor da sua carteira: "))

while carteira>0: 
    v=False
    n=False
    x=True
    y=True
    aposta = float(input('Insira o valor da sua aposta: '))
    while aposta>carteira:
        print('Você não tem esse tanto de dinheiro! Faça uma aposta possível')
        aposta = float(input('Insira o valor da sua aposta: '))
        
    soma=0
    mao=[]
    mao_dealer=[]
    
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
    
    PRIMEIRA_CARTA=random.choice(list(cartas.items())) 
    del(cartas[PRIMEIRA_CARTA[0]])
    SEGUNDA_CARTA=random.choice(list(cartas.items()))  
    del(cartas[SEGUNDA_CARTA[0]])
    CARTA_DEALER_CIMA=random.choice(list(cartas.items())) 
    del(cartas[CARTA_DEALER_CIMA[0]])
    CARTA_DEALER_BAIXO=random.choice(list(cartas.items())) 
    del(cartas[CARTA_DEALER_BAIXO[0]])
       
    
    mao.append(PRIMEIRA_CARTA)
    mao.append(SEGUNDA_CARTA)
    mao_dealer.append(CARTA_DEALER_CIMA)
    mao_dealer.append(CARTA_DEALER_BAIXO)
    print('Você retirou {} e {}. Sua soma é {}. A carta virada para cima do dealer é {}'.format(PRIMEIRA_CARTA[0], SEGUNDA_CARTA[0],contador(mao),CARTA_DEALER_CIMA[0]))
    
    if contador(mao)==21:
        print('Blackjack! Você fez 21!')
        carteira=carteira+1.5*aposta
        print('Seu novo saldo é de R${}.'.format(carteira))
        saida=str(input('Digite [sair] para parar de jogar e [continuar] para continuar jogando:'))
        if saida=='sair':
            break
        elif saida=='continuar':
            continue

    mais_carta=str(input('Digite [hit] para mais cartas ou [hold] para fechar a mão:'))
    
    while mais_carta=='hit':
        v=True
        CARTA_EXTRA=random.choice(list(cartas.items()))
        del(cartas[CARTA_EXTRA[0]])
        mao.append(CARTA_EXTRA)
        print('Você retirou {}. Sua mão é {}. A soma é {}.'.format(CARTA_EXTRA[0],mao,contador(mao)))
        
        if contador(mao)>21:
            print('Você estorou!')
            carteira=carteira-aposta
            print('Seu novo saldo é de R${}.'.format(carteira))
            saida=str(input('Digite [sair] para parar de jogar ou [continuar] para continuar jogando:')) 
            if saida=='sair':
                 x=False
                 break
            if saida=='continuar':
                 break
        elif contador(mao)==21:
             print('BLACKJACK! Você fez 21!')
             carteira=carteira+1.5*aposta
             print('Seu novo saldo é de R${}.'.format(carteira))
             saida=str(input('Digite [sair] para parar de jogar ou [continuar] para continuar jogando:'))
             if saida=='sair':
                 x=False
                 break
             if saida=='continuar':
                 break
        else:
            mais_carta=str(input('Digite [hit] para mais cartas ou [hold] para fechar a mão:'))       
    if x==False and v==True and mais_carta!='hold':
        break
    elif x==True and v==True and mais_carta!='hold':
        continue

    while mais_carta=='hold':
        n=True
        print('A carta virada para baixo do dealer é {}.A soma do dealer é {}'.format(CARTA_DEALER_BAIXO[0],contador(mao_dealer)))
        while contador(mao_dealer)<17:
            CARTA_DEALER_EXTRA=random.choice(list(cartas.items()))
            del(cartas[CARTA_DEALER_EXTRA[0]])
            mao_dealer.append(CARTA_DEALER_EXTRA)
        while contador(mao_dealer)<contador(mao):
            CARTA_DEALER_EXTRA2=random.choice(list(cartas.items()))
            del(cartas[CARTA_DEALER_EXTRA2[0]])
            mao_dealer.append(CARTA_DEALER_EXTRA2)
        
        print('O dealer puxou as cartas. A nova mão do dealer é {}. A soma do dealer é {}'.format(mao_dealer,contador(mao_dealer)))    
        if contador(mao_dealer)>21:
            print('Você GANHOU!')
            print('Seu novo saldo é de R${}.'.format(carteira))
            saida=str(input('Digite [sair] para parar de jogar ou [continuar] para continuar jogando:'))
            if saida=='sair':
                y=False
                break
            if saida=='continuar':
                break
        elif contador(mao_dealer)>contador(mao):
            print('Você PERDEU!')
            carteira=carteira-aposta
            print('Seu novo saldo é de R${}.'.format(carteira))
            saida=str(input('Digite [sair] para parar de jogar ou [continuar] para continuar jogando:')) 
            if saida=='sair':
                 y=False
                 break
            if saida=='continuar':
                 break 
        elif contador(mao_dealer)==contador(mao):
            print('EMPATE!')
            print('Seu novo saldo é de R${}.'.format(carteira))
            saida=str(input('Digite [sair] para parar de jogar ou [continuar] para continuar jogando:')) 
            if saida=='sair':
                 y=False
                 break
            if saida=='continuar':
                 break 
    if y==False and n==True:
        break
    elif y==True and n==True:
        continue

if carteira<=0:
    print('Acabou seu dinheiro!!')

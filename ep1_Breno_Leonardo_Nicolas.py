import random


def saque(baralho):
    random.shuffle(baralho)
    carta=baralho.pop()
    return carta

def soma(mao):
    a=False
    listasemas=[]
    i=0
    while i<len(mao):
        if mao[i]!=1:
            listasemas.append(mao[i])
            i+=1
        elif mao[i]==1 and '1' not in listasemas:
            a=True
            for e in mao[i+1:]:
                if mao[i]==e:
                    listasemas.append(e)
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

def maior_soma(lista_jogadores, dic_valores):
    somatorias_jogadores=[]
    for e in lista_jogadores:
        somatorias_jogadores.append(soma(dic_valores[e]))
    return max(somatorias_jogadores)

def valor(carta):
    a=carta[1]
    if a=='J' or a=='Q' or a=='K' :
        a=10  
    elif a=='As':
        a=1
    else:      
        a=int(carta[1])
    return a        

                #FEATURE 4: MULTIJOGADOR!
n=int(input('quantas pessoas vao jogar?'))

lista_jogadores_definitiva=[]
lista_carteira=[]
dic_carteira={}


i=0
while i<n:
    nome=input('nome do jogador:')
    carteira=int(input('{}, quanto possui?'.format(nome)))
    lista_jogadores_definitiva.append(nome)
    lista_carteira.append(carteira)
    dic_carteira[lista_jogadores_definitiva[i]]=lista_carteira[i]
    i+=1

            #FEATURE 5:MULTIPLOS BARALHOS!
numero_de_baralhos=int(input('Quantos baralhos?'))
numeros=['As','2','3','4','5','6','7','8','9','10','J','Q','K']*numero_de_baralhos
naipes=['Espadas ♠','Copas ♥','Paus ♣','Ouros ♦']*numero_de_baralhos
baralho=[[p + ' de ' + n,p] for n in naipes for p in numeros]
   

RESTAURAR=False
JOGAR=True
             
while JOGAR==True:
    lista_jogadores=lista_jogadores_definitiva
    dic_cartas={}
    dic_valores={}
    dic_apostas={}
    valor_dealer=[]
    cartas_dealer=[]
    
     #FEATURE LIVRE 1:RESTAURAR BARALHO OU MANTER
    if RESTAURAR == True:
        novo_baralho=int(input('Digite [1] para restaurar o baralho e [2] para manter:'))
        if novo_baralho=='1':
            numero_de_baralhos=int(input('Quantos baralhos?'))
            numeros=['As','2','3','4','5','6','7','8','9','10','J','Q','K']*numero_de_baralhos
            naipes=['Espadas ♠','Copas ♥','Paus ♣','Ouros ♦']*numero_de_baralhos
            baralho=[[p + ' de ' + n,p] for n in naipes for p in numeros]
     
        #FEATURES 1 E 2: LIMITE DE APOSTA E FIM DO JOGO
    e=0
    while e<len(lista_jogadores):   
        aposta=str(input('{}, quanto você quer apostar? Digite [fim] para sair do jogo:'.format(lista_jogadores[e])))
        if aposta=='fim':
            del(dic_carteira[lista_jogadores[e]])
            del(lista_carteira[e])
            del(lista_jogadores[e])
            del(lista_jogadores_definitiva[e])
        else:
            aposta=float(aposta)
            while aposta>lista_carteira[e] or aposta<=0:
                aposta=float(input('Aposta impossível! Digite um valor possível:'))
            dic_apostas[lista_jogadores[e]]=aposta
        e+=1
    
    if len(lista_jogadores)<1:
        break
    
    i=0
    while i<len(lista_jogadores):
        carta1=saque(baralho)
        carta2=saque(baralho)
        lista_valores=[valor(carta1),valor(carta2)]
        lista_cartas=[carta1[0],carta2[0]]
        dic_valores[lista_jogadores[i]]=lista_valores
        dic_cartas[lista_jogadores[i]]=lista_cartas
     
        if soma(dic_valores[lista_jogadores[i]])==21:
            print('BLACKJACK!.{}, você fez 21'.format(lista_jogadores[i]))
            dic_carteira[lista_jogadores[i]]=dic_carteira[lista_jogadores[i]]+ dic_apostas[lista_jogadores[i]]*1.5       
            del(lista_jogadores[i])
            del(lista_carteira[i])
            i-=1
        i+=1
    
    print('Suas mãos:{}.'.format(dic_cartas))

    #FEATURE LIVRE:CARTA VIRADA PARA CIMA DO DEALER 
    baixo_dealer=saque(baralho)
    cima_dealer=saque(baralho)
    valor_dealer.append(valor(baixo_dealer))
    valor_dealer.append(valor(cima_dealer))
    cartas_dealer.append(baixo_dealer[0])
    cartas_dealer.append(cima_dealer[0])
    print('Carta de cima do dealer:{}'.format(cima_dealer[0]))

           
            
    i=0
    while i<len(lista_jogadores):
        continuidade=str(input('{}, digite [1] para pedir mais cartas ou [2] para parar:'.format(lista_jogadores[i])))
    
        while continuidade=='1':
            carta_extra=saque(baralho)
            dic_valores[lista_jogadores[i]].append(valor(carta_extra)) 
            dic_cartas[lista_jogadores[i]].append(carta_extra[0])
            print('{}, sua nova mão: {}'.format(lista_jogadores[i],dic_cartas[lista_jogadores[i]]))
        
            if soma(dic_valores[lista_jogadores[i]])>21:
                print('{}, você ESTOUROU!'.format(lista_jogadores[i]))
                dic_carteira[lista_jogadores[i]]=dic_carteira[lista_jogadores[i]]- dic_apostas[lista_jogadores[i]]
                del(lista_jogadores[i])
                del(lista_carteira[i])
                i-=1
                break
            elif soma(dic_valores[lista_jogadores[i]])==21:
                print('BLACKJACK!.{}, você fez 21'.format(lista_jogadores[i]))
                dic_carteira[lista_jogadores[i]]=dic_carteira[lista_jogadores[i]]+ dic_apostas[lista_jogadores[i]]*1.5
                del(lista_jogadores[i])
                del(lista_carteira[i])
                i-=1
                break
            else:
                continuidade=str(input('{}, digite [1] para pedir mais cartas ou [2] para parar:'.format(lista_jogadores[i])))
        i+=1
            
    if len(lista_jogadores)>0:
        print('Mão do dealer era: {}'.format(cartas_dealer))
        while soma(valor_dealer)<17:
            carta_extra_dealer=saque(baralho)
            valor_dealer.append(valor(carta_extra_dealer))
            cartas_dealer.append(carta_extra_dealer[0])
        while soma(valor_dealer)<maior_soma(lista_jogadores,dic_valores):
            carta_extra_dealer2=saque(baralho)
            valor_dealer.append(valor(carta_extra_dealer2))
            cartas_dealer.append(carta_extra_dealer2[0])
        print('Após puxar cartas, a nova mão do dealer: {}. A soma do dealer foi {}'.format(cartas_dealer,soma(valor_dealer)))
    
        for e in lista_jogadores:
            if soma(valor_dealer)>21:
                print('{}, você GANHOU!'.format(e))
            elif soma(dic_valores[e])<soma(valor_dealer) and soma(valor_dealer)<=21:
                print('{}, você PERDEU!'.format(e))
                dic_carteira[e]=dic_carteira[e]- dic_apostas[e]
            elif soma(dic_valores[e])==soma(valor_dealer):
                print('{}, você EMPATOU!'.format(e))

    print('RESULTADOS')
    print('MÃOS DOS JOGADORES:{}'.format(dic_cartas))
    print('MÃO DO DEALER:{}'.format(cartas_dealer))
    print('CARTEIRAS:{}'.format(dic_carteira))
    
    
        #FEATURE LIVRE: SEGUNDA CHANCE!
    for e in lista_jogadores_definitiva:
        if dic_carteira[e]<=0:
            print('{}, acabou deu dinheiro! Algum jogador deseja dar dinheiro para {}?'.format(e,e))
            doar=str(input('Se sim DIGITE O NOME DO JOGADOR. Se não digite [nao]:'))
            if doar=='nao':
                print('{}, mais sorte na proxima'.format(e))            
                del(dic_carteira[lista_jogadores[e]])
                del(lista_carteira[e])
                del(lista_jogadores[e])
                del(lista_jogadores_definitiva[e])
            else:
                doacao=float(input('{}, quanto você deseja doar:'.format(doar)))
                dic_carteira[e]=doacao
                dic_carteira[doar]=dic_carteira[doar]-doacao
            print('CARTEIRAS:{}'.format(dic_carteira))
            
    print(lista_jogadores)
    print(lista_jogadores_definitiva)
    RESTAURAR=True
    
    continuar=str(input('Digite [1] para continuar a jogar e [2] para sair:'))
    if continuar=='2':
        JOGAR=False

print('Até a próxima!')
    

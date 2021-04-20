from random import randint
from time import sleep
j = cont = c = somajogador = somacomputador = rodada = 0
respostajogador = winner = ''
cstop = jstop = jogganha = False
print('VAMOS JOGAR 21!')
start = str(input('Aperte ENTER para começar '))
endgame = True
while endgame:
    if jstop == True and cstop == True:
        break
    rodada += 1
    # situação 1 deicação do jogador
    if rodada % 2 == 0:
        while True:
            if jstop == True:
                break
            elif rodada < 3:
                respostajogador = str(input('Você deseja VIRAR A PRIMEIRA CARTA AGORA ? [S/N] ')).upper().strip()[0]
            elif rodada > 2:
                respostajogador = str(input(f'\nO COMPUTADOR ESTÁ com {somacomputador} VOCÊ ESTÁ COM {somajogador}\n'
                                            f'Você deseja VIRAR OUTRA CARTA ? [S/N] ')).upper().strip()[0]
            if respostajogador in 'N':
                print(f'\nSua pontuação no jogo foi de {somajogador}\n')
                jstop = True
                if somajogador == 0:
                    endgame = False
                    winner = 'COMPUTADOR'
                if somacomputador > somajogador and somacomputador < 21:
                    endgame = False
                    winner = 'COMPUTADOR'
                break
            elif respostajogador in 'S':
                break
            else:
                print('Valor incorreto. Por favor inserir um valor valido.')
        if jstop == False:
            sleep(1)                                        # processamento da decisão positiva do jogador
            print('=-' * 10, 'Sua VEZ', '=-' * 10)
            sleep(1)
            print('... EMBARALHANDO ...')
            sleep(3)
            j = randint(1, 10)
            somajogador += j
            print('A carta virada tem valor de {}'.format(j))
            print('A soma acumulada é de {}.'.format(somajogador))
            if somajogador == 21:
                sleep(1)
                print('VOCÊ GANHOU')
                jstop = True
                winner = 'VOCÊ'
                endgame = False
            elif somajogador > 21:
                sleep(1.5)
                print('Você PERDEU')
                endgame = False
                winner = 'COMPUTADOR'
        elif jstop == True:
            sleep(0.5)
            print(f'\nJOGADOR DESISTIU COM PONTUAÇÃO DE {somajogador}\n')
# situação 2 processamento da jogada do computador
    if rodada % 2 > 0:
        if cstop == False:
            sleep(1)
            print('\n', '=-' * 5, 'VEZ DO COMPUTADOR', '=-' * 5)
            sleep(1)
            print('COMPUTADOR ESTÁ PENSANDO... ')
            sleep(2)
            print('COMPUTADOR PEDE PARA VIRAR UMA CARTA')
            print('... EMBARALHANDO ...')
            sleep(3)
            c = randint(1, 10)
            somacomputador += c
            print('A carta virada tem valor de {}'.format(c))
            print('A soma acumulada é de {}.'.format(somacomputador))
            if somacomputador == 21:
                sleep(1)
                print('COMPUTADOR ATINGIU A PONTUAÇÃO MÁXIMA')
                winner = 'COMPUTADOR'
                endgame = False
            if somacomputador > 21:
                sleep(1.5)
                print('COMPUTADOR PERDEU')
                winner = 'VOCÊ'
                endgame = False
            if 17 < somacomputador < 21:
                sleep(2)
                print('\nO COMPUTADOR ENCERROU\nA Pontuação do COMPUTADOR é de {}.'.format(somacomputador))
                cstop = True
        elif cstop == True:
            sleep(0.5)
            print(f'\nO COMPUTADOR DESISTIU COM PONTUAÇÃO DE {somacomputador}')
sleep(1)
print('ACABOU')
sleep(1.5)
if somacomputador > 21 and somajogador > 21:
    menor = 0
    if somacomputador < somajogador:
        menor = somacomputador
        winner = 'COMPUTADOR'
    else:
        menor = somajogador
        winner = 'VOCÊ'
elif somacomputador < 21 and somajogador < 21:
    maior = 0
    if somacomputador > somajogador:
        maior = somacomputador
        winner = 'COMPUTADOR'
    else:
        maior = somajogador
        winner = 'VOCÊ'
elif somacomputador == somajogador:
    winner = 'EMPATE'
    print('\n\nDEU EMPATE')
if winner == 'EMPATE':
    print('PARABÉNS\nPELO MENOS VOCÊ NÃO PERDEU!')
else:
    print('\nO Vencedor foi {} \n   PARABÉNS !!  '.format(winner))
    print('PONTUAÇÃO DO COMPUTADOR FOI {} e PONTUAÇÃO DO JOGADOR FOI {}'.format(somacomputador, somajogador))

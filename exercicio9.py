print('{:=^40}'.format('Your game'))

from random import randint

from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print(''' SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')

jogador = int(input('Qual é a sua jogada? '))

print('=+' * 11)

print('Computador escolheu: {}\n'.format(itens[computador]))

print('Jogador escolheu: {}'.format(itens[jogador]))

print('\nJO')

sleep(1)

print('KEN')

sleep(1)

print('PO!!!')

print('=+' * 11)

if computador == 0:# computador jogou PEDRA
    if jogador == 0:
        print('Jogo EMPATADO!')
    
    elif jogador == 1:
        print('Jogador VENCEU!')

    elif jogador == 2:
        print('Computador VENCEU!')

    else:
        print('Jogada INVÁLIDA!')

elif computador == 1:# computador jogou PAPEL
    if jogador == 0:
        print('Computador VENCEU!')
    
    elif jogador == 1:
        print('Jogo EMPATADO!')

    elif jogador == 2:
        print('Jogador VENCEU')

    else:
        print('Jogada INVÁLIDA!')

elif computador == 2:# computador jogou TESOURA
    if jogador == 0:
        print('Jogador VENCEU')

    elif jogador == 1:
        print('Computador VENCEU')

    elif jogador == 2:
        print('Jogo EMPATADO!')

    else:
        print('Jogada INVALIDA!')

print('{:=^40}'.format('End of the game'))
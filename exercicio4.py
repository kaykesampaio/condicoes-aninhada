# Alistamento militar
from datetime import date

atual = date.today().year

nasc = int(input('Ano de nascimento?: '))

idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado ha {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano)) 






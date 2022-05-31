# comprando uma casa!
    #crie um programa que pede o valor da casa do salário do sujeito, dos anos que ele quer pagar e se exeder 30% do salario mostrar  na tela que não da para ele financiar uma casa

print('_=_' * 26)

casa = float(input('Valor da casa: R$ '))

salario = float(input('Salário do comprador: R$ '))

anos = int(input('Anos de financiamento: '))

minimo= salario * 30/100

prestação = casa / (anos * 12)

print('\nPara pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}\n'.format(prestação))

if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO! ')
else:
    print('Empréstimo NEGADO!')


print('_=_' * 26)
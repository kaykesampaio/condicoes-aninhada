print('{:=^40}'.format(' LOJAS AZEVEDO '))

preço = float(input('Preço das compras: R$'))

print('''\nFORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\n''')

opção = int(input('Qual é a Opção?: '))

if opção == 1:
    total = preço -(preço * 10 / 100)

elif opção == 2:
    total = preço - (preço * 5 / 100)

elif opção == 3:
    total = preço
    parcela = total / 2
    print('\nSua compra será parecelada em 2x de R${:.2f}'.format(parcela))

elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?: '))
    parcela = total / totparc
    print('\nSua compra será parcelada em {}x de {:.2f} COM JUROS.'.format(totparc, parcela))

else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento, Tente Novamente!')

print('\nSua compra de R${:.2f} vai custar R${:.2f} no final.\n'.format(preço, total))


print('{:=^40}'.format(' Obrigado por Comprar '))



print('=--=' * 25)


peso = float(input('Qual é seu peso? (Kg): '))

altura = float(input('Qual é sua altuta? (m): '))

imc = peso / (altura**2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc), end='')

if imc < 18.5:
    print(' Você está abaixo do PESO Normal!')

elif imc >= 18.5 and imc < 25:# ou assim: 18.5 <= imc < 25:
    print(' Você esta no PESO Ideal!')

elif imc >= 25 and imc < 30:
    print(' Você está em Sobrepeso!')

elif imc >= 30 and imc < 40:
    print(' Você está em Obesidade')

elif imc >= 40:
    print(' Você está em Obesidade Mórbita, cuidado!')



print('=--=' * 25)
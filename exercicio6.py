print('+=+' * 25)

r1 = int(input('Primeiro segmento: '))

r2 = int(input('Segundo segmento: '))

r3 = int(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!', end='')
    if r1 == r2 and r2 == r3:
        print(' "Equilátero!"')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print(' "Escaleno!"')
    else:
        print(' "Isóceles!"')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

print('+=+' * 25)
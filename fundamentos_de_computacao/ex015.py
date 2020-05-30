decimal = int(input('Informe um numero inteiro decimal: '))
dig1 = int(0)
dig2 = int(0)
dig3 = int(0)


dig1 = (decimal%8)
aux = (decimal//8)
decimal = aux




dig2 = (decimal%8)
aux = (decimal//8)
dig3 = aux

print('{}{}{}'.format((dig3),(dig2),(dig1)))



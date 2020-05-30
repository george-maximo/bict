'''
    questão 5
'''

aux = int(0)
amostaR1 = int(0)
amostaR2 = int(0)
amostaR3 = int(0)

for r1 in range(1, 3):
    amostra = int(input('digite valor da amostra do r1'))
    aux = aux + amostra

mediaR1 = aux / 2
aux = 0

for r2 in range(1, 3):
    amostra = int(input('digite valor da amostra do r2'))
    aux = aux + amostra

mediaR2 = aux / 2
aux = 0

for r3 in range(1, 4):
    amostra = int(input('digite valor da amostra do r3'))
    aux = aux + amostra

mediaR3 = aux / 3

mediaTotal = (mediaR1 + mediaR2 + mediaR3) / 3
print('Media total', mediaTotal)

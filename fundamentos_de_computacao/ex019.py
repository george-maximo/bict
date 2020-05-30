produto1 = float(input('Informe o preco do produto1: '))
produto2 = float(input('Informe o preco do produto2: '))
produto3 = float(input('Informe o preco do produto3: '))

if((produto1 < produto2) and (produto1 < produto3)):
   menor = 'produto1'

elif((produto2 < produto1) and (produto2 < produto3)):
   menor = 'produto2'

elif((produto3 < produto1) and (produto3 < produto2)):
   menor = 'produto3'

print('Voce deve comprar o '+menor+' pois tem o preco mais barato de todos')
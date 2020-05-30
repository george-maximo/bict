gasolina = 2.50
alcool = 1.90

litros = float(input('Informe litros abastecidos: '))
cod = str(input('Informe o codigo do comustivel sendo A - alcool, G - gasolina: '))

if(litros <= 20):
    alcool = alcool - (alcool * 0.03)
    gasolina = gasolina - (gasolina * 0.04)

else:
    alcool = alcool - (alcool * 0.05)
    gasolina = gasolina - (gasolina * 0.06)

if(cod == 'A'):
    valor = litros * alcool
    print('Valor a pagar: R$',valor)

elif(cod == 'G'):
    valor = litros * gasolina
    print('Valor a pagar: R$',valor)

else:
    print('Codigo invalido')
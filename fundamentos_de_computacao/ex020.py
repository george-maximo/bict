print('Informe seu turno de estudo, obedecendo a legenda abaixo: ')
print('M-matutino V-vespertino N- noturno')
turno = str(input('turno = '))

if(turno == 'M'):
    print('Bom dia')

elif(turno == 'V'):
    print('Boa tarde')

elif(turno == 'N'):
    print('Boa noite')

else:
    print('Valor Invalido')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2)/2

if((media >= 9.0) and (media <= 10)):
    conceito = 'A'

elif((media >= 7.5) and (media < 9.0)):
    conceito = 'B'

elif((media >= 6.0) and (media < 7.5)):
    conceito = 'C'

elif((media >= 4.0) and (media < 6.0)):
    conceito = 'D'

elif(media < 4):
    conceito = 'E'

if((conceito == 'A') or (conceito == 'B') or (conceito == 'C')):
     print('Nota1: ',nota1)
     print('Nota2: ',nota2)
     print('Media: ',media)
     print('Conceito: ', conceito)
     print('Aprovado')

else:
     print('Nota1: ',nota1)
     print('Nota2: ',nota2)
     print('Media: ',media)
     print('Conceito: ', conceito)
     print('Reprovado')
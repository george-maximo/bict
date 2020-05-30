'''
    3)  Realiza saques com a menor quantidade de cédulas possíveis de um caixa eletrônico
que dispõem apenas de notas de 1, 10 e 100 reais.

'''
nota100 = 0
nota10 = 0
nota1 = 0

valor = int(input('Informe valor do saque: '))
if valor >= 100:
    nota100 = int(valor/100)
    if valor % 100 != 0:
        valor = valor % 100

if valor >=10 and valor < 100:
    nota10 = int(valor/10)
    if valor % 10 != 0:
        valor = valor % 10

if valor < 10:
    nota1 = valor

print(nota100,' notas de 100')
print(nota10, 'notas de 10')
print(nota1, 'notas de 1')

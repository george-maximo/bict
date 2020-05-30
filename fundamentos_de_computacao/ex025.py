valor = float(input('Informe o valor do saque ente 10 e 600: '))
notas100 = int(0)
notas50 = int(0)
notas10 = int(0)
notas5 = int(0)
notas1 = int(0)

if ((valor < 10) or (valor > 600)):
    print('Valor invalido')
else:

    if (valor >= 100):
        aux = valor // 100
        notas100 = int(aux)
        valor = valor - (aux * 100)

    if (valor >= 50):
        aux = valor // 50
        notas50 = int(aux)
        valor = valor - (aux * 50)

    if (valor >= 10):
        aux = valor // 10
        notas10 = int(aux)
        valor = valor - (aux * 10)

    if (valor >= 5):
        aux = valor // 5
        notas5 = int(aux)
        valor = valor - (aux * 5)

    if (valor >= 1):
        aux = valor // 1
        notas1 = int(aux)
        valor = valor - (aux * 1)

print('Você receberá: ')
print(notas100, 'notas de 100')
print(notas50, 'notas de 50')
print(notas10, 'notas de 10')
print(notas5, 'notas de 5')
print(notas1, 'notas de 1')
'''
    questão 3
'''

n = int(input('Informe a quantidade de numeros a ser processados: '))
maiorNum = int()
posicao = int()

for i in range(1, n + 1):
    num = int(input('Informe um numero '))
    if (i == 1):
        maiorNum = num
        posicao = i

    if (num > maiorNum):
        maiorNum = num
        posicao = i
print('O maior numero informado foi {}, e sua posicao é {}'.format(maiorNum, posicao))

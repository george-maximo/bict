'''
3. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
pares e a quantidade de números impares.
'''

lista = []
countPar = int(0)
countImpar = int(0)
for i in range(0,10):
    num = int(input('Informe um numero: '))
    lista.append(num)
    if(num%2==0):
        countPar +=1
    else:
        countImpar +=1
print('Quantidade de numeros pares: ',countPar)
print('Quantidade de numeros impares: ',countImpar)

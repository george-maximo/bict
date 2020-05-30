'''
2. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
intervalo compreendido por eles.

'''

num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
if (num1 < num2):
    for i in range(num1, num2 + 1):
        print(i)
elif(num1 > num2):
    for i in range(num1, num2 - 1, -1):
        print(i)
else:
    print('Voce informou dois numeros iguais, opção invalida ')


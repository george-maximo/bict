'''
4. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa
capaz de gerar a série até o n-ésimo termo.
'''

n = int(input('Informe a quantidade de termos da serie: '))
t1 = 0
t2 = 1
print('{} , {}'.format(t1,t2), end='')
cont = 3
while(cont <= n):
    t3 = t1 + t2

    print(' , {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

'''2. Dada uma lista L de números inteiros, escreva uma função que imprima todos os números de
índices múltiplos de 3.'''

l = [i for i in range(20)]

p=[]

def m3(lista):
    for i in lista:
        if(i % 3 == 0):
            p.append(i)
    return p

print(m3(l))

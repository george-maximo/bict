'''7. Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P com os
valores ordenados de P, agrupados em números pares primeiro e ímpares depois.'''

l = [1,0,5,4,3,2,6,7,8,9,10]

def ordena_lista(l):
    p=[]
    i=[]
    l_ordenada = sorted(l)
    for item in l_ordenada:
        if (item % 2 == 0):
            p.append(item)
        else:
            i.append(item)
    l = p + i
    return l

print(ordena_lista(l))

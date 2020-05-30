''' 1) Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P contendo os
números pares de L. Observação: utilize criação implícita de listas'''

l = [item for item in range(10)]
p=[]

def par(lista):
    for i in lista:
        if(i % 2 == 0):
            p.append(i)
    return p

print(l)

print(par(l))




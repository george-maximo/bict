'''4. Dada uma lista L de números inteiros, escreva uma função que imprima os itens de L de trás para
frente, sem utilizar reverse().'''

l = [item for item in range(10)]

p = []

def reverte(lista):
    t = len(lista) - 1
    while (t >= 0):
        p.append(lista[t])
        t = t - 1
    return p

print(l)
print(reverte(l))


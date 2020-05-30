'''3. Dada uma lista L de números inteiros, escreva uma função retorne uma lista P contendo todos os
itens de L acrescidos em 10%.'''

l = [item for item in range(10)]

p = []

def add10(lista):
    for i in lista:
        p.append(lista[i] + (lista[i]*0.10))
    return p
                 

print(add10(l))

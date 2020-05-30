'''5. Dada uma lista L de números inteiros, escreva uma função que retorne uma lista P contendo os
itens de L sem repetição.'''

l = [0,1,0,1,2,3]

def semRepetir(l1):
    l2=[]
    
    for i in range(len(l1)):
        n = l1.count(l1[i])
        if(n == 1):
            l2.append(l1[i])
    return l2


print(l)
print(semRepetir(l))


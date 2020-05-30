'''Dada uma lista L de números inteiros, escreva uma função que imprima os índices de todas as
ocorrências de um número especificado.'''

l = [0,1,0,1,2,3]
print('Lista = {}'.format(l))
num = int(input("Informe um numero da lista acima: "))

def indice(l,n):
    indices=[]
    for i in range(len(l)):
        if(n == l[i]):
            indices.append(i)
    if(len(indices) > 0):
        return indices
    else:
        erro = 'O numero informado não pertence a lista!'
        return erro
    
    
print(indice(l,num))

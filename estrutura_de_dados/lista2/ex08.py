'''Faça um programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20
elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras
listas.'''

a = [1,3,5,7,9,11,13,15,17,19]
b = [2,4,6,8,10,12,14,16,18,20]
c=[]
for i in range(10):
    c.append(a[i])
    c.append(b[i])

print(a)
print(b)
print(c)

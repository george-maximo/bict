'''
10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de
20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois
outros vetores. Calcule e mostre a soma dos quadrados dos elementos do terceiro vetor.
'''

v1 = [1,2,3,4,5,6,7,8,9,10]
v2 = [11,12,13,14,15,16,17,18,19,20]
v3 = []
soma = int(0)
for i in range(0,10):
    v3.append(v1[i])
    v3.append(v2[i])
print(v3)

for i in v3:
    quadrado = i*i
    soma = soma + quadrado
print(soma)

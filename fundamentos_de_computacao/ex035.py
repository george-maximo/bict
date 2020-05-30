'''
9. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene
os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use
um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os
lançamentos dos dados.
'''

from random import randint

dado = [0,0,0,0,0,0]

for i in range(0,100):
    a = randint(1,6)
    print(a)
    dado[(a-1)]+=1
for j in range(0,6):
    print(' Numero ',(j+1),' foi sorteado ',dado[j],' vezes')

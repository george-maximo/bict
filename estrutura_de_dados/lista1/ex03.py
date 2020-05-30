#Escreva um programa que escolha um numero aleatoriamente entre 0 e 10
#ao qual o usuario deve tentar advinhar, o Jogo acaba quando o usuário acerta 
#ou desiste digitando 0

from random import randint
num = (randint(1,10))
x = ''
while num != x:
  palpite = int(input('Digite seu palpite ou 0 para desistir '))
  if(palpite == 0):
    print('Boa sorte na proxima vez!!!')
    break
  elif(palpite == num):
    print('Parabens, você acertou!!!') 
    break
  x = palpite

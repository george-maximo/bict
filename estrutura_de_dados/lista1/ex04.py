#escreva um programa que mostre o seno e cosseno de
#0 a 360 de 10 em 10(utilize math.sin() e math.cos())

import math
i = 0
while(i <= 360):
  seno = math.sin(math.radians(i))
  cos = math.cos(math.radians(i))

  print('O seno de {} vale {:.2f}'.format(i, seno))
  print('O cosseno de {} vale {:.2f}'.format(i, cos))

  print(' ')

  i = i + 10

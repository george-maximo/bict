'''
   Implemente um programa em Python que recebe do usuário o placar de um jogo de
futebol (os gols de cada time) e informa se o resultado foi um empate, a vitória do primeiro
time ou do segundo time.
'''

gols_time1 = int(input("Informe o numero de gols do time1: "))
gols_time2 = int(input("Informe o numero de gols do time2: "))

if (gols_time1 == gols_time2):
    print("empate")

elif (gols_time1 > gols_time2):
    print("Vitoria do time1")

else:
    print("Vitoria do time2")
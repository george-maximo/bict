'''
    Construa um código em Python para converter um número inteiro decimal em base
binária desde que o número de bits na base não passe de 3, por exemplo, para a base
binária o máximo número convertido será (111)
'''

num = int(input("Informe um numero entre 0 e 7: "))

teste = (num%2)
if(teste == 1):
    resultado_posicao2 = str(1)
else:
    resultado_posicao2 = str(0)


proximo_dividendo = (num//2)
teste = (proximo_dividendo%2)
if(teste == 1):
    resultado_posicao1 = str(1)
else:
    resultado_posicao1 = str(0)



proximo_dividendo = (proximo_dividendo//2)
teste = (proximo_dividendo%2)
if(teste == 1):
    resultado_posicao0 = str(1)
else:
    resultado_posicao0 = str(0)


print(resultado_posicao0 + resultado_posicao1 + resultado_posicao2)

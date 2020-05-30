'''
    Escreva um código em Python que receba como entrada os coeficientes de uma equação
do segundo grau (a, b e c) e informa se o sistema tem raízes repetidas, diferentes ou
complexas. Adicionalmente, mostra as raízes.
'''

a=int(input("Informe o coeficiente a da equação do segundo grau: "))
b=int(input("Informe o coeficiente b da equação do segundo grau: "))
c=int(input("Informe o coeficiente c da equação do segundo grau: "))

delta = b**2 - (4*a*c)
print(delta)

if(delta == 0):
    print("delta = 0, logo a equacao possui duas raizes reais iguais")
    x = -b / (2*a)
    print("x1 = x2 = ",x)

elif(delta > 0):
    print("delta > 0, logo a equacao possui duas raizes reais diferentes")
    x1 = -b + (delta**0.5) / (2*a)
    x2 = -b - (delta**0.5) / (2*a)
    print("x1 = ",x1)
    print("x2 = ",x2)


else:
    print("delta < 0, logo a equacao possui raize complexa")
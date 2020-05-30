'''
    Escreva um programa em Python para determinar se um dado número (N) é POSITIVO,
NEGATIVO ou NULO.
'''

num = int(input("Informe um numero:" ))

if(num > 0):
    print("{} é POSITIVO".format(num))

elif(num < 0):
    print("{} é NEGATIVO".format(num))

else:
    print("{} é nulo".format(num))

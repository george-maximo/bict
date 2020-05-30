'''
    1) dados dois números, informe o maior
'''

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if (num1 == num2):
    print("{} é igual a {} ".format(num1, num2))

elif (num1 > num2):
    print("{} é maior que {} ".format(num1, num2))

elif (num1 < num2):
    print("{} é menor que {} ".format(num1, num2))

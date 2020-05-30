'''
    Implemente um programa em Python que dado três números (n1, n2 3 n3) informe se
existe um maior, assim como informa quem é o maior dos três números.
'''

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))

if((num1==num2) and (num2 == num3)):
    print("Não exite numero maior entre os numeros informados, todos são iguais a ",num1)

elif ((num1>=num2) and (num1>=num3)):
    maior = num1
    print("O maior numero informado foi ",maior)

elif((num2>=num1) and (num2>=num3)):
    maior = num2
    print("O maior numero informado foi ",maior)

elif ((num3>=num1) and (num3>=num2)):
    maior = num3
    print("O maior numero informado foi ",maior)
num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
num3 = int(input('Informe o terceiro numero: '))

if((num1 > num2) and (num1 > num3)):
   maior = num1

elif((num2 > num1) and (num2 > num3)):
   maior = num2

elif((num3 > num1) and (num3 > num2)):
   maior = num3

print('O maior numero informado foi: ',maior)
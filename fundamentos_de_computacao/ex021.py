salario = float(input('Informe o valor do salario atual: '))

if(salario <= 280.00):
    reajuste = 0.2
    salario_ajustado = (salario * reajuste) + salario

elif((salario > 280.00) and (salario <= 700.00)):
    reajuste = 0.15
    salario_ajustado = (salario * reajuste) + salario

elif((salario > 700.00) and (salario <= 1500.00)):
    reajuste = 0.1
    salario_ajustado = (salario * reajuste) + salario

elif(salario > 1500.00):
    reajuste = 0.05
    salario_ajustado = (salario * reajuste) + salario

print('O salario antes do reajuste: ',salario)
print('O percentual de aumento aplicado: ',reajuste*100,'%')
print('O valor do aumento: ',reajuste*salario)
print('O valor do novo salario: ',salario_ajustado)
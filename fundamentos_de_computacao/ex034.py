'''
8. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com
base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas
brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma
semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um
programa (usando um array de contadores) que determine quantos vendedores receberam
salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs
aninhados.
'''

vendendores = ['joao', 250.00, 'maria', 450.00, 'carlos', 3578.00, 'francisco',
436.00, 'chato', 15782.00, 'fabio', 875.00, 'raimundo', 987.00]
contadores = [[],[],[],[],[],[],[],[],[]]
tamanho = len(vendendores)
for i in range(0,tamanho):
    if (i % 2) != 0:
        if((vendendores[i] >= 200) and (vendendores[i]<=299)):
            contadores[0].append(vendendores[i-1])
        elif((vendendores[i] >= 300) and (vendendores[i]<=399)):
            contadores[1].append(vendendores[i-1])
        elif ((vendendores[i] >= 400) and (vendendores[i] <= 499)):
            contadores[2].append(vendendores[i - 1])
        elif ((vendendores[i] >= 500) and (vendendores[i] <= 599)):
            contadores[3].append(vendendores[i - 1])
        elif ((vendendores[i] >= 600) and (vendendores[i] <= 699)):
            contadores[4].append(vendendores[i - 1])
        elif ((vendendores[i] >= 700) and (vendendores[i] <= 799)):
            contadores[5].append(vendendores[i - 1])
        elif ((vendendores[i] >= 800) and (vendendores[i] <= 899)):
            contadores[6].append(vendendores[i - 1])
        elif ((vendendores[i] >= 900) and (vendendores[i] <= 999)):
            contadores[7].append(vendendores[i - 1])
        else:
            contadores[8].append(vendendores[i-1])
print('Vendedores com salario na faixa $200 - $299', contadores[0])
print('Vendedores com salario na faixa $300 - $399', contadores[1])
print('Vendedores com salario na faixa $400 - $499', contadores[2])
print('Vendedores com salario na faixa $500 - $599', contadores[3])
print('Vendedores com salario na faixa $600 - $699', contadores[4])
print('Vendedores com salario na faixa $700 - $799', contadores[5])
print('Vendedores com salario na faixa $800 - $899', contadores[6])
print('Vendedores com salario na faixa $900 - $999', contadores[7])
print('Vendedores com salario acima $1000', contadores[8])

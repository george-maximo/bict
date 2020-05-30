'''
5. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o
número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno
mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo,
junto com suas alturas.
'''

alunos=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
maior=[0,0]
menor=[0,0]
for i in range (0,10):
    alunos[i][0] = int(input('Informe o numero do aluno: '))
    alunos[i][1] = int(input('Informe a altura em centimetros do aluno: '))
    if(alunos[i][1] > maior[1]):
        maior[0] = alunos[i][0]
        maior[1] = alunos[i][1]
        menor[0] = maior[0]
        menor[1] = maior[1]
for j in range (0,10):
    if (alunos[j][1] < menor[1]):
        menor[0] = alunos[j][0]
        menor[1] = alunos[j][1]
print('O maior aluno é o de numero: {} e sua altura é:{}'.format(maior[0],maior[1]) )
print('O menor aluno é o de numero: {} e sua altura é:{}'.format(menor[0],menor[1]) )

'''
7. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será
digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
3
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7
Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''

tab = int(input('Informe a tabuada que deseja: '))
inicio = int(input('Informe inicio da tabuada: '))
fim = int(input('Informe fim da tabuada: '))
if(fim > inicio):
    for i in range(inicio,(fim+1)):
        print(tab,' x ',i,' = ', (tab*i))
else:
    print('Voce informou valores incorretos, fim deve ser maior que inicio')
    print('Tente outra vez')

'''
    questão 4
'''

menorNota = float()
media = float()
notaReposicao = float()

nota1 = float(input('Informe a primeira nota'))
nota2 = float(input('Informe a  segunda nota'))
nota3 = float(input('Informe a terceira nota'))

if ((nota1 < nota2) and (nota1 < nota3)):
    menorNota = nota1

elif ((nota2 < nota1) and (nota2 < nota3)):
    menorNota = nota2
elif ((nota3 < nota1) and (nota3 < nota2)):
    menorNota = nota3

media = (nota1 + nota2 + nota3) / 3
print('media', media)
if (media >= 7):
    print('O aluno foi aprovado')
else:
    print('O aluno fara reposicao da menor nota')
    notaReposicao = float(input('Informe a nota de reposicao'))

    if (nota1 == menorNota):
        nota1 = notaReposicao

    elif (nota2 == menorNota):
        nota2 = notaReposicao

    elif (nota3 == menorNota):
        nota3 = notaReposicao

    media = (nota1 + nota2 + nota3) / 3
    print('nova media', media)

    if (media >= 7):
        print('O aluno foi aprovado na reposicao')
    else:
        final = float(input('Informe a nota da prova final: '))
        if ((media + final) >= 12):
            print('O aluno foi aprovado na final')
        else:
            print('O aluno foi Reprovado')





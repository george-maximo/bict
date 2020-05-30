'''
6. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de
trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito (em 1999)
Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
2
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

'''

dados = [[1,1530,301],[2,3590,575],[3,16590,1799],[4,167798,15700],[5,18,1]]
auxMaior=int(0)
auxMenor=int(0)
maiorIndice=int(0)
menorIndice=int(0)
codMaior = int(0)
codMenor = int(0)
soma = int(0)
soma2 = int(0)
count = int(0)
for i in range(0,5):
    for j in range(2,3,3):
        if((dados[i][j]) > auxMaior):
            maiorIndice = dados[i][j]
            auxMaior = maiorIndice
            codMaior = dados[i][j-2]
            auxMenor = maiorIndice
for i in range(0,5):
    for j in range(2,3,3):
        if((dados[i][j]) < auxMenor):
            menorIndice = dados[i][j]
            auxMenor = menorIndice
            codMenor = dados[i][j-2]
for i in range(0,5):
    soma = dados[i][1] + soma
    if((dados[i][1]) < 2000):
        soma2 = dados[i][1] + soma2
    count = count + 1
    media = soma / 5
    media2 = soma2 / count
print('Maior indice de acidentes = ',maiorIndice,' ,ocorreu na cidade cod:',codMaior)
print('Menor indice de acidentes = ',menorIndice,' ,ocorreu na cidade cod:',codMenor)
print('A media total de veiculos nas cinco cidades: ',media)
print('A media de acidentes nas cidades com menos de 2000 veiculos: ',media2)

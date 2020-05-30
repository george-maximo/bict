nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
ultimoNome = separado[len(separado) - 1]

tamanhoNome = len(nome)
tamanhoUltimoNome = len(ultimoNome)
fimNome = tamanhoNome - tamanhoUltimoNome



print(ultimoNome,',',nome[0:fimNome])



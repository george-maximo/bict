contador = int(0)
palavra1 = str(input('Digite uma String: '))
espacos = palavra1.count(' ')
for c in palavra1:
    contador += 1
print(contador - espacos)


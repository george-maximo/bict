num = int(1)
den = int(1)
soma = int(1)

n=int(input('Informe a quantidade de somas'))

for i in range (1,n):
    num = num + 2
    den = den + 1
    soma = soma + (num/den)

print(soma)

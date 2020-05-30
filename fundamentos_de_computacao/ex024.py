a = float(input('Informe o tamanho do lado a: '))
b = float(input('Informe o tamanho do lado b: '))
c = float(input('Informe o tamanho do lado c: '))

if((a<(b+c)) and (b<(a+c)) and (c<(a+b))):
    print('Os valores informados podem formar um triangulo')

    if((a==b) and (b==c)):
        print('Triangulo Equilatero')

    elif((a==b) or (b==c) or (a==c)):
        print('Triangulo Isóceles')

    else:
        print('Triangulo Escaleno')
else:
    print('Os valores informados não formao um triangulo')
 
#Escreva um algoritmo que leia um valor e mostre o valor em dolar
cotacao = float(input(' Informe a cotação do Dolar '))
valor = float(input(" Informe a quantidade em reais "))

valorEmDolar = valor/cotacao
print("R${:.2f} é equivalente a US${:.2f} ".format(valor,valorEmDolar))

#Escreva um programa que imprima os números pares de 1 a quantidade que o usuário escolher.
qtd = int(input('escreva a quantidade :'))
for x in range(qtd +1 ):
   if x %2 == 0 :
       print(x)


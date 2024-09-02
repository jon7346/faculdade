#Escreva um programa que solicite ao usuário um intervalo de números e,
# em seguida,exiba todos os números pares e ímpares dentro desse intervalo.

qtd = int(input('escreva a quantidade :'))
for x in range(qtd +1 ):
   if x %2 == 1 :
       print(x)


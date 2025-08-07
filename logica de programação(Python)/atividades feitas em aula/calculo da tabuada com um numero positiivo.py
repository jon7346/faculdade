#Escreva um programa onde você fara a cálculos de multiplicação
# como os da tabuada somente quando o número é positivo e abaixo de 1000.

numero = int(input('escreva um numero: '))

if numero < 1000 and 0 > numero:
    for x in range(11):
        print(x)
else:
     print(" o numero não é positivo ou é maior ou igual a 1000")
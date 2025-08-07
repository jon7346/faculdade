#Contagem regressiva: Escreva um programa que solicite ao
#usuário um número e exiba uma contagem regressiva até zero.

t = int(input('tempo a ser contado:'))
y = 0

for i in range(-t,0):
    y = i * (-1)
    print(y)


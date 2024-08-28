'''

Escreva um programa que imprima os N primeiros termos da sequência de Fibonacci,
 onde N é fornecido pelo usuário.

'''

inicio = int(input('insira a o numero de repetição da sequência: '))
x = 0
y = 0
z = 1
for i in range(inicio +1):
    y = z + x
    z = z + y
    x = y + z
    print(x)
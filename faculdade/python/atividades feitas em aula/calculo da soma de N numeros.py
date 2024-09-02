# Escreva um programa que calcule a soma dos primeiros N números, onde N é fornecido pelo usuário.
qtd = int(input('escreva a quantidade de numeros a serem somados: '))
soma = 0

for x in range(qtd):
  soma = x + soma
  print(soma)

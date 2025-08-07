# Escreva um programa que solicite
# ao usuário um número inteiro e calcule seu fatorial.
qtd = int(input('digite um numero: '))
y = 1

for x in range(1, qtd + 1):
    y *= x

    print(y)



    # 5! = 1 * 2 * 3 * 4 * 5
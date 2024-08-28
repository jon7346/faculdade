#Escreva um programa que
#exiba o seguinte padrão de asteriscos baseado na quantidade de repetições incluída
#pelo usuário:
n = int(input('insira a quantidade'))
y = 0
for i in range(n):
    y = i*'*'
    print(y)


#Escreva um
#programa que solicite ao usuário um intervalo de números e calcule a soma de
#todos os números pares dentro desse intervalo.
qtd = int(input('insira o intervalo:'))
soma = 0
for i in range(qtd +1):
    if i%2==0:
        soma = soma + i


print(soma)
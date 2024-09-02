"""
Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
negativos e o percentual de valores negativos e positivos.
"""
quantidade_n = 0
soma = 0
quantidade_de_valores_positivos =  0
quantidade_de_valores_negativos = 0
media_aritiméitca = 0
percentual_posi = 0
percentual_neg = 0

final = int(input('insira o final do intervalo de numeros a serem analisados: '))
começo = int(input('insira onde começa o intervalo: '))

for i in range(começo,(final+1)):
    quantidade_n = quantidade_n +1
    soma = soma + i
    media_aritiméitca= soma/quantidade_n
    if i < 0 :
     quantidade_de_valores_negativos = quantidade_de_valores_negativos + 1
    elif i > 0 :
     quantidade_de_valores_positivos= quantidade_de_valores_positivos + 1

quantidade_n = quantidade_n - 1
percentual_neg = ( quantidade_de_valores_negativos/quantidade_n) * 100
percentual_posi = (quantidade_de_valores_positivos/quantidade_n) * 100

print('média aritimética: ', media_aritiméitca)
print('quantidade de valores positivos', quantidade_de_valores_positivos)
print('quantidade de valores negativos', quantidade_de_valores_negativos)
print('percentual de negativos ', percentual_neg,'%')
print('percentual de positivos ', percentual_posi,'%')
print(soma)
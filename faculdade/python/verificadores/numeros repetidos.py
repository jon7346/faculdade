#criando variaveis
primeironumero = float(input('Digite o primeiro numero: '))
segundonumero = float(input('Digite o segundo numero: '))
terceironumero = float(input('Digite o terceiro numero: '))

print(type(primeironumero))
print(type(segundonumero))
print(type(terceironumero))

if terceironumero == segundonumero == primeironumero:
    print("todos os numeros são repetidos")
else:
    if segundonumero == primeironumero:
        print('primeiro e segundo numero são repetidos ')

if terceironumero == primeironumero:
    print('terceiro e primeiro numero são repetidos')
else:
    if segundonumero == terceironumero:
        print('terceiro e segundo numero são repetidos')

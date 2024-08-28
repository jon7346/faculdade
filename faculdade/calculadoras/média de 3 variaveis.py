#criando três variaveis
primeiranota = int(input('Digite a primeira nota'))
segundanota = int(input('Digite a segunda nota: '))
terceiranota = int(input('Digite a terceira nota: '))
#definindo tipos das variaveis
print(type(primeiranota))
print(type(segundanota))
print(type(terceiranota))
#calculando a soma
soma = (primeiranota + segundanota + terceiranota)
#calculando a média
média = (soma/3)
#Exibindo a média
print(média)
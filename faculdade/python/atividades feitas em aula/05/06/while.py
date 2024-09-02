senha =  input(str('insira a senha: '))
contador = 0 
while senha != 'unifafibe123':
    print('senha incorreta')
    contador = contador + 1 
    senha = input(str('insira a senha: '))
    if contador == 2 :
        break
    if senha =='Unifafibe123':
        print('senha correta')
    else:
        print('o numero de tentativas esgotaram')